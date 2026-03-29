# AGENTS.md

## Proje Genel Bakış

PhiCookBook, Microsoft'un Phi ailesine ait Küçük Dil Modelleri (SLM'ler) ile çalışma için uygulamalı örnekler, öğreticiler ve dokümantasyon içeren kapsamlı bir tarif kitabı deposudur. Depo, çıkarım, ince ayar, kuantizasyon, RAG uygulamaları ve farklı platformlar ve çerçeveler aracılığıyla çok modlu uygulamalar dahil olmak üzere çeşitli kullanım senaryolarını göstermektedir.

**Ana Teknolojiler:**
- **Diller:** Python, C#/.NET, JavaScript/Node.js
- **Çerçeveler:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformlar:** Microsoft Foundry, GitHub Modelleri, Hugging Face, Ollama
- **Model Türleri:** Phi-3, Phi-3.5, Phi-4 (metin, görsel, çok modlu, akıl yürütme varyantları)

**Depo Yapısı:**
- `/code/` - Çalışan kod örnekleri ve örnek uygulamalar
- `/md/` - Detaylı dokümantasyon, öğreticiler ve kullanım kılavuzları  
- `/translations/` - Çok dilli çeviriler (otomatik iş akışı ile 50+ dil)
- `/.devcontainer/` - Geliştirici konteyner yapılandırması (Python 3.12 ve Ollama ile)

## Geliştirme Ortamı Kurulumu

### GitHub Codespaces veya Dev Containers Kullanımı (Tavsiye Edilir)

1. GitHub Codespaces’da açmak (en hızlı):
   - README'deki "Open in GitHub Codespaces" rozeti üzerine tıklayın
   - Konteyner Python 3.12 ve Phi-3 ile Ollama’yı otomatik yapılandırır

2. VS Code Dev Containers’da açmak:
   - README’deki "Open in Dev Containers" rozeti kullanın
   - Konteyner için minimum 16GB ana bellek gerekir

### Yerel Kurulum

**Gereksinimler:**
- Python 3.12 veya üzeri
- .NET 8.0 SDK (C# örnekleri için)
- Node.js 18+ ve npm (JavaScript örnekleri için)
- Minimum tavsiye edilen: 16GB RAM

**Kurulum:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python Örnekleri için:**
Belirli örnek klasörlerine gidin ve bağımlılıkları yükleyin:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # eğer requirements.txt varsa
```

**.NET Örnekleri için:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Web Örnekleri için:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Geliştirme sunucusunu başlat
npm run build  # Üretim için derle
```

## Depo Organizasyonu

### Kod Örnekleri (`/code/`)

- **01.Introduce/** - Temel tanıtımlar ve başlangıç örnekleri
- **03.Finetuning/** ve **04.Finetuning/** - Çeşitli yöntemlerle ince ayar örnekleri
- **03.Inference/** - Farklı donanımlarda çıkarım örnekleri (AIPC, MLX)
- **06.E2E/** - Uçtan uca uygulama örnekleri
- **07.Lab/** - Laboratuvar/deneysel uygulamalar
- **08.RAG/** - Retrieval-Augmented Generation örnekleri
- **09.UpdateSamples/** - En güncel örnekler

### Dokümantasyon (`/md/`)

- **01.Introduction/** - Giriş rehberleri, ortam kurulumu, platform kılavuzları
- **02.Application/** - Türlerine göre düzenlenmiş uygulama örnekleri (Metin, Kod, Görsel, Ses, vb.)
- **02.QuickStart/** - Microsoft Foundry ve GitHub Modelleri için hızlı başlangıç kılavuzları
- **03.FineTuning/** - İnce ayar dokümantasyonu ve öğreticiler
- **04.HOL/** - Uygulamalı laboratuvarlar (.NET örnekleri dahil)

### Dosya Formatları

- **Jupyter Notebooks (`.ipynb`)** - README'de 📓 ile işaretlenmiş etkileşimli Python öğreticileri
- **Python Scriptleri (`.py`)** - Bağımsız Python örnekleri
- **C# Projeleri (`.csproj`, `.sln`)** - .NET uygulama ve örnekleri
- **JavaScript (`.js`, `package.json`)** - Web tabanlı ve Node.js örnekleri
- **Markdown (`.md`)** - Dokümantasyon ve kılavuzlar

## Örneklerle Çalışmak

### Jupyter Notebook’ları Çalıştırmak

Çoğu örnek Jupyter notebook olarak sağlanır:
```bash
pip install jupyter notebook
jupyter notebook  # Tarayıcı arayüzünü açar
# İstenen .ipynb dosyasına gidin
```

### Python Scriptlerini Çalıştırmak

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET Örneklerini Çalıştırmak

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Ya da tüm çözüme derleme yapın:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Web Örneklerini Çalıştırmak

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Sıcak yeniden yükleme ile geliştirme
```

## Test Etme

Bu depo, birim testleri olan geleneksel bir yazılım projesi yerine örnek kodlar ve öğreticiler içermektedir. Doğrulama genellikle:

1. **Örnekleri çalıştırarak** - Her örneğin hata vermeden çalışması gerekir
2. **Çıktıları doğrulayarak** - Model yanıtlarının uygunluğunu kontrol etmek
3. **Öğreticileri takip ederek** - Adım adım rehberlerin belgelenmiş şekilde çalışması

**Yaygın doğrulama yöntemi:**
- Hedef ortamda örnek çalıştırma testi
- Bağımlılıkların doğru kurulup kurulmadığını kontrol etme
- Model indirmenin/yüklemenin başarıyla tamamlanması
- Beklenen davranışın dokümantasyonla uyumlu olduğunun teyidi

## Kod Stili ve Kurallar

### Genel Yönergeler

- Örnekler açık, iyi yorumlanmış ve eğitici olmalıdır
- Dil özelindeki standartlara uyun (Python için PEP 8, .NET için C# standartları)
- Örneklerde Phi modelinin spesifik yeteneklerini göstermek hedeflenmeli
- Anahtar kavramları ve model özel parametrelerini açıklayan yorumlar ekleyin

### Dokümantasyon Standartları

**URL Formatı:**
- `[text](../../url)` formatı boşluk olmadan kullanılmalı
- Göreceli bağlantılar: mevcut dizin için `./`, üst dizin için `../` kullanılmalı
- URL'lerde ülkeye özgü yerel dil kodları bulunmamalı (örneğin `/en-us/`, `/en/`)

**Görseller:**
- Tüm görseller `/imgs/` dizininde saklanmalı
- İngilizce karakterler, sayılar ve tireler ile açıklayıcı isimler kullanılmalı
- Örnek: `phi-3-architecture.png`

**Markdown Dosyaları:**
- Gerçek çalışan örneklere, `/code/` dizininden referans verilmeli
- Dokümantasyon kod değişiklikleriyle senkronize tutulmalı
- README içindeki Jupyter notebook bağlantıları 📓 ile işaretlenmeli

### Dosya Organizasyonu

- Kod örnekleri `/code/` dizininde konulara/görevlere göre düzenlenmiş
- Dokümantasyon `/md/` dizininde mümkün olduğunca kod yapısını yansıtmalı
- İlgili dosyalar (notebooklar, scriptler, yapılandırmalar) alt dizinlerde birlikte tutulmalı

## Pull Request (PR) Rehberi

### Göndermeden Önce

1. Depoyu kendi hesabınıza **fork** edin
2. **PR’ları türlerine göre ayırın:**
   - Hata düzeltmeleri ayrı PR’da
   - Dokümantasyon güncellemeleri başka PR’da
   - Yeni örnekler ayrı PR’larda
   - Yazım hatası düzeltmeleri bir arada olabilir

3. **Birleştirme çatışmalarını çözün:**
   - Değişiklik yapmadan önce yerel `main` şubenizi güncelleyin
   - Yukarı akışla sık senkronize olun

4. **Çeviri PR’ları:**
   - Klasördeki TÜM dosyalar için çeviriler içermeli
   - Orijinal dil ile tutarlı yapıyı korumalı

### Gerekli Kontroller

PR’lar GitHub iş akışları ile otomatik olarak doğrulanır:

1. **Göreceli yol doğrulaması** - Tüm dahili bağlantılar çalışmalı
   - VS Code’da Ctrl+Tıklama ile test edin
   - Yol önerilerini kullanın (`./` veya `../`)

2. **URL yerel kontrolü** - Web URL'lerinde ülke yerel kodları olmamalı
   - `/en-us/`, `/en/` veya benzeri diller kaldırılmalı
   - Genel uluslararası URL’ler tercih edilmeli

3. **Kırık URL kontrolü** - Tüm URL’ler 200 status döndürmeli
   - Gönderimden önce bağlantılar erişilebilir olmalı
   - Not: Bazı başarısızlıklar ağ kısıtlamalarından kaynaklanabilir

### PR Başlık Formatı

```
[component] Brief description
```

Örnekler:
- `[docs] Phi-4 çıkarım öğreticisi ekle`
- `[code] ONNX Runtime entegrasyon örneğini düzelt`
- `[translation] Giriş rehberleri için Japonca çeviri ekle`

## Yaygın Geliştirme Desenleri

### Phi Modelleri ile Çalışma

**Model Yükleme:**
- Örnekler Transformers, ONNX Runtime, MLX, OpenVINO gibi çerçeveleri kullanır
- Modeller genellikle Hugging Face, Azure veya GitHub Modellerinden indirilir
- Donanım uyumluluğunu kontrol edin (CPU, GPU, NPU)

**Çıkarım Desenleri:**
- Metin üretimi: Çoğu örnek sohbet/yönerge varyantlarını kullanır
- Görsel: Phi-3-vision ve Phi-4-multimodal görüntü anlama için
- Ses: Phi-4-multimodal ses girişlerini destekler
- Akıl yürütme: Gelişmiş akıl yürütme için Phi-4-reasoning varyantları

### Platforma Özgü Notlar

**Microsoft Foundry:**
- Azure aboneliği ve API anahtarları gerektirir
- `/md/02.QuickStart/AzureAIFoundry_QuickStart.md` dosyasına bakınız

**GitHub Modelleri:**
- Test için ücretsiz katman sunar
- `/md/02.QuickStart/GitHubModel_QuickStart.md` dosyasına bakınız

**Yerel Çıkarım:**
- ONNX Runtime: Çok platformlu, optimize çıkarım
- Ollama: Kolay yerel model yönetimi (dev konteynerde ön yapılandırmalı)
- Apple MLX: Apple Silicon için optimize edilmiştir

## Sorun Giderme

### Yaygın Sorunlar

**Bellek Sorunları:**
- Phi modelleri (özellikle görsel/çok modlu varyantlar) yüksek RAM gerektirir
- Kaynak kısıtlı ortamlar için kuantize modeller kullanılabilir
- Bakınız: `/md/01.Introduction/04/QuantifyingPhi.md`

**Bağımlılık Çakışmaları:**
- Python örnekleri belirli sürüm gereksinimleri içerebilir
- Her örnek için sanal ortam kullanın
- Tek tek `requirements.txt` dosyalarını kontrol edin

**Model İndirme Hataları:**
- Büyük modeller yavaş bağlantılarda zaman aşımına uğrayabilir
- Bulut ortamları (Codespaces, Azure) kullanmayı düşünün
- Hugging Face önbelleğini kontrol edin: `~/.cache/huggingface/`

**.NET Proje Sorunları:**
- .NET 8.0 SDK kurulu olduğundan emin olun
- Derlemeden önce `dotnet restore` komutunu kullanın
- Bazı projeler CUDA’ya özgü yapılandırmalar içerir (Debug_Cuda)

**JavaScript/Web Örnekleri:**
- Uyumluluk için Node.js 18+ kullanın
- Sorun devam ediyorsa `node_modules` klasörünü temizleyip yeniden kurun
- WebGPU uyumluluğu için tarayıcı konsolunu kontrol edin

### Yardım Alma

- **Discord:** Microsoft Foundry Topluluk Discord’una katılın
- **GitHub Issues:** Projede hata ve sorun bildirin
- **GitHub Discussions:** Soru sorup bilgi paylaşın

## Ek Bağlam

### Sorumlu Yapay Zeka

Tüm Phi modeli kullanımları Microsoft’un Sorumlu Yapay Zeka ilkelerine uygun olmalıdır:
- Adalet, güvenilirlik, emniyet
- Gizlilik ve güvenlik  
- Kapsayıcılık, şeffaflık, hesap verebilirlik
- Üretim uygulamaları için Azure AI İçerik Güvenliğini kullanın
- Bakınız: `/md/01.Introduction/01/01.AISafety.md`

### Çeviriler

- 50+ dil otomatik GitHub Action ile desteklenir
- Çeviriler `/translations/` dizinindedir
- co-op-translator iş akışı tarafından yönetilir
- Çevrilen dosyalar manuel düzenlenmemelidir (otomatik oluşturulur)

### Katkıda Bulunma

- `CONTRIBUTING.md` içindeki rehberlere uyun
- Katkı Sağlayıcı Lisans Sözleşmesi’ni (CLA) kabul edin
- Microsoft Açık Kaynak Davranış Kuralları’na uyun
- Güvenlik bilgisi ve kimlik bilgilerini commit’lerden çıkarın

### Çok Dilli Destek

Bu depo çok dilli örnekler içerir:
- **Python** - ML/AI iş akışları, Jupyter notebooklar, ince ayar
- **C#/.NET** - Kurumsal uygulamalar, ONNX Runtime entegrasyonu
- **JavaScript** - Web tabanlı yapay zeka, WebGPU ile tarayıcı çıkarımı

Kullanım ve dağıtım hedefinize en uygun dili seçin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermemize rağmen, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlama veya yorumlama için sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->