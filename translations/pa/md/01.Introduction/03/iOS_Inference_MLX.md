<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:10:19+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "pa"
}
-->
# iOS 'ਤੇ Apple MLX Framework ਨਾਲ Phi-3 ਅਤੇ Phi-4 ਚਲਾਉਣਾ

ਇਹ ਟਿਊਟੋਰਿਯਲ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਵੇਂ ਇੱਕ iOS ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈ ਜਾ ਸਕਦੀ ਹੈ ਜੋ ਡਿਵਾਈਸ 'ਤੇ Phi-3 ਜਾਂ Phi-4 ਮਾਡਲ ਚਲਾਉਂਦੀ ਹੈ, Apple MLX ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ। [MLX](https://opensource.apple.com/projects/mlx/) Apple ਦਾ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਫਰੇਮਵਰਕ ਹੈ ਜੋ Apple Silicon ਚਿਪਸ ਲਈ ਅਪਟੀਮਾਈਜ਼ਡ ਹੈ।

## ਲੋੜੀਂਦੇ ਸਾਧਨ

- macOS ਅਤੇ Xcode 16 (ਜਾਂ ਇਸ ਤੋਂ ਵੱਧ)
- iOS 18 (ਜਾਂ ਇਸ ਤੋਂ ਵੱਧ) ਵਾਲਾ ਟਾਰਗੇਟ ਡਿਵਾਈਸ, ਘੱਟੋ-ਘੱਟ 8GB ਰੈਮ (ਉਹ iPhone ਜਾਂ iPad ਜੋ Apple Intelligence ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਦਾ ਹੈ, ਕਿਉਂਕਿ ਇਹ Phi ਦੇ ਕਵਾਂਟਾਈਜ਼ਡ ਵਰਜਨ ਵਰਗੇ ਹੀ ਹਨ)
- Swift ਅਤੇ SwiftUI ਬਾਰੇ ਬੁਨਿਆਦੀ ਜਾਣਕਾਰੀ

## ਕਦਮ 1: ਨਵਾਂ iOS ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

Xcode ਵਿੱਚ ਨਵਾਂ iOS ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣਾ ਸ਼ੁਰੂ ਕਰੋ:

1. Xcode ਖੋਲ੍ਹੋ ਅਤੇ "Create a new Xcode project" ਚੁਣੋ
2. "App" ਟੈਮਪਲੇਟ ਚੁਣੋ
3. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦਾ ਨਾਮ ਰੱਖੋ (ਜਿਵੇਂ "Phi3-iOS-App") ਅਤੇ ਇੰਟਰਫੇਸ ਲਈ SwiftUI ਚੁਣੋ
4. ਪ੍ਰੋਜੈਕਟ ਸੇਵ ਕਰਨ ਲਈ ਥਾਂ ਚੁਣੋ

## ਕਦਮ 2: ਜ਼ਰੂਰੀ Dependencies ਸ਼ਾਮਲ ਕਰੋ

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ਸ਼ਾਮਲ ਕਰੋ, ਜਿਸ ਵਿੱਚ ਸਾਰੇ ਲੋੜੀਂਦੇ ਡੀਪੈਂਡੇਨਸੀਜ਼ ਅਤੇ ਮਾਡਲ ਪ੍ਰੀਲੋਡ ਕਰਨ ਅਤੇ ਇੰਫਰੈਂਸ ਕਰਨ ਲਈ ਸਹਾਇਕ ਹਨ:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

ਜਦਕਿ ਬੇਸ [MLX Swift package](https://github.com/ml-explore/mlx-swift) ਮੁੱਖ ਟੈਂਸਰ ਓਪਰੇਸ਼ਨ ਅਤੇ ਬੁਨਿਆਦੀ ML ਫੰਕਸ਼ਨਲਿਟੀ ਲਈ ਕਾਫ਼ੀ ਹੈ, MLX Examples package ਵਿੱਚ ਕਈ ਹੋਰ ਕੰਪੋਨੈਂਟ ਹਨ ਜੋ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਅਤੇ ਇੰਫਰੈਂਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦੇ ਹਨ:

- Hugging Face ਤੋਂ ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਨ ਵਾਲੇ ਯੂਟਿਲਿਟੀਜ਼
- ਟੋਕਨਾਈਜ਼ਰ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
- ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਲਈ ਇੰਫਰੈਂਸ ਸਹਾਇਕ
- ਪਹਿਲਾਂ ਤੋਂ ਕਨਫਿਗਰ ਕੀਤੇ ਮਾਡਲ ਡਿਫੀਨੀਸ਼ਨ

## ਕਦਮ 3: Entitlements ਕਨਫਿਗਰ ਕਰੋ

ਸਾਡੇ ਐਪ ਨੂੰ ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਨ ਅਤੇ ਕਾਫ਼ੀ ਮੈਮੋਰੀ ਐਲੋਕੇਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦੇਣ ਲਈ, ਸਾਨੂੰ ਖਾਸ entitlements ਸ਼ਾਮਲ ਕਰਨੇ ਪੈਣਗੇ। ਆਪਣੇ ਐਪ ਲਈ `.entitlements` ਫਾਇਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਹੋਵੇ:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement ਵੱਡੇ ਮਾਡਲ ਚਲਾਉਣ ਲਈ ਜਰੂਰੀ ਹੈ, ਕਿਉਂਕਿ ਇਹ ਐਪ ਨੂੰ ਆਮ ਤੌਰ 'ਤੇ ਦਿੱਤੀ ਜਾਂਦੀ ਮੈਮੋਰੀ ਤੋਂ ਵੱਧ ਮੰਗਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

## ਕਦਮ 4: Chat Message ਮਾਡਲ ਬਣਾਓ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਚੈਟ ਮੈਸੇਜ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਇੱਕ ਬੁਨਿਆਦੀ ਸਟ੍ਰਕਚਰ ਬਣਾਈਏ:

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

## ਕਦਮ 5: ViewModel ਲਾਗੂ ਕਰੋ

ਹੁਣ, ਅਸੀਂ `PhiViewModel` ਕਲਾਸ ਬਣਾਵਾਂਗੇ ਜੋ ਮਾਡਲ ਲੋਡਿੰਗ ਅਤੇ ਇੰਫਰੈਂਸ ਸੰਭਾਲਦੀ ਹੈ:

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

ViewModel ਵਿੱਚ ਮੁੱਖ MLX ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੇ ਪੌਇੰਟ ਹਨ:

- GPU ਕੈਸ਼ ਲਿਮਿਟ ਸੈੱਟ ਕਰਨਾ `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit` ਨਾਲ, ਜੋ ਇੱਕ ਖਾਸ ਪ੍ਰੀ-ਕਨਵਰਟ ਕੀਤੇ MLX ਮਾਡਲ ਨੂੰ ਰੇਫਰੈਂਸ ਕਰਦਾ ਹੈ ਜੋ ਆਪਣੇ ਆਪ ਡਾਊਨਲੋਡ ਹੋ ਜਾਵੇਗਾ:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

ਤੁਸੀਂ ਆਪਣੇ ਮਾਡਲ ਕਨਫਿਗਰੇਸ਼ਨ ਬਣਾ ਸਕਦੇ ਹੋ ਜੋ Hugging Face ਉੱਤੇ ਕਿਸੇ ਵੀ ਮੇਲ ਖਾਂਦੇ ਮਾਡਲ ਨੂੰ ਪੋਇੰਟ ਕਰਦੇ ਹਨ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ Phi-4 mini ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਆਪਣੀ ਕਨਫਿਗਰੇਸ਼ਨ ਇਸ ਤਰ੍ਹਾਂ ਡਿਫਾਈਨ ਕਰ ਸਕਦੇ ਹੋ:

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

> **Note:** Phi-4 ਸਹਾਇਤਾ MLX Swift Examples ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ ਫਰਵਰੀ 2025 ਦੇ ਅੰਤ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੀ ਗਈ ਸੀ ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))। ਮਾਰਚ 2025 ਤੱਕ, ਅਖੀਰਲਾ ਅਧਿਕਾਰਿਕ ਰਿਲੀਜ਼ (2.21.2, ਦਸੰਬਰ 2024 ਤੋਂ) ਵਿੱਚ Phi-4 ਸਹਾਇਤਾ ਨਹੀਂ ਹੈ। Phi-4 ਮਾਡਲ ਵਰਤਣ ਲਈ, ਤੁਹਾਨੂੰ ਪੈਕੇਜ ਨੂੰ ਮੁੱਖ ਬ੍ਰਾਂਚ ਤੋਂ ਸਿੱਧਾ ਰੇਫਰੈਂਸ ਕਰਨਾ ਪਵੇਗਾ:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

ਇਸ ਤਰ੍ਹਾਂ ਤੁਹਾਨੂੰ ਸਭ ਤੋਂ ਨਵੇਂ ਮਾਡਲ ਕਨਫਿਗਰੇਸ਼ਨ, ਜਿਵੇਂ Phi-4, ਤੱਕ ਪਹੁੰਚ ਮਿਲਦੀ ਹੈ ਜੋ ਅਧਿਕਾਰਿਕ ਰਿਲੀਜ਼ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਹਨ। ਤੁਸੀਂ ਇਸ ਤਰੀਕੇ ਨਾਲ ਵੱਖ-ਵੱਖ Phi ਮਾਡਲ ਵਰਜਨਾਂ ਜਾਂ ਹੋਰ ਮਾਡਲ ਜੋ MLX ਫਾਰਮੈਟ ਵਿੱਚ ਕਨਵਰਟ ਕੀਤੇ ਗਏ ਹਨ, ਵਰਤ ਸਕਦੇ ਹੋ।

## ਕਦਮ 6: UI ਬਣਾਓ

ਹੁਣ ਅਸੀਂ ਇੱਕ ਸਧਾਰਣ ਚੈਟ ਇੰਟਰਫੇਸ ਲਾਗੂ ਕਰਦੇ ਹਾਂ ਜੋ ਸਾਡੇ ViewModel ਨਾਲ ਇੰਟਰੈਕਟ ਕਰੇਗਾ:

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

UI ਵਿੱਚ ਤਿੰਨ ਮੁੱਖ ਹਿੱਸੇ ਹਨ ਜੋ ਮਿਲ ਕੇ ਇੱਕ ਬੁਨਿਆਦੀ ਚੈਟ ਇੰਟਰਫੇਸ ਬਣਾਉਂਦੇ ਹਨ। `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` ਇੱਕ ਸਧਾਰਣ ਐਨੀਮੇਟਿਡ ਇੰਡਿਕੇਟਰ ਦਿੰਦੇ ਹਨ ਜੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ AI ਪ੍ਰੋਸੈਸਿੰਗ ਕਰ ਰਿਹਾ ਹੈ।

## ਕਦਮ 7: ਐਪ ਬਿਲਡ ਅਤੇ ਚਲਾਓ

ਹੁਣ ਅਸੀਂ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਬਿਲਡ ਅਤੇ ਚਲਾਉਣ ਲਈ ਤਿਆਰ ਹਾਂ।

> **Important!** MLX ਸਿਮੁਲੇਟਰ ਨੂੰ ਸਹਾਇਤਾ ਨਹੀਂ ਕਰਦਾ। ਤੁਹਾਨੂੰ ਐਪ ਨੂੰ ਸਿੱਧਾ ਇੱਕ ਫਿਜ਼ੀਕਲ ਡਿਵਾਈਸ 'ਤੇ ਚਲਾਉਣਾ ਪਵੇਗਾ ਜਿਸ ਵਿੱਚ Apple Silicon ਚਿਪ ਹੋਵੇ। ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ [ਇਥੇ](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) ਵੇਖੋ।

ਜਦੋਂ ਐਪ ਲਾਂਚ ਹੋਵੇ, "Load model" ਬਟਨ 'ਤੇ ਟੈਪ ਕਰੋ ਤਾਂ ਜੋ Phi-3 (ਜਾਂ ਤੁਹਾਡੇ ਕਨਫਿਗਰੇਸ਼ਨ ਅਨੁਸਾਰ Phi-4) ਮਾਡਲ ਡਾਊਨਲੋਡ ਅਤੇ ਇਨੀਸ਼ੀਅਲਾਈਜ਼ ਹੋ ਜਾਵੇ। ਇਹ ਪ੍ਰਕਿਰਿਆ ਤੁਹਾਡੇ ਇੰਟਰਨੈੱਟ ਕਨੈਕਸ਼ਨ ਦੇ ਅਨੁਸਾਰ ਕੁਝ ਸਮਾਂ ਲੈ ਸਕਦੀ ਹੈ ਕਿਉਂਕਿ ਮਾਡਲ Hugging Face ਤੋਂ ਡਾਊਨਲੋਡ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ। ਸਾਡੀ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਵਿੱਚ ਸਿਰਫ਼ ਲੋਡਿੰਗ ਦੌਰਾਨ ਇੱਕ ਸਪਿੰਨਰ ਹੈ, ਪਰ ਤੁਸੀਂ Xcode ਕਨਸੋਲ ਵਿੱਚ ਅਸਲ ਪ੍ਰਗਤੀ ਦੇਖ ਸਕਦੇ ਹੋ।

ਲੋਡ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਟੈਕਸਟ ਫੀਲਡ ਵਿੱਚ ਪ੍ਰਸ਼ਨ ਲਿਖ ਕੇ ਅਤੇ ਭੇਜਣ ਵਾਲੇ ਬਟਨ 'ਤੇ ਟੈਪ ਕਰਕੇ ਮਾਡਲ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰ ਸਕਦੇ ਹੋ।

ਇਹੋ ਜਿਹਾ ਸਾਡਾ ਐਪਲੀਕੇਸ਼ਨ iPad Air M1 'ਤੇ ਚੱਲਦਾ ਹੋਇਆ:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## ਨਤੀਜਾ

ਬਸ ਹੋ ਗਿਆ! ਇਹ ਕਦਮਾਂ ਪ従ਰ ਕਰਕੇ, ਤੁਸੀਂ ਇੱਕ ਐਸਾ iOS ਐਪ ਬਣਾਇਆ ਹੈ ਜੋ ਸਿੱਧਾ ਡਿਵਾਈਸ 'ਤੇ Phi-3 (ਜਾਂ Phi-4) ਮਾਡਲ Apple ਦੇ MLX ਫਰੇਮਵਰਕ ਨਾਲ ਚਲਾਉਂਦਾ ਹੈ।

ਵਧਾਈਆਂ!

**ਅਸਵੀਕਾਰੋक्ति**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।