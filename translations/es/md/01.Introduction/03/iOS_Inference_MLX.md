<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-03-27T07:17:24+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference_MLX.md",
  "language_code": "es"
}
-->
# Ejecutar Phi-3 y Phi-4 en iOS con el Framework Apple MLX

Este tutorial muestra cómo crear una aplicación iOS que ejecute el modelo Phi-3 o Phi-4 en el dispositivo, utilizando el framework Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) es el framework de aprendizaje automático de Apple optimizado para los chips Apple Silicon.

## Requisitos previos

- macOS con Xcode 16 (o superior)
- Dispositivo objetivo iOS 18 (o superior) con al menos 8GB (iPhone o iPad compatible con los requisitos de Apple Intelligence, ya que serían similares a los requisitos de Phi cuantificado)
- Conocimientos básicos de Swift y SwiftUI

## Paso 1: Crear un nuevo proyecto iOS

Comienza creando un nuevo proyecto iOS en Xcode:

1. abre Xcode y selecciona "Crear un nuevo proyecto Xcode"
2. elige "App" como plantilla
3. nombra tu proyecto (por ejemplo, "Phi3-iOS-App") y selecciona SwiftUI como interfaz
4. elige una ubicación para guardar tu proyecto

## Paso 2: Agregar las dependencias necesarias

Agrega el paquete [MLX Examples](https://github.com/ml-explore/mlx-swift-examples), que contiene todas las dependencias y herramientas necesarias para precargar modelos y realizar inferencias:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Aunque el paquete base [MLX Swift](https://github.com/ml-explore/mlx-swift) sería suficiente para operaciones tensoriales básicas y funcionalidad de aprendizaje automático, el paquete MLX Examples ofrece varios componentes adicionales diseñados para trabajar con modelos de lenguaje y facilitar el proceso de inferencia:

- Utilidades de carga de modelos que gestionan la descarga desde Hugging Face
- Integración de tokenizadores
- Herramientas de inferencia para generación de texto
- Definiciones de modelos preconfiguradas

## Paso 3: Configurar los permisos

Para permitir que nuestra aplicación descargue modelos y asigne suficiente memoria, necesitamos agregar permisos específicos. Crea un archivo `.entitlements` para tu aplicación con el siguiente contenido:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.files.user-selected.read-only</key>
    <true/>
    <key>com.apple.security.network.client</key>
    <true/>
    <key>com.apple.developer.kernel.increased-memory-limit</key>
    <true/>
</dict>
</plist>
```

> **Nota:** El permiso `com.apple.developer.kernel.increased-memory-limit` es importante para ejecutar modelos más grandes, ya que permite que la aplicación solicite más memoria de la que normalmente se permite.

## Paso 4: Crear el modelo de mensaje del chat

Primero, vamos a crear una estructura básica para representar nuestros mensajes de chat:

```swift
import SwiftUI

enum MessageState {
    case ok
    case waiting
}

struct ChatMessage: Identifiable {
    let id = UUID()
    let text: String
    let isUser: Bool
    let state: MessageState
}
```

## Paso 5: Implementar el ViewModel

A continuación, crearemos la clase `PhiViewModel` que se encargará de la carga del modelo y la inferencia:

```swift
import MLX
import MLXLLM
import MLXLMCommon
import SwiftUI

@MainActor
class PhiViewModel: ObservableObject {
    @Published var isLoading: Bool = false
    @Published var isLoadingEngine: Bool = false
    @Published var messages: [ChatMessage] = []
    @Published var prompt: String = ""
    @Published var isReady: Bool = false
    
    private let maxTokens = 1024
    
    private var modelContainer: ModelContainer?
    
    func loadModel() async {
        DispatchQueue.main.async {
            self.isLoadingEngine = true
        }
        
        do {
            MLX.GPU.set(cacheLimit: 20 * 1024 * 1024)
            
            // Phi 3.5 mini is preconfigured in Swift MLX Examples
            let modelConfig = ModelRegistry.phi3_5_4bit
            
            // Phi 4 mini can be pulled from Hugging Face, but requires referencing Swift MLX Examples from the main branch
            //let modelConfig = ModelConfiguration(
            //    id: "mlx-community/Phi-4-mini-instruct-4bit",
            //    defaultPrompt: "You are a helpful assistant.",
            //    extraEOSTokens: ["<|end|>"]
            //)
            
            print("Loading \(modelConfig.name)...")
            self.modelContainer = try await LLMModelFactory.shared.loadContainer(
                configuration: modelConfig
            ) { progress in
                print("Download progress: \(Int(progress.fractionCompleted * 100))%")
            }
            
            // Log model parameters
            if let container = self.modelContainer {
                let numParams = await container.perform { context in
                    context.model.numParameters()
                }
                print("Model loaded. Parameters: \(numParams / (1024*1024))M")
            }
            
            DispatchQueue.main.async {
                self.isLoadingEngine = false
                self.isReady = true
            }
        } catch {
            print("Failed to load model: \(error)")
            
            DispatchQueue.main.async {
                self.isLoadingEngine = false
            }
        }
    }
    
    func fetchAIResponse() async {
        guard !isLoading, let container = self.modelContainer else {
            print("Cannot generate: model not loaded or already processing")
            return
        }
        
        let userQuestion = prompt
        let currentMessages = self.messages
        
        DispatchQueue.main.async {
            self.isLoading = true
            self.prompt = ""
            self.messages.append(ChatMessage(text: userQuestion, isUser: true, state: .ok))
            self.messages.append(ChatMessage(text: "", isUser: false, state: .waiting))
        }
        
        do {
            let _ = try await container.perform { context in
                var messageHistory: [[String: String]] = [
                    ["role": "system", "content": "You are a helpful assistant."]
                ]
                
                for message in currentMessages {
                    let role = message.isUser ? "user" : "assistant"
                    messageHistory.append(["role": role, "content": message.text])
                }
                
                messageHistory.append(["role": "user", "content": userQuestion])
                
                let input = try await context.processor.prepare(
                    input: .init(messages: messageHistory))
                let startTime = Date()
                
                let result = try MLXLMCommon.generate(
                    input: input,
                    parameters: GenerateParameters(temperature: 0.6),
                    context: context
                ) { tokens in
                    let output = context.tokenizer.decode(tokens: tokens)
                    Task { @MainActor in
                        if let index = self.messages.lastIndex(where: { !$0.isUser }) {
                            self.messages[index] = ChatMessage(
                                text: output,
                                isUser: false,
                                state: .ok
                            )
                        }
                    }
                    
                    if tokens.count >= self.maxTokens {
                        return .stop
                    } else {
                        return .more
                    }
                }
                
                let finalOutput = context.tokenizer.decode(tokens: result.tokens)
                Task { @MainActor in
                    if let index = self.messages.lastIndex(where: { !$0.isUser }) {
                        self.messages[index] = ChatMessage(
                            text: finalOutput,
                            isUser: false,
                            state: .ok
                        )
                    }
                    
                    self.isLoading = false
                    
                    print("Inference complete:")
                    print("Tokens: \(result.tokens.count)")
                    print("Tokens/second: \(result.tokensPerSecond)")
                    print("Time: \(Date().timeIntervalSince(startTime))s")
                }
                
                return result
            }
        } catch {
            print("Inference error: \(error)")
            
            DispatchQueue.main.async {
                if let index = self.messages.lastIndex(where: { !$0.isUser }) {
                    self.messages[index] = ChatMessage(
                        text: "Sorry, an error occurred: \(error.localizedDescription)",
                        isUser: false,
                        state: .ok
                    )
                }
                self.isLoading = false
            }
        }
    }
}

```

El ViewModel demuestra los puntos clave de integración con MLX:

- establecer límites de caché de GPU con `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, hace referencia a un modelo MLX específico preconvertido que se descargará automáticamente:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Puedes crear tus propias configuraciones de modelo para apuntar a cualquier modelo compatible en Hugging Face. Por ejemplo, para usar Phi-4 mini, podrías definir tu propia configuración:

```swift
let phi4_mini_4bit = ModelConfiguration(
    id: "mlx-community/Phi-4-mini-instruct-4bit",
    defaultPrompt: "Explain quantum computing in simple terms.",
    extraEOSTokens: ["<|end|>"]
)

// Then use this configuration when loading the model
self.modelContainer = try await LLMModelFactory.shared.loadContainer(
    configuration: phi4_mini_4bit
) { progress in
    print("Download progress: \(Int(progress.fractionCompleted * 100))%")
}
```

> **Nota:** El soporte para Phi-4 se agregó al repositorio MLX Swift Examples a finales de febrero de 2025 (en [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). A partir de marzo de 2025, la última versión oficial (2.21.2 de diciembre de 2024) no incluye soporte integrado para Phi-4. Para usar modelos Phi-4, deberás referenciar el paquete directamente desde la rama principal:
>
> ```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Esto te da acceso a las configuraciones de modelo más recientes, incluido Phi-4, antes de que se incluyan en una versión oficial. Puedes usar este enfoque para utilizar diferentes versiones de modelos Phi o incluso otros modelos que hayan sido convertidos al formato MLX.

## Paso 6: Crear la interfaz de usuario

Ahora implementemos una interfaz de chat sencilla para interactuar con nuestro ViewModel:

```swift
import SwiftUI

struct ContentView: View {
    @ObservedObject var viewModel = PhiViewModel()

    var body: some View {
        NavigationStack {
            if !viewModel.isReady {
                Spacer()
                if viewModel.isLoadingEngine {
                    ProgressView()
                } else {
                    Button("Load model") {
                        Task {
                            await viewModel.loadModel()
                        }
                    }
                }
                Spacer()
            } else {
                VStack(spacing: 0) {
                    ScrollViewReader { proxy in
                        ScrollView {
                            VStack(alignment: .leading, spacing: 8) {
                                ForEach(viewModel.messages) { message in
                                    MessageView(message: message).padding(.bottom)
                                }
                            }
                            .id("wrapper").padding()
                            .padding()
                        }
                        .onChange(of: viewModel.messages.last?.id, perform: { value in
                            if viewModel.isLoading {
                                proxy.scrollTo("wrapper", anchor: .bottom)
                            } else if let lastMessage = viewModel.messages.last {
                                proxy.scrollTo(lastMessage.id, anchor: .bottom)
                            }
                            
                        })
                    }
                    
                    HStack {
                        TextField("Type a question...", text: $viewModel.prompt, onCommit: {
                            Task {
                                await viewModel.fetchAIResponse()
                            }
                        })
                        .padding(10)
                        .background(Color.gray.opacity(0.2))
                        .cornerRadius(20)
                        .padding(.horizontal)
                        
                        Button(action: {
                            Task {
                                await viewModel.fetchAIResponse()
                            }
                        }) {
                            Image(systemName: "paperplane.fill")
                                .font(.system(size: 24))
                                .foregroundColor(.blue)
                        }
                        .padding(.trailing)
                    }
                    .padding(.bottom)
                }
            }
        }.navigationTitle("Phi Sample")
    }
}

struct MessageView: View {
    let message: ChatMessage

    var body: some View {
        HStack {
            if message.isUser {
                Spacer()
                Text(message.text)
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            } else {
                if message.state == .waiting {
                    TypingIndicatorView()
                } else {
                    VStack {
                        Text(message.text)
                            .padding()
                    }
                    .background(Color.gray.opacity(0.1))
                    .cornerRadius(10)
                    Spacer()
                }
            }
        }
        .padding(.horizontal)
    }
}

struct TypingIndicatorView: View {
    @State private var shouldAnimate = false

    var body: some View {
        HStack {
            ForEach(0..<3) { index in
                Circle()
                    .frame(width: 10, height: 10)
                    .foregroundColor(.gray)
                    .offset(y: shouldAnimate ? -5 : 0)
                    .animation(
                        Animation.easeInOut(duration: 0.5)
                            .repeatForever()
                            .delay(Double(index) * 0.2)
                    )
            }
        }
        .onAppear { shouldAnimate = true }
        .onDisappear { shouldAnimate = false }
    }
}

```

La interfaz de usuario consta de tres componentes principales que trabajan juntos para crear una interfaz de chat básica. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` proporciona un indicador animado simple para mostrar que la IA está procesando.

## Paso 7: Compilar y ejecutar la aplicación

Ahora estamos listos para compilar y ejecutar la aplicación.

> **¡Importante!** MLX no es compatible con el simulador. Debes ejecutar la aplicación en un dispositivo físico con un chip Apple Silicon. Consulta [aquí](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) para más información.

Cuando la aplicación se inicie, toca el botón "Cargar modelo" para descargar e inicializar el modelo Phi-3 (o, dependiendo de tu configuración, Phi-4). Este proceso puede tomar algún tiempo dependiendo de tu conexión a internet, ya que implica descargar el modelo desde Hugging Face. Nuestra implementación incluye solo un indicador de carga, pero puedes ver el progreso real en la consola de Xcode.

Una vez cargado, puedes interactuar con el modelo escribiendo preguntas en el campo de texto y tocando el botón de enviar.

Así es como debería comportarse nuestra aplicación, ejecutándose en un iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Conclusión

¡Y eso es todo! Siguiendo estos pasos, has creado una aplicación iOS que ejecuta el modelo Phi-3 (o Phi-4) directamente en el dispositivo utilizando el framework MLX de Apple.

¡Felicidades!

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No somos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.