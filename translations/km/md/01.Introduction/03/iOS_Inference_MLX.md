# ការរត់ Phi-3 និង Phi-4 លើ iOS ជាមួយផ្នែកមុខ Apple MLX

មេរៀននេះបង្ហាញពីវិធីបង្កើតកម្មវិធី iOS ដែលរត់ម៉ូដែល Phi-3 ឬ Phi-4 ដោយផ្ទាល់លើឧបករណ៍ ដោយប្រើផ្នែកមុខ Apple MLX។ [MLX](https://opensource.apple.com/projects/mlx/) គឺជាផ្នែកមុខម៉ាស៊ីនរៀនរបស់ Apple ដែលទាន់សម័យសម្រាប់ឈីប Apple Silicon។

## គ្រឿងចាំបាច់

- macOS ជាមួយ Xcode 16 (ឬថ្មីជាង)
- ឧបករណ៍គោលដៅ iOS 18 (ឬថ្មីជាង) មានបណ្តោយអង្គចងចាំយ៉ាងតិច 8GB (iPhone ឬ iPad ដែលស្មើរតាមតម្រូវការស្ទាត់ជំនាញ Apple Intelligence ដូចជា តម្រូវការពហុមាត្រ Phi)
- ចំណេះដឹងមូលដ្ឋានអំពី Swift និង SwiftUI

## ជំហានទី 1: បង្កើតគម្រោង iOS ថ្មី

ចាប់ផ្តើមដោយបង្កើតគម្រោង iOS ថ្មីនៅក្នុង Xcode៖

1. បើក Xcode ហើយជ្រើស "Create a new Xcode project"
2. ជ្រើស "App" ជាតំបន់រៀបចំ
3. ឈ្មោះគម្រោងរបស់អ្នក (ឧ. "Phi3-iOS-App") ហើយជ្រើស SwiftUI ជាឥរិយាបថ
4. ជ្រើសទីតាំងសម្រាប់រក្សាទុកគម្រោងរបស់អ្នក

## ជំហានទី 2: បន្ថែមការទំនាក់ទំនងតម្រូវការ

បន្ថែម [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ដែលមានបណ្ដុំទំនាក់ទំនងនិងជំនួយសម្រាប់ការពិនិត្យម៉ូដែលនិងការធ្វើជម្រះ៖

```swift
// នៅក្នុង Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

ខណៈពេល [MLX Swift package](https://github.com/ml-explore/mlx-swift) មូលដ្ឋានគឺគ្រប់គ្រាន់សម្រាប់សកម្មភាព tensor មូលដ្ឋាននិងមុខងារ ML មូលដ្ឋាន កញ្ចប់ MLX Examples ផ្តល់ជម្រើសបន្ថែមសម្រាប់ការងារជាមួយម៉ូដែលភាសា និងធ្វើឲ្យដំណើរការជម្រះកាន់តែងាយស្រួល៖

- ឧបករណ៍ផ្ទុកម៉ូដែលដែលគ្រប់គ្រងការទាញយកពី Hugging Face
- ការរួមបញ្ចូល tokenizer
- ជំនួយការជម្រះសម្រាប់ការបង្កើតអត្ថបទ
- ការកំណត់ម៉ូដែលដែលបានកំណត់រួចជាស្រេច

## ជំហានទី 3: កំណត់ Entitlements

ដើម្បីអនុញ្ញាតឲ្យកម្មវិធីរបស់យើងទាញយកម៉ូដែលនិងចែកចាយអង្គចងចាំគ្រប់គ្រាន់ អ្នកត្រូវបន្ថែម entitlements ជាក់លាក់។ បង្កើតឯកសារ `.entitlements` សម្រាប់កម្មវិធីរបស់អ្នកដែលមានខ្លឹមសារដូចខាងក្រោម៖

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

> **ចំណាំ៖** entitlement `com.apple.developer.kernel.increased-memory-limit` មានសារៈសំខាន់សម្រាប់ការរត់ម៉ូដែលធំៗ ព្រោះវាអនុញ្ញាតឲ្យកម្មវិធីអាចស្នើសុំអង្គចងចាំច្រើនជាងដែលបានអនុញ្ញាតធម្មតា។

## ជំហានទី 4: បង្កើតម៉ូដែលសារជជែក

ទីមុន តោះបង្កើតរចនាសម្ព័ន្ធមូលដ្ឋានសម្រាប់តំណាងសារជជែករបស់យើង៖

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

បន្ទាប់មក យើងនឹងបង្កើតថ្នាក់ `PhiViewModel` ដែលគ្រប់គ្រងការផ្ទុកម៉ូដែល និងការជម្រះ៖

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
            
            // Phi 3.5 mini ត្រូវបានកំណត់ជាមុននៅក្នុងឧទាហរណ៍ Swift MLX
            let modelConfig = ModelRegistry.phi3_5_4bit
            
            // Phi 4 mini អាចទាញយកពី Hugging Face បាន ប៉ុន្តែត្រូវការ​ឲ្យយោងឧទាហរណ៍ Swift MLX ពីសាខាធំ
            //let modelConfig = ModelConfiguration(
            //    id: "mlx-community/Phi-4-mini-instruct-4bit",
            //    defaultPrompt: "អ្នកគឺជាជំនួយការជួយបាន។",
            //    extraEOSTokens: ["<|end|>"]
            //)
            
            print("Loading \(modelConfig.name)...")
            self.modelContainer = try await LLMModelFactory.shared.loadContainer(
                configuration: modelConfig
            ) { progress in
                print("Download progress: \(Int(progress.fractionCompleted * 100))%")
            }
            
            // កត់ត្រាប៉ារ៉ាម៉ែត្រម៉ូដែល
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

- កំណត់ព្រំដែនស្មើ GPU ជាមួយ `MLX.GPU.set(cacheLimit:)` ដើម្បីធ្វើឲ្យការប្រើអង្គចងចាំលើឧបករណ៍ចល័តមានប្រសិទ្ធភាព
- ប្រើ `LLMModelFactory` ដើម្បីទាញយកម៉ូដែលដោយឆាប់រហ័ស និងចាប់ផ្តើមម៉ូដែលដែលបានបង្កើតឲ្យសមស្របដល់ MLX
- ចូលដំណើរការពន្យល់និងរចនាសម្ព័ន្ធម៉ូដែលតាមរយៈ `ModelContainer`
- ប្រើមុខងារ token-by-token នៃ MLX តាមរយៈវិធីសាស្រ្ត `MLXLMCommon.generate`
- គ្រប់គ្រងដំណើរការជម្រះដោយកំណត់សីតុណ្ហភាព និងកំណត់ព្រំ token ឲ្យសមរម្យ

វិធីសាស្រ្តផលិត token ជាបន្តផ្ទាល់ផ្តល់មធ្យោបាយឲ្យអ្នកប្រើប្រាស់ឆ្លើយតបភ្លាមៗ ខណៈដែលម៉ូដែលបង្កើតអត្ថបទ។ វាដូចជាអ្វីដែលម៉ូដែលមួយចំនួនបង្កើតនៅលើម៉ាស៊ីនមេ ដោយចាក់បញ្ចូល token ទៅអ្នកប្រើប្រាស់ โดยគ្មានការពន្យារពេលផ្ទាល់ប្រព័ន្ធបណ្តាញ។

នៅក្នុងចំណុចអន្តរកម្ម UI មុខងារសំខាន់គឺ `loadModel()` ដែលចាប់ផ្តើម LLM និង `fetchAIResponse()` ដែលដំណើរការបញ្ចូលពីអ្នកប្រើ និងបង្កើតចម្លើយ AI។

### ការពិចារណារូបមន្តម៉ូដែល

> **សំខាន់៖** ម៉ូដែល Phi សម្រាប់ MLX មិនអាចប្រើបានក្នុងរូបមន្តលំនាំដើម ឬ GGUF ទេ។ ត្រូវតែបម្លែងទៅជារូបមន្ត MLX ដែលគ្រប់គ្រងដោយសហគមន៍ MLX។ អ្នកអាចរកម៉ូដែលដែលបានបម្លែងរួចនៅ [huggingface.co/mlx-community](https://huggingface.co/mlx-community)។

កញ្ចប់ MLX Examples រួមបញ្ចូលការចុះបញ្ជីដែលបានកំណត់រួចសម្រាប់ម៉ូដែលជាច្រើន រួមទាំង Phi-3។ នៅពេលអ្នកហៅ `ModelRegistry.phi3_5_4bit` វាចង្អុលទៅម៉ូដែល MLX ដែលបានបម្លែងរួចជាក់លាក់មួយដែលនឹងត្រូវបានទាញយកស្វ័យប្រវត្តិ៖

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

អ្នកអាចបង្កើតការកំណត់ម៉ូដែលរបស់អ្នកឯង ដើម្បីចង្អុលទៅម៉ូដែលឆ្គាំឆ្គងណាមួយនៅលើ Hugging Face។ ឧទាហរណ៍ ដើម្បីប្រើ Phi-4 mini ជំនួស អ្នកអាចកំណត់ការកំណត់របស់អ្នកឯង៖

```swift
let phi4_mini_4bit = ModelConfiguration(
    id: "mlx-community/Phi-4-mini-instruct-4bit",
    defaultPrompt: "Explain quantum computing in simple terms.",
    extraEOSTokens: ["<|end|>"]
)

// បន្ទាប់មកប្រើការកំណត់នេះពេលធ្វើការបញ្ចូលម៉ូដែល
self.modelContainer = try await LLMModelFactory.shared.loadContainer(
    configuration: phi4_mini_4bit
) { progress in
    print("Download progress: \(Int(progress.fractionCompleted * 100))%")
}
```

> **ចំណាំ៖** សេចក្តីគាំទ្រសម្រាប់ Phi-4 ត្រូវបានបន្ថែមចូលក្នុងឃ្លាំង MLX Swift Examples នៅចុងខែកុម្ភៈ ២០២៥ (នៅក្នុង [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216))។ នៅខែមិនា ២០២៥ កំណែផ្លូវការថ្មីបំផុត (2.21.2 ពីធ្នូ ២០២៤) មិនរួមបញ្ចូលការគាំទ្រពីមូលដ្ឋានសម្រាប់ Phi-4 ទេ។ ដើម្បីប្រើម៉ូដែល Phi-4 អ្នកត្រូវយោងកញ្ចប់ពីសាខាចម្បងរបស់ repository:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

នេះអនុញ្ញាតឲ្យអ្នកចូលដំណើរការការកំណត់ម៉ូដែលថ្មីៗ រួមទាំង Phi-4 មុនពេលវាត្រូវបានបញ្ចូលទៅក្នុងការដាក់បញ្ចេញផ្លូវការ។ អ្នកអាចប្រើវិធីនេះដើម្បីប្រើវើស្យុងផ្សេងៗនៃម៉ូដែល Phi ឬម៉ូដែលផ្សេងទៀតដែលបានបម្លែងទៅរូបមន្ត MLX។

## ជំហានទី 6: បង្កើត UI

ឥឡូវនេះ តោះអនុវត្ត UI ជជែកសាមញ្ញសម្រាប់អន្តរកម្មជាមួយ view model របស់យើង៖

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

UI មានបីចំណុចសំខាន់ដែលរស់រវើកអោយធ្វើការរួមគ្នាបង្កើតចំណុចប្រជុំជជែកមូលដ្ឋាន។ `ContentView` បង្កើតអ៊ីនធ័រហ្វេសពីររដ្ឋដែលបង្ហាញ either ប៊ូតុងផ្ទុក ឬ អ៊ីនធ័រហ្វេសជជែក ដោយផ្អែកលើយោទ្ធភាពម៉ូដែល។ `MessageView` បង្ហាញសារជជែកនីមួយៗខុសគ្នា លើមូលដ្ឋានថាតើវាជាសារអ្នកប្រើប្រាស់ (ស្តាំ-បំណែកខៀវ) ឬចម្លើយ Phi ម៉ូដែល (ឆ្វេង-បំណែកសាប)។ `TypingIndicatorView` ផ្តល់កម្មវិធីបង្ហាញស្វ័យប្រវត្តិមួយសម្រាប់បង្ហាញថា AI កំពុងដំណើរការ។

## ជំហានទី 7: សាងសង់និងរត់កម្មវិធី

ឥឡូវនេះយើងរួចរាល់ក្នុងការសាងសង់និងរត់កម្មវិធី។

> **សំខាន់!** MLX មិនគាំទ្រការសាំល្បីល្បាញ។ អ្នកត្រូវរត់កម្មវិធីលើឧបករណ៍ធម្មតាមួយដែលមានឈីប Apple Silicon។ ព័ត៌មានលម្អិតសូមមើល [ទីនេះ](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)។

ពេលកម្មវិធីចាប់ផ្តើម ចុចប៊ូតុង "Load model" ដើម្បីទាញយកនិងចាប់ផ្តើមម៉ូដែល Phi-3 (ឬ Phi-4 តាមការកំណត់របស់អ្នក)។ ដំណើរការនេះអាចចំណាយពេលខ្លះ ប្រសិនបើឧបករណ៍ភ្ជាប់អ៊ីនធឺណិត ត្រូវទាញយកម៉ូដែលពី Hugging Face។ ការអនុវត្តរបស់យើងមានទียงតែសញ្ញាបង្វិលបង្ហាញការផ្ទុក ប៉ុន្តែអ្នកអាចមើលការរីកចម្រើនពិតនៅក្នុងកុងសូល Xcode។

ពេលបានបញ្ចូលរួច អ្នកអាចអន្តរកម្មជាមួយម៉ូដែលដោយវាយសំណួរនៅក្នុងប្រអប់អត្ថបទ ហើយចុចប៊ូតុងផ្ញើ។

នេះគឺជារបៀបកម្មវិធីរបស់យើងគួរតែអនុវត្តពេលរត់លើ iPad Air M1៖

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## សេចក្ដីសន្និដ្ឋាន

ហើយនេះហើយជាចុងក្រោយ! ដោយអនុវត្តតាមជំហានទាំងនេះ អ្នកបានបង្កើតកម្មវិធី iOS មួយដែលរត់ម៉ូដែល Phi-3 (ឬ Phi-4) ដោយផ្ទាល់លើឧបករណ៍ដោយប្រើផ្នែកមុខ Apple MLX។

សូមអបអរសាទរ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយបម្រើការបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងឱ្យមានភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែអូតូម៉ែតិកអាចមានកំហុសឬភាពខុសគ្នា។ ឯកសារដើមភាសាតំណាងសម្រាប់ប្រភពផ្លូវការដើម្បីយោង។ សម្រាប់ព័ត៌មានសំខាន់ ជំនាញការបកប្រែដោយមនុស្សជំនាញត្រូវបានផ្តល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->