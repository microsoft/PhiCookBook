<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07ca611437b569633d7aacf855ecaa7e",
  "translation_date": "2025-04-03T06:51:06+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference_MLX.md",
  "language_code": "ur"
}
-->
# iOS پر Apple MLX فریم ورک کے ساتھ Phi-3 اور Phi-4 چلانا

یہ ٹیوٹوریل دکھاتا ہے کہ کیسے ایک iOS ایپلیکیشن بنائی جائے جو Phi-3 یا Phi-4 ماڈل کو ڈیوائس پر چلائے، Apple MLX فریم ورک کا استعمال کرتے ہوئے۔ [MLX](https://opensource.apple.com/projects/mlx/) ایپل کا مشین لرننگ فریم ورک ہے جو ایپل سلیکون چپس کے لیے موزوں بنایا گیا ہے۔

## ضروریات

- macOS اور Xcode 16 (یا اس سے زیادہ)
- iOS 18 (یا اس سے زیادہ) کا ٹارگٹ ڈیوائس جس میں کم از کم 8GB ہو (ایپل انٹیلیجنس کی ضروریات کے مطابق آئی فون یا آئی پیڈ، کیونکہ یہ Phi کے کوانٹائزڈ ماڈلز کی ضروریات سے مماثل ہوں گے)
- Swift اور SwiftUI کی بنیادی معلومات

## مرحلہ 1: نیا iOS پروجیکٹ بنائیں

Xcode میں نیا iOS پروجیکٹ بنانے سے شروع کریں:

1. Xcode لانچ کریں اور "Create a new Xcode project" منتخب کریں۔
2. "App" کو بطور ٹیمپلیٹ منتخب کریں۔
3. اپنے پروجیکٹ کا نام رکھیں (مثلاً، "Phi3-iOS-App") اور SwiftUI کو بطور انٹرفیس منتخب کریں۔
4. اپنے پروجیکٹ کو محفوظ کرنے کے لیے ایک مقام منتخب کریں۔

## مرحلہ 2: ضروری ڈپینڈنسیز شامل کریں

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) شامل کریں، جو ماڈلز کو پری لوڈ کرنے اور انفیرنس کرنے کے لیے تمام ضروری ڈپینڈنسیز اور ہیلپرز فراہم کرتا ہے:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

جبکہ بنیادی [MLX Swift package](https://github.com/ml-explore/mlx-swift) بنیادی ٹینسر آپریشنز اور بنیادی ML فنکشنلٹی کے لیے کافی ہے، MLX Examples پیکیج کئی اضافی کمپوننٹس فراہم کرتا ہے جو لینگویج ماڈلز کے ساتھ کام کرنے کے لیے ڈیزائن کیے گئے ہیں اور انفیرنس کے عمل کو آسان بناتے ہیں:

- ماڈل لوڈنگ کی یوٹیلٹیز جو Hugging Face سے ڈاؤن لوڈنگ کو سنبھالتی ہیں۔
- ٹوکنائزر انٹیگریشن
- ٹیکسٹ جنریشن کے لیے انفیرنس ہیلپرز
- پہلے سے کنفیگرڈ ماڈل ڈیفینیشنز

## مرحلہ 3: اینٹائٹلمنٹس کنفیگر کریں

اپنی ایپ کو ماڈلز ڈاؤن لوڈ کرنے اور کافی میموری مختص کرنے کی اجازت دینے کے لیے مخصوص اینٹائٹلمنٹس شامل کریں۔ اپنی ایپ کے لیے ایک `.entitlements` فائل بنائیں جس میں درج ذیل مواد ہو:

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

> **نوٹ:** `com.apple.developer.kernel.increased-memory-limit` اینٹائٹلمنٹ بڑے ماڈلز چلانے کے لیے اہم ہے، کیونکہ یہ ایپ کو عام طور پر اجازت یافتہ سے زیادہ میموری کی درخواست کرنے کی اجازت دیتا ہے۔

## مرحلہ 4: چیٹ میسج ماڈل بنائیں

سب سے پہلے، آئیے اپنے چیٹ میسجز کی نمائندگی کرنے کے لیے ایک بنیادی اسٹرکچر بناتے ہیں:

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

## مرحلہ 5: ویو ماڈل نافذ کریں

اگلے مرحلے میں، ہم `PhiViewModel` کلاس بنائیں گے جو ماڈل لوڈنگ اور انفیرنس کو سنبھالے گی:

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

ویو ماڈل MLX انٹیگریشن کے اہم نکات کو ظاہر کرتا ہے:

- GPU کیش کی حد مقرر کرنا `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`، یہ ایک خاص پہلے سے کنورٹ شدہ MLX ماڈل کا حوالہ دیتا ہے جو خودکار طور پر ڈاؤن لوڈ ہو جائے گا:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

آپ اپنی ماڈل کنفیگریشنز بنا سکتے ہیں تاکہ Hugging Face پر کسی بھی موزوں ماڈل کی طرف اشارہ کیا جا سکے۔ مثال کے طور پر، Phi-4 mini استعمال کرنے کے لیے، آپ اپنی کنفیگریشن ڈیفائن کر سکتے ہیں:

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

> **نوٹ:** Phi-4 کی سپورٹ MLX Swift Examples ریپوزیٹری میں فروری 2025 کے آخر میں شامل کی گئی تھی (میں [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))۔ مارچ 2025 تک، تازہ ترین آفیشل ریلیز (دسمبر 2024 کی 2.21.2) میں Phi-4 کی بلٹ ان سپورٹ شامل نہیں ہے۔ Phi-4 ماڈلز استعمال کرنے کے لیے، آپ کو پیکیج کو براہ راست مین برانچ سے ریفرنس کرنا ہوگا:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

یہ آپ کو تازہ ترین ماڈل کنفیگریشنز تک رسائی فراہم کرتا ہے، بشمول Phi-4، اس سے پہلے کہ وہ کسی آفیشل ریلیز میں شامل ہوں۔ آپ اس طریقے کو مختلف ورژنز کے Phi ماڈلز یا دیگر ماڈلز کے ساتھ استعمال کر سکتے ہیں جو MLX فارمیٹ میں تبدیل کیے گئے ہوں۔

## مرحلہ 6: UI بنائیں

اب آئیے ایک سادہ چیٹ انٹرفیس نافذ کریں تاکہ ہمارے ویو ماڈل کے ساتھ تعامل کیا جا سکے:

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

UI تین اہم کمپوننٹس پر مشتمل ہے جو ایک بنیادی چیٹ انٹرفیس بنانے کے لیے مل کر کام کرتے ہیں۔ `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` ایک سادہ اینیمیٹڈ انڈیکیٹر فراہم کرتا ہے جو دکھاتا ہے کہ AI پراسیسنگ کر رہا ہے۔

## مرحلہ 7: ایپ بنائیں اور چلائیں

ہم اب ایپلیکیشن بنانے اور چلانے کے لیے تیار ہیں۔

> **اہم!** MLX سیمولیٹر کو سپورٹ نہیں کرتا۔ آپ کو ایپ کو ایپل سلیکون چپ والے فزیکل ڈیوائس پر چلانا ہوگا۔ مزید معلومات کے لیے [یہاں](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) دیکھیں۔

جب ایپ لانچ ہوتی ہے، "Load model" بٹن پر ٹیپ کریں تاکہ Phi-3 (یا، آپ کی کنفیگریشن کے مطابق، Phi-4) ماڈل کو ڈاؤن لوڈ اور انیشیئلائز کیا جا سکے۔ یہ عمل آپ کے انٹرنیٹ کنیکشن کی رفتار پر منحصر ہے، کیونکہ اس میں Hugging Face سے ماڈل ڈاؤن لوڈ کرنا شامل ہوتا ہے۔ ہماری امپلیمنٹیشن میں صرف ایک اسپنر شامل ہے جو لوڈنگ ظاہر کرتا ہے، لیکن آپ Xcode کنسول میں اصل پیش رفت دیکھ سکتے ہیں۔

ایک بار لوڈ ہو جانے کے بعد، آپ ماڈل کے ساتھ سوالات ٹائپ کر کے اور سینڈ بٹن پر ٹیپ کر کے تعامل کر سکتے ہیں۔

یہاں ہماری ایپلیکیشن کا رویہ دکھایا گیا ہے، جو iPad Air M1 پر چل رہی ہے:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## نتیجہ

اور بس! ان مراحل پر عمل کرتے ہوئے، آپ نے ایک iOS ایپلیکیشن بنائی ہے جو Phi-3 (یا Phi-4) ماڈل کو ایپل کے MLX فریم ورک کا استعمال کرتے ہوئے براہ راست ڈیوائس پر چلاتی ہے۔

مبارک ہو!

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم یہ جان لیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ذمہ دار نہیں ہیں۔