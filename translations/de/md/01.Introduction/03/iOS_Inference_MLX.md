<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-03-27T07:18:25+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference_MLX.md",
  "language_code": "de"
}
-->
# Ausführen von Phi-3 und Phi-4 auf iOS mit dem Apple MLX Framework

Dieses Tutorial zeigt, wie man eine iOS-Anwendung erstellt, die das Phi-3- oder Phi-4-Modell direkt auf dem Gerät mit dem Apple MLX Framework ausführt. [MLX](https://opensource.apple.com/projects/mlx/) ist Apples Machine-Learning-Framework, das für Apple-Silicon-Chips optimiert ist.

## Voraussetzungen

- macOS mit Xcode 16 (oder höher)
- iOS 18 (oder höher) Zielgerät mit mindestens 8GB (iPhone oder iPad, kompatibel mit den Anforderungen von Apple Intelligence, da diese den quantisierten Phi-Anforderungen ähnlich sind)
- Grundkenntnisse in Swift und SwiftUI

## Schritt 1: Neues iOS-Projekt erstellen

Beginnen Sie mit der Erstellung eines neuen iOS-Projekts in Xcode:

1. Starten Sie Xcode und wählen Sie „Create a new Xcode project“.
2. Wählen Sie „App“ als Vorlage.
3. Benennen Sie Ihr Projekt (z. B. „Phi3-iOS-App“) und wählen Sie SwiftUI als Benutzeroberfläche.
4. Wählen Sie einen Speicherort für Ihr Projekt.

## Schritt 2: Erforderliche Abhängigkeiten hinzufügen

Fügen Sie das [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) hinzu, das alle notwendigen Abhängigkeiten und Hilfsmittel zum Vorladen von Modellen und zur Durchführung von Inferenz enthält:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Das grundlegende [MLX Swift package](https://github.com/ml-explore/mlx-swift) reicht zwar für Kern-Tensor-Operationen und grundlegende ML-Funktionen aus, aber das MLX Examples-Paket bietet mehrere zusätzliche Komponenten, die speziell für die Arbeit mit Sprachmodellen entwickelt wurden und den Inferenzprozess vereinfachen:

- Modell-Ladehilfen, die das Herunterladen von Hugging Face übernehmen
- Tokenizer-Integration
- Inferenz-Hilfsmittel für Textgenerierung
- Vorgefertigte Modelldefinitionen

## Schritt 3: Berechtigungen konfigurieren

Damit unsere App Modelle herunterladen und ausreichend Speicher zuweisen kann, müssen wir bestimmte Berechtigungen hinzufügen. Erstellen Sie eine `.entitlements`-Datei für Ihre App mit folgendem Inhalt:

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

> **Hinweis:** Die Berechtigung `com.apple.developer.kernel.increased-memory-limit` ist wichtig, um größere Modelle auszuführen, da sie der App erlaubt, mehr Speicher anzufordern als normalerweise zulässig.

## Schritt 4: Chat-Nachrichtenmodell erstellen

Erstellen wir zunächst eine einfache Struktur, um unsere Chat-Nachrichten darzustellen:

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

## Schritt 5: ViewModel implementieren

Als Nächstes erstellen wir die `PhiViewModel`-Klasse, die das Laden von Modellen und die Inferenz übernimmt:

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

Das ViewModel demonstriert die wichtigsten Integrationspunkte von MLX:

- Festlegen von GPU-Cache-Grenzen mit `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`. Es verweist auf ein spezifisches, vorab konvertiertes MLX-Modell, das automatisch heruntergeladen wird:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Sie können Ihre eigenen Modellkonfigurationen erstellen, um auf jedes kompatible Modell auf Hugging Face zu verweisen. Um beispielsweise Phi-4 mini zu verwenden, könnten Sie Ihre eigene Konfiguration definieren:

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

> **Hinweis:** Die Unterstützung für Phi-4 wurde Ende Februar 2025 zum MLX Swift Examples Repository hinzugefügt (in [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Ab März 2025 enthält die neueste offizielle Version (2.21.2 von Dezember 2024) keine integrierte Unterstützung für Phi-4. Um Phi-4-Modelle zu verwenden, müssen Sie das Paket direkt vom Hauptzweig referenzieren:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Dies ermöglicht Ihnen Zugriff auf die neuesten Modellkonfigurationen, einschließlich Phi-4, bevor sie in einer offiziellen Version enthalten sind. Sie können diesen Ansatz verwenden, um verschiedene Versionen von Phi-Modellen oder sogar andere Modelle zu nutzen, die in das MLX-Format konvertiert wurden.

## Schritt 6: UI erstellen

Implementieren wir nun eine einfache Chat-Oberfläche, um mit unserem ViewModel zu interagieren:

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

Die Benutzeroberfläche besteht aus drei Hauptkomponenten, die zusammenarbeiten, um eine grundlegende Chat-Oberfläche zu erstellen. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` bietet einen einfachen animierten Indikator, der anzeigt, dass die KI gerade verarbeitet.

## Schritt 7: App erstellen und ausführen

Wir sind nun bereit, die Anwendung zu erstellen und auszuführen.

> **Wichtig!** MLX unterstützt den Simulator nicht. Sie müssen die App auf einem physischen Gerät mit einem Apple-Silicon-Chip ausführen. Weitere Informationen finden Sie [hier](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Wenn die App startet, tippen Sie auf die Schaltfläche „Load model“, um das Phi-3- (oder, je nach Konfiguration, Phi-4-) Modell herunterzuladen und zu initialisieren. Dieser Vorgang kann je nach Internetverbindung einige Zeit dauern, da das Modell von Hugging Face heruntergeladen wird. Unsere Implementierung enthält lediglich einen Spinner, um das Laden anzuzeigen, aber Sie können den tatsächlichen Fortschritt in der Xcode-Konsole sehen.

Sobald das Modell geladen ist, können Sie mit ihm interagieren, indem Sie Fragen in das Textfeld eingeben und auf die Senden-Schaltfläche tippen.

So sollte unsere Anwendung aussehen, ausgeführt auf einem iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Fazit

Das war's! Durch das Befolgen dieser Schritte haben Sie eine iOS-Anwendung erstellt, die das Phi-3- (oder Phi-4-) Modell direkt auf dem Gerät mit Apples MLX Framework ausführt.

Herzlichen Glückwunsch!

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.