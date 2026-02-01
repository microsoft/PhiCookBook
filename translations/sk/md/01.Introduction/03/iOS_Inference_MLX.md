# Spustenie Phi-3 a Phi-4 na iOS s Apple MLX Frameworkom

Tento tutoriál ukazuje, ako vytvoriť iOS aplikáciu, ktorá spúšťa model Phi-3 alebo Phi-4 priamo na zariadení pomocou Apple MLX frameworku. [MLX](https://opensource.apple.com/projects/mlx/) je Apple framework pre strojové učenie optimalizovaný pre čipy Apple Silicon.

## Požiadavky

- macOS s Xcode 16 (alebo novším)
- cieľové zariadenie s iOS 18 (alebo novším) a minimálne 8 GB RAM (iPhone alebo iPad kompatibilný s požiadavkami Apple Intelligence, ktoré sú podobné požiadavkám na kvantizovaný Phi)
- základné znalosti Swift a SwiftUI

## Krok 1: Vytvorenie nového iOS projektu

Začnite vytvorením nového iOS projektu v Xcode:

1. spustite Xcode a vyberte „Create a new Xcode project“
2. zvoľte šablónu „App“
3. pomenujte projekt (napr. „Phi3-iOS-App“) a vyberte SwiftUI ako používateľské rozhranie
4. vyberte miesto, kam chcete projekt uložiť

## Krok 2: Pridanie potrebných závislostí

Pridajte [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples), ktorý obsahuje všetky potrebné závislosti a pomocné nástroje na prednačítanie modelov a vykonávanie inferencie:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Zatiaľ čo základný [MLX Swift package](https://github.com/ml-explore/mlx-swift) postačuje pre základné operácie s tenzormi a základnú ML funkcionalitu, balík MLX Examples poskytuje niekoľko ďalších komponentov určených na prácu s jazykovými modelmi a zjednodušenie inferenčného procesu:

- nástroje na načítanie modelov, ktoré zvládajú sťahovanie z Hugging Face
- integrácia tokenizéra
- pomocníci pre generovanie textu
- predkonfigurované definície modelov

## Krok 3: Konfigurácia oprávnení (Entitlements)

Aby naša aplikácia mohla sťahovať modely a alokovať dostatok pamäte, musíme pridať špecifické oprávnenia. Vytvorte `.entitlements` súbor pre vašu aplikáciu s nasledujúcim obsahom:

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

> **Poznámka:** Oprávnenie `com.apple.developer.kernel.increased-memory-limit` je dôležité pre spúšťanie väčších modelov, pretože umožňuje aplikácii žiadať o viac pamäte, než je bežne povolené.

## Krok 4: Vytvorenie modelu správy chatu

Najskôr si vytvoríme základnú štruktúru na reprezentáciu správ v chate:

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

- nastavenie limitu GPU cache pomocou `MLX.GPU.set(cacheLimit:)` na optimalizáciu využitia pamäte na mobilných zariadeniach
- použitie `LLMModelFactory` na sťahovanie modelu na požiadanie a inicializáciu MLX-optimalizovaného modelu
- prístup k parametrom a štruktúre modelu cez `ModelContainer`
- využitie token-po-tokene generovania pomocou metódy `MLXLMCommon.generate`
- riadenie inferenčného procesu s vhodným nastavením teploty a limitmi tokenov

Prístup generovania tokenov v reálnom čase poskytuje používateľom okamžitú spätnú väzbu počas generovania textu modelom. Je to podobné ako pri serverových modeloch, ktoré streamujú tokeny späť používateľovi, ale bez oneskorenia spôsobeného sieťovými požiadavkami.

Čo sa týka interakcie s UI, dve kľúčové funkcie sú `loadModel()`, ktorá inicializuje LLM, a `fetchAIResponse()`, ktorá spracováva vstup používateľa a generuje odpovede AI.

### Úvahy o formáte modelu

> **Dôležité:** Phi modely pre MLX nemožno používať v ich predvolenom alebo GGUF formáte. Musia byť prevedené do MLX formátu, čo zabezpečuje komunita MLX. Predkonvertované modely nájdete na [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Balík MLX Examples obsahuje predkonfigurované registrácie pre niekoľko modelov, vrátane Phi-3. Keď zavoláte `ModelRegistry.phi3_5_4bit`, odkazuje to na konkrétny predkonvertovaný MLX model, ktorý sa automaticky stiahne:

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

> **Poznámka:** Podpora Phi-4 bola pridaná do repozitára MLX Swift Examples koncom februára 2025 (v [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). K marcu 2025 najnovšie oficiálne vydanie (2.21.2 z decembra 2024) neobsahuje zabudovanú podporu Phi-4. Ak chcete používať Phi-4 modely, musíte odkazovať na balík priamo z hlavnej vetvy:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Tým získate prístup k najnovším konfiguráciám modelov vrátane Phi-4 ešte pred ich zaradením do oficiálneho vydania. Tento prístup môžete využiť na používanie rôznych verzií Phi modelov alebo iných modelov prevedených do MLX formátu.

## Krok 6: Vytvorenie používateľského rozhrania

Teraz implementujme jednoduché chatové rozhranie na interakciu s naším view modelom:

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

UI pozostáva z troch hlavných komponentov, ktoré spolu tvoria základné chatové rozhranie. `ContentView` vytvára rozhranie s dvoma stavmi, ktoré zobrazuje buď tlačidlo na načítanie modelu, alebo chat podľa pripravenosti modelu. `MessageView` zobrazuje jednotlivé správy v chate odlišne podľa toho, či ide o správy používateľa (zarovnané vpravo, modré pozadie) alebo odpovede Phi modelu (zarovnané vľavo, sivé pozadie). `TypingIndicatorView` poskytuje jednoduchý animovaný indikátor, ktorý ukazuje, že AI spracováva požiadavku.

## Krok 7: Kompilácia a spustenie aplikácie

Teraz sme pripravení aplikáciu zostaviť a spustiť.

> **Dôležité!** MLX nepodporuje simulátor. Aplikáciu musíte spustiť na fyzickom zariadení s čipom Apple Silicon. Viac informácií nájdete [tu](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Po spustení aplikácie klepnite na tlačidlo „Load model“ na stiahnutie a inicializáciu modelu Phi-3 (alebo podľa vašej konfigurácie Phi-4). Tento proces môže trvať určitý čas v závislosti od rýchlosti vášho internetového pripojenia, pretože zahŕňa sťahovanie modelu z Hugging Face. Naša implementácia obsahuje iba točiaci sa indikátor načítania, ale skutočný priebeh môžete sledovať v konzole Xcode.

Po načítaní môžete s modelom komunikovať písaním otázok do textového poľa a stlačením tlačidla odoslať.

Takto by mala naša aplikácia fungovať na iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Záver

A to je všetko! Dodržiavaním týchto krokov ste vytvorili iOS aplikáciu, ktorá spúšťa model Phi-3 (alebo Phi-4) priamo na zariadení pomocou Apple MLX frameworku.

Gratulujeme!

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.