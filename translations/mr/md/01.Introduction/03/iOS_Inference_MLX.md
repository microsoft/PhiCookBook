<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:29:56+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "mr"
}
-->
# iOS वर Apple MLX Framework सह Phi-3 आणि Phi-4 चालविणे

हा ट्युटोरियल दाखवतो की Apple MLX फ्रेमवर्क वापरून iOS अॅप्लिकेशन कसे तयार करायचे जे डिव्हाइसवरच Phi-3 किंवा Phi-4 मॉडेल चालवते. [MLX](https://opensource.apple.com/projects/mlx/) हा Apple Silicon चिप्ससाठी ऑप्टिमाइझ केलेला Apple चा मशीन लर्निंग फ्रेमवर्क आहे.

## आवश्यक अटी

- Xcode 16 (किंवा त्याहून अधिक) असलेले macOS
- iOS 18 (किंवा त्याहून अधिक) टार्गेट डिव्हाइस ज्यामध्ये किमान 8GB RAM असावी (Apple Intelligence आवश्यकतांसाठी सुसंगत iPhone किंवा iPad, जे क्वांटाइज्ड Phi आवश्यकतांसारखे असतील)
- Swift आणि SwiftUI ची प्राथमिक माहिती

## पाऊल 1: नवीन iOS प्रोजेक्ट तयार करा

Xcode मध्ये नवीन iOS प्रोजेक्ट तयार करण्यापासून सुरुवात करा:

1. Xcode सुरू करा आणि "Create a new Xcode project" निवडा
2. टेम्प्लेट म्हणून "App" निवडा
3. प्रोजेक्टचे नाव द्या (उदा. "Phi3-iOS-App") आणि इंटरफेससाठी SwiftUI निवडा
4. प्रोजेक्ट जतन करण्यासाठी स्थान निवडा

## पाऊल 2: आवश्यक Dependencies जोडा

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) जोडा, ज्यामध्ये मॉडेल प्रीलोडिंग आणि इन्फरन्ससाठी आवश्यक सर्व dependencies आणि सहाय्यक आहेत:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

मुळ [MLX Swift package](https://github.com/ml-explore/mlx-swift) मध्ये कोर टेन्सर ऑपरेशन्स आणि बेसिक ML फंक्शनॅलिटी पुरेशी आहे, पण MLX Examples package मध्ये भाषा मॉडेल्ससाठी आणि इन्फरन्स प्रक्रिया सुलभ करण्यासाठी अनेक अतिरिक्त घटक आहेत:

- Hugging Face वरून डाउनलोड करण्यासाठी मॉडेल लोडिंग युटिलिटीज
- टोकनायझर इंटिग्रेशन
- टेक्स्ट जनरेशनसाठी इन्फरन्स सहाय्यक
- प्री-कॉन्फिगर केलेली मॉडेल डिफिनिशन्स

## पाऊल 3: Entitlements कॉन्फिगर करा

आपल्या अॅपला मॉडेल डाउनलोड करण्याची आणि पुरेशी मेमरी अलोकेट करण्याची परवानगी देण्यासाठी, विशिष्ट entitlements जोडणे आवश्यक आहे. आपल्या अॅपसाठी `.entitlements` फाइल तयार करा ज्यामध्ये खालील सामग्री असावी:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement मोठ्या मॉडेल्स चालवण्यासाठी महत्त्वाचे आहे, कारण हे अॅपला सामान्यतः परवानगी दिलेल्या पेक्षा अधिक मेमरी मागण्याची परवानगी देते.

## पाऊल 4: Chat Message मॉडेल तयार करा

सुरुवातीला, आपल्या चॅट मेसेजेसचे प्रतिनिधित्व करण्यासाठी एक सोपी स्ट्रक्चर तयार करूया:

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

## पाऊल 5: ViewModel अंमलात आणा

नंतर, `PhiViewModel` क्लास तयार करूया जो मॉडेल लोडिंग आणि इन्फरन्स हाताळेल:

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

ViewModel मध्ये MLX इंटिग्रेशनचे मुख्य मुद्दे दाखवले आहेत:

- मोबाइल डिव्हाइसेसवर मेमरी वापर ऑप्टिमाइझ करण्यासाठी `MLX.GPU.set(cacheLimit:)` वापरून GPU कॅश लिमिट सेट करणे
- `LLMModelFactory` वापरून मॉडेल ऑन-डिमांड डाउनलोड करणे आणि MLX-ऑप्टिमाइझ्ड मॉडेल इनिशियलाइझ करणे
- `ModelContainer` द्वारे मॉडेलचे पॅरामीटर्स आणि स्ट्रक्चर ऍक्सेस करणे
- MLX च्या `MLXLMCommon.generate` पद्धतीने टोकन-बाय-टोकन जनरेशनचा लाभ घेणे
- योग्य temperature सेटिंग्ज आणि टोकन लिमिट्ससह इन्फरन्स प्रक्रिया व्यवस्थापित करणे

स्ट्रीमिंग टोकन जनरेशन पद्धत वापरकर्त्यांना त्वरित प्रतिसाद देते, जसे की सर्व्हर-आधारित मॉडेल्स टोकन्स वापरकर्त्याला परत पाठवतात, पण नेटवर्क विलंबाशिवाय.

UI इंटरॅक्शनसाठी दोन मुख्य फंक्शन्स आहेत: `loadModel()`, जे LLM इनिशियलाइझ करते, आणि `fetchAIResponse()`, जे वापरकर्त्याचा इनपुट प्रक्रिया करून AI प्रतिसाद तयार करते.

### मॉडेल फॉरमॅट संदर्भात

> **Important:** MLX साठी Phi मॉडेल्स त्यांच्या डीफॉल्ट किंवा GGUF फॉरमॅटमध्ये वापरता येत नाहीत. त्यांना MLX फॉरमॅटमध्ये रूपांतरित करणे आवश्यक आहे, जे MLX समुदायाकडून हाताळले जाते. प्री-कन्व्हर्टेड मॉडेल्स [huggingface.co/mlx-community](https://huggingface.co/mlx-community) येथे उपलब्ध आहेत.

MLX Examples package मध्ये Phi-3 सह अनेक मॉडेल्ससाठी प्री-कॉन्फिगर केलेली नोंदणी आहे. जेव्हा तुम्ही `ModelRegistry.phi3_5_4bit` कॉल करता, तेव्हा ते एका विशिष्ट प्री-कन्व्हर्टेड MLX मॉडेलकडे निर्देश करते जे आपोआप डाउनलोड होईल:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

तुम्ही तुमचे स्वतःचे मॉडेल कॉन्फिगरेशन तयार करू शकता जे Hugging Face वरील कोणत्याही सुसंगत मॉडेलकडे निर्देश करते. उदाहरणार्थ, Phi-4 मिनी वापरण्यासाठी, तुम्ही तुमचे स्वतःचे कॉन्फिगरेशन परिभाषित करू शकता:

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

> **Note:** Phi-4 सपोर्ट MLX Swift Examples रिपॉजिटरीमध्ये फेब्रुवारी 2025 च्या शेवटी (PR #216 मध्ये) जोडले गेले. मार्च 2025 पर्यंत, डिसेंबर 2024 मधील 2.21.2 हा अधिकृत रिलीझ Phi-4 सपोर्ट समाविष्ट करत नाही. Phi-4 मॉडेल्स वापरण्यासाठी, तुम्हाला मुख्य ब्रँचमधून पॅकेज थेट संदर्भित करावे लागेल:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

हे तुम्हाला अधिकृत रिलीझमध्ये समाविष्ट होण्यापूर्वी नवीनतम मॉडेल कॉन्फिगरेशन, ज्यात Phi-4 देखील आहे, वापरण्याची परवानगी देते. तुम्ही या पद्धतीने Phi मॉडेल्सच्या वेगवेगळ्या आवृत्त्या किंवा MLX फॉरमॅटमध्ये रूपांतरित इतर मॉडेल्स वापरू शकता.

## पाऊल 6: UI तयार करा

आता आपल्या ViewModel सोबत संवाद साधण्यासाठी एक सोपी चॅट इंटरफेस अंमलात आणूया:

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

UI मध्ये तीन मुख्य घटक आहेत जे एकत्र काम करून मूलभूत चॅट इंटरफेस तयार करतात. `ContentView` दोन स्थितींचा इंटरफेस तयार करते जो मॉडेल तयार होईपर्यंत लोडिंग बटण दाखवतो आणि तयार झाल्यावर चॅट इंटरफेस दर्शवतो. `MessageView` वेगवेगळ्या प्रकारे चॅट मेसेजेस रेंडर करते - वापरकर्त्याचे मेसेजेस (उजवीकडे संरेखित, निळ्या पार्श्वभूमीसह) आणि Phi मॉडेल प्रतिसाद (डावीकडे संरेखित, करड्या पार्श्वभूमीसह). `TypingIndicatorView` AI प्रक्रिया करत असल्याचे दर्शविण्यासाठी एक साधा अॅनिमेटेड इंडिकेटर प्रदान करते.

## पाऊल 7: अॅप बिल्ड आणि रन करा

आता आपण अॅप्लिकेशन बिल्ड आणि रन करण्यास तयार आहोत.

> **Important!** MLX सिम्युलेटरला सपोर्ट करत नाही. तुम्हाला Apple Silicon चिप असलेल्या फिजिकल डिव्हाइसवर अॅप चालवावे लागेल. अधिक माहितीसाठी [येथे](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) पहा.

अॅप सुरू झाल्यावर, "Load model" बटणावर टॅप करा जेणेकरून Phi-3 (किंवा तुमच्या कॉन्फिगरेशननुसार Phi-4) मॉडेल डाउनलोड आणि इनिशियलाइझ होईल. इंटरनेट कनेक्शनवर अवलंबून हा प्रक्रिया काही वेळ घेऊ शकते, कारण मॉडेल Hugging Face वरून डाउनलोड करणे आवश्यक आहे. आमच्या अंमलबजावणीत फक्त लोडिंग सूचक म्हणून स्पिनर आहे, पण तुम्ही Xcode कन्सोलमध्ये प्रत्यक्ष प्रगती पाहू शकता.

लोड झाल्यानंतर, तुम्ही टेक्स्ट फील्डमध्ये प्रश्न टाइप करून आणि पाठवा बटणावर टॅप करून मॉडेलशी संवाद साधू शकता.

आमच्या अॅप्लिकेशनचा iPad Air M1 वर चालणारा वर्तन खालीलप्रमाणे आहे:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## निष्कर्ष

बस इतकंच! या पायऱ्या पाळून, तुम्ही Apple च्या MLX फ्रेमवर्कचा वापर करून डिव्हाइसवर थेट Phi-3 (किंवा Phi-4) मॉडेल चालवणारे iOS अॅप्लिकेशन तयार केले आहे.

अभिनंदन!

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.