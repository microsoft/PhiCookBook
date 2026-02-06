# Spuštění Phi-3 a Phi-4 na iOS s Apple MLX Frameworkem

Tento tutoriál ukazuje, jak vytvořit iOS aplikaci, která spustí model Phi-3 nebo Phi-4 přímo na zařízení pomocí Apple MLX frameworku. [MLX](https://opensource.apple.com/projects/mlx/) je Apple framework pro strojové učení optimalizovaný pro čipy Apple Silicon.

## Požadavky

- macOS s Xcode 16 (nebo novějším)
- iOS 18 (nebo novější) cílové zařízení s minimálně 8GB RAM (iPhone nebo iPad kompatibilní s požadavky Apple Intelligence, které jsou podobné požadavkům na kvantizovaný Phi)
- základní znalost Swift a SwiftUI

## Krok 1: Vytvoření nového iOS projektu

Začněte vytvořením nového iOS projektu v Xcode:

1. spusťte Xcode a vyberte „Create a new Xcode project“
2. zvolte šablonu „App“
3. pojmenujte svůj projekt (např. „Phi3-iOS-App“) a vyberte SwiftUI jako rozhraní
4. vyberte místo, kam projekt uložíte

## Krok 2: Přidání potřebných závislostí

Přidejte balíček [MLX Examples](https://github.com/ml-explore/mlx-swift-examples), který obsahuje všechny potřebné závislosti a pomocné funkce pro přednačítání modelů a provádění inference:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Zatímco základní [MLX Swift balíček](https://github.com/ml-explore/mlx-swift) by stačil pro základní operace s tensory a základní ML funkce, balíček MLX Examples přináší několik dalších komponent navržených pro práci s jazykovými modely a usnadnění inference:

- nástroje pro načítání modelů, které zvládají stahování z Hugging Face
- integraci tokenizéru
- pomocníky pro generování textu
- přednastavené definice modelů

## Krok 3: Konfigurace oprávnění (Entitlements)

Aby naše aplikace mohla stahovat modely a alokovat dostatek paměti, musíme přidat specifická oprávnění. Vytvořte `.entitlements` soubor pro vaši aplikaci s následujícím obsahem:

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

> **Poznámka:** Oprávnění `com.apple.developer.kernel.increased-memory-limit` je důležité pro spuštění větších modelů, protože umožňuje aplikaci požádat o více paměti, než je běžně povoleno.

## Krok 4: Vytvoření modelu zprávy chatu

Nejprve vytvoříme základní strukturu pro reprezentaci našich chatových zpráv:

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

## Krok 5: Implementace ViewModelu

Dále vytvoříme třídu `PhiViewModel`, která se postará o načítání modelu a inference:

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

ViewModel ukazuje klíčové body integrace MLX:

- nastavení limitu GPU cache pomocí `MLX.GPU.set(cacheLimit:)` pro optimalizaci využití paměti na mobilních zařízeních
- použití `LLMModelFactory` pro on-demand stažení modelu a inicializaci MLX-optimalizovaného modelu
- přístup k parametrům a struktuře modelu přes `ModelContainer`
- využití token-po-token generování MLX pomocí metody `MLXLMCommon.generate`
- řízení inference s vhodným nastavením teploty a limitů tokenů

Přístup generování tokenů ve streamu poskytuje uživatelům okamžitou zpětnou vazbu během generování textu modelem. Je to podobné jako u serverových modelů, které tokeny posílají zpět uživateli průběžně, ale bez zpoždění způsobeného síťovými požadavky.

Z hlediska UI jsou klíčové dvě funkce: `loadModel()`, která inicializuje LLM, a `fetchAIResponse()`, která zpracovává uživatelský vstup a generuje odpovědi AI.

### Úvahy o formátu modelu

> **Důležité:** Phi modely pro MLX nelze použít ve výchozím nebo GGUF formátu. Musí být převedeny do MLX formátu, což zajišťuje komunita MLX. Převedené modely najdete na [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Balíček MLX Examples obsahuje přednastavené registrace pro několik modelů, včetně Phi-3. Když zavoláte `ModelRegistry.phi3_5_4bit`, odkazuje to na konkrétní předpřeváděný MLX model, který se automaticky stáhne:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Můžete si vytvořit vlastní konfigurace modelů, které budou odkazovat na jakýkoli kompatibilní model na Hugging Face. Například pro použití Phi-4 mini můžete definovat vlastní konfiguraci:

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

> **Poznámka:** Podpora Phi-4 byla přidána do repozitáře MLX Swift Examples koncem února 2025 (v [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). K březnu 2025 nejnovější oficiální verze (2.21.2 z prosince 2024) nepodporuje Phi-4 nativně. Pro použití Phi-4 modelů je třeba odkazovat balíček přímo z hlavní větve:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Tím získáte přístup k nejnovějším konfiguracím modelů, včetně Phi-4, ještě před jejich zařazením do oficiálního vydání. Tento přístup můžete využít pro různé verze Phi modelů nebo i jiné modely převedené do MLX formátu.

## Krok 6: Vytvoření uživatelského rozhraní

Nyní implementujeme jednoduché chatovací rozhraní pro interakci s naším view modelem:

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

UI se skládá ze tří hlavních komponent, které společně tvoří základní chatovací rozhraní. `ContentView` vytváří rozhraní se dvěma stavy, které zobrazuje buď tlačítko pro načtení modelu, nebo chatovací rozhraní podle připravenosti modelu. `MessageView` vykresluje jednotlivé zprávy chatu odlišně podle toho, zda jde o uživatelskou zprávu (zarovnanou vpravo, modré pozadí) nebo odpověď modelu Phi (zarovnanou vlevo, šedé pozadí). `TypingIndicatorView` poskytuje jednoduchý animovaný indikátor, který ukazuje, že AI právě zpracovává vstup.

## Krok 7: Sestavení a spuštění aplikace

Nyní jsme připraveni aplikaci sestavit a spustit.

> **Důležité!** MLX nepodporuje simulátor. Aplikaci musíte spustit na fyzickém zařízení s čipem Apple Silicon. Více informací najdete [zde](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Po spuštění aplikace klepněte na tlačítko „Load model“ pro stažení a inicializaci modelu Phi-3 (nebo podle vaší konfigurace Phi-4). Tento proces může trvat déle v závislosti na rychlosti vašeho internetového připojení, protože se model stahuje z Hugging Face. Naše implementace zobrazuje pouze načítací spinner, ale skutečný průběh můžete sledovat v konzoli Xcode.

Po načtení můžete s modelem komunikovat zadáváním otázek do textového pole a stisknutím tlačítka odeslat.

Takto by měla naše aplikace fungovat na iPadu Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Závěr

A je to! Pokud jste postupovali podle těchto kroků, vytvořili jste iOS aplikaci, která spouští model Phi-3 (nebo Phi-4) přímo na zařízení pomocí Apple MLX frameworku.

Gratulujeme!

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.