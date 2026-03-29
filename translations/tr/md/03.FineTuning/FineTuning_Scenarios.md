## İnce Ayar Senaryoları

![FineTuning with MS Services](../../../../translated_images/tr/FinetuningwithMS.3d0cec8ae693e094.webp)

Bu bölüm, Microsoft Foundry ve Azure ortamlarında ince ayar senaryolarına genel bir bakış sunar; dağıtım modelleri, altyapı katmanları ve yaygın olarak kullanılan optimizasyon teknikleri dahil.

**Platform**  
Bu, model yönetimi, orkestrasyon, deney takibi ve dağıtım iş akışları sağlayan Microsoft Foundry (eski adıyla Microsoft Foundry) ve Azure Machine Learning gibi yönetilen servisleri içerir.

**Altyapı**  
İnce ayar, ölçeklenebilir hesaplama kaynakları gerektirir. Azure ortamlarında, bu genellikle GPU tabanlı sanal makineler ve hafif iş yükleri için CPU kaynakları ile veri setleri ve kontrol noktaları için ölçeklenebilir depolamayı içerir.

**Araçlar ve Çerçeve**  
İnce ayar iş akışları genellikle Hugging Face Transformers, DeepSpeed ve PEFT (Parametre Verimli İnce Ayar) gibi çerçeveler ve optimizasyon kütüphanelerine dayanır.

Microsoft teknolojileri ile ince ayar süreci, platform servisleri, hesaplama altyapısı ve eğitim çerçevelerini kapsar. Bu bileşenlerin nasıl birlikte çalıştığını anlayarak, geliştiriciler temel modelleri belirli görevlere ve üretim senaryolarına etkin şekilde uyarlayabilir.

## Model Hizmet Olarak

Hesaplama oluşturma ve yönetme ihtiyacı olmadan, barındırılan ince ayar kullanarak modeli ince ayarlayın.

![MaaS Fine Tuning](../../../../translated_images/tr/MaaSfinetune.3eee4630607aff0d.webp)

Phi-3, Phi-3.5 ve Phi-4 model aileleri için sunucusuz ince ayar artık kullanılabilir; geliştiricilerin hesaplama düzenlemeden bulut ve uç senaryolar için modelleri hızlı ve kolayca özelleştirmesine olanak tanır.

## Platform Olarak Model

Kullanıcılar modellerini ince ayarlamak için kendi hesaplama kaynaklarını yönetir.

![Maap Fine Tuning](../../../../translated_images/tr/MaaPFinetune.fd3829c1122f5d1c.webp)

[İnce Ayar Örneği](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## İnce Ayar Teknikleri Karşılaştırması

|Senaryo|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Önceden eğitilmiş büyük dil modellerini belirli görev veya alanlara uyarlama|Evet|Evet|Evet|Evet|Evet|Evet|
|Metin sınıflandırma, adlandırılmış varlık tanıma ve makine çevirisi gibi NLP görevleri için ince ayar|Evet|Evet|Evet|Evet|Evet|Evet|
|Soru-cevap görevleri için ince ayar|Evet|Evet|Evet|Evet|Evet|Evet|
|Sohbet robotlarında insan benzeri cevaplar üretmek için ince ayar|Evet|Evet|Evet|Evet|Evet|Evet|
|Müzik, sanat veya diğer yaratıcılık formları üretmek için ince ayar|Evet|Evet|Evet|Evet|Evet|Evet|
|Hesaplama ve finansal maliyetlerin azaltılması|Evet|Evet|Evet|Evet|Evet|Evet|
|Bellek kullanımının azaltılması|Evet|Evet|Evet|Evet|Evet|Evet|
|Verimli ince ayar için daha az parametre kullanımı|Evet|Evet|Evet|Hayır|Hayır|Evet|
|Tüm GPU cihazlarının toplam GPU belleğine erişim sağlayan bellek-verimli veri paralelliği formu|Hayır|Hayır|Hayır|Evet|Evet|Hayır|

> [!NOTE]
> LoRA, QLoRA, PEFT ve DoRA parametre-verimli ince ayar yöntemleridir, DeepSpeed ve ZeRO ise dağıtık eğitim ve bellek optimizasyonuna odaklanır.

## İnce Ayar Performans Örnekleri

![Finetuning Performance](../../../../translated_images/tr/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlardan sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->