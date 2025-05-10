<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-09T11:18:41+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "he"
}
-->
# הפעלת Phi-3 ו-Phi-4 על iOS עם Apple MLX Framework

מדריך זה מראה כיצד ליצור אפליקציית iOS שמריצה את מודל Phi-3 או Phi-4 על המכשיר, באמצעות מסגרת Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) היא מסגרת למידת מכונה של Apple המותאמת לשבבי Apple Silicon.

## דרישות מוקדמות

- macOS עם Xcode 16 (או גרסה חדשה יותר)  
- מכשיר יעד עם iOS 18 (או גרסה חדשה יותר) עם לפחות 8GB זיכרון (iPhone או iPad התואמים לדרישות Apple Intelligence, שדומות לדרישות הכמותיות של Phi)  
- ידע בסיסי ב-Swift ו-SwiftUI  

## שלב 1: יצירת פרויקט iOS חדש

התחילו ביצירת פרויקט iOS חדש ב-Xcode:

1. פתחו את Xcode ובחרו "Create a new Xcode project"  
2. בחרו בתבנית "App"  
3. תנו שם לפרויקט שלכם (למשל "Phi3-iOS-App") ובחרו SwiftUI כממשק  
4. בחרו מיקום לשמירת הפרויקט  

## שלב 2: הוספת תלויות נדרשות

הוסיפו את חבילת [MLX Examples package](https://github.com/ml-explore/mlx-swift-examples) שמכילה את כל התלויות והעזרות הדרושות לטעינת מודלים וביצוע אינפרנס:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

בעוד שחבילת ה-[MLX Swift package](https://github.com/ml-explore/mlx-swift) מספיקה עבור פעולות טנזור בסיסיות ותפקודי ML בסיסיים, חבילת MLX Examples מספקת רכיבים נוספים המיועדים לעבודה עם מודלי שפה ולהקל על תהליך האינפרנס:

- כלים לטעינת מודלים שמטפלים בהורדה מ-Hugging Face  
- אינטגרציה עם tokenizer  
- עזרי אינפרנס ליצירת טקסט  
- הגדרות מודל מוכנות מראש  

## שלב 3: קביעת הרשאות

כדי לאפשר לאפליקציה להוריד מודלים ולהקצות זיכרון מספיק, יש להוסיף הרשאות ספציפיות. צרו קובץ `.entitlements` לאפליקציה שלכם עם התוכן הבא:

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

> **Note:** ההרשאה `com.apple.developer.kernel.increased-memory-limit` חשובה להרצת מודלים גדולים יותר, כי היא מאפשרת לאפליקציה לבקש יותר זיכרון מהרגיל.

## שלב 4: יצירת מודל הודעת הצ'אט

ראשית, ניצור מבנה בסיסי שייצג את הודעות הצ'אט שלנו:

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

## שלב 5: מימוש ה-ViewModel

בהמשך, ניצור את המחלקה `PhiViewModel` שמטפלת בטעינת המודל ובאינפרנס:

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

ה-ViewModel מדגים את נקודות האינטגרציה המרכזיות עם MLX:

- קביעת מגבלות מטמון GPU עם `MLX.GPU.set(cacheLimit:)`  
- שימוש ב-`LLMModelFactory` ו-`ModelContainer`  
- הפעלת הפונקציה `MLXLMCommon.generate`  
- טעינת מודל עם `loadModel()`  
- קבלת תגובות AI עם `fetchAIResponse()`  
- שימוש ב-`ModelRegistry.phi3_5_4bit` שמצביע על מודל MLX מומר ספציפי שיורד אוטומטית:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

אפשר ליצור הגדרות מודל משלכם כדי להפנות לכל מודל תואם ב-Hugging Face. לדוגמה, לשימוש ב-Phi-4 mini במקום זאת, תוכלו להגדיר הגדרה משלכם:

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

> **Note:** תמיכה ב-Phi-4 נוספה למאגר MLX Swift Examples בסוף פברואר 2025 (ב-[PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). נכון למרץ 2025, הגרסה הרשמית האחרונה (2.21.2 מדצמבר 2024) אינה כוללת תמיכה מובנית ב-Phi-4. כדי להשתמש במודלי Phi-4, יש להפנות ישירות לחבילה מהענף הראשי:  
>  
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

כך תקבלו גישה להגדרות המודל העדכניות ביותר, כולל Phi-4, לפני שהן כלולות בשחרור רשמי. ניתן להשתמש בגישה זו כדי להפעיל גרסאות שונות של מודלי Phi או מודלים אחרים שהומרו לפורמט MLX.

## שלב 6: יצירת ממשק המשתמש

כעת נממש ממשק צ'אט פשוט לאינטראקציה עם ה-ViewModel שלנו:

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

ממשק המשתמש מורכב משלושה רכיבים עיקריים שעובדים יחד ליצירת ממשק צ'אט בסיסי. `ContentView`, `MessageView` ו-`TypingIndicatorView` מספקים אינדיקטור מונפש פשוט שמראה שה-AI מעבד את הבקשה.

## שלב 7: בנייה והרצת האפליקציה

כעת אנו מוכנים לבנות ולהריץ את האפליקציה.

> **Important!** MLX אינו תומך בסימולטור. יש להריץ את האפליקציה על מכשיר פיזי עם שבב Apple Silicon. למידע נוסף ראו [כאן](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS).

כאשר האפליקציה עולה, הקישו על כפתור "Load model" כדי להוריד ולהתחיל את מודל Phi-3 (או, בהתאם להגדרות שלכם, Phi-4). תהליך זה עשוי לקחת זמן בהתאם למהירות חיבור האינטרנט, שכן הוא כולל הורדת המודל מ-Hugging Face. המימוש שלנו כולל רק סמן טעינה, אך ניתן לראות את ההתקדמות בקונסול של Xcode.

לאחר הטעינה, תוכלו לתקשר עם המודל על ידי הקלדת שאלות בשדה הטקסט והקשה על כפתור השליחה.

כך האפליקציה שלנו אמורה לפעול על iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## סיכום

וזהו! בעקבות שלבים אלה יצרתם אפליקציית iOS שמריצה את מודל Phi-3 (או Phi-4) ישירות על המכשיר באמצעות מסגרת MLX של Apple.

מזל טוב!

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.