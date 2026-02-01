# Chạy Phi-3 và Phi-4 trên iOS với Apple MLX Framework

Hướng dẫn này trình bày cách tạo một ứng dụng iOS chạy mô hình Phi-3 hoặc Phi-4 trực tiếp trên thiết bị, sử dụng framework Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) là framework máy học của Apple được tối ưu cho chip Apple Silicon.

## Yêu cầu trước

- macOS với Xcode 16 (hoặc cao hơn)
- Thiết bị mục tiêu iOS 18 (hoặc cao hơn) với ít nhất 8GB RAM (iPhone hoặc iPad tương thích với yêu cầu Apple Intelligence, vì những yêu cầu này tương tự với yêu cầu lượng tử hóa của Phi)
- Kiến thức cơ bản về Swift và SwiftUI

## Bước 1: Tạo dự án iOS mới

Bắt đầu bằng cách tạo một dự án iOS mới trong Xcode:

1. Mở Xcode và chọn "Create a new Xcode project"
2. Chọn mẫu "App"
3. Đặt tên dự án (ví dụ: "Phi3-iOS-App") và chọn SwiftUI làm giao diện
4. Chọn vị trí lưu dự án

## Bước 2: Thêm các phụ thuộc cần thiết

Thêm gói [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) chứa tất cả các phụ thuộc và tiện ích cần thiết để tải trước mô hình và thực hiện suy luận:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Mặc dù gói [MLX Swift package](https://github.com/ml-explore/mlx-swift) cơ bản đã đủ cho các phép toán tensor cốt lõi và chức năng ML cơ bản, gói MLX Examples cung cấp thêm nhiều thành phần hỗ trợ làm việc với các mô hình ngôn ngữ và giúp quá trình suy luận dễ dàng hơn:

- tiện ích tải mô hình từ Hugging Face
- tích hợp tokenizer
- trợ giúp suy luận cho việc tạo văn bản
- định nghĩa mô hình được cấu hình sẵn

## Bước 3: Cấu hình Entitlements

Để cho phép ứng dụng tải mô hình và cấp phát đủ bộ nhớ, chúng ta cần thêm các quyền đặc biệt. Tạo một file `.entitlements` cho ứng dụng với nội dung sau:

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

> **Note:** Quyền `com.apple.developer.kernel.increased-memory-limit` rất quan trọng để chạy các mô hình lớn hơn, vì nó cho phép ứng dụng yêu cầu bộ nhớ nhiều hơn mức bình thường.

## Bước 4: Tạo mô hình tin nhắn chat

Trước tiên, hãy tạo một cấu trúc cơ bản để đại diện cho các tin nhắn chat:

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

## Bước 5: Triển khai ViewModel

Tiếp theo, chúng ta sẽ tạo lớp `PhiViewModel` để xử lý việc tải mô hình và suy luận:

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

ViewModel minh họa các điểm tích hợp chính với MLX:

- thiết lập giới hạn bộ nhớ cache GPU với `MLX.GPU.set(cacheLimit:)` để tối ưu bộ nhớ trên thiết bị di động
- sử dụng `LLMModelFactory` để tải mô hình theo yêu cầu và khởi tạo mô hình tối ưu MLX
- truy cập các tham số và cấu trúc mô hình qua `ModelContainer`
- tận dụng khả năng tạo token từng bước của MLX thông qua phương thức `MLXLMCommon.generate`
- quản lý quá trình suy luận với các thiết lập nhiệt độ và giới hạn token phù hợp

Phương pháp tạo token theo luồng giúp người dùng nhận phản hồi ngay lập tức khi mô hình tạo văn bản. Điều này tương tự cách các mô hình chạy trên server hoạt động, khi chúng truyền token về cho người dùng, nhưng không có độ trễ do mạng.

Về tương tác giao diện, hai hàm chính là `loadModel()`, khởi tạo LLM, và `fetchAIResponse()`, xử lý đầu vào người dùng và tạo phản hồi AI.

### Lưu ý về định dạng mô hình

> **Important:** Mô hình Phi cho MLX không thể sử dụng ở định dạng mặc định hoặc GGUF. Chúng phải được chuyển đổi sang định dạng MLX, do cộng đồng MLX thực hiện. Bạn có thể tìm các mô hình đã chuyển đổi sẵn tại [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Gói MLX Examples bao gồm các đăng ký cấu hình sẵn cho một số mô hình, bao gồm Phi-3. Khi bạn gọi `ModelRegistry.phi3_5_4bit`, nó sẽ tham chiếu đến một mô hình MLX đã được chuyển đổi sẵn và sẽ tự động tải về:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Bạn có thể tạo cấu hình mô hình riêng để trỏ đến bất kỳ mô hình tương thích nào trên Hugging Face. Ví dụ, để dùng Phi-4 mini, bạn có thể định nghĩa cấu hình riêng:

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

> **Note:** Hỗ trợ Phi-4 được thêm vào kho MLX Swift Examples vào cuối tháng 2 năm 2025 (trong [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Tính đến tháng 3 năm 2025, bản phát hành chính thức mới nhất (2.21.2 từ tháng 12 năm 2024) chưa bao gồm hỗ trợ Phi-4. Để sử dụng mô hình Phi-4, bạn cần tham chiếu gói trực tiếp từ nhánh chính:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Cách này cho phép bạn truy cập các cấu hình mô hình mới nhất, bao gồm Phi-4, trước khi chúng được đưa vào bản phát hành chính thức. Bạn có thể dùng cách này để sử dụng các phiên bản khác nhau của mô hình Phi hoặc các mô hình khác đã được chuyển đổi sang định dạng MLX.

## Bước 6: Tạo giao diện người dùng

Bây giờ hãy triển khai một giao diện chat đơn giản để tương tác với view model:

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

Giao diện gồm ba thành phần chính phối hợp tạo thành một giao diện chat cơ bản. `ContentView` tạo giao diện hai trạng thái, hiển thị nút tải mô hình hoặc giao diện chat tùy theo trạng thái sẵn sàng của mô hình. `MessageView` hiển thị từng tin nhắn chat khác nhau dựa trên việc đó là tin nhắn người dùng (căn phải, nền xanh) hay phản hồi từ mô hình Phi (căn trái, nền xám). `TypingIndicatorView` cung cấp chỉ báo động đơn giản để cho biết AI đang xử lý.

## Bước 7: Xây dựng và chạy ứng dụng

Bây giờ chúng ta đã sẵn sàng để xây dựng và chạy ứng dụng.

> **Important!** MLX không hỗ trợ trình giả lập. Bạn phải chạy ứng dụng trên thiết bị vật lý có chip Apple Silicon. Xem thêm [tại đây](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) để biết thêm chi tiết.

Khi ứng dụng khởi chạy, nhấn nút "Load model" để tải và khởi tạo mô hình Phi-3 (hoặc tùy cấu hình, Phi-4). Quá trình này có thể mất một lúc tùy tốc độ kết nối internet, vì phải tải mô hình từ Hugging Face. Triển khai của chúng ta chỉ có vòng xoay để báo hiệu đang tải, nhưng bạn có thể xem tiến trình thực tế trong bảng điều khiển Xcode.

Khi mô hình đã tải xong, bạn có thể tương tác bằng cách nhập câu hỏi vào ô văn bản và nhấn nút gửi.

Dưới đây là cách ứng dụng của chúng ta hoạt động trên iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Kết luận

Vậy là xong! Bằng cách làm theo các bước này, bạn đã tạo được một ứng dụng iOS chạy mô hình Phi-3 (hoặc Phi-4) trực tiếp trên thiết bị sử dụng framework MLX của Apple.

Chúc mừng bạn!

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.