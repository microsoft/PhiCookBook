<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:30:30+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "pa"
}
-->
# iOS 'ਤੇ Apple MLX ਫਰੇਮਵਰਕ ਨਾਲ Phi-3 ਅਤੇ Phi-4 ਚਲਾਉਣਾ

ਇਹ ਟਿਊਟੋਰਿਯਲ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਵੇਂ ਇੱਕ iOS ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈ ਜਾਵੇ ਜੋ Apple MLX ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3 ਜਾਂ Phi-4 ਮਾਡਲ ਨੂੰ ਡਿਵਾਈਸ 'ਤੇ ਚਲਾਉਂਦਾ ਹੈ। [MLX](https://opensource.apple.com/projects/mlx/) Apple ਦਾ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਫਰੇਮਵਰਕ ਹੈ ਜੋ Apple Silicon ਚਿਪਸ ਲਈ ਅਨੁਕੂਲਿਤ ਹੈ।

## ਲੋੜੀਂਦੇ ਸਾਧਨ

- macOS ਜਿਸ ਵਿੱਚ Xcode 16 (ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ) ਹੋਵੇ
- iOS 18 (ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ) ਟਾਰਗੇਟ ਡਿਵਾਈਸ ਜਿਸ ਵਿੱਚ ਘੱਟੋ-ਘੱਟ 8GB ਰੈਮ ਹੋਵੇ (iPhone ਜਾਂ iPad ਜੋ Apple Intelligence ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਦਾ ਹੋਵੇ, ਕਿਉਂਕਿ ਇਹ Phi ਦੇ ਕਵਾਂਟਾਈਜ਼ਡ ਮਾਡਲ ਦੀਆਂ ਲੋੜਾਂ ਵਰਗੇ ਹਨ)
- Swift ਅਤੇ SwiftUI ਦੀ ਬੁਨਿਆਦੀ ਜਾਣਕਾਰੀ

## ਕਦਮ 1: ਨਵਾਂ iOS ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

Xcode ਵਿੱਚ ਨਵਾਂ iOS ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ:

1. Xcode ਖੋਲ੍ਹੋ ਅਤੇ "Create a new Xcode project" ਚੁਣੋ
2. ਟੈਮਪਲੇਟ ਵਜੋਂ "App" ਚੁਣੋ
3. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦਾ ਨਾਮ ਦਿਓ (ਜਿਵੇਂ "Phi3-iOS-App") ਅਤੇ ਇੰਟਰਫੇਸ ਵਜੋਂ SwiftUI ਚੁਣੋ
4. ਪ੍ਰੋਜੈਕਟ ਸੇਵ ਕਰਨ ਲਈ ਥਾਂ ਚੁਣੋ

## ਕਦਮ 2: ਲੋੜੀਂਦੇ Dependencies ਸ਼ਾਮਲ ਕਰੋ

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ਸ਼ਾਮਲ ਕਰੋ ਜਿਸ ਵਿੱਚ ਸਾਰੇ ਜਰੂਰੀ dependencies ਅਤੇ ਮਾਡਲ ਪ੍ਰੀਲੋਡਿੰਗ ਅਤੇ ਇੰਫਰੈਂਸ ਲਈ ਸਹਾਇਕ ਹਨ:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

ਜਦਕਿ ਬੇਸ [MLX Swift package](https://github.com/ml-explore/mlx-swift) ਕੋਰ ਟੈਂਸਰ ਓਪਰੇਸ਼ਨ ਅਤੇ ਬੁਨਿਆਦੀ ML ਫੰਕਸ਼ਨਾਲਿਟੀ ਲਈ ਕਾਫ਼ੀ ਹੈ, MLX Examples package ਵਿੱਚ ਕਈ ਵਾਧੂ ਹਿੱਸੇ ਹਨ ਜੋ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਅਤੇ ਇੰਫਰੈਂਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦੇ ਹਨ:

- Hugging Face ਤੋਂ ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਨ ਵਾਲੀਆਂ ਯੂਟਿਲਿਟੀਜ਼
- ਟੋਕਨਾਈਜ਼ਰ ਇੰਟੀਗ੍ਰੇਸ਼ਨ
- ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਲਈ ਇੰਫਰੈਂਸ ਸਹਾਇਕ
- ਪਹਿਲਾਂ ਤੋਂ ਕਨਫਿਗਰ ਕੀਤੇ ਮਾਡਲ ਡਿਫਿਨੀਸ਼ਨ

## ਕਦਮ 3: Entitlements ਕਨਫਿਗਰ ਕਰੋ

ਸਾਡੇ ਐਪ ਨੂੰ ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਨ ਅਤੇ ਕਾਫ਼ੀ ਮੈਮੋਰੀ ਅਲੋਕੇਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦੇਣ ਲਈ, ਸਾਨੂੰ ਖਾਸ entitlements ਸ਼ਾਮਲ ਕਰਨੇ ਪੈਣਗੇ। ਆਪਣੇ ਐਪ ਲਈ `.entitlements` ਫਾਇਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਇਹ ਸਮੱਗਰੀ ਹੋਵੇ:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement ਵੱਡੇ ਮਾਡਲ ਚਲਾਉਣ ਲਈ ਜਰੂਰੀ ਹੈ, ਕਿਉਂਕਿ ਇਹ ਐਪ ਨੂੰ ਆਮ ਤੌਰ 'ਤੇ ਮਨਜ਼ੂਰ ਕੀਤੀ ਮੈਮੋਰੀ ਤੋਂ ਵੱਧ ਮੰਗਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

## ਕਦਮ 4: Chat Message ਮਾਡਲ ਬਣਾਓ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਚੈਟ ਸੁਨੇਹਿਆਂ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਇੱਕ ਬੁਨਿਆਦੀ ਸਟ੍ਰਕਚਰ ਬਣਾਈਏ:

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

ਹੁਣ, `PhiViewModel` ਕਲਾਸ ਬਣਾਓ ਜੋ ਮਾਡਲ ਲੋਡਿੰਗ ਅਤੇ ਇੰਫਰੈਂਸ ਨੂੰ ਸੰਭਾਲੇਗੀ:

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

ViewModel ਵਿੱਚ MLX ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੇ ਮੁੱਖ ਬਿੰਦੂ ਦਰਸਾਏ ਗਏ ਹਨ:

- ਮੋਬਾਈਲ ਡਿਵਾਈਸਾਂ 'ਤੇ ਮੈਮੋਰੀ ਦੀ ਬਚਤ ਲਈ `MLX.GPU.set(cacheLimit:)` ਨਾਲ GPU ਕੈਸ਼ ਸੀਮਾ ਸੈੱਟ ਕਰਨਾ
- `LLMModelFactory` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਡਲ ਨੂੰ ਲੋੜ ਅਨੁਸਾਰ ਡਾਊਨਲੋਡ ਕਰਨਾ ਅਤੇ MLX-ਅਨੁਕੂਲ ਮਾਡਲ ਸ਼ੁਰੂ ਕਰਨਾ
- `ModelContainer` ਰਾਹੀਂ ਮਾਡਲ ਦੇ ਪੈਰਾਮੀਟਰ ਅਤੇ ਸਟ੍ਰਕਚਰ ਤੱਕ ਪਹੁੰਚ
- MLX ਦੇ `MLXLMCommon.generate` ਮੈਥਡ ਨਾਲ ਟੋਕਨ-ਬਾਈ-ਟੋਕਨ ਜਨਰੇਸ਼ਨ
- ਇੰਫਰੈਂਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਢੰਗ ਨਾਲ ਟੈਮਪਰੇਚਰ ਸੈਟਿੰਗ ਅਤੇ ਟੋਕਨ ਸੀਮਾਵਾਂ ਨਾਲ ਸੰਭਾਲਣਾ

ਸਟ੍ਰੀਮਿੰਗ ਟੋਕਨ ਜਨਰੇਸ਼ਨ ਤਰੀਕਾ ਮਾਡਲ ਦੇ ਟੈਕਸਟ ਬਣਾਉਂਦੇ ਸਮੇਂ ਤੁਰੰਤ ਫੀਡਬੈਕ ਦਿੰਦਾ ਹੈ। ਇਹ ਸਰਵਰ-ਆਧਾਰਿਤ ਮਾਡਲਾਂ ਵਾਂਗ ਹੈ ਜੋ ਟੋਕਨ ਨੂੰ ਯੂਜ਼ਰ ਨੂੰ ਸਟ੍ਰੀਮ ਕਰਦੇ ਹਨ, ਪਰ ਬਿਨਾਂ ਨੈੱਟਵਰਕ ਦੇਰੀ ਦੇ।

UI ਇੰਟਰੈਕਸ਼ਨ ਦੇ ਸੰਦਰਭ ਵਿੱਚ, ਦੋ ਮੁੱਖ ਫੰਕਸ਼ਨ ਹਨ: `loadModel()`, ਜੋ LLM ਨੂੰ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ, ਅਤੇ `fetchAIResponse()`, ਜੋ ਯੂਜ਼ਰ ਇਨਪੁੱਟ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਕੇ AI ਜਵਾਬ ਬਣਾਉਂਦਾ ਹੈ।

### ਮਾਡਲ ਫਾਰਮੈਟ ਬਾਰੇ ਵਿਚਾਰ

> **Important:** MLX ਲਈ Phi ਮਾਡਲ ਆਪਣੇ ਡਿਫਾਲਟ ਜਾਂ GGUF ਫਾਰਮੈਟ ਵਿੱਚ ਵਰਤੇ ਨਹੀਂ ਜਾ ਸਕਦੇ। ਇਹਨਾਂ ਨੂੰ MLX ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣਾ ਪੈਂਦਾ ਹੈ, ਜੋ MLX ਕਮਿਊਨਿਟੀ ਦੁਆਰਾ ਸੰਭਾਲਿਆ ਜਾਂਦਾ ਹੈ। ਤੁਸੀਂ ਪਹਿਲਾਂ ਤੋਂ ਬਦਲੇ ਹੋਏ ਮਾਡਲ [huggingface.co/mlx-community](https://huggingface.co/mlx-community) 'ਤੇ ਲੱਭ ਸਕਦੇ ਹੋ।

MLX Examples package ਵਿੱਚ ਕਈ ਮਾਡਲਾਂ ਲਈ ਪਹਿਲਾਂ ਤੋਂ ਕਨਫਿਗਰ ਕੀਤੀਆਂ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਹਨ, ਜਿਵੇਂ Phi-3। ਜਦੋਂ ਤੁਸੀਂ `ModelRegistry.phi3_5_4bit` ਕਾਲ ਕਰਦੇ ਹੋ, ਇਹ ਇੱਕ ਖਾਸ ਪਹਿਲਾਂ ਤੋਂ ਬਦਲੇ ਹੋਏ MLX ਮਾਡਲ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ ਜੋ ਆਪਣੇ ਆਪ ਡਾਊਨਲੋਡ ਹੋ ਜਾਵੇਗਾ:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

ਤੁਸੀਂ ਆਪਣੀਆਂ ਮਾਡਲ ਕਨਫਿਗਰੇਸ਼ਨ ਬਣਾਕੇ Hugging Face 'ਤੇ ਕਿਸੇ ਵੀ ਅਨੁਕੂਲ ਮਾਡਲ ਨੂੰ ਪੌਇੰਟ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ, Phi-4 ਮਿਨੀ ਵਰਤਣ ਲਈ, ਤੁਸੀਂ ਆਪਣੀ ਕਨਫਿਗਰੇਸ਼ਨ ਇਸ ਤਰ੍ਹਾਂ ਬਣਾ ਸਕਦੇ ਹੋ:

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

> **Note:** Phi-4 ਸਹਾਇਤਾ MLX Swift Examples ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਫਰਵਰੀ 2025 ਦੇ ਅੰਤ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੀ ਗਈ ਸੀ ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))। ਮਾਰਚ 2025 ਤੱਕ, ਦਸੰਬਰ 2024 ਦੀ ਆਖਰੀ ਅਧਿਕਾਰਿਕ ਰਿਲੀਜ਼ (2.21.2) ਵਿੱਚ Phi-4 ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਨਹੀਂ ਹੈ। Phi-4 ਮਾਡਲ ਵਰਤਣ ਲਈ, ਤੁਹਾਨੂੰ ਮੁੱਖ ਬ੍ਰਾਂਚ ਤੋਂ ਪੈਕੇਜ ਨੂੰ ਸਿੱਧਾ ਰੈਫਰ ਕਰਨਾ ਪਵੇਗਾ:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

ਇਸ ਤਰੀਕੇ ਨਾਲ ਤੁਹਾਨੂੰ ਨਵੀਆਂ ਮਾਡਲ ਕਨਫਿਗਰੇਸ਼ਨਾਂ ਤੱਕ ਪਹੁੰਚ ਮਿਲਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ Phi-4 ਵੀ ਸ਼ਾਮਲ ਹੈ, ਜਦੋਂ ਤੱਕ ਇਹ ਅਧਿਕਾਰਿਕ ਰਿਲੀਜ਼ ਵਿੱਚ ਸ਼ਾਮਲ ਨਹੀਂ ਹੁੰਦਾ। ਤੁਸੀਂ ਇਸ ਤਰੀਕੇ ਨਾਲ ਵੱਖ-ਵੱਖ Phi ਮਾਡਲਾਂ ਜਾਂ ਹੋਰ ਮਾਡਲਾਂ ਨੂੰ ਜੋ MLX ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲੇ ਗਏ ਹਨ, ਵਰਤ ਸਕਦੇ ਹੋ।

## ਕਦਮ 6: UI ਬਣਾਓ

ਹੁਣ ਸਾਡੇ ViewModel ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ ਇੱਕ ਸਧਾਰਣ ਚੈਟ ਇੰਟਰਫੇਸ ਬਣਾਈਏ:

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

UI ਵਿੱਚ ਤਿੰਨ ਮੁੱਖ ਹਿੱਸੇ ਹਨ ਜੋ ਮਿਲ ਕੇ ਇੱਕ ਬੁਨਿਆਦੀ ਚੈਟ ਇੰਟਰਫੇਸ ਬਣਾਉਂਦੇ ਹਨ। `ContentView` ਇੱਕ ਦੋ-ਹਾਲਤ ਵਾਲਾ ਇੰਟਰਫੇਸ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਮਾਡਲ ਤਿਆਰ ਹੋਣ 'ਤੇ ਲੋਡਿੰਗ ਬਟਨ ਜਾਂ ਚੈਟ ਇੰਟਰਫੇਸ ਦਿਖਾਉਂਦਾ ਹੈ। `MessageView` ਵੱਖ-ਵੱਖ ਤਰੀਕੇ ਨਾਲ ਯੂਜ਼ਰ ਦੇ ਸੁਨੇਹੇ (ਸੱਜੇ ਪਾਸੇ, ਨੀਲੇ ਬੈਕਗ੍ਰਾਊਂਡ) ਅਤੇ Phi ਮਾਡਲ ਦੇ ਜਵਾਬ (ਖੱਬੇ ਪਾਸੇ, ਧੂਸਰ ਬੈਕਗ੍ਰਾਊਂਡ) ਨੂੰ ਰੇਂਡਰ ਕਰਦਾ ਹੈ। `TypingIndicatorView` ਇੱਕ ਸਧਾਰਣ ਐਨੀਮੇਟਿਡ ਇੰਡਿਕੇਟਰ ਦਿੰਦਾ ਹੈ ਜੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ AI ਪ੍ਰੋਸੈਸ ਕਰ ਰਿਹਾ ਹੈ।

## ਕਦਮ 7: ਐਪ ਬਣਾਓ ਅਤੇ ਚਲਾਓ

ਹੁਣ ਅਸੀਂ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਬਣਾਉਣ ਅਤੇ ਚਲਾਉਣ ਲਈ ਤਿਆਰ ਹਾਂ।

> **Important!** MLX ਸਿਮੂਲੇਟਰ ਨੂੰ ਸਪੋਰਟ ਨਹੀਂ ਕਰਦਾ। ਤੁਹਾਨੂੰ ਐਪ ਨੂੰ Apple Silicon ਚਿਪ ਵਾਲੇ ਫਿਜ਼ੀਕਲ ਡਿਵਾਈਸ 'ਤੇ ਚਲਾਉਣਾ ਪਵੇਗਾ। ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਲਈ [ਇੱਥੇ](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) ਵੇਖੋ।

ਜਦੋਂ ਐਪ ਲਾਂਚ ਹੋਵੇ, "Load model" ਬਟਨ 'ਤੇ ਟੈਪ ਕਰੋ ਤਾਂ ਜੋ Phi-3 (ਜਾਂ ਤੁਹਾਡੇ ਕਨਫਿਗਰੇਸ਼ਨ ਅਨੁਸਾਰ Phi-4) ਮਾਡਲ ਡਾਊਨਲੋਡ ਅਤੇ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾਵੇ। ਇਹ ਪ੍ਰਕਿਰਿਆ ਤੁਹਾਡੇ ਇੰਟਰਨੈੱਟ ਕਨੈਕਸ਼ਨ ਦੇ ਅਨੁਸਾਰ ਕੁਝ ਸਮਾਂ ਲੈ ਸਕਦੀ ਹੈ, ਕਿਉਂਕਿ ਮਾਡਲ Hugging Face ਤੋਂ ਡਾਊਨਲੋਡ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ। ਸਾਡੀ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਵਿੱਚ ਸਿਰਫ਼ ਲੋਡਿੰਗ ਦਿਖਾਉਣ ਲਈ ਸਪਿੰਨਰ ਹੈ, ਪਰ ਤੁਸੀਂ Xcode ਕੰਸੋਲ ਵਿੱਚ ਅਸਲ ਪ੍ਰਗਤੀ ਵੇਖ ਸਕਦੇ ਹੋ।

ਲੋਡ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਮਾਡਲ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰ ਸਕਦੇ ਹੋ, ਟੈਕਸਟ ਫੀਲਡ ਵਿੱਚ ਸਵਾਲ ਲਿਖ ਕੇ ਅਤੇ ਸੈਂਡ ਬਟਨ 'ਤੇ ਟੈਪ ਕਰਕੇ।

ਇਹ ਹੈ ਕਿ ਸਾਡੀ ਐਪਲੀਕੇਸ਼ਨ iPad Air M1 'ਤੇ ਕਿਵੇਂ ਕੰਮ ਕਰਦੀ ਹੈ:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## ਨਤੀਜਾ

ਬਸ ਇਹੀ! ਇਹਨਾਂ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ, ਤੁਸੀਂ ਇੱਕ iOS ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈ ਹੈ ਜੋ Apple ਦੇ MLX ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3 (ਜਾਂ Phi-4) ਮਾਡਲ ਨੂੰ ਸਿੱਧਾ ਡਿਵਾਈਸ 'ਤੇ ਚਲਾਉਂਦਾ ਹੈ।

ਵਧਾਈਆਂ!

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।