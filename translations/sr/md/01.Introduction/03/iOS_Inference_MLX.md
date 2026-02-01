# Покретање Phi-3 и Phi-4 на iOS-у уз Apple MLX Framework

Овај туторијал показује како направити iOS апликацију која покреће Phi-3 или Phi-4 модел директно на уређају, користећи Apple MLX framework. [MLX](https://opensource.apple.com/projects/mlx/) је Apple-ов машински учењски фрејмворк оптимизован за Apple Silicon чипове.

## Захтеви

- macOS са Xcode 16 (или новијим)
- iOS 18 (или новији) уређај са најмање 8GB RAM-а (iPhone или iPad компатибилан са Apple Intelligence захтевима, који су слични захтевима за квантоване Phi моделе)
- основно познавање Swift и SwiftUI

## Корак 1: Креирање новог iOS пројекта

Почните креирањем новог iOS пројекта у Xcode-у:

1. покрените Xcode и изаберите „Create a new Xcode project“
2. изаберите „App“ као шаблон
3. именујте пројекат (нпр. „Phi3-iOS-App“) и изаберите SwiftUI као интерфејс
4. изаберите локацију за чување пројекта

## Корак 2: Додавање потребних зависности

Додајте [MLX Examples пакет](https://github.com/ml-explore/mlx-swift-examples) који садржи све неопходне зависности и помоћне алате за претходно учитавање модела и извођење инференце:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Иако би основни [MLX Swift пакет](https://github.com/ml-explore/mlx-swift) био довољан за основне тензорске операције и базичну ML функционалност, MLX Examples пакет пружа додатне компоненте дизајниране за рад са језичким моделима и олакшавање процеса инференце:

- алате за учитавање модела који подржавају преузимање са Hugging Face
- интеграцију токенизатора
- помоћне функције за генерисање текста
- унапред конфигурисане дефиниције модела

## Корак 3: Конфигурисање дозвола (entitlements)

Да бисмо апликацији омогућили преузимање модела и доделу довољно меморије, потребно је додати одређене дозволе. Креирајте `.entitlements` фајл за вашу апликацију са следећим садржајем:

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

> **Note:** Дозвола `com.apple.developer.kernel.increased-memory-limit` је важна за покретање већих модела, јер апликацији омогућава да затражи више меморије него што је уобичајено дозвољено.

## Корак 4: Креирање модела поруке у ћаскању

Прво, направимо основну структуру која представља поруке у ћаскању:

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

## Корак 5: Имплементација ViewModel-а

Затим ћемо направити класу `PhiViewModel` која управља учитавањем модела и инференцом:

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

ViewModel илуструје кључне тачке интеграције са MLX-ом:

- подешавање ограничења кеша на GPU-у помоћу `MLX.GPU.set(cacheLimit:)` ради оптимизације коришћења меморије на мобилним уређајима
- коришћење `LLMModelFactory` за преузимање модела по потреби и иницијализацију MLX-оптимизованог модела
- приступ параметрима и структури модела преко `ModelContainer`
- коришћење MLX-ове генерације токен по токен кроз `MLXLMCommon.generate` метод
- управљање процесом инференце са одговарајућим подешавањима температуре и ограничењима броја токена

Приступ стримовања токена пружа корисницима тренутну повратну информацију док модел генерише текст. Ово је слично раду сервера који шаље токене кориснику у реалном времену, али без кашњења услед мрежних захтева.

Што се тиче корисничког интерфејса, две кључне функције су `loadModel()`, која иницијализује LLM, и `fetchAIResponse()`, која обрађује унос корисника и генерише одговоре вештачке интелигенције.

### Разматрања о формату модела

> **Important:** Phi модели за MLX не могу се користити у свом подразумеваном или GGUF формату. Морају бити конвертовани у MLX формат, што обавља MLX заједница. Пре-конвертоване моделе можете пронаћи на [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

MLX Examples пакет укључује унапред конфигурисане регистрације за неколико модела, укључујући Phi-3. Када позовете `ModelRegistry.phi3_5_4bit`, он референцира одређени пре-конвертовани MLX модел који ће бити аутоматски преузет:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Можете направити своје конфигурације модела које показују на било који компатибилан модел на Hugging Face-у. На пример, да бисте користили Phi-4 mini, можете дефинисати своју конфигурацију:

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

> **Note:** Подршка за Phi-4 додата је у MLX Swift Examples репозиторијум крајем фебруара 2025. (у [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Од марта 2025, најновије званично издање (2.21.2 из децембра 2024) не укључује уграђену подршку за Phi-4. Да бисте користили Phi-4 моделе, потребно је да пакет референцирате директно са главне гране:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Ово вам омогућава приступ најновијим конфигурацијама модела, укључујући Phi-4, пре него што буду укључене у званично издање. Овим приступом можете користити различите верзије Phi модела или чак друге моделе који су конвертовани у MLX формат.

## Корак 6: Креирање корисничког интерфејса

Сада ћемо имплементирати једноставан интерфејс за ћаскање који комуницира са нашим view model-ом:

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

Кориснички интерфејс се састоји из три главне компоненте које заједно праве основни интерфејс за ћаскање. `ContentView` креира интерфејс са два стања који приказује или дугме за учитавање или интерфејс за ћаскање у зависности од спремности модела. `MessageView` приказује појединачне поруке у ћаскању различито у зависности од тога да ли су поруке корисника (постављене десно, са плавом позадином) или одговори Phi модела (постављени лево, са сивом позадином). `TypingIndicatorView` пружа једноставан анимирани индикатор који показује да AI обрађује унос.

## Корак 7: Компилација и покретање апликације

Сада смо спремни да компајлирамо и покренемо апликацију.

> **Important!** MLX не подржава симулатор. Апликацију морате покренути на физичком уређају са Apple Silicon чипом. Више информација потражите [овде](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

Када апликација крене, додирните дугме „Load model“ да бисте преузели и иницијализовали Phi-3 (или, у зависности од конфигурације, Phi-4) модел. Овај процес може потрајати у зависности од ваше интернет везе, јер укључује преузимање модела са Hugging Face-а. Наша имплементација укључује само индикатор учитавања, али стварни напредак можете пратити у Xcode конзоли.

Када се модел учита, можете комуницирати са њим тако што ћете уносити питања у текстуално поље и притиснути дугме за слање.

Ево како наша апликација треба да функционише на iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Закључак

И то је то! Пратећи ове кораке, направили сте iOS апликацију која покреће Phi-3 (или Phi-4) модел директно на уређају користећи Apple MLX framework.

Честитамо!

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.