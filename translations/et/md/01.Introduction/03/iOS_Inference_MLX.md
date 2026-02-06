# Phi-3 ja Phi-4 käivitamine iOS-is Apple MLX raamistikuga

See juhend näitab, kuidas luua iOS-i rakendus, mis käivitab Phi-3 või Phi-4 mudeli otse seadmes, kasutades Apple MLX raamistikku. [MLX](https://opensource.apple.com/projects/mlx/) on Apple'i masinõppe raamistik, mis on optimeeritud Apple Silicon kiipidele.

## Eeltingimused

- macOS koos Xcode 16 (või uuemaga)
- iOS 18 (või uuem) sihtseade, millel on vähemalt 8GB mälu (iPhone või iPad, mis vastab Apple Intelligence nõuetele, kuna need on sarnased kvantiseeritud Phi nõuetega)
- põhiteadmised Swiftist ja SwiftUI-st

## Samm 1: Loo uus iOS-i projekt

Alusta uue iOS-i projekti loomisega Xcode'is:

1. käivita Xcode ja vali "Create a new Xcode project"
2. vali malliks "App"
3. anna projektile nimi (nt "Phi3-iOS-App") ja vali liideseks SwiftUI
4. vali asukoht, kuhu projekt salvestada

## Samm 2: Lisa vajalikud sõltuvused

Lisa [MLX Examples pakett](https://github.com/ml-explore/mlx-swift-examples), mis sisaldab kõiki vajalikke sõltuvusi ja abivahendeid mudelite eelkoormamiseks ja järelduste tegemiseks:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Kuigi [MLX Swift pakett](https://github.com/ml-explore/mlx-swift) oleks piisav põhiliste tensorite operatsioonide ja masinõppe funktsionaalsuse jaoks, pakub MLX Examples pakett mitmeid lisakomponente, mis on mõeldud keelemudelitega töötamiseks ja järeldusprotsessi lihtsustamiseks:

- mudeli laadimise tööriistad, mis haldavad allalaadimist Hugging Face'ist
- tokeniseerija integreerimine
- järeldusabivahendid tekstigeneratsiooniks
- eelkonfigureeritud mudeli definitsioonid

## Samm 3: Konfigureeri õigused

Et võimaldada rakendusel mudeleid alla laadida ja piisavalt mälu eraldada, tuleb lisada spetsiifilised õigused. Loo oma rakendusele `.entitlements` fail järgmise sisuga:

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

> **Märkus:** Õigus `com.apple.developer.kernel.increased-memory-limit` on oluline suuremate mudelite käivitamiseks, kuna see võimaldab rakendusel taotleda rohkem mälu, kui tavaliselt lubatud.

## Samm 4: Loo vestlussõnumite mudel

Alustame lihtsa struktuuri loomisega, et esindada vestlussõnumeid:

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

## Samm 5: Rakenda ViewModel

Järgmisena loome `PhiViewModel` klassi, mis haldab mudeli laadimist ja järeldusi:

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

ViewModel näitab MLX integratsiooni peamisi punkte:

- GPU vahemälu piirangute seadistamine `MLX.GPU.set(cacheLimit:)` abil, et optimeerida mälukasutust mobiilseadmetes
- `LLMModelFactory` kasutamine mudeli allalaadimiseks ja MLX-optimeeritud mudeli initsialiseerimiseks
- mudeli parameetrite ja struktuuri juurdepääs `ModelContainer` kaudu
- MLX-i tokenite kaupa generatsiooni kasutamine `MLXLMCommon.generate` meetodi abil
- järeldusprotsessi haldamine sobivate temperatuuriseadete ja tokenite piirangutega

Tokenite voogesituse generatsiooni lähenemine pakub kasutajatele kohest tagasisidet, kui mudel teksti genereerib. See sarnaneb serveripõhiste mudelite toimimisega, kus tokenid voogesitatakse kasutajale tagasi, kuid ilma võrguühenduse viivituseta.

UI interaktsiooni osas on kaks peamist funktsiooni: `loadModel()`, mis initsialiseerib LLM-i, ja `fetchAIResponse()`, mis töötleb kasutaja sisendit ja genereerib AI vastuseid.

### Mudeli formaadi kaalutlused

> **Oluline:** MLX-i jaoks mõeldud Phi mudeleid ei saa kasutada nende vaikimisi või GGUF formaadis. Need tuleb konverteerida MLX formaati, mida haldab MLX kogukond. Eelkonverteeritud mudelid leiad [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

MLX Examples pakett sisaldab eelkonfigureeritud registreerimisi mitmele mudelile, sealhulgas Phi-3. Kui kutsud `ModelRegistry.phi3_5_4bit`, viitab see spetsiifilisele eelkonverteeritud MLX mudelile, mis laaditakse automaatselt alla:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Sa saad luua oma mudeli konfiguratsioone, et viidata mis tahes ühilduvale mudelile Hugging Face'is. Näiteks, kui soovid kasutada Phi-4 mini mudelit, saad määratleda oma konfiguratsiooni:

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

> **Märkus:** Phi-4 tugi lisati MLX Swift Examples repository'sse 2025. aasta veebruari lõpus (PR [#216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Alates 2025. aasta märtsist ei sisalda viimane ametlik versioon (2.21.2 detsembrist 2024) sisseehitatud Phi-4 tuge. Phi-4 mudelite kasutamiseks pead viitama paketile otse põhiharust:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

See annab sulle juurdepääsu uusimatele mudeli konfiguratsioonidele, sealhulgas Phi-4-le, enne kui need ametlikku versiooni lisatakse. Seda lähenemist saab kasutada erinevate Phi mudelite versioonide või isegi teiste mudelite jaoks, mis on konverteeritud MLX formaati.

## Samm 6: Loo kasutajaliides

Rakendame nüüd lihtsa vestlusliidese, et suhelda meie ViewModeliga:

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

Kasutajaliides koosneb kolmest põhikomponendist, mis töötavad koos, et luua lihtne vestlusliides. `ContentView` loob kahe olekuga liidese, mis näitab kas laadimisnuppu või vestlusliidest sõltuvalt mudeli valmisolekust. `MessageView` kuvab individuaalseid vestlussõnumeid erinevalt, olenevalt sellest, kas need on kasutaja sõnumid (paremale joondatud, sinise taustaga) või Phi mudeli vastused (vasakule joondatud, halli taustaga). `TypingIndicatorView` pakub lihtsat animatsiooni, mis näitab, et AI töötleb.

## Samm 7: Rakenduse ehitamine ja käivitamine

Nüüd oleme valmis rakendust ehitama ja käivitama.

> **Oluline!** MLX ei toeta simulaatorit. Rakendust tuleb käivitada füüsilises seadmes, millel on Apple Silicon kiip. Vaata [siit](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) lisainfot.

Kui rakendus käivitub, vajuta "Load model" nuppu, et mudel Phi-3 (või, sõltuvalt konfiguratsioonist, Phi-4) alla laadida ja initsialiseerida. See protsess võib võtta aega sõltuvalt internetiühendusest, kuna see hõlmab mudeli allalaadimist Hugging Face'ist. Meie rakendus sisaldab ainult spinnerit laadimise näitamiseks, kuid tegelikku progressi saab näha Xcode'i konsoolis.

Kui mudel on laaditud, saad mudeliga suhelda, sisestades küsimusi tekstiväljale ja vajutades saatmisnuppu.

Siin on näide, kuidas meie rakendus peaks käituma, töötades iPad Air M1 seadmes:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Kokkuvõte

Ja ongi kõik! Järgides neid samme, oled loonud iOS-i rakenduse, mis käivitab Phi-3 (või Phi-4) mudeli otse seadmes, kasutades Apple'i MLX raamistikku.

Palju õnne!

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.