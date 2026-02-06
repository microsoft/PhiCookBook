# Phi-3 ir Phi-4 paleidimas iOS su Apple MLX sistema

Šiame vadove parodoma, kaip sukurti iOS programą, kuri vykdo Phi-3 arba Phi-4 modelį tiesiogiai įrenginyje, naudojant Apple MLX sistemą. [MLX](https://opensource.apple.com/projects/mlx/) yra Apple mašininio mokymosi sistema, optimizuota Apple Silicon lustams.

## Reikalavimai

- macOS su Xcode 16 (ar naujesne versija)
- iOS 18 (ar naujesnė) tikslinis įrenginys su bent 8GB (iPhone arba iPad, suderinamas su Apple Intelligence reikalavimais, kurie yra panašūs į kvantizuoto Phi reikalavimus)
- pagrindinės Swift ir SwiftUI žinios

## 1 žingsnis: Naujo iOS projekto sukūrimas

Pradėkite kurdami naują iOS projektą Xcode:

1. paleiskite Xcode ir pasirinkite „Create a new Xcode project“
2. pasirinkite „App“ kaip šabloną
3. pavadinkite savo projektą (pvz., „Phi3-iOS-App“) ir pasirinkite SwiftUI kaip sąsają
4. pasirinkite vietą, kur išsaugoti projektą

## 2 žingsnis: Reikalingų priklausomybių pridėjimas

Pridėkite [MLX Examples paketą](https://github.com/ml-explore/mlx-swift-examples), kuris apima visas reikalingas priklausomybes ir pagalbines priemones modelių išankstiniam įkrovimui ir inferencijai atlikti:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Nors bazinis [MLX Swift paketas](https://github.com/ml-explore/mlx-swift) yra pakankamas pagrindinėms tensorų operacijoms ir bazinėms ML funkcijoms, MLX Examples paketas siūlo keletą papildomų komponentų, skirtų darbui su kalbos modeliais ir inferencijos proceso palengvinimui:

- modelių įkrovimo įrankiai, kurie tvarko atsisiuntimą iš Hugging Face
- integracija su tokenizatoriumi
- inferencijos pagalbinės priemonės tekstų generavimui
- iš anksto sukonfigūruoti modelių apibrėžimai

## 3 žingsnis: Entitlementų konfigūravimas

Kad mūsų programa galėtų atsisiųsti modelius ir paskirstyti pakankamai atminties, turime pridėti specifinius entitlementus. Sukurkite `.entitlements` failą savo programai su šiuo turiniu:

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

> **Pastaba:** `com.apple.developer.kernel.increased-memory-limit` entitlementas yra svarbus didesnių modelių paleidimui, nes leidžia programai prašyti daugiau atminties nei paprastai leidžiama.

## 4 žingsnis: Pokalbių žinučių modelio sukūrimas

Pirmiausia sukurkime pagrindinę struktūrą, skirtą reprezentuoti mūsų pokalbių žinutes:

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

## 5 žingsnis: ViewModel įgyvendinimas

Toliau sukursime `PhiViewModel` klasę, kuri tvarko modelio įkrovimą ir inferenciją:

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

ViewModel parodo pagrindinius MLX integracijos taškus:

- GPU talpyklos limitų nustatymą su `MLX.GPU.set(cacheLimit:)`, siekiant optimizuoti atminties naudojimą mobiliuosiuose įrenginiuose
- `LLMModelFactory` naudojimą modelio atsisiuntimui pagal poreikį ir MLX optimizuoto modelio inicializavimą
- prieigą prie modelio parametrų ir struktūros per `ModelContainer`
- MLX tokenų generavimo metodą `MLXLMCommon.generate`
- inferencijos proceso valdymą su tinkamais temperatūros nustatymais ir tokenų limitais

Tokenų generavimo srauto metodas suteikia vartotojams tiesioginį grįžtamąjį ryšį, kai modelis generuoja tekstą. Tai panašu į serveriu pagrįstus modelius, kurie grąžina tokenus vartotojui, tačiau be tinklo užklausų vėlavimo.

Kalbant apie sąveiką su UI, pagrindinės funkcijos yra `loadModel()`, kuri inicializuoja LLM, ir `fetchAIResponse()`, kuri apdoroja vartotojo įvestį ir generuoja AI atsakymus.

### Modelio formato svarstymai

> **Svarbu:** Phi modeliai MLX negali būti naudojami jų numatytame arba GGUF formate. Jie turi būti konvertuoti į MLX formatą, kurį tvarko MLX bendruomenė. Iš anksto konvertuotus modelius galite rasti [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

MLX Examples paketas apima iš anksto sukonfigūruotas registracijas keliems modeliams, įskaitant Phi-3. Kai kviečiate `ModelRegistry.phi3_5_4bit`, tai nurodo specifinį iš anksto konvertuotą MLX modelį, kuris bus automatiškai atsisiųstas:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Galite sukurti savo modelio konfigūracijas, kad nurodytumėte bet kurį suderinamą modelį Hugging Face. Pavyzdžiui, norėdami naudoti Phi-4 mini, galite apibrėžti savo konfigūraciją:

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

> **Pastaba:** Phi-4 palaikymas buvo pridėtas MLX Swift Examples saugykloje 2025 m. vasario pabaigoje (PR #216). Nuo 2025 m. kovo naujausia oficiali versija (2.21.2 nuo 2024 m. gruodžio) neapima įmontuoto Phi-4 palaikymo. Norėdami naudoti Phi-4 modelius, turėsite nurodyti paketą tiesiai iš pagrindinės šakos:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Tai suteikia prieigą prie naujausių modelio konfigūracijų, įskaitant Phi-4, prieš jiems įtraukiant į oficialų leidimą. Šį metodą galite naudoti norėdami naudoti skirtingas Phi modelių versijas ar net kitus modelius, kurie buvo konvertuoti į MLX formatą.

## 6 žingsnis: UI sukūrimas

Dabar įgyvendinkime paprastą pokalbių sąsają, kad galėtume sąveikauti su mūsų ViewModel:

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

UI sudaro trys pagrindiniai komponentai, kurie kartu sukuria paprastą pokalbių sąsają. `ContentView` sukuria dviejų būsenų sąsają, kuri rodo arba įkrovimo mygtuką, arba pokalbių sąsają, priklausomai nuo modelio parengties. `MessageView` skirtingai atvaizduoja individualias pokalbių žinutes, priklausomai nuo to, ar tai vartotojo žinutės (dešinėje, mėlynas fonas), ar Phi modelio atsakymai (kairėje, pilkas fonas). `TypingIndicatorView` pateikia paprastą animuotą indikatorių, rodantį, kad AI apdoroja.

## 7 žingsnis: Programos kūrimas ir paleidimas

Dabar esame pasiruošę sukurti ir paleisti programą.

> **Svarbu!** MLX nepalaiko simuliatoriaus. Programą turite paleisti fiziniame įrenginyje su Apple Silicon lustu. Daugiau informacijos rasite [čia](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Kai programa paleidžiama, paspauskite „Load model“ mygtuką, kad atsisiųstumėte ir inicializuotumėte Phi-3 (arba, priklausomai nuo jūsų konfigūracijos, Phi-4) modelį. Šis procesas gali užtrukti, priklausomai nuo jūsų interneto ryšio, nes tai apima modelio atsisiuntimą iš Hugging Face. Mūsų įgyvendinimas apima tik suktuką, rodantį įkrovimą, tačiau faktinį progresą galite matyti Xcode konsolėje.

Kai modelis įkeltas, galite sąveikauti su juo, įvesdami klausimus teksto lauke ir paspausdami siuntimo mygtuką.

Štai kaip mūsų programa turėtų veikti, paleista iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Išvada

Ir viskas! Sekdami šiuos žingsnius, sukūrėte iOS programą, kuri tiesiogiai įrenginyje vykdo Phi-3 (arba Phi-4) modelį, naudodama Apple MLX sistemą.

Sveikiname!

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.