# **Microsoft Foundry'de Phi-3 Kullanımı**

Generative AI’nin gelişimi ile farklı LLM ve SLM, kurumsal veri entegrasyonu, ince ayar/RAG operasyonları ve bütünleşmiş LLM ve SLM sonrası farklı kurumsal işlerin değerlendirilmesi gibi işlemleri yönetmek için birleşik bir platform kullanılmasını umuyoruz; böylece generative AI Smart uygulamalar daha iyi hayata geçirilebilir. [Microsoft Foundry](https://ai.azure.com), kurumsal düzeyde generative AI uygulama platformudur.

![aistudo](../../../../translated_images/tr/aifoundry_home.f28a8127c96c7d93.webp)

Microsoft Foundry ile, büyük dil modeli (LLM) yanıtlarını değerlendirebilir ve daha iyi performans için prompt flow ile prompt uygulama bileşenlerini düzenleyebilirsiniz. Platform, kavram kanıtlarını tam işlevli üretime dönüştürmek için ölçeklenebilirlik sağlar. Sürekli izleme ve iyileştirme uzun vadeli başarıyı destekler.

Phi-3 modelini Microsoft Foundry üzerinde basit adımlarla hızlıca dağıtabilir, ardından Microsoft Foundry ile Phi-3 ile ilişkili Playground/Chat, ince ayar, değerlendirme ve diğer ilgili çalışmaları tamamlayabilirsiniz.

## **1. Hazırlık**

Makinenizde zaten [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) kuruluysa, bu şablonu kullanmak yeni bir dizinde bu komutu çalıştırmak kadar basittir.

## Manuel Oluşturma

Microsoft Foundry projesi ve hub'ı oluşturmak, AI çalışmalarınızı düzenlemek ve yönetmek için harika bir yoldur. İşte başlamanız için adım adım kılavuz:

### Microsoft Foundry'de Proje Oluşturma

1. **Microsoft Foundry'ye gidin**: Microsoft Foundry portalına giriş yapın.
2. **Proje Oluşturun**:
   - Eğer bir projedeyseniz, sayfanın sol üst kısmındaki "Microsoft Foundry" seçeneğine basarak Ana sayfaya gidin.
   - "+ Proje oluştur" seçeneğini seçin.
   - Proje için bir ad girin.
   - Eğer bir hub’ınız varsa, varsayılan olarak seçilecektir. Birden fazla hub’a erişiminiz varsa, açılır menüden farklı bir hub seçebilirsiniz. Yeni bir hub oluşturmak isterseniz, "Yeni hub oluştur" seçeneğini seçin ve bir isim verin.
   - "Oluştur" seçeneğini seçin.

### Microsoft Foundry'de Hub Oluşturma

1. **Microsoft Foundry'ye gidin**: Azure hesabınızla giriş yapın.
2. **Hub Oluşturun**:
   - Sol menüden Yönetim merkezini seçin.
   - "Tüm kaynaklar" seçeneğini, ardından "+ Yeni proje" yanındaki aşağı oka tıklayın ve "+ Yeni hub"ı seçin.
   - "Yeni bir hub oluştur" iletişim kutusunda, hub için bir ad girin (örneğin, contoso-hub) ve diğer alanları isteğinize göre düzenleyin.
   - "İleri"yi seçin, bilgileri gözden geçirin ve "Oluştur"u seçin.

Daha ayrıntılı talimatlar için resmi [Microsoft belgelerine](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects) bakabilirsiniz.

Başarıyla oluşturduktan sonra, oluşturduğunuz stüdyoya [ai.azure.com](https://ai.azure.com/) üzerinden erişebilirsiniz.

Tek bir AI Foundry üzerinde birden çok proje olabilir. Hazırlık için AI Foundry’de proje oluşturun.

Microsoft Foundry [Hızlı Başlangıçlar](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code) oluşturun.


## **2. Microsoft Foundry'de Phi modelini dağıtma**

Projede Explore seçeneğine tıklayarak Model Kataloğuna girin ve Phi-3’ü seçin

Phi-3-mini-4k-instruct modelini seçin

Phi-3-mini-4k-instruct modelini dağıtmak için 'Deploy'a tıklayın

> [!NOTE]
>
> Dağıtım sırasında hesaplama gücünü seçebilirsiniz

## **3. Microsoft Foundry'de Playground Chat Phi**

Dağıtım sayfasına gidin, Playground’u seçin ve Microsoft Foundry’nin Phi-3 modeli ile sohbet edin

## **4. Microsoft Foundry'den Model Dağıtımı**

Azure Model Kataloğundan model dağıtmak için şu adımları izleyebilirsiniz:

- Microsoft Foundry'e giriş yapın.
- Microsoft Foundry model kataloğundan dağıtmak istediğiniz modeli seçin.
- Modelin Detaylar sayfasında, Dağıt seçeneğini ve ardından Azure AI İçerik Güvenliği ile Sunucusuz API'yi seçin.
- Modellerinizi dağıtmak istediğiniz projeyi seçin. Sunucusuz API teklifini kullanmak için çalışma alanınızın East US 2 veya Sweden Central bölgesinde olması gerekir. Dağıtım adını özelleştirebilirsiniz.
- Dağıtım sihirbazında, fiyatlandırma ve kullanım koşullarını inceleyin.
- Dağıt’ı seçin. Dağıtım hazır hale gelene ve Dağıtımlar sayfasına yönlendirilene kadar bekleyin.
- Modelle etkileşime başlamak için playground’da Aç’ı seçin.
- Dağıtıma geri dönüp Dağıtımı seçebilir ve çağrıları yapmak veya tamamlamalar oluşturmak için kullanabileceğiniz hedef URL ve Gizli Anahtar bilgilerini not alabilirsiniz.
- Endpoint detayları, URL ve erişim anahtarlarını her zaman Oluştur sekmesinden ve Bileşenler bölümünden Dağıtımlar'a giderek bulabilirsiniz.

> [!NOTE]
> Bu adımları gerçekleştirebilmek için hesabınızın Kaynak Grubunda Azure AI Developer rolü izinlerine sahip olması gerektiğini unutmayın.

## **5. Microsoft Foundry'de Phi API'nin Kullanımı**

https://{Proje adınız}.region.inference.ml.azure.com/swagger.json adresine Postman GET ile erişebilir ve Key ile birlikte sağlanan arayüzleri öğrenebilirsiniz.

İstek parametrelerini çok kolayca alabilir, ayrıca yanıt parametrelerini inceleyebilirsiniz.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum farklılıklarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->