<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-07-16T20:31:51+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "tr"
}
-->
# iOS'ta Apple MLX Framework ile Phi-3 ve Phi-4 Çalıştırma

Bu eğitim, Apple MLX framework'ünü kullanarak Phi-3 veya Phi-4 modelini cihaz üzerinde çalıştıran bir iOS uygulamasının nasıl oluşturulacağını gösterir. [MLX](https://opensource.apple.com/projects/mlx/), Apple Silicon çipleri için optimize edilmiş Apple’ın makine öğrenimi framework’üdür.

## Gereksinimler

- Xcode 16 (veya üzeri) yüklü macOS
- En az 8GB belleğe sahip iOS 18 (veya üzeri) hedef cihaz (Apple Intelligence gereksinimlerini karşılayan iPhone veya iPad, çünkü bunlar quantize edilmiş Phi gereksinimlerine benzer)
- Swift ve SwiftUI hakkında temel bilgi

## Adım 1: Yeni Bir iOS Projesi Oluşturun

Xcode’da yeni bir iOS projesi oluşturarak başlayın:

1. Xcode’u açın ve "Create a new Xcode project" seçeneğini seçin
2. Şablon olarak "App" seçin
3. Projenize bir isim verin (örneğin, "Phi3-iOS-App") ve arayüz olarak SwiftUI’ı seçin
4. Projenizi kaydetmek için bir konum belirleyin

## Adım 2: Gerekli Bağımlılıkları Ekleyin

Modelleri önceden yüklemek ve çıkarım yapmak için gerekli tüm bağımlılıkları ve yardımcıları içeren [MLX Examples paketi](https://github.com/ml-explore/mlx-swift-examples) ekleyin:

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Temel [MLX Swift paketi](https://github.com/ml-explore/mlx-swift), çekirdek tensör işlemleri ve temel ML işlevselliği için yeterli olsa da, MLX Examples paketi dil modelleriyle çalışmak ve çıkarım sürecini kolaylaştırmak için ek bileşenler sunar:

- Hugging Face’den indirme işlemini yöneten model yükleme araçları
- tokenizer entegrasyonu
- metin üretimi için çıkarım yardımcıları
- önceden yapılandırılmış model tanımları

## Adım 3: Yetkilendirmeleri Yapılandırın

Uygulamamızın modelleri indirebilmesi ve yeterli belleği ayırabilmesi için belirli yetkilendirmeler eklememiz gerekiyor. Uygulamanız için aşağıdaki içeriğe sahip bir `.entitlements` dosyası oluşturun:

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

> **Not:** `com.apple.developer.kernel.increased-memory-limit` yetkilendirmesi, uygulamanın normalde izin verilenin üzerinde bellek talep etmesine olanak tanıdığı için daha büyük modellerin çalıştırılması açısından önemlidir.

## Adım 4: Sohbet Mesajı Modelini Oluşturun

Öncelikle sohbet mesajlarımızı temsil edecek basit bir yapı oluşturalım:

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

## Adım 5: ViewModel’i Uygulayın

Sonraki adımda, model yükleme ve çıkarımı yöneten `PhiViewModel` sınıfını oluşturacağız:

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

ViewModel, MLX entegrasyonunun temel noktalarını gösterir:

- mobil cihazlarda bellek kullanımını optimize etmek için `MLX.GPU.set(cacheLimit:)` ile GPU önbellek sınırlarının ayarlanması
- modeli talep üzerine indirmek ve MLX optimize edilmiş modeli başlatmak için `LLMModelFactory` kullanımı
- modelin parametrelerine ve yapısına `ModelContainer` üzerinden erişim
- MLX’in token token üretimini `MLXLMCommon.generate` yöntemiyle kullanma
- çıkarım sürecini uygun sıcaklık ayarları ve token limitleri ile yönetme

Akış halinde token üretimi, model metin üretirken kullanıcılara anlık geri bildirim sağlar. Bu, sunucu tabanlı modellerin tokenları kullanıcıya akıtmasına benzer, ancak ağ gecikmesi olmadan gerçekleşir.

Kullanıcı arayüzü etkileşimi açısından, iki temel fonksiyon vardır: LLM’i başlatan `loadModel()` ve kullanıcı girdisini işleyip AI yanıtları üreten `fetchAIResponse()`.

### Model formatı ile ilgili notlar

> **Önemli:** MLX için Phi modelleri varsayılan veya GGUF formatında kullanılamaz. MLX formatına dönüştürülmeleri gerekir ve bu dönüşüm MLX topluluğu tarafından yapılır. Önceden dönüştürülmüş modelleri [huggingface.co/mlx-community](https://huggingface.co/mlx-community) adresinde bulabilirsiniz.

MLX Examples paketi, Phi-3 dahil olmak üzere birkaç model için önceden yapılandırılmış kayıtlar içerir. `ModelRegistry.phi3_5_4bit` çağrıldığında, otomatik olarak indirilecek belirli bir önceden dönüştürülmüş MLX modeline referans verir:

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Kendi model yapılandırmalarınızı Hugging Face üzerindeki uyumlu herhangi bir modele işaret edecek şekilde oluşturabilirsiniz. Örneğin, Phi-4 mini kullanmak isterseniz kendi yapılandırmanızı şöyle tanımlayabilirsiniz:

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

> **Not:** Phi-4 desteği, Şubat 2025 sonunda MLX Swift Examples deposuna eklendi ([PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). Mart 2025 itibarıyla, Aralık 2024 tarihli en son resmi sürüm (2.21.2) yerleşik Phi-4 desteği içermez. Phi-4 modellerini kullanmak için paketi ana dal üzerinden doğrudan referans vermeniz gerekir:
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Bu yöntem, resmi sürüme dahil edilmeden önce Phi-4 dahil en güncel model yapılandırmalarına erişmenizi sağlar. Farklı Phi model sürümlerini veya MLX formatına dönüştürülmüş diğer modelleri kullanmak için bu yaklaşımı tercih edebilirsiniz.

## Adım 6: Kullanıcı Arayüzünü Oluşturun

Şimdi, view modelimizle etkileşim kurmak için basit bir sohbet arayüzü uygulayalım:

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

Arayüz, temel bir sohbet deneyimi oluşturmak için birlikte çalışan üç ana bileşenden oluşur. `ContentView`, model hazır olana kadar yükleme butonunu veya sohbet arayüzünü gösteren iki durumlu bir arayüz oluşturur. `MessageView`, kullanıcı mesajlarını (sağa hizalı, mavi arka plan) ve Phi model yanıtlarını (sola hizalı, gri arka plan) farklı şekilde render eder. `TypingIndicatorView` ise AI’nın işlemde olduğunu göstermek için basit bir animasyonlu gösterge sağlar.

## Adım 7: Uygulamayı Derleyip Çalıştırma

Artık uygulamayı derleyip çalıştırmaya hazırız.

> **Önemli!** MLX simülatörü desteklemez. Uygulamayı Apple Silicon çipli gerçek bir cihazda çalıştırmalısınız. Daha fazla bilgi için [buraya](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) bakabilirsiniz.

Uygulama açıldığında, Phi-3 (veya yapılandırmanıza bağlı olarak Phi-4) modelini indirmek ve başlatmak için "Load model" butonuna dokunun. Bu işlem, modelin Hugging Face’den indirilmesini içerdiği için internet bağlantınıza bağlı olarak biraz zaman alabilir. Uygulamamızda sadece yükleme göstergesi (spinner) bulunmakta, ancak gerçek ilerlemeyi Xcode konsolunda görebilirsiniz.

Model yüklendikten sonra, metin alanına sorularınızı yazıp gönder butonuna dokunarak modelle etkileşime geçebilirsiniz.

Uygulamamızın iPad Air M1 üzerinde çalışırken nasıl davrandığı aşağıdaki gibidir:

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Sonuç

İşte bu kadar! Bu adımları takip ederek, Apple’ın MLX framework’ünü kullanarak Phi-3 (veya Phi-4) modelini doğrudan cihaz üzerinde çalıştıran bir iOS uygulaması oluşturmuş oldunuz.

Tebrikler!

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.