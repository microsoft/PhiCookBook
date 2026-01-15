<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:41:16+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "tr"
}
-->
# **Azure Machine Learning Servisini Tanıtma**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo), makine öğrenimi (ML) proje yaşam döngüsünü hızlandırmak ve yönetmek için bulut tabanlı bir hizmettir.

ML uzmanları, veri bilimcileri ve mühendisler, günlük iş akışlarında şunları yapabilirler:

- Modelleri eğitmek ve dağıtmak.  
- Makine öğrenimi operasyonlarını (MLOps) yönetmek.  
- Azure Machine Learning’de bir model oluşturabilir veya PyTorch, TensorFlow ya da scikit-learn gibi açık kaynaklı platformlardan oluşturulmuş bir modeli kullanabilirsiniz.  
- MLOps araçları, modelleri izlemenize, yeniden eğitmenize ve yeniden dağıtmanıza yardımcı olur.

## Azure Machine Learning Kimler İçin?

**Veri Bilimcileri ve ML Mühendisleri**

Günlük iş akışlarını hızlandırmak ve otomatikleştirmek için araçları kullanabilirler.  
Azure ML, adalet, açıklanabilirlik, izleme ve denetlenebilirlik özellikleri sunar.

**Uygulama Geliştiricileri**

Modelleri uygulamalara veya hizmetlere sorunsuzca entegre edebilirler.

**Platform Geliştiricileri**

Dayanıklı Azure Resource Manager API’leri destekli güçlü araçlara erişimleri vardır.  
Bu araçlar, gelişmiş ML araçları geliştirmeye olanak tanır.

**Kurumlar**

Microsoft Azure bulutunda çalışan kurumlar, tanıdık güvenlik ve rol tabanlı erişim kontrolünden faydalanır.  
Korunan verilere ve belirli işlemlere erişimi kontrol etmek için projeler kurabilirler.

## Takımdaki Herkes İçin Verimlilik  
ML projeleri genellikle farklı beceri setlerine sahip bir ekip gerektirir.

Azure ML, size şu imkânları sağlar:  
- Paylaşılan not defterleri, hesaplama kaynakları, sunucusuz hesaplama, veri ve ortamlar aracılığıyla ekibinizle iş birliği yapabilirsiniz.  
- Adalet, açıklanabilirlik, izleme ve denetlenebilirlik özellikleriyle modeller geliştirebilir, soy ağacı ve denetim uyumluluğu gereksinimlerini karşılayabilirsiniz.  
- ML modellerini hızlı ve kolayca ölçeklendirebilir, MLOps ile etkin şekilde yönetip denetleyebilirsiniz.  
- Yerleşik yönetişim, güvenlik ve uyumluluk ile makine öğrenimi iş yüklerini her yerde çalıştırabilirsiniz.

## Platformlar Arası Uyumluluk Araçları

ML ekibindeki herkes, işi tamamlamak için tercih ettiği araçları kullanabilir.  
Hızlı deneyler yapıyor, hiperparametre ayarlaması yapıyor, boru hatları oluşturuyor veya çıkarımları yönetiyor olun, tanıdık arayüzleri kullanabilirsiniz:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST API’leri  

Modelleri geliştirirken ve geliştirme döngüsü boyunca iş birliği yaparken, Azure Machine Learning studio kullanıcı arayüzü içinde varlıkları, kaynakları ve metrikleri paylaşabilir ve bulabilirsiniz.

## **Azure ML’de LLM/SLM**

Azure ML, LLMOps ve SLMOps’u birleştirerek kurumsal çapta üretken yapay zeka teknolojisi platformu oluşturmak için birçok LLM/SLM ile ilgili işlev ekledi.

### **Model Kataloğu**

Kurumsal kullanıcılar, Model Kataloğu aracılığıyla farklı iş senaryolarına göre çeşitli modeller dağıtabilir ve Model as Service olarak kurumsal geliştiriciler veya kullanıcıların erişimine sunabilir.

![models](../../../../translated_images/tr/models.e6c7ff50a51806fd.png)

Azure Machine Learning studio’daki Model Kataloğu, üretken yapay zeka uygulamaları oluşturmanızı sağlayan geniş bir model yelpazesini keşfetmek ve kullanmak için merkezdir. Model kataloğu, Azure OpenAI servisi, Mistral, Meta, Cohere, Nvidia, Hugging Face gibi model sağlayıcılarının yanı sıra Microsoft tarafından eğitilmiş modeller dahil yüzlerce modeli içerir. Microsoft dışındaki sağlayıcılardan gelen modeller, Microsoft’un Ürün Şartları’nda tanımlandığı üzere Microsoft Dışı Ürünlerdir ve modelle birlikte sağlanan şartlara tabidir.

### **İş Boru Hattı**

Bir makine öğrenimi boru hattının temel amacı, tam bir makine öğrenimi görevini çok adımlı bir iş akışına bölmektir. Her adım, ayrı ayrı geliştirilebilen, optimize edilebilen, yapılandırılabilen ve otomatikleştirilebilen yönetilebilir bir bileşendir. Adımlar, iyi tanımlanmış arayüzlerle birbirine bağlanır. Azure Machine Learning boru hattı servisi, boru hattı adımları arasındaki tüm bağımlılıkları otomatik olarak koordine eder.

SLM / LLM ince ayarında, verilerimizi, eğitimi ve üretim süreçlerini Pipeline aracılığıyla yönetebiliriz.

![finetuning](../../../../translated_images/tr/finetuning.6559da198851fa52.png)

### **Prompt flow**

Azure Machine Learning prompt flow kullanmanın faydaları  
Azure Machine Learning prompt flow, kullanıcıların fikir aşamasından deneylere ve nihayetinde üretime hazır LLM tabanlı uygulamalara geçişini kolaylaştıran çeşitli avantajlar sunar:

**Prompt mühendisliğinde çeviklik**

Etkileşimli yazım deneyimi: Azure Machine Learning prompt flow, akış yapısının görsel bir temsilini sunar, böylece kullanıcılar projelerini kolayca anlayıp gezinebilir. Ayrıca, verimli akış geliştirme ve hata ayıklama için not defteri benzeri bir kodlama deneyimi sağlar.  
Prompt ayarlaması için varyantlar: Kullanıcılar birden çok prompt varyantı oluşturup karşılaştırabilir, yinelemeli iyileştirme sürecini kolaylaştırabilir.

Değerlendirme: Yerleşik değerlendirme akışları, kullanıcıların prompt ve akışlarının kalitesini ve etkinliğini ölçmesini sağlar.

Kapsamlı kaynaklar: Azure Machine Learning prompt flow, geliştirme için başlangıç noktası olan yerleşik araçlar, örnekler ve şablonlar kütüphanesi içerir; bu da yaratıcılığı teşvik eder ve süreci hızlandırır.

**LLM tabanlı uygulamalar için kurumsal hazır olma**

İş birliği: Azure Machine Learning prompt flow, birden çok kullanıcının prompt mühendisliği projelerinde birlikte çalışmasına, bilgi paylaşmasına ve sürüm kontrolü yapmasına olanak tanır.

Hepsi bir arada platform: Azure Machine Learning prompt flow, geliştirme ve değerlendirmeden dağıtım ve izlemeye kadar tüm prompt mühendisliği sürecini kolaylaştırır. Kullanıcılar, akışlarını Azure Machine Learning uç noktaları olarak zahmetsizce dağıtabilir ve performanslarını gerçek zamanlı izleyerek en iyi çalışmayı ve sürekli iyileştirmeyi sağlar.

Azure Machine Learning Kurumsal Hazır Olma Çözümleri: Prompt flow, Azure Machine Learning’in sağlam kurumsal hazır olma çözümlerinden yararlanarak, akışların geliştirilmesi, deneysel çalışmaları ve dağıtımı için güvenli, ölçeklenebilir ve güvenilir bir temel sunar.

Azure Machine Learning prompt flow ile kullanıcılar, prompt mühendisliği çevikliklerini ortaya çıkarabilir, etkili iş birliği yapabilir ve başarılı LLM tabanlı uygulama geliştirme ve dağıtımı için kurumsal düzeyde çözümlerden faydalanabilir.

Azure ML’in hesaplama gücü, veri ve farklı bileşenlerini birleştirerek, kurumsal geliştiriciler kendi yapay zeka uygulamalarını kolayca oluşturabilir.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.