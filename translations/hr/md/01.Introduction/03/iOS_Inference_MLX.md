<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:30:57+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "hr"
}
-->
# Pokretanje Phi-3 i Phi-4 na iOS-u s Apple MLX Frameworkom

Ovaj vodič pokazuje kako napraviti iOS aplikaciju koja pokreće Phi-3 ili Phi-4 model na uređaju, koristeći Apple MLX framework. [MLX](https://opensource.apple.com/projects/mlx/) je Appleov framework za strojno učenje optimiziran za Apple Silicon čipove.

## Preduvjeti

- macOS s Xcode 16 (ili novijim)
- iOS 18 (ili noviji) na ciljnom uređaju s barem 8GB (iPhone ili iPad kompatibilan s Apple Intelligence zahtjevima, koji su slični zahtjevima za kvantizirani Phi)
- osnovno znanje Swifta i SwiftUI-a

## Korak 1: Kreirajte novi iOS projekt

Započnite kreiranjem novog iOS projekta u Xcodeu:

1. pokrenite Xcode i odaberite "Create a new Xcode project"
2. odaberite "App" kao predložak
3. imenujte projekt (npr. "Phi3-iOS-App") i odaberite SwiftUI kao sučelje
4. odaberite lokaciju za spremanje projekta

## Korak 2: Dodajte potrebne ovisnosti

Dodajte [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) koji sadrži sve potrebne ovisnosti i pomoćne alate za prethodno učitavanje modela i izvođenje inferencije:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Iako bi osnovni [MLX Swift package](https://github.com/ml-explore/mlx-swift) bio dovoljan za osnovne tensor operacije i osnovne ML funkcionalnosti, MLX Examples package pruža dodatne komponente namijenjene radu s jezičnim modelima i olakšava proces inferencije:

- alati za učitavanje modela koji podržavaju preuzimanje s Hugging Facea
- integracija tokenizatora
- pomoćnici za generiranje teksta
- unaprijed konfigurirane definicije modela

## Korak 3: Konfigurirajte entitlements

Da bismo omogućili aplikaciji preuzimanje modela i alociranje dovoljno memorije, potrebno je dodati određene entitlements. Kreirajte `.entitlements` datoteku za vašu aplikaciju s ovim sadržajem:

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

> **Note:** Entitlement `com.apple.developer.kernel.increased-memory-limit` je važan za pokretanje većih modela jer omogućuje aplikaciji zahtijevati više memorije nego što je inače dopušteno.

## Korak 4: Kreirajte model poruke za chat

Prvo, napravimo osnovnu strukturu koja predstavlja naše poruke u chatu:

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

## Korak 5: Implementirajte ViewModel

Zatim ćemo kreirati klasu `PhiViewModel` koja upravlja učitavanjem modela i inferencijom:

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

ViewModel pokazuje ključne točke integracije s MLX-om:

- postavljanje limita GPU cachea s `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, referencira specifični unaprijed konvertirani MLX model koji će se automatski preuzeti:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Možete kreirati vlastite konfiguracije modela koje pokazuju na bilo koji kompatibilni model na Hugging Faceu. Na primjer, za korištenje Phi-4 mini umjesto toga, možete definirati vlastitu konfiguraciju:

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

> **Note:** Podrška za Phi-4 dodana je u MLX Swift Examples repozitorij krajem veljače 2025. (u [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Od ožujka 2025., najnovije službeno izdanje (2.21.2 iz prosinca 2024.) ne uključuje ugrađenu podršku za Phi-4. Za korištenje Phi-4 modela, potrebno je referencirati paket direktno iz glavne grane:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Ovim pristupom imate pristup najnovijim konfiguracijama modela, uključujući Phi-4, prije nego što budu uključene u službeno izdanje. Možete koristiti ovaj pristup za različite verzije Phi modela ili čak druge modele koji su konvertirani u MLX format.

## Korak 6: Kreirajte korisničko sučelje

Sada implementirajmo jednostavno chat sučelje za interakciju s našim view modelom:

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

UI se sastoji od tri glavne komponente koje zajedno čine osnovno chat sučelje. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` pruža jednostavan animirani indikator koji pokazuje da AI obrađuje upit

## Korak 7: Izgradnja i pokretanje aplikacije

Sada smo spremni izgraditi i pokrenuti aplikaciju.

> **Important!** MLX ne podržava simulator. Morate pokrenuti aplikaciju na fizičkom uređaju s Apple Silicon čipom. Više informacija potražite [ovdje](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Kad se aplikacija pokrene, dodirnite gumb "Load model" za preuzimanje i inicijalizaciju Phi-3 (ili, ovisno o konfiguraciji, Phi-4) modela. Ovaj proces može potrajati ovisno o vašoj internetskoj vezi, jer uključuje preuzimanje modela s Hugging Facea. Naša implementacija prikazuje samo spinner za vrijeme učitavanja, ali stvarni napredak možete pratiti u Xcode konzoli.

Nakon učitavanja, možete komunicirati s modelom tako da u polje za tekst upisujete pitanja i dodirnete gumb za slanje.

Evo kako bi naša aplikacija trebala izgledati, pokrenuta na iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Zaključak

I to je to! Slijedeći ove korake, kreirali ste iOS aplikaciju koja izravno na uređaju pokreće Phi-3 (ili Phi-4) model koristeći Appleov MLX framework.

Čestitamo!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili kriva tumačenja proizašla iz korištenja ovog prijevoda.