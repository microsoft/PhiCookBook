<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:20:44+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "tl"
}
-->
# Running Phi-3 and Phi-4 on iOS with Apple MLX Framework

Ang tutorial na ito ay nagpapakita kung paano gumawa ng iOS application na nagpapatakbo ng Phi-3 o Phi-4 model nang on-device, gamit ang Apple MLX framework. Ang [MLX](https://opensource.apple.com/projects/mlx/) ay machine learning framework ng Apple na optimized para sa Apple Silicon chips.

## Prerequisites

- macOS na may Xcode 16 (o mas mataas)
- iOS 18 (o mas mataas) na target device na may hindi bababa sa 8GB (iPhone o iPad na compatible sa Apple Intelligence requirements, dahil kahalintulad ito sa quantized Phi requirements)
- basic na kaalaman sa Swift at SwiftUI

## Step 1: Create a New iOS Project

Magsimula sa paggawa ng bagong iOS project sa Xcode:

1. buksan ang Xcode at piliin ang "Create a new Xcode project"
2. piliin ang "App" bilang template
3. pangalanan ang project mo (halimbawa, "Phi3-iOS-App") at piliin ang SwiftUI bilang interface
4. piliin ang lokasyon kung saan ise-save ang project mo

## Step 2: Add Required Dependencies

Idagdag ang [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) na naglalaman ng lahat ng kinakailangang dependencies at helpers para sa pag-preload ng mga modelo at pag-perform ng inference:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Habang sapat na ang base [MLX Swift package](https://github.com/ml-explore/mlx-swift) para sa core tensor operations at basic ML functionality, ang MLX Examples package ay nagbibigay ng ilang dagdag na components na ginawa para sa pagtrabaho sa language models at para mapadali ang inference process:

- utilities para sa pag-load ng model na nagha-handle ng pag-download mula sa Hugging Face
- integration ng tokenizer
- inference helpers para sa text generation
- pre-configured na mga model definitions

## Step 3: Configure Entitlements

Para payagan ang app na mag-download ng mga modelo at mag-allocate ng sapat na memorya, kailangan nating magdagdag ng specific entitlements. Gumawa ng `.entitlements` file para sa iyong app na may sumusunod na nilalaman:

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

> **Note:** Mahalaga ang `com.apple.developer.kernel.increased-memory-limit` entitlement para sa pagpapatakbo ng mas malalaking modelo, dahil pinapayagan nito ang app na humiling ng mas malaking memorya kaysa sa karaniwang pinapayagan.

## Step 4: Create the Chat Message Model

Una, gumawa tayo ng basic na structure para i-represent ang ating chat messages:

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

## Step 5: Implement the ViewModel

Sunod, gagawa tayo ng `PhiViewModel` class na humahandle ng model loading at inference:

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

Ipinapakita ng ViewModel ang mga pangunahing MLX integration points:

- pag-set ng GPU cache limits gamit ang `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, na tumutukoy sa isang partikular na pre-converted MLX model na automatic na mada-download:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Pwede kang gumawa ng sarili mong model configurations para ituro sa kahit anong compatible na modelo sa Hugging Face. Halimbawa, para gamitin ang Phi-4 mini, pwede kang gumawa ng sarili mong configuration:

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

> **Note:** Nadagdag ang suporta para sa Phi-4 sa MLX Swift Examples repository sa katapusan ng Pebrero 2025 (sa [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Hanggang Marso 2025, ang pinakabagong official release (2.21.2 mula Disyembre 2024) ay walang built-in na suporta para sa Phi-4. Para magamit ang Phi-4 models, kailangan mong i-reference ang package diretso mula sa main branch:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Binibigyan ka nito ng access sa pinakabagong model configurations, kasama na ang Phi-4, bago pa man ito maisama sa official release. Pwede mong gamitin ang paraan na ito para gumamit ng iba't ibang bersyon ng Phi models o iba pang mga modelo na na-convert sa MLX format.

## Step 6: Create the UI

Gawin natin ngayon ang isang simpleng chat interface para makipag-interact sa ating view model:

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

Binubuo ang UI ng tatlong pangunahing bahagi na nagtutulungan para gumawa ng basic chat interface. Ang `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` ay nagbibigay ng simpleng animated indicator para ipakita na nagpoproseso ang AI

## Step 7: Building and Running the App

Handa na tayong i-build at patakbuhin ang application.

> **Important!** Hindi sinusuportahan ng MLX ang simulator. Kailangan mong patakbuhin ang app sa physical device na may Apple Silicon chip. Tingnan [dito](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) para sa karagdagang impormasyon.

Pag nag-launch ang app, i-tap ang "Load model" button para i-download at i-initialize ang Phi-3 (o, depende sa iyong configuration, Phi-4) model. Maaaring tumagal ito depende sa bilis ng iyong internet connection, dahil kailangan nitong i-download ang modelo mula sa Hugging Face. Ang implementation natin ay may spinner lang para ipakita ang loading, pero makikita mo ang aktwal na progreso sa Xcode console.

Kapag na-load na, pwede kang makipag-interact sa model sa pamamagitan ng pag-type ng mga tanong sa text field at pag-tap sa send button.

Ganito ang dapat na pag-andar ng ating application na tumatakbo sa iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Conclusion

At 'yan na! Sa pagsunod sa mga hakbang na ito, nakagawa ka ng iOS application na nagpapatakbo ng Phi-3 (o Phi-4) model nang direkta sa device gamit ang Apple MLX framework.

Congratulations!

**Pagsasabi ng Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.