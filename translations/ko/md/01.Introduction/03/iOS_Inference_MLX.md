# iOS에서 Apple MLX 프레임워크로 Phi-3 및 Phi-4 실행하기

이 튜토리얼에서는 Apple MLX 프레임워크를 사용해 Phi-3 또는 Phi-4 모델을 iOS 기기에서 직접 실행하는 iOS 애플리케이션을 만드는 방법을 설명합니다. [MLX](https://opensource.apple.com/projects/mlx/)는 Apple Silicon 칩에 최적화된 Apple의 머신러닝 프레임워크입니다.

## 사전 준비 사항

- Xcode 16 이상이 설치된 macOS
- iOS 18 이상이 탑재된 최소 8GB 메모리의 대상 기기 (Apple Intelligence 요구사항을 충족하는 iPhone 또는 iPad, 이는 양자화된 Phi 요구사항과 유사합니다)
- Swift 및 SwiftUI 기본 지식

## 1단계: 새 iOS 프로젝트 생성

Xcode에서 새 iOS 프로젝트를 생성합니다:

1. Xcode를 실행하고 "Create a new Xcode project"를 선택합니다.
2. 템플릿으로 "App"을 선택합니다.
3. 프로젝트 이름을 지정합니다(예: "Phi3-iOS-App") 그리고 인터페이스로 SwiftUI를 선택합니다.
4. 프로젝트를 저장할 위치를 선택합니다.

## 2단계: 필요한 의존성 추가

모델 사전 로드 및 추론에 필요한 모든 의존성과 헬퍼가 포함된 [MLX Examples 패키지](https://github.com/ml-explore/mlx-swift-examples)를 추가합니다:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

기본 [MLX Swift 패키지](https://github.com/ml-explore/mlx-swift)는 핵심 텐서 연산과 기본 ML 기능에 충분하지만, MLX Examples 패키지는 언어 모델 작업과 추론 과정을 더 쉽게 하기 위한 여러 추가 컴포넌트를 제공합니다:

- Hugging Face에서 모델 다운로드를 처리하는 모델 로딩 유틸리티
- 토크나이저 통합
- 텍스트 생성용 추론 헬퍼
- 사전 구성된 모델 정의

## 3단계: 권한 설정 구성

앱이 모델을 다운로드하고 충분한 메모리를 할당할 수 있도록 특정 권한을 추가해야 합니다. 앱용 `.entitlements` 파일을 생성하고 다음 내용을 포함하세요:

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` 권한은 더 큰 모델을 실행할 때 중요합니다. 이 권한이 있어야 앱이 일반적으로 허용되는 메모리보다 더 많은 메모리를 요청할 수 있습니다.

## 4단계: 채팅 메시지 모델 생성

먼저, 채팅 메시지를 나타내는 기본 구조체를 만듭니다:

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

다음으로, 모델 로딩과 추론을 담당하는 `PhiViewModel` 클래스를 만듭니다:

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

ViewModel은 MLX 통합의 주요 포인트를 보여줍니다:

- `MLX.GPU.set(cacheLimit:)`를 사용해 모바일 기기에서 메모리 사용을 최적화하기 위한 GPU 캐시 제한 설정
- `LLMModelFactory`를 통해 필요 시 모델을 다운로드하고 MLX 최적화 모델 초기화
- `ModelContainer`를 통해 모델의 파라미터와 구조 접근
- MLX의 토큰 단위 생성 기능인 `MLXLMCommon.generate` 활용
- 적절한 온도 설정과 토큰 제한으로 추론 과정 관리

스트리밍 토큰 생성 방식은 모델이 텍스트를 생성하는 즉시 사용자에게 피드백을 제공합니다. 이는 서버 기반 모델이 네트워크 지연 없이 토큰을 스트리밍하는 방식과 유사합니다.

UI 상호작용 측면에서 핵심 함수는 LLM을 초기화하는 `loadModel()`과 사용자 입력을 처리해 AI 응답을 생성하는 `fetchAIResponse()`입니다.

### 모델 포맷 관련 사항

> **Important:** MLX용 Phi 모델은 기본 포맷이나 GGUF 포맷으로 사용할 수 없습니다. MLX 커뮤니티에서 처리하는 MLX 포맷으로 변환되어야 합니다. 사전 변환된 모델은 [huggingface.co/mlx-community](https://huggingface.co/mlx-community)에서 찾을 수 있습니다.

MLX Examples 패키지에는 Phi-3를 포함한 여러 모델에 대한 사전 구성된 등록이 포함되어 있습니다. `ModelRegistry.phi3_5_4bit`를 호출하면 자동으로 다운로드되는 특정 사전 변환 MLX 모델을 참조합니다:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

원하는 경우 Hugging Face의 호환 가능한 모델을 가리키도록 직접 모델 구성을 만들 수도 있습니다. 예를 들어 Phi-4 mini를 사용하려면 다음과 같이 구성할 수 있습니다:

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

> **Note:** Phi-4 지원은 2025년 2월 말에 MLX Swift Examples 저장소에 추가되었습니다 ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). 2025년 3월 기준, 2024년 12월의 최신 공식 릴리스(2.21.2)에는 Phi-4 지원이 포함되어 있지 않습니다. Phi-4 모델을 사용하려면 메인 브랜치에서 직접 패키지를 참조해야 합니다:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

이 방법을 통해 공식 릴리스에 포함되기 전 최신 모델 구성(예: Phi-4)을 사용할 수 있습니다. 이를 활용해 다양한 버전의 Phi 모델이나 MLX 포맷으로 변환된 다른 모델도 사용할 수 있습니다.

## 6단계: UI 생성

이제 ViewModel과 상호작용할 간단한 채팅 인터페이스를 구현해봅시다:

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

UI는 세 가지 주요 컴포넌트로 구성되어 기본 채팅 인터페이스를 만듭니다. `ContentView`는 모델 준비 상태에 따라 로딩 버튼 또는 채팅 인터페이스를 보여주는 두 상태 인터페이스를 생성합니다. `MessageView`는 사용자 메시지(오른쪽 정렬, 파란색 배경)와 Phi 모델 응답(왼쪽 정렬, 회색 배경)을 다르게 렌더링합니다. `TypingIndicatorView`는 AI가 처리 중임을 보여주는 간단한 애니메이션 표시기입니다.

## 7단계: 앱 빌드 및 실행

이제 애플리케이션을 빌드하고 실행할 준비가 되었습니다.

> **Important!** MLX는 시뮬레이터를 지원하지 않습니다. Apple Silicon 칩이 탑재된 실제 기기에서 앱을 실행해야 합니다. 자세한 내용은 [여기](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)를 참고하세요.

앱이 실행되면 "Load model" 버튼을 눌러 Phi-3(또는 구성에 따라 Phi-4) 모델을 다운로드하고 초기화합니다. 이 과정은 인터넷 연결 속도에 따라 시간이 걸릴 수 있으며, Hugging Face에서 모델을 다운로드하는 작업이 포함됩니다. 구현에는 로딩 상태를 나타내는 스피너만 포함되어 있지만, 실제 진행 상황은 Xcode 콘솔에서 확인할 수 있습니다.

모델이 로드되면 텍스트 필드에 질문을 입력하고 전송 버튼을 눌러 모델과 상호작용할 수 있습니다.

다음은 iPad Air M1에서 실행 중인 애플리케이션의 동작 모습입니다:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## 결론

이상으로, Apple의 MLX 프레임워크를 사용해 Phi-3(또는 Phi-4) 모델을 기기 내에서 직접 실행하는 iOS 애플리케이션을 만드는 과정을 마쳤습니다.

축하합니다!

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.