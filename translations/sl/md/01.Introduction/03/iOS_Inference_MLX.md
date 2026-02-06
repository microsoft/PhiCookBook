# Zagon Phi-3 in Phi-4 na iOS z Apple MLX Framework

Ta vodič prikazuje, kako ustvariti iOS aplikacijo, ki na napravi izvaja model Phi-3 ali Phi-4 z uporabo Apple MLX frameworka. [MLX](https://opensource.apple.com/projects/mlx/) je Applov strojno-učeči framework, optimiziran za Apple Silicon čipe.

## Zahteve

- macOS z Xcode 16 (ali novejši)
- iOS 18 (ali novejši) ciljna naprava z vsaj 8 GB RAM (iPhone ali iPad, združljiv z zahtevami Apple Intelligence, ki so podobne zahtevam za kvantizirane modele Phi)
- osnovno znanje Swifta in SwiftUI

## 1. korak: Ustvarite nov iOS projekt

Začnite z ustvarjanjem novega iOS projekta v Xcode:

1. zaženite Xcode in izberite "Create a new Xcode project"
2. izberite predlogo "App"
3. poimenujte projekt (npr. "Phi3-iOS-App") in izberite SwiftUI kot uporabniški vmesnik
4. izberite lokacijo za shranjevanje projekta

## 2. korak: Dodajte potrebne odvisnosti

Dodajte [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples), ki vsebuje vse potrebne odvisnosti in pripomočke za predhodno nalaganje modelov in izvajanje inferenc:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Medtem ko bi bila osnovna [MLX Swift package](https://github.com/ml-explore/mlx-swift) dovolj za osnovne tenzorske operacije in osnovno ML funkcionalnost, paket MLX Examples ponuja več dodatnih komponent, namenjenih delu z jezikovnimi modeli in poenostavitvi procesa inferenc:

- pripomočki za nalaganje modelov, ki omogočajo prenos z Hugging Face
- integracija tokenizatorja
- pomočniki za generiranje besedila
- vnaprej konfigurirane definicije modelov

## 3. korak: Konfigurirajte entitlements

Da aplikaciji omogočimo prenos modelov in dodelitev dovolj pomnilnika, moramo dodati posebne entitlements. Ustvarite `.entitlements` datoteko za vašo aplikacijo z naslednjo vsebino:

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

> **Note:** Entitlement `com.apple.developer.kernel.increased-memory-limit` je pomemben za zagon večjih modelov, saj aplikaciji omogoča zahtevo po več pomnilnika, kot je običajno dovoljeno.

## 4. korak: Ustvarite model sporočila za klepet

Najprej ustvarimo osnovno strukturo za predstavitev sporočil v klepetu:

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

## 5. korak: Implementirajte ViewModel

Nato ustvarimo razred `PhiViewModel`, ki upravlja z nalaganjem modela in inferenco:

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

ViewModel prikazuje ključne točke integracije z MLX:

- nastavljanje omejitev GPU predpomnilnika z `MLX.GPU.set(cacheLimit:)` za optimizacijo porabe pomnilnika na mobilnih napravah
- uporaba `LLMModelFactory` za prenos modela po potrebi in inicializacijo MLX-optimiziranega modela
- dostop do parametrov in strukture modela preko `ModelContainer`
- izkoriščanje MLX-jeve generacije tokenov enega za drugim preko metode `MLXLMCommon.generate`
- upravljanje procesa inferenc z ustreznimi nastavitvami temperature in omejitvami števila tokenov

Pristop generiranja tokenov v realnem času omogoča takojšnjo povratno informacijo uporabnikom med generiranjem besedila. To je podobno delovanju strežniških modelov, ki uporabniku pošiljajo tokene sproti, vendar brez zakasnitve zaradi omrežnih zahtev.

Kar zadeva interakcijo z UI, sta ključni funkciji `loadModel()`, ki inicializira LLM, in `fetchAIResponse()`, ki obdela uporabniški vnos in generira AI odzive.

### Razmisleki o formatu modela

> **Important:** Phi modeli za MLX ne morejo biti uporabljeni v privzetem ali GGUF formatu. Morajo biti pretvorjeni v MLX format, kar ureja skupnost MLX. Predhodno pretvorjene modele najdete na [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Paket MLX Examples vključuje vnaprej konfigurirane registracije za več modelov, vključno s Phi-3. Ko pokličete `ModelRegistry.phi3_5_4bit`, se sklicujete na določen predhodno pretvorjen MLX model, ki se bo samodejno prenesel:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Lahko ustvarite tudi svoje konfiguracije modelov, ki kažejo na poljuben združljiv model na Hugging Face. Na primer, za uporabo Phi-4 mini lahko definirate svojo konfiguracijo:

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

> **Note:** Podpora za Phi-4 je bila dodana v repozitorij MLX Swift Examples konec februarja 2025 (v [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Do marca 2025 najnovejša uradna izdaja (2.21.2 iz decembra 2024) ne vključuje vgrajene podpore za Phi-4. Za uporabo Phi-4 modelov morate paket neposredno referencirati iz glavne veje:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

To vam omogoča dostop do najnovejših konfiguracij modelov, vključno s Phi-4, preden so vključene v uradno izdajo. Ta pristop lahko uporabite za uporabo različnih različic Phi modelov ali celo drugih modelov, pretvorjenih v MLX format.

## 6. korak: Ustvarite uporabniški vmesnik

Sedaj implementirajmo preprost klepetalni vmesnik za interakcijo z našim view modelom:

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

UI sestavljajo tri glavne komponente, ki skupaj ustvarijo osnovni klepetalni vmesnik. `ContentView` ustvari dvo-stanjski vmesnik, ki prikaže bodisi gumb za nalaganje bodisi klepetalni vmesnik, odvisno od pripravljenosti modela. `MessageView` prikaže posamezna sporočila v klepetu različno glede na to, ali gre za uporabniška sporočila (poravnana desno, modro ozadje) ali odzive Phi modela (poravnana levo, sivo ozadje). `TypingIndicatorView` prikaže preprost animiran indikator, ki nakazuje, da AI obdeluje vnos.

## 7. korak: Gradnja in zagon aplikacije

Zdaj smo pripravljeni za gradnjo in zagon aplikacije.

> **Important!** MLX ne podpira simulatorja. Aplikacijo morate zagnati na fizični napravi z Apple Silicon čipom. Več informacij najdete [tukaj](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Ko se aplikacija zažene, tapnite gumb "Load model" za prenos in inicializacijo modela Phi-3 (ali, glede na vašo konfiguracijo, Phi-4). Ta postopek lahko traja nekaj časa, odvisno od vaše internetne povezave, saj vključuje prenos modela z Hugging Face. Naša implementacija vključuje le vrteči se indikator nalaganja, dejanski napredek pa lahko spremljate v Xcode konzoli.

Ko je model naložen, lahko z njim komunicirate tako, da v polje za vnos vnesete vprašanja in pritisnete gumb za pošiljanje.

Tako naj bi se obnašala naša aplikacija, ki teče na iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Zaključek

In to je to! Z upoštevanjem teh korakov ste ustvarili iOS aplikacijo, ki neposredno na napravi izvaja model Phi-3 (ali Phi-4) z uporabo Applovega MLX frameworka.

Čestitke!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.