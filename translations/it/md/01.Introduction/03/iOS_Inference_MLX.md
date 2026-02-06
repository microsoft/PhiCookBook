# Esecuzione di Phi-3 e Phi-4 su iOS con Apple MLX Framework

Questo tutorial mostra come creare un'app iOS che esegue il modello Phi-3 o Phi-4 direttamente sul dispositivo, utilizzando il framework Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) è il framework di machine learning di Apple ottimizzato per i chip Apple Silicon.

## Prerequisiti

- macOS con Xcode 16 (o superiore)
- dispositivo iOS 18 (o superiore) con almeno 8GB di RAM (iPhone o iPad compatibile con i requisiti di Apple Intelligence, simili a quelli richiesti per Phi quantizzato)
- conoscenze di base di Swift e SwiftUI

## Passo 1: Crea un Nuovo Progetto iOS

Inizia creando un nuovo progetto iOS in Xcode:

1. avvia Xcode e seleziona "Create a new Xcode project"
2. scegli il template "App"
3. dai un nome al progetto (es. "Phi3-iOS-App") e seleziona SwiftUI come interfaccia
4. scegli una cartella in cui salvare il progetto

## Passo 2: Aggiungi le Dipendenze Necessarie

Aggiungi il pacchetto [MLX Examples](https://github.com/ml-explore/mlx-swift-examples) che contiene tutte le dipendenze e gli helper necessari per il pre-caricamento dei modelli e l’esecuzione dell’inferenza:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Mentre il pacchetto base [MLX Swift](https://github.com/ml-explore/mlx-swift) è sufficiente per le operazioni tensoriali di base e le funzionalità ML fondamentali, il pacchetto MLX Examples offre diversi componenti aggiuntivi pensati per lavorare con modelli di linguaggio e semplificare il processo di inferenza:

- utility per il caricamento dei modelli che gestiscono il download da Hugging Face
- integrazione del tokenizer
- helper per l’inferenza nella generazione di testo
- definizioni di modelli preconfigurate

## Passo 3: Configura gli Entitlements

Per permettere all’app di scaricare modelli e allocare memoria sufficiente, dobbiamo aggiungere specifici entitlements. Crea un file `.entitlements` per la tua app con il seguente contenuto:

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

> **Note:** L’entitlement `com.apple.developer.kernel.increased-memory-limit` è importante per eseguire modelli più grandi, poiché consente all’app di richiedere più memoria rispetto al limite standard.

## Passo 4: Crea il Modello per i Messaggi di Chat

Per prima cosa, creiamo una struttura base per rappresentare i messaggi di chat:

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

## Passo 5: Implementa il ViewModel

Successivamente, creiamo la classe `PhiViewModel` che gestisce il caricamento del modello e l’inferenza:

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

Il ViewModel mostra i punti chiave dell’integrazione con MLX:

- impostare i limiti della cache GPU con `MLX.GPU.set(cacheLimit:)` per ottimizzare l’uso della memoria su dispositivi mobili
- usare `LLMModelFactory` per scaricare il modello on-demand e inizializzare il modello ottimizzato MLX
- accedere ai parametri e alla struttura del modello tramite `ModelContainer`
- sfruttare la generazione token-per-token di MLX tramite il metodo `MLXLMCommon.generate`
- gestire il processo di inferenza con impostazioni appropriate di temperatura e limiti di token

L’approccio di generazione token in streaming fornisce un feedback immediato all’utente mentre il modello genera il testo. Questo è simile a come funzionano i modelli basati su server, che inviano i token in streaming all’utente, ma senza la latenza delle richieste di rete.

Per quanto riguarda l’interazione con l’interfaccia utente, le due funzioni principali sono `loadModel()`, che inizializza il LLM, e `fetchAIResponse()`, che elabora l’input dell’utente e genera le risposte AI.

### Considerazioni sul formato del modello

> **Importante:** I modelli Phi per MLX non possono essere usati nel loro formato predefinito o GGUF. Devono essere convertiti nel formato MLX, operazione gestita dalla community MLX. Puoi trovare modelli già convertiti su [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Il pacchetto MLX Examples include registrazioni preconfigurate per diversi modelli, incluso Phi-3. Quando chiami `ModelRegistry.phi3_5_4bit`, si fa riferimento a un modello MLX preconvertito specifico che verrà scaricato automaticamente:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Puoi creare le tue configurazioni di modello per puntare a qualsiasi modello compatibile su Hugging Face. Ad esempio, per usare Phi-4 mini, potresti definire una tua configurazione:

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

> **Note:** Il supporto per Phi-4 è stato aggiunto al repository MLX Swift Examples alla fine di febbraio 2025 (nel [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). A marzo 2025, l’ultima release ufficiale (2.21.2 di dicembre 2024) non include il supporto integrato per Phi-4. Per usare modelli Phi-4, devi fare riferimento al pacchetto direttamente dal branch main:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Questo ti dà accesso alle ultime configurazioni di modello, inclusa Phi-4, prima che vengano incluse in una release ufficiale. Puoi usare questo metodo per utilizzare versioni diverse dei modelli Phi o altri modelli convertiti nel formato MLX.

## Passo 6: Crea l’Interfaccia Utente

Ora implementiamo una semplice interfaccia di chat per interagire con il nostro view model:

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

L’interfaccia utente è composta da tre componenti principali che lavorano insieme per creare una chat di base. `ContentView` crea un’interfaccia a due stati che mostra un pulsante di caricamento o la chat a seconda della disponibilità del modello. `MessageView` rende i singoli messaggi di chat in modo diverso a seconda che siano messaggi dell’utente (allineati a destra, sfondo blu) o risposte del modello Phi (allineate a sinistra, sfondo grigio). `TypingIndicatorView` fornisce un semplice indicatore animato per mostrare che l’AI sta elaborando.

## Passo 7: Compilare ed Eseguire l’App

Ora siamo pronti per compilare ed eseguire l’applicazione.

> **Importante!** MLX non supporta il simulatore. Devi eseguire l’app su un dispositivo fisico con chip Apple Silicon. Vedi [qui](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) per maggiori informazioni.

Quando l’app si avvia, tocca il pulsante "Load model" per scaricare e inizializzare il modello Phi-3 (o, a seconda della configurazione, Phi-4). Questo processo può richiedere un po’ di tempo a seconda della connessione internet, poiché comporta il download del modello da Hugging Face. La nostra implementazione include solo un indicatore di caricamento, ma puoi vedere il progresso reale nella console di Xcode.

Una volta caricato, puoi interagire con il modello digitando domande nel campo di testo e premendo il pulsante di invio.

Ecco come dovrebbe comportarsi la nostra applicazione, in esecuzione su iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Conclusione

Ecco fatto! Seguendo questi passaggi, hai creato un’app iOS che esegue il modello Phi-3 (o Phi-4) direttamente sul dispositivo usando il framework MLX di Apple.

Congratulazioni!

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.