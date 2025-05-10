<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:23:01+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "sk"
}
-->
# Spustenie Phi-3 a Phi-4 na iOS s Apple MLX Frameworkom

Tento tutoriál ukazuje, ako vytvoriť iOS aplikáciu, ktorá spustí model Phi-3 alebo Phi-4 priamo na zariadení pomocou Apple MLX frameworku. [MLX](https://opensource.apple.com/projects/mlx/) je Apple framework pre strojové učenie optimalizovaný pre čipy Apple Silicon.

## Požiadavky

- macOS s Xcode 16 (alebo novším)
- cieľové zariadenie s iOS 18 (alebo novším) a aspoň 8GB RAM (iPhone alebo iPad kompatibilný s požiadavkami Apple Intelligence, ktoré sú podobné požiadavkám kvantizovaného Phi)
- základné znalosti Swift a SwiftUI

## Krok 1: Vytvorenie nového iOS projektu

Začnite vytvorením nového iOS projektu v Xcode:

1. spustite Xcode a vyberte „Create a new Xcode project“
2. zvoľte šablónu „App“
3. pomenujte projekt (napr. „Phi3-iOS-App“) a vyberte SwiftUI ako rozhranie
4. vyberte miesto, kam chcete projekt uložiť

## Krok 2: Pridanie potrebných závislostí

Pridajte [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples), ktorý obsahuje všetky potrebné závislosti a pomocné nástroje na prednačítanie modelov a vykonávanie inferencie:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Zatiaľ čo základný [MLX Swift package](https://github.com/ml-explore/mlx-swift) stačí na základné tensorové operácie a základnú ML funkcionalitu, MLX Examples package prináša niekoľko ďalších komponentov určených na prácu s jazykovými modelmi a uľahčenie inferenčného procesu:

- nástroje na načítanie modelov s podporou sťahovania z Hugging Face
- integrácia tokenizéra
- pomocníci na generovanie textu
- predkonfigurované definície modelov

## Krok 3: Konfigurácia entitlements

Aby naša aplikácia mohla sťahovať modely a alokovať dostatok pamäte, je potrebné pridať špecifické entitlements. Vytvorte `.entitlements` súbor pre vašu aplikáciu s nasledovným obsahom:

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

> **Note:** Entitlement `com.apple.developer.kernel.increased-memory-limit` je dôležitý pre spustenie väčších modelov, pretože umožňuje aplikácii požadovať viac pamäte, než je bežne povolené.

## Krok 4: Vytvorenie modelu správy chatu

Najskôr vytvoríme základnú štruktúru na reprezentáciu správ v chate:

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

## Krok 5: Implementácia ViewModelu

Ďalej vytvoríme triedu `PhiViewModel`, ktorá sa postará o načítanie modelu a inferenciu:

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

ViewModel ukazuje kľúčové body integrácie MLX:

- nastavenie limitu GPU cache pomocou `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, kde sa odkazuje na konkrétny predkonvertovaný MLX model, ktorý sa automaticky stiahne:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Môžete si vytvoriť vlastné konfigurácie modelov, ktoré budú smerovať na akýkoľvek kompatibilný model na Hugging Face. Napríklad, ak chcete použiť Phi-4 mini, môžete definovať vlastnú konfiguráciu:

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

> **Note:** Podpora Phi-4 bola pridaná do MLX Swift Examples repozitára koncom februára 2025 (v [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). K marcu 2025 najnovšie oficiálne vydanie (2.21.2 z decembra 2024) neobsahuje vstavanú podporu Phi-4. Ak chcete používať Phi-4 modely, musíte odkazovať balík priamo z hlavnej vetvy:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Tým získate prístup k najnovším konfiguráciám modelov vrátane Phi-4 ešte pred ich oficiálnym vydaním. Túto metódu môžete použiť na rôzne verzie Phi modelov alebo aj iné modely prevedené do MLX formátu.

## Krok 6: Vytvorenie používateľského rozhrania

Teraz implementujeme jednoduché chatové rozhranie na interakciu s naším view modelom:

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

UI pozostáva z troch hlavných komponentov, ktoré spolu tvoria základné chatové rozhranie. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` poskytuje jednoduchý animovaný indikátor, ktorý ukazuje, že AI spracováva požiadavku.

## Krok 7: Kompilácia a spustenie aplikácie

Teraz sme pripravení aplikáciu zostaviť a spustiť.

> **Important!** MLX nepodporuje simulátor. Aplikáciu musíte spustiť na fyzickom zariadení s Apple Silicon čipom. Viac informácií nájdete [tu](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Po spustení aplikácie ťuknite na tlačidlo „Load model“, čím sa začne sťahovanie a inicializácia modelu Phi-3 (alebo podľa vašej konfigurácie Phi-4). Tento proces môže trvať určitý čas v závislosti od rýchlosti vášho internetového pripojenia, keďže zahŕňa stiahnutie modelu z Hugging Face. Naša implementácia obsahuje iba spinner na indikáciu načítavania, ale skutočný priebeh môžete sledovať v Xcode konzole.

Po načítaní môžete s modelom komunikovať písaním otázok do textového poľa a stlačením tlačidla odoslať.

Takto by mala naša aplikácia fungovať na iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Záver

A to je všetko! Dodržaním týchto krokov ste vytvorili iOS aplikáciu, ktorá spúšťa model Phi-3 (alebo Phi-4) priamo na zariadení pomocou Apple MLX frameworku.

Gratulujeme!

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.