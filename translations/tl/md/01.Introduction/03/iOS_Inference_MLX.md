# Pagpapatakbo ng Phi-3 at Phi-4 sa iOS gamit ang Apple MLX Framework

Ipinapakita ng tutorial na ito kung paano gumawa ng iOS application na nagpapatakbo ng Phi-3 o Phi-4 na modelo nang direkta sa device, gamit ang Apple MLX framework. Ang [MLX](https://opensource.apple.com/projects/mlx/) ay machine learning framework ng Apple na in-optimize para sa Apple Silicon chips.

## Mga Kinakailangan

- macOS na may Xcode 16 (o mas mataas)
- iOS 18 (o mas mataas) na target device na may hindi bababa sa 8GB (iPhone o iPad na compatible sa Apple Intelligence requirements, dahil kahalintulad ito sa mga kinakailangan ng quantized Phi)
- pangunahing kaalaman sa Swift at SwiftUI

## Hakbang 1: Gumawa ng Bagong iOS Project

Magsimula sa paggawa ng bagong iOS project sa Xcode:

1. buksan ang Xcode at piliin ang "Create a new Xcode project"
2. piliin ang "App" bilang template
3. pangalanan ang iyong project (halimbawa, "Phi3-iOS-App") at piliin ang SwiftUI bilang interface
4. pumili ng lokasyon kung saan ise-save ang iyong project

## Hakbang 2: Idagdag ang Mga Kinakailangang Dependencies

Idagdag ang [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) na naglalaman ng lahat ng kinakailangang dependencies at helpers para sa preloading ng mga modelo at pagsasagawa ng inference:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Bagaman sapat na ang base [MLX Swift package](https://github.com/ml-explore/mlx-swift) para sa core tensor operations at basic ML functionality, nagbibigay ang MLX Examples package ng ilang karagdagang bahagi na idinisenyo para sa paggamit ng mga language model, at pagpapadali ng proseso ng inference:

- mga utility para sa pag-load ng modelo na humahawak ng pag-download mula sa Hugging Face
- integrasyon ng tokenizer
- mga helper para sa inference sa text generation
- pre-configured na mga depinisyon ng modelo

## Hakbang 3: I-configure ang Entitlements

Para payagan ang app na mag-download ng mga modelo at maglaan ng sapat na memorya, kailangan nating magdagdag ng mga partikular na entitlements. Gumawa ng `.entitlements` file para sa iyong app na may sumusunod na nilalaman:

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

> **Note:** Mahalaga ang `com.apple.developer.kernel.increased-memory-limit` entitlement para sa pagpapatakbo ng mas malalaking modelo, dahil pinapayagan nito ang app na humiling ng mas malaking memorya kaysa karaniwang pinapayagan.

## Hakbang 4: Gumawa ng Chat Message Model

Una, gumawa tayo ng simpleng istruktura para kumatawan sa ating mga chat message:

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

## Hakbang 5: I-implementa ang ViewModel

Susunod, gagawa tayo ng `PhiViewModel` class na humahawak sa pag-load ng modelo at inference:

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

Ipinapakita ng ViewModel ang mga pangunahing punto ng integrasyon sa MLX:

- pagtatakda ng GPU cache limits gamit ang `MLX.GPU.set(cacheLimit:)` para i-optimize ang paggamit ng memorya sa mga mobile device
- paggamit ng `LLMModelFactory` para i-download ang modelo kapag kailangan at i-initialize ang MLX-optimized na modelo
- pag-access sa mga parameter at istruktura ng modelo sa pamamagitan ng `ModelContainer`
- paggamit ng MLX token-by-token generation gamit ang `MLXLMCommon.generate` method
- pamamahala sa proseso ng inference gamit ang angkop na temperature settings at token limits

Ang paraan ng streaming token generation ay nagbibigay ng agarang feedback sa mga user habang nagge-generate ng teksto ang modelo. Katulad ito ng paraan ng mga server-based na modelo, na nag-stream ng mga token pabalik sa user, ngunit walang delay ng network requests.

Sa aspeto ng UI interaction, ang dalawang pangunahing function ay `loadModel()`, na nag-i-initialize ng LLM, at `fetchAIResponse()`, na nagpoproseso ng input ng user at nagge-generate ng AI responses.

### Mga konsiderasyon sa format ng modelo

> **Important:** Hindi maaaring gamitin ang Phi models para sa MLX sa kanilang default o GGUF format. Kailangan silang i-convert sa MLX format, na ginagawa ng MLX community. Makakakita ka ng mga pre-converted na modelo sa [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Kasama sa MLX Examples package ang mga pre-configured na registration para sa ilang mga modelo, kabilang ang Phi-3. Kapag tinawag mo ang `ModelRegistry.phi3_5_4bit`, ito ay tumutukoy sa isang partikular na pre-converted na MLX model na awtomatikong ida-download:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Maaari kang gumawa ng sarili mong mga configuration ng modelo para ituro sa anumang compatible na modelo sa Hugging Face. Halimbawa, para gamitin ang Phi-4 mini, maaari kang gumawa ng sarili mong configuration:

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

> **Note:** Idinagdag ang suporta para sa Phi-4 sa MLX Swift Examples repository noong katapusan ng Pebrero 2025 (sa [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Hanggang Marso 2025, ang pinakabagong opisyal na release (2.21.2 mula Disyembre 2024) ay walang built-in na suporta para sa Phi-4. Para magamit ang Phi-4 models, kailangan mong i-reference ang package direkta mula sa main branch:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Binibigyan ka nito ng access sa pinakabagong mga configuration ng modelo, kabilang ang Phi-4, bago pa man ito maisama sa opisyal na release. Maaari mong gamitin ang paraang ito para gumamit ng iba't ibang bersyon ng Phi models o iba pang mga modelo na na-convert sa MLX format.

## Hakbang 6: Gumawa ng UI

Ngayon, i-implement natin ang isang simpleng chat interface para makipag-ugnayan sa ating view model:

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

Binubuo ang UI ng tatlong pangunahing bahagi na nagtutulungan upang makabuo ng isang basic chat interface. Gumagawa ang `ContentView` ng two-state interface na nagpapakita ng loading button o chat interface depende sa pagiging handa ng modelo. Ipinapakita ng `MessageView` ang mga indibidwal na chat message nang iba depende kung ito ay mensahe ng user (nakahanay sa kanan, may asul na background) o sagot mula sa Phi model (nakahanay sa kaliwa, may kulay-abo na background). Nagbibigay naman ang `TypingIndicatorView` ng simpleng animated indicator na nagpapakita na nagpoproseso ang AI.

## Hakbang 7: Pagbuo at Pagpapatakbo ng App

Handa na tayong i-build at patakbuhin ang application.

> **Important!** Hindi sinusuportahan ng MLX ang simulator. Kailangan mong patakbuhin ang app sa isang physical device na may Apple Silicon chip. Tingnan [dito](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) para sa karagdagang impormasyon.

Kapag nag-launch ang app, pindutin ang "Load model" button para i-download at i-initialize ang Phi-3 (o, depende sa iyong configuration, Phi-4) na modelo. Maaaring tumagal ang prosesong ito depende sa iyong internet connection, dahil kailangan nitong i-download ang modelo mula sa Hugging Face. Ang implementasyon namin ay may spinner lang bilang indikasyon ng loading, pero makikita mo ang aktwal na progreso sa Xcode console.

Kapag na-load na, maaari ka nang makipag-ugnayan sa modelo sa pamamagitan ng pag-type ng mga tanong sa text field at pagpindot sa send button.

Ganito ang magiging takbo ng ating application, na tumatakbo sa iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Konklusyon

At ayan na! Sa pagsunod sa mga hakbang na ito, nakagawa ka ng iOS application na nagpapatakbo ng Phi-3 (o Phi-4) na modelo nang direkta sa device gamit ang Apple MLX framework.

Binabati kita!

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.