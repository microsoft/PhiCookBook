<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:09:44+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "ne"
}
-->
# iOS मा Apple MLX Framework सँग Phi-3 र Phi-4 चलाउने तरिका

यस ट्यूटोरियलले देखाउँछ कि कसरी Apple MLX फ्रेमवर्क प्रयोग गरी iOS एप्लिकेशन बनाउने जसले Phi-3 वा Phi-4 मोडेल डिभाइसमै चलाउन सक्छ। [MLX](https://opensource.apple.com/projects/mlx/) भनेको Apple Silicon चिपहरूका लागि अनुकूलित Apple को मेशिन लर्निङ फ्रेमवर्क हो।

## आवश्यकताहरू

- Xcode 16 (वा माथि) भएको macOS
- iOS 18 (वा माथि) लक्षित डिभाइस, कम्तीमा 8GB मेमोरी (Apple Intelligence आवश्यकतासँग मिल्ने iPhone वा iPad, जुन क्वान्टाइज्ड Phi आवश्यकतासँग समान हुन्छ)
- Swift र SwiftUI को आधारभूत ज्ञान

## चरण 1: नयाँ iOS प्रोजेक्ट बनाउनुहोस्

Xcode मा नयाँ iOS प्रोजेक्ट बनाएर सुरु गर्नुहोस्:

1. Xcode खोल्नुहोस् र "Create a new Xcode project" चयन गर्नुहोस्
2. टेम्प्लेटको रूपमा "App" छान्नुहोस्
3. प्रोजेक्टको नाम राख्नुहोस् (जस्तै, "Phi3-iOS-App") र इन्टरफेस SwiftUI चयन गर्नुहोस्
4. प्रोजेक्ट सुरक्षित गर्न स्थान छान्नुहोस्

## चरण 2: आवश्यक Dependencies थप्नुहोस्

[MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) थप्नुहोस् जसले मोडेलहरू प्रीलोड गर्न र इन्फरेन्स गर्न आवश्यक सबै निर्भरता र सहायकहरू समावेश गर्छ:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

मूल [MLX Swift package](https://github.com/ml-explore/mlx-swift) ले मुख्य टेन्सर अपरेसन र आधारभूत ML कार्यक्षमता पुर्याउँछ, तर MLX Examples package ले भाषा मोडेलहरूमा काम गर्न र इन्फरेन्स प्रक्रिया सजिलो बनाउन थप कम्पोनेन्टहरू प्रदान गर्छ:

- Hugging Face बाट डाउनलोड गर्ने मोडेल लोड गर्ने युटिलिटीहरू
- टोकनाइजर इन्टिग्रेसन
- टेक्स्ट जेनेरेशनका लागि इन्फरेन्स हेल्परहरू
- पूर्व-कन्फिगर गरिएको मोडेल परिभाषाहरू

## चरण 3: Entitlements कन्फिगर गर्नुहोस्

हाम्रो एपलाई मोडेलहरू डाउनलोड गर्न र पर्याप्त मेमोरी आवंटन गर्न अनुमति दिन, विशेष entitlements थप्न आवश्यक छ। आफ्नो एपका लागि `.entitlements` फाइल निम्न सामग्रीसहित बनाउनुहोस्:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement ठूलो मोडेलहरू चलाउन महत्त्वपूर्ण छ, किनभने यसले एपलाई सामान्यभन्दा बढी मेमोरी माग्न अनुमति दिन्छ।

## चरण 4: Chat Message मोडेल बनाउनुहोस्

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

## चरण 5: ViewModel कार्यान्वयन गर्नुहोस्

अब, `PhiViewModel` क्लास बनाउँछौं जसले मोडेल लोडिङ र इन्फरेन्स ह्यान्डल गर्छ:

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

ViewModel ले मुख्य MLX इन्टिग्रेसन पोइन्टहरू देखाउँछ:

- `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit` सँग GPU क्यास सीमा सेट गर्दै, जुन स्वतः डाउनलोड हुने विशेष पूर्व-परिवर्तित MLX मोडेललाई रेफरेन्स गर्छ:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

तपाईं आफ्नो मोडेल कन्फिगरेसनहरू बनाउन सक्नुहुन्छ जुन Hugging Face मा कुनै पनि उपयुक्त मोडेललाई पोइन्ट गर्छ। उदाहरणका लागि, Phi-4 mini प्रयोग गर्न, आफ्नो कन्फिगरेसन यसरी परिभाषित गर्न सक्नुहुन्छ:

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

> **Note:** Phi-4 समर्थन MLX Swift Examples रिपोजिटरीमा फेब्रुअरी 2025 को अन्त्यमा थपिएको हो ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))। मार्च 2025 सम्म, डिसेम्बर 2024 को आधिकारिक रिलीज (2.21.2) मा Phi-4 समर्थन समावेश छैन। Phi-4 मोडेलहरू प्रयोग गर्न, तपाईंले मुख्य ब्रान्चबाट सोझै प्याकेज रेफरेन्स गर्नुपर्नेछ:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

यसले आधिकारिक रिलीज अघि नै Phi-4 सहित नयाँ मोडेल कन्फिगरेसनहरू पहुँच दिन्छ। यस तरिकाले, तपाईं फरक Phi मोडेल संस्करणहरू वा MLX फर्म्याटमा रूपान्तरण गरिएका अन्य मोडेलहरू पनि प्रयोग गर्न सक्नुहुन्छ।

## चरण 6: UI बनाउनुहोस्

अब, हाम्रो ViewModel सँग अन्तरक्रिया गर्न सरल च्याट इन्टरफेस कार्यान्वयन गरौं:

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

UI तीन मुख्य कम्पोनेन्टहरू मिलेर बनेको छ जसले आधारभूत च्याट इन्टरफेस तयार पार्छ। `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` ले AI ले प्रक्रिया गरिरहेको देखाउन सरल एनिमेटेड संकेत दिन्छ।

## चरण 7: एप बनाउने र चलाउने

अब एप बनाउने र चलाउन तयार छौं।

> **Important!** MLX सिम्युलेटरलाई समर्थन गर्दैन। तपाईंले एपलाई Apple Silicon चिप भएको भौतिक डिभाइसमा मात्र चलाउनुपर्नेछ। थप जानकारीका लागि [यहाँ](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) हेर्नुहोस्।

एप सुरु हुँदा, "Load model" बटन थिचेर Phi-3 (वा तपाईंको कन्फिगरेसन अनुसार Phi-4) मोडेल डाउनलोड र इनिसियलाइज गर्नुहोस्। यो प्रक्रिया इन्टरनेट कनेक्शन अनुसार केही समय लाग्न सक्छ किनभने मोडेल Hugging Face बाट डाउनलोड हुँदैछ। हाम्रो कार्यान्वयनमा लोडिङ देखाउन स्पिनर मात्र छ, तर वास्तविक प्रगति Xcode कन्सोलमा हेर्न सकिन्छ।

लोड भएपछि, तपाईं मोडेलसँग अन्तरक्रिया गर्न टेक्स्ट फिल्डमा प्रश्न टाइप गरी पठाउन सक्नुहुन्छ।

iPad Air M1 मा चलिरहेको हाम्रो एप यसरी देखिन्छ:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## निष्कर्ष

त्यसोभए यति नै! यी चरणहरू पालना गरेर, तपाईंले Apple को MLX फ्रेमवर्क प्रयोग गरी डिभाइसमै सिधै Phi-3 (वा Phi-4) मोडेल चलाउने iOS एप्लिकेशन बनाउनु भयो।

बधाई छ!

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको प्रयास गर्छौं, तर कृपया जान्नुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।