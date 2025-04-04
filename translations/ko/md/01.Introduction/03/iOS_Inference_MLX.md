<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07ca611437b569633d7aacf855ecaa7e",
  "translation_date": "2025-04-04T05:56:23+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference_MLX.md",
  "language_code": "ko"
}
-->
# iOS에서 Apple MLX 프레임워크를 사용하여 Phi-3 및 Phi-4 실행하기

이 튜토리얼에서는 Apple MLX 프레임워크를 사용하여 Phi-3 또는 Phi-4 모델을 디바이스에서 실행하는 iOS 애플리케이션을 만드는 방법을 보여줍니다. [MLX](https://opensource.apple.com/projects/mlx/)는 Apple Silicon 칩에 최적화된 Apple의 머신 러닝 프레임워크입니다.

## 사전 준비

- Xcode 16 이상이 설치된 macOS
- iOS 18 이상을 지원하는 디바이스 (8GB 이상의 메모리를 가진 iPhone 또는 iPad, Apple Intelligence 요구 사항을 충족하는 디바이스. 이는 양자화된 Phi 요구 사항과 유사할 것입니다.)
- Swift 및 SwiftUI에 대한 기본 지식

## 1단계: 새로운 iOS 프로젝트 생성

Xcode에서 새로운 iOS 프로젝트를 생성하세요:

1. Xcode를 실행하고 "새로운 Xcode 프로젝트 생성"을 선택합니다.
2. 템플릿으로 "앱(App)"을 선택합니다.
3. 프로젝트 이름을 지정합니다(예: "Phi3-iOS-App") 그리고 SwiftUI를 인터페이스로 선택합니다.
4. 프로젝트를 저장할 위치를 선택합니다.

## 2단계: 필수 종속성 추가

모델 사전 로드 및 추론을 수행하는 데 필요한 모든 종속성과 헬퍼를 포함하는 [MLX Examples 패키지](https://github.com/ml-explore/mlx-swift-examples)를 추가하세요:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

기본 [MLX Swift 패키지](https://github.com/ml-explore/mlx-swift)만으로도 핵심 텐서 작업 및 기본 ML 기능은 충분하지만, MLX Examples 패키지는 언어 모델 작업 및 추론 과정을 간소화하기 위해 설계된 추가 구성 요소를 제공합니다:

- Hugging Face에서 다운로드를 처리하는 모델 로딩 유틸리티
- 토크나이저 통합
- 텍스트 생성용 추론 헬퍼
- 사전 구성된 모델 정의

## 3단계: 권한 설정 구성

앱이 모델을 다운로드하고 충분한 메모리를 할당할 수 있도록 특정 권한을 추가해야 합니다. 앱에 `.entitlements` 파일을 생성하고 다음 내용을 추가하세요:

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

> **참고:** `com.apple.developer.kernel.increased-memory-limit` 권한은 더 큰 모델을 실행하기 위해 중요합니다. 이 권한은 앱이 일반적으로 허용되는 메모리보다 더 많은 메모리를 요청할 수 있도록 합니다.

## 4단계: 채팅 메시지 모델 생성

먼저 채팅 메시지를 표현하는 기본 구조를 만듭니다:

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

## 5단계: ViewModel 구현

다음으로, 모델 로딩 및 추론을 처리하는 `PhiViewModel` 클래스를 생성합니다:

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

ViewModel은 MLX 통합의 주요 지점을 보여줍니다:

- `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`을 사용하여 특정 MLX 모델을 참조합니다. 이 모델은 자동으로 다운로드됩니다:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Hugging Face에서 호환 가능한 모델을 가리키는 자체 모델 구성을 생성할 수도 있습니다. 예를 들어, Phi-4 mini를 사용하려면 다음과 같이 구성할 수 있습니다:

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

> **참고:** Phi-4 지원은 2025년 2월 말 [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)에서 MLX Swift Examples 리포지토리에 추가되었습니다. 2025년 3월 현재, 최신 공식 릴리스(2024년 12월의 2.21.2 버전)에는 Phi-4 지원이 포함되어 있지 않습니다. Phi-4 모델을 사용하려면 메인 브랜치에서 직접 패키지를 참조해야 합니다:
>
> ```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

이 방법을 사용하면 공식 릴리스에 포함되기 전에 Phi-4를 포함한 최신 모델 구성을 사용할 수 있습니다. 이 접근법을 사용하여 다른 버전의 Phi 모델 또는 MLX 형식으로 변환된 다른 모델도 사용할 수 있습니다.

## 6단계: UI 생성

이제 ViewModel과 상호작용하기 위한 간단한 채팅 인터페이스를 구현해 봅시다:

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

UI는 세 가지 주요 구성 요소로 이루어져 있으며, 이들이 함께 작동하여 기본 채팅 인터페이스를 만듭니다. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView`는 AI가 처리 중임을 보여주는 간단한 애니메이션 인디케이터를 제공합니다.

## 7단계: 앱 빌드 및 실행

이제 애플리케이션을 빌드하고 실행할 준비가 되었습니다.

> **중요!** MLX는 시뮬레이터를 지원하지 않습니다. 반드시 Apple Silicon 칩이 장착된 실제 디바이스에서 앱을 실행해야 합니다. 자세한 내용은 [여기](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)를 참조하세요.

앱이 실행되면 "Load model" 버튼을 눌러 Phi-3(또는 구성에 따라 Phi-4) 모델을 다운로드하고 초기화합니다. 이 과정은 인터넷 연결 속도에 따라 시간이 걸릴 수 있습니다. 이는 Hugging Face에서 모델을 다운로드하기 때문입니다. 구현에는 로딩을 표시하는 스피너만 포함되어 있지만, 실제 진행 상황은 Xcode 콘솔에서 확인할 수 있습니다.

모델이 로드되면 텍스트 필드에 질문을 입력하고 전송 버튼을 눌러 모델과 상호작용할 수 있습니다.

다음은 iPad Air M1에서 실행 중인 애플리케이션의 모습입니다:

![데모 GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## 결론

이제 끝났습니다! 이 단계를 따라 Apple의 MLX 프레임워크를 사용하여 Phi-3(또는 Phi-4) 모델을 디바이스에서 직접 실행하는 iOS 애플리케이션을 만들었습니다.

축하합니다!

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역은 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서가 원어로 작성된 경우, 이를 권위 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.