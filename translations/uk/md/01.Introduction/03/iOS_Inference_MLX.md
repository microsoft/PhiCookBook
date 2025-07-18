<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:38:13+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "uk"
}
-->
# Запуск Phi-3 та Phi-4 на iOS з використанням Apple MLX Framework

Цей посібник показує, як створити iOS-додаток, який запускає модель Phi-3 або Phi-4 безпосередньо на пристрої, використовуючи фреймворк Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) — це машинне навчання від Apple, оптимізоване для чипів Apple Silicon.

## Вимоги

- macOS з Xcode 16 (або новішою версією)
- Цільовий пристрій iOS 18 (або новіший) з мінімум 8 ГБ оперативної пам’яті (iPhone або iPad, сумісний з вимогами Apple Intelligence, оскільки вони схожі на вимоги до квантизованих моделей Phi)
- базові знання Swift та SwiftUI

## Крок 1: Створення нового iOS-проєкту

Почніть зі створення нового iOS-проєкту в Xcode:

1. Запустіть Xcode і виберіть «Create a new Xcode project»
2. Оберіть шаблон «App»
3. Назвіть свій проєкт (наприклад, «Phi3-iOS-App») і виберіть SwiftUI як інтерфейс
4. Вкажіть місце для збереження проєкту

## Крок 2: Додайте необхідні залежності

Додайте пакет [MLX Examples](https://github.com/ml-explore/mlx-swift-examples), який містить усі потрібні залежності та допоміжні засоби для попереднього завантаження моделей і виконання інференсу:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Хоча базового [MLX Swift пакету](https://github.com/ml-explore/mlx-swift) достатньо для основних операцій з тензорами та базового функціоналу ML, пакет MLX Examples надає додаткові компоненти, розроблені для роботи з мовними моделями та спрощення процесу інференсу:

- утиліти для завантаження моделей з Hugging Face
- інтеграція токенізатора
- допоміжні функції для генерації тексту
- попередньо налаштовані визначення моделей

## Крок 3: Налаштування Entitlements

Щоб дозволити додатку завантажувати моделі та виділяти достатньо пам’яті, потрібно додати відповідні entitlements. Створіть файл `.entitlements` для вашого додатку з таким вмістом:

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

> **Note:** Entitlement `com.apple.developer.kernel.increased-memory-limit` важливий для запуску більших моделей, оскільки дозволяє додатку запитувати більше пам’яті, ніж зазвичай дозволено.

## Крок 4: Створення моделі повідомлення чату

Спочатку створимо базову структуру для представлення повідомлень у чаті:

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

## Крок 5: Реалізація ViewModel

Далі створимо клас `PhiViewModel`, який відповідає за завантаження моделі та інференс:

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

ViewModel демонструє основні точки інтеграції з MLX:

- встановлення обмежень кешу GPU за допомогою `MLX.GPU.set(cacheLimit:)` для оптимізації використання пам’яті на мобільних пристроях
- використання `LLMModelFactory` для завантаження моделі за потребою та ініціалізації оптимізованої MLX-моделі
- доступ до параметрів і структури моделі через `ModelContainer`
- використання покрокової генерації токенів MLX через метод `MLXLMCommon.generate`
- керування процесом інференсу з відповідними налаштуваннями температури та лімітами токенів

Потокова генерація токенів забезпечує миттєвий зворотний зв’язок користувачам під час генерації тексту моделлю. Це схоже на роботу серверних моделей, які передають токени користувачу в режимі реального часу, але без затримок, пов’язаних із мережею.

Щодо взаємодії з UI, дві ключові функції — це `loadModel()`, яка ініціалізує LLM, та `fetchAIResponse()`, яка обробляє введення користувача і генерує відповіді ШІ.

### Особливості формату моделі

> **Important:** Моделі Phi для MLX не можна використовувати у їхньому стандартному або GGUF форматі. Їх потрібно конвертувати у формат MLX, що виконує спільнота MLX. Ви можете знайти попередньо конвертовані моделі на [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Пакет MLX Examples містить попередньо налаштовані реєстрації для кількох моделей, включно з Phi-3. Коли ви викликаєте `ModelRegistry.phi3_5_4bit`, це посилається на конкретну попередньо конвертовану MLX-модель, яка буде автоматично завантажена:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Ви можете створити власні конфігурації моделей, щоб вказати будь-яку сумісну модель на Hugging Face. Наприклад, щоб використати Phi-4 mini, можна визначити власну конфігурацію:

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

> **Note:** Підтримка Phi-4 була додана до репозиторію MLX Swift Examples наприкінці лютого 2025 року (у [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Станом на березень 2025 року останній офіційний реліз (2.21.2 від грудня 2024) не містить вбудованої підтримки Phi-4. Щоб використовувати моделі Phi-4, потрібно посилатися на пакет безпосередньо з main гілки:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Це дає доступ до останніх конфігурацій моделей, включно з Phi-4, до їхнього включення в офіційний реліз. Ви можете використовувати цей підхід для роботи з різними версіями моделей Phi або іншими моделями, конвертованими у формат MLX.

## Крок 6: Створення UI

Тепер реалізуємо простий чат-інтерфейс для взаємодії з нашим ViewModel:

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

Інтерфейс складається з трьох основних компонентів, які разом створюють базовий чат. `ContentView` створює інтерфейс з двома станами, який показує або кнопку завантаження, або чат залежно від готовності моделі. `MessageView` відображає окремі повідомлення чату по-різному, залежно від того, чи це повідомлення користувача (вирівняне праворуч, синій фон), чи відповіді моделі Phi (вирівняне ліворуч, сірий фон). `TypingIndicatorView` надає простий анімований індикатор, що показує, що ШІ обробляє запит.

## Крок 7: Збірка та запуск додатку

Тепер ми готові зібрати та запустити додаток.

> **Important!** MLX не підтримує симулятор. Додаток потрібно запускати на фізичному пристрої з чипом Apple Silicon. Детальніше дивіться [тут](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Після запуску додатку натисніть кнопку «Load model», щоб завантажити та ініціалізувати модель Phi-3 (або, залежно від конфігурації, Phi-4). Цей процес може зайняти деякий час залежно від швидкості інтернет-з’єднання, оскільки модель завантажується з Hugging Face. У нашій реалізації є лише індикатор завантаження, але фактичний прогрес можна побачити в консолі Xcode.

Після завантаження ви можете взаємодіяти з моделлю, вводячи запитання у текстове поле та натискаючи кнопку відправки.

Ось як має працювати наш додаток на iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Висновок

Ось і все! Дотримуючись цих кроків, ви створили iOS-додаток, який запускає модель Phi-3 (або Phi-4) безпосередньо на пристрої за допомогою фреймворку Apple MLX.

Вітаємо!

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.