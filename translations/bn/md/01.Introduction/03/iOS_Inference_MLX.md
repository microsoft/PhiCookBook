<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:08:22+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "bn"
}
-->
# iOS-এ Apple MLX Framework দিয়ে Phi-3 এবং Phi-4 চালানো

এই টিউটোরিয়ালে দেখানো হয়েছে কীভাবে Apple MLX ফ্রেমওয়ার্ক ব্যবহার করে iOS অ্যাপে Phi-3 বা Phi-4 মডেল ডিভাইসে চালানো যায়। [MLX](https://opensource.apple.com/projects/mlx/) হল Apple-এর মেশিন লার্নিং ফ্রেমওয়ার্ক যা Apple Silicon চিপের জন্য অপ্টিমাইজড।

## প্রয়োজনীয়তা

- macOS এবং Xcode 16 (বা তার উপরে)
- iOS 18 (বা তার উপরে) টার্গেট ডিভাইস যার RAM কমপক্ষে ৮GB (Apple Intelligence-এর জন্য উপযুক্ত iPhone বা iPad, যা প্রায়শই quantized Phi-এর চাহিদার মতো)
- Swift এবং SwiftUI-এর বেসিক জ্ঞান

## ধাপ ১: একটি নতুন iOS প্রজেক্ট তৈরি করুন

Xcode-তে একটি নতুন iOS প্রজেক্ট তৈরি করে শুরু করুন:

1. Xcode চালু করুন এবং "Create a new Xcode project" নির্বাচন করুন
2. টেমপ্লেট হিসেবে "App" বেছে নিন
3. আপনার প্রজেক্টের নাম দিন (যেমন, "Phi3-iOS-App") এবং ইন্টারফেস হিসেবে SwiftUI নির্বাচন করুন
4. প্রজেক্ট সংরক্ষণের জন্য একটি লোকেশন বেছে নিন

## ধাপ ২: প্রয়োজনীয় ডিপেন্ডেন্সি যোগ করুন

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) যোগ করুন, যা মডেল প্রিলোড এবং ইনফারেন্সের জন্য প্রয়োজনীয় সব ডিপেন্ডেন্সি ও হেল্পারস সরবরাহ করে:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

যদিও বেস [MLX Swift package](https://github.com/ml-explore/mlx-swift) মূল টেনসর অপারেশন এবং মৌলিক ML ফাংশনালিটির জন্য যথেষ্ট, MLX Examples প্যাকেজ ভাষা মডেলের জন্য বিশেষ কিছু অতিরিক্ত কম্পোনেন্ট দেয় এবং ইনফারেন্স প্রক্রিয়াকে সহজ করে:

- Hugging Face থেকে ডাউনলোডের জন্য মডেল লোডিং ইউটিলিটি
- টোকেনাইজার ইন্টিগ্রেশন
- টেক্সট জেনারেশনের জন্য ইনফারেন্স হেল্পারস
- প্রি-কনফিগার্ড মডেল ডেফিনিশন

## ধাপ ৩: Entitlements কনফিগার করুন

আমাদের অ্যাপকে মডেল ডাউনলোড করার এবং পর্যাপ্ত মেমরি বরাদ্দ করার অনুমতি দিতে হবে, এজন্য নির্দিষ্ট entitlements যোগ করতে হবে। আপনার অ্যাপের জন্য একটি `.entitlements` ফাইল তৈরি করুন নিচের কন্টেন্ট দিয়ে:

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

> **Note:** বড় মডেল চালানোর জন্য `com.apple.developer.kernel.increased-memory-limit` entitlement গুরুত্বপূর্ণ, কারণ এটি অ্যাপকে স্বাভাবিকের চেয়ে বেশি মেমরি চাওয়ার অনুমতি দেয়।

## ধাপ ৪: Chat Message মডেল তৈরি করুন

প্রথমে, আমাদের চ্যাট মেসেজগুলো উপস্থাপনের জন্য একটি বেসিক স্ট্রাকচার তৈরি করি:

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

## ধাপ ৫: ViewModel ইমপ্লিমেন্ট করুন

এরপর, `PhiViewModel` ক্লাস তৈরি করব যা মডেল লোডিং এবং ইনফারেন্স পরিচালনা করবে:

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

ViewModel-এ MLX ইন্টিগ্রেশনের মূল পয়েন্টগুলো দেখানো হয়েছে:

- `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit` দিয়ে GPU ক্যাশ সীমা নির্ধারণ, এটি একটি নির্দিষ্ট প্রি-কনভার্টেড MLX মডেল রেফার করে যা স্বয়ংক্রিয়ভাবে ডাউনলোড হবে:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

আপনি নিজের মডেল কনফিগারেশন তৈরি করে Hugging Face-এর যেকোনো উপযুক্ত মডেলের দিকে পয়েন্ট করতে পারেন। উদাহরণস্বরূপ, Phi-4 mini ব্যবহার করতে চাইলে নিজের কনফিগারেশন এভাবে তৈরি করতে পারেন:

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

> **Note:** Phi-4 সাপোর্ট MLX Swift Examples রিপোজিটরিতে ফেব্রুয়ারি ২০২৫-এর শেষে যোগ করা হয়েছে ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))। মার্চ ২০২৫ পর্যন্ত, ডিসেম্বরে ২০২৪-এর অফিসিয়াল সর্বশেষ রিলিজ (2.21.2) এ Phi-4 সাপোর্ট অন্তর্ভুক্ত নেই। Phi-4 মডেল ব্যবহারের জন্য আপনাকে মেইন ব্রাঞ্চ থেকে সরাসরি প্যাকেজ রেফারেন্স করতে হবে:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

এভাবে আপনি অফিসিয়াল রিলিজের আগে সর্বশেষ মডেল কনফিগারেশন, যেমন Phi-4, ব্যবহার করতে পারবেন। একই পদ্ধতিতে Phi মডেলের বিভিন্ন ভার্সন বা MLX ফরম্যাটে রূপান্তরিত অন্য মডেলও ব্যবহার করা সম্ভব।

## ধাপ ৬: UI তৈরি করুন

এখন আমাদের ViewModel-এর সাথে ইন্টারঅ্যাকশনের জন্য একটি সহজ চ্যাট ইন্টারফেস তৈরি করি:

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

UI-তে তিনটি প্রধান কম্পোনেন্ট আছে যা মিলে একটি বেসিক চ্যাট ইন্টারফেস তৈরি করে। `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` একটি সহজ অ্যানিমেটেড ইন্ডিকেটর দেয় যা দেখায় AI প্রক্রিয়াকরণ করছে।

## ধাপ ৭: অ্যাপ বিল্ড এবং রান করা

এখন অ্যাপ্লিকেশন বিল্ড এবং চালানোর জন্য প্রস্তুত।

> **Important!** MLX সিমুলেটর সাপোর্ট করে না। অ্যাপটি অবশ্যই Apple Silicon চিপযুক্ত ফিজিক্যাল ডিভাইসে চালাতে হবে। বিস্তারিত জানতে দেখুন [এখানে](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)।

অ্যাপ চালু হলে, "Load model" বাটনে ট্যাপ করুন Phi-3 (অথবা আপনার কনফিগারেশনের ওপর নির্ভর করে Phi-4) মডেল ডাউনলোড এবং ইনিশিয়ালাইজ করার জন্য। ইন্টারনেট সংযোগের উপর নির্ভর করে এই প্রক্রিয়াটি কিছু সময় নিতে পারে, কারণ মডেলটি Hugging Face থেকে ডাউনলোড হচ্ছে। আমাদের ইমপ্লিমেন্টেশনে লোডিং নির্দেশ করতে একটি স্পিনার রয়েছে, তবে প্রকৃত প্রগ্রেস Xcode কনসোলে দেখা যাবে।

লোড হয়ে গেলে, আপনি টেক্সট ফিল্ডে প্রশ্ন টাইপ করে এবং সেন্ড বাটনে ট্যাপ করে মডেলের সাথে ইন্টারঅ্যাক্ট করতে পারবেন।

এখানে iPad Air M1-এ চলমান আমাদের অ্যাপ্লিকেশনের আচরণ দেখানো হয়েছে:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## উপসংহার

এতটুকুই! এই ধাপগুলো অনুসরণ করে আপনি Apple-এর MLX ফ্রেমওয়ার্ক ব্যবহার করে সরাসরি ডিভাইসে Phi-3 (বা Phi-4) মডেল চালানো একটি iOS অ্যাপ তৈরি করেছেন।

অভিনন্দন!

**অস্বীকারোক্তি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বতন্ত্র ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।