# iOS ပေါ်တွင် Apple MLX Framework ဖြင့် Phi-3 နှင့် Phi-4 ကို ပြေးဆွဲခြင်း

ဤသင်ခန်းစာတွင် Apple MLX framework ကို အသုံးပြု၍ Phi-3 သို့မဟုတ် Phi-4 မော်ဒယ်ကို iOS စက်ပေါ်တွင် တိုက်ရိုက် ပြေးဆွဲနိုင်သော iOS အက်ပလီကေးရှင်းတစ်ခု ဖန်တီးနည်းကို ပြသထားသည်။ [MLX](https://opensource.apple.com/projects/mlx/) သည် Apple Silicon chip များအတွက် အထူးပြုထားသော Apple ၏ machine learning framework ဖြစ်သည်။

## လိုအပ်ချက်များ

- Xcode 16 (သို့မဟုတ် အထက်) ပါသော macOS
- iOS 18 (သို့မဟုတ် အထက်) ရှိပြီး အနည်းဆုံး 8GB RAM ပါသော iPhone သို့မဟုတ် iPad (Apple Intelligence လိုအပ်ချက်များနှင့် ကိုက်ညီသော စက်)
- Swift နှင့် SwiftUI အခြေခံ သိရှိမှု

## အဆင့် ၁: iOS Project အသစ် တည်ဆောက်ခြင်း

Xcode တွင် iOS project အသစ် တည်ဆောက်ခြင်းဖြင့် စတင်ပါ။

1. Xcode ကို ဖွင့်ပြီး "Create a new Xcode project" ကို ရွေးချယ်ပါ
2. "App" template ကို ရွေးပါ
3. Project အမည် (ဥပမာ - "Phi3-iOS-App") ထားပြီး SwiftUI ကို interface အဖြစ် ရွေးချယ်ပါ
4. Project ကို သိမ်းမည့် တည်နေရာကို ရွေးချယ်ပါ

## အဆင့် ၂: လိုအပ်သော Dependencies များ ထည့်သွင်းခြင်း

မော်ဒယ်များကို preload လုပ်ခြင်းနှင့် inference လုပ်ဆောင်ရန် လိုအပ်သော dependencies နှင့် helper များ ပါဝင်သော [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ကို ထည့်သွင်းပါ။

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

အခြေခံ [MLX Swift package](https://github.com/ml-explore/mlx-swift) သည် core tensor operations နှင့် အခြေခံ ML လုပ်ဆောင်ချက်များအတွက် လုံလောက်သော်လည်း၊ MLX Examples package သည် ဘာသာစကား မော်ဒယ်များနှင့် inference လုပ်ငန်းစဉ်ကို ပိုမိုလွယ်ကူစေရန် အပို components များ ပါဝင်သည်။

- Hugging Face မှ မော်ဒယ်များ ဒေါင်းလုပ်လုပ်ရန် အသုံးပြုသော model loading utilities
- tokenizer ပေါင်းစည်းမှု
- စာသားထုတ်လုပ်မှုအတွက် inference helpers
- ကြိုတင်ပြင်ဆင်ထားသော model သတ်မှတ်ချက်များ

## အဆင့် ၃: Entitlements များ ပြင်ဆင်ခြင်း

အက်ပလီကေးရှင်းမှ မော်ဒယ်များ ဒေါင်းလုပ်လုပ်ခြင်းနှင့် လုံလောက်သော memory ကို ခွင့်ပြုရန် အထူး entitlements များ ထည့်သွင်းရမည်ဖြစ်သည်။ သင့်အက်ပလီကေးရှင်းအတွက် `.entitlements` ဖိုင်ကို အောက်ပါအတိုင်း ဖန်တီးပါ။

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement သည် မော်ဒယ်အရွယ်အစားကြီးများကို ပြေးဆွဲရာတွင် အရေးကြီးသည်။ အက်ပလီကေးရှင်းအား ပုံမှန်ထက် ပိုမို memory တောင်းဆိုခွင့်ပြုသည်။

## အဆင့် ၄: Chat Message Model ဖန်တီးခြင်း

ပထမဦးဆုံး ကျွန်ုပ်တို့၏ chat message များကို ကိုယ်စားပြုရန် အခြေခံ structure တစ်ခု ဖန်တီးပါ။

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

## အဆင့် ၅: ViewModel ကို အကောင်အထည်ဖော်ခြင်း

နောက်တစ်ဆင့်တွင် မော်ဒယ် loading နှင့် inference ကို ကိုင်တွယ်မည့် `PhiViewModel` class ကို ဖန်တီးပါ။

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

ViewModel သည် MLX ပေါင်းစည်းမှုအချက်အလက် အဓိကများကို ပြသသည်။

- မိုဘိုင်းစက်များတွင် memory အသုံးပြုမှုကို အကောင်းဆုံးဖြစ်စေရန် `MLX.GPU.set(cacheLimit:)` ဖြင့် GPU cache ကန့်သတ်ချက်များ သတ်မှတ်ခြင်း
- `LLMModelFactory` ကို အသုံးပြု၍ မော်ဒယ်ကို လိုအပ်သလို ဒေါင်းလုပ်လုပ်ပြီး MLX အတွက် optimize လုပ်ထားသော မော်ဒယ်ကို စတင်ခြင်း
- `ModelContainer` မှတဆင့် မော်ဒယ်၏ parameter များနှင့် ဖွဲ့စည်းမှုကို ရယူခြင်း
- MLX ၏ token-by-token စာထုတ်လုပ်မှုကို `MLXLMCommon.generate` method ဖြင့် အသုံးပြုခြင်း
- temperature နှင့် token ကန့်သတ်ချက်များကို သင့်တော်စွာ စီမံကိန်းဆွဲ၍ inference လုပ်ငန်းစဉ်ကို စီမံခြင်း

streaming token ထုတ်လုပ်မှုနည်းလမ်းသည် မော်ဒယ်မှ စာသားထုတ်လုပ်သည့်အခါ အသုံးပြုသူများအား ချက်ချင်းတုံ့ပြန်မှု ပေးနိုင်သည်။ ၎င်းသည် server-based မော်ဒယ်များကဲ့သို့ token များကို streaming ဖြင့် ပြန်ပေးပို့သော်လည်း network request ၏ နောက်ကျမှု မရှိပါ။

UI အပြန်အလှန်ဆက်သွယ်မှုအတွက် အဓိက function နှစ်ခုမှာ `loadModel()` (LLM ကို စတင်ခြင်း) နှင့် `fetchAIResponse()` (အသုံးပြုသူ input ကို လက်ခံပြီး AI တုံ့ပြန်ချက် ထုတ်လုပ်ခြင်း) ဖြစ်သည်။

### မော်ဒယ်ဖော်မတ်ဆိုင်ရာ စဉ်းစားချက်များ

> **Important:** Phi မော်ဒယ်များကို MLX ၏ default သို့မဟုတ် GGUF ဖော်မတ်ဖြင့် မသုံးနိုင်ပါ။ MLX ဖော်မတ်သို့ ပြောင်းလဲထားရမည်ဖြစ်ပြီး ၎င်းကို MLX community မှ စီမံထားသည်။ ပြောင်းလဲပြီး မော်ဒယ်များကို [huggingface.co/mlx-community](https://huggingface.co/mlx-community) တွင် ရှာဖွေနိုင်သည်။

MLX Examples package တွင် Phi-3 အပါအဝင် မော်ဒယ်အချို့အတွက် ကြိုတင်ပြင်ဆင်ထားသော registration များ ပါဝင်သည်။ `ModelRegistry.phi3_5_4bit` ကို ခေါ်သည့်အခါ အလိုအလျောက် ဒေါင်းလုပ်လုပ်မည့် MLX ဖော်မတ်ပြောင်းလဲထားသော မော်ဒယ်တစ်ခုကို ရည်ညွှန်းသည်။

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

သင်သည် Hugging Face တွင် ရှိသည့် ကိုက်ညီသော မော်ဒယ် မည်သည့်မော်ဒယ်ကိုမဆို ရည်ညွှန်းရန် မိမိကိုယ်ပိုင် မော်ဒယ် configuration များ ဖန်တီးနိုင်သည်။ ဥပမာအားဖြင့် Phi-4 mini ကို အသုံးပြုလိုပါက မိမိ configuration ကို အောက်ပါအတိုင်း သတ်မှတ်နိုင်သည်။

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

> **Note:** Phi-4 အထောက်အပံ့ကို MLX Swift Examples repository တွင် 2025 ဖေဖော်ဝါရီလ အဆုံးတွင် ထည့်သွင်းခဲ့သည် ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))။ 2025 မတ်လအထိ December 2024 မှ ထွက်ရှိထားသော 2.21.2 official release တွင် Phi-4 အထောက်အပံ့ မပါဝင်သေးပါ။ Phi-4 မော်ဒယ်များကို အသုံးပြုရန်အတွက် main branch မှ package ကို တိုက်ရိုက် ရည်ညွှန်းရမည်ဖြစ်သည်။
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

ဤနည်းလမ်းဖြင့် Phi-4 အပါအဝင် နောက်ဆုံးမော်ဒယ် configuration များကို official release မထွက်မီ အသုံးပြုနိုင်သည်။ Phi မော်ဒယ် မျိုးစုံ သို့မဟုတ် MLX ဖော်မတ်သို့ ပြောင်းလဲထားသော အခြားမော်ဒယ်များကိုလည်း ဒီနည်းဖြင့် အသုံးပြုနိုင်သည်။

## အဆင့် ၆: UI ဖန်တီးခြင်း

ယခု ကျွန်ုပ်တို့၏ view model နှင့် ဆက်သွယ်ရန် ရိုးရှင်းသော chat interface တစ်ခုကို အကောင်အထည်ဖော်ပါ။

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

UI သည် အဓိက component သုံးခု ပါဝင်ပြီး အခြေခံ chat interface တစ်ခု ဖန်တီးရန် ပူးပေါင်းဆောင်ရွက်သည်။ `ContentView` သည် မော်ဒယ် ပြင်ဆင်မှုအခြေအနေအပေါ် မူတည်၍ loading button သို့မဟုတ် chat interface ကို ပြသသည့် two-state interface ဖြစ်သည်။ `MessageView` သည် အသုံးပြုသူ စာများ (ညာဘက် alignment၊ အပြာရောင် နောက်ခံ) နှင့် Phi မော်ဒယ် တုံ့ပြန်ချက်များ (ဘယ်ဘက် alignment၊ အမည်းရောင် နောက်ခံ) ကို ကွဲပြားစွာ ပြသသည်။ `TypingIndicatorView` သည် AI က အလုပ်လုပ်နေသည်ကို ပြသသည့် ရိုးရှင်းသော animation indicator ဖြစ်သည်။

## အဆင့် ၇: အက်ပလီကေးရှင်းကို တည်ဆောက်ပြီး ပြေးဆွဲခြင်း

ယခု အက်ပလီကေးရှင်းကို တည်ဆောက်ပြီး ပြေးဆွဲရန် အသင့်ဖြစ်ပါပြီ။

> **Important!** MLX သည် simulator ကို မထောက်ပံ့ပါ။ Apple Silicon chip ပါသော စက်တစ်လုံးပေါ်တွင်သာ အက်ပလီကေးရှင်းကို ပြေးဆွဲရမည်ဖြစ်သည်။ အသေးစိတ်အချက်အလက်များအတွက် [ဒီနေရာ](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) ကို ကြည့်ပါ။

အက်ပလီကေးရှင်း စတင်သောအခါ "Load model" ခလုတ်ကို နှိပ်၍ Phi-3 (သို့မဟုတ် သင့် configuration အရ Phi-4) မော်ဒယ်ကို ဒေါင်းလုပ်လုပ်ပြီး စတင်ပါ။ ၎င်းလုပ်ငန်းစဉ်သည် သင့်အင်တာနက် ချိတ်ဆက်မှုအရ အချိန်ယူနိုင်ပြီး Hugging Face မှ မော်ဒယ်ကို ဒေါင်းလုပ်လုပ်ခြင်း ပါဝင်သည်။ ကျွန်ုပ်တို့၏ အကောင်အထည်ဖော်မှုတွင် loading ကို ပြသရန် spinner တစ်ခုသာ ပါဝင်သော်လည်း Xcode console တွင် တကယ့် progress ကို ကြည့်ရှုနိုင်သည်။

မော်ဒယ် load ပြီးပါက စာသား ရိုက်ထည့်ရန် text field တွင် မေးခွန်းများ ရိုက်ထည့်ပြီး send ခလုတ်ကို နှိပ်၍ မော်ဒယ်နှင့် ဆက်သွယ်နိုင်ပါသည်။

ကျွန်ုပ်တို့၏ အက်ပလီကေးရှင်းသည် iPad Air M1 ပေါ်တွင် အောက်ပါအတိုင်း လည်ပတ်မည်ဖြစ်သည်။

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## နိဂုံးချုပ်

ဒါဆိုရင် အဆင့်ဆင့် လိုက်နာပြီး Apple ၏ MLX framework ကို အသုံးပြုကာ Phi-3 (သို့မဟုတ် Phi-4) မော်ဒယ်ကို iOS စက်ပေါ်တွင် တိုက်ရိုက် ပြေးဆွဲနိုင်သော အက်ပလီကေးရှင်းတစ်ခု ဖန်တီးနိုင်ခဲ့ပါပြီ။

ဂုဏ်ယူပါတယ်!

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။