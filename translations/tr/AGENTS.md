<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T10:54:47+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tr"
}
-->
# AGENTS.md

## Proje Genel Bakış

PhiCookBook, Microsoft'un Phi ailesine ait Küçük Dil Modelleri (SLM) ile çalışmak için pratik örnekler, eğitimler ve belgeler içeren kapsamlı bir yemek kitabı deposudur. Depo, çıkarım, ince ayar, kuantizasyon, RAG uygulamaları ve farklı platformlar ve çerçeveler üzerinde çok modlu uygulamalar dahil olmak üzere çeşitli kullanım senaryolarını göstermektedir.

**Anahtar Teknolojiler:**
- **Diller:** Python, C#/.NET, JavaScript/Node.js
- **Çerçeveler:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformlar:** Azure AI Foundry, GitHub Modelleri, Hugging Face, Ollama
- **Model Türleri:** Phi-3, Phi-3.5, Phi-4 (metin, görsel, çok modlu, akıl yürütme varyantları)

**Depo Yapısı:**
- `/code/` - Çalışan kod örnekleri ve örnek uygulamalar
- `/md/` - Ayrıntılı belgeler, eğitimler ve nasıl yapılır kılavuzları  
- `/translations/` - Çok dilli çeviriler (50+ dilde otomatik iş akışı ile)
- `/.devcontainer/` - Geliştirme konteyner yapılandırması (Python 3.12 ve Ollama ile)

## Geliştirme Ortamı Kurulumu

### GitHub Codespaces veya Geliştirme Konteynerleri Kullanımı (Önerilen)

1. GitHub Codespaces'te açın (en hızlısı):
   - README'deki "Open in GitHub Codespaces" rozetine tıklayın
   - Konteyner, Python 3.12 ve Phi-3 ile Ollama ile otomatik olarak yapılandırılır

2. VS Code Geliştirme Konteynerlerinde açın:
   - README'deki "Open in Dev Containers" rozetini kullanın
   - Konteyner, minimum 16GB ana bellek gerektirir

### Yerel Kurulum

**Ön Koşullar:**
- Python 3.12 veya üstü
- .NET 8.0 SDK (C# örnekleri için)
- Node.js 18+ ve npm (JavaScript örnekleri için)
- Minimum 16GB RAM önerilir

**Kurulum:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python Örnekleri İçin:**
Belirli örnek dizinlerine gidin ve bağımlılıkları yükleyin:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**.NET Örnekleri İçin:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Web Örnekleri İçin:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Depo Organizasyonu

### Kod Örnekleri (`/code/`)

- **01.Introduce/** - Temel tanıtımlar ve başlangıç örnekleri
- **03.Finetuning/** ve **04.Finetuning/** - Çeşitli yöntemlerle ince ayar örnekleri
- **03.Inference/** - Farklı donanımlarda çıkarım örnekleri (AIPC, MLX)
- **06.E2E/** - Uçtan uca uygulama örnekleri
- **07.Lab/** - Laboratuvar/deneysel uygulamalar
- **08.RAG/** - Retrieval-Augmented Generation örnekleri
- **09.UpdateSamples/** - En son güncellenmiş örnekler

### Belgeler (`/md/`)

- **01.Introduction/** - Giriş kılavuzları, ortam kurulumu, platform kılavuzları
- **02.Application/** - Türüne göre düzenlenmiş uygulama örnekleri (Metin, Kod, Görsel, Ses vb.)
- **02.QuickStart/** - Azure AI Foundry ve GitHub Modelleri için hızlı başlangıç kılavuzları
- **03.FineTuning/** - İnce ayar belgeleri ve eğitimler
- **04.HOL/** - Uygulamalı laboratuvarlar (.NET örneklerini içerir)

### Dosya Formatları

- **Jupyter Notebooks (`.ipynb`)** - README'de 📓 ile işaretlenmiş etkileşimli Python eğitimleri
- **Python Scripts (`.py`)** - Bağımsız Python örnekleri
- **C# Projeleri (`.csproj`, `.sln`)** - .NET uygulamaları ve örnekleri
- **JavaScript (`.js`, `package.json`)** - Web tabanlı ve Node.js örnekleri
- **Markdown (`.md`)** - Belgeler ve kılavuzlar

## Örneklerle Çalışma

### Jupyter Notebooks Çalıştırma

Çoğu örnek Jupyter notebook olarak sunulmaktadır:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Python Scriptleri Çalıştırma

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET Örneklerini Çalıştırma

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Veya tüm çözümü oluşturun:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Web Örneklerini Çalıştırma

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Test Etme

Bu depo, birim testleri olan geleneksel bir yazılım projesinden ziyade örnek kodlar ve eğitimler içermektedir. Doğrulama genellikle şu şekilde yapılır:

1. **Örnekleri çalıştırmak** - Her örnek hatasız çalışmalıdır
2. **Çıktıları doğrulamak** - Model yanıtlarının uygun olup olmadığını kontrol edin
3. **Eğitimleri takip etmek** - Adım adım kılavuzlar belgelerde belirtildiği gibi çalışmalıdır

**Yaygın doğrulama yaklaşımı:**
- Hedef ortamda örnek çalıştırmayı test edin
- Bağımlılıkların doğru şekilde yüklendiğini doğrulayın
- Modelin başarıyla indirildiğini/yüklendiğini kontrol edin
- Beklenen davranışın belgelerle uyumlu olduğunu doğrulayın

## Kod Stili ve Konvansiyonlar

### Genel Yönergeler

- Örnekler açık, iyi yorumlanmış ve eğitici olmalıdır
- Dil spesifik konvansiyonlara uyun (Python için PEP 8, .NET için C# standartları)
- Örnekleri belirli Phi model yeteneklerini göstermeye odaklı tutun
- Anahtar kavramları ve model spesifik parametreleri açıklayan yorumlar ekleyin

### Belge Standartları

**URL Formatı:**
- Ekstra boşluk olmadan `[metin](../../url)` formatını kullanın
- Göreceli bağlantılar: Mevcut dizin için `./`, üst dizin için `../` kullanın
- URL'lerde ülke spesifik yerel ayarları kullanmayın (örneğin `/en-us/`, `/en/`)

**Görseller:**
- Tüm görselleri `/imgs/` dizininde saklayın
- İngilizce karakterler, sayılar ve tireler içeren açıklayıcı isimler kullanın
- Örnek: `phi-3-architecture.png`

**Markdown Dosyaları:**
- `/code/` dizinindeki gerçek çalışan örneklere referans verin
- Belgeleri kod değişiklikleriyle senkronize tutun
- README'de Jupyter notebook bağlantılarını 📓 emojisiyle işaretleyin

### Dosya Organizasyonu

- `/code/` içindeki kod örnekleri konu/özelliklere göre düzenlenmiştir
- `/md/` içindeki belgeler mümkün olduğunda kod yapısını yansıtır
- İlgili dosyaları (notebooklar, scriptler, yapılandırmalar) alt dizinlerde bir arada tutun

## Pull Request Yönergeleri

### Göndermeden Önce

1. **Depoyu kendi hesabınıza çatallayın**
2. **PR'leri türüne göre ayırın:**
   - Hata düzeltmeleri için ayrı bir PR
   - Belge güncellemeleri için başka bir PR
   - Yeni örnekler için ayrı PR'ler
   - Yazım hataları düzeltmeleri birleştirilebilir

3. **Birleşme çatışmalarını ele alın:**
   - Değişiklik yapmadan önce yerel `main` dalınızı güncelleyin
   - Sık sık üst akışla senkronize olun

4. **Çeviri PR'leri:**
   - Klasördeki TÜM dosyaların çevirilerini içermelidir
   - Orijinal dil ile tutarlı yapı korunmalıdır

### Gerekli Kontroller

PR'ler, GitHub iş akışları tarafından otomatik olarak doğrulanır:

1. **Göreceli yol doğrulaması** - Tüm dahili bağlantılar çalışmalıdır
   - Bağlantıları yerel olarak test edin: VS Code'da Ctrl+Tıklayın
   - VS Code'dan yol önerilerini kullanın (`./` veya `../`)

2. **URL yerel ayar kontrolü** - Web URL'lerinde ülke yerel ayarları bulunmamalıdır
   - `/en-us/`, `/en/` veya diğer dil kodlarını kaldırın
   - Genel uluslararası URL'ler kullanın

3. **Bozuk URL kontrolü** - Tüm URL'ler 200 durum kodu döndürmelidir
   - Bağlantıların gönderimden önce erişilebilir olduğunu doğrulayın
   - Not: Bazı hatalar ağ kısıtlamalarından kaynaklanabilir

### PR Başlık Formatı

```
[component] Brief description
```

Örnekler:
- `[docs] Phi-4 çıkarım eğitimi eklendi`
- `[code] ONNX Runtime entegrasyon örneği düzeltildi`
- `[translation] Giriş kılavuzları için Japonca çeviri eklendi`

## Yaygın Geliştirme Kalıpları

### Phi Modelleri ile Çalışma

**Model Yükleme:**
- Örnekler çeşitli çerçeveler kullanır: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeller genellikle Hugging Face, Azure veya GitHub Modellerinden indirilir
- Modelin donanımınızla uyumluluğunu kontrol edin (CPU, GPU, NPU)

**Çıkarım Kalıpları:**
- Metin oluşturma: Çoğu örnek sohbet/talimat varyantlarını kullanır
- Görsel: Görüntü anlama için Phi-3-vision ve Phi-4-multimodal
- Ses: Phi-4-multimodal ses girişlerini destekler
- Akıl yürütme: Gelişmiş akıl yürütme görevleri için Phi-4-reasoning varyantları

### Platforma Özgü Notlar

**Azure AI Foundry:**
- Azure aboneliği ve API anahtarları gerektirir
- Bkz. `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Modelleri:**
- Test için ücretsiz katman mevcuttur
- Bkz. `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Yerel Çıkarım:**
- ONNX Runtime: Çapraz platform, optimize edilmiş çıkarım
- Ollama: Kolay yerel model yönetimi (geliştirme konteynerinde önceden yapılandırılmış)
- Apple MLX: Apple Silicon için optimize edilmiş

## Sorun Giderme

### Yaygın Sorunlar

**Bellek Sorunları:**
- Phi modelleri önemli miktarda RAM gerektirir (özellikle görsel/çok modlu varyantlar)
- Kaynak kısıtlı ortamlar için kuantize edilmiş modelleri kullanın
- Bkz. `/md/01.Introduction/04/QuantifyingPhi.md`

**Bağımlılık Çakışmaları:**
- Python örneklerinin belirli sürüm gereksinimleri olabilir
- Her örnek için sanal ortamlar kullanın
- Bireysel `requirements.txt` dosyalarını kontrol edin

**Model İndirme Hataları:**
- Büyük modeller yavaş bağlantılarda zaman aşımına uğrayabilir
- Bulut ortamlarını kullanmayı düşünün (Codespaces, Azure)
- Hugging Face önbelleğini kontrol edin: `~/.cache/huggingface/`

**.NET Proje Sorunları:**
- .NET 8.0 SDK'nın yüklü olduğundan emin olun
- Oluşturmadan önce `dotnet restore` kullanın
- Bazı projelerde CUDA'ya özgü yapılandırmalar bulunur (Debug_Cuda)

**JavaScript/Web Örnekleri:**
- Uyumluluk için Node.js 18+ kullanın
- `node_modules` klasörünü temizleyin ve sorun devam ederse yeniden yükleyin
- WebGPU uyumluluk sorunları için tarayıcı konsolunu kontrol edin

### Yardım Alma

- **Discord:** Azure AI Foundry Community Discord'a katılın
- **GitHub Issues:** Depodaki hataları ve sorunları bildirin
- **GitHub Discussions:** Sorular sorun ve bilgi paylaşın

## Ek Bağlam

### Sorumlu AI

Tüm Phi modeli kullanımı Microsoft'un Sorumlu AI ilkelerine uygun olmalıdır:
- Adalet, güvenilirlik, güvenlik
- Gizlilik ve güvenlik  
- Kapsayıcılık, şeffaflık, hesap verebilirlik
- Üretim uygulamaları için Azure AI İçerik Güvenliğini kullanın
- Bkz. `/md/01.Introduction/01/01.AISafety.md`

### Çeviriler

- Otomatik GitHub Action aracılığıyla 50+ dil desteklenmektedir
- Çeviriler `/translations/` dizininde bulunmaktadır
- Co-op-translator iş akışı tarafından yönetilmektedir
- Çevrilmiş dosyaları manuel olarak düzenlemeyin (otomatik oluşturulmuş)

### Katkıda Bulunma

- `CONTRIBUTING.md` dosyasındaki yönergeleri takip edin
- Katkıda Bulunan Lisans Sözleşmesi'ni (CLA) kabul edin
- Microsoft Açık Kaynak Davranış Kurallarına uyun
- Güvenlik ve kimlik bilgilerini commitlere dahil etmeyin

### Çok Dilli Destek

Bu depo, aşağıdaki dillerde örnekler içeren bir poliglot depodur:
- **Python** - ML/AI iş akışları, Jupyter notebooklar, ince ayar
- **C#/.NET** - Kurumsal uygulamalar, ONNX Runtime entegrasyonu
- **JavaScript** - Web tabanlı AI, WebGPU ile tarayıcı çıkarımı

Kullanım senaryonuza ve dağıtım hedefinize en uygun dili seçin.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.