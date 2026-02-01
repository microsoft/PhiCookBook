# iOS-এ Apple MLX ফ্রেমওয়ার্ক দিয়ে Phi-3 এবং Phi-4 চালানো

এই টিউটোরিয়ালে দেখানো হয়েছে কিভাবে Apple MLX ফ্রেমওয়ার্ক ব্যবহার করে একটি iOS অ্যাপ্লিকেশন তৈরি করা যায় যা Phi-3 বা Phi-4 মডেল ডিভাইসে চালাতে পারে। [MLX](https://opensource.apple.com/projects/mlx/) হলো Apple-এর মেশিন লার্নিং ফ্রেমওয়ার্ক যা Apple Silicon চিপের জন্য অপ্টিমাইজ করা হয়েছে।

## প্রয়োজনীয়তা

- macOS এবং Xcode 16 (বা তার উপরে)
- iOS 18 (বা তার উপরে) টার্গেট ডিভাইস, কমপক্ষে 8GB RAM সহ (Apple Intelligence এর প্রয়োজনীয়তার সাথে সামঞ্জস্যপূর্ণ iPhone বা iPad, যা প্রায়শই কোয়ান্টাইজড Phi মডেলের প্রয়োজনীয়তার মতো)
- Swift এবং SwiftUI এর মৌলিক জ্ঞান

## ধাপ ১: একটি নতুন iOS প্রজেক্ট তৈরি করুন

Xcode-তে একটি নতুন iOS প্রজেক্ট তৈরি করে শুরু করুন:

1. Xcode চালু করুন এবং "Create a new Xcode project" নির্বাচন করুন
2. টেমপ্লেট হিসেবে "App" নির্বাচন করুন
3. আপনার প্রজেক্টের নাম দিন (যেমন, "Phi3-iOS-App") এবং ইন্টারফেস হিসেবে SwiftUI নির্বাচন করুন
4. প্রজেক্ট সংরক্ষণের জন্য একটি লোকেশন নির্বাচন করুন

## ধাপ ২: প্রয়োজনীয় ডিপেন্ডেন্সি যোগ করুন

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) যোগ করুন, যা মডেল প্রিলোড এবং ইনফারেন্স করার জন্য প্রয়োজনীয় সব ডিপেন্ডেন্সি এবং হেল্পারস সরবরাহ করে:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

যদিও বেস [MLX Swift package](https://github.com/ml-explore/mlx-swift) কোর টেনসর অপারেশন এবং মৌলিক ML ফাংশনালিটির জন্য যথেষ্ট, MLX Examples প্যাকেজ ভাষা মডেলের সাথে কাজ করার জন্য এবং ইনফারেন্স প্রক্রিয়াকে সহজ করার জন্য অতিরিক্ত অনেক উপাদান দেয়:

- Hugging Face থেকে মডেল ডাউনলোড করার জন্য মডেল লোডিং ইউটিলিটি
- টোকেনাইজার ইন্টিগ্রেশন
- টেক্সট জেনারেশনের জন্য ইনফারেন্স হেল্পারস
- প্রি-কনফিগার্ড মডেল ডেফিনিশন

## ধাপ ৩: Entitlements কনফিগার করুন

আমাদের অ্যাপকে মডেল ডাউনলোড এবং পর্যাপ্ত মেমোরি বরাদ্দ করার অনুমতি দিতে, নির্দিষ্ট entitlements যোগ করতে হবে। আপনার অ্যাপের জন্য একটি `.entitlements` ফাইল তৈরি করুন নিচের বিষয়বস্তু সহ:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement বড় মডেল চালানোর জন্য গুরুত্বপূর্ণ, কারণ এটি অ্যাপকে সাধারণ অনুমতির চেয়ে বেশি মেমোরি চাওয়ার সুযোগ দেয়।

## ধাপ ৪: চ্যাট মেসেজ মডেল তৈরি করুন

প্রথমে, আমাদের চ্যাট মেসেজগুলো উপস্থাপনের জন্য একটি মৌলিক স্ট্রাকচার তৈরি করি:

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

এরপর, `PhiViewModel` ক্লাস তৈরি করব যা মডেল লোড এবং ইনফারেন্স পরিচালনা করবে:

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

- মোবাইল ডিভাইসে মেমোরি ব্যবহারের জন্য `MLX.GPU.set(cacheLimit:)` দিয়ে GPU ক্যাশ সীমা নির্ধারণ
- `LLMModelFactory` ব্যবহার করে মডেল অন-ডিমান্ড ডাউনলোড এবং MLX-অপ্টিমাইজড মডেল ইনিশিয়ালাইজ করা
- `ModelContainer` এর মাধ্যমে মডেলের প্যারামিটার এবং স্ট্রাকচার অ্যাক্সেস করা
- MLX এর টোকেন-বাই-টোকেন জেনারেশন `MLXLMCommon.generate` পদ্ধতির মাধ্যমে করা
- উপযুক্ত টেম্পারেচার সেটিংস এবং টোকেন সীমা দিয়ে ইনফারেন্স প্রক্রিয়া পরিচালনা

স্ট্রিমিং টোকেন জেনারেশন পদ্ধতি ব্যবহারকারীদের জন্য মডেল টেক্সট তৈরি করার সময় তাৎক্ষণিক ফিডব্যাক দেয়। এটি সার্ভার-ভিত্তিক মডেলের মতো, যেখানে টোকেনগুলো ব্যবহারকারীর কাছে স্ট্রিম করা হয়, তবে নেটওয়ার্ক লেটেন্সি ছাড়াই।

UI ইন্টারঅ্যাকশনের ক্ষেত্রে, দুটি মূল ফাংশন হলো `loadModel()`, যা LLM ইনিশিয়ালাইজ করে, এবং `fetchAIResponse()`, যা ব্যবহারকারীর ইনপুট প্রক্রিয়া করে AI রেসপন্স তৈরি করে।

### মডেল ফরম্যাট বিবেচনা

> **Important:** MLX এর জন্য Phi মডেলগুলো তাদের ডিফল্ট বা GGUF ফরম্যাটে ব্যবহার করা যায় না। এগুলো MLX ফরম্যাটে রূপান্তর করতে হয়, যা MLX কমিউনিটি পরিচালনা করে। আপনি প্রি-কনভার্টেড মডেলগুলো [huggingface.co/mlx-community](https://huggingface.co/mlx-community) থেকে পেতে পারেন।

MLX Examples প্যাকেজে Phi-3 সহ বেশ কয়েকটি মডেলের জন্য প্রি-কনফিগার্ড রেজিস্ট্রেশন রয়েছে। যখন আপনি `ModelRegistry.phi3_5_4bit` কল করবেন, এটি একটি নির্দিষ্ট প্রি-কনভার্টেড MLX মডেলকে রেফার করে যা স্বয়ংক্রিয়ভাবে ডাউনলোড হবে:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

আপনি আপনার নিজস্ব মডেল কনফিগারেশন তৈরি করে Hugging Face এর যেকোনো সামঞ্জস্যপূর্ণ মডেল নির্দেশ করতে পারেন। উদাহরণস্বরূপ, Phi-4 mini ব্যবহার করতে চাইলে, আপনি নিজস্ব কনফিগারেশন এভাবে তৈরি করতে পারেন:

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

> **Note:** Phi-4 সাপোর্ট MLX Swift Examples রিপোজিটরিতে ফেব্রুয়ারি ২০২৫ এর শেষের দিকে যোগ করা হয়েছে ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))। মার্চ ২০২৫ পর্যন্ত, সর্বশেষ অফিসিয়াল রিলিজ (ডিসেম্বর ২০২৪ এর 2.21.2) এ Phi-4 সাপোর্ট অন্তর্ভুক্ত নয়। Phi-4 মডেল ব্যবহার করতে হলে আপনাকে প্যাকেজটি সরাসরি মেইন ব্রাঞ্চ থেকে রেফারেন্স করতে হবে:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

এটি আপনাকে অফিসিয়াল রিলিজের আগে সর্বশেষ মডেল কনফিগারেশন, যার মধ্যে Phi-4 রয়েছে, ব্যবহারের সুযোগ দেয়। এই পদ্ধতি ব্যবহার করে আপনি Phi মডেলের বিভিন্ন সংস্করণ বা MLX ফরম্যাটে রূপান্তরিত অন্য মডেলও ব্যবহার করতে পারেন।

## ধাপ ৬: UI তৈরি করুন

এখন আমাদের ভিউ মডেলের সাথে ইন্টারঅ্যাক্ট করার জন্য একটি সহজ চ্যাট ইন্টারফেস তৈরি করি:

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

UI তিনটি প্রধান উপাদান নিয়ে গঠিত যা একসাথে একটি মৌলিক চ্যাট ইন্টারফেস তৈরি করে। `ContentView` একটি দুই-স্টেট ইন্টারফেস তৈরি করে যা মডেল প্রস্তুত না হলে লোডিং বাটন এবং প্রস্তুত হলে চ্যাট ইন্টারফেস দেখায়। `MessageView` ব্যবহারকারীর মেসেজ (ডানদিকে সজ্জিত, নীল ব্যাকগ্রাউন্ড) এবং Phi মডেলের রেসপন্স (বামদিকে সজ্জিত, ধূসর ব্যাকগ্রাউন্ড) আলাদা ভাবে রেন্ডার করে। `TypingIndicatorView` একটি সহজ অ্যানিমেটেড ইন্ডিকেটর প্রদান করে যা দেখায় AI প্রক্রিয়াকরণ করছে।

## ধাপ ৭: অ্যাপ বিল্ড এবং রান করা

এখন আমরা অ্যাপ্লিকেশন বিল্ড এবং রান করার জন্য প্রস্তুত।

> **Important!** MLX সিমুলেটর সাপোর্ট করে না। আপনাকে অবশ্যই Apple Silicon চিপযুক্ত একটি ফিজিক্যাল ডিভাইসে অ্যাপ চালাতে হবে। বিস্তারিত জানতে দেখুন [এখানে](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)।

অ্যাপ চালু হলে, "Load model" বাটনে ট্যাপ করুন Phi-3 (অথবা আপনার কনফিগারেশনের উপর নির্ভর করে Phi-4) মডেল ডাউনলোড এবং ইনিশিয়ালাইজ করার জন্য। ইন্টারনেট সংযোগের উপর নির্ভর করে এই প্রক্রিয়াটি কিছু সময় নিতে পারে, কারণ এটি Hugging Face থেকে মডেল ডাউনলোড করে। আমাদের ইমপ্লিমেন্টেশনে শুধুমাত্র একটি স্পিনার রয়েছে লোডিং নির্দেশ করার জন্য, তবে আপনি Xcode কনসোলে প্রকৃত প্রগ্রেস দেখতে পারবেন।

লোড হয়ে গেলে, আপনি টেক্সট ফিল্ডে প্রশ্ন টাইপ করে এবং সেন্ড বাটনে ট্যাপ করে মডেলের সাথে ইন্টারঅ্যাক্ট করতে পারবেন।

এখানে iPad Air M1-এ চলমান আমাদের অ্যাপ্লিকেশনের আচরণ কেমন হওয়া উচিত তার একটি ডেমো GIF:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## উপসংহার

এটাই সব! এই ধাপগুলো অনুসরণ করে আপনি একটি iOS অ্যাপ্লিকেশন তৈরি করেছেন যা Apple-এর MLX ফ্রেমওয়ার্ক ব্যবহার করে সরাসরি ডিভাইসে Phi-3 (বা Phi-4) মডেল চালাতে পারে।

অভিনন্দন!

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।