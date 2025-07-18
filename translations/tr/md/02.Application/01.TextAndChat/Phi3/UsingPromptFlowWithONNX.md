<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:00:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "tr"
}
-->
# Phi-3.5-Instruct ONNX ile Windows GPU kullanarak Prompt flow çözümü oluşturma

Aşağıdaki belge, Phi-3 modellerine dayalı yapay zeka uygulamaları geliştirmek için PromptFlow'u ONNX (Open Neural Network Exchange) ile nasıl kullanacağınıza dair bir örnektir.

PromptFlow, LLM tabanlı (Büyük Dil Modeli) yapay zeka uygulamalarının fikir aşamasından prototiplemeye, test ve değerlendirmeye kadar uçtan uca geliştirme döngüsünü kolaylaştırmak için tasarlanmış bir geliştirme araçları paketidir.

PromptFlow'u ONNX ile entegre ederek geliştiriciler:

- Model Performansını Optimize Edebilir: Verimli model çıkarımı ve dağıtımı için ONNX'ten yararlanabilir.
- Geliştirmeyi Basitleştirebilir: İş akışını yönetmek ve tekrarlayan görevleri otomatikleştirmek için PromptFlow'u kullanabilir.
- İş Birliğini Artırabilir: Birleşik bir geliştirme ortamı sağlayarak ekip üyeleri arasında daha iyi iş birliği kolaylaştırabilir.

**Prompt flow**, LLM tabanlı yapay zeka uygulamalarının fikir aşamasından prototipleme, test, değerlendirme, üretim dağıtımı ve izlemeye kadar uçtan uca geliştirme döngüsünü kolaylaştırmak için tasarlanmış bir geliştirme araçları paketidir. Prompt mühendisliğini çok daha kolay hale getirir ve üretim kalitesinde LLM uygulamaları oluşturmanızı sağlar.

Prompt flow, OpenAI, Azure OpenAI Service ve özelleştirilebilir modellerle (Huggingface, yerel LLM/SLM) bağlantı kurabilir. Phi-3.5'in kuantize edilmiş ONNX modelini yerel uygulamalara dağıtmayı hedefliyoruz. Prompt flow, işimizi daha iyi planlamamıza ve Phi-3.5 tabanlı yerel çözümleri tamamlamamıza yardımcı olabilir. Bu örnekte, Windows GPU tabanlı Prompt flow çözümünü tamamlamak için ONNX Runtime GenAI Kütüphanesi ile birleştireceğiz.

## **Kurulum**

### **Windows GPU için ONNX Runtime GenAI**

Windows GPU için ONNX Runtime GenAI'yi kurmak için bu kılavuzu okuyun [buraya tıklayın](./ORTWindowGPUGuideline.md)

### **VSCode'da Prompt flow kurulumu**

1. Prompt flow VS Code Eklentisini yükleyin

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.tr.png)

2. Prompt flow VS Code Eklentisini yükledikten sonra, eklentiye tıklayın ve **Installation dependencies** seçeneğini seçin, bu kılavuzu takip ederek ortamınıza Prompt flow SDK'yı kurun

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.tr.png)

3. [Örnek Kodu](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) indirin ve VS Code ile bu örneği açın

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.tr.png)

4. Python ortamınızı seçmek için **flow.dag.yaml** dosyasını açın

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.tr.png)

   Phi-3.5-instruct ONNX Model konumunuzu değiştirmek için **chat_phi3_ort.py** dosyasını açın

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.tr.png)

5. Prompt flow'u test etmek için çalıştırın

**flow.dag.yaml** dosyasını açın ve görsel editöre tıklayın

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.tr.png)

Buna tıkladıktan sonra çalıştırarak testi başlatın

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.tr.png)

1. Daha fazla sonuç kontrol etmek için terminalde toplu çalıştırma yapabilirsiniz


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Sonuçları varsayılan tarayıcınızda kontrol edebilirsiniz


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.tr.png)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.