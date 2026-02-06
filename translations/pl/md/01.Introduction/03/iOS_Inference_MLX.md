# Uruchamianie Phi-3 i Phi-4 na iOS z użyciem Apple MLX Framework

Ten samouczek pokazuje, jak stworzyć aplikację na iOS, która uruchamia model Phi-3 lub Phi-4 bezpośrednio na urządzeniu, korzystając z frameworka Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) to framework Apple do uczenia maszynowego zoptymalizowany pod kątem chipów Apple Silicon.

## Wymagania wstępne

- macOS z Xcode 16 (lub nowszym)
- urządzenie docelowe z iOS 18 (lub nowszym) z co najmniej 8 GB RAM (iPhone lub iPad spełniający wymagania Apple Intelligence, które są podobne do wymagań kwantyzowanego Phi)
- podstawowa znajomość Swift i SwiftUI

## Krok 1: Utwórz nowy projekt iOS

Zacznij od utworzenia nowego projektu iOS w Xcode:

1. uruchom Xcode i wybierz „Create a new Xcode project”
2. wybierz szablon „App”
3. nazwij swój projekt (np. „Phi3-iOS-App”) i wybierz SwiftUI jako interfejs
4. wybierz lokalizację do zapisania projektu

## Krok 2: Dodaj wymagane zależności

Dodaj pakiet [MLX Examples](https://github.com/ml-explore/mlx-swift-examples), który zawiera wszystkie niezbędne zależności i pomocniki do wczytywania modeli i wykonywania inferencji:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Podstawowy pakiet [MLX Swift](https://github.com/ml-explore/mlx-swift) wystarczyłby do podstawowych operacji na tensorach i funkcji ML, ale pakiet MLX Examples dostarcza dodatkowe komponenty zaprojektowane do pracy z modelami językowymi i ułatwiające proces inferencji:

- narzędzia do ładowania modeli, które obsługują pobieranie z Hugging Face
- integrację tokenizera
- pomocniki do generowania tekstu
- wstępnie skonfigurowane definicje modeli

## Krok 3: Skonfiguruj uprawnienia

Aby umożliwić aplikacji pobieranie modeli i przydzielenie odpowiedniej ilości pamięci, musimy dodać odpowiednie uprawnienia. Utwórz plik `.entitlements` dla swojej aplikacji z następującą zawartością:

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

> **Note:** Uprawnienie `com.apple.developer.kernel.increased-memory-limit` jest ważne dla uruchamiania większych modeli, ponieważ pozwala aplikacji na żądanie większej ilości pamięci niż zwykle dozwolona.

## Krok 4: Utwórz model wiadomości czatu

Najpierw stwórzmy prostą strukturę reprezentującą nasze wiadomości czatu:

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

Następnie utworzymy klasę `PhiViewModel`, która zajmie się ładowaniem modelu i inferencją:

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

- ustawianie limitów pamięci podręcznej GPU za pomocą `MLX.GPU.set(cacheLimit:)` w celu optymalizacji wykorzystania pamięci na urządzeniach mobilnych
- użycie `LLMModelFactory` do pobierania modelu na żądanie i inicjalizacji modelu zoptymalizowanego pod MLX
- dostęp do parametrów i struktury modelu przez `ModelContainer`
- wykorzystanie generowania token po tokenie MLX za pomocą metody `MLXLMCommon.generate`
- zarządzanie procesem inferencji z odpowiednimi ustawieniami temperatury i limitami tokenów

Podejście do generowania tokenów w trybie strumieniowym zapewnia użytkownikom natychmiastową informację zwrotną podczas generowania tekstu przez model. Jest to podobne do działania modeli serwerowych, które przesyłają tokeny do użytkownika na bieżąco, ale bez opóźnień związanych z zapytaniami sieciowymi.

W kontekście interakcji UI, dwie kluczowe funkcje to `loadModel()`, która inicjalizuje LLM, oraz `fetchAIResponse()`, która przetwarza dane wejściowe użytkownika i generuje odpowiedzi AI.

### Uwagi dotyczące formatu modelu

> **Important:** Modele Phi dla MLX nie mogą być używane w ich domyślnym lub formacie GGUF. Muszą zostać przekonwertowane do formatu MLX, co jest realizowane przez społeczność MLX. Możesz znaleźć modele już przekonwertowane na [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Pakiet MLX Examples zawiera wstępnie skonfigurowane rejestracje dla kilku modeli, w tym Phi-3. Gdy wywołujesz `ModelRegistry.phi3_5_4bit`, odnosi się to do konkretnego, wcześniej przekonwertowanego modelu MLX, który zostanie automatycznie pobrany:

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

> **Note:** Wsparcie dla Phi-4 zostało dodane do repozytorium MLX Swift Examples pod koniec lutego 2025 (w [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Na dzień marca 2025, najnowsza oficjalna wersja (2.21.2 z grudnia 2024) nie zawiera wbudowanego wsparcia dla Phi-4. Aby korzystać z modeli Phi-4, musisz odwołać się do pakietu bezpośrednio z gałęzi main:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Daje to dostęp do najnowszych konfiguracji modeli, w tym Phi-4, zanim zostaną one uwzględnione w oficjalnym wydaniu. Możesz użyć tego sposobu, aby korzystać z różnych wersji modeli Phi lub innych modeli przekonwertowanych do formatu MLX.

## Krok 6: Utwórz interfejs użytkownika

Zaimplementujmy teraz prosty interfejs czatu do interakcji z naszym ViewModel:

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

UI składa się z trzech głównych komponentów, które współpracują, tworząc podstawowy interfejs czatu. `ContentView` tworzy interfejs dwustanowy, który pokazuje przycisk ładowania lub interfejs czatu w zależności od gotowości modelu. `MessageView` renderuje pojedyncze wiadomości czatu inaczej, w zależności od tego, czy są to wiadomości użytkownika (wyrównane do prawej, niebieskie tło), czy odpowiedzi modelu Phi (wyrównane do lewej, szare tło). `TypingIndicatorView` zapewnia prosty animowany wskaźnik pokazujący, że AI przetwarza dane.

## Krok 7: Budowanie i uruchamianie aplikacji

Jesteśmy gotowi, aby zbudować i uruchomić aplikację.

> **Important!** MLX nie obsługuje symulatora. Musisz uruchomić aplikację na fizycznym urządzeniu z chipem Apple Silicon. Więcej informacji znajdziesz [tutaj](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Po uruchomieniu aplikacji, stuknij przycisk „Load model”, aby pobrać i zainicjalizować model Phi-3 (lub, w zależności od konfiguracji, Phi-4). Proces ten może potrwać chwilę, w zależności od szybkości połączenia internetowego, ponieważ obejmuje pobieranie modelu z Hugging Face. Nasza implementacja zawiera tylko spinner wskazujący ładowanie, ale rzeczywisty postęp można zobaczyć w konsoli Xcode.

Po załadowaniu możesz wchodzić w interakcję z modelem, wpisując pytania w polu tekstowym i stukając przycisk wysyłania.

Tak powinna działać nasza aplikacja, uruchomiona na iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Podsumowanie

I to wszystko! Postępując zgodnie z tymi krokami, stworzyłeś aplikację na iOS, która uruchamia model Phi-3 (lub Phi-4) bezpośrednio na urządzeniu, korzystając z frameworka Apple MLX.

Gratulacje!

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.