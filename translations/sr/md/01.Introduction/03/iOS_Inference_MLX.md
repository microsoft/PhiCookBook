<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:30:17+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "sr"
}
-->
# Pokretanje Phi-3 i Phi-4 na iOS-u uz Apple MLX Framework

Ovaj vodič pokazuje kako napraviti iOS aplikaciju koja pokreće Phi-3 ili Phi-4 model direktno na uređaju, koristeći Apple MLX framework. [MLX](https://opensource.apple.com/projects/mlx/) je Apple-ov framework za mašinsko učenje optimizovan za Apple Silicon čipove.

## Preduslovi

- macOS sa Xcode 16 (ili novijim)
- iOS 18 (ili noviji) uređaj sa najmanje 8GB RAM-a (iPhone ili iPad kompatibilan sa Apple Intelligence zahtevima, koji su slični zahtevima za kvantizovani Phi)
- osnovno znanje Swift i SwiftUI

## Korak 1: Kreirajte novi iOS projekat

Počnite tako što ćete kreirati novi iOS projekat u Xcode-u:

1. pokrenite Xcode i izaberite "Create a new Xcode project"
2. izaberite "App" kao šablon
3. imenujte projekat (npr. "Phi3-iOS-App") i izaberite SwiftUI kao interfejs
4. odaberite lokaciju gde ćete sačuvati projekat

## Korak 2: Dodajte potrebne zavisnosti

Dodajte [MLX Examples paket](https://github.com/ml-explore/mlx-swift-examples) koji sadrži sve potrebne zavisnosti i pomoćne alate za učitavanje modela i izvođenje inferencije:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Iako je osnovni [MLX Swift paket](https://github.com/ml-explore/mlx-swift) dovoljan za osnovne tenzorske operacije i osnovnu funkcionalnost ML-a, MLX Examples paket pruža dodatne komponente za rad sa jezičkim modelima i olakšava proces inferencije:

- alati za učitavanje modela koji omogućavaju preuzimanje sa Hugging Face-a
- integracija tokenizatora
- pomoćni alati za generisanje teksta
- unapred konfigurisane definicije modela

## Korak 3: Konfigurišite entitlements

Da bismo omogućili aplikaciji da preuzima modele i alocira dovoljno memorije, potrebno je dodati određene entitlements. Kreirajte `.entitlements` fajl za vašu aplikaciju sa sledećim sadržajem:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` entitlement je važan za pokretanje većih modela, jer omogućava aplikaciji da zatraži više memorije nego što je inače dozvoljeno.

## Korak 4: Kreirajte model za poruke u četu

Prvo, napravimo osnovnu strukturu za predstavljanje poruka u četu:

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

Zatim ćemo napraviti `PhiViewModel` klasu koja upravlja učitavanjem modela i inferencijom:

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

ViewModel prikazuje ključne tačke integracije sa MLX:

- podešavanje limita GPU keša sa `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, gde se referencira konkretan prethodno konvertovani MLX model koji će biti automatski preuzet:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Možete kreirati sopstvene konfiguracije modela koje pokazuju na bilo koji kompatibilan model na Hugging Face-u. Na primer, za korišćenje Phi-4 mini modela, možete definisati sopstvenu konfiguraciju:

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

> **Note:** Podrška za Phi-4 je dodata u MLX Swift Examples repozitorijum krajem februara 2025. (u [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Od marta 2025, najnovije zvanično izdanje (2.21.2 iz decembra 2024) ne uključuje ugrađenu podršku za Phi-4. Da biste koristili Phi-4 modele, potrebno je da referencirate paket direktno sa glavne grane:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Ovo vam daje pristup najnovijim konfiguracijama modela, uključujući Phi-4, pre nego što budu uključene u zvanično izdanje. Ovim pristupom možete koristiti različite verzije Phi modela ili čak druge modele koji su konvertovani u MLX format.

## Korak 6: Kreirajte korisnički interfejs

Sada ćemo implementirati jednostavan chat interfejs za interakciju sa našim ViewModel-om:

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

UI se sastoji od tri glavne komponente koje zajedno prave osnovni chat interfejs. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` pruža jednostavan animirani indikator koji pokazuje da AI obrađuje zahtev.

## Korak 7: Izgradnja i pokretanje aplikacije

Sada smo spremni da izgradimo i pokrenemo aplikaciju.

> **Important!** MLX ne podržava simulator. Aplikaciju morate pokrenuti na fizičkom uređaju sa Apple Silicon čipom. Više informacija potražite [ovde](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Kada se aplikacija pokrene, dodirnite dugme "Load model" da biste preuzeli i inicijalizovali Phi-3 (ili, u zavisnosti od konfiguracije, Phi-4) model. Ovaj proces može potrajati u zavisnosti od vaše internet konekcije, jer se model preuzima sa Hugging Face-a. Naša implementacija prikazuje samo spinner tokom učitavanja, ali stvarni napredak možete pratiti u Xcode konzoli.

Kada se model učita, možete komunicirati sa njim tako što ćete kucati pitanja u tekstualno polje i pritiskati dugme za slanje.

Ovako bi naša aplikacija trebalo da funkcioniše, pokrenuta na iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Zaključak

I to je to! Prateći ove korake, napravili ste iOS aplikaciju koja pokreće Phi-3 (ili Phi-4) model direktno na uređaju koristeći Apple MLX framework.

Čestitamo!

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне тумачења која произилазе из коришћења овог превода.