<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:21:56+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "hu"
}
-->
# Phi-3 és Phi-4 futtatása iOS-en az Apple MLX keretrendszerrel

Ez a bemutató megmutatja, hogyan készíthetünk iOS alkalmazást, amely a Phi-3 vagy Phi-4 modellt helyben futtatja az Apple MLX keretrendszer segítségével. Az [MLX](https://opensource.apple.com/projects/mlx/) az Apple gépi tanulási keretrendszere, amely az Apple Silicon chipekre van optimalizálva.

## Előfeltételek

- macOS Xcode 16-tal (vagy újabb)
- iOS 18 (vagy újabb) célkészülék, legalább 8 GB memóriával (iPhone vagy iPad, amely megfelel az Apple Intelligence követelményeinek, mivel ezek hasonlóak a kvantált Phi követelményekhez)
- alapvető Swift és SwiftUI ismeretek

## 1. lépés: Új iOS projekt létrehozása

Kezdjük egy új iOS projekt létrehozásával Xcode-ban:

1. Indítsd el az Xcode-ot, és válaszd a „Create a new Xcode project” lehetőséget
2. Válaszd az „App” sablont
3. Nevezd el a projektet (pl. „Phi3-iOS-App”), és válaszd a SwiftUI-t felületként
4. Válassz helyet a projekt mentéséhez

## 2. lépés: Szükséges függőségek hozzáadása

Add hozzá az [MLX Examples csomagot](https://github.com/ml-explore/mlx-swift-examples), amely tartalmazza az összes szükséges függőséget és segédeszközt a modellek előtöltéséhez és az inferencia végrehajtásához:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Míg az alap [MLX Swift csomag](https://github.com/ml-explore/mlx-swift) elegendő az alapvető tenzor műveletekhez és ML funkciókhoz, az MLX Examples csomag további komponenseket kínál a nyelvi modellekkel való munkához és az inferencia folyamat megkönnyítéséhez:

- modell betöltő segédprogramok, amelyek kezelik a Hugging Face-ről való letöltést
- tokenizáló integráció
- inferencia segédek szöveg generáláshoz
- előre konfigurált modell definíciók

## 3. lépés: Jogosultságok beállítása

Ahhoz, hogy az alkalmazásunk modelleket tölthessen le és elegendő memóriát foglalhasson, hozzá kell adnunk bizonyos jogosultságokat. Hozz létre egy `.entitlements` fájlt az alkalmazásodhoz az alábbi tartalommal:

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

> **Megjegyzés:** A `com.apple.developer.kernel.increased-memory-limit` jogosultság fontos a nagyobb modellek futtatásához, mert lehetővé teszi az alkalmazás számára, hogy több memóriát kérjen, mint ami általában engedélyezett.

## 4. lépés: Chat üzenet modell létrehozása

Először hozzunk létre egy egyszerű struktúrát a chat üzenetek reprezentálásához:

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

## 5. lépés: ViewModel implementálása

Ezután készítsük el a `PhiViewModel` osztályt, amely kezeli a modell betöltését és az inferenciát:

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

A ViewModel bemutatja az MLX integráció kulcspontjait:

- GPU cache korlát beállítása `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit` segítségével, amely egy konkrét előre átkonvertált MLX modellt hivatkozik, amely automatikusan letöltődik:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Saját modell konfigurációkat is létrehozhatsz, amelyek bármilyen kompatibilis modellt a Hugging Face-ről céloznak meg. Például, ha a Phi-4 mini modellt szeretnéd használni, definiálhatod a saját konfigurációdat:

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

> **Megjegyzés:** A Phi-4 támogatás 2025 február végén került hozzáadásra az MLX Swift Examples tárolóhoz ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). 2025 márciusáig a legfrissebb hivatalos kiadás (a 2024 decemberi 2.21.2 verzió) nem tartalmaz beépített Phi-4 támogatást. A Phi-4 modellek használatához közvetlenül a főágból kell hivatkoznod a csomagra:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Ez hozzáférést ad a legfrissebb modell konfigurációkhoz, beleértve a Phi-4-et is, mielőtt azok hivatalos kiadásba kerülnének. Ezzel a módszerrel különböző Phi modellek vagy akár más MLX formátumra konvertált modellek különböző verzióit is használhatod.

## 6. lépés: Felhasználói felület létrehozása

Most valósítsunk meg egy egyszerű chat felületet, amellyel kommunikálhatunk a view modellel:

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

A felhasználói felület három fő komponensből áll, amelyek együtt alkotnak egy alap chat felületet. A `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` egyszerű animált jelzést ad, hogy az AI éppen dolgozik.

## 7. lépés: Az alkalmazás buildelése és futtatása

Most készen állunk az alkalmazás buildelésére és futtatására.

> **Fontos!** Az MLX nem támogatja a szimulátort. Az alkalmazást fizikai Apple Silicon chippel rendelkező eszközön kell futtatni. További információkért lásd [itt](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Az alkalmazás indításakor érintsd meg a „Load model” gombot, hogy letöltsd és inicializáld a Phi-3 (vagy a konfigurációdtól függően Phi-4) modellt. Ez a folyamat az internetkapcsolatodtól függően eltarthat egy ideig, mivel a modellt a Hugging Face-ről tölti le. A megvalósítás csak egy betöltést jelző forgó ikont tartalmaz, de az aktuális folyamat előrehaladását az Xcode konzoljában követheted.

Betöltés után kérdéseket írva a szövegmezőbe, majd a küldés gombra kattintva léphetsz interakcióba a modellel.

Így kell működnie az alkalmazásunknak iPad Air M1-en futtatva:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Összegzés

Ennyi volt! Ezeknek a lépéseknek a követésével létrehoztál egy iOS alkalmazást, amely az Apple MLX keretrendszer segítségével közvetlenül az eszközön futtatja a Phi-3 (vagy Phi-4) modellt.

Gratulálunk!

**Felelősségkizárás**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.