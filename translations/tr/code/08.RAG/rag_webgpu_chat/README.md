<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:18:08+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "tr"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## WebGPU ve RAG Desenini Gösteren Demo
Phi-3 Onnx Hosted model ile RAG Deseni, Retrieval-Augmented Generation yaklaşımını kullanarak Phi-3 modellerinin gücünü ONNX barındırma ile birleştirir ve verimli AI dağıtımları sağlar. Bu desen, alan spesifik görevler için modellerin ince ayar yapılmasında önemli rol oynar; kalite, maliyet etkinliği ve uzun bağlam anlayışını bir arada sunar. Azure AI’nin bir parçası olarak, çeşitli sektörlerin özelleştirme ihtiyaçlarına hitap eden, kolayca bulunabilen, denenebilen ve kullanılabilen geniş bir model seçkisi sunar. Phi-3-mini, Phi-3-small ve Phi-3-medium dahil Phi-3 modelleri, Azure AI Model Kataloğunda mevcuttur ve HuggingFace, ONNX gibi platformlar üzerinden ya da kendi kendine yönetilen yöntemlerle ince ayar yapılıp dağıtılabilir; bu da Microsoft’un erişilebilir ve verimli AI çözümlerine olan bağlılığını gösterir.

## WebGPU Nedir
WebGPU, web tarayıcılarından doğrudan cihazın grafik işlem birimine (GPU) verimli erişim sağlamak üzere tasarlanmış modern bir web grafik API’sidir. WebGL’in halefi olarak geliştirilmiş olup, şu önemli iyileştirmeleri sunar:

1. **Modern GPU’larla Uyumluluk**: WebGPU, Vulkan, Metal ve Direct3D 12 gibi sistem API’lerini kullanarak güncel GPU mimarileriyle sorunsuz çalışacak şekilde tasarlanmıştır.
2. **Geliştirilmiş Performans**: Hem grafik render işlemleri hem de makine öğrenimi görevleri için uygun olan genel amaçlı GPU hesaplamalarını ve daha hızlı işlemleri destekler.
3. **Gelişmiş Özellikler**: Daha karmaşık ve dinamik grafik ve hesaplama iş yüklerine olanak tanıyan gelişmiş GPU yeteneklerine erişim sağlar.
4. **Azaltılmış JavaScript İş Yükü**: Daha fazla görevi GPU’ya devrederek JavaScript üzerindeki iş yükünü önemli ölçüde azaltır, böylece daha iyi performans ve daha akıcı deneyimler sunar.

WebGPU şu anda Google Chrome gibi tarayıcılarda desteklenmektedir ve diğer platformlara desteğin genişletilmesi için çalışmalar devam etmektedir.

### 03.WebGPU
Gerekli Ortam:

**Desteklenen tarayıcılar:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU’yu Etkinleştirme:

- Chrome/Microsoft Edge’de

`chrome://flags/#enable-unsafe-webgpu` bayrağını etkinleştirin.

#### Tarayıcınızı Açın:
Google Chrome veya Microsoft Edge’i başlatın.

#### Bayraklar Sayfasına Erişin:
Adres çubuğuna `chrome://flags` yazın ve Enter’a basın.

#### Bayrağı Arayın:
Sayfanın üstündeki arama kutusuna 'enable-unsafe-webgpu' yazın.

#### Bayrağı Etkinleştirin:
Sonuçlar listesinde #enable-unsafe-webgpu bayrağını bulun.

Yanındaki açılır menüden Enabled seçeneğini seçin.

#### Tarayıcınızı Yeniden Başlatın:

Bayrağı etkinleştirdikten sonra değişikliklerin uygulanması için tarayıcınızı yeniden başlatmanız gerekir. Sayfanın alt kısmında beliren Relaunch düğmesine tıklayın.

- Linux için, tarayıcıyı `--enable-features=Vulkan` ile başlatın.
- Safari 18 (macOS 15) varsayılan olarak WebGPU etkin halde gelir.
- Firefox Nightly’de adres çubuğuna about:config yazın ve `set dom.webgpu.enabled to true`.

### Microsoft Edge için GPU Ayarları

Windows üzerinde Microsoft Edge için yüksek performanslı GPU ayarlamak için şu adımları izleyin:

- **Ayarları Açın:** Başlat menüsüne tıklayın ve Ayarlar’ı seçin.
- **Sistem Ayarları:** Sistem’e, ardından Görüntüle’ye gidin.
- **Grafik Ayarları:** Aşağı kaydırın ve Grafik ayarları’na tıklayın.
- **Uygulama Seçin:** “Tercih ayarlamak için bir uygulama seçin” altında Masaüstü uygulaması’nı seçin ve Gözat’a tıklayın.
- **Edge’i Seçin:** Edge kurulum klasörüne gidin (genellikle `C:\Program Files (x86)\Microsoft\Edge\Application`) ve `msedge.exe` dosyasını seçin.
- **Tercihi Ayarlayın:** Seçenekler’e tıklayın, Yüksek performans’ı seçin ve Kaydet’e tıklayın.
Bu, Microsoft Edge’in daha iyi performans için yüksek performanslı GPU’nuzu kullanmasını sağlar.
- Bu ayarların geçerli olması için bilgisayarınızı yeniden başlatın.

### Kod Alanınızı Açın:
GitHub’daki depoya gidin.
Kod düğmesine tıklayın ve Codespaces ile Aç seçeneğini seçin.

Henüz bir Codespace’iniz yoksa, Yeni codespace’e tıklayarak oluşturabilirsiniz.

**Not** Codespace’inizde Node Ortamını Kurma
GitHub Codespace’ten npm demosu çalıştırmak, projenizi test etmek ve geliştirmek için harika bir yoldur. İşte başlamanıza yardımcı olacak adım adım rehber:

### Ortamınızı Kurun:
Codespace açıldıktan sonra Node.js ve npm’nin kurulu olduğundan emin olun. Bunu şu komutları çalıştırarak kontrol edebilirsiniz:
```
node -v
```
```
npm -v
```

Eğer kurulu değillerse, şu komutlarla kurabilirsiniz:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Proje Dizininize Geçin:
Terminalde npm projenizin bulunduğu dizine gidin:
```
cd path/to/your/project
```

### Bağımlılıkları Yükleyin:
package.json dosyanızda listelenen tüm gerekli bağımlılıkları yüklemek için şu komutu çalıştırın:

```
npm install
```

### Demoyu Çalıştırın:
Bağımlılıklar yüklendikten sonra demo script’inizi çalıştırabilirsiniz. Bu genellikle package.json’daki scripts bölümünde belirtilir. Örneğin, demo script’inizin adı start ise şu komutu kullanabilirsiniz:

```
npm run build
```
```
npm run dev
```

### Demoya Erişim:
Demo bir web sunucusu içeriyorsa, Codespaces erişim için bir URL sağlar. Bildirime bakın veya URL’yi bulmak için Ports sekmesini kontrol edin.

**Not:** Modelin tarayıcıda önbelleğe alınması gerekir, bu yüzden yüklenmesi biraz zaman alabilir.

### RAG Demo
Markdown dosyasını yükleyin `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Dosyanızı Seçin:
Yüklemek istediğiniz belgeyi seçmek için “Dosya Seç” düğmesine tıklayın.

### Belgeyi Yükleyin:
Dosyanızı seçtikten sonra, RAG (Retrieval-Augmented Generation) için belgenizi yüklemek üzere “Yükle” düğmesine tıklayın.

### Sohbete Başlayın:
Belge yüklendikten sonra, belgenizin içeriğine dayalı olarak RAG kullanarak bir sohbet oturumu başlatabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.