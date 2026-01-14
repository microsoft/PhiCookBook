<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:11:33+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "tr"
}
-->
## VS Code için AI Araç Setine Hoş Geldiniz

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main), Azure AI Studio Kataloğu ve Hugging Face gibi diğer kataloglardan çeşitli modelleri bir araya getirir. Araç seti, üretken AI araçları ve modelleriyle AI uygulamaları geliştirmek için yaygın geliştirme görevlerini şu şekilde kolaylaştırır:
- Model keşfi ve oyun alanı ile başlayın.
- Yerel hesaplama kaynakları kullanarak model ince ayarı ve çıkarım.
- Azure kaynakları kullanarak uzaktan ince ayar ve çıkarım.

[VSCode için AI Toolkit’i Yükleyin](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/tr/Aitoolkit.7157953df04812dc.png)

**[Private Preview]** Model ince ayarı ve çıkarımı bulutta çalıştırmak için Azure Container Apps’e tek tıkla kaynak sağlama.

Şimdi AI uygulama geliştirmeye geçelim:

- [VS Code için AI Araç Setine Hoş Geldiniz](../../../../md/03.FineTuning)
- [Yerel Geliştirme](../../../../md/03.FineTuning)
  - [Hazırlıklar](../../../../md/03.FineTuning)
  - [Conda’yı Aktifleştirme](../../../../md/03.FineTuning)
  - [Sadece Temel Model İnce Ayarı](../../../../md/03.FineTuning)
  - [Model İnce Ayarı ve Çıkarımı](../../../../md/03.FineTuning)
  - [Model İnce Ayarı](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [İnce Ayar Örnekleri ve Kaynaklar](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Uzaktan Geliştirme](../../../../md/03.FineTuning)
  - [Ön Koşullar](../../../../md/03.FineTuning)
  - [Uzaktan Geliştirme Projesi Kurulumu](../../../../md/03.FineTuning)
  - [Azure Kaynaklarını Sağlama](../../../../md/03.FineTuning)
  - [\[İsteğe Bağlı\] Huggingface Token’ını Azure Container App Secret’a Ekleme](../../../../md/03.FineTuning)
  - [İnce Ayarı Çalıştırma](../../../../md/03.FineTuning)
  - [Çıkarım Uç Noktası Sağlama](../../../../md/03.FineTuning)
  - [Çıkarım Uç Noktasını Dağıtma](../../../../md/03.FineTuning)
  - [Gelişmiş Kullanım](../../../../md/03.FineTuning)

## Yerel Geliştirme
### Hazırlıklar

1. Ana makinede NVIDIA sürücüsünün yüklü olduğundan emin olun.  
2. HF veri seti kullanıyorsanız `huggingface-cli login` komutunu çalıştırın.  
3. Bellek kullanımını değiştiren herhangi bir ayar için `Olive` anahtar ayarlarının açıklamalarını inceleyin.  

### Conda’yı Aktifleştirme
WSL ortamı kullandığımız ve paylaşılan bir ortam olduğu için conda ortamını manuel olarak aktifleştirmeniz gerekir. Bu adımdan sonra ince ayar veya çıkarım işlemlerini çalıştırabilirsiniz.

```bash
conda activate [conda-env-name] 
```

### Sadece Temel Model İnce Ayarı
Sadece temel modeli ince ayar yapmadan denemek isterseniz, conda’yı aktifleştirdikten sonra aşağıdaki komutu çalıştırabilirsiniz.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Model İnce Ayarı ve Çıkarımı

Çalışma alanı bir geliştirme konteynerinde açıldıktan sonra, bir terminal açın (varsayılan yol proje kök dizinidir) ve seçilen veri seti üzerinde bir LLM modelini ince ayar yapmak için aşağıdaki komutu çalıştırın.

```bash
python finetuning/invoke_olive.py 
```

Kontrol noktaları ve son model `models` klasöründe kaydedilecektir.

Sonrasında, ince ayarlı modeli kullanarak `console`, `web browser` veya `prompt flow` üzerinden sohbetlerle çıkarım yapabilirsiniz.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

VS Code’da `prompt flow` kullanmak için lütfen bu [Hızlı Başlangıç](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html) rehberine bakın.

### Model İnce Ayarı

Sonraki adımda, cihazınızda GPU bulunup bulunmamasına göre aşağıdaki modellerden birini indirin.

QLoRA kullanarak yerel ince ayar oturumunu başlatmak için kataloğumuzdan ince ayar yapmak istediğiniz modeli seçin.
| Platform(lar) | GPU mevcut | Model adı | Boyut (GB) |
|---------|---------|--------|--------|
| Windows | Evet | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Evet | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | Hayır | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Not_** Modelleri indirmek için Azure Hesabı gerekmez.

Phi3-mini (int4) modeli yaklaşık 2GB-3GB boyutundadır. Ağ hızınıza bağlı olarak indirme birkaç dakika sürebilir.

Öncelikle bir proje adı ve konumu seçin.  
Sonra model kataloğundan bir model seçin. Proje şablonunu indirmeniz istenecek. Ardından çeşitli ayarları yapmak için "Configure Project" butonuna tıklayabilirsiniz.

### Microsoft Olive

Kataloğumuzdaki PyTorch modeli üzerinde QLoRA ince ayarını çalıştırmak için [Olive](https://microsoft.github.io/Olive/why-olive.html) kullanıyoruz. Tüm ayarlar, ince ayar sürecini yerel olarak optimize edilmiş bellek kullanımıyla çalıştırmak için varsayılan değerlerle önceden yapılandırılmıştır, ancak senaryonuza göre ayarlanabilir.

### İnce Ayar Örnekleri ve Kaynaklar

- [İnce Ayara Başlarken Kılavuzu](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)  
- [HuggingFace Veri Seti ile İnce Ayar](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)  
- [Basit Veri Seti ile İnce Ayar](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)  

## **[Private Preview]** Uzaktan Geliştirme

### Ön Koşullar

1. Uzaktaki Azure Container App ortamınızda model ince ayarını çalıştırmak için aboneliğinizde yeterli GPU kapasitesi olduğundan emin olun. Uygulamanız için gereken kapasiteyi talep etmek üzere bir [destek talebi](https://azure.microsoft.com/support/create-ticket/) oluşturun. [GPU kapasitesi hakkında daha fazla bilgi alın](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)  
2. HuggingFace’de özel veri seti kullanıyorsanız, bir [HuggingFace hesabınızın](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) ve [erişim token’ınızın](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo) olduğundan emin olun.  
3. VS Code için AI Toolkit’te Uzaktan İnce Ayar ve Çıkarım özellik bayrağını etkinleştirin:  
   1. *File -> Preferences -> Settings* menüsünden VS Code Ayarlarını açın.  
   2. *Extensions* bölümüne gidin ve *AI Toolkit*’i seçin.  
   3. *"Enable Remote Fine-tuning And Inference"* seçeneğini işaretleyin.  
   4. Değişikliğin etkili olması için VS Code’u yeniden başlatın.

- [Uzaktan İnce Ayar](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Uzaktan Geliştirme Projesi Kurulumu
1. Komut paletinde `AI Toolkit: Focus on Resource View` komutunu çalıştırın.  
2. *Model Fine-tuning* bölümüne giderek model kataloğuna erişin. Projenize bir isim verin ve makinenizdeki konumunu seçin. Ardından *"Configure Project"* butonuna tıklayın.  
3. Proje Yapılandırması  
    1. *"Fine-tune locally"* seçeneğini etkinleştirmeyin.  
    2. Olive yapılandırma ayarları varsayılan değerlerle görünecektir. Gerekirse bu ayarları düzenleyin ve doldurun.  
    3. *Generate Project* aşamasına geçin. Bu aşama WSL kullanır ve yeni bir Conda ortamı kurar; gelecekte Dev Container güncellemeleri için hazırlık yapar.  
4. *"Relaunch Window In Workspace"* butonuna tıklayarak uzaktan geliştirme projenizi açın.

> **Not:** Proje şu anda AI Toolkit for VS Code içinde ya yerel ya da uzaktan çalışır. Proje oluştururken *"Fine-tune locally"* seçeneğini işaretlerseniz, proje sadece WSL içinde çalışır ve uzaktan geliştirme desteği olmaz. Eğer bu seçeneği işaretlemezseniz, proje sadece uzaktaki Azure Container App ortamında çalışır.

### Azure Kaynaklarını Sağlama
Uzaktan ince ayar için Azure Kaynağı sağlamak üzere komut paletinden `AI Toolkit: Provision Azure Container Apps job for fine-tuning` komutunu çalıştırın.

Sağlama işleminin ilerlemesini çıktı kanalında gösterilen bağlantı üzerinden takip edin.

### [İsteğe Bağlı] Huggingface Token’ını Azure Container App Secret’a Ekleme
Özel HuggingFace veri seti kullanıyorsanız, HuggingFace token’ınızı ortam değişkeni olarak ayarlayarak Hugging Face Hub’a manuel giriş yapma ihtiyacını ortadan kaldırabilirsiniz.  
Bunu `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning` komutuyla yapabilirsiniz. Bu komutla gizli adını [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) olarak belirleyip Hugging Face token’ınızı gizli değer olarak kullanabilirsiniz.

### İnce Ayarı Çalıştırma
Uzaktan ince ayar işini başlatmak için `AI Toolkit: Run fine-tuning` komutunu çalıştırın.

Sistem ve konsol günlüklerini görmek için çıktı panelindeki bağlantı üzerinden Azure portalına gidebilirsiniz ([Azure’da Günlükleri Görüntüleme ve Sorgulama](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure) rehberine bakınız).  
Ya da `AI Toolkit: Show the running fine-tuning job streaming logs` komutunu çalıştırarak VSCode çıktı panelinde konsol günlüklerini doğrudan görüntüleyebilirsiniz.  
> **Not:** Kaynak yetersizliği nedeniyle iş kuyruğa alınabilir. Günlükler görünmüyorsa, `AI Toolkit: Show the running fine-tuning job streaming logs` komutunu çalıştırın, biraz bekleyin ve tekrar çalıştırarak akış günlüklerine yeniden bağlanın.

Bu süreçte QLoRA ince ayar için kullanılacak ve çıkarım sırasında modelin kullanacağı LoRA adaptörleri oluşturulacaktır.  
İnce ayar sonuçları Azure Files’da saklanacaktır.

### Çıkarım Uç Noktası Sağlama
Adaptörler uzaktaki ortamda eğitildikten sonra, modelle etkileşim için basit bir Gradio uygulaması kullanılır.  
İnce ayar sürecine benzer şekilde, uzaktan çıkarım için Azure Kaynaklarını sağlamak üzere komut paletinden `AI Toolkit: Provision Azure Container Apps for inference` komutunu çalıştırın.

Varsayılan olarak, çıkarım için abonelik ve kaynak grubu ince ayarda kullanılanlarla aynı olmalıdır. Çıkarım, aynı Azure Container App Ortamını kullanacak ve ince ayar sırasında oluşturulan model ve model adaptörüne Azure Files üzerinden erişecektir.

### Çıkarım Uç Noktasını Dağıtma
Çıkarım kodunu güncellemek veya çıkarım modelini yeniden yüklemek isterseniz, `AI Toolkit: Deploy for inference` komutunu çalıştırın. Bu işlem en son kodunuzu Azure Container App ile senkronize eder ve replika’yı yeniden başlatır.

Dağıtım başarıyla tamamlandıktan sonra, VSCode bildiriminde görünen "*Go to Inference Endpoint*" butonuna tıklayarak çıkarım API’sine erişebilirsiniz.  
Ya da web API uç noktası `./infra/inference.config.json` içindeki `ACA_APP_ENDPOINT` altında ve çıktı panelinde bulunabilir. Artık bu uç noktayı kullanarak modeli değerlendirmeye hazırsınız.

### Gelişmiş Kullanım
AI Toolkit ile uzaktan geliştirme hakkında daha fazla bilgi için [Modelleri uzaktan ince ayarlama](https://aka.ms/ai-toolkit/remote-provision) ve [İnce ayarlı modelle çıkarım](https://aka.ms/ai-toolkit/remote-inference) dokümantasyonlarına bakabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.