<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:15:11+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "th"
}
-->
# การรัน Phi-3 และ Phi-4 บน iOS ด้วย Apple MLX Framework

บทแนะนำนี้จะแสดงวิธีสร้างแอป iOS ที่รันโมเดล Phi-3 หรือ Phi-4 บนอุปกรณ์โดยตรง โดยใช้ Apple MLX framework [MLX](https://opensource.apple.com/projects/mlx/) คือเฟรมเวิร์ก machine learning ของ Apple ที่ออกแบบมาเพื่อให้เหมาะกับชิป Apple Silicon

## สิ่งที่ต้องมี

- macOS พร้อม Xcode 16 (หรือสูงกว่า)
- อุปกรณ์เป้าหมาย iOS 18 (หรือสูงกว่า) ที่มี RAM อย่างน้อย 8GB (iPhone หรือ iPad ที่รองรับความต้องการ Apple Intelligence ซึ่งจะคล้ายกับความต้องการของโมเดล Phi ที่ถูกควอนไทซ์)
- ความรู้พื้นฐานเกี่ยวกับ Swift และ SwiftUI

## ขั้นตอนที่ 1: สร้างโปรเจกต์ iOS ใหม่

เริ่มต้นด้วยการสร้างโปรเจกต์ iOS ใหม่ใน Xcode:

1. เปิด Xcode แล้วเลือก "Create a new Xcode project"
2. เลือก "App" เป็นเทมเพลต
3. ตั้งชื่อโปรเจกต์ของคุณ (เช่น "Phi3-iOS-App") และเลือก SwiftUI เป็นอินเทอร์เฟซ
4. เลือกตำแหน่งที่จะบันทึกโปรเจกต์

## ขั้นตอนที่ 2: เพิ่ม Dependencies ที่จำเป็น

เพิ่ม [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ซึ่งมี dependencies และ helpers ที่จำเป็นสำหรับการโหลดโมเดลล่วงหน้าและการทำ inference:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

แม้ว่า [MLX Swift package](https://github.com/ml-explore/mlx-swift) จะเพียงพอสำหรับการทำ tensor operations และฟังก์ชันพื้นฐานของ ML แต่ MLX Examples package จะมีคอมโพเนนต์เพิ่มเติมที่ออกแบบมาเพื่อการทำงานกับ language models และช่วยให้งาน inference ง่ายขึ้น:

- เครื่องมือช่วยโหลดโมเดลที่จัดการการดาวน์โหลดจาก Hugging Face
- การผนวกรวม tokenizer
- helpers สำหรับการสร้างข้อความ
- คอนฟิกโมเดลที่ตั้งค่าไว้ล่วงหน้า

## ขั้นตอนที่ 3: ตั้งค่า Entitlements

เพื่อให้แอปของเราสามารถดาวน์โหลดโมเดลและจัดสรรหน่วยความจำได้เพียงพอ เราต้องเพิ่ม entitlements เฉพาะ สร้างไฟล์ `.entitlements` สำหรับแอปของคุณโดยมีเนื้อหาดังนี้:

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

> **Note:** entitlement `com.apple.developer.kernel.increased-memory-limit` มีความสำคัญสำหรับการรันโมเดลขนาดใหญ่ เพราะช่วยให้แอปขอหน่วยความจำมากกว่าปกติได้

## ขั้นตอนที่ 4: สร้างโมเดลข้อความแชท

เริ่มจากสร้างโครงสร้างพื้นฐานเพื่อแทนข้อความแชทของเรา:

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

## ขั้นตอนที่ 5: เขียน ViewModel

ถัดไป เราจะสร้างคลาส `PhiViewModel` ที่จัดการการโหลดโมเดลและการทำ inference:

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

ViewModel นี้แสดงจุดสำคัญของการผนวกรวม MLX:

- การตั้งค่าขีดจำกัดแคช GPU ด้วย `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit` ซึ่งอ้างอิงโมเดล MLX ที่ถูกแปลงไว้ล่วงหน้าตัวหนึ่งที่จะถูกดาวน์โหลดโดยอัตโนมัติ:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

คุณสามารถสร้างคอนฟิกโมเดลของตัวเองเพื่อชี้ไปยังโมเดลที่เข้ากันได้บน Hugging Face ได้ เช่น หากต้องการใช้ Phi-4 mini แทน ก็สามารถกำหนดคอนฟิกของตัวเองได้ดังนี้:

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

> **Note:** การรองรับ Phi-4 ถูกเพิ่มเข้ามาใน MLX Swift Examples repository ปลายเดือนกุมภาพันธ์ 2025 (ใน [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)) ณ เดือนมีนาคม 2025 รุ่นล่าสุดที่ออกอย่างเป็นทางการ (2.21.2 จากธันวาคม 2024) ยังไม่มีการรองรับ Phi-4 แบบ built-in หากต้องการใช้โมเดล Phi-4 คุณต้องอ้างอิงแพ็กเกจโดยตรงจาก main branch:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

วิธีนี้จะช่วยให้คุณเข้าถึงคอนฟิกโมเดลล่าสุด รวมถึง Phi-4 ก่อนที่จะถูกรวมใน release อย่างเป็นทางการ คุณสามารถใช้วิธีนี้เพื่อใช้งานเวอร์ชันต่าง ๆ ของโมเดล Phi หรือโมเดลอื่น ๆ ที่ถูกแปลงเป็นฟอร์แมต MLX

## ขั้นตอนที่ 6: สร้าง UI

ตอนนี้มาสร้างอินเทอร์เฟซแชทง่าย ๆ เพื่อโต้ตอบกับ view model ของเรากัน:

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

UI ประกอบด้วยสามส่วนหลักที่ทำงานร่วมกันเพื่อสร้างอินเทอร์เฟซแชทพื้นฐาน `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` มีตัวบ่งชี้แบบเคลื่อนไหวง่าย ๆ เพื่อแสดงว่า AI กำลังประมวลผล

## ขั้นตอนที่ 7: สร้างและรันแอป

ตอนนี้เราพร้อมที่จะสร้างและรันแอปแล้ว

> **Important!** MLX ไม่รองรับ simulator คุณต้องรันแอปบนอุปกรณ์จริงที่ใช้ชิป Apple Silicon ดูรายละเอียดเพิ่มเติมได้ที่ [นี่](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)

เมื่อแอปรันขึ้นมา ให้แตะปุ่ม "Load model" เพื่อดาวน์โหลดและเริ่มต้นโมเดล Phi-3 (หรือ Phi-4 ตามคอนฟิกของคุณ) กระบวนการนี้อาจใช้เวลาขึ้นอยู่กับความเร็วอินเทอร์เน็ต เพราะต้องดาวน์โหลดโมเดลจาก Hugging Face การใช้งานของเรามีเพียง spinner เพื่อแสดงสถานะการโหลด แต่คุณสามารถดูความคืบหน้าในคอนโซลของ Xcode ได้

เมื่อโหลดเสร็จ คุณก็สามารถโต้ตอบกับโมเดลโดยพิมพ์คำถามในช่องข้อความแล้วกดปุ่มส่งได้เลย

นี่คือลักษณะการทำงานของแอปบน iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## สรุป

แค่นี้แหละ! โดยทำตามขั้นตอนเหล่านี้ คุณก็ได้สร้างแอป iOS ที่รันโมเดล Phi-3 (หรือ Phi-4) บนอุปกรณ์โดยตรงด้วย Apple MLX framework

ขอแสดงความยินดี!

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาดั้งเดิมถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ควรใช้บริการแปลโดยมนุษย์ผู้เชี่ยวชาญ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้