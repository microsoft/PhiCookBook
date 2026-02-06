# Стартиране на Phi-3 и Phi-4 на iOS с Apple MLX Framework

Този урок показва как да създадете iOS приложение, което изпълнява модела Phi-3 или Phi-4 директно на устройството, използвайки Apple MLX framework. [MLX](https://opensource.apple.com/projects/mlx/) е машинно обучителна рамка на Apple, оптимизирана за чипове Apple Silicon.

## Изисквания

- macOS с Xcode 16 (или по-нова версия)
- iOS 18 (или по-нова) устройство с поне 8GB RAM (iPhone или iPad, съвместими с изискванията на Apple Intelligence, тъй като те са сходни с изискванията за квантизираните Phi модели)
- основни познания по Swift и SwiftUI

## Стъпка 1: Създаване на нов iOS проект

Започнете със създаване на нов iOS проект в Xcode:

1. стартирайте Xcode и изберете "Create a new Xcode project"
2. изберете шаблона "App"
3. наименувайте проекта си (например "Phi3-iOS-App") и изберете SwiftUI като интерфейс
4. изберете място за запазване на проекта

## Стъпка 2: Добавяне на необходими зависимости

Добавете [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples), който съдържа всички необходими зависимости и помощни средства за предварително зареждане на модели и извършване на инференция:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Докато базовият [MLX Swift package](https://github.com/ml-explore/mlx-swift) е достатъчен за основни тензорни операции и базова ML функционалност, MLX Examples пакетът предоставя допълнителни компоненти, предназначени за работа с езикови модели и улесняване на процеса на инференция:

- помощни средства за зареждане на модели, които се грижат за изтегляне от Hugging Face
- интеграция на токенизатор
- помощници за инференция при генериране на текст
- предварително конфигурирани дефиниции на модели

## Стъпка 3: Конфигуриране на права (Entitlements)

За да позволим на приложението да изтегля модели и да заделя достатъчно памет, трябва да добавим специфични права. Създайте `.entitlements` файл за вашето приложение със следното съдържание:

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

> **Note:** Правото `com.apple.developer.kernel.increased-memory-limit` е важно за стартиране на по-големи модели, тъй като позволява на приложението да поиска повече памет от обичайно разрешената.

## Стъпка 4: Създаване на модела за чат съобщения

Първо, нека създадем базова структура, която да представя нашите чат съобщения:

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

## Стъпка 5: Имплементиране на ViewModel

След това ще създадем класа `PhiViewModel`, който се грижи за зареждането на модела и инференцията:

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

ViewModel демонстрира ключовите точки на интеграция с MLX:

- задаване на лимити за GPU кеша с `MLX.GPU.set(cacheLimit:)` за оптимизиране на използването на памет на мобилни устройства
- използване на `LLMModelFactory` за изтегляне на модела при поискване и инициализиране на MLX-оптимизирания модел
- достъп до параметрите и структурата на модела чрез `ModelContainer`
- използване на токен-по-токен генериране чрез метода `MLXLMCommon.generate`
- управление на процеса на инференция с подходящи настройки за температура и лимити на токени

Подходът с поточно генериране на токени осигурява незабавна обратна връзка към потребителите, докато моделът генерира текст. Това е подобно на начина, по който работят сървърните модели, които изпращат токените обратно към потребителя, но без забавяне от мрежови заявки.

Що се отнася до взаимодействието с потребителския интерфейс, двете ключови функции са `loadModel()`, която инициализира LLM, и `fetchAIResponse()`, която обработва входа от потребителя и генерира AI отговори.

### Съображения относно формата на модела

> **Important:** Phi моделите за MLX не могат да се използват в техния стандартен или GGUF формат. Те трябва да бъдат конвертирани във формат MLX, което се извършва от MLX общността. Можете да намерите предварително конвертирани модели на [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

MLX Examples пакетът включва предварително конфигурирани регистрации за няколко модела, включително Phi-3. Когато извикате `ModelRegistry.phi3_5_4bit`, той препраща към конкретен предварително конвертиран MLX модел, който ще бъде изтеглен автоматично:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Можете да създадете свои собствени конфигурации на модели, които сочат към всеки съвместим модел в Hugging Face. Например, за да използвате Phi-4 mini, можете да дефинирате своя конфигурация:

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

> **Note:** Поддръжката на Phi-4 беше добавена в MLX Swift Examples хранилището в края на февруари 2025 (в [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Към март 2025, последното официално издание (2.21.2 от декември 2024) не включва вградена поддръжка за Phi-4. За да използвате Phi-4 модели, трябва да реферирате пакета директно от основния клон:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Това ви дава достъп до най-новите конфигурации на модели, включително Phi-4, преди да бъдат включени в официално издание. Можете да използвате този подход, за да ползвате различни версии на Phi модели или дори други модели, конвертирани във формат MLX.

## Стъпка 6: Създаване на потребителския интерфейс

Сега нека имплементираме прост чат интерфейс за взаимодействие с нашия view model:

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

Потребителският интерфейс се състои от три основни компонента, които работят заедно, за да създадат базов чат интерфейс. `ContentView` създава интерфейс с два състояния, който показва или бутон за зареждане, или чат интерфейс в зависимост от готовността на модела. `MessageView` визуализира отделните чат съобщения по различен начин в зависимост дали са съобщения от потребителя (подравнени вдясно, със син фон) или отговори на Phi модела (подравнени вляво, със сив фон). `TypingIndicatorView` предоставя прост анимиран индикатор, който показва, че AI обработва заявката.

## Стъпка 7: Компилиране и стартиране на приложението

Сега сме готови да компилираме и стартираме приложението.

> **Important!** MLX не поддържа симулатора. Трябва да стартирате приложението на физическо устройство с Apple Silicon чип. Вижте [тук](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) за повече информация.

Когато приложението се стартира, натиснете бутона "Load model", за да изтеглите и инициализирате модела Phi-3 (или, в зависимост от конфигурацията, Phi-4). Този процес може да отнеме известно време в зависимост от интернет връзката ви, тъй като включва изтегляне на модела от Hugging Face. Нашата имплементация включва само въртящ се индикатор за зареждане, но можете да видите реалния прогрес в конзолата на Xcode.

След като моделът е зареден, можете да взаимодействате с него, като въвеждате въпроси в текстовото поле и натискате бутона за изпращане.

Ето как трябва да се държи нашето приложение, работещо на iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Заключение

Това е всичко! Следвайки тези стъпки, създадохте iOS приложение, което изпълнява модела Phi-3 (или Phi-4) директно на устройството, използвайки Apple MLX framework.

Поздравления!

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.