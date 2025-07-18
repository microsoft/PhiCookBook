<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:28:11+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "mo"
}
-->
# 在 iOS 上使用 Apple MLX 框架運行 Phi-3 和 Phi-4

本教學示範如何使用 Apple MLX 框架建立一個 iOS 應用程式，在裝置上運行 Phi-3 或 Phi-4 模型。[MLX](https://opensource.apple.com/projects/mlx/) 是 Apple 專為 Apple Silicon 晶片優化的機器學習框架。

## 先決條件

- macOS 與 Xcode 16（或更新版本）
- iOS 18（或更新版本）目標裝置，至少 8GB 記憶體（iPhone 或 iPad，需符合 Apple Intelligence 要求，這與量化後的 Phi 模型需求相似）
- 基本的 Swift 和 SwiftUI 知識

## 第一步：建立新的 iOS 專案

首先在 Xcode 中建立一個新的 iOS 專案：

1. 啟動 Xcode，選擇「Create a new Xcode project」
2. 選擇「App」作為範本
3. 為專案命名（例如「Phi3-iOS-App」），並選擇 SwiftUI 作為介面
4. 選擇專案儲存位置

## 第二步：加入所需的相依套件

加入包含所有必要相依與輔助工具的 [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples)，用於預載模型與執行推論：

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

雖然基礎的 [MLX Swift package](https://github.com/ml-explore/mlx-swift) 已足以支援核心張量運算與基本機器學習功能，但 MLX Examples 套件提供了多個專為語言模型設計的額外元件，讓推論流程更簡便：

- 處理從 Hugging Face 下載模型的工具
- 分詞器整合
- 用於文字生成的推論輔助工具
- 預先配置的模型定義

## 第三步：設定權限

為了讓應用程式能下載模型並分配足夠的記憶體，我們需要新增特定的權限。為你的應用程式建立一個 `.entitlements` 檔案，內容如下：

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

> **Note:** `com.apple.developer.kernel.increased-memory-limit` 權限對於運行較大型模型非常重要，因為它允許應用程式請求比平常更多的記憶體。

## 第四步：建立聊天訊息模型

首先，我們建立一個基本結構來表示聊天訊息：

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

## 第五步：實作 ViewModel

接著，我們建立 `PhiViewModel` 類別，負責模型載入與推論：

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

這個 ViewModel 展示了 MLX 整合的關鍵點：

- 使用 `MLX.GPU.set(cacheLimit:)` 設定 GPU 快取限制，以優化行動裝置的記憶體使用
- 利用 `LLMModelFactory` 按需下載模型並初始化 MLX 優化模型
- 透過 `ModelContainer` 存取模型參數與結構
- 使用 MLX 的逐詞生成方法 `MLXLMCommon.generate`
- 以適當的溫度設定與詞元限制管理推論流程

串流式詞元生成方式能即時回饋使用者，類似伺服器端模型的運作，將詞元串流回使用者，但無需等待網路請求延遲。

在 UI 互動方面，兩個主要函式是 `loadModel()`，用於初始化大型語言模型，以及 `fetchAIResponse()`，用於處理使用者輸入並生成 AI 回應。

### 模型格式注意事項

> **Important:** Phi 模型無法直接使用預設或 GGUF 格式於 MLX。必須轉換成 MLX 格式，這部分由 MLX 社群負責。你可以在 [huggingface.co/mlx-community](https://huggingface.co/mlx-community) 找到已轉換好的模型。

MLX Examples 套件包含多個模型的預配置註冊，包括 Phi-3。當你呼叫 `ModelRegistry.phi3_5_4bit` 時，它會參考一個特定的預轉換 MLX 模型，並自動下載：

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

你也可以自行建立模型配置，指向 Hugging Face 上任何相容的模型。例如，若要使用 Phi-4 mini，可以定義自己的配置：

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

> **Note:** Phi-4 支援於 2025 年 2 月底加入 MLX Swift Examples 倉庫（見 [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)）。截至 2025 年 3 月，最新官方版本（2024 年 12 月的 2.21.2）尚未內建 Phi-4 支援。若要使用 Phi-4 模型，需直接從主分支引用套件：
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

這讓你能在官方版本釋出前，使用包含 Phi-4 的最新模型配置。你也可以用此方法使用不同版本的 Phi 模型，甚至其他已轉換成 MLX 格式的模型。

## 第六步：建立使用者介面

現在來實作一個簡單的聊天介面，與我們的 ViewModel 互動：

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

介面由三個主要元件組成，共同打造基本的聊天體驗。`ContentView` 根據模型是否準備好，顯示載入按鈕或聊天介面。`MessageView` 根據訊息是使用者（靠右、藍底）或 Phi 模型回應（靠左、灰底）分別呈現。`TypingIndicatorView` 則提供簡單的動畫指示，顯示 AI 正在處理中。

## 第七步：建置並執行應用程式

現在準備建置並執行應用程式。

> **Important!** MLX 不支援模擬器。你必須在搭載 Apple Silicon 晶片的實體裝置上執行。詳情請參考 [這裡](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)。

應用程式啟動後，點擊「Load model」按鈕下載並初始化 Phi-3（或依配置為 Phi-4）模型。此過程視網路連線速度可能需要一些時間，因為需從 Hugging Face 下載模型。我們的實作僅有載入指示器，但你可以在 Xcode 主控台看到實際進度。

載入完成後，你可以在文字欄輸入問題，點擊送出按鈕與模型互動。

以下是我們的應用程式在 iPad Air M1 上的運行示範：

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## 結語

就這樣！照著這些步驟，你已成功建立一個使用 Apple MLX 框架，能在裝置上直接運行 Phi-3（或 Phi-4）模型的 iOS 應用程式。

恭喜你！

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。