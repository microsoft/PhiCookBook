# Kjøre Phi-3 og Phi-4 på iOS med Apple MLX Framework

Denne veiledningen viser hvordan du lager en iOS-applikasjon som kjører Phi-3 eller Phi-4-modellen på enheten, ved bruk av Apple MLX-rammeverket. [MLX](https://opensource.apple.com/projects/mlx/) er Apples maskinlæringsrammeverk optimalisert for Apple Silicon-brikker.

## Forutsetninger

- macOS med Xcode 16 (eller nyere)
- iOS 18 (eller nyere) mål-enhet med minst 8GB (iPhone eller iPad som oppfyller Apple Intelligence-kravene, da disse ligner på kravene for kvantiserte Phi-modeller)
- grunnleggende kunnskap om Swift og SwiftUI

## Steg 1: Opprett et nytt iOS-prosjekt

Start med å opprette et nytt iOS-prosjekt i Xcode:

1. åpne Xcode og velg "Create a new Xcode project"
2. velg "App" som mal
3. gi prosjektet ditt et navn (f.eks. "Phi3-iOS-App") og velg SwiftUI som grensesnitt
4. velg en plassering for å lagre prosjektet

## Steg 2: Legg til nødvendige avhengigheter

Legg til [MLX Examples-pakken](https://github.com/ml-explore/mlx-swift-examples) som inneholder alle nødvendige avhengigheter og hjelpere for forhåndslasting av modeller og utføring av inferens:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Selv om den grunnleggende [MLX Swift-pakken](https://github.com/ml-explore/mlx-swift) er nok for kjerneoperasjoner med tensorer og grunnleggende ML-funksjonalitet, tilbyr MLX Examples-pakken flere ekstra komponenter designet for å jobbe med språkmodeller og gjøre inferensprosessen enklere:

- verktøy for modellinnlasting som håndterer nedlasting fra Hugging Face
- integrasjon av tokenizer
- hjelpere for tekstgenerering under inferens
- forhåndskonfigurerte modelldefinisjoner

## Steg 3: Konfigurer entitlements

For å tillate at appen vår laster ned modeller og allokerer tilstrekkelig minne, må vi legge til spesifikke entitlements. Lag en `.entitlements`-fil for appen din med følgende innhold:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit`-entitlement er viktig for å kjøre større modeller, da den tillater appen å be om mer minne enn normalt tillatt.

## Steg 4: Lag chat-meldingsmodellen

La oss først lage en enkel struktur for å representere chat-meldingene våre:

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

## Steg 5: Implementer ViewModel

Deretter lager vi `PhiViewModel`-klassen som håndterer modellinnlasting og inferens:

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

ViewModel viser de viktigste integrasjonspunktene med MLX:

- sette GPU-cache-grenser med `MLX.GPU.set(cacheLimit:)` for å optimalisere minnebruk på mobile enheter
- bruke `LLMModelFactory` for å laste ned modellen ved behov og initialisere MLX-optimalisert modell
- få tilgang til modellens parametere og struktur via `ModelContainer`
- utnytte MLX sin token-for-token-generering gjennom `MLXLMCommon.generate`-metoden
- styre inferensprosessen med passende temperaturinnstillinger og tokenbegrensninger

Streaming av token-generering gir umiddelbar tilbakemelding til brukeren mens modellen genererer tekst. Dette ligner på hvordan serverbaserte modeller fungerer, ved at de streamer tokens tilbake til brukeren, men uten forsinkelsen som nettverksforespørsler medfører.

Når det gjelder UI-interaksjon, er de to viktigste funksjonene `loadModel()`, som initialiserer LLM, og `fetchAIResponse()`, som behandler brukerinput og genererer AI-svar.

### Vurderinger rundt modellformat

> **Important:** Phi-modeller for MLX kan ikke brukes i sitt standard- eller GGUF-format. De må konverteres til MLX-format, noe som håndteres av MLX-fellesskapet. Du finner forhåndskonverterte modeller på [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

MLX Examples-pakken inkluderer forhåndskonfigurerte registreringer for flere modeller, inkludert Phi-3. Når du kaller `ModelRegistry.phi3_5_4bit`, refererer det til en spesifikk forhåndskonvertert MLX-modell som lastes ned automatisk:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Du kan lage dine egne modellkonfigurasjoner som peker til hvilken som helst kompatibel modell på Hugging Face. For eksempel, for å bruke Phi-4 mini i stedet, kan du definere din egen konfigurasjon:

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

> **Note:** Phi-4-støtte ble lagt til i MLX Swift Examples-repositoriet i slutten av februar 2025 (i [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Per mars 2025 inkluderer ikke den siste offisielle utgivelsen (2.21.2 fra desember 2024) innebygd Phi-4-støtte. For å bruke Phi-4-modeller må du referere pakken direkte fra main-branchen:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Dette gir deg tilgang til de nyeste modellkonfigurasjonene, inkludert Phi-4, før de er inkludert i en offisiell utgivelse. Du kan bruke denne metoden for å bruke forskjellige versjoner av Phi-modeller eller andre modeller som er konvertert til MLX-format.

## Steg 6: Lag UI

La oss nå implementere et enkelt chattegrensesnitt for å samhandle med view modellen vår:

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

UI-en består av tre hovedkomponenter som samarbeider for å lage et grunnleggende chattegrensesnitt. `ContentView` lager et to-tilstandsgrensesnitt som viser enten en last-knapp eller chattegrensesnittet avhengig av modellens tilgjengelighet. `MessageView` viser individuelle chatmeldinger forskjellig basert på om de er brukermeldinger (høyrejustert, blå bakgrunn) eller Phi-modellens svar (venstrejustert, grå bakgrunn). `TypingIndicatorView` gir en enkel animert indikator som viser at AI-en prosesserer.

## Steg 7: Bygg og kjør appen

Nå er vi klare til å bygge og kjøre applikasjonen.

> **Important!** MLX støtter ikke simulatoren. Du må kjøre appen på en fysisk enhet med Apple Silicon-brikke. Se [her](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) for mer informasjon.

Når appen starter, trykk på "Load model"-knappen for å laste ned og initialisere Phi-3 (eller, avhengig av konfigurasjonen din, Phi-4) modellen. Denne prosessen kan ta litt tid avhengig av internettforbindelsen din, siden den innebærer nedlasting av modellen fra Hugging Face. Vår implementasjon inkluderer kun en spinner for å indikere lasting, men du kan se den faktiske fremgangen i Xcode-konsollen.

Når modellen er lastet, kan du samhandle med den ved å skrive spørsmål i tekstfeltet og trykke på send-knappen.

Slik skal applikasjonen vår oppføre seg, kjørende på iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Konklusjon

Og det var det! Ved å følge disse stegene har du laget en iOS-applikasjon som kjører Phi-3 (eller Phi-4) modellen direkte på enheten ved hjelp av Apples MLX-rammeverk.

Gratulerer!

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.