# Pokretanje Phi-3 i Phi-4 na iOS-u s Apple MLX Frameworkom

Ovaj vodič pokazuje kako napraviti iOS aplikaciju koja pokreće Phi-3 ili Phi-4 model lokalno na uređaju, koristeći Apple MLX framework. [MLX](https://opensource.apple.com/projects/mlx/) je Appleov strojno-učeći framework optimiziran za Apple Silicon čipove.

## Preduvjeti

- macOS s Xcode 16 (ili noviji)
- iOS 18 (ili noviji) uređaj s najmanje 8GB RAM-a (iPhone ili iPad kompatibilan s Apple Intelligence zahtjevima, koji su slični zahtjevima za kvantizirane Phi modele)
- osnovno znanje Swifta i SwiftUI-ja

## Korak 1: Kreirajte novi iOS projekt

Započnite kreiranjem novog iOS projekta u Xcode-u:

1. pokrenite Xcode i odaberite "Create a new Xcode project"
2. odaberite "App" kao predložak
3. imenujte svoj projekt (npr. "Phi3-iOS-App") i odaberite SwiftUI kao sučelje
4. odaberite lokaciju za spremanje projekta

## Korak 2: Dodajte potrebne ovisnosti

Dodajte [MLX Examples paket](https://github.com/ml-explore/mlx-swift-examples) koji sadrži sve potrebne ovisnosti i pomoćne alate za učitavanje modela i izvođenje inferencije:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Iako bi osnovni [MLX Swift paket](https://github.com/ml-explore/mlx-swift) bio dovoljan za osnovne tenzorske operacije i osnovnu ML funkcionalnost, MLX Examples paket donosi dodatne komponente namijenjene radu s jezičnim modelima i olakšavanju procesa inferencije:

- alati za učitavanje modela koji podržavaju preuzimanje s Hugging Face-a
- integracija tokenizatora
- pomoćni alati za generiranje teksta
- unaprijed konfigurirane definicije modela

## Korak 3: Konfigurirajte entitlements

Da bismo omogućili aplikaciji preuzimanje modela i dodjelu dovoljne količine memorije, potrebno je dodati određene entitlements. Kreirajte `.entitlements` datoteku za svoju aplikaciju sa sljedećim sadržajem:

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

> **Note:** Entitlement `com.apple.developer.kernel.increased-memory-limit` je važan za pokretanje većih modela jer omogućuje aplikaciji da zatraži više memorije nego što je inače dozvoljeno.

## Korak 4: Kreirajte model poruke za chat

Prvo, napravimo osnovnu strukturu za predstavljanje chat poruka:

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

ViewModel prikazuje ključne točke integracije s MLX-om:

- postavljanje ograničenja GPU cache-a pomoću `MLX.GPU.set(cacheLimit:)` za optimizaciju korištenja memorije na mobilnim uređajima
- korištenje `LLMModelFactory` za preuzimanje modela po potrebi i inicijalizaciju MLX-optimiziranog modela
- pristup parametrima i strukturi modela preko `ModelContainer`
- iskorištavanje MLX-ove generacije token po token kroz metodu `MLXLMCommon.generate`
- upravljanje procesom inferencije s odgovarajućim postavkama temperature i ograničenjima tokena

Pristup generiranju tokena u streamu omogućuje korisnicima trenutnu povratnu informaciju dok model generira tekst. To je slično načinu rada modela na serveru, koji korisniku šalju tokene u stvarnom vremenu, ali bez kašnjenja mrežnih zahtjeva.

Što se tiče interakcije s korisničkim sučeljem, dvije ključne funkcije su `loadModel()`, koja inicijalizira LLM, i `fetchAIResponse()`, koja obrađuje korisnički unos i generira AI odgovore.

### Razmatranja o formatu modela

> **Important:** Phi modeli za MLX ne mogu se koristiti u svom zadanim ili GGUF formatu. Moraju se konvertirati u MLX format, što obavlja MLX zajednica. Prekonvertirane modele možete pronaći na [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

MLX Examples paket uključuje unaprijed konfigurirane registracije za nekoliko modela, uključujući Phi-3. Kada pozovete `ModelRegistry.phi3_5_4bit`, on referencira određeni prekonvertirani MLX model koji će se automatski preuzeti:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Možete kreirati vlastite konfiguracije modela koje upućuju na bilo koji kompatibilni model na Hugging Face-u. Na primjer, za korištenje Phi-4 mini modela, možete definirati vlastitu konfiguraciju:

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

> **Note:** Podrška za Phi-4 dodana je u MLX Swift Examples repozitorij krajem veljače 2025. (u [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Do ožujka 2025., najnovije službeno izdanje (2.21.2 iz prosinca 2024.) ne uključuje ugrađenu podršku za Phi-4. Za korištenje Phi-4 modela potrebno je referencirati paket direktno iz glavne grane:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Ovim pristupom imate pristup najnovijim konfiguracijama modela, uključujući Phi-4, prije nego što budu uključene u službeno izdanje. Ovu metodu možete koristiti za različite verzije Phi modela ili čak druge modele konvertirane u MLX format.

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

Korisničko sučelje sastoji se od tri glavne komponente koje zajedno stvaraju osnovno chat sučelje. `ContentView` kreira sučelje s dva stanja koje prikazuje ili gumb za učitavanje ili chat sučelje, ovisno o spremnosti modela. `MessageView` prikazuje pojedinačne chat poruke različito, ovisno o tome jesu li poruke korisnika (poravnate desno, plava pozadina) ili odgovori Phi modela (poravnati lijevo, siva pozadina). `TypingIndicatorView` pruža jednostavan animirani indikator koji pokazuje da AI obrađuje upit.

## Korak 7: Izgradnja i pokretanje aplikacije

Sada smo spremni za izgradnju i pokretanje aplikacije.

> **Important!** MLX ne podržava simulator. Aplikaciju morate pokrenuti na fizičkom uređaju s Apple Silicon čipom. Više informacija potražite [ovdje](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Kad se aplikacija pokrene, dodirnite gumb "Load model" za preuzimanje i inicijalizaciju Phi-3 (ili, ovisno o konfiguraciji, Phi-4) modela. Ovaj proces može potrajati ovisno o vašoj internetskoj vezi jer uključuje preuzimanje modela s Hugging Face-a. Naša implementacija prikazuje samo spinner za vrijeme učitavanja, ali stvarni napredak možete pratiti u Xcode konzoli.

Nakon učitavanja, možete komunicirati s modelom tako da upisujete pitanja u tekstualno polje i pritiskom na gumb za slanje.

Evo kako bi naša aplikacija trebala izgledati u radu na iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Zaključak

I to je to! Slijedeći ove korake, napravili ste iOS aplikaciju koja pokreće Phi-3 (ili Phi-4) model izravno na uređaju koristeći Appleov MLX framework.

Čestitamo!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.