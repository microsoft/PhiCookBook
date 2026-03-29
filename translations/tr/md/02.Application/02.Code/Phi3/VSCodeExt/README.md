# **Microsoft Phi-3 Ailesi ile Kendi Visual Studio Code GitHub Copilot Chat’inizi Oluşturun**

GitHub Copilot Chat'teki çalışma alanı ajanını kullandınız mı? Kendi ekibinizin kod ajanını oluşturmak ister misiniz? Bu uygulamalı laboratuvar, kurumsal düzeyde bir kod iş ajanı oluşturmak için açık kaynak modeli birleştirmeyi amaçlamaktadır.

## **Temel Bilgiler**

### **Neden Microsoft Phi-3 Tercih Edilmeli**

Phi-3, metin üretimi, diyalog tamamlama ve kod üretimi için farklı eğitim parametrelerine dayanan phi-3-mini, phi-3-small ve phi-3-medium'u içeren bir aile serisidir. Ayrıca Vision tabanlı phi-3-vision da vardır. Bu, işletmeler veya farklı ekipler için çevrimdışı üretken AI çözümleri oluşturmak için uygundur.

Bu bağlantıyı okumanız önerilir [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat uzantısı, VS Code içinde kodlama ile ilgili sorularınıza doğrudan yanıt almanızı sağlayan bir sohbet arayüzü sunar; belgeye göz atmanıza veya çevrimiçi forumlarda arama yapmanıza gerek kalmaz.

Copilot Chat, üretilen yanıta netlik katmak için sözdizimi vurgulama, girinti ve diğer biçimlendirme özelliklerini kullanabilir. Kullanıcıdan gelen sorunun türüne bağlı olarak, sonuç, yanıt üretmek için Copilot’un kullandığı kaynak kod dosyaları veya belgeler gibi bağlama bağlantıları veya VS Code işlevselliğine erişim için düğmeler içerebilir.

- Copilot Chat, geliştirici akışınıza entegre olur ve ihtiyacınız olan yerde size yardımcı olur:

- Kod yazarken yardım almak için editör veya terminalden doğrudan satır içi sohbet başlatın

- Chat görünümünde bir yapay zeka asistanına her zaman yanınızda sahip olun

- Hızlı Soru-Cevap özelliği ile çabuk sorular sorun ve kaldığınız yere dönün

GitHub Copilot Chat’i şu senaryolarda kullanabilirsiniz:

- Bir problemi en iyi şekilde çözme hakkında kodlama sorularını yanıtlamak

- Başkasının kodunu açıklamak ve geliştirme önerileri sunmak

- Kod düzeltme önerileri yapmak

- Birim test durumları oluşturmak

- Kod dokümantasyonu üretmek

Bu bağlantıyı okumanız önerilir [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat’te **@workspace** kullanmak, tüm kod tabanınızla ilgili sorular sormanızı sağlar. Sorulara bağlı olarak, Copilot ilgili dosyaları ve sembolleri akıllıca getirir ve ardından bunları yanıtında bağlantılar ve kod örnekleri olarak referans gösterir.

Sorunuza yanıt verirken, **@workspace** VS Code’da bir geliştiricinin kod tabanında gezinirken kullandığı aynı kaynaklarda arama yapar:

- .gitignore dosyası tarafından yok sayılan dosyalar hariç çalışma alanındaki tüm dosyalar

- İç içe klasör ve dosya adlarından oluşan dizin yapısı

- Çalışma alanı bir GitHub deposuysa ve kod arama tarafından dizinlendiyse GitHub'ın kod arama dizini

- Çalışma alanındaki semboller ve tanımlar

- Aktif editörde seçili metin veya görünen metin

Not: .gitignore, açık bir dosyanız varsa veya yok sayılan bir dosyada metin seçiliyse atlanır.

Bu bağlantıyı okumanız önerilir [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Bu Laboratuvar Hakkında Daha Fazla Bilgi**

GitHub Copilot, işletmelerin programlama verimliliğini büyük ölçüde artırdı ve her işletme GitHub Copilot’un ilgili işlevlerini özelleştirmek istiyor. Birçok işletme, kendi iş senaryoları ve açık kaynak modellerine dayanarak GitHub Copilot’a benzer Özelleştirilmiş Uzantılar oluşturdu. İşletmeler için özelleştirilmiş Uzantılar kontrolü kolaylaştırır, ancak bu aynı zamanda kullanıcı deneyimini etkiler. Sonuçta, GitHub Copilot genel senaryolar ve uzmanlıkta daha güçlü işlevlere sahiptir. Deneyim tutarlı tutulabilirse, işletmenin kendi Uzantısını özelleştirmesi daha iyi olur. GitHub Copilot Chat, işletmelerin sohbet deneyimini genişletmeleri için ilgili API’lar sağlar. Tutarlı bir deneyim sürdürmek ve özel işlevlere sahip olmak daha iyi bir kullanıcı deneyimidir.

Bu laboratuvar, Phi-3 modelini yerel NPU ve Azure hibriti ile birleştirerek GitHub Copilot Chat’te ***@PHI3*** adında özel bir Ajan oluşturur; kurumsal geliştiricilere kod üretimi tamamlamada ***(@PHI3 /gen)*** ve görüntü tabanlı kod üretiminde destek sağlar ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/tr/cover.1017ebc9a7c46d09.webp)

### ***Not:***

Bu laboratuvar şu anda Intel CPU ve Apple Silicon AIPC’lerinde uygulanmıştır. Qualcomm versiyonlu NPU üzerinde güncellemeler yapılmaya devam edilecektir.

## **Laboratuvar**


| İsim | Açıklama | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Kurulumlar(✅) | İlgili ortamları ve kurulum araçlarını yapılandırma ve kurma | [Git](./HOL/AIPC/01.Installations.md) |[Git](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini ile Prompt Akışını Çalıştırma (✅) | AIPC / Apple Silicon ile birlikte yerel NPU kullanarak Phi-3-mini ile kod üretimi oluşturma | [Git](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Git](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Phi-3-vision’u Azure Machine Learning Servisinde Dağıtma(✅) | Azure Machine Learning Servisinin Model Kataloğu - Phi-3-vision görüntüsünün dağıtımı ile kod üretme | [Git](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Git](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat’te @phi-3 ajanı oluşturma(✅)  | GitHub Copilot Chat’te kod üretimi, grafik üretimi kodu, RAG vb. tamamlamak için özel Phi-3 ajanı oluşturma | [Git](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Git](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Örnek Kod (✅)  | Örnek kod indir | [Git](../../../../../../../code/07.Lab/01/AIPC) | [Git](../../../../../../../code/07.Lab/01/Apple) |


## **Kaynaklar**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot hakkında daha fazla bilgi edinin [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat hakkında daha fazla bilgi edinin [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API hakkında daha fazla bilgi edinin [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry hakkında daha fazla bilgi edinin [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry Model Kataloğu hakkında daha fazla bilgi edinin [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi tavsiye edilir. Bu çevirinin kullanılması sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->