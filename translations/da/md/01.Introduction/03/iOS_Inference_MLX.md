<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:32:55+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "da"
}
-->
# Kørsel af Phi-3 og Phi-4 på iOS med Apple MLX Framework

Denne vejledning viser, hvordan man opretter en iOS-applikation, der kører Phi-3 eller Phi-4 modellen direkte på enheden ved hjælp af Apple MLX frameworket. [MLX](https://opensource.apple.com/projects/mlx/) er Apples maskinlæringsframework optimeret til Apple Silicon chips.

## Forudsætninger

- macOS med Xcode 16 (eller nyere)
- iOS 18 (eller nyere) mål-enhed med mindst 8GB (iPhone eller iPad kompatibel med Apple Intelligence krav, da disse ligner kravene for kvantiserede Phi-modeller)
- grundlæggende kendskab til Swift og SwiftUI

## Trin 1: Opret et nyt iOS-projekt

Start med at oprette et nyt iOS-projekt i Xcode:

1. åbn Xcode og vælg "Create a new Xcode project"
2. vælg "App" som skabelon
3. navngiv dit projekt (f.eks. "Phi3-iOS-App") og vælg SwiftUI som interface
4. vælg en placering til at gemme dit projekt

## Trin 2: Tilføj nødvendige afhængigheder

Tilføj [MLX Examples pakken](https://github.com/ml-explore/mlx-swift-examples), som indeholder alle nødvendige afhængigheder og hjælpefunktioner til forudindlæsning af modeller og udførelse af inferens:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Selvom den grundlæggende [MLX Swift pakke](https://github.com/ml-explore/mlx-swift) er tilstrækkelig til kerne tensor-operationer og basal ML-funktionalitet, tilbyder MLX Examples pakken flere ekstra komponenter designet til arbejde med sprogmodeller og for at gøre inferensprocessen nemmere:

- værktøjer til modelindlæsning, der håndterer download fra Hugging Face
- tokenizer-integration
- hjælpefunktioner til tekstgenerering
- forudkonfigurerede modeldefinitioner

## Trin 3: Konfigurer entitlements

For at tillade vores app at downloade modeller og allokere tilstrækkelig hukommelse, skal vi tilføje specifikke entitlements. Opret en `.entitlements` fil til din app med følgende indhold:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement er vigtig for at køre større modeller, da den tillader appen at anmode om mere hukommelse end normalt tilladt.

## Trin 4: Opret chatbesked-modellen

Lad os først oprette en simpel struktur til at repræsentere vores chatbeskeder:

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

## Trin 5: Implementer ViewModel

Dernæst opretter vi `PhiViewModel` klassen, som håndterer modelindlæsning og inferens:

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

ViewModel demonstrerer de vigtigste MLX integrationspunkter:

- indstilling af GPU cache-grænser med `MLX.GPU.set(cacheLimit:)` for at optimere hukommelsesforbruget på mobile enheder
- brug af `LLMModelFactory` til at downloade modellen efter behov og initialisere den MLX-optimerede model
- adgang til modellens parametre og struktur via `ModelContainer`
- udnyttelse af MLX’s token-for-token generering gennem `MLXLMCommon.generate` metoden
- styring af inferensprocessen med passende temperaturindstillinger og token-grænser

Den streaming-baserede token-generering giver brugerne øjeblikkelig feedback, mens modellen genererer tekst. Dette minder om, hvordan serverbaserede modeller fungerer, da de streamer tokens tilbage til brugeren, men uden netværksforsinkelsen.

I forhold til UI-interaktion er de to nøglefunktioner `loadModel()`, som initialiserer LLM, og `fetchAIResponse()`, som behandler brugerinput og genererer AI-svar.

### Overvejelser om modelformat

> **Important:** Phi-modeller til MLX kan ikke bruges i deres standard- eller GGUF-format. De skal konverteres til MLX-formatet, hvilket håndteres af MLX-fællesskabet. Du kan finde for-konverterede modeller på [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

MLX Examples pakken inkluderer forudkonfigurerede registreringer for flere modeller, inklusive Phi-3. Når du kalder `ModelRegistry.phi3_5_4bit`, refererer det til en specifik for-konverteret MLX-model, som automatisk downloades:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Du kan oprette dine egne modelkonfigurationer, der peger på enhver kompatibel model på Hugging Face. For eksempel, hvis du vil bruge Phi-4 mini i stedet, kan du definere din egen konfiguration:

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

> **Note:** Phi-4 support blev tilføjet til MLX Swift Examples repository i slutningen af februar 2025 (i [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Fra marts 2025 inkluderer den seneste officielle udgivelse (2.21.2 fra december 2024) ikke indbygget Phi-4 support. For at bruge Phi-4 modeller skal du referere pakken direkte fra main branch:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Dette giver dig adgang til de nyeste modelkonfigurationer, inklusive Phi-4, før de inkluderes i en officiel udgivelse. Du kan bruge denne metode til at anvende forskellige versioner af Phi-modeller eller endda andre modeller, der er konverteret til MLX-formatet.

## Trin 6: Opret UI

Lad os nu implementere et simpelt chat-interface til at interagere med vores view model:

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

UI’en består af tre hovedkomponenter, der arbejder sammen om at skabe et grundlæggende chat-interface. `ContentView` skaber et to-tilstands interface, der viser enten en loading-knap eller chat-interfacet afhængigt af modellens tilgængelighed. `MessageView` gengiver individuelle chatbeskeder forskelligt, afhængigt af om det er brugermeddelelser (højrestillet, blå baggrund) eller Phi-modelsvar (venstrestillet, grå baggrund). `TypingIndicatorView` giver en simpel animeret indikator, der viser, at AI’en er i gang med at behandle.

## Trin 7: Byg og kør appen

Vi er nu klar til at bygge og køre applikationen.

> **Important!** MLX understøtter ikke simulatoren. Du skal køre appen på en fysisk enhed med en Apple Silicon chip. Se [her](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) for mere information.

Når appen starter, tryk på "Load model" knappen for at downloade og initialisere Phi-3 (eller, afhængigt af din konfiguration, Phi-4) modellen. Denne proces kan tage noget tid afhængigt af din internetforbindelse, da den involverer download af modellen fra Hugging Face. Vores implementering inkluderer kun en spinner til at indikere loading, men du kan se den faktiske fremdrift i Xcode-konsollen.

Når modellen er indlæst, kan du interagere med den ved at skrive spørgsmål i tekstfeltet og trykke på send-knappen.

Sådan bør vores applikation opføre sig, kørende på iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Konklusion

Og det var det! Ved at følge disse trin har du oprettet en iOS-applikation, der kører Phi-3 (eller Phi-4) modellen direkte på enheden ved hjælp af Apples MLX framework.

Tillykke!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.