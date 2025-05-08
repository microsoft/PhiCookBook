<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-07T14:38:32+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "fa"
}
-->
# اجرای Phi-3 و Phi-4 روی iOS با چارچوب Apple MLX

این آموزش نحوه ساخت یک اپلیکیشن iOS را نشان می‌دهد که مدل Phi-3 یا Phi-4 را به صورت محلی روی دستگاه اجرا می‌کند، با استفاده از چارچوب Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) چارچوب یادگیری ماشینی اپل است که برای چیپ‌های Apple Silicon بهینه شده است.

## پیش‌نیازها

- macOS با Xcode 16 (یا بالاتر)
- دستگاه هدف iOS 18 (یا بالاتر) با حداقل ۸ گیگابایت حافظه (آیفون یا آیپدی که با نیازهای Apple Intelligence سازگار باشد، زیرا این نیازها مشابه نیازهای کوانتیزه‌شده Phi هستند)
- دانش پایه‌ای از Swift و SwiftUI

## مرحله ۱: ایجاد پروژه جدید iOS

با ایجاد یک پروژه جدید iOS در Xcode شروع کنید:

1. Xcode را باز کنید و گزینه "Create a new Xcode project" را انتخاب کنید
2. قالب "App" را انتخاب کنید
3. پروژه خود را نام‌گذاری کنید (مثلاً "Phi3-iOS-App") و SwiftUI را به عنوان رابط کاربری انتخاب کنید
4. محل ذخیره پروژه را انتخاب کنید

## مرحله ۲: افزودن وابستگی‌های لازم

بسته [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) را اضافه کنید که شامل تمام وابستگی‌ها و ابزارهای کمکی لازم برای بارگذاری پیش‌فرض مدل‌ها و انجام استنتاج است:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

در حالی که بسته پایه [MLX Swift package](https://github.com/ml-explore/mlx-swift) برای عملیات اصلی تنسور و عملکرد پایه یادگیری ماشین کافی است، بسته MLX Examples چندین مؤلفه اضافی ارائه می‌دهد که برای کار با مدل‌های زبانی و ساده‌تر کردن فرآیند استنتاج طراحی شده‌اند:

- ابزارهای بارگذاری مدل که دانلود از Hugging Face را مدیریت می‌کنند
- یکپارچه‌سازی توکنایزر
- ابزارهای کمکی برای تولید متن
- تعریف مدل‌های پیش‌پیکربندی شده

## مرحله ۳: پیکربندی مجوزها

برای اینکه اپ ما بتواند مدل‌ها را دانلود کند و حافظه کافی اختصاص دهد، باید مجوزهای خاصی اضافه کنیم. یک فایل `.entitlements` برای اپ خود با محتوای زیر بسازید:

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

> **Note:** مجوز `com.apple.developer.kernel.increased-memory-limit` برای اجرای مدل‌های بزرگ‌تر اهمیت دارد، زیرا به اپ اجازه می‌دهد حافظه بیشتری نسبت به حالت عادی درخواست کند.

## مرحله ۴: ایجاد مدل پیام چت

ابتدا یک ساختار ساده برای نمایش پیام‌های چت ایجاد می‌کنیم:

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

## مرحله ۵: پیاده‌سازی ViewModel

سپس کلاس `PhiViewModel` را ایجاد می‌کنیم که مسئول بارگذاری مدل و استنتاج است:

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

ViewModel نقاط کلیدی ادغام با MLX را نشان می‌دهد:

- تنظیم محدودیت کش GPU با `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit` که به یک مدل MLX خاص و پیش‌تبدیل شده اشاره می‌کند که به صورت خودکار دانلود می‌شود:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

شما می‌توانید تنظیمات مدل خود را بسازید تا به هر مدل سازگار در Hugging Face اشاره کند. به عنوان مثال، برای استفاده از Phi-4 mini، می‌توانید تنظیمات خود را به شکل زیر تعریف کنید:

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

> **Note:** پشتیبانی از Phi-4 در مخزن MLX Swift Examples در پایان فوریه ۲۰۲۵ اضافه شده است (در [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). تا مارس ۲۰۲۵، آخرین نسخه رسمی (2.21.2 از دسامبر ۲۰۲۴) شامل پشتیبانی داخلی Phi-4 نیست. برای استفاده از مدل‌های Phi-4 باید بسته را مستقیماً از شاخه اصلی فراخوانی کنید:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

این روش به شما امکان دسترسی به جدیدترین تنظیمات مدل‌ها، از جمله Phi-4، را قبل از قرار گرفتن در نسخه رسمی می‌دهد. می‌توانید از این روش برای استفاده از نسخه‌های مختلف مدل‌های Phi یا حتی مدل‌های دیگر که به فرمت MLX تبدیل شده‌اند، بهره ببرید.

## مرحله ۶: ایجاد رابط کاربری

اکنون یک رابط چت ساده برای تعامل با ViewModel خود پیاده‌سازی می‌کنیم:

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

رابط کاربری از سه بخش اصلی تشکیل شده که با هم یک رابط چت پایه را می‌سازند. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` یک نشانگر متحرک ساده برای نمایش پردازش AI ارائه می‌دهد.

## مرحله ۷: ساخت و اجرای اپ

اکنون آماده‌ایم که اپلیکیشن را بسازیم و اجرا کنیم.

> **Important!** چارچوب MLX شبیه‌ساز را پشتیبانی نمی‌کند. باید اپ را روی یک دستگاه فیزیکی با چیپ Apple Silicon اجرا کنید. برای اطلاعات بیشتر به [اینجا](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) مراجعه کنید.

وقتی اپ اجرا شد، روی دکمه "Load model" ضربه بزنید تا مدل Phi-3 (یا بسته به تنظیمات، Phi-4) دانلود و راه‌اندازی شود. این فرایند ممکن است بسته به سرعت اینترنت شما مدتی طول بکشد، چون مدل از Hugging Face دانلود می‌شود. در پیاده‌سازی ما فقط یک چرخنده برای نمایش بارگذاری وجود دارد، اما می‌توانید پیشرفت واقعی را در کنسول Xcode مشاهده کنید.

پس از بارگذاری، می‌توانید با تایپ سوالات در فیلد متن و زدن دکمه ارسال با مدل تعامل داشته باشید.

در اینجا نحوه عملکرد اپ ما را هنگام اجرا روی iPad Air M1 مشاهده می‌کنید:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## نتیجه‌گیری

همین بود! با دنبال کردن این مراحل، یک اپلیکیشن iOS ساختید که مدل Phi-3 (یا Phi-4) را مستقیماً روی دستگاه با استفاده از چارچوب MLX اپل اجرا می‌کند.

تبریک می‌گوییم!

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه ماشینی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.