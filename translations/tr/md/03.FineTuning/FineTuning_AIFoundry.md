# Microsoft Foundry ile Phi-3'ü İnce Ayar Yapma

Microsoft Foundry kullanarak Microsoft'un Phi-3 Mini dil modelini nasıl ince ayar yapacağımızı keşfedelim. İnce ayar, Phi-3 Mini'yi belirli görevlere uyarlamanızı sağlar ve böylece modeli daha güçlü ve bağlama duyarlı hale getirir.

## Dikkat Edilmesi Gerekenler

- **Yetenekler:** Hangi modeller ince ayar yapılabilir? Temel model ne için ince ayar yapılabilir?
- **Maliyet:** İnce ayar için fiyatlandırma modeli nedir?
- **Özelleştirilebilirlik:** Temel modeli ne kadar ve hangi şekillerde değiştirebilirim?
- **Kolaylık:** İnce ayar nasıl yapılır – özel kod yazmam gerekir mi? Kendi işlem gücümü getirmem gerekir mi?
- **Güvenlik:** İnce ayar yapılmış modellerin güvenlik riskleri olduğu biliniyor – istenmeyen zararları önlemek için herhangi bir koruma mekanizması var mı?

![AIFoundry Models](../../../../translated_images/tr/AIFoundryModels.0e1b16f7d0b09b73.webp)

## İnce Ayar Hazırlığı

### Ön Koşullar

> [!NOTE]
> Phi-3 ailesi modeller için, kullandıkça öde modeli ince ayar seçeneği yalnızca **East US 2** bölgelerinde oluşturulan hub’lar ile kullanılabilir.

- Bir Azure aboneliği. Azure aboneliğiniz yoksa, başlamak için bir [ücretli Azure hesabı](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) oluşturun.

- Bir [AI Foundry projesi](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure rol tabanlı erişim kontrolleri (Azure RBAC), Microsoft Foundry içindeki işlemlere erişim vermek için kullanılır. Bu makaledeki adımları uygulamak için kullanıcı hesabınıza kaynak grubunda __Azure AI Developer rolü__ atanmış olmalıdır.

### Abonelik sağlayıcı kaydı

Aboneliğin `Microsoft.Network` kaynak sağlayıcısına kayıtlı olduğunu doğrulayın.

1. [Azure portalı](https://portal.azure.com)'na giriş yapın.
1. Sol menüden **Abonelikler**'i seçin.
1. Kullanmak istediğiniz aboneliği seçin.
1. Sol menüden **AI proje ayarları** > **Kaynak sağlayıcıları**'nı seçin.
1. **Microsoft.Network** kaynak sağlayıcılarının listesinde olup olmadığını onaylayın. Yoksa ekleyin.

### Veri hazırlığı

Modelinizi ince ayar yapmak için eğitim ve doğrulama verilerinizi hazırlayın. Eğitim ve doğrulama veri kümeleri, modelin nasıl çalışmasını istediğinize dair giriş ve çıkış örneklerinden oluşur.

Tüm eğitim örneklerinizin çıkarım için beklenen formata uygun olduğundan emin olun. Modelleri etkili bir şekilde ince ayar yapmak için dengeli ve çeşitli bir veri setine sahip olun.

Bu, veri dengesini korumak, çeşitli senaryoları dahil etmek ve eğitim verilerini zaman içinde gerçek dünyadaki beklentilere uyacak şekilde düzenli olarak iyileştirmeyi içerir; böylece daha doğru ve dengeli model yanıtları elde edilir.

Farklı model türleri farklı eğitim veri formatları gerektirir.

### Sohbet Tamamlama

Kullanacağınız eğitim ve doğrulama verileri **JSON Lines (JSONL)** formatında olmalıdır. `Phi-3-mini-128k-instruct` için ince ayar veri kümesi, Sohbet tamamlama API'si tarafından kullanılan konuşma formatında hazırlanmalıdır.

### Örnek dosya formatı

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```
  
Desteklenen dosya türü JSON Lines’dır. Dosyalar varsayılan veri depolama alanına yüklenir ve projenizde kullanılabilir hale getirilir.

## Microsoft Foundry ile Phi-3'ü İnce Ayar Yapma

Microsoft Foundry, büyük dil modellerini kişisel veri setlerinize uyarlamanıza olanak sağlayan bir süreç olan ince ayar yapmayı mümkün kılar. İnce ayar, belirli görev ve uygulamalar için özelleştirme ve optimizasyon sunarak önemli değer sağlar. Bu, performans artışı, maliyet verimliliği, gecikmenin azalması ve istenilen çıktılara ulaşılması ile sonuçlanır.

![Finetune AI Foundry](../../../../translated_images/tr/AIFoundryfinetune.193aaddce48d553c.webp)

### Yeni Proje Oluşturma

1. [Microsoft Foundry](https://ai.azure.com)'e giriş yapın.

1. Microsoft Foundry içinde yeni proje oluşturmak için **+Yeni proje** seçeneğini tıklayın.

    ![FineTuneSelect](../../../../translated_images/tr/select-new-project.cd31c0404088d7a3.webp)

1. Aşağıdaki işlemleri gerçekleştirin:

    - Proje **Hub adı**. Benzersiz bir değer olmalıdır.
    - Kullanılacak **Hub** seçin (gerekirse yeni oluşturun).

    ![FineTuneSelect](../../../../translated_images/tr/create-project.ca3b71298b90e420.webp)

1. Yeni bir hub oluşturmak için aşağıdaki işlemleri yapın:

    - **Hub adı** girin. Benzersiz bir değer olmalıdır.
    - Azure **Aboneliğinizi** seçin.
    - Kullanılacak **Kaynak grubunu** seçin (gerekirse yeni oluşturun).
    - Kullanmak istediğiniz **Konumu** seçin.
    - Kullanmak istediğiniz **Azure AI Servislerini Bağla** seçeneğini belirleyin (gerekirse yeni oluşturun).
    - **Azure AI Arama Bağlantısını** **Bağlantıyı atla** olarak seçin.

    ![FineTuneSelect](../../../../translated_images/tr/create-hub.49e53d235e80779e.webp)

1. **İleri**'yi seçin.
1. **Bir proje oluştur**'u seçin.

### Veri Hazırlığı

İnce ayar öncesi, görevle ilgili bir veri seti toplayın veya oluşturun; örneğin sohbet talimatları, soru-cevap çiftleri veya diğer uygun metin verileri. Veriyi gürültüden arındırın, eksik değerleri yönetin ve metni tokenize edin.

### Microsoft Foundry'de Phi-3 modellerini ince ayar yapma

> [!NOTE]
> Phi-3 modellerinin ince ayarı şu anda yalnızca East US 2 bölgelerindeki projelerde desteklenmektedir.

1. Sol yan sekmeden **Model kataloğu**nu seçin.

1. **Arama çubuğuna** *phi-3* yazın ve kullanmak istediğiniz phi-3 modelini seçin.

    ![FineTuneSelect](../../../../translated_images/tr/select-model.60ef2d4a6a3cec57.webp)

1. **İnce Ayar**'ı seçin.

    ![FineTuneSelect](../../../../translated_images/tr/select-finetune.a976213b543dd9d8.webp)

1. **İnce ayar yapılmış model adı** girin.

    ![FineTuneSelect](../../../../translated_images/tr/finetune1.c2b39463f0d34148.webp)

1. **İleri**'yi seçin.

1. Aşağıdakileri yapın:

    - Görev türü olarak **Sohbet tamamlama**'yı seçin.
    - Kullanmak istediğiniz **Eğitim verisini** seçin. Microsoft Foundry verisi veya yerel ortamınızdan yükleyebilirsiniz.

    ![FineTuneSelect](../../../../translated_images/tr/finetune2.43cb099b1a94442d.webp)

1. **İleri**'yi seçin.

1. Kullanmak istediğiniz **Doğrulama verisini** yükleyin veya **Eğitim verisinin otomatik bölünmesini** seçin.

    ![FineTuneSelect](../../../../translated_images/tr/finetune3.fd96121b67dcdd92.webp)

1. **İleri**'yi seçin.

1. Aşağıdakileri yapın:

    - Kullanmak istediğiniz **Batch boyutu çarpanını** seçin.
    - Kullanmak istediğiniz **Öğrenme oranını** seçin.
    - Kullanmak istediğiniz **Epok sayısını** seçin.

    ![FineTuneSelect](../../../../translated_images/tr/finetune4.e18b80ffccb5834a.webp)

1. İnce ayar sürecini başlatmak için **Gönder**'i seçin.

    ![FineTuneSelect](../../../../translated_images/tr/select-submit.0a3802d581bac271.webp)

1. Modeliniz ince ayar yapıldıktan sonra durumu aşağıdaki resimde gösterildiği gibi **Tamamlandı** olarak görünür. Artık modeli dağıtabilir ve kendi uygulamanızda, uygulama alanında veya prompt flow'da kullanabilirsiniz. Daha fazla bilgi için bkz. [Microsoft Foundry ile Phi-3 ailesi küçük dil modellerini dağıtma](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/tr/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Phi-3 modellerini ince ayar yapma ile ilgili daha detaylı bilgi için lütfen [Microsoft Foundry'de Phi-3 modellerini ince ayar yapma](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini) sayfasını ziyaret edin.

## İnce ayar yapılmış modellerinizi temizleme

İnce ayar modeli listesinden veya model detay sayfasından bir ince ayar yapılmış modeli silebilirsiniz. İnce ayar sayfasından silmek istediğiniz modeli seçin ve ardından modelin silinmesi için Sil düğmesini tıklayın.

> [!NOTE]
> Mevcut bir dağıtımı olan özel modeli silemezsiniz. Önce model dağıtımınızı silmeniz gerekir ki özel modelinizi silebilesiniz.

## Maliyet ve kota

### Hizmet olarak ince ayar yapılan Phi-3 modeller için maliyet ve kota

Hizmet olarak ince ayar yapılmış Phi modelleri Microsoft tarafından sunulur ve Microsoft Foundry ile entegre edilmiştir. Modellerin fiyatlandırmasını, modelleri [dağıtırken](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) veya ince ayar yaparken Dağıtım sihirbazındaki Fiyatlandırma ve koşullar sekmesinde bulabilirsiniz.

## İçerik filtreleme

Kullandıkça öde ile hizmet olarak dağıtılan modeller Azure AI İçerik Güvenliği tarafından korunur. Gerçek zamanlı uç noktalara dağıtıldığında, bu özelliği devre dışı bırakabilirsiniz. Azure AI içerik güvenliği etkinken hem istem hem de tamamlamalar, zararlı içerik üretimini tespit ve önlemek için sınıflandırma modellerinden oluşan bir toplu incelemeden geçer. İçerik filtre sistemi, girdi istemlerinde ve çıktı tamamlamalarında potansiyel zararlı içerik kategorilerini algılar ve işlem yapar. Daha fazla bilgi için bkz. [Azure AI İçerik Güvenliği](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**İnce Ayar Yapılandırması**

Hiperparametreler: Öğrenme oranı, batch boyutu ve eğitim epok sayısı gibi hiperparametreleri tanımlayın.

**Kayıp Fonksiyonu**

Görevinize uygun bir kayıp fonksiyonu seçin (ör. çapraz entropi).

**Optimizatör**

Eğitim sırasında gradyan güncellemeleri için bir optimizatör seçin (ör. Adam).

**İnce Ayar Süreci**

- Önceden Eğitilmiş Modeli Yükleyin: Phi-3 Mini kontrol noktasını yükleyin.
- Özel Katmanlar Ekleyin: Görev özel katmanları ekleyin (ör. sohbet talimatları için sınıflandırma başlığı).

**Modeli Eğitin**
Hazırladığınız veri seti ile modeli ince ayar yapın. Eğitim ilerlemesini izleyin ve gerekirse hiperparametreleri ayarlayın.

**Değerlendirme ve Doğrulama**

Doğrulama Seti: Verinizi eğitim ve doğrulama setlerine bölün.

**Performansı Değerlendirin**

Doğruluk, F1-skora ya da perplexity gibi metriklerle model performansını ölçün.

## İnce Ayar Yapılmış Modeli Kaydetme

**Kontrol Noktası**
İnce ayar yapılmış model kontrol noktasını sonraki kullanımlar için kaydedin.

## Dağıtım

- Web Hizmeti Olarak Dağıtın: İnce ayar yapılmış modelinizi Microsoft Foundry’de web hizmeti olarak dağıtın.
- Uç Noktayı Test Edin: Dağıtılmış uç noktaya test sorguları göndererek işlevselliğini doğrulayın.

## Tekrarlayın ve İyileştirin

Tekrar: Performans tatmin edici değilse hiperparametre ayarları yaparak, daha fazla veri ekleyerek ya da ek epok ince ayar yaparak süreci tekrarlayın.

## İzleyin ve İyileştirin

Model davranışını sürekli izleyin ve gerektiğinde iyileştirin.

## Özelleştirin ve Genişletin

Özel Görevler: Phi-3 Mini, sohbet talimatlarının ötesinde çeşitli görevler için ince ayar yapılabilir. Diğer kullanım alanlarını keşfedin!  
Deneyler: Performansı artırmak için farklı mimariler, katman kombinasyonları ve teknikler deneyin.

> [!NOTE]
> İnce ayar yinelemeli bir süreçtir. Deneyin, öğrenin ve modelinizi göreviniz için en iyi sonuçları elde edecek şekilde uyarlayın!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak tercüme edilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde otoriter kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi tavsiye edilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->