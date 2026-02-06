# iOS ನಲ್ಲಿ Apple MLX ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿಕೊಂಡು Phi-3 ಮತ್ತು Phi-4 ನಡೆಸುವುದು

ಈ ಟ್ಯುಟೋರಿಯಲ್ Apple MLX ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ Phi-3 ಅಥವಾ Phi-4 ಮಾದರಿಯನ್ನು ಡಿವೈಸ್‌ನಲ್ಲಿ ಕಾರ್ಯಗತಗೊಳಿಸುವ ಅನುಭವವನ್ನು ತೋರಿಸುತ್ತದೆ. [MLX](https://opensource.apple.com/projects/mlx/) ಎಂಬುದು Apple Silicon ಚಿಪ್‌ಗಳಿಗೆ ಆప్టಿಮೈಝ್ ಮಾಡಲಾದ Apple's ಮೆಷಿನ್ ಲರ್ನಿಂಗ್ ಫ್ರೇಮ್ವರ್ಕ್.

## ಅಗತ್ಯಗಳು

- Xcode 16 (ಅಥವಾ ಮೇಲಿನ) ಹೊಂದಿರುವ macOS
- ಕನಿಷ್ಠ 8GB ಇರುವ iOS 18 (ಅಥವಾ ಮೇಲಿನ) ಗುರಿತಾಗಿರುವ ಸಾಧನ (Apple Intelligence ಅನಿವಾರ್ಯತೆಗಳಿಗೆ ಹೊಂದಿಕೊಳ್ಳುವ iPhone ಅಥವಾ iPad, ಏಕೆಂದರೆ ಅವು ಗುಣಾತ್ಮಕ Phi ಅವಶ್ಯಕತೆಗಳಿಗೆ ಸಮಾನವಾಗಿರುತ್ತವೆ)
- Swift ಮತ್ತು SwiftUI ಬಗ್ಗೆ בסיס ಜ್ಞಾನ

## ಹೆಜ್ಜೆ 1: ಹೊಸ iOS ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಿ

Xcode ನಲ್ಲಿ ಹೊಸ iOS ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸುವುದರೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸಿ:

1. Xcode ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು "Create a new Xcode project" ಆಯ್ಕೆಮಾಡಿ
2. ಟೆಂಪ್ಲೇಟಾಗಿ "App" ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ
3. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ ಹೆಸರು ನೀಡಿರಿ (ಉದಾಹರಣೆಗೆ, "Phi3-iOS-App") ಮತ್ತು ಇಂಟರ್ಫೇಸ್‌ಗೆ SwiftUI ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ
4. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಉಳಿಸಲು ಸ್ಥಳವನ್ನು ಆಯ್ಕೆಮಾಡಿ

## ಹೆಜ್ಜೆ 2: ಅಗತ್ಯ ನಿರ್ಭರಶೀಲತೆಗಳನ್ನು ಸೇರಿಸಿ

ಮಾಡೆಲ್ಗಳನ್ನು ಪೂರ್ವಲೋಡ್ ಮಾಡುವ ಮತ್ತು ಇನ್ಫೆರೆನ್ಸ್ ನಿರ್ವಹಿಸಲು ಅಗತ್ಯವಿರುವ ಎಲ್ಲಾ ನಿರ್ಭರಶೀಲತೆಗಳು ಮತ್ತು ಸಹಾಯಕಾಂಶಗಳನ್ನು ಒಳಗೊಂಡಿರುವ [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ಅನ್ನು ಸೇರಿಸಿ:

```swift
// Xcode ನಲ್ಲಿ: ಫೈಲ್ > ಪ್ಯಾಕೇಜ್ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ
// ಯುಆರ್‌ಎಲ್: https://github.com/ml-explore/mlx-swift-examples
```

ಮೂಲ [MLX Swift package](https://github.com/ml-explore/mlx-swift) ಮೂಲ ಟೆನ್ಸರ್ ಆಪರೇಷನ್ಗಳು ಮತ್ತು ಮೂಲ ML ಕಾರ್ಯಕ್ಷಮತೆಗೆ ಸಾಕಾಗುತ್ತಿದ್ದರೂ, MLX Examples package ಭಾಷಾ ಮಾದರಿಗಳೊಂದಿಗೆ ಕೆಲಸ ಮಾಡುವ ಮತ್ತು ಇನ್ಫೆರೆನ್ಸ್ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಸುಲಭಗೊಳಿಸುವ ಕೆಲವು ಹೆಚ್ಚುವರಿ ಘಟಕಗಳನ್ನು ನೀಡುತ್ತದೆ:

- Hugging Face ನಿಂದ ಡೌನ್‍ಲೋಡ್ ಮಾಡುವುದನ್ನು ನಿರ್ವಹಿಸುವ ಮಾದರಿ ಲೋಡಿಂಗ್ ಯೂಟಿಲಿಟಿಗಳು
- ಟೋಕನೈಸರ್ ಇಂಟಿಗ್ರೇಷನ್
- ಪಠ್ಯ ರಚನೆಗಾಗಿ ಇನ್ಫೆರೆನ್ಸ್ ಸಹಾಯಕರ
- ಪೂರ್ವ-ವಿನ್ಯಸ್ತ ಮಾದರಿ ವ್ಯಾಖ್ಯಾನಗಳು

## ಹೆಜ್ಜೆ 3: ಎಂಟೈಟಲ್‌ಮೆಂಟ್‌ಗಳನ್ನು 구성ಿಸಿ

ನಮ್ಮ ಆಪ್ ಮಾದರಿಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಮತ್ತು ಪ್ರಚುರ ಪ್ರಮಾಣದ ಮೆಮೊರಿ ಅನ್ನು ವಹಿಸಲು ಅನುಮತಿ ನೀಡಲು, ನಮಗೆ ನಿರ್ದಿಷ್ಟ ಎಂಟೈಟಲ್‌ಮೆಂಟ್‌ಗಳು ಸೇರಿಸಬೇಕಾಗುತ್ತದೆ. ನಿಮ್ಮ ಆಪ್‌ಗಾಗಿ `.entitlements` ಫೈಲ್ ಅನ್ನು ಕೆಳಗಿನ ವಿಷಯದೊಂದಿಗೆ ರಚಿಸಿ:

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

> **ಗಮನಿಸಿ:** ದೊಡ್ಡ ಮಾದರಿಗಳನ್ನು ಚಲಾಯಿಸಲು `com.apple.developer.kernel.increased-memory-limit` ಎಂಟೈಟಲ್‌ಮೆಂಟ್ ಮುಖ್ಯವಾಗಿದೆ, ಇದರಿಂದ ಆಪ್ सामान्यವಾಗಿ ಅನುಮತಿಗಿಂತ ಹೆಚ್ಚಿನ ಮೆಮೊರಿಯನ್ನು ವಿನಂತಿಸುವಂತೆ ಮಾಡಬಹುದು.

## ಹೆಜ್ಜೆ 4: ಚಾಟ್ ಮೆಸೇಜ್ ಮಾದರಿಯನ್ನು ರಚಿಸಿ

ಮೊದಲು, ನಮ್ಮ ಚಾಟ್ ಸಂದೇಶಗಳನ್ನು ಪ್ರತಿನಿಧಿಸಲು ಮೂಲ ರಚನೆಯನ್ನು ರಚಿಸೋಣ:

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

## ಹೆಜ್ಜೆ 5: ViewModel ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ

ಮುಂದಾಗಿ, ಮಾದರಿ ಲೋಡಿಂಗ್ ಮತ್ತು ಇನ್ಫೆರೆನ್ಸ್ ಅನ್ನು ನಿರ್ವಹಿಸುವ `PhiViewModel` ಕ್ಲಾಸ್ ಅನ್ನು ರಚಿಸೋಣ:

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
            
            // Phi 3.5 mini ಅನ್ನು Swift MLX ಉದಾಹರಣೆಗಳಲ್ಲಿ ಪೂರ್ವಸಂರಚಿಸಲಾಗಿದೆ
            let modelConfig = ModelRegistry.phi3_5_4bit
            
            // Phi 4 mini ಅನ್ನು Hugging Face ನಿಂದ ಪಡೆಯಬಹುದು, ಆದರೆ ಮುಖ್ಯ ಶಾಖೆಯಿಂದ Swift MLX ಉದಾಹರಣೆಗಳನ್ನು ಉಲ್ಲೇಖಿಸಬೇಕಾಗುತ್ತದೆ
            //let modelConfig = ModelConfiguration(
            //    id: "mlx-community/Phi-4-mini-instruct-4bit",
            //    defaultPrompt: "ನೀವು ಸಹಾಯಕನಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತೀರಿ.",
            //    extraEOSTokens: ["<|end|>"]
            //)
            
            print("Loading \(modelConfig.name)...")
            self.modelContainer = try await LLMModelFactory.shared.loadContainer(
                configuration: modelConfig
            ) { progress in
                print("Download progress: \(Int(progress.fractionCompleted * 100))%")
            }
            
            // ಮಾದರಿಯ ಪ್ಯಾರಾಮೀಟರ್ಗಳನ್ನು ಲಾಗ್ ಮಾಡಿ
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

ViewModel ನಲ್ಲಿ MLX ಏಕೀಕರಣದ ಮುಖ್ಯ ಬಿಂದುಗಳನ್ನು ತೋರಿಸಲಾಗುತ್ತದೆ:

- ಮೊಬೈಲ್ ಸಾಧನಗಳಲ್ಲಿ ಮೆಮೊರಿ ಬಳಕೆಯನ್ನು tốiಮೈಸು ಮಾಡಲು `MLX.GPU.set(cacheLimit:)` ಮೂಲಕ GPU ಕ್ಯಾಶ್ ಮಿತಿ ಸೆಟ್ ಮಾಡುವುದು
- LLMModelFactory ಬಳಸಿ ಮಾದರಿಯನ್ನು ಆವಶ್ಯಕತೆಗೊಂದು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ MLX-ಆಪ್ಟಿಮೈಸ್ ಮಾಡಿದ ಮಾದರಿಯನ್ನು ಪ್ರಾರಂಭಿಸುವುದು
- `ModelContainer` ಮೂಲಕ ಮಾದರಿಯ ಪರಿಮಾಣಗಳು ಮತ್ತು ರಚನೆಯನ್ನು ಪ್ರವೇಶಿಸುವುದು
- `MLXLMCommon.generate` ವಿಧಾನ ಮೂಲಕ MLX ನ ಟೋಕನ್-ಬೈ-ಟೋಕನ್ ಉತ್ಪಾದನೆಯನ್ನು ಲಾಭದಾಯಕವಾಗಿ ಬಳಸಿಕೊಳ್ಳುವುದು
- ಸೂಕ್ತ temperature ಸೆಟ್ಟಿಂಗ್ಗಳ ಮತ್ತು ಟೋಕನ್ ಮಿತಿಗಳೊಂದಿಗೆ ಇನ್ಫೆರೆನ್ಸ್ ಪ್ರಕ್ರಿಯೆಯನ್ನು ನಿರ್ವಹಿಸುವುದು

ಸ್ಟ್ರೀಮಿಂಗ್ ಟೋಕನ್ ಉತ್ಪಾದನೆಯ ವಿಧಾನವು ಮಾದರಿ ಪಠ್ಯ ಉತ್ಪಾದಿಸುವಂತೆ ತಕ್ಷಣದ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಬಳಕೆದಾರರಿಗೆ ಒದಗಿಸುತ್ತದೆ. ಇದು ಸೇವರ್-ಆಧಾರಿತ ಮಾದರಿಗಳಂತೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ಅವು ಬಳಕೆದಾರರಿಗೆ ಟೋಕನ್‌ಗಳನ್ನು ಸ್ಟ್ರೀಮ್ ಮೂಲಕ ಹಿಂತಿರುಗಿಸುತ್ತವೆ, ಆದರೆ ನೆಟ್ವರ್ಕ್ ವಿನಂತಿಗಳ ವಿರಳತೆಯಿಲ್ಲದೆ.

UI ಇಂಟರಾಕ್ಷನ್ ದೃಷ್ಟಿಯಿಂದ, ಎರಡು ಮುಖ್ಯ ಕಾರ್ಯಗಳೆಂದರೆ `loadModel()` ಇದು LLM ಅನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ, ಮತ್ತು `fetchAIResponse()` ಇದು ಬಳಕೆದಾರರ ಇನ್‌ಪುಟ್ ಅನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ AI ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ರಚಿಸುತ್ತದೆ.

### ಮಾದರಿ ಫಾರ್ಮ್ಯಾಟ್ ಪರಿಗಣನೆಗಳು

> **ಮುಖ್ಯ:** MLXಗಾಗಿPhi ಮಾದರಿಗಳು ಅವರ ಡೀಫಾಲ್ಟ್ ಅಥವಾ GGUF ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಬಳಸಲು ಆಗುವುದಿಲ್ಲ. ಅವುಗಳನ್ನು MLX ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸುವಬೇಕು, ಇದು MLX ಸಮುದಾಯದ ಮೂಲಕ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ. ಪೂರ್ವ-ಪರಿವರ್ತಿತ ಮಾದರಿಗಳನ್ನು ನೀವು ಇಲ್ಲಿ ಕಂಡುಬರುವುದು: [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

MLX Examples package ನಲ್ಲಿ ಹಲವಾರು ಮಾದರಿಗಳ ಪೂರ್ವ-ವಿನ್ಯಸ್ತ ನೋಂದಣಿಗಳು ಸೇರಿವೆ, ಇದರಲ್ಲಿ Phi-3 ಕೂಡ ಸೇರಿದೆ. ನೀವು `ModelRegistry.phi3_5_4bit` ಅನ್ನು ಕರೆಮಾಡಿದಾಗ, ಅದು ಸ್ವಯಂಕ್ರಿಯವಾಗಿ ಡೌನ್‍ಲೋಡ್ ಆಗುವ ವಿಶೇಷ ಪೂರ್ವ-ಪರಿವರ್ತಿತ MLX ಮಾದರಿಯನ್ನು ಸೂಚಿಸುತ್ತದೆ:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

ನೀವು Hugging Face ನಲ್ಲಿ ಯಾವುದೇ ಹೊಂದಾಣಿಕೆಯ ಮಾದರಿಯನ್ನು ಸೂಚಿಸಲು ನಿಮ್ಮದೇ ಮಾದರಿ ಕಾನ್ಫಿಗರೇಶನ್‌ಗಳನ್ನು ರಚಿಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ಬದಲಾಗಿ Phi-4 mini ಬಳಸಲು, ನೀವು ನಿಮ್ಮದೇ ಕಾನ್ಫಿಗರೇಶನ್ ಅನ್ನು ಈ ರೀತಿ ವ್ಯಾಖ್ಯಾನಿಸಬಹುದು:

```swift
let phi4_mini_4bit = ModelConfiguration(
    id: "mlx-community/Phi-4-mini-instruct-4bit",
    defaultPrompt: "Explain quantum computing in simple terms.",
    extraEOSTokens: ["<|end|>"]
)

// ಆಮೇಲೆ ಮಾದರಿಯನ್ನು ಲೋಡ್ ಮಾಡುವಾಗ ಈ ಸಂರಚನೆಯನ್ನು ಬಳಸಿ
self.modelContainer = try await LLMModelFactory.shared.loadContainer(
    configuration: phi4_mini_4bit
) { progress in
    print("Download progress: \(Int(progress.fractionCompleted * 100))%")
}
```

> **ಗಮನಿಸಿ:** Phi-4 ಬೆಂಬಲವನ್ನು MLX Swift Examples ರೆಪೊಸಿಟರಿಗೆ ಫೆಬ್ರವರಿ 2025 ಅಡಿಯಲ್ಲೇ ಸೇರಿಸಲಾಗಿದೆ ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). ಮಾರ್ಚ್ 2025 ರವರೆಗೆ, ಡಿಸೆಂಬರ್ 2024 ರಲ್ಲಿ ಬಿಡುಗಡೆಯಾದ ಇತ್ತೀಚಿನ ಅಧಿಕೃತ ರಿಲೀಸ್ (2.21.2) ನಲ್ಲಿ ನಿರ್ಮಿತ Phi-4 ಬೆಂಬಲ ಇಲ್ಲ. Phi-4 ಮಾದರಿಗಳನ್ನು ಬಳಸಲು, ನೀವು ಮುಖ್ಯ ಶಾಖೆಯಿಂದ ನೇರವಾಗಿ ಪ್ಯಾಕೇಜ್ ಅನ್ನು ಉಲ್ಲೇಖಿಸಬೇಕಾಗುತ್ತದೆ:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

ಇದು ಅಧಿಕೃತ ಬಿಡುಗಡೆಯಿಗೆ ಮುಂಚೆಯೇ ಇತ್ತೀಚಿನ ಮಾದರಿ ಕಾನ್ಫಿಗರೇಶನ್‌ಗಳಿಗೆ, ಸೇರಿದಂತೆ Phi-4, ಪ್ರವೇಶವನ್ನು ಒದಗಿಸುತ್ತದೆ. ಈ ವಿಧಾನವನ್ನು ವಿವಿಧ Phi ಮಾದರಿ ಆವೃತ್ತಿಗಳನ್ನು ಅಥವಾ MLX ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸಲಾದ ಇತರ ಮಾದರಿಗಳನ್ನು ಬಳಸಲು ಬಳಸಬಹುದು.

## ಹೆಜ್ಜೆ 6: UI ರಚಿಸಿ

ಇಗ್ಗೆ, ನಮ್ಮ view model ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲು ಸರಳ ಚಾಟ್ ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸೋಣ:

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

UI ಮೂರು ಮುಖ್ಯ ಘಟಕಗಳಿಂದ ಕೂಡಿದೆ, ಅವು ಒಟ್ಟಾಗಿ ಮೂಲ ಚಾಟ್ ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ರಚಿಸುತ್ತವೆ. `ContentView` ಮಾದರಿಯ ಸಿದ್ಧತೆಗೆ ಅನುಗುಣವಾಗಿ ಲೋಡಿಂಗ್ ಬಟನ್ ಅಥವಾ ಚಾಟ್ ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ತೋರಿಸುವ ಎರಡು-ಸ್ಥಿತಿಯ ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ರಚಿಸುತ್ತದೆ. `MessageView` ಬಳಕೆದಾರ ಸಂದೇಶಗಳ (ಬಲಕ್ಕೆ ಸರಿತೂ, ನೀಲಿ ಹಿನ್ನೆಲೆ) ಅಥವಾ Phi ಮಾದರಿ ಪ್ರತಿಕ್ರಿಯೆಗಳ (ಎಡಕ್ಕೆ ಸರಿತೂ, ಬೂದು ಹಿನ್ನೆಲೆ) ಆಧಾರದ ಮೇಲೆ ವೈಯಕ್ತಿಕ ಚಾಟ್ ಸಂದೇಶಗಳನ್ನು ವಿಭಿನ್ನವಾಗಿ ರೆಂಡರ್ ಮಾಡುತ್ತದೆ. `TypingIndicatorView` AI ಪ್ರಕ್ರಿಯೆ ವೇಳೆ ತೋರಿಸಲು ಸರಳ ಅನಿಮೇಟೆಡ್ ಸೂಚಕವನ್ನು ಒದಗಿಸುತ್ತದೆ

## ಹೆಜ್ಜೆ 7: ಆಪ್ ಅನ್ನು ಬಿಲ್ಡ್ ಮಾಡಿ ಮತ್ತು ಚಾಲನೆ ಮಾಡಿ

ನಾವು ಈಗ ಆಪ್ ಅನ್ನು ಬಿಲ್ಡ್ ಮತ್ತು ಚಾಲನೆ ಮಾಡಲು ಸಿದ್ಧರಾಗಿದ್ದೇವೆ.

> **ಮುಖ್ಯ!** MLX ಸಿಮ್ಯುಲೇಟರ್ ಅನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ. ನೀವು ಆಪ್ ಅನ್ನು Apple Silicon ಚಿಪ್ ಇರುವ ಭೌತಿಕ ಸಾಧನದಲ್ಲಿ ಕಾರ್ಯಗತಗೊಳಿಸಬೇಕು. ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ ಇಲ್ಲಿ ನೋಡಿ: [here](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

ಆಪ್ ಆರಂಭವಾದಾಗ, Phi-3 (ಅಥವಾ ನಿಮ್ಮ ಕಾನ್ಫಿಗರೇಶನ್ ಅನುಸಾರ Phi-4) ಮಾದರಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ಪ್ರಾರಂಭಿಸಲು "Load model" ಬಟನ್ ಅನ್ನು ಟ್ಯಾಪ್ ಮಾಡಿ. ಇದು Hugging Face ನಂದಿಂದ ಮಾದರಿಯನ್ನು ಡೌನ್‍ಲೋಡ್ ಮಾಡಲು ಸಂಬಂಧಿಸಿದ ಕಾರಣದಿಂದ ನಿಮ್ಮ ಇಂಟರ್‌ನೆಟ್ ಕನೆಕ್ಷನ್ ಅವಲಂಬನೆಯಂತೆ ಕೆಲವು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳಬಹುದು. ನಮ್ಮ ಅನುಷ್ಠಾನದಲ್ಲಿ ಲೋಡಿಂಗ್ ಸೂಚಿಸಲು ಕೇವಲ ಸ್ಪಿನ್ನರ್ ಇದೆ, ಆದರೆ ನೀವು ನಿಖರ ಪ್ರಗತಿಯನ್ನು Xcode ಕನ್‌ಸೋಲ್‌ನಲ್ಲಿ ನೋಡಬಹುದು.

ಒಮ್ಮೆ ಲೋಡ್ ಆದಮೇಲೆ, ನೀವು ಪಠ್ಯ ಫೀಲ್ಡ್‌ನಲ್ಲಿ ಪ್ರಶ್ನೆಗಳನ್ನು ಟೈಪ್ ಮಾಡಿ ಸेंड್ ಬಟನ್ ಅನ್ನು ಟ್ಯಾಪ್ ಮಾಡುವ ಮೂಲಕ ಮಾದರಿಯೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಬಹುದು.

ನಮ್ಮ ಅನ್ವಯಿಕೆ iPad Air M1 ನಲ್ಲಿ ಚಾಲನೆಯಲ್ಲಿರುವಾಗ ಹೇಗೆ ನಡೆದುಕೊಳ್ಳಬೇಕು ಎಂಬುದನ್ನು ಇಲ್ಲಿ ನೋಡಬಹುದು:

![ಡೆಮೋ GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## ನಿರ್ಗಮನ

ಇಷ್ಟೆ! ಈ ಹೆಜ್ಜೆಗಳನ್ನು ಅನುಸರಿಸುವ ಮೂಲಕ, ನೀವು Apple ರ MLX ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ Phi-3 (ಅಥವಾ Phi-4) ಮಾದರಿಯನ್ನು ನೇರವಾಗಿ ಸಾಧನದಲ್ಲಿ ಚಾಲನೆ ಮಾಡುವ iOS ಆಪ್ ಅನ್ನು ರಚಿಸಿದ್ದೀರಿ.

ಅಭಿನಂದನೆಗಳು!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಅಸ್ವೀಕರಣ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಭಾಷಾಂತರ ಸೇವೆ Co‑op Translator (https://github.com/Azure/co-op-translator) ಬಳಸಿ ಭಾಷಾಂತರಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ ಸಹ, ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸ್ಪಷ್ಟತೆಗಳು ಇರಬಹುದೆಂದು ದಯವಿಟ್ಟು ತಿಳಿದುಕೊಳ್ಳಿ. ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕಾದದ್ದು ಮೂಲ ದಸ್ತಾವೇಜಿನ ಸ್ವದೇಶಿ (ಮೂಲ) ಭಾಷೆಯೇ ಆಗಿದೆ. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸಿಸಲಾಗಿದೆ. ಈ ಭಾಷಾಂತರವನ್ನು ಬಳಸುವುದರಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೆಗಳು ಅಥವಾ ದುರ್ಭಾವನೆಗಳಿಗಾಗಿ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->