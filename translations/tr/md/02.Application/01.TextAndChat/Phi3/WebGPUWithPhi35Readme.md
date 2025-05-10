<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:57:26+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "tr"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## WebGPU ve RAG Desenini Gösteren Demo

Phi-3.5 Onnx Hosted modeli ile RAG Deseni, Retrieval-Augmented Generation yaklaşımını kullanarak Phi-3.5 modellerinin gücünü ONNX barındırma ile birleştirir ve verimli AI dağıtımları sağlar. Bu desen, alanına özgü görevler için modellerin ince ayar yapılmasında önemli rol oynar; kalite, maliyet etkinliği ve uzun bağlam anlama özelliklerini bir arada sunar. Azure AI’nin bir parçası olarak, çeşitli sektörlerin özelleştirme ihtiyaçlarına hitap eden, kolay bulunabilir, denenebilir ve kullanılabilir geniş bir model yelpazesi sağlar.

## WebGPU Nedir  
WebGPU, web tarayıcılarından doğrudan bir cihazın grafik işleme birimine (GPU) verimli erişim sağlamak için tasarlanmış modern bir web grafik API'sidir. WebGL’in halefi olarak düşünülür ve birkaç önemli geliştirme sunar:

1. **Modern GPU’larla Uyumluluk**: WebGPU, Vulkan, Metal ve Direct3D 12 gibi sistem API’lerini kullanarak çağdaş GPU mimarileriyle sorunsuz çalışacak şekilde tasarlanmıştır.
2. **Geliştirilmiş Performans**: Genel amaçlı GPU hesaplamalarını ve daha hızlı işlemleri destekler; hem grafik render hem de makine öğrenimi görevleri için uygundur.
3. **Gelişmiş Özellikler**: Daha karmaşık ve dinamik grafik ile hesaplama iş yüklerine olanak tanıyan ileri GPU yeteneklerine erişim sağlar.
4. **Azaltılmış JavaScript İş Yükü**: Daha fazla görevi GPU’ya devrederek JavaScript üzerindeki iş yükünü önemli ölçüde azaltır, bu da daha iyi performans ve daha akıcı deneyimler sağlar.

WebGPU şu anda Google Chrome gibi tarayıcılarda desteklenmekte olup, diğer platformlara destek genişletme çalışmaları devam etmektedir.

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

#### Bayraklar Sayfasına Erişim:  
Adres çubuğuna `chrome://flags` yazın ve Enter’a basın.

#### Bayrağı Arayın:  
Sayfanın üstündeki arama kutusuna 'enable-unsafe-webgpu' yazın.

#### Bayrağı Etkinleştirin:  
Sonuçlar listesindeki #enable-unsafe-webgpu bayrağını bulun.

Yanındaki açılır menüye tıklayın ve Enabled seçeneğini seçin.

#### Tarayıcınızı Yeniden Başlatın:  
Bayrağı etkinleştirdikten sonra değişikliklerin geçerli olması için tarayıcınızı yeniden başlatmanız gerekir. Sayfanın altındaki Relaunch butonuna tıklayın.

- Linux için, tarayıcıyı `--enable-features=Vulkan` ile başlatın.  
- Safari 18 (macOS 15) varsayılan olarak WebGPU etkin.  
- Firefox Nightly’de adres çubuğuna about:config yazın ve `set dom.webgpu.enabled to true`.

### Microsoft Edge için GPU Ayarları  

Windows üzerinde Microsoft Edge için yüksek performanslı GPU ayarlama adımları:

- **Ayarları Açın:** Başlat menüsüne tıklayın ve Ayarlar’ı seçin.  
- **Sistem Ayarları:** Sistem’e, ardından Görüntüle’ye gidin.  
- **Grafik Ayarları:** Aşağı kaydırın ve Grafik ayarları’na tıklayın.  
- **Uygulama Seçin:** “Tercih ayarlamak için bir uygulama seçin” altında Masaüstü uygulaması’nı seçin ve Gözat’a tıklayın.  
- **Edge’i Seçin:** Edge kurulum klasörüne gidin (genellikle `C:\Program Files (x86)\Microsoft\Edge\Application`) ve `msedge.exe` dosyasını seçin.  
- **Tercihi Ayarlayın:** Seçenekler’e tıklayın, Yüksek performans’ı seçin ve Kaydet’e basın.  
Bu, Microsoft Edge’in daha iyi performans için yüksek performanslı GPU’yu kullanmasını sağlar.  
- **Bilgisayarınızı Yeniden Başlatın** ayarların etkin olması için.

### Örnekler : Lütfen [bu bağlantıya tıklayın](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.