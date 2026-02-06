# Rularea Phi-3 și Phi-4 pe iOS cu Apple MLX Framework

Acest tutorial arată cum să creezi o aplicație iOS care rulează modelul Phi-3 sau Phi-4 direct pe dispozitiv, folosind framework-ul Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) este framework-ul Apple pentru învățare automată, optimizat pentru cipurile Apple Silicon.

## Cerințe preliminare

- macOS cu Xcode 16 (sau versiune superioară)
- Dispozitiv țintă iOS 18 (sau versiune superioară) cu cel puțin 8GB RAM (iPhone sau iPad compatibil cu cerințele Apple Intelligence, similare cu cele pentru Phi cuantificat)
- cunoștințe de bază despre Swift și SwiftUI

## Pasul 1: Creează un proiect iOS nou

Începe prin a crea un proiect iOS nou în Xcode:

1. deschide Xcode și selectează „Create a new Xcode project”
2. alege șablonul „App”
3. denumește proiectul (de exemplu, „Phi3-iOS-App”) și selectează SwiftUI ca interfață
4. alege o locație pentru salvarea proiectului

## Pasul 2: Adaugă dependențele necesare

Adaugă pachetul [MLX Examples](https://github.com/ml-explore/mlx-swift-examples) care conține toate dependențele și ajutoarele necesare pentru încărcarea modelelor și efectuarea inferenței:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Deși pachetul de bază [MLX Swift](https://github.com/ml-explore/mlx-swift) este suficient pentru operațiuni tensoriale de bază și funcționalități ML simple, pachetul MLX Examples oferă componente suplimentare pentru lucrul cu modele de limbaj și pentru a simplifica procesul de inferență:

- utilitare pentru încărcarea modelelor care gestionează descărcarea de pe Hugging Face
- integrare tokenizer
- ajutoare pentru generarea textului
- definiții preconfigurate ale modelelor

## Pasul 3: Configurează entitlements

Pentru a permite aplicației să descarce modele și să aloce suficientă memorie, trebuie să adăugăm entitlements specifice. Creează un fișier `.entitlements` pentru aplicația ta cu următorul conținut:

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

> **Note:** Entitlement-ul `com.apple.developer.kernel.increased-memory-limit` este important pentru rularea modelelor mai mari, deoarece permite aplicației să solicite mai multă memorie decât în mod normal.

## Pasul 4: Creează modelul pentru mesajele din chat

Mai întâi, să creăm o structură simplă pentru a reprezenta mesajele din chat:

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

## Pasul 5: Implementează ViewModel-ul

Apoi, vom crea clasa `PhiViewModel` care se ocupă de încărcarea modelului și inferență:

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

ViewModel-ul evidențiază punctele cheie de integrare MLX:

- setarea limitelor cache-ului GPU cu `MLX.GPU.set(cacheLimit:)` pentru optimizarea utilizării memoriei pe dispozitive mobile
- folosirea `LLMModelFactory` pentru descărcarea modelului la cerere și inițializarea modelului optimizat MLX
- accesarea parametrilor și structurii modelului prin `ModelContainer`
- utilizarea generării token cu token prin metoda `MLXLMCommon.generate`
- gestionarea procesului de inferență cu setări adecvate pentru temperatură și limite de tokeni

Abordarea de generare a tokenilor în streaming oferă feedback imediat utilizatorilor pe măsură ce modelul generează text. Este similară cu modul în care funcționează modelele pe server, care transmit tokenii înapoi utilizatorului, dar fără întârzierea cauzată de cererile de rețea.

În ceea ce privește interacțiunea UI, cele două funcții principale sunt `loadModel()`, care inițializează LLM-ul, și `fetchAIResponse()`, care procesează inputul utilizatorului și generează răspunsurile AI.

### Considerații privind formatul modelului

> **Important:** Modelele Phi pentru MLX nu pot fi folosite în formatul lor implicit sau GGUF. Ele trebuie convertite în formatul MLX, proces gestionat de comunitatea MLX. Poți găsi modele pre-convertite la [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Pachetul MLX Examples include înregistrări preconfigurate pentru mai multe modele, inclusiv Phi-3. Când apelezi `ModelRegistry.phi3_5_4bit`, acesta face referire la un model MLX pre-convertit specific, care va fi descărcat automat:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Poți crea propriile configurații de model pentru a indica orice model compatibil de pe Hugging Face. De exemplu, pentru a folosi Phi-4 mini, poți defini propria configurație:

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

> **Note:** Suportul pentru Phi-4 a fost adăugat în depozitul MLX Swift Examples la sfârșitul lunii februarie 2025 (în [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Până în martie 2025, ultima versiune oficială (2.21.2 din decembrie 2024) nu include suport nativ pentru Phi-4. Pentru a folosi modelele Phi-4, trebuie să faci referire direct la pachetul din ramura principală:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Aceasta îți oferă acces la cele mai noi configurații de modele, inclusiv Phi-4, înainte de a fi incluse într-o versiune oficială. Poți folosi această metodă pentru a utiliza diferite versiuni ale modelelor Phi sau chiar alte modele convertite în format MLX.

## Pasul 6: Creează interfața UI

Acum să implementăm o interfață simplă de chat pentru a interacționa cu view model-ul nostru:

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

Interfața UI este compusă din trei componente principale care lucrează împreună pentru a crea o interfață de chat de bază. `ContentView` creează o interfață cu două stări care afișează fie un buton de încărcare, fie interfața de chat, în funcție de starea de pregătire a modelului. `MessageView` afișează mesajele individuale diferit, în funcție de faptul că sunt mesaje ale utilizatorului (aliniate la dreapta, fundal albastru) sau răspunsuri ale modelului Phi (aliniate la stânga, fundal gri). `TypingIndicatorView` oferă un indicator animat simplu care arată că AI-ul procesează.

## Pasul 7: Construirea și rularea aplicației

Acum suntem gata să construim și să rulăm aplicația.

> **Important!** MLX nu suportă simulatorul. Trebuie să rulezi aplicația pe un dispozitiv fizic cu cip Apple Silicon. Vezi [aici](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) pentru mai multe informații.

La lansarea aplicației, apasă butonul „Load model” pentru a descărca și inițializa modelul Phi-3 (sau, în funcție de configurația ta, Phi-4). Acest proces poate dura ceva timp, în funcție de conexiunea ta la internet, deoarece implică descărcarea modelului de pe Hugging Face. Implementarea noastră include doar un spinner pentru a indica încărcarea, dar poți vedea progresul efectiv în consola Xcode.

Odată încărcat, poți interacționa cu modelul tastând întrebări în câmpul de text și apăsând butonul de trimitere.

Iată cum ar trebui să se comporte aplicația noastră, rulând pe un iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Concluzie

Și asta este tot! Urmând acești pași, ai creat o aplicație iOS care rulează modelul Phi-3 (sau Phi-4) direct pe dispozitiv folosind framework-ul MLX de la Apple.

Felicitări!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.