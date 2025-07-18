<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:30:51+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "pt"
}
-->
# Executar Phi-3 e Phi-4 no iOS com o Apple MLX Framework

Este tutorial demonstra como criar uma aplicação iOS que execute o modelo Phi-3 ou Phi-4 localmente, utilizando o framework Apple MLX. O [MLX](https://opensource.apple.com/projects/mlx/) é o framework de machine learning da Apple otimizado para chips Apple Silicon.

## Pré-requisitos

- macOS com Xcode 16 (ou superior)
- Dispositivo iOS 18 (ou superior) com pelo menos 8GB (iPhone ou iPad compatível com os requisitos de Apple Intelligence, que são semelhantes aos requisitos quantizados do Phi)
- conhecimentos básicos de Swift e SwiftUI

## Passo 1: Criar um Novo Projeto iOS

Comece por criar um novo projeto iOS no Xcode:

1. abra o Xcode e selecione "Create a new Xcode project"
2. escolha "App" como template
3. dê um nome ao seu projeto (ex.: "Phi3-iOS-App") e selecione SwiftUI como interface
4. escolha uma localização para guardar o seu projeto

## Passo 2: Adicionar as Dependências Necessárias

Adicione o pacote [MLX Examples](https://github.com/ml-explore/mlx-swift-examples) que contém todas as dependências e utilitários necessários para pré-carregar modelos e realizar inferência:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Embora o pacote base [MLX Swift](https://github.com/ml-explore/mlx-swift) seja suficiente para operações tensorais básicas e funcionalidades de ML, o pacote MLX Examples oferece vários componentes adicionais pensados para trabalhar com modelos de linguagem e facilitar o processo de inferência:

- utilitários para carregar modelos que tratam do download a partir do Hugging Face
- integração do tokenizer
- helpers para geração de texto durante a inferência
- definições de modelos pré-configuradas

## Passo 3: Configurar os Entitlements

Para permitir que a nossa app faça download de modelos e aloque memória suficiente, precisamos adicionar entitlements específicos. Crie um ficheiro `.entitlements` para a sua app com o seguinte conteúdo:

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

> **Note:** O entitlement `com.apple.developer.kernel.increased-memory-limit` é importante para correr modelos maiores, pois permite que a app solicite mais memória do que o habitual.

## Passo 4: Criar o Modelo de Mensagem de Chat

Primeiro, vamos criar uma estrutura básica para representar as mensagens do chat:

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

## Passo 5: Implementar o ViewModel

De seguida, vamos criar a classe `PhiViewModel` que trata do carregamento do modelo e da inferência:

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

O ViewModel demonstra os principais pontos de integração com o MLX:

- definir limites de cache da GPU com `MLX.GPU.set(cacheLimit:)` para otimizar o uso de memória em dispositivos móveis
- usar `LLMModelFactory` para descarregar o modelo sob demanda e inicializar o modelo otimizado para MLX
- aceder aos parâmetros e estrutura do modelo através do `ModelContainer`
- aproveitar a geração token a token do MLX com o método `MLXLMCommon.generate`
- gerir o processo de inferência com definições adequadas de temperatura e limites de tokens

A geração de tokens em streaming oferece feedback imediato ao utilizador enquanto o modelo gera texto. Isto é semelhante ao funcionamento dos modelos baseados em servidor, que enviam os tokens em tempo real, mas sem a latência das chamadas de rede.

Em termos de interação na UI, as duas funções principais são `loadModel()`, que inicializa o LLM, e `fetchAIResponse()`, que processa a entrada do utilizador e gera respostas da IA.

### Considerações sobre o formato do modelo

> **Important:** Os modelos Phi para MLX não podem ser usados no seu formato padrão ou GGUF. Devem ser convertidos para o formato MLX, processo gerido pela comunidade MLX. Pode encontrar modelos pré-convertidos em [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

O pacote MLX Examples inclui registos pré-configurados para vários modelos, incluindo o Phi-3. Quando chama `ModelRegistry.phi3_5_4bit`, está a referenciar um modelo MLX pré-convertido específico que será descarregado automaticamente:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Pode criar as suas próprias configurações de modelo para apontar para qualquer modelo compatível no Hugging Face. Por exemplo, para usar o Phi-4 mini, pode definir a sua própria configuração:

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

> **Note:** O suporte ao Phi-4 foi adicionado ao repositório MLX Swift Examples no final de fevereiro de 2025 (em [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Em março de 2025, a versão oficial mais recente (2.21.2 de dezembro de 2024) não inclui suporte nativo ao Phi-4. Para usar modelos Phi-4, terá de referenciar o pacote diretamente a partir da branch main:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Isto dá-lhe acesso às configurações mais recentes dos modelos, incluindo o Phi-4, antes de serem incluídas numa versão oficial. Pode usar este método para utilizar diferentes versões dos modelos Phi ou até outros modelos convertidos para o formato MLX.

## Passo 6: Criar a UI

Vamos agora implementar uma interface de chat simples para interagir com o nosso view model:

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

A UI é composta por três componentes principais que trabalham em conjunto para criar uma interface básica de chat. O `ContentView` cria uma interface com dois estados que mostra um botão de carregamento ou a interface de chat, dependendo da disponibilidade do modelo. O `MessageView` apresenta as mensagens do chat de forma diferente, consoante sejam mensagens do utilizador (alinhadas à direita, fundo azul) ou respostas do modelo Phi (alinhadas à esquerda, fundo cinzento). O `TypingIndicatorView` fornece um indicador animado simples para mostrar que a IA está a processar.

## Passo 7: Construir e Executar a App

Estamos agora prontos para construir e executar a aplicação.

> **Important!** O MLX não suporta o simulador. Deve executar a app num dispositivo físico com chip Apple Silicon. Veja [aqui](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) para mais informações.

Quando a app arrancar, toque no botão "Load model" para descarregar e inicializar o modelo Phi-3 (ou, dependendo da sua configuração, Phi-4). Este processo pode demorar algum tempo, dependendo da sua ligação à internet, pois envolve o download do modelo a partir do Hugging Face. A nossa implementação inclui apenas um spinner para indicar o carregamento, mas pode ver o progresso real no console do Xcode.

Depois de carregado, pode interagir com o modelo escrevendo perguntas no campo de texto e tocando no botão de enviar.

Aqui está como a nossa aplicação deve funcionar, a correr num iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Conclusão

E é tudo! Seguindo estes passos, criou uma aplicação iOS que executa o modelo Phi-3 (ou Phi-4) diretamente no dispositivo usando o framework MLX da Apple.

Parabéns!

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.