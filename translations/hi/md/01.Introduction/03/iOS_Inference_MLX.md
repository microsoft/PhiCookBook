<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07ca611437b569633d7aacf855ecaa7e",
  "translation_date": "2025-04-04T17:47:11+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference_MLX.md",
  "language_code": "hi"
}
-->
# iOS पर Apple MLX Framework के साथ Phi-3 और Phi-4 चलाना

यह ट्यूटोरियल दिखाता है कि Apple MLX फ्रेमवर्क का उपयोग करके Phi-3 या Phi-4 मॉडल को डिवाइस पर चलाने वाला iOS एप्लिकेशन कैसे बनाया जाए। [MLX](https://opensource.apple.com/projects/mlx/) Apple का मशीन लर्निंग फ्रेमवर्क है, जो Apple Silicon चिप्स के लिए ऑप्टिमाइज़ किया गया है।

## आवश्यकताएँ

- Xcode 16 (या उच्च) के साथ macOS
- iOS 18 (या उच्च) लक्ष्य डिवाइस जिसमें कम से कम 8GB RAM हो (ऐसे iPhone या iPad जो Apple Intelligence आवश्यकताओं के अनुरूप हों, क्योंकि वे क्वांटाइज़्ड Phi आवश्यकताओं के समान होंगे)
- Swift और SwiftUI का बुनियादी ज्ञान

## चरण 1: एक नया iOS प्रोजेक्ट बनाना

Xcode में एक नया iOS प्रोजेक्ट बनाकर शुरुआत करें:

1. Xcode लॉन्च करें और "Create a new Xcode project" चुनें।
2. टेम्पलेट के रूप में "App" चुनें।
3. अपने प्रोजेक्ट का नाम रखें (जैसे, "Phi3-iOS-App") और इंटरफेस के लिए SwiftUI चुनें।
4. अपने प्रोजेक्ट को सेव करने के लिए एक स्थान चुनें।

## चरण 2: आवश्यक डिपेंडेंसीज़ जोड़ें

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) जोड़ें, जिसमें मॉडल्स को प्रीलोड करने और इन्फरेंस करने के लिए सभी आवश्यक डिपेंडेंसीज़ और हेल्पर्स शामिल हैं:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

हालांकि बेस [MLX Swift package](https://github.com/ml-explore/mlx-swift) कोर टेन्सर ऑपरेशन्स और बेसिक ML कार्यक्षमता के लिए पर्याप्त होगा, MLX Examples पैकेज कई अतिरिक्त घटकों को प्रदान करता है, जो भाषा मॉडल्स के साथ काम करने और इन्फरेंस प्रक्रिया को आसान बनाने के लिए डिज़ाइन किए गए हैं:

- मॉडल लोडिंग यूटिलिटीज़ जो Hugging Face से डाउनलोडिंग को संभालती हैं
- टोकनाइज़र इंटीग्रेशन
- टेक्स्ट जनरेशन के लिए इन्फरेंस हेल्पर्स
- प्री-कॉन्फ़िगर मॉडल डेफिनिशन

## चरण 3: एंटाइटलमेंट्स कॉन्फ़िगर करें

हमारे ऐप को मॉडल डाउनलोड करने और पर्याप्त मेमोरी आवंटित करने की अनुमति देने के लिए, हमें कुछ विशेष एंटाइटलमेंट्स जोड़ने की आवश्यकता है। अपने ऐप के लिए एक `.entitlements` फ़ाइल बनाएं, जिसमें निम्नलिखित सामग्री हो:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` एंटाइटलमेंट बड़े मॉडल्स को चलाने के लिए महत्वपूर्ण है, क्योंकि यह ऐप को सामान्य रूप से अनुमत मेमोरी से अधिक का अनुरोध करने की अनुमति देता है।

## चरण 4: चैट संदेश मॉडल बनाएं

सबसे पहले, आइए अपने चैट संदेशों का प्रतिनिधित्व करने के लिए एक बेसिक संरचना बनाएं:

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

## चरण 5: व्यू मॉडल को लागू करें

इसके बाद, हम `PhiViewModel` क्लास बनाएंगे, जो मॉडल लोडिंग और इन्फरेंस को संभालता है:

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

व्यू मॉडल MLX इंटीग्रेशन के मुख्य बिंदुओं को प्रदर्शित करता है:

- `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit` के साथ GPU कैश लिमिट सेट करना। यह एक विशेष प्री-कन्वर्टेड MLX मॉडल को संदर्भित करता है, जिसे स्वचालित रूप से डाउनलोड किया जाएगा:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

आप अपनी खुद की मॉडल कॉन्फ़िगरेशन बना सकते हैं, जो Hugging Face पर किसी भी संगत मॉडल की ओर इंगित करती हो। उदाहरण के लिए, यदि आप Phi-4 mini का उपयोग करना चाहते हैं, तो आप अपनी कॉन्फ़िगरेशन परिभाषित कर सकते हैं:

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

> **Note:** Phi-4 सपोर्ट फरवरी 2025 के अंत में MLX Swift Examples रिपॉजिटरी में जोड़ा गया था (देखें [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))। मार्च 2025 तक, नवीनतम आधिकारिक रिलीज़ (दिसंबर 2024 की 2.21.2) में बिल्ट-इन Phi-4 सपोर्ट शामिल नहीं है। Phi-4 मॉडल्स का उपयोग करने के लिए, आपको मुख्य शाखा से पैकेज को सीधे संदर्भित करना होगा:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

यह आपको नवीनतम मॉडल कॉन्फ़िगरेशन, जिनमें Phi-4 शामिल है, आधिकारिक रिलीज़ से पहले एक्सेस करने की अनुमति देता है। आप इस दृष्टिकोण का उपयोग Phi मॉडल्स के विभिन्न संस्करणों या यहां तक कि अन्य मॉडल्स का उपयोग करने के लिए कर सकते हैं, जिन्हें MLX प्रारूप में कन्वर्ट किया गया है।

## चरण 6: UI बनाएं

अब चलिए एक साधारण चैट इंटरफेस को लागू करते हैं, जो हमारे व्यू मॉडल के साथ इंटरैक्ट करता है:

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

UI तीन मुख्य घटकों से बना है, जो मिलकर एक बेसिक चैट इंटरफेस बनाते हैं। `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` एक साधारण एनिमेटेड इंडिकेटर प्रदान करता है, जो दिखाता है कि AI प्रोसेसिंग कर रहा है।

## चरण 7: ऐप को बिल्ड और रन करें

अब हम एप्लिकेशन को बिल्ड और रन करने के लिए तैयार हैं।

> **Important!** MLX सिम्युलेटर को सपोर्ट नहीं करता। आपको ऐप को Apple Silicon चिप वाले फिजिकल डिवाइस पर चलाना होगा। अधिक जानकारी के लिए [यहां](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) देखें।

जब ऐप लॉन्च होता है, तो "Load model" बटन पर टैप करें ताकि Phi-3 (या, आपके कॉन्फ़िगरेशन के अनुसार, Phi-4) मॉडल डाउनलोड और इनिशियलाइज़ हो सके। यह प्रक्रिया आपके इंटरनेट कनेक्शन पर निर्भर करते हुए कुछ समय ले सकती है, क्योंकि इसमें Hugging Face से मॉडल डाउनलोड करना शामिल है। हमारे इम्प्लीमेंटेशन में केवल एक स्पिनर लोडिंग को इंगित करता है, लेकिन आप Xcode कंसोल में वास्तविक प्रोग्रेस देख सकते हैं।

एक बार लोड हो जाने के बाद, आप टेक्स्ट फ़ील्ड में प्रश्न टाइप करके और "Send" बटन पर टैप करके मॉडल के साथ इंटरैक्ट कर सकते हैं।

यहां दिखाया गया है कि हमारा एप्लिकेशन iPad Air M1 पर कैसे व्यवहार करेगा:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## निष्कर्ष

और बस इतना ही! इन चरणों का पालन करके, आपने Apple के MLX फ्रेमवर्क का उपयोग करके डिवाइस पर सीधे Phi-3 (या Phi-4) मॉडल चलाने वाला एक iOS एप्लिकेशन बना लिया है।

बधाई हो!

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।