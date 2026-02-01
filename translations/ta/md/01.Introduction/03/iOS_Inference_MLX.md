# iOS-ல் Apple MLX Framework-ஐ பயன்படுத்தி Phi-3 மற்றும் Phi-4 இயக்குதல்

இந்த வழிகாட்டி, Apple MLX framework-ஐ பயன்படுத்தி, Phi-3 அல்லது Phi-4 மாதிரியை iOS சாதனத்தில் இயக்கும் ஒரு பயன்பாட்டை உருவாக்குவது எப்படி என்பதை விளக்குகிறது. [MLX](https://opensource.apple.com/projects/mlx/) என்பது Apple Silicon சிப்களுக்காக மேம்படுத்தப்பட்ட Apple-இன் இயந்திர கற்றல் framework ஆகும்.

## முன் தேவைகள்

- Xcode 16 (அல்லது அதற்கு மேல்) கொண்ட macOS
- குறைந்தது 8GB கொண்ட iOS 18 (அல்லது அதற்கு மேல்) இலக்கு சாதனம் (Apple Intelligence தேவைகளுக்கு இணையான iPhone அல்லது iPad, ஏனெனில் அவை quantized Phi தேவைகளுக்கு ஒத்ததாக இருக்கும்)
- Swift மற்றும் SwiftUI பற்றிய அடிப்படை அறிவு

## படி 1: புதிய iOS திட்டத்தை உருவாக்கவும்

Xcode-ல் புதிய iOS திட்டத்தை உருவாக்கத் தொடங்குங்கள்:

1. Xcode-ஐ தொடங்கி "Create a new Xcode project" என்பதைத் தேர்ந்தெடுக்கவும்
2. "App" எனும் டெம்ப்ளேட்டைத் தேர்ந்தெடுக்கவும்
3. உங்கள் திட்டத்திற்கு பெயர் (எ.கா., "Phi3-iOS-App") கொடுத்து SwiftUI-ஐ இடைமுகமாகத் தேர்ந்தெடுக்கவும்
4. உங்கள் திட்டத்தை சேமிக்க இடத்தைத் தேர்ந்தெடுக்கவும்

## படி 2: தேவையான சார்புகளைச் சேர்க்கவும்

மாதிரிகளை முன்-ஏற்றுதல் மற்றும் தீர்மானங்களைச் செய்ய தேவையான சார்புகள் மற்றும் உதவிகளை உள்ளடக்கிய [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples)-ஐ சேர்க்கவும்:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

அடிப்படை [MLX Swift package](https://github.com/ml-explore/mlx-swift) முக்கியமான டென்சர் செயல்பாடுகள் மற்றும் அடிப்படை ML செயல்பாடுகளுக்கு போதுமானதாக இருக்கும், ஆனால் MLX Examples package மொழி மாதிரிகளுடன் வேலை செய்வதற்காக வடிவமைக்கப்பட்ட கூடுதல் கூறுகளை வழங்குகிறது, மேலும் தீர்மான செயல்முறையை எளிதாக்குகிறது:

- Hugging Face-இல் இருந்து பதிவிறக்கத்தைச் செயல்படுத்தும் மாதிரி ஏற்ற உதவிகள்
- டோக்கனைசர் ஒருங்கிணைப்பு
- உரை உருவாக்கத்திற்கான தீர்மான உதவிகள்
- முன்-கட்டமைக்கப்பட்ட மாதிரி வரையறைகள்

## படி 3: உரிமைகளை உள்ளமைக்கவும்

மாதிரிகளை பதிவிறக்கவும் மற்றும் போதுமான நினைவகத்தை ஒதுக்கவும் உங்கள் பயன்பாட்டிற்கு குறிப்பிட்ட உரிமைகள் தேவைப்படும். உங்கள் பயன்பாட்டிற்கான `.entitlements` கோப்பை பின்வரும் உள்ளடக்கத்துடன் உருவாக்கவும்:

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

> **குறிப்பு:** `com.apple.developer.kernel.increased-memory-limit` உரிமை பெரிய மாதிரிகளை இயக்குவதற்கு முக்கியமானது, ஏனெனில் இது பயன்பாட்டிற்கு சாதாரணமாக அனுமதிக்கப்பட்டதை விட அதிக நினைவகத்தை கோர அனுமதிக்கிறது.

## படி 4: Chat Message மாதிரியை உருவாக்கவும்

முதலில், நமது உரையாடல் செய்திகளை பிரதிநிதித்துவப்படுத்த ஒரு அடிப்படை அமைப்பை உருவாக்குவோம்:

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

## படி 5: ViewModel-ஐ செயல்படுத்தவும்

அடுத்ததாக, மாதிரி ஏற்றுதல் மற்றும் தீர்மானத்தைச் செயல்படுத்தும் `PhiViewModel` வகுப்பை உருவாக்குவோம்:

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

ViewModel MLX ஒருங்கிணைப்பு புள்ளிகளை விளக்குகிறது:

- மொபைல் சாதனங்களில் நினைவக பயன்பாட்டை மேம்படுத்த GPU cache வரம்புகளை `MLX.GPU.set(cacheLimit:)` மூலம் அமைத்தல்
- `LLMModelFactory`-ஐப் பயன்படுத்தி மாதிரியை தேவைப்படும் போது பதிவிறக்கி MLX-ஆக மேம்படுத்தப்பட்ட மாதிரியை ஆரம்பித்தல்
- `ModelContainer` மூலம் மாதிரியின் அளவுகள் மற்றும் அமைப்பை அணுகுதல்
- `MLXLMCommon.generate` முறையின் மூலம் MLX-இன் டோக்கன்-மூலம்-டோக்கன் உருவாக்கத்தை பயன்படுத்துதல்
- சரியான வெப்பநிலை அமைப்புகள் மற்றும் டோக்கன் வரம்புகளுடன் தீர்மான செயல்முறையை நிர்வகித்தல்

ஸ்ட்ரீமிங் டோக்கன் உருவாக்க அணுகுமுறை, மாதிரி உரையை உருவாக்கும் போது பயனர்களுக்கு உடனடி பின்னூட்டத்தை வழங்குகிறது. இது சர்வர்-அடிப்படையிலான மாதிரிகள் செயல்படும் விதத்திற்கு ஒத்ததாக உள்ளது, ஆனால் நெட்வொர்க் கோரிக்கைகளின் தாமதம் இல்லாமல்.

UI தொடர்பு அடிப்படையில், முக்கியமான இரண்டு செயல்பாடுகள் `loadModel()`, இது LLM-ஐ ஆரம்பிக்கிறது, மற்றும் `fetchAIResponse()`, இது பயனர் உள்ளீட்டை செயல்படுத்தி AI பதில்களை உருவாக்குகிறது.

### மாதிரி வடிவமைப்பு கருத்துக்கள்

> **முக்கியமானது:** MLX-க்கு Phi மாதிரிகள் தங்கள் இயல்பான அல்லது GGUF வடிவத்தில் பயன்படுத்த முடியாது. அவை MLX வடிவத்திற்கு மாற்றப்பட வேண்டும், இது MLX சமூகத்தால் நிர்வகிக்கப்படுகிறது. முன்-மாற்றிய மாதிரிகளை [huggingface.co/mlx-community](https://huggingface.co/mlx-community)-இல் காணலாம்.

MLX Examples package பல மாதிரிகளுக்கான முன்-கட்டமைக்கப்பட்ட பதிவுகளை உள்ளடக்கியது, Phi-3 உட்பட. நீங்கள் `ModelRegistry.phi3_5_4bit`-ஐ அழைக்கும் போது, இது குறிப்பிட்ட முன்-மாற்றிய MLX மாதிரியை குறிப்பிடுகிறது, இது தானாகவே பதிவிறக்கப்படும்:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Hugging Face-இல் எந்த மாதிரிக்கும் இணையான உங்கள் சொந்த மாதிரி கட்டமைப்புகளை உருவாக்கலாம். உதாரணமாக, Phi-4 mini-ஐ பயன்படுத்த, நீங்கள் உங்கள் சொந்த கட்டமைப்பை வரையறுக்கலாம்:

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

> **குறிப்பு:** Phi-4 ஆதரவு MLX Swift Examples repository-க்கு 2025 பிப்ரவரி இறுதியில் சேர்க்கப்பட்டது ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)-இல்). 2025 மார்ச் நிலவரப்படி, சமீபத்திய அதிகாரப்பூர்வ வெளியீடு (2024 டிசம்பர் 2.21.2) உள்ள built-in Phi-4 ஆதரவை கொண்டிருக்காது. Phi-4 மாதிரிகளைப் பயன்படுத்த, நீங்கள் package-ஐ நேரடியாக முக்கிய கிளையிலிருந்து குறிப்பிட வேண்டும்:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

இது Phi-4 உட்பட சமீபத்திய மாதிரி கட்டமைப்புகளுக்கு அணுகலை வழங்குகிறது, அவை அதிகாரப்பூர்வ வெளியீட்டில் சேர்க்கப்படுவதற்கு முன். இந்த அணுகுமுறையைப் பயன்படுத்தி Phi மாதிரிகளின் வெவ்வேறு பதிப்புகளை அல்லது MLX வடிவத்திற்கு மாற்றப்பட்ட பிற மாதிரிகளைப் பயன்படுத்தலாம்.

## படி 6: UI உருவாக்கவும்

இப்போது நமது ViewModel-இன் மூலம் தொடர்பு கொள்ள ஒரு எளிய உரையாடல் இடைமுகத்தை செயல்படுத்துவோம்:

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

UI மூன்று முக்கிய கூறுகளை உள்ளடக்கியது, அவை ஒன்றாக இணைந்து ஒரு அடிப்படை உரையாடல் இடைமுகத்தை உருவாக்குகின்றன. `ContentView` மாதிரி தயாராக உள்ளதா என்பதைப் பொறுத்து ஒரு இரண்டு நிலை இடைமுகத்தை உருவாக்குகிறது, இது ஏற்றும் பொத்தானை அல்லது உரையாடல் இடைமுகத்தை காட்டுகிறது. `MessageView` தனிப்பட்ட உரையாடல் செய்திகளை, பயனர் செய்திகளாக (வலது பக்கம், நீல பின்னணி) அல்லது Phi மாதிரி பதில்களாக (இடது பக்கம், சாம்பல் பின்னணி) வேறுபடுத்தி காட்டுகிறது. `TypingIndicatorView` AI செயல்படுவதை காட்ட ஒரு எளிய அனிமேஷன் குறியீட்டை வழங்குகிறது.

## படி 7: பயன்பாட்டை கட்டமைத்து இயக்கவும்

இப்போது பயன்பாட்டை கட்டமைத்து இயக்க தயாராக உள்ளோம்.

> **முக்கியமானது!** MLX சிமுலேட்டரை ஆதரிக்காது. Apple Silicon சிப்புடன் கூடிய ஒரு இயல்பான சாதனத்தில் பயன்பாட்டை இயக்க வேண்டும். மேலும் தகவலுக்கு [இங்கே](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) பார்க்கவும்.

பயன்பாடு தொடங்கும்போது, "Load model" பொத்தானை தட்டவும், இது Phi-3 (அல்லது உங்கள் கட்டமைப்பைப் பொறுத்து Phi-4) மாதிரியை பதிவிறக்கி ஆரம்பிக்கும். Hugging Face-இல் இருந்து மாதிரியை பதிவிறக்குவதால், உங்கள் இணைய இணைப்பின் வேகத்தைப் பொறுத்து இந்த செயல்முறை சில நேரம் எடுக்கலாம். நமது செயல்பாட்டில் ஏற்றத்தை குறிக்க ஒரு ஸ்பின்னர் மட்டுமே உள்ளது, ஆனால் நீங்கள் Xcode console-இல் உண்மையான முன்னேற்றத்தை காணலாம்.

மாதிரி ஏற்றப்பட்டவுடன், உரை புலத்தில் கேள்விகளை தட்டச்சு செய்து, அனுப்பும் பொத்தானை தட்டுவதன் மூலம் மாதிரியுடன் தொடர்பு கொள்ளலாம்.

இது iPad Air M1-ல் இயங்கும் நமது பயன்பாட்டின் செயல்பாடு:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## முடிவு

அதுவே! இந்த படிகளைப் பின்பற்றுவதன் மூலம், Apple MLX framework-ஐப் பயன்படுத்தி Phi-3 (அல்லது Phi-4) மாதிரியை நேரடியாக சாதனத்தில் இயக்கும் iOS பயன்பாட்டை உருவாக்கியுள்ளீர்கள்.

வாழ்த்துக்கள்!

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரத்தை உறுதிப்படுத்த முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.