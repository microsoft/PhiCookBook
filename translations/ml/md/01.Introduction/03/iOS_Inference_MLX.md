# iOS ൽ Apple MLX ഫ്രെയിംവർക്കുമായി Phi-3 மற்றும் Phi-4 പ്രവർത്തിപ്പിക്കൽ

ഈ ട്യൂട്ടോറിയൽ Apple MLX ഫ്രെയിംവർക്കാണ് ഉപയോഗിച്ച് Phi-3 അല്ലെങ്കിൽ Phi-4 മോഡൽ സജ്ജീകരണത്തിലല്ലാതെ (on-device) ഓടിക്കുന്ന iOS ആപ് എങ്ങനെ സൃഷ്ടിക്കാമെന്നത് കാണിക്കുന്നു. [MLX](https://opensource.apple.com/projects/mlx/) ആണ് Apple Silicon ചിപ്പുകൾക്ക് ഒപ്റ്റിമൈസ്ഡ് ചെയ്ത Apple-യുടെ മെഷീൻ ലേണിംഗ് ഫ്രെയിംവർക്ക്.

## ആവശ്യമായ മുൻ‌പരീക്ഷണങ്ങൾ

- Xcode 16 (അഥവാ അതിനേക്കാൾ ഉയർന്ന) ഉള്ള macOS
- കുറഞ്ഞത് 8GB മെമ്മറി ഉള്ള iOS 18 (അഥവാ ഉയർന്ന) ലക്ഷ്യ ഡിവൈസ് (Apple Intelligence ആവശ്യകതകൾ നിറവേറ്റുന്ന iPhone അല്ലെങ്കിൽ iPad, കാരണം അവ quantized Phi ആവശ്യകതകളുമായി സാദൃശ്യമാകും)
- Swift, SwiftUI എന്നിവയുടെ അടിസ്ഥാനജ്ഞാനം

## ഘട്ടം 1: പുതിയ iOS പ്രൊജക്‌ട് സൃഷ്ടിക്കുക

Xcode-ൽ പുതിയ iOS പ്രൊജക്‌ട് സൃഷ്ടിച്ച് ആരംഭിക്കുക:

1. Xcode തുറന്ന് "Create a new Xcode project" തിരഞ്ഞെടുക്കുക
2. ടെംപ്ലേറ്റായി "App" തിരഞ്ഞെടുക്കുക
3. നിങ്ങളുടെ പ്രൊജക്‌ടിന് പേര് നൽകര (ഉദാ., "Phi3-iOS-App") കൂടാതെ ഇന്റർഫേസിന് SwiftUI തിരഞ്ഞടുക്കുക
4. പ്രൊജക്‌ട് സേവ് ചെയ്യാനുള്ള സ്ഥലം തിരഞ്ഞെടുക്കുക

## ഘട്ടം 2: ആവശ്യമായ ഡിപെൻഡൻസികൾ ചേർക്കുക

പ്രതിസന്ധിയില്ലാതെ മോഡലുകൾ പ്രീലോഡ് ചെയ്യാനും ഇൻഫറൻസ് നടത്താനുമുള്ള എല്ലാ സഹായകങ്ങളും ഉൾക്കൊള്ളുന്ന [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ചേർക്കുക:

```swift
// Xcode-ൽ: ഫയൽ > പാക്കേജ് ആശ്രിതത്വങ്ങൾ ചേർക്കുക
// URL: https://github.com/ml-explore/mlx-swift-examples
```

മൂലപരമായി കോർ ടെൻസർ ഓപ്പറേഷനുകളുടെ және അടിസ്ഥാന ML ഫംഗ്ഷണാലിറ്റി വേണ്ടി [MLX Swift package](https://github.com/ml-explore/mlx-swift) മതിയാകും എങ്കിലും, MLX Examples package ഭാഷാ മോഡലുകൾ തുടങ്ങിയവ കൈകാര്യം ചെയ്യുന്നതിനും ഇൻഫറൻസ് പ്രക്രിയ എളുപ്പമാക്കുന്നതിനും രൂപകൽപ്പന ചെയ്ത അധിക ഘടകങ്ങൾ നൽകുന്നു:

- Hugging Face-ൽ നിന്ന് ഡൗൺലോഡ് ചെയ്യുന്നത് കൈകാര്യം ചെയ്യുന്ന മോഡൽ ലോഡിംഗ് ഉപകരണങ്ങൾ
- ടോക്കിനൈസർ ഇൻടഗ്രേഷൻ
- ടെക്സ്റ്റ് ജനറേഷനിനുള്ള ഇൻഫറൻസ് സഹായങ്ങൾ
- മുൻകൂട്ടി കോൺഫിഗർ ചെയ്ത മോഡൽ നിർവചനങ്ങൾ

## ഘട്ടം 3: എൻറ്റൈറ്റിൽമെന്റുകൾ കോൺഫിഗർ ചെയ്യുക

അപ്ലിക്കേഷൻ മോഡലുകൾ ഡൗൺലോഡ് ചെയ്യാനും മതിയായ മെമ്മറി വകവരുത്താനുമുള്ള അനുമതികൾ നൽകാൻ, നമുക്ക് പ്രത്യേക എൻറ്റൈറ്റിൽമെന്റുകൾ ചേർക്കേണ്ടതുണ്ട്. നിങ്ങളുടെ ആപ്പിനായി `.entitlements` ഫയൽ താഴെ ഉള്ള ഉള്ളടക്കത്തോടെ സൃഷ്ടിക്കുക:

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

> **കുറിപ്പ്:** വലിയ മോഡലുകൾ ഓടിക്കുന്നതിനായി `com.apple.developer.kernel.increased-memory-limit` എൻറ്റൈറ്റിൽമെന്റ് പ്രധാനമാണ്, ഇത് ആപ്പിന് സാധാരണ അനുവദിച്ചതിന്മുകളിൽ കൂടുതൽ മെമ്മറി ആവശ്യപ്പെടാൻ അനുവദിക്കുന്നു.

## ഘട്ടം 4: ചാറ്റ് സന്ദേശ മോഡൽ സൃഷ്ടിക്കുക

മുമ്പ്, നമുക്ക് നമ്മുടെ ചാറ്റ് സന്ദേശങ്ങളെ പ്രതിനിധീകരിക്കാൻ ഒരു അടിസ്ഥാന ഘടന സൃഷ്ടിക്കാം:

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

## ഘട്ടം 5: ViewModel നടപ്പിലാക്കുക

അടുത്തതായി, മോഡൽ ലോഡിംഗും ഇൻഫറൻസും കൈകാര്യം ചെയ്യുന്നതിനുള്ള `PhiViewModel` ക്ലാസ് സൃഷ്ടിക്കാം:

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
            
            // Phi 3.5 മിനി Swift MLX ഉദാഹരണങ്ങളിൽ മുൻകൂട്ടി ക്രമീകരിച്ചിരിക്കുന്നു
            let modelConfig = ModelRegistry.phi3_5_4bit
            
            // Phi 4 മിനി Hugging Face-ൽ നിന്ന് ലഭിക്കാവുന്നതാണ്, പക്ഷേ പ്രധാന ബ്രാഞ്ചിലുള്ള Swift MLX ഉദാഹരണങ്ങളെ റഫറൻസ് ചെയ്യേണ്ടതാണ്
            //let modelConfig = ModelConfiguration(
            //    id: "mlx-community/Phi-4-mini-instruct-4bit",
            //    defaultPrompt: "നിങ്ങൾ സഹായകരമായൊരു അസിസ്റ്റന്റാണ്."
            //    extraEOSTokens: ["<|end|>"]
            //)
            
            print("Loading \(modelConfig.name)...")
            self.modelContainer = try await LLMModelFactory.shared.loadContainer(
                configuration: modelConfig
            ) { progress in
                print("Download progress: \(Int(progress.fractionCompleted * 100))%")
            }
            
            // മോഡൽ പാരാമീറ്ററുകൾ ലോഗ് ചെയ്യുക
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

ViewModel താഴെ പറയുന്ന പ്രധാന MLX ഇന്റഗ്രേഷൻ പോയിന്റുകൾ പ്രകടിപ്പിക്കുന്നു:

- മൊബൈൽ ഡിവൈസുകളിൽ മെമ്മറി ഉപയോഗം Optimize ചെയ്യാൻ `MLX.GPU.set(cacheLimit:)` ഉപയോഗിച്ച് GPU cache പരിധികൾ സജ്ജീകരിക്കൽ
- മോഡൽ ഓൺ-ഡിമാൻഡ് ഡൗൺലോഡ് ചെയ്ത് MLX-ഓപ്‌റ്റിമൈസ്ഡ് മോഡലായി ഇൻഷെഷ്യലൈസ് ചെയ്യാൻ `LLMModelFactory` ഉപയോഗിക്കൽ
- മോഡലിന്റെ പാരാമീറ്ററുകളും ഘടനയും `ModelContainer` വഴി ആക്സസ് ചെയ്യൽ
- MLX-യുടെ ടോക്കൺ-ബൈ-ടോക്കൺ ജനറേഷൻ `MLXLMCommon.generate` മെത്തഡ് ഉപയോഗിച്ച് പ്രയോഗിക്കൽ
- അനുയോജ്യമായ ടേംപറേച്ചർ സെറ്റിംഗ്‌സ്, ടോക്കൺ വരമ്പ് എന്നിവയോടെ ഇൻഫറൻസ് പ്രക്രിയ കൈകാര്യം ചെയ്യൽ

ടോക്കൺ സ്ട്രീമിംഗ് ജനറേഷൻ സമീപനം മോഡൽ ടെക്സ്റ്റ് ജനറേറ്റ് ചെയ്യുമ്പോൾ ഉപയോക്താവിന് ഉടൻ ഫീഡ്ബാക്ക് നൽകുന്നു. ഇത് സെർവര്‍-അധിഷ്ഠിത മോഡലുകൾ മേഖലയിൽ പ്രവർത്തിക്കുന്ന വിധത്തോട് സാദൃശ്യമാണ്, എന്നാല്‍ നെറ്റ്വർക്ക് അഭ്യർത്ഥനകളുടെ വൈകിയത ഇല്ലാതെ.

UI ഇന്ററാക്ഷന്റെ കാര്യത്തിൽ, രണ്ട് പ്രധാന ഫംഗ്ഷനുകൾ `loadModel()` (LLM ഇൻഷെഷ്യലൈസ് ചെയ്യുന്നത്) കൂടാതെ `fetchAIResponse()` (ഉപയോക്തൃ ഇൻപുട്ട് പ്രോസസ് ചെയ്ത് AI പ്രതികരണങ്ങൾ ജനറേറ്റ് ചെയ്യുന്നത്) ആണ്.

### മോഡൽ ഫോർമാറ്റ് പരിഗണനകൾ

> **പ്രധാനമാണ്:** MLX-യ്ക്ക് വേണ്ടി Phi മോഡലുകൾ അവരുടെ ഡീഫോൾട്ട് അല്ലെങ്കിൽ GGUF ഫോർമാറ്റിൽ നേരിട്ട് ഉപയോഗിക്കാനാകില്ല. അവ MLX ഫോർമാറ്റിലേക്ക് കൺവേർട്ട് ചെയ്യേണ്ടതാണ്, ഇത് MLX കമ്മ്യൂണിറ്റി കൈകാര്യം ചെയ്യുന്നു. മുൻകൂട്ടി കൺവേർട്ടുചെയ്‌ത മോഡലുകൾ [huggingface.co/mlx-community](https://huggingface.co/mlx-community)ൽ ലഭ്യമാണ്.

MLX Examples package бірнеше മോഡലുകൾക്കുള്ള മുൻകൂട്ടി കോൺഫിഗർ ചെയ്ത രജിസ്ട്രേഷൻहरू ഉൾക്കൊള്ളുന്നു, Phi-3 ഉൾപ്പെടെ. നിങ്ങൾ `ModelRegistry.phi3_5_4bit` വിളിക്കുമ്പോൾ, അതു ഓൺ-ഡിമാൻഡ് ഡൗൺലോഡ് ചെയ്യപ്പെടുന്ന ഒരു പ്രത്യേക മുൻകൂട്ടി കൺവേർട്ടുചെയ്‌ത MLX മോഡലിനെ റഫറൻസ് ചെയ്യുന്നു:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

നിങ്ങൾക്ക് Hugging Face-ൽ ഉള്ള ഏതെങ്കിലും അനുയോജ്യമായ മോഡലിലേക്ക് പോയിന്റ് ചെയ്യാൻ നിങ്ങളുടെ സ്വന്തം മോഡൽ കോൺഫിഗറേഷനുകൾ സൃഷ്ടിക്കാമെന്നതാണ്. ഉദാഹരണത്തിന്, Phi-4 mini ഉപയോഗിക്കാൻ നിങ്ങൾക്ക് നിങ്ങളുടെ സ്വന്തം കോൺഫിഗറേഷൻ നിർവചിക്കാമായിരുന്നു:

```swift
let phi4_mini_4bit = ModelConfiguration(
    id: "mlx-community/Phi-4-mini-instruct-4bit",
    defaultPrompt: "Explain quantum computing in simple terms.",
    extraEOSTokens: ["<|end|>"]
)

// അതിന് ശേഷം മോഡൽ ലോഡ് ചെയ്യുമ്പോൾ ഈ ക്രമീകരണം ഉപയോഗിക്കുക
self.modelContainer = try await LLMModelFactory.shared.loadContainer(
    configuration: phi4_mini_4bit
) { progress in
    print("Download progress: \(Int(progress.fractionCompleted * 100))%")
}
```

> **കുറിപ്പ്:** Phi-4 സപ്പോർട്ട് MLX Swift Examples റിപ്പോസിറ്ററിയിൽ ഫെബ്രുവരി 2025 അവസാനം [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216) ൽ ചേർത്തു. മാർച്ച് 2025നുള്ള നിലവിലെ ഔദ്യോഗിക റിലീസ് (2024 ഡിസംബർ നിന്നുള്ള 2.21.2) ഇനിപ്പറയുന്നPhi-4 സപ്പോർട്ട് ഉൾക്കൊള്ളുന്നില്ല. Phi-4 മോഡലുകൾ ഉപയോഗിക്കാൻ, നിങ്ങൾക്ക് പാക്കേജ് നേരിട്ട് main ബ്രാഞ്ചിൽ നിന്നു റഫറൻസ് ചെയ്യേണ്ടതുണ്ട്:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

ഇതിലൂടെ നിങ്ങൾക്ക് Phi-4 ഉൾപ്പെടെ ഏറ്റവും പുതിയ മോഡൽ കോൺഫിഗറേഷനുകൾ ഔദ്യോഗിക റിലീസിലേക്കുമുമ്പ് ആക്സസ് ചെയ്യാം. വ്യത്യസ്ത Phi മോഡൽ പതിപ്പുകൾ അല്ലെങ്കിൽ MLX ഫോർമാറ്റിലേക്ക് കൺവേർട്ട് ചെയ്ത മറ്റ് മോഡലുകൾ ഉപയോഗിക്കാൻ ഈ സമീപനം ഉപയോഗിക്കാവുന്നതാണ്.

## ഘട്ടം 6: UI സൃഷ്ടിക്കുക

ഇപ്പോൾ നമുക്ക് നമ്മുടെ view model-നോട് ഇന്ററാക്റ്റ് ചെയ്യാൻ ഒരു ലളിതമായ ചാറ്റ് ഇന്റർഫേസ് നടപ്പിലാക്കാം:

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

UI മൂന്ന് പ്രധാന ഘടകങ്ങളായ സംയോജിതമായ രീതിയിൽ അടിസ്ഥാന ചാറ്റ് ഇന്റർഫേസ് സൃഷ്ടിക്കുന്നു. `ContentView` മോഡൽ റെഡിയാവുന്നവൻഅയോ അല്ലയോ എന്നതിന്റെ അടിസ്ഥാനത്തിൽ ലോഡിംഗ് ബട്ടണോ ചാറ്റ് ഇന്റർഫേസോ കാണിക്കുന്ന രണ്ട്-സ്റ്റെറ്റ് ഇന്റർഫേസ് ഉണ്ടാക്കുന്നു. `MessageView` ഉപയോക്താവിന്റെ സന്ദേശങ്ങൾ (വലത്-അലൈനഡ്, നീല പശ്ചാത്തലം) അല്ലെങ്കിൽ Phi മോഡൽ പ്രതികരണങ്ങൾ (ഇടം-അലൈനഡ്, കരുപ്പ്/ഗ്രേ പശ്ചാത്തലം) എന്നീ അടിസ്ഥാനത്തിൽ വ്യത്യസ്തമായി പ്രദർശിപ്പിക്കുന്നു. `TypingIndicatorView` AI പ്രോസസ്സ് ചെയ്യുന്നുണ്ടെന്ന് കാണിക്കാൻ ലളിതമായ ആനിമേറ്റഡ് സൂചിക നൽകുന്നു.

## ഘട്ടം 7: ആപ്പ് ബിൽഡ് ചെയ്ത് റൺ ചെയ്യുക

ആപ്പ് അവർണത്തിലാക്കി റൺ ചെയ്യാൻ ഇപ്പോൾ തയ്യാറാണ്.

> **പ്രധാനമാണ്!** MLX സിമുലേറ്ററെ പിന്തുണയ്ക്കുന്നില്ല. Apple Silicon ചിപ്പ് ഉള്ള ഫിസിക്കൽ ഡിവൈസിൽ ആപ്പ് റൺ ചെയ്യണം. കൂടുതൽ വിവരങ്ങൾക്ക് [ഇവിടം](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) കാണുക.

ആപ്പ് ലോഞ്ച് ചെയ്യുമ്പോൾ, Phi-3 (അഥവാ നിങ്ങളുടെ കോൺഫിഗറേഷനോട് അനുസരിച്ച് Phi-4) മോഡൽ ഡൗൺലോഡ് ചെയ്ത് ഇൻഷെഷ്യലൈസ് ചെയ്യാൻ "Load model" ബട്ടൺ ടാപ്പ് ചെയ്യുക. Hugging Face-ൽ നിന്നുള്ള മോഡൽ ഡൗൺലോഡ് ചെയ്യുന്നത് അടിസ്ഥാനപരമായി നടക്കുന്ന所以 ഇന്റർനെറ്റ് കണക്ഷന്റെ അടിസ്ഥാനത്തിൽ ഈ പ്രക്രിയക്ക് സമയമെടുക്കാം. നമ്മുടെ ഇമ്പ്ലിമെൻറേഷൻ ലോഡിംഗ് സൂചകമായി വലിയൊരു സ്പിന്നർ മാത്രമേ ഉൾക്കൊള്ളുന്നുള്ളു, പക്ഷേ യഥാർത്ഥ പ്രോഗ്രസ് Xcode കൺസോളിൽ കാണാം.

ലോഡ് ആകുന്നതിന് ശേഷം, ടെക്സ്റ്റ് ഫീൽഡിൽ ചോദ്യങ്ങൾ ടൈപ് ചെയ്ത് സെൻഡ് ബട്ടൺ ടാപ്പ് ചെയ്താൽ മോഡലുമായി സംവദിക്കാം.

എന്റെ അപ്ലിക്കേഷൻ iPad Air M1-ൽ ഓടുമ്പോൾ ഇത് എങ്ങനെ പെരുമാറണമെന്ന് ഇവിടെ കാണാം:

![ഡെമോ GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## ഉപസംഹാരം

ഇതോടെ انتهിയായി! ഈ ഘട്ടങ്ങൾ പിന്തുടർന്നാൽ, Apple-ന്റെ MLX ഫ്രെയിംവർക്കുപയോഗിച്ച് Phi-3 (അഥവാ Phi-4) മോഡൽ നേരിട്ട് ഡിവൈസിൽ ഓടിക്കുന്ന ഒരു iOS ആപ്പ് നിങ്ങൾ സൃഷ്ടിച്ചു.

അഭിനന്ദനങ്ങൾ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്ക്ലെയിമർ:
ഈ രേഖ AI വിവർത്തനസേവനമായ Co-op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണെന്ന് 알려ിക്കുന്നു. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകളും അച്ചടക്കഭേദങ്ങളും ഉണ്ടാവാൻ സാധ്യതയുണ്ടെന്ന് ദയവായി മനസിലാക്കുക. യഥാഭാഷയിലെ മൗലിക രേഖ അധികാരപ്രദമായ ഉറവിടമായി പരിഗണിക്കപ്പെടണം. നിർണ്ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശിക്കുന്നു. ഈ വിവർത്തനം ഉപയോഗത്തിലുണ്ടാകുന്ന തെറ്റിദ്ധാരണങ്ങളിലോ തെറ്റായ വ്യാഖ്യാനങ്ങളിലോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->