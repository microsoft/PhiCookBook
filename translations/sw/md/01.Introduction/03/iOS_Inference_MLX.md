<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:21:19+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "sw"
}
-->
# Kuendesha Phi-3 na Phi-4 kwenye iOS kwa kutumia Apple MLX Framework

Mafunzo haya yanaonyesha jinsi ya kuunda programu ya iOS inayoweza kuendesha modeli ya Phi-3 au Phi-4 kwenye kifaa, kwa kutumia Apple MLX framework. [MLX](https://opensource.apple.com/projects/mlx/) ni mfumo wa mashine za kujifunza wa Apple ulioboreshwa kwa ajili ya chips za Apple Silicon.

## Mahitaji

- macOS yenye Xcode 16 (au juu zaidi)
- Kifaa lengwa cha iOS 18 (au juu zaidi) chenye angalau 8GB (iPhone au iPad kinachokidhi mahitaji ya Apple Intelligence, kwani haya ni sawa na mahitaji ya modeli za Phi zilizoquantize)
- ujuzi wa msingi wa Swift na SwiftUI

## Hatua ya 1: Unda Mradi Mpya wa iOS

Anza kwa kuunda mradi mpya wa iOS katika Xcode:

1. fungua Xcode na chagua "Create a new Xcode project"
2. chagua "App" kama template
3. panga jina la mradi wako (mfano, "Phi3-iOS-App") na chagua SwiftUI kama interface
4. chagua mahali pa kuhifadhi mradi wako

## Hatua ya 2: Ongeza Maktaba Zinazohitajika

Ongeza kifurushi cha [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ambacho kina maktaba zote muhimu na msaada wa kupakia modeli na kufanya inference:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Ingawa kifurushi cha msingi cha [MLX Swift package](https://github.com/ml-explore/mlx-swift) kinatosha kwa shughuli za msingi za tensor na kazi za mashine za kujifunza, kifurushi cha MLX Examples kinatoa vipengele vingine vingi vinavyolenga kazi na modeli za lugha, na kurahisisha mchakato wa inference:

- zana za kupakia modeli zinazoshughulikia kupakua kutoka Hugging Face
- ujumuishaji wa tokenizer
- msaada wa inference kwa ajili ya uzalishaji wa maandishi
- ufafanuzi wa modeli uliowekwa tayari

## Hatua ya 3: Sanidi Ruhusa

Ili kuruhusu programu yetu kupakua modeli na kupata kumbukumbu ya kutosha, tunahitaji kuongeza ruhusa maalum. Unda faili la `.entitlements` kwa programu yako yenye maudhui yafuatayo:

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

> **Note:** Ruhusa ya `com.apple.developer.kernel.increased-memory-limit` ni muhimu kwa kuendesha modeli kubwa zaidi, kwani inaruhusu programu kuomba kumbukumbu zaidi kuliko kawaida inavyoruhusiwa.

## Hatua ya 4: Unda Muundo wa Ujumbe wa Chat

Kwanza, tunda muundo wa msingi unaowakilisha ujumbe wetu wa mazungumzo:

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

## Hatua ya 5: Tekeleza ViewModel

Ifuatayo, tutaunda darasa la `PhiViewModel` linaloshughulikia upakiaji wa modeli na inference:

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

ViewModel inaonyesha sehemu muhimu za ujumuishaji wa MLX:

- kuweka mipaka ya cache ya GPU kwa kutumia `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, inarejelea modeli maalum ya MLX iliyobadilishwa awali ambayo itapakuliwa kiotomatiki:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Unaweza kuunda usanidi wako wa modeli kuonyesha modeli yoyote inayolingana kwenye Hugging Face. Kwa mfano, kutumia Phi-4 mini badala yake, unaweza kufafanua usanidi wako:

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

> **Note:** Msaada wa Phi-4 uliongezwa kwenye hazina ya MLX Swift Examples mwishoni mwa Februari 2025 (katika [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Hadi Machi 2025, toleo la hivi karibuni rasmi (2.21.2 kutoka Desemba 2024) halijajumuisha msaada wa Phi-4. Ili kutumia modeli za Phi-4, unahitaji kurejelea kifurushi moja kwa moja kutoka tawi kuu:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Hii inakupa ufikiaji wa usanidi wa hivi karibuni wa modeli, ikiwa ni pamoja na Phi-4, kabla hayajajumuishwa kwenye toleo rasmi. Unaweza kutumia njia hii kutumia matoleo tofauti ya modeli za Phi au hata modeli nyingine zilizobadilishwa kwa muundo wa MLX.

## Hatua ya 6: Unda UI

Sasa tutaweka kiolesura rahisi cha mazungumzo kuwasiliana na view model yetu:

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

UI ina sehemu kuu tatu zinazofanya kazi pamoja kuunda kiolesura cha msingi cha mazungumzo. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` hutoa kiashiria rahisi cha kusogea kinachoonyesha kwamba AI inaendelea kuchakata

## Hatua ya 7: Kujenga na Kuendesha Programu

Sasa tuko tayari kujenga na kuendesha programu.

> **Important!** MLX haitegemezi simulator. Lazima uendeshe programu kwenye kifaa halisi chenye chip ya Apple Silicon. Angalia [hapa](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) kwa maelezo zaidi.

Programu itakapozinduliwa, gonga kitufe cha "Load model" kupakua na kuanzisha modeli ya Phi-3 (au, kulingana na usanidi wako, Phi-4). Mchakato huu unaweza kuchukua muda kulingana na muunganisho wako wa intaneti, kwani unahusisha kupakua modeli kutoka Hugging Face. Utekelezaji wetu unajumuisha tu spina kuonyesha upakiaji, lakini unaweza kuona maendeleo halisi kwenye koni ya Xcode.

Baada ya kupakuliwa, unaweza kuwasiliana na modeli kwa kuandika maswali kwenye sehemu ya maandishi na kugonga kitufe cha kutuma.

Hivi ndivyo programu yetu inavyopaswa kufanya kazi, ikionyeshwa kwenye iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Hitimisho

Na hapo umefanya! Kwa kufuata hatua hizi, umeunda programu ya iOS inayoweza kuendesha modeli ya Phi-3 (au Phi-4) moja kwa moja kwenye kifaa kwa kutumia Apple MLX framework.

Hongera!

**Kifungu cha kutanguliza**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatubebeki dhima kwa maelewano mabaya au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.