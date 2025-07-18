<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:17:14+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "tr"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## WebGPU ve RAG Desenini Gösteren Demo
Phi-3 Onnx Hosted model ile RAG Deseni, Retrieval-Augmented Generation yaklaşımını kullanarak Phi-3 modellerinin gücünü ONNX barındırma ile birleştirir ve verimli AI dağıtımları sağlar. Bu desen, alan spesifik görevler için modellerin ince ayarını yapmakta önemli bir rol oynar; kalite, maliyet etkinliği ve uzun bağlam anlama yeteneğini bir arada sunar. Azure AI’nin bir parçası olarak, çeşitli sektörlerin özelleştirme ihtiyaçlarına hitap eden, kolayca bulunabilen, denenebilen ve kullanılabilen geniş bir model seçkisi sunar. Phi-3 modelleri, Phi-3-mini, Phi-3-small ve Phi-3-medium dahil olmak üzere, Azure AI Model Kataloğu’nda mevcuttur ve kendi kendine yönetilen ya da HuggingFace ve ONNX gibi platformlar üzerinden ince ayar yapılıp dağıtılabilir; bu da Microsoft’un erişilebilir ve verimli AI çözümlerine olan bağlılığını gösterir.

## WebGPU Nedir
WebGPU, web tarayıcılarından doğrudan bir cihazın grafik işlem birimine (GPU) verimli erişim sağlamak için tasarlanmış modern bir web grafik API’sidir. WebGL’in halefi olarak tasarlanmış olup, birkaç önemli iyileştirme sunar:

1. **Modern GPU’larla Uyumluluk**: WebGPU, Vulkan, Metal ve Direct3D 12 gibi sistem API’lerini kullanarak çağdaş GPU mimarileriyle sorunsuz çalışacak şekilde geliştirilmiştir.
2. **Geliştirilmiş Performans**: Genel amaçlı GPU hesaplamalarını ve daha hızlı işlemleri destekler, bu da hem grafik işleme hem de makine öğrenimi görevleri için uygundur.
3. **Gelişmiş Özellikler**: Daha karmaşık ve dinamik grafik ve hesaplama iş yüklerine olanak tanıyan gelişmiş GPU yeteneklerine erişim sağlar.
4. **Azaltılmış JavaScript Yükü**: Daha fazla görevi GPU’ya devrederek JavaScript üzerindeki yükü önemli ölçüde azaltır, böylece daha iyi performans ve daha akıcı deneyimler sunar.

WebGPU şu anda Google Chrome gibi tarayıcılarda desteklenmekte olup, diğer platformlara desteğin genişletilmesi için çalışmalar devam etmektedir.

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

#### Bayraklar Sayfasına Gidin:
Adres çubuğuna `chrome://flags` yazın ve Enter’a basın.

#### Bayrağı Arayın:
Sayfanın üstündeki arama kutusuna 'enable-unsafe-webgpu' yazın.

#### Bayrağı Etkinleştirin:
Sonuçlar listesinden #enable-unsafe-webgpu bayrağını bulun.

Yanındaki açılır menüye tıklayın ve Etkin olarak seçin.

#### Tarayıcınızı Yeniden Başlatın:

Bayrağı etkinleştirdikten sonra değişikliklerin geçerli olması için tarayıcınızı yeniden başlatmanız gerekir. Sayfanın altındaki Yeniden Başlat düğmesine tıklayın.

- Linux için, tarayıcıyı `--enable-features=Vulkan` parametresiyle başlatın.  
- Safari 18 (macOS 15) varsayılan olarak WebGPU etkin.  
- Firefox Nightly’de adres çubuğuna about:config yazın ve `dom.webgpu.enabled` değerini true olarak ayarlayın.

### Microsoft Edge için GPU Ayarlama

Windows üzerinde Microsoft Edge için yüksek performanslı GPU ayarlamak için adımlar:

- **Ayarları Açın:** Başlat menüsüne tıklayın ve Ayarlar’ı seçin.  
- **Sistem Ayarları:** Sistem’e, ardından Görüntüle’ye gidin.  
- **Grafik Ayarları:** Aşağı kaydırın ve Grafik ayarları’na tıklayın.  
- **Uygulama Seçin:** “Tercih ayarlamak için bir uygulama seçin” altında Masaüstü uygulaması’nı seçin ve Gözat’a tıklayın.  
- **Edge’i Seçin:** Edge kurulum klasörüne gidin (genellikle `C:\Program Files (x86)\Microsoft\Edge\Application`) ve `msedge.exe` dosyasını seçin.  
- **Tercihi Ayarlayın:** Seçenekler’e tıklayın, Yüksek performans’ı seçin ve Kaydet’e tıklayın.  
Bu, Microsoft Edge’in daha iyi performans için yüksek performanslı GPU’nuzu kullanmasını sağlar.  
- Bu ayarların geçerli olması için bilgisayarınızı yeniden başlatın.

### Codespace’inizi Açın:
GitHub’daki depoya gidin.  
Kod butonuna tıklayın ve Codespaces ile Aç’ı seçin.

Henüz bir Codespace’iniz yoksa, Yeni codespace’e tıklayarak oluşturabilirsiniz.

**Not** Codespace’inizde Node Ortamı Kurulumu  
GitHub Codespace’ten npm demosu çalıştırmak, projenizi test etmek ve geliştirmek için harika bir yoldur. İşte başlamanıza yardımcı olacak adım adım rehber:

### Ortamınızı Kurun:
Codespace açıldıktan sonra Node.js ve npm’nin yüklü olduğundan emin olun. Bunu kontrol etmek için şunu çalıştırabilirsiniz:  
```
node -v
```  
```
npm -v
```

Yüklü değilse, şu komutlarla yükleyebilirsiniz:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Proje Dizininize Gidin:
Terminali kullanarak npm projenizin bulunduğu dizine gidin:  
```
cd path/to/your/project
```

### Bağımlılıkları Yükleyin:
package.json dosyanızda listelenen tüm gerekli bağımlılıkları yüklemek için şu komutu çalıştırın:  
```
npm install
```

### Demoyu Çalıştırın:
Bağımlılıklar yüklendikten sonra demo script’inizi çalıştırabilirsiniz. Bu genellikle package.json’daki scripts bölümünde belirtilir. Örneğin, demo script’iniz start ise şu komutu kullanabilirsiniz:  
```
npm run build
```  
```
npm run dev
```

### Demo’ya Erişim:
Demo bir web sunucusu içeriyorsa, Codespaces erişim için bir URL sağlar. Bildirimleri kontrol edin veya URL’yi bulmak için Ports sekmesine bakın.

**Not:** Modelin tarayıcıda önbelleğe alınması gerekir, bu yüzden yüklenmesi biraz zaman alabilir.

### RAG Demo  
RAG çözümünü tamamlamak için `intro_rag.md` markdown dosyasını yükleyin. Codespaces kullanıyorsanız, dosyayı `01.InferencePhi3/docs/` klasöründen indirebilirsiniz.

### Dosyanızı Seçin:  
Yüklemek istediğiniz belgeyi seçmek için “Choose File” butonuna tıklayın.

### Belgeyi Yükleyin:  
Dosyanızı seçtikten sonra, RAG (Retrieval-Augmented Generation) için belgenizi yüklemek üzere “Upload” butonuna tıklayın.

### Sohbete Başlayın:  
Belge yüklendikten sonra, belgenizin içeriğine dayalı olarak RAG kullanarak sohbet oturumuna başlayabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.