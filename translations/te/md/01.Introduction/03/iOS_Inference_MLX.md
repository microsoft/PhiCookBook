<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-12-22T00:53:45+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "te"
}
-->
# Apple MLX ఫ్రేమ్‌వర్క్‌తో iOSలో Phi-3 మరియు Phi-4 నడపడం

This tutorial demonstrates how to create an iOS application that runs the Phi-3 or Phi-4 model on-device, using the Apple MLX framework. [MLX](https://opensource.apple.com/projects/mlx/) is Apple's machine learning framework optimized for Apple Silicon chips.

## ముందస్తు అవసరాలు

- Xcode 16 (లేదా అంతకంటే కొత్త వెర్షన్)తో macOS
- కనీసం 8GB మెమరీ ఉన్న iOS 18 (లేదా అంతకంటే కొత్త) టార్గెట్ డివైస్ (Apple Intelligence అవసరాలకు అనుగుణమైన iPhone లేదా iPad, ఇవి క్వాంటైజ్డ్ Phi అవసరాలకు సమానంగా ఉంటాయి)
- Swift మరియు SwiftUI యొక్క ప్రాథమిక పరిజ్ఞానం

## దశ 1: కొత్త iOS ప్రాజెక్ట్ సృష్టించండి

Start by creating a new iOS project in Xcode:

1. launch Xcode and select "Create a new Xcode project"
2. choose "App" as the template
3. name your project (e.g., "Phi3-iOS-App") and select SwiftUI as the interface
4. choose a location to save your project

## దశ 2: అవసరమైన డిపెండెన్సీలను జోడించండి

Add the [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) which contains all the necessary dependencies and helpers for preloading models and performing inference:

```swift
// Xcodeలో: ఫైల్ > ప్యాకేజ్ డిపెండెన్సీలను జత చేయండి
// యుఆర్‌ఎల్: https://github.com/ml-explore/mlx-swift-examples
```

While the base [MLX Swift package](https://github.com/ml-explore/mlx-swift) would be enough for core tensor operations and basic ML functionality, the MLX Examples package provides several additional components designed for working with language models, and making the inference process easier:

- model loading utilities that handle downloading from Hugging Face
- tokenizer integration
- inference helpers for text generation
- pre-configured model definitions

## దశ 3: ఎంటిట్ల్మెంట్లను కాన్ఫిగర్ చేయండి

To allow our app to download models and allocate sufficient memory, we need to add specific entitlements. Create an `.entitlements` file for your app with the following content:

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

> **గమనిక:** `com.apple.developer.kernel.increased-memory-limit` ఎంటిట్ల్మెంట్ పెద్ద మోడల్‌లను నడపడానికి ముఖ్యమైనది, ఎందుకంటే ఇది సాధారణంగా అనుమతించబడినదికంటే ఎక్కువ మెమరీని యాప్ కోరుకునేలా చేస్తుంది.

## దశ 4: చాట్ సందేశ మోడల్ సృష్టించండి

First, let's create a basic structure to represent our chat messages:

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

## దశ 5: ViewModel ని అమలు చేయండి

Next, we'll create the `PhiViewModel` class that handles model loading and inference:

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
            
            // Phi 3.5 mini Swift MLX Examples లో మునుపే కాన్ఫిగర్ చేయబడింది
            let modelConfig = ModelRegistry.phi3_5_4bit
            
            // Phi 4 mini ను Hugging Face నుండి పొందవచ్చు, కానీ ప్రధాన బ్రాంచ్ నుంచి Swift MLX Examples ను సూచించాల్సి ఉంటుంది
            //let modelConfig = ModelConfiguration(
            //    id: "mlx-community/Phi-4-mini-instruct-4bit",
            //    defaultPrompt: "మీరు ఒక ఉపయోగకరమైన సహాయకుడు."
            //    extraEOSTokens: ["<|end|>"]
            //)
            
            print("Loading \(modelConfig.name)...")
            self.modelContainer = try await LLMModelFactory.shared.loadContainer(
                configuration: modelConfig
            ) { progress in
                print("Download progress: \(Int(progress.fractionCompleted * 100))%")
            }
            
            // మోడల్ పరామితులను లాగ్ చేయండి
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

The ViewModel demonstrates the key MLX integration points:

- setting GPU cache limits with `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### మోడల్ ఫార్మాట్ పరిగణనలు

> **ముఖ్యమైనది:** MLX కోసం Phi మోడళ్లను వారి డిఫాల్ట్ లేదా GGUF ఫార్మాట్‌లో ఉపయోగించరాదు. అవి MLX ఫార్మాట్‌కు మార్పిడి చేయబడాలి, ఇది MLX కమ్యూనిటీ ద్వారా నిర్వహించబడుతుంది. మీరు ముందుగా కన్వర్ట్ చేయబడిన మోడళ్లను [huggingface.co/mlx-community](https://huggingface.co/mlx-community) వద్ద కనుగొనవచ్చు.

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, it references a specific pre-converted MLX model that will be automatically downloaded:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

You can create your own model configurations to point to any compatible model on Hugging Face. For example, to use Phi-4 mini instead, you could define your own configuration:

```swift
let phi4_mini_4bit = ModelConfiguration(
    id: "mlx-community/Phi-4-mini-instruct-4bit",
    defaultPrompt: "Explain quantum computing in simple terms.",
    extraEOSTokens: ["<|end|>"]
)

// తరువాత మోడల్‌ను లోడ్ చేసేటప్పుడు ఈ కాన్ఫిగరేషన్‌ను ఉపయోగించండి
self.modelContainer = try await LLMModelFactory.shared.loadContainer(
    configuration: phi4_mini_4bit
) { progress in
    print("Download progress: \(Int(progress.fractionCompleted * 100))%")
}
```

> **గమనిక:** Phi-4 సపోర్ట్ MLX Swift Examples రిపోజిటరీలో ఫిబ్రవరి 2025 చివరలో (in [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)) జోడించబడింది. మార్చి 2025 నాటికి, డిసెంబర్ 2024 నుండి విడుదలైన తాజా అధికారిక రీలీజ్ (2.21.2)లో బిల్ట్-ఇన్ Phi-4 సపోర్ట్ లేదు. Phi-4 మోడళ్లను ఉపయోగించడానికి, మీరు ప్యాకేజ్‌ను నేరుగా main బ్రాంచ్ నుండి సూచించాలి:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

This gives you access to the latest model configurations, including Phi-4, before they're included in an official release. You can use this approach to use different versions of Phi models or even other models that have been converted to the MLX format.

## దశ 6: UI సృష్టించండి

Let's now implement a simple chat interface to interact with our view model:

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

The UI consists of three main components that work together to create a basic chat interface. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` provides a simple animated indicator to show that the AI is processing

## దశ 7: అప్లికేషన్ బిల్డ్ చేసి నడపడం

We are now ready to build and run the application.

> **ముఖ్యమైనది!** MLX సిమ్యూలేటర్‌ని మద్దతు చేయదు. మీరు యాప్‌ని Apple Silicon చిప్ ఉన్న ఫిజికల్ డివైస్‌పై నడపాలి. మరిన్ని వివరాల కోసం చూడండి [here](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

When the app launches, tap the "Load model" button to download and initialize the Phi-3 (or, depending on your configuration, Phi-4) model. This process may take some time depending on your internet connection, as it involves downloading the model from Hugging Face. Our implementation includes only a spinner to indicate loading, but you can see the actual progress in the Xcode console.

Once loaded, you can interact with the model by typing questions in the text field and tapping the send button.

Here is how our application should behave application, running on iPad Air M1:

![డెమో GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## ముగింపు

And that's it! By following these steps, you've created an iOS application that runs the Phi-3 (or Phi-4) model directly on device using Apple's MLX framework.

అభినందనలు!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తామని గానీ, స్వయంచాలక అనువాదాల్లో పొరపాట్లు లేదా లోపాలు ఉండే అవకాశం ఉండదని దయచేసి గమనించండి. స్థానిక భాషలో ఉన్న మూల పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. కీలక సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదాన్ని ఉపయోగించాలని సిఫార్సు చేయబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించడంతో ఏర్పడిన ఏవైనా అపవగాహనలకు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->