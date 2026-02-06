# iOS मा Apple MLX Framework प्रयोग गरी Phi-3 र Phi-4 चलाउने तरिका

यो ट्युटोरियलले देखाउँछ कि कसरी Apple MLX framework प्रयोग गरी iOS एप्लिकेशनमा Phi-3 वा Phi-4 मोडेल डिभाइसमै चलाउने। [MLX](https://opensource.apple.com/projects/mlx/) भनेको Apple Silicon चिपहरूका लागि अनुकूलित Apple को मेशिन लर्निङ फ्रेमवर्क हो।

## आवश्यकताहरू

- macOS र Xcode 16 (वा माथि)
- iOS 18 (वा माथि) लक्षित डिभाइस जसमा कम्तीमा 8GB मेमोरी होस् (Apple Intelligence आवश्यकतासँग मिल्ने iPhone वा iPad, जुन क्वान्टाइज्ड Phi आवश्यकतासँग समान हुन्छ)
- Swift र SwiftUI को आधारभूत ज्ञान

## चरण १: नयाँ iOS प्रोजेक्ट बनाउने

Xcode मा नयाँ iOS प्रोजेक्ट बनाएर सुरु गर्नुहोस्:

1. Xcode खोल्नुहोस् र "Create a new Xcode project" छान्नुहोस्
2. टेम्प्लेटको रूपमा "App" रोज्नुहोस्
3. प्रोजेक्टको नाम राख्नुहोस् (जस्तै, "Phi3-iOS-App") र इन्टरफेस SwiftUI छान्नुहोस्
4. प्रोजेक्ट बचत गर्ने स्थान छान्नुहोस्

## चरण २: आवश्यक निर्भरता थप्ने

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) थप्नुहोस् जसले मोडेल प्रीलोड र इन्फरेन्सका लागि आवश्यक सबै निर्भरता र सहायकहरू समावेश गर्दछ:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

जबकि आधारभूत [MLX Swift package](https://github.com/ml-explore/mlx-swift) कोर टेन्सर अपरेसन र आधारभूत ML कार्यक्षमताका लागि पर्याप्त हुन्छ, MLX Examples package ले भाषा मोडेलहरूसँग काम गर्न र इन्फरेन्स प्रक्रियालाई सजिलो बनाउन थप कम्पोनेन्टहरू प्रदान गर्छ:

- Hugging Face बाट मोडेल डाउनलोड गर्ने युटिलिटीहरू
- टोकनाइजर एकीकरण
- टेक्स्ट जेनेरेसनका लागि इन्फरेन्स सहायकहरू
- पूर्व-कन्फिगर गरिएको मोडेल परिभाषाहरू

## चरण ३: Entitlements कन्फिगर गर्ने

हाम्रो एपलाई मोडेल डाउनलोड गर्न र पर्याप्त मेमोरी आवंटन गर्न अनुमति दिन, हामीले विशेष entitlements थप्नुपर्छ। आफ्नो एपको लागि `.entitlements` फाइल बनाउनुहोस् र यसमा तलको सामग्री राख्नुहोस्:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement ठूलो मोडेलहरू चलाउन महत्वपूर्ण छ, किनकि यसले एपलाई सामान्य भन्दा बढी मेमोरी माग्न अनुमति दिन्छ।

## चरण ४: Chat Message मोडेल बनाउने

पहिले, हाम्रो च्याट सन्देशहरू प्रतिनिधित्व गर्न एउटा आधारभूत संरचना बनाऔं:

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

## चरण ५: ViewModel कार्यान्वयन गर्ने

अब, `PhiViewModel` क्लास बनाउनेछौं जसले मोडेल लोड गर्ने र इन्फरेन्स गर्ने काम गर्छ:

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

ViewModel ले मुख्य MLX एकीकरण बुँदाहरू देखाउँछ:

- मोबाइल उपकरणमा मेमोरी उपयोग अनुकूलन गर्न `MLX.GPU.set(cacheLimit:)` प्रयोग गरी GPU क्यास सीमा सेट गर्ने
- `LLMModelFactory` प्रयोग गरी मोडेल आवश्यक पर्दा डाउनलोड गर्ने र MLX-अनुकूलित मोडेल सुरु गर्ने
- `ModelContainer` मार्फत मोडेलका प्यारामिटर र संरचनामा पहुँच गर्ने
- MLX को टोकन-द्वारा-टोकन जेनेरेसन `MLXLMCommon.generate` विधि मार्फत गर्ने
- उपयुक्त तापक्रम सेटिङ र टोकन सीमासहित इन्फरेन्स प्रक्रिया व्यवस्थापन गर्ने

स्ट्रीमिङ टोकन जेनेरेसनले मोडेलले टेक्स्ट जेनेरेट गर्दा प्रयोगकर्तालाई तुरुन्त प्रतिक्रिया दिन्छ। यो सर्भर-आधारित मोडेलहरू जस्तै हो, जसले टोकनहरू प्रयोगकर्तालाई स्ट्रिम गर्छन्, तर नेटवर्क अनुरोधको ढिलाइ बिना।

UI अन्तरक्रियाको हिसाबले, दुई मुख्य फङ्सनहरू हुन्: `loadModel()`, जसले LLM सुरु गर्छ, र `fetchAIResponse()`, जसले प्रयोगकर्ताको इनपुट प्रक्रिया गरी AI प्रतिक्रिया बनाउँछ।

### मोडेल फर्म्याट सम्बन्धी विचारहरू

> **Important:** MLX का लागि Phi मोडेलहरू तिनीहरूको डिफल्ट वा GGUF फर्म्याटमा प्रयोग गर्न सकिँदैन। तिनीहरूलाई MLX फर्म्याटमा रूपान्तरण गर्नुपर्छ, जुन MLX समुदायले ह्यान्डल गर्छ। पूर्व-रूपान्तरण गरिएका मोडेलहरू [huggingface.co/mlx-community](https://huggingface.co/mlx-community) मा फेला पार्न सकिन्छ।

MLX Examples package मा Phi-3 सहित विभिन्न मोडेलहरूको पूर्व-कन्फिगर गरिएको रजिस्ट्रेसनहरू समावेश छन्। जब तपाईं `ModelRegistry.phi3_5_4bit` कल गर्नुहुन्छ, यो स्वतः डाउनलोड हुने पूर्व-रूपान्तरण गरिएको MLX मोडेललाई जनाउँछ:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

तपाईं आफ्नो मोडेल कन्फिगरेसनहरू बनाउन सक्नुहुन्छ जुन Hugging Face मा कुनै पनि उपयुक्त मोडेललाई जनाउँछ। उदाहरणका लागि, Phi-4 मिनी प्रयोग गर्न चाहनुहुन्छ भने, तपाईं आफ्नो कन्फिगरेसन यसरी परिभाषित गर्न सक्नुहुन्छ:

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

> **Note:** Phi-4 समर्थन MLX Swift Examples रिपोजिटरीमा फेब्रुअरी २०२५ को अन्त्यमा थपिएको हो ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))। मार्च २०२५ सम्मको आधिकारिक रिलिज (डिसेम्बर २०२४ को 2.21.2) मा Phi-4 समर्थन समावेश छैन। Phi-4 मोडेलहरू प्रयोग गर्न, तपाईंले मुख्य ब्रान्चबाट सिधै प्याकेजलाई रेफरेन्स गर्नुपर्ने हुन्छ:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

यसले तपाईंलाई आधिकारिक रिलिजमा समावेश हुनु अघि नवीनतम मोडेल कन्फिगरेसनहरू, जस्तै Phi-4, पहुँच दिन्छ। यस तरिकाले तपाईं विभिन्न Phi मोडेल संस्करणहरू वा MLX फर्म्याटमा रूपान्तरण गरिएका अन्य मोडेलहरू प्रयोग गर्न सक्नुहुन्छ।

## चरण ६: UI बनाउने

अब हाम्रो ViewModel सँग अन्तरक्रिया गर्न सरल च्याट इन्टरफेस कार्यान्वयन गरौं:

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

UI तीन मुख्य कम्पोनेन्टहरू मिलेर बनेको छ जसले आधारभूत च्याट इन्टरफेस तयार गर्छ। `ContentView` ले दुई-राज्य इन्टरफेस बनाउँछ जुन मोडेल तयार नभएसम्म लोडिङ बटन देखाउँछ र तयार भएपछि च्याट इन्टरफेस देखाउँछ। `MessageView` ले व्यक्तिगत च्याट सन्देशहरू फरक तरिकाले देखाउँछ—प्रयोगकर्ताका सन्देशहरू दायाँतर्फ, निलो पृष्ठभूमिमा, र Phi मोडेलका प्रतिक्रियाहरू बाँयातर्फ, खैरो पृष्ठभूमिमा। `TypingIndicatorView` ले AI प्रक्रिया गरिरहेको देखाउन सरल एनिमेटेड संकेत दिन्छ।

## चरण ७: एप बनाउने र चलाउने

अब एप बनाउने र चलाउन तयार छौं।

> **Important!** MLX सिम्युलेटरलाई समर्थन गर्दैन। तपाईंले एप Apple Silicon चिप भएको भौतिक डिभाइसमा चलाउनुपर्छ। थप जानकारीका लागि [यहाँ](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) हेर्नुहोस्।

एप सुरु हुँदा, "Load model" बटन थिचेर Phi-3 (वा तपाईंको कन्फिगरेसन अनुसार Phi-4) मोडेल डाउनलोड र सुरु गर्नुहोस्। यो प्रक्रिया इन्टरनेट कनेक्शनको आधारमा केही समय लाग्न सक्छ किनकि मोडेल Hugging Face बाट डाउनलोड हुन्छ। हाम्रो कार्यान्वयनमा लोडिङ देखाउन स्पिनर मात्र छ, तर Xcode कन्सोलमा वास्तविक प्रगति हेर्न सकिन्छ।

लोड भएपछि, तपाईं मोडेलसँग अन्तरक्रिया गर्न टेक्स्ट फिल्डमा प्रश्न टाइप गरी पठाउने बटन थिच्न सक्नुहुन्छ।

यहाँ हाम्रो एपले iPad Air M1 मा चल्दा कस्तो व्यवहार गर्नेछ:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## निष्कर्ष

यति नै! यी चरणहरू पालना गरेर, तपाईंले Apple को MLX framework प्रयोग गरी डिभाइसमै सिधै Phi-3 (वा Phi-4) मोडेल चलाउने iOS एप्लिकेशन बनाउनु भयो।

बधाई छ!

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।