# Запуск Phi-3 и Phi-4 на iOS с использованием Apple MLX Framework

В этом руководстве показано, как создать iOS-приложение, которое запускает модель Phi-3 или Phi-4 непосредственно на устройстве с помощью фреймворка Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) — это машинное обучение от Apple, оптимизированное для чипов Apple Silicon.

## Требования

- macOS с Xcode 16 (или новее)
- Целевое устройство с iOS 18 (или новее) и минимум 8 ГБ оперативной памяти (iPhone или iPad, совместимые с требованиями Apple Intelligence, так как они схожи с требованиями к квантизированным моделям Phi)
- базовые знания Swift и SwiftUI

## Шаг 1: Создайте новый iOS-проект

Начните с создания нового iOS-проекта в Xcode:

1. запустите Xcode и выберите «Create a new Xcode project»
2. выберите шаблон «App»
3. задайте имя проекта (например, «Phi3-iOS-App») и выберите SwiftUI в качестве интерфейса
4. выберите папку для сохранения проекта

## Шаг 2: Добавьте необходимые зависимости

Добавьте пакет [MLX Examples](https://github.com/ml-explore/mlx-swift-examples), который содержит все нужные зависимости и вспомогательные инструменты для предварительной загрузки моделей и выполнения инференса:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Хотя базового [MLX Swift пакета](https://github.com/ml-explore/mlx-swift) достаточно для основных операций с тензорами и базового ML-функционала, пакет MLX Examples предоставляет дополнительные компоненты, специально разработанные для работы с языковыми моделями и упрощающие процесс инференса:

- утилиты для загрузки моделей с Hugging Face
- интеграция токенизатора
- помощники для генерации текста
- преднастроенные определения моделей

## Шаг 3: Настройте права доступа (Entitlements)

Чтобы разрешить приложению загружать модели и выделять достаточный объём памяти, нужно добавить специальные права доступа. Создайте файл `.entitlements` для вашего приложения со следующим содержимым:

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

> **Note:** Права `com.apple.developer.kernel.increased-memory-limit` важны для запуска больших моделей, так как позволяют приложению запрашивать больше памяти, чем обычно разрешено.

## Шаг 4: Создайте модель сообщения чата

Сначала создадим простую структуру для представления сообщений в чате:

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

## Шаг 5: Реализуйте ViewModel

Далее создадим класс `PhiViewModel`, который будет отвечать за загрузку модели и инференс:

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

В этом ViewModel показаны ключевые моменты интеграции с MLX:

- установка лимитов кеша GPU с помощью `MLX.GPU.set(cacheLimit:)` для оптимизации использования памяти на мобильных устройствах
- использование `LLMModelFactory` для загрузки модели по требованию и инициализации оптимизированной модели MLX
- доступ к параметрам и структуре модели через `ModelContainer`
- использование по-токенной генерации MLX через метод `MLXLMCommon.generate`
- управление процессом инференса с настройками температуры и лимитами токенов

Подход с потоковой генерацией токенов обеспечивает мгновенную обратную связь пользователю по мере генерации текста моделью. Это похоже на работу серверных моделей, которые отправляют токены пользователю по мере их генерации, но без задержек, связанных с сетевыми запросами.

С точки зрения взаимодействия с UI, две ключевые функции — это `loadModel()`, которая инициализирует LLM, и `fetchAIResponse()`, которая обрабатывает ввод пользователя и генерирует ответ ИИ.

### Особенности формата модели

> **Important:** Модели Phi для MLX нельзя использовать в их стандартном или GGUF формате. Их нужно конвертировать в формат MLX, что выполняет сообщество MLX. Предварительно конвертированные модели можно найти на [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Пакет MLX Examples включает преднастроенные регистрации для нескольких моделей, включая Phi-3. При вызове `ModelRegistry.phi3_5_4bit` используется конкретная предварительно конвертированная MLX-модель, которая будет загружена автоматически:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Вы можете создать собственные конфигурации моделей, указывая на любую совместимую модель на Hugging Face. Например, чтобы использовать Phi-4 mini, можно определить свою конфигурацию:

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

> **Note:** Поддержка Phi-4 была добавлена в репозиторий MLX Swift Examples в конце февраля 2025 года (в [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). На март 2025 года последняя официальная версия (2.21.2 от декабря 2024) не включает встроенную поддержку Phi-4. Чтобы использовать модели Phi-4, нужно подключать пакет напрямую из основной ветки:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Это даёт доступ к последним конфигурациям моделей, включая Phi-4, до их включения в официальный релиз. Такой подход позволяет использовать разные версии моделей Phi или даже другие модели, конвертированные в формат MLX.

## Шаг 6: Создайте UI

Теперь реализуем простой интерфейс чата для взаимодействия с нашим ViewModel:

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

UI состоит из трёх основных компонентов, которые вместе создают базовый чат. `ContentView` создаёт интерфейс с двумя состояниями — либо кнопка загрузки, либо сам чат, в зависимости от готовности модели. `MessageView` отображает отдельные сообщения по-разному: сообщения пользователя выравниваются вправо с синим фоном, а ответы модели Phi — влево с серым фоном. `TypingIndicatorView` показывает простую анимацию, сигнализирующую, что ИИ обрабатывает запрос.

## Шаг 7: Сборка и запуск приложения

Теперь можно собрать и запустить приложение.

> **Important!** MLX не поддерживает симулятор. Приложение нужно запускать на реальном устройстве с чипом Apple Silicon. Подробнее см. [здесь](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

При запуске приложения нажмите кнопку «Load model», чтобы скачать и инициализировать модель Phi-3 (или, в зависимости от конфигурации, Phi-4). Этот процесс может занять некоторое время в зависимости от скорости интернета, так как модель загружается с Hugging Face. В нашей реализации отображается только индикатор загрузки, но реальный прогресс можно увидеть в консоли Xcode.

После загрузки вы можете взаимодействовать с моделью, вводя вопросы в текстовое поле и нажимая кнопку отправки.

Вот как должно работать наше приложение на iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Заключение

Вот и всё! Следуя этим шагам, вы создали iOS-приложение, которое запускает модель Phi-3 (или Phi-4) прямо на устройстве с помощью фреймворка Apple MLX.

Поздравляем!

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.