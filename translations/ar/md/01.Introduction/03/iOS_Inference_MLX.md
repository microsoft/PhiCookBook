<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:27:09+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "ar"
}
-->
# تشغيل Phi-3 و Phi-4 على iOS باستخدام إطار عمل Apple MLX

يوضح هذا الدليل كيفية إنشاء تطبيق iOS يقوم بتشغيل نموذج Phi-3 أو Phi-4 على الجهاز، باستخدام إطار عمل Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) هو إطار عمل تعلم آلي من Apple مُحسّن لمعالجات Apple Silicon.

## المتطلبات الأساسية

- نظام macOS مع Xcode 16 (أو أحدث)
- جهاز iOS 18 (أو أحدث) مستهدف بسعة ذاكرة لا تقل عن 8 جيجابايت (iPhone أو iPad متوافق مع متطلبات Apple Intelligence، حيث تكون مشابهة لمتطلبات Phi المكممة)
- معرفة أساسية بـ Swift و SwiftUI

## الخطوة 1: إنشاء مشروع iOS جديد

ابدأ بإنشاء مشروع iOS جديد في Xcode:

1. افتح Xcode واختر "Create a new Xcode project"
2. اختر قالب "App"
3. سمِّ مشروعك (مثلاً "Phi3-iOS-App") واختر SwiftUI كواجهة المستخدم
4. اختر موقعًا لحفظ مشروعك

## الخطوة 2: إضافة التبعيات المطلوبة

أضف [حزمة أمثلة MLX](https://github.com/ml-explore/mlx-swift-examples) التي تحتوي على جميع التبعيات والمساعدات اللازمة لتحميل النماذج مسبقًا وأداء الاستدلال:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

بينما حزمة [MLX Swift الأساسية](https://github.com/ml-explore/mlx-swift) تكفي للعمليات الأساسية على التنسورات والوظائف الأساسية للتعلم الآلي، توفر حزمة أمثلة MLX عدة مكونات إضافية مصممة للعمل مع نماذج اللغة، وتسهيل عملية الاستدلال:

- أدوات تحميل النماذج التي تدير التنزيل من Hugging Face
- دمج أدوات تقسيم النصوص (tokenizer)
- مساعدات الاستدلال لتوليد النصوص
- تعريفات النماذج المُعدة مسبقًا

## الخطوة 3: تكوين الأذونات

للسماح لتطبيقنا بتنزيل النماذج وتخصيص ذاكرة كافية، نحتاج إلى إضافة أذونات محددة. أنشئ ملف `.entitlements` لتطبيقك بالمحتوى التالي:

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

> **ملاحظة:** إذن `com.apple.developer.kernel.increased-memory-limit` مهم لتشغيل النماذج الأكبر، حيث يسمح للتطبيق بطلب ذاكرة أكثر مما هو مسموح به عادة.

## الخطوة 4: إنشاء نموذج رسالة الدردشة

أولاً، لننشئ هيكلًا بسيطًا لتمثيل رسائل الدردشة:

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

## الخطوة 5: تنفيذ ViewModel

بعد ذلك، سننشئ فئة `PhiViewModel` التي تتولى تحميل النموذج وأداء الاستدلال:

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

يعرض ViewModel نقاط التكامل الرئيسية مع MLX:

- تعيين حدود ذاكرة التخزين المؤقت على GPU باستخدام `MLX.GPU.set(cacheLimit:)` لتحسين استخدام الذاكرة على الأجهزة المحمولة
- استخدام `LLMModelFactory` لتنزيل النموذج عند الطلب وتهيئة النموذج المحسّن لـ MLX
- الوصول إلى معلمات وبنية النموذج عبر `ModelContainer`
- الاستفادة من توليد الرموز واحدًا تلو الآخر عبر طريقة `MLXLMCommon.generate`
- إدارة عملية الاستدلال مع إعدادات درجة الحرارة والحدود المناسبة للرموز

تتيح طريقة توليد الرموز المتدفقة تقديم ردود فورية للمستخدمين أثناء توليد النص من النموذج. هذا مشابه لكيفية عمل النماذج القائمة على الخادم، حيث يتم تدفق الرموز للمستخدم، ولكن بدون تأخير طلبات الشبكة.

من حيث التفاعل مع واجهة المستخدم، الوظيفتان الرئيسيتان هما `loadModel()` التي تهيئ LLM، و `fetchAIResponse()` التي تعالج مدخلات المستخدم وتولد ردود الذكاء الاصطناعي.

### اعتبارات تنسيق النموذج

> **مهم:** لا يمكن استخدام نماذج Phi لـ MLX بصيغتها الافتراضية أو بصيغة GGUF. يجب تحويلها إلى تنسيق MLX، ويتم ذلك بواسطة مجتمع MLX. يمكنك العثور على نماذج محولة مسبقًا على [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

تتضمن حزمة أمثلة MLX تسجيلات مُعدة مسبقًا لعدة نماذج، بما في ذلك Phi-3. عند استدعاء `ModelRegistry.phi3_5_4bit`، فإنه يشير إلى نموذج MLX محول مسبقًا سيتم تنزيله تلقائيًا:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

يمكنك إنشاء تكوينات نموذج خاصة بك للإشارة إلى أي نموذج متوافق على Hugging Face. على سبيل المثال، لاستخدام Phi-4 mini بدلاً من ذلك، يمكنك تعريف تكوين خاص بك:

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

> **ملاحظة:** تمت إضافة دعم Phi-4 إلى مستودع أمثلة MLX Swift في نهاية فبراير 2025 (في [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). حتى مارس 2025، الإصدار الرسمي الأخير (2.21.2 من ديسمبر 2024) لا يتضمن دعمًا مدمجًا لـ Phi-4. لاستخدام نماذج Phi-4، ستحتاج إلى الإشارة إلى الحزمة مباشرة من الفرع الرئيسي:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

يمنحك هذا الوصول إلى أحدث تكوينات النماذج، بما في ذلك Phi-4، قبل تضمينها في إصدار رسمي. يمكنك استخدام هذا الأسلوب لاستخدام إصدارات مختلفة من نماذج Phi أو حتى نماذج أخرى تم تحويلها إلى تنسيق MLX.

## الخطوة 6: إنشاء واجهة المستخدم

لنقم الآن بتنفيذ واجهة دردشة بسيطة للتفاعل مع ViewModel الخاص بنا:

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

تتكون واجهة المستخدم من ثلاثة مكونات رئيسية تعمل معًا لإنشاء واجهة دردشة أساسية. يقوم `ContentView` بإنشاء واجهة ذات حالتين تعرض إما زر تحميل أو واجهة الدردشة حسب جاهزية النموذج. يعرض `MessageView` رسائل الدردشة الفردية بشكل مختلف بناءً على ما إذا كانت رسائل المستخدم (محاذاة لليمين، خلفية زرقاء) أو ردود نموذج Phi (محاذاة لليسار، خلفية رمادية). يوفر `TypingIndicatorView` مؤشرًا متحركًا بسيطًا لإظهار أن الذكاء الاصطناعي يعالج الطلب.

## الخطوة 7: بناء وتشغيل التطبيق

نحن الآن جاهزون لبناء وتشغيل التطبيق.

> **مهم!** MLX لا يدعم المحاكي. يجب تشغيل التطبيق على جهاز فعلي بمعالج Apple Silicon. راجع [هنا](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) لمزيد من المعلومات.

عند تشغيل التطبيق، اضغط على زر "Load model" لتنزيل وتهيئة نموذج Phi-3 (أو، حسب تكوينك، Phi-4). قد تستغرق هذه العملية بعض الوقت حسب سرعة اتصالك بالإنترنت، لأنها تتضمن تنزيل النموذج من Hugging Face. تنفيذنا يتضمن فقط مؤشر تحميل، لكن يمكنك رؤية التقدم الفعلي في وحدة تحكم Xcode.

بمجرد التحميل، يمكنك التفاعل مع النموذج بكتابة الأسئلة في حقل النص والضغط على زر الإرسال.

إليك كيف يجب أن يتصرف تطبيقنا عند التشغيل على iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## الخاتمة

وهذا كل شيء! باتباع هذه الخطوات، تكون قد أنشأت تطبيق iOS يقوم بتشغيل نموذج Phi-3 (أو Phi-4) مباشرة على الجهاز باستخدام إطار عمل Apple MLX.

تهانينا!

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.