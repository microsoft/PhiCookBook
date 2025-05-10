<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:17:30+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "fi"
}
-->
# Phi-3:n ja Phi-4:n ajaminen iOS:llä Apple MLX -kehyksen avulla

Tässä opetusohjelmassa näytetään, miten luodaan iOS-sovellus, joka suorittaa Phi-3- tai Phi-4-mallin laitteella käyttäen Apple MLX -kehystä. [MLX](https://opensource.apple.com/projects/mlx/) on Applen koneoppimiskehys, joka on optimoitu Apple Silicon -piireille.

## Esivaatimukset

- macOS, jossa on Xcode 16 (tai uudempi)
- iOS 18 (tai uudempi) -laitteisto, jossa vähintään 8GB muistia (iPhone tai iPad, joka täyttää Apple Intelligence -vaatimukset, jotka ovat samankaltaisia kuin kvantisoidun Phi:n vaatimukset)
- perusosaaminen Swiftistä ja SwiftUI:sta

## Vaihe 1: Luo uusi iOS-projekti

Aloita luomalla uusi iOS-projekti Xcodessa:

1. käynnistä Xcode ja valitse "Create a new Xcode project"
2. valitse malliksi "App"
3. nimeä projektisi (esim. "Phi3-iOS-App") ja valitse käyttöliittymäksi SwiftUI
4. valitse sijainti projektin tallennukselle

## Vaihe 2: Lisää tarvittavat riippuvuudet

Lisää [MLX Examples -paketti](https://github.com/ml-explore/mlx-swift-examples), joka sisältää kaikki tarvittavat riippuvuudet ja apuvälineet mallien esilataukseen ja päättelyyn:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Vaikka perus [MLX Swift -paketti](https://github.com/ml-explore/mlx-swift) riittäisi ydin tensor-toimintoihin ja peruskoneoppimisen ominaisuuksiin, MLX Examples -paketti tarjoaa useita lisäosia, jotka on suunniteltu kielimallien käsittelyyn ja päättelyprosessin helpottamiseen:

- mallin latausvälineet, jotka hoitavat latauksen Hugging Facesta
- tokenisaattorin integrointi
- päättelyapuvälineet tekstin generointiin
- esikonfiguroidut mallin määritelmät

## Vaihe 3: Määritä oikeudet

Jotta sovelluksemme voi ladata malleja ja varata riittävästi muistia, meidän täytyy lisätä erityiset oikeudet. Luo sovelluksellesi `.entitlements`-tiedosto seuraavalla sisällöllä:

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

> [!NOTE] `com.apple.developer.kernel.increased-memory-limit` -oikeus on tärkeä isompien mallien ajamiseksi, sillä se sallii sovelluksen pyytää enemmän muistia kuin normaalisti olisi sallittua.

## Vaihe 4: Luo chat-viestimalli

Aloitetaan luomalla yksinkertainen rakenne, joka kuvaa chat-viestejämme:

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

## Vaihe 5: Toteuta ViewModel

Seuraavaksi luomme `PhiViewModel`-luokan, joka hoitaa mallin latauksen ja päättelyn:

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

ViewModel esittelee keskeiset MLX-integraatiokohdat:

- GPU-välimuistin rajoitusten asettaminen `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit` avulla, tässä viitataan tiettyyn valmiiksi muunnettuun MLX-malliin, joka ladataan automaattisesti:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Voit luoda omat mallikonfiguraatiosi osoittamaan mihin tahansa yhteensopivaan malliin Hugging Facessa. Esimerkiksi Phi-4 miniä varten voisit määritellä oman konfiguraation:

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

> [!NOTE] Phi-4 -tuki lisättiin MLX Swift Examples -repositorioon helmikuun 2025 lopussa (PR #216). Maaliskuusta 2025 lähtien uusin virallinen julkaisu (2.21.2 joulukuulta 2024) ei sisällä sisäänrakennettua Phi-4 -tukea. Phi-4 -mallien käyttämiseksi sinun täytyy viitata pakettiin suoraan päähaaran koodista:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Tämä antaa pääsyn uusimpiin mallikonfiguraatioihin, mukaan lukien Phi-4, ennen kuin ne sisällytetään viralliseen julkaisuun. Tätä menetelmää voi käyttää myös eri Phi-mallien tai muiden MLX-muotoon muunnettujen mallien kanssa.

## Vaihe 6: Luo käyttöliittymä

Toteutetaan nyt yksinkertainen chat-käyttöliittymä, jolla voi olla vuorovaikutusta view modelin kanssa:

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

Käyttöliittymä koostuu kolmesta pääkomponentista, jotka yhdessä muodostavat perus chat-rajapinnan. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` tarjoaa yksinkertaisen animaation, joka näyttää AI:n käsittelevän syötettä.

## Vaihe 7: Sovelluksen rakentaminen ja ajaminen

Nyt olemme valmiita rakentamaan ja ajamaan sovelluksen.

> [!IMPORTANT] MLX ei tue simulaattoria. Sovellus täytyy ajaa fyysisellä laitteella, jossa on Apple Silicon -piiri. Lisätietoja löytyy [täältä](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Kun sovellus käynnistyy, napauta "Load model" -painiketta ladataksesi ja alustaksesi Phi-3 (tai asetuksistasi riippuen Phi-4) mallin. Tämä voi kestää hetken internet-yhteydestäsi riippuen, sillä malli ladataan Hugging Facesta. Toteutuksemme näyttää latauksen aikana vain pyörivän indikaattorin, mutta voit seurata etenemistä Xcoden konsolista.

Kun malli on ladattu, voit keskustella sen kanssa kirjoittamalla kysymyksiä tekstikenttään ja painamalla lähetä-painiketta.

Tältä sovelluksemme pitäisi näyttää iPad Air M1:llä ajettaessa:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Yhteenveto

Siinä se! Näitä ohjeita noudattamalla olet luonut iOS-sovelluksen, joka ajaa Phi-3- (tai Phi-4-) mallin suoraan laitteella käyttäen Applen MLX-kehystä.

Onnittelut!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.