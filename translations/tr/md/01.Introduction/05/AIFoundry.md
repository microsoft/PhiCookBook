# **Microsoft Foundry Kullanarak Değerlendirme**

![aistudo](../../../../../translated_images/tr/AIFoundry.9e0b513e999a1c5a.webp)

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) kullanarak üretken yapay zeka uygulamanızı nasıl değerlendireceğinizi öğrenin. Tek adımlı veya çok adımlı sohbetleri değerlendiriyor olsanız da, Microsoft Foundry model performansı ve güvenliği değerlendirmek için araçlar sunar.

![aistudo](../../../../../translated_images/tr/AIPortfolio.69da59a8e1eaa70f.webp)

## Microsoft Foundry ile Üretken Yapay Zeka Uygulamaları Nasıl Değerlendirilir
Daha ayrıntılı talimatlar için bkz. [Microsoft Foundry Belgeleri](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Başlamak için şu adımları izleyin:

## Microsoft Foundry'de Üretken Yapay Zeka Modellerini Değerlendirme

**Önkoşullar**

- CSV veya JSON formatında bir test veri seti.
- Dağıtılmış bir üretken yapay zeka modeli (Phi-3, GPT 3.5, GPT 4 veya Davinci modelleri gibi).
- Değerlendirmeyi çalıştırmak için bir hesaplama örneği içeren bir çalışma zamanı.

## Dahili Değerlendirme Ölçütleri

Microsoft Foundry hem tek adımlı hem de karmaşık çok adımlı sohbetleri değerlendirmenize olanak verir.  
Modelin belirli verilere dayandığı Retrieval Augmented Generation (RAG) senaryolarında, dahili değerlendirme ölçütleri ile performans değerlendirmesi yapabilirsiniz.  
Ayrıca genel tek adımlı soru-cevap senaryolarını (RAG olmayan) da değerlendirebilirsiniz.

## Değerlendirme Oturumu Oluşturma

Microsoft Foundry kullanıcı arayüzünden Değerlendir sayfasına veya Prompt Flow sayfasına gidin.  
Değerlendirme oluşturma sihirbazını takip ederek bir değerlendirme oturumu kurun. Değerlendirmenize isteğe bağlı bir isim verin.  
Uygulamanızın hedeflerine uygun senaryoyu seçin.  
Model çıkışını değerlendirmek için bir veya daha fazla değerlendirme ölçütü seçin.

## Özel Değerlendirme Akışı (İsteğe Bağlı)

Daha fazla esneklik için özel bir değerlendirme akışı oluşturabilirsiniz. Değerlendirme sürecini özel gereksinimlerinize göre özelleştirin.

## Sonuçları Görüntüleme

Değerlendirmeyi çalıştırdıktan sonra, Microsoft Foundry'de ayrıntılı değerlendirme ölçütlerini kaydedin, görüntüleyin ve analiz edin. Uygulamanızın yetenekleri ve sınırlamaları hakkında bilgi edinin.

**Not** Microsoft Foundry şu anda genel önizlemede olduğundan, deney ve geliştirme amaçları için kullanın. Üretim iş yükleri için diğer seçenekleri düşünün. Daha fazla detay ve adım adım talimatlar için resmi [AI Foundry belgelerini](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) inceleyin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermemize rağmen, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->