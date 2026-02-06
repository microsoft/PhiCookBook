# Menjalankan Phi-3 dan Phi-4 di iOS dengan Apple MLX Framework

Tutorial ini menunjukkan cara membuat aplikasi iOS yang menjalankan model Phi-3 atau Phi-4 secara langsung di perangkat, menggunakan framework Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) adalah framework machine learning dari Apple yang dioptimalkan untuk chip Apple Silicon.

## Prasyarat

- macOS dengan Xcode 16 (atau lebih baru)
- Perangkat target iOS 18 (atau lebih baru) dengan minimal 8GB (iPhone atau iPad yang kompatibel dengan persyaratan Apple Intelligence, karena persyaratan ini mirip dengan kebutuhan Phi yang sudah dikuantisasi)
- pengetahuan dasar tentang Swift dan SwiftUI

## Langkah 1: Buat Proyek iOS Baru

Mulailah dengan membuat proyek iOS baru di Xcode:

1. buka Xcode dan pilih "Create a new Xcode project"
2. pilih template "App"
3. beri nama proyek Anda (misalnya, "Phi3-iOS-App") dan pilih SwiftUI sebagai interface
4. pilih lokasi untuk menyimpan proyek Anda

## Langkah 2: Tambahkan Dependensi yang Diperlukan

Tambahkan paket [MLX Examples](https://github.com/ml-explore/mlx-swift-examples) yang berisi semua dependensi dan helper yang diperlukan untuk memuat model dan melakukan inferensi:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Meskipun paket dasar [MLX Swift](https://github.com/ml-explore/mlx-swift) sudah cukup untuk operasi tensor inti dan fungsi ML dasar, paket MLX Examples menyediakan beberapa komponen tambahan yang dirancang untuk bekerja dengan model bahasa dan mempermudah proses inferensi:

- utilitas pemuatan model yang menangani pengunduhan dari Hugging Face
- integrasi tokenizer
- helper inferensi untuk generasi teks
- definisi model yang sudah dikonfigurasi sebelumnya

## Langkah 3: Konfigurasikan Entitlements

Untuk mengizinkan aplikasi kita mengunduh model dan mengalokasikan memori yang cukup, kita perlu menambahkan entitlements tertentu. Buat file `.entitlements` untuk aplikasi Anda dengan isi berikut:

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

> **Note:** Entitlement `com.apple.developer.kernel.increased-memory-limit` penting untuk menjalankan model yang lebih besar, karena memungkinkan aplikasi meminta memori lebih banyak dari batas normal.

## Langkah 4: Buat Model Pesan Chat

Pertama, mari buat struktur dasar untuk merepresentasikan pesan chat kita:

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

## Langkah 5: Implementasikan ViewModel

Selanjutnya, kita akan membuat kelas `PhiViewModel` yang menangani pemuatan model dan inferensi:

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

- mengatur batas cache GPU dengan `MLX.GPU.set(cacheLimit:)` untuk mengoptimalkan penggunaan memori di perangkat mobile
- menggunakan `LLMModelFactory` untuk mengunduh model sesuai permintaan dan menginisialisasi model yang dioptimalkan MLX
- mengakses parameter dan struktur model melalui `ModelContainer`
- memanfaatkan generasi token per token MLX melalui metode `MLXLMCommon.generate`
- mengelola proses inferensi dengan pengaturan temperature dan batas token yang sesuai

Pendekatan generasi token secara streaming memberikan umpan balik langsung kepada pengguna saat model menghasilkan teks. Ini mirip dengan cara kerja model berbasis server yang mengalirkan token kembali ke pengguna, tapi tanpa latensi permintaan jaringan.

Dalam hal interaksi UI, dua fungsi utama adalah `loadModel()`, yang menginisialisasi LLM, dan `fetchAIResponse()`, yang memproses input pengguna dan menghasilkan respons AI.

### Pertimbangan format model

> **Important:** Model Phi untuk MLX tidak bisa digunakan dalam format default atau GGUF. Model harus dikonversi ke format MLX, yang dikelola oleh komunitas MLX. Anda dapat menemukan model yang sudah dikonversi di [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

Paket MLX Examples sudah menyertakan pendaftaran yang dikonfigurasi untuk beberapa model, termasuk Phi-3. Saat Anda memanggil `ModelRegistry.phi3_5_4bit`, itu merujuk pada model MLX yang sudah dikonversi dan akan diunduh secara otomatis:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Anda juga bisa membuat konfigurasi model sendiri untuk menunjuk ke model kompatibel mana pun di Hugging Face. Misalnya, untuk menggunakan Phi-4 mini, Anda bisa mendefinisikan konfigurasi sendiri:

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

> **Note:** Dukungan Phi-4 ditambahkan ke repositori MLX Swift Examples pada akhir Februari 2025 (dalam [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Hingga Maret 2025, rilis resmi terbaru (2.21.2 dari Desember 2024) belum menyertakan dukungan Phi-4 secara built-in. Untuk menggunakan model Phi-4, Anda perlu merujuk paket langsung dari main branch:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Ini memberi Anda akses ke konfigurasi model terbaru, termasuk Phi-4, sebelum dimasukkan dalam rilis resmi. Anda bisa menggunakan cara ini untuk memakai versi berbeda dari model Phi atau model lain yang sudah dikonversi ke format MLX.

## Langkah 6: Buat UI

Sekarang mari kita buat antarmuka chat sederhana untuk berinteraksi dengan view model kita:

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

UI terdiri dari tiga komponen utama yang bekerja sama untuk membuat antarmuka chat dasar. `ContentView` membuat antarmuka dua status yang menampilkan tombol loading atau antarmuka chat tergantung kesiapan model. `MessageView` menampilkan pesan chat secara berbeda berdasarkan apakah itu pesan pengguna (rata kanan, latar belakang biru) atau respons model Phi (rata kiri, latar belakang abu-abu). `TypingIndicatorView` menyediakan indikator animasi sederhana untuk menunjukkan bahwa AI sedang memproses.

## Langkah 7: Membangun dan Menjalankan Aplikasi

Sekarang kita siap membangun dan menjalankan aplikasi.

> **Important!** MLX tidak mendukung simulator. Anda harus menjalankan aplikasi di perangkat fisik dengan chip Apple Silicon. Lihat [di sini](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) untuk informasi lebih lanjut.

Saat aplikasi diluncurkan, ketuk tombol "Load model" untuk mengunduh dan menginisialisasi model Phi-3 (atau, tergantung konfigurasi Anda, Phi-4). Proses ini mungkin memakan waktu tergantung koneksi internet Anda, karena melibatkan pengunduhan model dari Hugging Face. Implementasi kami hanya menampilkan spinner sebagai indikator loading, tapi Anda bisa melihat progres sebenarnya di konsol Xcode.

Setelah dimuat, Anda bisa berinteraksi dengan model dengan mengetik pertanyaan di kolom teks dan mengetuk tombol kirim.

Berikut adalah bagaimana aplikasi kita seharusnya berjalan, dijalankan di iPad Air M1:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Kesimpulan

Itu dia! Dengan mengikuti langkah-langkah ini, Anda telah membuat aplikasi iOS yang menjalankan model Phi-3 (atau Phi-4) langsung di perangkat menggunakan framework MLX dari Apple.

Selamat!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.