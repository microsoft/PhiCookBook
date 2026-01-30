# iOSでApple MLXフレームワークを使ってPhi-3およびPhi-4を実行する

このチュートリアルでは、AppleのMLXフレームワークを使って、Phi-3またはPhi-4モデルをiOSデバイス上で動作させるアプリケーションの作成方法を説明します。[MLX](https://opensource.apple.com/projects/mlx/)はApple Siliconチップに最適化されたAppleの機械学習フレームワークです。

## 前提条件

- macOSとXcode 16（またはそれ以上）
- iOS 18（またはそれ以上）対応デバイスで、8GB以上のメモリ（Apple Intelligence要件に対応したiPhoneまたはiPad。これは量子化されたPhiの要件に近いものです）
- SwiftおよびSwiftUIの基本知識

## ステップ1: 新しいiOSプロジェクトを作成する

まずはXcodeで新しいiOSプロジェクトを作成します：

1. Xcodeを起動し、「Create a new Xcode project」を選択
2. テンプレートとして「App」を選択
3. プロジェクト名を入力（例: "Phi3-iOS-App"）し、インターフェースはSwiftUIを選択
4. プロジェクトの保存場所を選択

## ステップ2: 必要な依存関係を追加する

モデルの事前読み込みや推論に必要な依存関係やヘルパーが含まれている[MLX Examplesパッケージ](https://github.com/ml-explore/mlx-swift-examples)を追加します：

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

基本的なテンソル操作や機械学習機能には[MLX Swiftパッケージ](https://github.com/ml-explore/mlx-swift)だけでも十分ですが、MLX Examplesパッケージは言語モデルの扱いを簡単にするための追加コンポーネントを提供しています：

- Hugging Faceからのモデルダウンロードを扱うユーティリティ
- トークナイザーの統合
- テキスト生成のための推論ヘルパー
- 事前設定されたモデル定義

## ステップ3: エンタイトルメントの設定

アプリがモデルをダウンロードし、十分なメモリを確保できるように、特定のエンタイトルメントを追加する必要があります。アプリ用に以下の内容の`.entitlements`ファイルを作成してください：

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

> **注意:** `com.apple.developer.kernel.increased-memory-limit`エンタイトルメントは、大きなモデルを実行する際に重要です。これにより、通常より多くのメモリをアプリが要求できるようになります。

## ステップ4: チャットメッセージモデルを作成する

まずはチャットメッセージを表す基本的な構造体を作成しましょう：

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

## ステップ5: ViewModelを実装する

次に、モデルの読み込みと推論を担当する`PhiViewModel`クラスを作成します：

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

このViewModelはMLXとの主要な連携ポイントを示しています：

- `MLX.GPU.set(cacheLimit:)`でGPUキャッシュの上限を設定し、モバイルデバイスでのメモリ使用を最適化
- `LLMModelFactory`を使ってモデルをオンデマンドでダウンロードし、MLX最適化モデルを初期化
- `ModelContainer`を通じてモデルのパラメータや構造にアクセス
- `MLXLMCommon.generate`メソッドを利用したトークン単位の生成
- 適切な温度設定やトークン制限で推論プロセスを管理

ストリーミングトークン生成は、モデルがテキストを生成する際に即座にユーザーにフィードバックを返します。これはサーバーベースのモデルがトークンをストリーム配信する動作に似ていますが、ネットワーク遅延がありません。

UIとの連携では、LLMを初期化する`loadModel()`と、ユーザー入力を処理してAI応答を生成する`fetchAIResponse()`の2つの関数が重要です。

### モデルフォーマットに関する注意点

> **重要:** MLX用のPhiモデルはデフォルトやGGUFフォーマットのままでは使用できません。MLXフォーマットに変換する必要があり、これはMLXコミュニティによって行われています。事前変換済みモデルは[huggingface.co/mlx-community](https://huggingface.co/mlx-community)で入手可能です。

MLX ExamplesパッケージにはPhi-3を含むいくつかのモデルの事前設定登録が含まれています。`ModelRegistry.phi3_5_4bit`を呼び出すと、特定の事前変換済みMLXモデルが自動的にダウンロードされます：

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

独自にモデル設定を作成して、Hugging Face上の互換モデルを指定することも可能です。例えばPhi-4 miniを使いたい場合は、以下のように設定できます：

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

> **注意:** Phi-4のサポートは2025年2月末にMLX Swift Examplesリポジトリに追加されました（[PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)）。2025年3月時点での最新公式リリース（2024年12月の2.21.2）にはPhi-4の組み込みサポートは含まれていません。Phi-4モデルを使うには、メインブランチから直接パッケージを参照する必要があります：
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

これにより、公式リリースに含まれる前の最新モデル設定（Phi-4を含む）にアクセスできます。この方法で、異なるバージョンのPhiモデルやMLXフォーマットに変換された他のモデルも利用可能です。

## ステップ6: UIを作成する

次に、ViewModelと連携するシンプルなチャットインターフェースを実装します：

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

UIは3つの主要コンポーネントで構成され、基本的なチャットインターフェースを作ります。`ContentView`はモデルの準備状況に応じて読み込みボタンかチャット画面を表示します。`MessageView`はユーザーメッセージ（右寄せ、青背景）とPhiモデルの応答（左寄せ、グレー背景）を区別して表示します。`TypingIndicatorView`はAIが処理中であることを示すシンプルなアニメーションインジケーターです。

## ステップ7: アプリのビルドと実行

これでアプリのビルドと実行の準備が整いました。

> **重要!** MLXはシミュレーターをサポートしていません。Apple Siliconチップ搭載の実機で実行する必要があります。詳細は[こちら](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)を参照してください。

アプリ起動後、「Load model」ボタンをタップしてPhi-3（または設定に応じてPhi-4）モデルをダウンロードし初期化します。これはHugging Faceからモデルをダウンロードするため、インターネット接続状況によって時間がかかる場合があります。実装では読み込み中を示すスピナーのみですが、Xcodeのコンソールで実際の進捗を確認できます。

読み込みが完了したら、テキストフィールドに質問を入力し、送信ボタンをタップしてモデルと対話できます。

iPad Air M1上で動作しているアプリの様子は以下の通りです：

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## まとめ

以上で、AppleのMLXフレームワークを使ってPhi-3（またはPhi-4）モデルをiOSデバイス上で直接動作させるアプリケーションを作成できました。

おめでとうございます！

**免責事項**：  

本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
