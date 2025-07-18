<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:27:39+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "ur"
}
-->
# iOS پر Apple MLX فریم ورک کے ساتھ Phi-3 اور Phi-4 چلانا

یہ ٹیوٹوریل دکھاتا ہے کہ کیسے ایک iOS ایپلیکیشن بنائی جائے جو Apple MLX فریم ورک استعمال کرتے ہوئے Phi-3 یا Phi-4 ماڈل کو ڈیوائس پر چلا سکے۔ [MLX](https://opensource.apple.com/projects/mlx/) ایپل کا مشین لرننگ فریم ورک ہے جو Apple Silicon چپس کے لیے بہتر بنایا گیا ہے۔

## ضروریات

- macOS جس میں Xcode 16 (یا اس سے جدید) ہو
- iOS 18 (یا اس سے جدید) ہدف ڈیوائس جس میں کم از کم 8GB میموری ہو (ایسا iPhone یا iPad جو Apple Intelligence کی ضروریات کو پورا کرتا ہو، کیونکہ یہ quantized Phi کی ضروریات کے مشابہ ہوں گے)
- Swift اور SwiftUI کی بنیادی معلومات

## مرحلہ 1: نیا iOS پروجیکٹ بنائیں

Xcode میں نیا iOS پروجیکٹ بنانے سے شروع کریں:

1. Xcode کھولیں اور "Create a new Xcode project" منتخب کریں  
2. "App" ٹیمپلیٹ منتخب کریں  
3. اپنے پروجیکٹ کا نام رکھیں (مثلاً "Phi3-iOS-App") اور انٹرفیس کے طور پر SwiftUI منتخب کریں  
4. پروجیکٹ کو محفوظ کرنے کے لیے جگہ منتخب کریں  

## مرحلہ 2: مطلوبہ dependencies شامل کریں

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) شامل کریں جس میں ماڈلز کو پری لوڈ کرنے اور inference کرنے کے لیے تمام ضروری dependencies اور مددگار کوڈ موجود ہے:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

اگرچہ بنیادی [MLX Swift package](https://github.com/ml-explore/mlx-swift) کور ٹینسر آپریشنز اور بنیادی ML فعالیت کے لیے کافی ہے، MLX Examples package کئی اضافی اجزاء فراہم کرتا ہے جو زبان کے ماڈلز کے ساتھ کام کرنے اور inference کے عمل کو آسان بنانے کے لیے بنائے گئے ہیں:

- ماڈل لوڈ کرنے کے لیے utilities جو Hugging Face سے ڈاؤن لوڈنگ کو سنبھالتے ہیں  
- tokenizer انٹیگریشن  
- ٹیکسٹ جنریشن کے لیے inference helpers  
- پہلے سے ترتیب دی گئی ماڈل کی تعریفیں  

## مرحلہ 3: Entitlements ترتیب دیں

اپنی ایپ کو ماڈلز ڈاؤن لوڈ کرنے اور مناسب میموری مختص کرنے کی اجازت دینے کے لیے مخصوص entitlements شامل کریں۔ اپنی ایپ کے لیے `.entitlements` فائل بنائیں جس میں درج ذیل مواد ہو:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement بڑے ماڈلز چلانے کے لیے اہم ہے کیونکہ یہ ایپ کو معمول سے زیادہ میموری مانگنے کی اجازت دیتا ہے۔

## مرحلہ 4: Chat Message ماڈل بنائیں

سب سے پہلے، ایک بنیادی ساخت بنائیں جو ہمارے چیٹ پیغامات کی نمائندگی کرے:

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

## مرحلہ 5: ViewModel نافذ کریں

اب، `PhiViewModel` کلاس بنائیں جو ماڈل لوڈنگ اور inference کو سنبھالے:

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

ViewModel MLX انٹیگریشن کے اہم نکات دکھاتا ہے:

- موبائل ڈیوائسز پر میموری کے استعمال کو بہتر بنانے کے لیے `MLX.GPU.set(cacheLimit:)` کے ذریعے GPU کیش کی حد مقرر کرنا  
- `LLMModelFactory` کا استعمال کرتے ہوئے ماڈل کو ضرورت کے مطابق ڈاؤن لوڈ کرنا اور MLX کے لیے بہتر ماڈل کو initialize کرنا  
- `ModelContainer` کے ذریعے ماڈل کے پیرامیٹرز اور ساخت تک رسائی  
- MLX کی token-by-token جنریشن کو `MLXLMCommon.generate` میتھڈ کے ذریعے استعمال کرنا  
- مناسب temperature سیٹنگز اور token limits کے ساتھ inference کے عمل کو منظم کرنا  

اسٹریمنگ ٹوکن جنریشن کا طریقہ صارفین کو فوری فیڈبیک دیتا ہے جب ماڈل متن تیار کرتا ہے۔ یہ سرور پر مبنی ماڈلز کی طرح ہے جو ٹوکنز کو صارف کو اسٹریمنگ کرتے ہیں، مگر نیٹ ورک کی تاخیر کے بغیر۔

UI تعامل کے لحاظ سے، دو اہم فنکشنز ہیں: `loadModel()` جو LLM کو initialize کرتا ہے، اور `fetchAIResponse()` جو صارف کے ان پٹ کو پراسیس کر کے AI جوابات تیار کرتا ہے۔

### ماڈل فارمیٹ کے حوالے سے غور و فکر

> **Important:** MLX کے لیے Phi ماڈلز کو ان کے ڈیفالٹ یا GGUF فارمیٹ میں استعمال نہیں کیا جا سکتا۔ انہیں MLX فارمیٹ میں تبدیل کرنا ضروری ہے، جو MLX کمیونٹی کے ذریعے کیا جاتا ہے۔ آپ پہلے سے تبدیل شدہ ماڈلز [huggingface.co/mlx-community](https://huggingface.co/mlx-community) پر حاصل کر سکتے ہیں۔

MLX Examples package میں کئی ماڈلز کے لیے پہلے سے ترتیب دی گئی رجسٹریشنز شامل ہیں، جن میں Phi-3 بھی شامل ہے۔ جب آپ `ModelRegistry.phi3_5_4bit` کال کرتے ہیں، تو یہ ایک مخصوص پہلے سے تبدیل شدہ MLX ماڈل کی طرف اشارہ کرتا ہے جو خود بخود ڈاؤن لوڈ ہو جائے گا:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

آپ اپنی مرضی کے مطابق ماڈل کنفیگریشنز بھی بنا سکتے ہیں جو Hugging Face پر کسی بھی مطابقت رکھنے والے ماڈل کی طرف اشارہ کریں۔ مثال کے طور پر، اگر آپ Phi-4 mini استعمال کرنا چاہتے ہیں تو آپ اپنی کنفیگریشن یوں بنا سکتے ہیں:

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

> **Note:** Phi-4 کی سپورٹ MLX Swift Examples ریپوزیٹری میں فروری 2025 کے آخر میں شامل کی گئی تھی ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))۔ مارچ 2025 تک، دسمبر 2024 کی تازہ ترین آفیشل ریلیز (2.21.2) میں Phi-4 کی بلٹ ان سپورٹ شامل نہیں ہے۔ Phi-4 ماڈلز استعمال کرنے کے لیے آپ کو پیکیج کو مین برانچ سے براہ راست ریفرنس کرنا ہوگا:  
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

اس سے آپ کو تازہ ترین ماڈل کنفیگریشنز تک رسائی ملتی ہے، بشمول Phi-4، اس سے پہلے کہ وہ کسی آفیشل ریلیز میں شامل ہوں۔ آپ اس طریقے سے مختلف ورژنز کے Phi ماڈلز یا دیگر ماڈلز جو MLX فارمیٹ میں تبدیل کیے گئے ہوں، استعمال کر سکتے ہیں۔

## مرحلہ 6: UI بنائیں

اب ایک سادہ چیٹ انٹرفیس بنائیں تاکہ ہمارے ویو ماڈل کے ساتھ بات چیت کی جا سکے:

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

UI تین اہم اجزاء پر مشتمل ہے جو مل کر ایک بنیادی چیٹ انٹرفیس بناتے ہیں۔ `ContentView` دو حالتوں والا انٹرفیس بناتا ہے جو ماڈل کی تیاری کے مطابق یا تو لوڈنگ بٹن دکھاتا ہے یا چیٹ انٹرفیس۔ `MessageView` انفرادی چیٹ پیغامات کو مختلف انداز میں دکھاتا ہے، صارف کے پیغامات (دائیں جانب سیدھے، نیلے پس منظر کے ساتھ) اور Phi ماڈل کے جوابات (بائیں جانب سیدھے، سرمئی پس منظر کے ساتھ)۔ `TypingIndicatorView` ایک سادہ متحرک اشارہ فراہم کرتا ہے جو ظاہر کرتا ہے کہ AI پروسیسنگ کر رہا ہے۔

## مرحلہ 7: ایپ بنائیں اور چلائیں

اب ہم ایپلیکیشن کو بنانے اور چلانے کے لیے تیار ہیں۔

> **Important!** MLX سیمولیٹر کی حمایت نہیں کرتا۔ آپ کو ایپ کو Apple Silicon چپ والے حقیقی ڈیوائس پر چلانا ہوگا۔ مزید معلومات کے لیے [یہاں](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) دیکھیں۔

جب ایپ شروع ہو، تو "Load model" بٹن پر ٹیپ کریں تاکہ Phi-3 (یا آپ کی کنفیگریشن کے مطابق Phi-4) ماڈل ڈاؤن لوڈ اور initialize ہو جائے۔ یہ عمل آپ کے انٹرنیٹ کنکشن کے مطابق کچھ وقت لے سکتا ہے کیونکہ ماڈل Hugging Face سے ڈاؤن لوڈ ہو رہا ہوتا ہے۔ ہماری امپلیمنٹیشن میں صرف لوڈنگ کا سپنر شامل ہے، لیکن آپ Xcode کنسول میں اصل پیش رفت دیکھ سکتے ہیں۔

ماڈل لوڈ ہونے کے بعد، آپ ٹیکسٹ فیلڈ میں سوالات ٹائپ کر کے اور بھیجنے کے بٹن پر ٹیپ کر کے ماڈل کے ساتھ بات چیت کر سکتے ہیں۔

یہ ہے کہ ہماری ایپلیکیشن iPad Air M1 پر کیسے کام کرے گی:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## نتیجہ

بس یہی تھا! ان مراحل پر عمل کرتے ہوئے، آپ نے ایک iOS ایپلیکیشن بنائی ہے جو Apple کے MLX فریم ورک کا استعمال کرتے ہوئے Phi-3 (یا Phi-4) ماڈل کو براہ راست ڈیوائس پر چلاتی ہے۔

مبارک ہو!

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔