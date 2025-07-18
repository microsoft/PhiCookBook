<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:32:26+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "th"
}
-->
# การรัน Phi-3 และ Phi-4 บน iOS ด้วย Apple MLX Framework

บทแนะนำนี้จะแสดงวิธีสร้างแอป iOS ที่รันโมเดล Phi-3 หรือ Phi-4 บนอุปกรณ์โดยตรง โดยใช้ Apple MLX framework [MLX](https://opensource.apple.com/projects/mlx/) คือเฟรมเวิร์กแมชชีนเลิร์นนิงของ Apple ที่ปรับแต่งมาเพื่อชิป Apple Silicon

## สิ่งที่ต้องเตรียม

- macOS พร้อม Xcode 16 (หรือสูงกว่า)
- อุปกรณ์เป้าหมาย iOS 18 (หรือสูงกว่า) ที่มี RAM อย่างน้อย 8GB (iPhone หรือ iPad ที่รองรับข้อกำหนด Apple Intelligence ซึ่งจะใกล้เคียงกับข้อกำหนดของ Phi ที่ถูกควอนไทซ์)
- ความรู้พื้นฐานเกี่ยวกับ Swift และ SwiftUI

## ขั้นตอนที่ 1: สร้างโปรเจกต์ iOS ใหม่

เริ่มต้นด้วยการสร้างโปรเจกต์ iOS ใหม่ใน Xcode:

1. เปิด Xcode แล้วเลือก "Create a new Xcode project"
2. เลือกเทมเพลตเป็น "App"
3. ตั้งชื่อโปรเจกต์ของคุณ (เช่น "Phi3-iOS-App") และเลือก SwiftUI เป็นอินเทอร์เฟซ
4. เลือกที่เก็บโปรเจกต์

## ขั้นตอนที่ 2: เพิ่ม Dependencies ที่จำเป็น

เพิ่ม [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) ซึ่งมี dependencies และตัวช่วยทั้งหมดสำหรับการโหลดโมเดลล่วงหน้าและการทำ inference:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

แม้ว่า [MLX Swift package](https://github.com/ml-explore/mlx-swift) จะเพียงพอสำหรับการทำงาน tensor พื้นฐานและฟังก์ชัน ML เบื้องต้น แต่ MLX Examples package จะมีส่วนประกอบเพิ่มเติมที่ออกแบบมาเพื่อทำงานกับโมเดลภาษา และช่วยให้งาน inference ง่ายขึ้น:

- เครื่องมือโหลดโมเดลที่จัดการการดาวน์โหลดจาก Hugging Face
- การผนวก tokenizer
- ตัวช่วยสำหรับการสร้างข้อความ
- การกำหนดโมเดลที่ตั้งค่าล่วงหน้า

## ขั้นตอนที่ 3: กำหนด Entitlements

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

> **Note:** entitlement `com.apple.developer.kernel.increased-memory-limit` มีความสำคัญสำหรับการรันโมเดลขนาดใหญ่ เพราะช่วยให้แอปขอหน่วยความจำได้มากกว่าปกติ

## ขั้นตอนที่ 4: สร้างโมเดลข้อความแชท

เริ่มด้วยการสร้างโครงสร้างพื้นฐานเพื่อแทนข้อความแชทของเรา:

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

ต่อไปเราจะสร้างคลาส `PhiViewModel` ที่จัดการการโหลดโมเดลและการทำ inference:

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

ViewModel นี้แสดงจุดเชื่อมต่อสำคัญของ MLX:

- กำหนดขีดจำกัดแคช GPU ด้วย `MLX.GPU.set(cacheLimit:)` เพื่อเพิ่มประสิทธิภาพการใช้หน่วยความจำบนอุปกรณ์มือถือ
- ใช้ `LLMModelFactory` เพื่อดาวน์โหลดโมเดลตามความต้องการและเริ่มต้นโมเดลที่ปรับแต่งด้วย MLX
- เข้าถึงพารามิเตอร์และโครงสร้างของโมเดลผ่าน `ModelContainer`
- ใช้การสร้างข้อความทีละโทเค็นของ MLX ผ่านเมธอด `MLXLMCommon.generate`
- จัดการกระบวนการ inference ด้วยการตั้งค่า temperature และขีดจำกัดโทเค็นที่เหมาะสม

การสร้างโทเค็นแบบสตรีมมิ่งช่วยให้ผู้ใช้ได้รับผลลัพธ์ทันทีขณะที่โมเดลกำลังสร้างข้อความ ซึ่งคล้ายกับโมเดลที่รันบนเซิร์ฟเวอร์ที่ส่งโทเค็นกลับมาแบบสตรีม แต่ไม่มีความหน่วงของการร้องขอผ่านเครือข่าย

ในแง่ของการโต้ตอบ UI ฟังก์ชันสำคัญสองอย่างคือ `loadModel()` ที่เริ่มต้น LLM และ `fetchAIResponse()` ที่ประมวลผลอินพุตของผู้ใช้และสร้างคำตอบจาก AI

### ข้อควรพิจารณาเกี่ยวกับรูปแบบโมเดล

> **Important:** โมเดล Phi สำหรับ MLX ไม่สามารถใช้ในรูปแบบเริ่มต้นหรือ GGUF ได้ ต้องแปลงเป็นรูปแบบ MLX ซึ่งชุมชน MLX จะดูแลการแปลงนี้ คุณสามารถหาโมเดลที่แปลงแล้วได้ที่ [huggingface.co/mlx-community](https://huggingface.co/mlx-community)

MLX Examples package มีการลงทะเบียนโมเดลที่ตั้งค่าล่วงหน้าหลายตัว รวมถึง Phi-3 เมื่อคุณเรียก `ModelRegistry.phi3_5_4bit` จะอ้างอิงโมเดล MLX ที่แปลงไว้ล่วงหน้าและดาวน์โหลดโดยอัตโนมัติ:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

คุณสามารถสร้างการกำหนดค่าโมเดลของตัวเองเพื่อชี้ไปยังโมเดลที่เข้ากันได้บน Hugging Face ได้ เช่น หากต้องการใช้ Phi-4 mini แทน คุณสามารถกำหนดการตั้งค่าของคุณเองได้ดังนี้:

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

> **Note:** การรองรับ Phi-4 ถูกเพิ่มเข้ามาใน MLX Swift Examples repository ปลายเดือนกุมภาพันธ์ 2025 (ใน [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)) ปัจจุบัน ณ มีนาคม 2025 รุ่นทางการล่าสุด (2.21.2 จากธันวาคม 2024) ยังไม่มีการรองรับ Phi-4 ในตัว หากต้องการใช้โมเดล Phi-4 คุณต้องอ้างอิงแพ็กเกจโดยตรงจาก main branch:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

วิธีนี้ช่วยให้คุณเข้าถึงการกำหนดค่าโมเดลล่าสุด รวมถึง Phi-4 ก่อนที่จะถูกรวมในรุ่นทางการ คุณสามารถใช้วิธีนี้เพื่อใช้เวอร์ชันต่าง ๆ ของโมเดล Phi หรือแม้แต่โมเดลอื่น ๆ ที่ถูกแปลงเป็นรูปแบบ MLX

## ขั้นตอนที่ 6: สร้าง UI

ตอนนี้เราจะสร้างอินเทอร์เฟซแชทง่าย ๆ เพื่อโต้ตอบกับ view model ของเรา:

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

UI ประกอบด้วยส่วนประกอบหลักสามส่วนที่ทำงานร่วมกันเพื่อสร้างอินเทอร์เฟซแชทพื้นฐาน `ContentView` สร้างอินเทอร์เฟซสองสถานะที่แสดงปุ่มโหลดโมเดลหรืออินเทอร์เฟซแชทขึ้นอยู่กับความพร้อมของโมเดล `MessageView` แสดงข้อความแชทแต่ละข้อความแตกต่างกันตามว่าเป็นข้อความของผู้ใช้ (ชิดขวา พื้นหลังสีน้ำเงิน) หรือคำตอบจากโมเดล Phi (ชิดซ้าย พื้นหลังสีเทา) ส่วน `TypingIndicatorView` แสดงตัวบ่งชี้แบบเคลื่อนไหวง่าย ๆ เพื่อแสดงว่า AI กำลังประมวลผล

## ขั้นตอนที่ 7: สร้างและรันแอป

ตอนนี้เราพร้อมที่จะสร้างและรันแอปแล้ว

> **Important!** MLX ไม่รองรับการรันบน simulator คุณต้องรันแอปบนอุปกรณ์จริงที่ใช้ชิป Apple Silicon ดูข้อมูลเพิ่มเติมได้ที่ [นี่](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS)

เมื่อแอปรันขึ้นมา ให้แตะปุ่ม "Load model" เพื่อดาวน์โหลดและเริ่มต้นโมเดล Phi-3 (หรือ Phi-4 ตามการตั้งค่าของคุณ) กระบวนการนี้อาจใช้เวลาขึ้นอยู่กับความเร็วอินเทอร์เน็ต เพราะต้องดาวน์โหลดโมเดลจาก Hugging Face การใช้งานของเราจะแสดงเพียงสปินเนอร์ระหว่างโหลด แต่คุณสามารถดูความคืบหน้าได้ในคอนโซลของ Xcode

เมื่อโหลดเสร็จแล้ว คุณสามารถโต้ตอบกับโมเดลได้โดยพิมพ์คำถามในช่องข้อความและกดปุ่มส่ง

นี่คือลักษณะการทำงานของแอปเรา ขณะรันบน iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## สรุป

เท่านี้ก็เสร็จเรียบร้อย! โดยทำตามขั้นตอนเหล่านี้ คุณได้สร้างแอป iOS ที่รันโมเดล Phi-3 (หรือ Phi-4) บนอุปกรณ์โดยตรงโดยใช้ Apple MLX framework

ขอแสดงความยินดี!

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้