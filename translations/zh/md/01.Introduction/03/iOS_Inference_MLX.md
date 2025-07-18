<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:27:57+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "zh"
}
-->
# 在 iOS 上使用 Apple MLX 框架运行 Phi-3 和 Phi-4

本教程演示如何使用 Apple MLX 框架创建一个在设备上运行 Phi-3 或 Phi-4 模型的 iOS 应用程序。[MLX](https://opensource.apple.com/projects/mlx/) 是苹果针对 Apple Silicon 芯片优化的机器学习框架。

## 前提条件

- macOS，安装 Xcode 16（或更高版本）
- 运行 iOS 18（或更高版本）的目标设备，至少 8GB 内存（兼容 Apple Intelligence 要求的 iPhone 或 iPad，这些要求与量化后的 Phi 模型类似）
- 具备 Swift 和 SwiftUI 的基础知识

## 第一步：创建新的 iOS 项目

首先在 Xcode 中创建一个新的 iOS 项目：

1. 启动 Xcode，选择“创建新的 Xcode 项目”
2. 选择“App”作为模板
3. 为项目命名（例如 “Phi3-iOS-App”），并选择 SwiftUI 作为界面
4. 选择项目保存位置

## 第二步：添加所需依赖

添加包含预加载模型和推理所需所有依赖和辅助工具的 [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples)：

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

虽然基础的 [MLX Swift package](https://github.com/ml-explore/mlx-swift) 足以支持核心张量操作和基本机器学习功能，但 MLX Examples 包提供了多个专为语言模型设计的额外组件，简化推理流程：

- 处理从 Hugging Face 下载模型的加载工具
- 分词器集成
- 用于文本生成的推理辅助工具
- 预配置的模型定义

## 第三步：配置权限

为了允许应用下载模型并分配足够的内存，我们需要添加特定的权限。为应用创建一个 `.entitlements` 文件，内容如下：

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

> **注意：** `com.apple.developer.kernel.increased-memory-limit` 权限对于运行较大模型非常重要，它允许应用请求比通常限制更多的内存。

## 第四步：创建聊天消息模型

首先，创建一个基本结构体来表示聊天消息：

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

## 第五步：实现 ViewModel

接下来，创建负责模型加载和推理的 `PhiViewModel` 类：

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

该 ViewModel 展示了 MLX 集成的关键点：

- 使用 `MLX.GPU.set(cacheLimit:)` 设置 GPU 缓存限制，优化移动设备上的内存使用
- 通过 `LLMModelFactory` 按需下载模型并初始化 MLX 优化模型
- 通过 `ModelContainer` 访问模型参数和结构
- 利用 MLX 的逐令牌生成方法 `MLXLMCommon.generate`
- 以合适的温度设置和令牌限制管理推理过程

流式令牌生成方式能在模型生成文本时即时反馈给用户，类似服务器端模型的工作方式，但避免了网络请求的延迟。

在 UI 交互方面，两个关键函数是 `loadModel()`，用于初始化 LLM，以及 `fetchAIResponse()`，用于处理用户输入并生成 AI 回复。

### 模型格式注意事项

> **重要：** MLX 不能直接使用默认或 GGUF 格式的 Phi 模型。必须将其转换为 MLX 格式，这由 MLX 社区负责。你可以在 [huggingface.co/mlx-community](https://huggingface.co/mlx-community) 找到预转换的模型。

MLX Examples 包包含多个模型的预配置注册，包括 Phi-3。当你调用 `ModelRegistry.phi3_5_4bit` 时，它会引用一个特定的预转换 MLX 模型，并自动下载：

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

你也可以创建自己的模型配置，指向 Hugging Face 上任何兼容的模型。例如，若想使用 Phi-4 mini，可以定义自己的配置：

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

> **注意：** Phi-4 支持于 2025 年 2 月底加入 MLX Swift Examples 仓库（见 [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)）。截至 2025 年 3 月，最新官方版本（2024 年 12 月发布的 2.21.2）尚未内置 Phi-4 支持。要使用 Phi-4 模型，需要直接从主分支引用该包：
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

这样你就能在官方发布之前使用最新的模型配置，包括 Phi-4。你也可以用此方法使用不同版本的 Phi 模型，甚至其他已转换为 MLX 格式的模型。

## 第六步：创建 UI

现在实现一个简单的聊天界面与 ViewModel 交互：

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

UI 由三个主要组件组成，共同构建基础聊天界面。`ContentView` 创建一个两状态界面，根据模型是否准备好显示加载按钮或聊天界面。`MessageView` 根据消息类型不同，分别以右对齐蓝色背景（用户消息）或左对齐灰色背景（Phi 模型回复）渲染单条消息。`TypingIndicatorView` 提供一个简单的动画指示器，显示 AI 正在处理。

## 第七步：构建并运行应用

现在可以构建并运行应用了。

> **重要！** MLX 不支持模拟器。必须在搭载 Apple Silicon 芯片的真机上运行。详情见 [这里](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)。

应用启动后，点击“Load model”按钮下载并初始化 Phi-3（或根据配置的 Phi-4）模型。此过程可能因网络状况而耗时较长，因为需要从 Hugging Face 下载模型。我们的实现仅显示加载指示器，但你可以在 Xcode 控制台查看实际进度。

加载完成后，你可以在文本框输入问题，点击发送按钮与模型交互。

以下是应用在 iPad Air M1 上运行的效果：

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## 结语

就是这样！按照这些步骤，你已经成功创建了一个使用 Apple MLX 框架，能在设备上直接运行 Phi-3（或 Phi-4）模型的 iOS 应用。

恭喜你！

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。