<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-07T14:39:34+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "mo"
}
-->
# Running Phi-3 and Phi-4 on iOS with Apple MLX Framework

This tutorial shows how to build an iOS app that runs the Phi-3 or Phi-4 model locally, using Apple’s MLX framework. [MLX](https://opensource.apple.com/projects/mlx/) is Apple’s machine learning framework optimized for Apple Silicon chips.

## Prerequisites

- macOS with Xcode 16 (or newer)  
- iOS 18 (or newer) device with at least 8GB RAM (iPhone or iPad compatible with Apple Intelligence requirements, similar to the quantized Phi requirements)  
- basic knowledge of Swift and SwiftUI  

## Step 1: Create a New iOS Project

Start by creating a new iOS project in Xcode:

1. open Xcode and select "Create a new Xcode project"  
2. choose "App" as the template  
3. name your project (e.g., "Phi3-iOS-App") and select SwiftUI as the interface  
4. pick a location to save your project  

## Step 2: Add Required Dependencies

Add the [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) which includes all needed dependencies and helpers for preloading models and running inference:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

While the core [MLX Swift package](https://github.com/ml-explore/mlx-swift) covers basic tensor operations and ML features, the MLX Examples package adds several components tailored for language models and simplifies inference:

- utilities to load models, including downloading from Hugging Face  
- tokenizer integration  
- helpers for text generation inference  
- pre-configured model definitions  

## Step 3: Configure Entitlements

To allow the app to download models and allocate enough memory, add specific entitlements. Create an `.entitlements` file for your app with the following content:

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

> **Note:** The `com.apple.developer.kernel.increased-memory-limit` entitlement is crucial for running larger models, as it lets the app request more memory than usual.

## Step 4: Create the Chat Message Model

First, define a simple structure to represent chat messages:

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

## Step 5: Implement the ViewModel

Next, create the `PhiViewModel` class to handle model loading and inference:

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

The ViewModel highlights key MLX integration points:

- setting GPU cache limits with `MLX.GPU.set(cacheLimit:)`  
- using `LLMModelFactory` and `ModelContainer`  
- calling `MLXLMCommon.generate`  
- methods like `loadModel()` and `fetchAIResponse()`  
- referencing `ModelRegistry.phi3_5_4bit`, which points to a specific pre-converted MLX model that will be downloaded automatically:  

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

You can create your own model configurations to use any compatible model from Hugging Face. For example, to use Phi-4 mini instead, define your own configuration:

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

> **Note:** Phi-4 support was added to the MLX Swift Examples repo at the end of February 2025 (in [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). As of March 2025, the latest official release (2.21.2 from December 2024) does not include built-in Phi-4 support. To use Phi-4 models, you need to reference the package directly from the main branch:  
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

This lets you access the latest model configurations, including Phi-4, before they’re officially released. You can use this method to try different Phi versions or other models converted to MLX format.

## Step 6: Create the UI

Now, build a simple chat interface to interact with the view model:

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

The UI consists of three main parts working together to create a basic chat interface. `ContentView`, `MessageView`, and `TypingIndicatorView` provide a simple animated indicator showing the AI is processing.

## Step 7: Building and Running the App

You’re now ready to build and run the app.

> **Important!** MLX does not support the simulator. You must run the app on a physical Apple Silicon device. See [here](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) for details.

When the app launches, tap the "Load model" button to download and initialize the Phi-3 (or Phi-4, depending on your setup) model. This can take some time depending on your internet speed, as it downloads the model from Hugging Face. Our example shows a spinner during loading, but you can monitor progress in the Xcode console.

Once loaded, you can chat with the model by typing questions in the text field and tapping send.

Here’s how the app should behave running on an iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Conclusion

That’s it! By following these steps, you’ve built an iOS app that runs the Phi-3 (or Phi-4) model directly on device using Apple’s MLX framework.

Congratulations!

**Disclaimer**:  
Thi documont haz bin translaited yuuzing AI translaiton sarvis [Co-op Translator](https://github.com/Azure/co-op-translator). Whil wi striv for akyurasi, pleez bi awair that otomaytid translaitons mei contain erors or inakyerasis. Thi orijinal documont in its naytiv langwij shud bi konsiderd thi autoritativ sors. For kritikel informashon, profeshonal hyuman translaiton iz rekomendid. Wi ar not laybl for eni misandurstandings or misinterpretashons arising from thi yuuz of this translaiton.