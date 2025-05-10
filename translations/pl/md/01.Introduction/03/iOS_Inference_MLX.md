<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:13:01+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "pl"
}
-->
# Uruchamianie Phi-3 i Phi-4 na iOS z użyciem Apple MLX Framework

Ten poradnik pokazuje, jak stworzyć aplikację na iOS, która uruchamia model Phi-3 lub Phi-4 lokalnie na urządzeniu, korzystając z frameworka Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) to framework Apple do uczenia maszynowego zoptymalizowany pod kątem chipów Apple Silicon.

## Wymagania wstępne

- macOS z Xcode 16 (lub nowszym)
- urządzenie docelowe z iOS 18 (lub nowszym) z co najmniej 8 GB pamięci (iPhone lub iPad kompatybilny z wymaganiami Apple Intelligence, podobnymi do wymagań kwantyzowanego Phi)
- podstawowa znajomość Swift i SwiftUI

## Krok 1: Utwórz nowy projekt iOS

Zacznij od stworzenia nowego projektu iOS w Xcode:

1. uruchom Xcode i wybierz "Create a new Xcode project"
2. wybierz szablon "App"
3. nazwij swój projekt (np. "Phi3-iOS-App") i wybierz SwiftUI jako interfejs
4. wybierz lokalizację do zapisania projektu

## Krok 2: Dodaj wymagane zależności

Dodaj pakiet [MLX Examples](https://github.com/ml-explore/mlx-swift-examples), który zawiera wszystkie potrzebne zależności i pomocniki do wstępnego ładowania modeli oraz przeprowadzania inferencji:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Podczas gdy podstawowy pakiet [MLX Swift](https://github.com/ml-explore/mlx-swift) wystarczyłby do podstawowych operacji na tensorach i podstawowej funkcjonalności ML, pakiet MLX Examples dostarcza dodatkowe komponenty przeznaczone do pracy z modelami językowymi oraz ułatwiające proces inferencji:

- narzędzia do ładowania modeli, które obsługują pobieranie z Hugging Face
- integracja tokenizera
- pomocniki do generowania tekstu
- wstępnie skonfigurowane definicje modeli

## Krok 3: Skonfiguruj uprawnienia

Aby umożliwić naszej aplikacji pobieranie modeli i przydzielanie odpowiedniej ilości pamięci, musimy dodać odpowiednie uprawnienia. Utwórz plik `.entitlements` dla swojej aplikacji z następującą zawartością:

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

> **Note:** Uprawnienie `com.apple.developer.kernel.increased-memory-limit` jest ważne do uruchamiania większych modeli, ponieważ pozwala aplikacji na żądanie większej ilości pamięci niż standardowo dozwolona.

## Krok 4: Utwórz model wiadomości czatu

Najpierw stwórzmy podstawową strukturę reprezentującą nasze wiadomości czatu:

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

## Krok 5: Zaimplementuj ViewModel

Następnie stworzymy klasę `PhiViewModel`, która będzie odpowiedzialna za ładowanie modelu i inferencję:

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

ViewModel pokazuje kluczowe punkty integracji z MLX:

- ustawianie limitu pamięci GPU za pomocą `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, odnosi się do konkretnego wstępnie skonwertowanego modelu MLX, który zostanie automatycznie pobrany:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Możesz stworzyć własne konfiguracje modeli, wskazujące na dowolny kompatybilny model na Hugging Face. Na przykład, aby użyć Phi-4 mini, możesz zdefiniować własną konfigurację:

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

> **Note:** Obsługa Phi-4 została dodana do repozytorium MLX Swift Examples pod koniec lutego 2025 (w [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Na marzec 2025 najnowsza oficjalna wersja (2.21.2 z grudnia 2024) nie zawiera wbudowanego wsparcia dla Phi-4. Aby korzystać z modeli Phi-4, musisz odwołać się do pakietu bezpośrednio z gałęzi głównej:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Daje to dostęp do najnowszych konfiguracji modeli, w tym Phi-4, zanim zostaną one uwzględnione w oficjalnym wydaniu. Możesz wykorzystać to podejście do korzystania z różnych wersji modeli Phi lub innych modeli przekonwertowanych do formatu MLX.

## Krok 6: Utwórz interfejs użytkownika

Teraz zaimplementujmy prosty interfejs czatu do komunikacji z naszym ViewModel:

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

Interfejs składa się z trzech głównych komponentów, które współpracują, tworząc podstawowy interfejs czatu. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` zapewnia prosty animowany wskaźnik pokazujący, że AI przetwarza dane

## Krok 7: Budowanie i uruchamianie aplikacji

Jesteśmy gotowi do zbudowania i uruchomienia aplikacji.

> **Important!** MLX nie obsługuje symulatora. Musisz uruchomić aplikację na fizycznym urządzeniu z chipem Apple Silicon. Więcej informacji znajdziesz [tutaj](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Po uruchomieniu aplikacji, naciśnij przycisk "Load model", aby pobrać i zainicjalizować model Phi-3 (lub, w zależności od konfiguracji, Phi-4). Proces ten może potrwać chwilę w zależności od prędkości Twojego internetu, ponieważ obejmuje pobieranie modelu z Hugging Face. Nasza implementacja zawiera tylko spinner wskazujący ładowanie, ale faktyczny postęp możesz zobaczyć w konsoli Xcode.

Po załadowaniu możesz wchodzić w interakcję z modelem, wpisując pytania w polu tekstowym i naciskając przycisk wysyłania.

Tak powinna zachowywać się nasza aplikacja działająca na iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Podsumowanie

I to wszystko! Postępując według tych kroków, stworzyłeś aplikację iOS, która uruchamia model Phi-3 (lub Phi-4) bezpośrednio na urządzeniu, korzystając z frameworka Apple MLX.

Gratulacje!

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.