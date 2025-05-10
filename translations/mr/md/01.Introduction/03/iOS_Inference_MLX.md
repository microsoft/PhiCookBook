<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:09:01+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "mr"
}
-->
# iOS वर Apple MLX Framework सह Phi-3 आणि Phi-4 चालवणे

हा ट्यूटोरियल दाखवतो की Apple MLX फ्रेमवर्क वापरून Phi-3 किंवा Phi-4 मॉडेल डिव्हाइसवर कसे चालवायचे यासाठी iOS अॅप कसे तयार करायचे. [MLX](https://opensource.apple.com/projects/mlx/) हा Apple Silicon चिपसाठी ऑप्टिमाइझ केलेला Apple चा मशीन लर्निंग फ्रेमवर्क आहे.

## आवश्यक अटी

- macOS सह Xcode 16 (किंवा त्याहून वर)
- किमान 8GB असलेले iOS 18 (किंवा त्याहून वर) टार्गेट डिव्हाइस (Apple Intelligence आवश्यकतांसाठी जसे iPhone किंवा iPad, जे क्वांटाइज्ड Phi आवश्यकतांप्रमाणेच आहेत)
- Swift आणि SwiftUI चे प्राथमिक ज्ञान

## टप्पा 1: नवीन iOS प्रोजेक्ट तयार करा

Xcode मध्ये नवीन iOS प्रोजेक्ट तयार करण्यापासून सुरुवात करा:

1. Xcode उघडा आणि "Create a new Xcode project" निवडा
2. टेम्प्लेट म्हणून "App" निवडा
3. तुमच्या प्रोजेक्टचे नाव द्या (उदा. "Phi3-iOS-App") आणि इंटरफेस म्हणून SwiftUI निवडा
4. प्रोजेक्ट जतन करण्यासाठी स्थान निवडा

## टप्पा 2: आवश्यक Dependencies जोडा

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) जोडा, ज्यामध्ये मॉडेल प्रीलोडिंग आणि इन्फरन्ससाठी आवश्यक सर्व डिपेंडेंसीज आणि हेल्पर्स असतात:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

जरी बेस [MLX Swift package](https://github.com/ml-explore/mlx-swift) मुख्य टेन्सर ऑपरेशन्स आणि बेसिक ML फंक्शनॅलिटीसाठी पुरेसा असेल, तरी MLX Examples package भाषिक मॉडेल्ससाठी आणि इन्फरन्स प्रोसेस सुलभ करण्यासाठी काही अतिरिक्त घटक पुरवते:

- Hugging Face वरून डाउनलोड करण्यासाठी मॉडेल लोडिंग युटिलिटीज
- टोकनायझर इंटिग्रेशन
- टेक्स्ट जनरेशनसाठी इन्फरन्स हेल्पर्स
- प्री-कॉन्फिगर केलेली मॉडेल डिफिनिशन्स

## टप्पा 3: Entitlements कॉन्फिगर करा

आमच्या अॅपला मॉडेल डाउनलोड करण्याची आणि पुरेशी मेमरी अलोकेट करण्याची परवानगी देण्यासाठी, विशिष्ट entitlements जोडणे आवश्यक आहे. तुमच्या अॅपसाठी `.entitlements` फाइल तयार करा खालील सामग्रीसह:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement मोठ्या मॉडेल्ससाठी महत्त्वाचे आहे कारण हे अॅपला सामान्यतः परवानगी दिलेल्या मेमरीपेक्षा जास्त मेमरी मागण्याची परवानगी देते.

## टप्पा 4: Chat Message मॉडेल तयार करा

सुरुवातीला, आमच्या चॅट मेसेजेसचे प्रतिनिधित्व करण्यासाठी एक बेसिक स्ट्रक्चर तयार करूया:

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

## टप्पा 5: ViewModel अंमलात आणा

पुढे, `PhiViewModel` क्लास तयार करूया जो मॉडेल लोडिंग आणि इन्फरन्स हाताळतो:

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

ViewModel मध्ये MLX इंटिग्रेशनचे मुख्य पॉइंट्स दाखवले आहेत:

- `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit` वापरून GPU कॅश लिमिट सेट करणे, जे एक विशिष्ट प्री-कन्व्हर्टेड MLX मॉडेल संदर्भित करते जे आपोआप डाउनलोड होईल:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

तुम्ही तुमचे स्वतःचे मॉडेल कॉन्फिगरेशन तयार करू शकता जे Hugging Face वर कोणत्याही सुसंगत मॉडेलकडे निर्देश करेल. उदाहरणार्थ, Phi-4 मिनी वापरण्यासाठी तुम्ही तुमचे कॉन्फिगरेशन असे तयार करू शकता:

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

> **Note:** Phi-4 सपोर्ट MLX Swift Examples रिपॉजिटरीमध्ये फेब्रुवारी 2025 च्या शेवटी ( [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216) मध्ये) जोडला गेला आहे. मार्च 2025 पर्यंत, डिसेंबर 2024 मधील 2.21.2 हा नवीनतम अधिकृत रिलीजमध्ये Phi-4 सपोर्ट अंतर्भूत नाही. Phi-4 मॉडेल वापरण्यासाठी, तुम्हाला मुख्य ब्रांचमधून थेट पॅकेज संदर्भित करावे लागेल:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

हे तुम्हाला नवीनतम मॉडेल कॉन्फिगरेशन वापरण्याची परवानगी देते, ज्यात Phi-4 देखील समाविष्ट आहे, ते अधिकृत रिलीजमध्ये समाविष्ट होण्यापूर्वी. तुम्ही हा मार्ग वापरून Phi मॉडेल्सच्या वेगवेगळ्या आवृत्त्या किंवा MLX फॉर्मॅटमध्ये कन्व्हर्ट केलेली इतर मॉडेल्स वापरू शकता.

## टप्पा 6: UI तयार करा

आता, आमच्या ViewModel शी संवाद साधण्यासाठी एक सोपी चॅट इंटरफेस तयार करूया:

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

UI तीन मुख्य घटकांनी बनलेले आहे जे एकत्रितपणे बेसिक चॅट इंटरफेस तयार करतात. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` एक सोपी अ‍ॅनिमेटेड इंडिकेटर पुरवतो जी AI प्रक्रिया करत असल्याचे दर्शवते.

## टप्पा 7: अॅप बिल्ड आणि रन करा

आता आपण अॅप्लिकेशन बिल्ड आणि रन करण्यासाठी तयार आहोत.

> **Important!** MLX सिम्युलेटरला सपोर्ट करत नाही. तुम्हाला अॅप Apple Silicon चिप असलेल्या फिजिकल डिव्हाइसवर चालवावे लागेल. अधिक माहितीसाठी [इथे](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) पहा.

अॅप लॉन्च झाल्यावर, "Load model" बटणावर टॅप करा जेणेकरून Phi-3 (किंवा तुमच्या कॉन्फिगरेशननुसार Phi-4) मॉडेल डाउनलोड आणि इनिशियलाइझ होईल. इंटरनेट कनेक्शननुसार हा प्रोसेस काही वेळ घेऊ शकतो कारण मॉडेल Hugging Face वरून डाउनलोड करावे लागते. आमच्या अंमलबजावणीत फक्त एक स्पिनर लोडिंग सूचित करण्यासाठी आहे, पण तुम्ही Xcode कन्सोलमध्ये प्रगती पाहू शकता.

लोड झाल्यावर, तुम्ही टेक्स्ट फील्डमध्ये प्रश्न टाइप करून आणि पाठवा बटण दाबून मॉडेलशी संवाद साधू शकता.

आमच्या अॅप्लिकेशनचे वर्तन iPad Air M1 वर असे दिसेल:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## निष्कर्ष

बस इतकंच! या टप्प्यांचे अनुसरण करून, तुम्ही Apple च्या MLX फ्रेमवर्क वापरून थेट डिव्हाइसवर Phi-3 (किंवा Phi-4) मॉडेल चालवणारे iOS अॅप तयार केले आहे.

अभिनंदन!

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतर शिफारसीय आहे. या भाषांतराच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुतींसाठी किंवा चुकीच्या अर्थलागीसाठी आम्ही जबाबदार नाही.