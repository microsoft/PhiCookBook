<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:09:45+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "tr"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## WebGPU ve RAG Desenini Tanıtmak İçin Demo

Phi-3.5 Onnx Hosted model ile RAG Deseni, Retrieval-Augmented Generation yaklaşımını kullanarak Phi-3.5 modellerinin gücünü ONNX barındırma ile birleştirir ve verimli yapay zeka uygulamaları sağlar. Bu desen, alanına özgü görevler için modellerin ince ayarını yapmakta önemli bir rol oynar; kalite, maliyet etkinliği ve uzun bağlam anlama yeteneğini bir arada sunar. Azure AI’nin bir parçası olarak, çeşitli sektörlerin özelleştirme ihtiyaçlarına hitap eden, kolayca bulunabilen, denenebilen ve kullanılabilen geniş bir model seçkisi sunar.

## WebGPU Nedir  
WebGPU, web tarayıcılarından doğrudan bir cihazın grafik işlem birimine (GPU) verimli erişim sağlamak için tasarlanmış modern bir web grafik API’sidir. WebGL’in halefi olarak düşünülmekte olup, birkaç önemli iyileştirme sunar:

1. **Modern GPU’larla Uyumluluk**: WebGPU, Vulkan, Metal ve Direct3D 12 gibi sistem API’lerini kullanarak güncel GPU mimarileriyle sorunsuz çalışacak şekilde tasarlanmıştır.
2. **Geliştirilmiş Performans**: Genel amaçlı GPU hesaplamalarını ve daha hızlı işlemleri destekler; hem grafik işleme hem de makine öğrenimi görevleri için uygundur.
3. **Gelişmiş Özellikler**: Daha karmaşık ve dinamik grafik ve hesaplama iş yüklerine olanak tanıyan ileri GPU yeteneklerine erişim sağlar.
4. **Azaltılmış JavaScript Yükü**: Daha fazla görevi GPU’ya devrederek JavaScript üzerindeki yükü önemli ölçüde azaltır, böylece daha iyi performans ve daha akıcı deneyimler sunar.

WebGPU şu anda Google Chrome gibi tarayıcılarda desteklenmekte olup, diğer platformlarda destek genişletme çalışmaları devam etmektedir.

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
- Safari 18 (macOS 15) WebGPU varsayılan olarak etkin.  
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
- Bu ayarların geçerli olması için **bilgisayarınızı yeniden başlatın**.

### Örnekler : Lütfen [bu bağlantıya tıklayın](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.