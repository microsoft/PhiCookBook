<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:34:47+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "ms"
}
-->
# Menjalankan Phi-3 dan Phi-4 pada iOS dengan Rangka Kerja Apple MLX

Tutorial ini menunjukkan cara untuk mencipta aplikasi iOS yang menjalankan model Phi-3 atau Phi-4 secara terus pada peranti, menggunakan rangka kerja Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) adalah rangka kerja pembelajaran mesin Apple yang dioptimumkan untuk cip Apple Silicon.

## Prasyarat

- macOS dengan Xcode 16 (atau lebih tinggi)
- Peranti sasaran iOS 18 (atau lebih tinggi) dengan sekurang-kurangnya 8GB (iPhone atau iPad yang serasi dengan keperluan Apple Intelligence, kerana ia serupa dengan keperluan kuantisasi Phi)
- pengetahuan asas tentang Swift dan SwiftUI

## Langkah 1: Cipta Projek iOS Baru

Mulakan dengan mencipta projek iOS baru dalam Xcode:

1. lancarkan Xcode dan pilih "Create a new Xcode project"
2. pilih "App" sebagai templat
3. namakan projek anda (contohnya, "Phi3-iOS-App") dan pilih SwiftUI sebagai antara muka
4. pilih lokasi untuk menyimpan projek anda

## Langkah 2: Tambah Kebergantungan Diperlukan

Tambah pakej [MLX Examples](https://github.com/ml-explore/mlx-swift-examples) yang mengandungi semua kebergantungan dan pembantu yang diperlukan untuk memuatkan model dan menjalankan inferens:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Walaupun pakej asas [MLX Swift](https://github.com/ml-explore/mlx-swift) sudah mencukupi untuk operasi tensor teras dan fungsi ML asas, pakej MLX Examples menyediakan beberapa komponen tambahan yang direka untuk bekerja dengan model bahasa, dan memudahkan proses inferens:

- utiliti pemuatan model yang mengendalikan muat turun dari Hugging Face
- integrasi tokenizer
- pembantu inferens untuk penjanaan teks
- definisi model yang telah dikonfigurasikan terlebih dahulu

## Langkah 3: Konfigurasikan Entitlements

Untuk membenarkan aplikasi kita memuat turun model dan memperuntukkan memori yang mencukupi, kita perlu menambah entitlements tertentu. Cipta fail `.entitlements` untuk aplikasi anda dengan kandungan berikut:

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

> **Note:** Entitlement `com.apple.developer.kernel.increased-memory-limit` penting untuk menjalankan model yang lebih besar, kerana ia membenarkan aplikasi meminta lebih banyak memori daripada yang biasanya dibenarkan.

## Langkah 4: Cipta Model Mesej Chat

Mula-mula, mari kita cipta struktur asas untuk mewakili mesej chat kita:

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

## Langkah 5: Laksanakan ViewModel

Seterusnya, kita akan cipta kelas `PhiViewModel` yang mengendalikan pemuatan model dan inferens:

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

ViewModel ini menunjukkan titik integrasi utama MLX:

- menetapkan had cache GPU dengan `MLX.GPU.set(cacheLimit:)` untuk mengoptimumkan penggunaan memori pada peranti mudah alih
- menggunakan `LLMModelFactory` untuk memuat turun model mengikut permintaan dan memulakan model yang dioptimumkan MLX
- mengakses parameter dan struktur model melalui `ModelContainer`
- menggunakan penjanaan token demi token MLX melalui kaedah `MLXLMCommon.generate`
- menguruskan proses inferens dengan tetapan suhu dan had token yang sesuai

Pendekatan penjanaan token secara streaming memberikan maklum balas segera kepada pengguna semasa model menjana teks. Ini serupa dengan cara model berasaskan pelayan berfungsi, yang menstrim token kembali kepada pengguna, tetapi tanpa kelewatan permintaan rangkaian.

Dari segi interaksi UI, dua fungsi utama adalah `loadModel()`, yang memulakan LLM, dan `fetchAIResponse()`, yang memproses input pengguna dan menjana respons AI.

### Pertimbangan format model

> **Important:** Model Phi untuk MLX tidak boleh digunakan dalam format lalai atau GGUF mereka. Ia mesti ditukar ke format MLX, yang dikendalikan oleh komuniti MLX. Anda boleh mendapatkan model yang telah ditukar di [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Pakej MLX Examples termasuk pendaftaran yang telah dikonfigurasikan untuk beberapa model, termasuk Phi-3. Apabila anda memanggil `ModelRegistry.phi3_5_4bit`, ia merujuk kepada model MLX yang telah ditukar yang akan dimuat turun secara automatik:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Anda boleh mencipta konfigurasi model anda sendiri untuk merujuk mana-mana model yang serasi di Hugging Face. Contohnya, untuk menggunakan Phi-4 mini, anda boleh mentakrifkan konfigurasi anda sendiri:

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

> **Note:** Sokongan Phi-4 ditambah ke repositori MLX Swift Examples pada akhir Februari 2025 (dalam [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Sehingga Mac 2025, keluaran rasmi terkini (2.21.2 dari Disember 2024) tidak termasuk sokongan Phi-4 terbina dalam. Untuk menggunakan model Phi-4, anda perlu merujuk pakej terus dari cabang utama:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Ini memberi anda akses kepada konfigurasi model terkini, termasuk Phi-4, sebelum ia dimasukkan dalam keluaran rasmi. Anda boleh menggunakan pendekatan ini untuk menggunakan versi berbeza model Phi atau model lain yang telah ditukar ke format MLX.

## Langkah 6: Cipta UI

Sekarang mari kita laksanakan antara muka chat ringkas untuk berinteraksi dengan view model kita:

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

UI terdiri daripada tiga komponen utama yang bekerjasama untuk mencipta antara muka chat asas. `ContentView` mencipta antara muka dua keadaan yang menunjukkan sama ada butang memuatkan atau antara muka chat bergantung pada kesediaan model. `MessageView` memaparkan mesej chat individu secara berbeza berdasarkan sama ada ia mesej pengguna (selari kanan, latar biru) atau respons model Phi (selari kiri, latar kelabu). `TypingIndicatorView` menyediakan penunjuk animasi ringkas untuk menunjukkan AI sedang memproses.

## Langkah 7: Membina dan Menjalankan Aplikasi

Kita kini bersedia untuk membina dan menjalankan aplikasi.

> **Important!** MLX tidak menyokong simulator. Anda mesti menjalankan aplikasi pada peranti fizikal dengan cip Apple Silicon. Lihat [di sini](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) untuk maklumat lanjut.

Apabila aplikasi dilancarkan, ketik butang "Load model" untuk memuat turun dan memulakan model Phi-3 (atau, bergantung pada konfigurasi anda, Phi-4). Proses ini mungkin mengambil masa bergantung pada sambungan internet anda, kerana ia melibatkan muat turun model dari Hugging Face. Pelaksanaan kami hanya termasuk penunjuk putaran untuk menunjukkan pemuatan, tetapi anda boleh melihat kemajuan sebenar dalam konsol Xcode.

Setelah dimuatkan, anda boleh berinteraksi dengan model dengan menaip soalan dalam medan teks dan mengetik butang hantar.

Berikut adalah bagaimana aplikasi kita sepatutnya berfungsi, berjalan pada iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Kesimpulan

Itulah dia! Dengan mengikuti langkah-langkah ini, anda telah mencipta aplikasi iOS yang menjalankan model Phi-3 (atau Phi-4) terus pada peranti menggunakan rangka kerja MLX Apple.

Tahniah!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.