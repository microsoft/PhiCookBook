<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-12-22T00:50:52+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "pcm"
}
-->
# How to run Phi-3 and Phi-4 for iOS wit Apple MLX Framework

Dis tutorial dey show how to create an iOS application wey go run the Phi-3 or Phi-4 model on-device, using the Apple MLX framework. [MLX](https://opensource.apple.com/projects/mlx/) na Apple's machine learning framework wey dem optimize for Apple Silicon chips.

## Wetin you need

- macOS wey get Xcode 16 (or higher)
- iOS 18 (or higher) target device wey get at least 8GB (iPhone or iPad wey dey compatible with Apple Intelligence requirements, as those go be similar to the quantized Phi requirements)
- basic sabi for Swift and SwiftUI

## Step 1: Make a New iOS Project

Start by create new iOS project for Xcode:

1. open Xcode and select "Create a new Xcode project"
2. choose "App" as the template
3. name your project (e.g., "Phi3-iOS-App") and select SwiftUI as the interface
4. choose a location to save your project

## Step 2: Add Required Dependencies

Add the [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) wey get all the necessary dependencies and helpers for preloading models and for performing inference:

```swift
// For Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

While the base [MLX Swift package](https://github.com/ml-explore/mlx-swift) go fit do core tensor operations and basic ML functionality, the MLX Examples package dey provide extra components wey dem design for working with language models, make inference process easier:

- model loading utilities wey dey handle downloading from Hugging Face
- tokenizer integration
- inference helpers for text generation
- pre-configured model definitions

## Step 3: Configure Entitlements

To make our app fit download models and allocate enough memory, we need to add specific entitlements. Create an `.entitlements` file for your app wit di following content:

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

> **Note:** The `com.apple.developer.kernel.increased-memory-limit` entitlement dey important to run bigger models, because e allow the app to request more memory pass wetin dem normally permit.

## Step 4: Create the Chat Message Model

First, make we create a basic structure to represent our chat messages:

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

Next, we go create the `PhiViewModel` class wey dey handle model loading and inference:

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
            
            // Phi 3.5 mini don set up already for Swift MLX Examples
            let modelConfig = ModelRegistry.phi3_5_4bit
            
            // Phi 4 mini fit comot for Hugging Face, but you go need reference Swift MLX Examples from the main branch
            //let modelConfig = ModelConfiguration(
            //    id: "mlx-community/Phi-4-mini-instruct-4bit",
            //    defaultPrompt: "You be helpful assistant."
            //    extraEOSTokens: ["<|end|>"]
            //)
            
            print("Loading \(modelConfig.name)...")
            self.modelContainer = try await LLMModelFactory.shared.loadContainer(
                configuration: modelConfig
            ) { progress in
                print("Download progress: \(Int(progress.fractionCompleted * 100))%")
            }
            
            // Make log for model parameters
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

Di ViewModel dey show the important MLX integration points:

- setting GPU cache limits with `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with correct temperature settings and token limits

The streaming token generation approach dey give immediate feedback to users as the model dey generate text. E be like how server-based models dey work — dem dey stream tokens back to the user — but without the network latency.

For UI interaction, di two important functions na `loadModel()`, wey dey initialize the LLM, and `fetchAIResponse()`, wey dey process user input and generate AI responses.

### Model format considerations

> **Important:** Phi models for MLX no fit dey used in their default or GGUF format. Dem must convert dem to the MLX format, and di MLX community dey handle dat. You fit find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Di MLX Examples package include pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, e dey reference a specific pre-converted MLX model wey go automatically download:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

You fit create your own model configurations to point to any compatible model on Hugging Face. For example, if you wan use Phi-4 mini instead, you fit define your own configuration:

```swift
let phi4_mini_4bit = ModelConfiguration(
    id: "mlx-community/Phi-4-mini-instruct-4bit",
    defaultPrompt: "Explain quantum computing in simple terms.",
    extraEOSTokens: ["<|end|>"]
)

// Den use dis configuration wen you dey load di model
self.modelContainer = try await LLMModelFactory.shared.loadContainer(
    configuration: phi4_mini_4bit
) { progress in
    print("Download progress: \(Int(progress.fractionCompleted * 100))%")
}
```

> **Note:** Phi-4 support add for the MLX Swift Examples repository for the end of February 2025 (for [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). As of March 2025, the latest official release (2.21.2 from December 2024) no include built-in Phi-4 support. To use Phi-4 models, you go need reference the package directly from the main branch:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Dis one go give you access to the latest model configurations, including Phi-4, before dem put am inside official release. You fit use this approach to use different versions of Phi models or even other models wey don convert to the MLX format.

## Step 6: Create the UI

Make we now implement simple chat interface to interact with our view model:

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

Di UI get three main components wey dey work together to create basic chat interface. `ContentView` dey create two-state interface wey go either show loading button or di chat interface depending on model readiness. `MessageView` dey render individual chat messages different based on whether na user message (right-aligned, blue background) or Phi model response (left-aligned, gray background). `TypingIndicatorView` dey provide simple animated indicator to show say the AI dey process.

## Step 7: Building and Running the App

We don ready to build and run the application now.

> **Important!** MLX no support the simulator. You must run the app for physical device wey get Apple Silicon chip. See [here](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) for more information.

When the app launch, tap the "Load model" button to download and initialize the Phi-3 (or, depending on your configuration, Phi-4) model. Dis process fit take small time depending on your internet connection, because e involve downloading the model from Hugging Face. Our implementation get only spinner to show loading, but you fit see the actual progress for the Xcode console.

Once e load, you fit interact with the model by typing questions for the text field and tapping the send button.

Here na how our application suppose behave, running on iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Conclusion

Na so e be! If you follow these steps, you don create iOS application wey fit run the Phi-3 (or Phi-4) model directly on device using Apple's MLX framework.

Congratulations!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Make una note:

Dis document don translate by AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automatic translations fit get errors or inaccuracy. The original document for im own language na di correct/official one wey you suppose trust. If na important information, better make professional human translator check am. We no go responsible for any misunderstanding or wrong interpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->