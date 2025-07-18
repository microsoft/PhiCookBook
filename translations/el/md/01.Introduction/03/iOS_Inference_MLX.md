<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:32:08+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "el"
}
-->
# Εκτέλεση των Phi-3 και Phi-4 σε iOS με το Apple MLX Framework

Αυτό το σεμινάριο δείχνει πώς να δημιουργήσετε μια εφαρμογή iOS που τρέχει το μοντέλο Phi-3 ή Phi-4 τοπικά στη συσκευή, χρησιμοποιώντας το Apple MLX framework. Το [MLX](https://opensource.apple.com/projects/mlx/) είναι το πλαίσιο μηχανικής μάθησης της Apple, βελτιστοποιημένο για τα τσιπ Apple Silicon.

## Απαιτήσεις

- macOS με Xcode 16 (ή νεότερο)
- Συσκευή στόχος iOS 18 (ή νεότερη) με τουλάχιστον 8GB (iPhone ή iPad συμβατό με τις απαιτήσεις Apple Intelligence, που είναι παρόμοιες με τις απαιτήσεις των κβαντισμένων μοντέλων Phi)
- βασικές γνώσεις Swift και SwiftUI

## Βήμα 1: Δημιουργία νέου έργου iOS

Ξεκινήστε δημιουργώντας ένα νέο έργο iOS στο Xcode:

1. ανοίξτε το Xcode και επιλέξτε "Create a new Xcode project"
2. επιλέξτε "App" ως πρότυπο
3. δώστε όνομα στο έργο σας (π.χ. "Phi3-iOS-App") και επιλέξτε SwiftUI ως διεπαφή
4. επιλέξτε τοποθεσία για αποθήκευση του έργου

## Βήμα 2: Προσθήκη απαιτούμενων εξαρτήσεων

Προσθέστε το πακέτο [MLX Examples](https://github.com/ml-explore/mlx-swift-examples) που περιέχει όλες τις απαραίτητες εξαρτήσεις και βοηθητικά εργαλεία για το προφόρτωμα μοντέλων και την εκτέλεση inference:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Ενώ το βασικό [MLX Swift package](https://github.com/ml-explore/mlx-swift) επαρκεί για βασικές λειτουργίες tensor και μηχανικής μάθησης, το πακέτο MLX Examples παρέχει επιπλέον στοιχεία σχεδιασμένα για εργασία με γλωσσικά μοντέλα και για να διευκολύνει τη διαδικασία inference:

- βοηθητικά εργαλεία φόρτωσης μοντέλων που διαχειρίζονται τη λήψη από το Hugging Face
- ενσωμάτωση tokenizer
- βοηθητικά για παραγωγή κειμένου
- προδιαμορφωμένοι ορισμοί μοντέλων

## Βήμα 3: Διαμόρφωση Entitlements

Για να επιτρέψουμε στην εφαρμογή να κατεβάζει μοντέλα και να δεσμεύει αρκετή μνήμη, πρέπει να προσθέσουμε συγκεκριμένα entitlements. Δημιουργήστε ένα αρχείο `.entitlements` για την εφαρμογή σας με το παρακάτω περιεχόμενο:

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

> **Note:** Το entitlement `com.apple.developer.kernel.increased-memory-limit` είναι σημαντικό για την εκτέλεση μεγαλύτερων μοντέλων, καθώς επιτρέπει στην εφαρμογή να ζητά περισσότερη μνήμη από το κανονικά επιτρεπτό.

## Βήμα 4: Δημιουργία μοντέλου μηνύματος συνομιλίας

Αρχικά, ας δημιουργήσουμε μια βασική δομή για να αναπαραστήσουμε τα μηνύματα συνομιλίας:

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

## Βήμα 5: Υλοποίηση του ViewModel

Στη συνέχεια, θα δημιουργήσουμε την κλάση `PhiViewModel` που διαχειρίζεται τη φόρτωση του μοντέλου και το inference:

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

Το ViewModel δείχνει τα βασικά σημεία ενσωμάτωσης με το MLX:

- ρύθμιση ορίων cache GPU με `MLX.GPU.set(cacheLimit:)` για βελτιστοποίηση της χρήσης μνήμης σε κινητές συσκευές
- χρήση του `LLMModelFactory` για λήψη του μοντέλου κατά ζήτηση και αρχικοποίηση του μοντέλου βελτιστοποιημένου για MLX
- πρόσβαση στις παραμέτρους και τη δομή του μοντέλου μέσω του `ModelContainer`
- αξιοποίηση της παραγωγής token-ανά-token του MLX μέσω της μεθόδου `MLXLMCommon.generate`
- διαχείριση της διαδικασίας inference με κατάλληλες ρυθμίσεις θερμοκρασίας και όρια token

Η προσέγγιση παραγωγής token σε ροή παρέχει άμεση ανατροφοδότηση στους χρήστες καθώς το μοντέλο παράγει κείμενο. Αυτό μοιάζει με τον τρόπο λειτουργίας μοντέλων σε διακομιστές, που στέλνουν τα tokens πίσω στον χρήστη σε ροή, αλλά χωρίς την καθυστέρηση των δικτυακών αιτημάτων.

Όσον αφορά την αλληλεπίδραση με το UI, οι δύο βασικές λειτουργίες είναι το `loadModel()`, που αρχικοποιεί το LLM, και το `fetchAIResponse()`, που επεξεργάζεται την είσοδο του χρήστη και παράγει απαντήσεις AI.

### Σκέψεις για τη μορφή μοντέλου

> **Important:** Τα μοντέλα Phi για MLX δεν μπορούν να χρησιμοποιηθούν στην προεπιλεγμένη ή GGUF μορφή τους. Πρέπει να μετατραπούν στη μορφή MLX, κάτι που αναλαμβάνει η κοινότητα MLX. Μπορείτε να βρείτε προ-μετατρεμμένα μοντέλα στο [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Το πακέτο MLX Examples περιλαμβάνει προδιαμορφωμένες εγγραφές για αρκετά μοντέλα, συμπεριλαμβανομένου του Phi-3. Όταν καλείτε το `ModelRegistry.phi3_5_4bit`, αναφέρεται σε ένα συγκεκριμένο προ-μετατρεμμένο μοντέλο MLX που θα κατέβει αυτόματα:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Μπορείτε να δημιουργήσετε τις δικές σας ρυθμίσεις μοντέλου για να δείξετε σε οποιοδήποτε συμβατό μοντέλο στο Hugging Face. Για παράδειγμα, για να χρησιμοποιήσετε το Phi-4 mini, μπορείτε να ορίσετε τη δική σας ρύθμιση:

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

> **Note:** Η υποστήριξη για Phi-4 προστέθηκε στο αποθετήριο MLX Swift Examples στα τέλη Φεβρουαρίου 2025 (στο [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Μέχρι τον Μάρτιο 2025, η τελευταία επίσημη έκδοση (2.21.2 από Δεκέμβριο 2024) δεν περιλαμβάνει ενσωματωμένη υποστήριξη για Phi-4. Για να χρησιμοποιήσετε μοντέλα Phi-4, πρέπει να αναφερθείτε απευθείας στο πακέτο από το κύριο branch:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Αυτό σας δίνει πρόσβαση στις πιο πρόσφατες ρυθμίσεις μοντέλων, συμπεριλαμβανομένου του Phi-4, πριν ενσωματωθούν σε επίσημη έκδοση. Μπορείτε να χρησιμοποιήσετε αυτή την προσέγγιση για να δουλέψετε με διαφορετικές εκδόσεις μοντέλων Phi ή ακόμα και με άλλα μοντέλα που έχουν μετατραπεί στη μορφή MLX.

## Βήμα 6: Δημιουργία του UI

Ας υλοποιήσουμε τώρα μια απλή διεπαφή συνομιλίας για να αλληλεπιδράσουμε με το view model μας:

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

Το UI αποτελείται από τρία βασικά στοιχεία που συνεργάζονται για να δημιουργήσουν μια απλή διεπαφή συνομιλίας. Το `ContentView` δημιουργεί μια διεπαφή δύο καταστάσεων που εμφανίζει είτε ένα κουμπί φόρτωσης είτε τη διεπαφή συνομιλίας ανάλογα με την ετοιμότητα του μοντέλου. Το `MessageView` εμφανίζει τα μεμονωμένα μηνύματα συνομιλίας διαφορετικά, ανάλογα με το αν είναι μηνύματα χρήστη (δεξιά στοίχιση, μπλε φόντο) ή απαντήσεις του μοντέλου Phi (αριστερή στοίχιση, γκρι φόντο). Το `TypingIndicatorView` παρέχει έναν απλό κινούμενο δείκτη που δείχνει ότι το AI επεξεργάζεται.

## Βήμα 7: Κατασκευή και εκτέλεση της εφαρμογής

Είμαστε πλέον έτοιμοι να κατασκευάσουμε και να τρέξουμε την εφαρμογή.

> **Important!** Το MLX δεν υποστηρίζει τον εξομοιωτή. Πρέπει να τρέξετε την εφαρμογή σε φυσική συσκευή με τσιπ Apple Silicon. Δείτε [εδώ](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) για περισσότερες πληροφορίες.

Όταν ξεκινήσει η εφαρμογή, πατήστε το κουμπί "Load model" για να κατεβάσετε και να αρχικοποιήσετε το μοντέλο Phi-3 (ή, ανάλογα με τη ρύθμισή σας, το Phi-4). Αυτή η διαδικασία μπορεί να διαρκέσει λίγο, ανάλογα με τη σύνδεσή σας στο διαδίκτυο, καθώς περιλαμβάνει τη λήψη του μοντέλου από το Hugging Face. Η υλοποίησή μας περιλαμβάνει μόνο έναν περιστρεφόμενο δείκτη φόρτωσης, αλλά μπορείτε να δείτε την πραγματική πρόοδο στην κονσόλα του Xcode.

Μόλις φορτωθεί, μπορείτε να αλληλεπιδράσετε με το μοντέλο πληκτρολογώντας ερωτήσεις στο πεδίο κειμένου και πατώντας το κουμπί αποστολής.

Έτσι θα πρέπει να συμπεριφέρεται η εφαρμογή μας, τρέχοντας σε iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Συμπέρασμα

Και αυτό ήταν! Ακολουθώντας αυτά τα βήματα, δημιουργήσατε μια εφαρμογή iOS που τρέχει το μοντέλο Phi-3 (ή Phi-4) απευθείας στη συσκευή, χρησιμοποιώντας το πλαίσιο MLX της Apple.

Συγχαρητήρια!

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.