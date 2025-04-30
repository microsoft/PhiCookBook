<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07ca611437b569633d7aacf855ecaa7e",
  "translation_date": "2025-04-04T12:01:30+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference_MLX.md",
  "language_code": "mo"
}
-->
# Phi-3 និង Phi-4 លើ iOS ដោយប្រើ Apple MLX Framework

សៀវភៅណែនាំនេះបង្ហាញពីរបៀបបង្កើតកម្មវិធី iOS ដែលដំណើរការម៉ូឌែល Phi-3 ឬ Phi-4 នៅលើឧបករណ៍ដោយប្រើ Apple MLX framework។ [MLX](https://opensource.apple.com/projects/mlx/) គឺជាគ្រោងការគណនាម៉ាស៊ីនរបស់ Apple ដែលបានបង្កើតឡើងសម្រាប់ឧបករណ៍ជាមួយឈីប Apple Silicon។

## លក្ខណៈត្រូវមាន

- macOS ជាមួយ Xcode 16 (ឬខ្ពស់ជាងនេះ)
- ឧបករណ៍ iOS 18 (ឬខ្ពស់ជាងនេះ) ដែលមានយ៉ាងហោចណាស់ 8GB (iPhone ឬ iPad ដែលសមស្របនឹងតម្រូវការបញ្ញាសិប្បនិម្មិតរបស់ Apple, ដែលប្រហែលជាដូចគ្នានឹងតម្រូវការម៉ូឌែល Phi ដែលបានបន្ថយទំហំ)
- ចំណេះដឹងមូលដ្ឋានអំពី Swift និង SwiftUI

## ជំហានទី 1: បង្កើតគម្រោង iOS ថ្មី

ចាប់ផ្តើមដោយបង្កើតគម្រោង iOS ថ្មីនៅក្នុង Xcode៖

1. បើក Xcode ហើយជ្រើស "Create a new Xcode project"
2. ជ្រើស "App" ជាទំរង់គំរូ
3. ដាក់ឈ្មោះគម្រោងរបស់អ្នក (ឧទាហរណ៍, "Phi3-iOS-App") និងជ្រើស SwiftUI ជាអន្តរកម្ម
4. ជ្រើសទីតាំងដើម្បីរក្សាទុកគម្រោងរបស់អ្នក

## ជំហានទី 2: បន្ថែម Dependencies ត្រូវការចាំបាច់

បន្ថែម [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ដែលមានផ្ទុកគ្រឿងផ្សំ និងឧបករណ៍ជំនួយសម្រាប់បញ្ចូលម៉ូឌែល និងធ្វើការវិភាគ៖

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

នៅពេលដែល [MLX Swift package](https://github.com/ml-explore/mlx-swift) ដើរតួជាមូលដ្ឋានសម្រាប់ប្រតិបត្តិការតិនស័រ និងមុខងារមូលដ្ឋាន ML, MLX Examples package ផ្តល់ឧបករណ៍បន្ថែមសម្រាប់ធ្វើការជាមួយម៉ូឌែលភាសា និងធ្វើឱ្យដំណើរការវិភាគកាន់តែងាយស្រួល៖

- ឧបករណ៍ផ្ទុកម៉ូឌែលដែលដោះស្រាយការទាញយកពី Hugging Face
- រួមបញ្ចូល tokenizer
- ជំនួយការវិភាគសម្រាប់បង្កើតអត្ថបទ
- កំណត់ម៉ូឌែលដែលបានកំណត់រួច

## ជំហានទី 3: កំណត់ Entitlements

ដើម្បីអនុញ្ញាតឱ្យកម្មវិធីរបស់យើងទាញយកម៉ូឌែល និងចែកចាយអង្គចងចាំគ្រប់គ្រាន់, យើងត្រូវបន្ថែម entitlements ជាក់លាក់។ បង្កើតឯកសារ `.entitlements` សម្រាប់កម្មវិធីរបស់អ្នកដោយមានមាតិកាដូចខាងក្រោម៖

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

> **សំគាល់៖** `com.apple.developer.kernel.increased-memory-limit` entitlement មានសារៈសំខាន់សម្រាប់ដំណើរការម៉ូឌែលធំៗ, ព្រោះវាអាចអោយកម្មវិធីស្នើសុំអង្គចងចាំច្រើនជាងដែលត្រូវបានអនុញ្ញាតដោយធម្មតា។

## ជំហានទី 4: បង្កើត Chat Message Model

ដំបូង, យើងនឹងបង្កើតរចនាសម្ព័ន្ធមូលដ្ឋានសម្រាប់តំណាងសារជជែក៖

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

## ជំហានទី 5: អនុវត្ត ViewModel

បន្ទាប់មក, យើងនឹងបង្កើតថ្នាក់ `PhiViewModel` ដែលដោះស្រាយការផ្ទុកម៉ូឌែល និងការវិភាគ៖

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

ViewModel បង្ហាញចំណុចសំខាន់នៃការរួមបញ្ចូល MLX៖

- កំណត់ដែនកំណត់ឃ្លាំង GPU ជាមួយ `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, វាមានការដកស្រង់ទៅម៉ូឌែល MLX ជាក់លាក់ដែលនឹងត្រូវបានទាញយកដោយស្វ័យប្រវត្តិ៖

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

អ្នកអាចបង្កើតការកំណត់រចនាសម្ព័ន្ធម៉ូឌែលផ្ទាល់ខ្លួនដើម្បីបញ្ជាក់ម៉ូឌែលណាមួយដែលសមស្របនៅ Hugging Face។ ឧទាហរណ៍, ដើម្បីប្រើ Phi-4 mini, អ្នកអាចកំណត់រចនាសម្ព័ន្ធផ្ទាល់ខ្លួន៖

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

> **សំគាល់៖** ការគាំទ្រ Phi-4 ត្រូវបានបន្ថែមទៅក្នុង MLX Swift Examples repository នៅចុងខែកុម្ភៈ 2025 (នៅក្នុង [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))។ រហូតដល់ខែមីនា 2025, ការចេញផ្សាយផ្លូវការចុងក្រោយបំផុត (2.21.2 ពីខែធ្នូ 2024) មិនមានការគាំទ្រ Phi-4។ ដើម្បីប្រើម៉ូឌែល Phi-4, អ្នកត្រូវយោងទៅកាន់ package ដោយផ្ទាល់ពីសាខាចម្បង៖

>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

នេះផ្តល់ឱ្យអ្នកនូវការចូលប្រើការកំណត់រចនាសម្ព័ន្ធម៉ូឌែលថ្មីបំផុត, រួមទាំង Phi-4, មុនពេលវាត្រូវបានបញ្ចូលក្នុងការចេញផ្សាយផ្លូវការណាមួយ។ អ្នកអាចប្រើវិធីសាស្រ្តនេះដើម្បីប្រើកំណែផ្សេងៗនៃម៉ូឌែល Phi ឬម៉ូឌែលផ្សេងទៀតដែលត្រូវបានបម្លែងទៅទ្រង់ទ្រាយ MLX។

## ជំហានទី 6: បង្កើត UI

ឥឡូវនេះ, យើងនឹងអនុវត្តចំណុចប្រទាក់ជជែកសាមញ្ញដើម្បីអន្តរកម្មជាមួយ view model របស់យើង៖

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

UI មានបីផ្នែកសំខាន់ដែលធ្វើការជាមួយគ្នាដើម្បីបង្កើតចំណុចប្រទាក់ជជែកមូលដ្ឋាន។ `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` ផ្តល់ឧបករណ៍សកម្មភាពសាមញ្ញសម្រាប់បង្ហាញថា AI កំពុងដំណើរការ។

## ជំហានទី 7: សាងសង់ និងដំណើរការកម្មវិធី

ឥឡូវនេះ, យើងត្រៀមសាងសង់ និងដំណើរការកម្មវិធីរួចរាល់។

> **សំខាន់!** MLX មិនគាំទ្រការសាកល្បងនៅលើស៊ីមុឡាទ័រ។ អ្នកត្រូវដំណើរការកម្មវិធីលើឧបករណ៍រូបធាតុដែលមានឈីប Apple Silicon។ មើល [នៅទីនេះ](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) សម្រាប់ព័ត៌មានបន្ថែម។

នៅពេលកម្មវិធីចាប់ផ្តើម, ចុចប៊ូតុង "Load model" ដើម្បីទាញយក និងចាប់ផ្តើមម៉ូឌែល Phi-3 (ឬ, អាស្រ័យលើការកំណត់រចនាសម្ព័ន្ធ, Phi-4)។ ដំណើរការនេះអាចចំណាយពេលព្រោះវាចាំបាច់ត្រូវទាញយកម៉ូឌែលពី Hugging Face។ ការអនុវត្តរបស់យើងមានតែ spinner ប៉ុណ្ណោះដើម្បីបង្ហាញការទាញយក, ប៉ុន្តែអ្នកអាចមើលការវិវត្តនៅក្នុង Xcode console។

បន្ទាប់ពីទាញយករួច, អ្នកអាចអន្តរកម្មជាមួយម៉ូឌែលដោយវាយសំណួរនៅក្នុងប្រអប់អត្ថបទ ហើយចុចប៊ូតុងផ្ញើ។

នេះគឺជារបៀបដែលកម្មវិធីរបស់យើងគួរតែដំណើរការលើ iPad Air M1៖

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## សេចក្តីសន្និដ្ឋាន

ហើយនេះគឺជាការស្រេច! ដោយអនុវត្តតាមជំហានទាំងនេះ, អ្នកបានបង្កើតកម្មវិធី iOS ដែលដំណើរការម៉ូឌែល Phi-3 (ឬ Phi-4) ដោយផ្ទាល់នៅលើឧបករណ៍ដោយប្រើ Apple MLX framework។

អបអរសាទរ!

It seems you are asking for a translation into "mo." Could you clarify what "mo" refers to? Are you requesting a translation into a specific language, such as Maori (mi), Mongolian (mn), or another language? Let me know, and I'll be happy to assist!