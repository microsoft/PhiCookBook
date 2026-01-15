<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-16T15:52:35+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "tr"
}
-->
# Lab. Cihaz Üzerinde Çıkarım için AI Modellerini Optimize Etme

## Giriş

> [!IMPORTANT]  
> Bu laboratuvar için **Nvidia A10 veya A100 GPU** ve ilgili sürücüler ile CUDA araç seti (sürüm 12+) yüklü olmalıdır.

> [!NOTE]  
> Bu, OLIVE kullanarak cihaz üzerinde çıkarım için modelleri optimize etmenin temel kavramlarını uygulamalı olarak öğreneceğiniz **35 dakikalık** bir laboratuvardır.

## Öğrenme Hedefleri

Bu laboratuvarın sonunda OLIVE kullanarak:

- AWQ kuantizasyon yöntemiyle bir AI modelini kuantize edebileceksiniz.
- Belirli bir görev için AI modelini ince ayar yapabileceksiniz.
- ONNX Runtime üzerinde verimli cihaz içi çıkarım için LoRA adaptörleri (ince ayarlı model) oluşturabileceksiniz.

### Olive Nedir

Olive (*O*NNX *live*), ONNX runtime +++https://onnxruntime.ai+++ için modelleri kalite ve performansla teslim etmenizi sağlayan, CLI destekli bir model optimizasyon araç setidir.

![Olive Akışı](../../../../../translated_images/tr/olive-flow.a47985655a756dcb.webp)

Olive’a genellikle bir PyTorch veya Hugging Face modeli girdi olarak verilir ve çıktı olarak ONNX runtime üzerinde çalışan optimize edilmiş bir ONNX modeli elde edilir. Olive, Qualcomm, AMD, Nvidia veya Intel gibi donanım sağlayıcılarının sunduğu AI hızlandırıcılar (NPU, GPU, CPU) için modeli hedef cihaza göre optimize eder.

Olive, *workflow* adı verilen, sıralı model optimizasyon görevlerinden oluşan bir işlem yürütür. Bu görevler *passes* olarak adlandırılır; örnek olarak model sıkıştırma, grafik yakalama, kuantizasyon, grafik optimizasyonu verilebilir. Her pass, doğruluk ve gecikme gibi metrikleri optimize etmek için ayarlanabilen parametreler içerir. Olive, her pass’i tek tek veya bir grup olarak otomatik ayarlamak için bir arama algoritması kullanır.

#### Olive’ın Faydaları

- Grafik optimizasyonu, sıkıştırma ve kuantizasyon için farklı tekniklerle deneme-yanılma yaparken yaşanan **zaman kaybı ve sıkıntıyı azaltır**. Kalite ve performans kısıtlarınızı belirleyin, Olive en iyi modeli otomatik bulsun.
- Kuantizasyon, sıkıştırma, grafik optimizasyonu ve ince ayar alanlarında **40+ yerleşik model optimizasyon bileşeni**.
- Yaygın model optimizasyon görevleri için **kullanımı kolay CLI**. Örneğin, olive quantize, olive auto-opt, olive finetune.
- Model paketleme ve dağıtımı dahili olarak desteklenir.
- **Multi LoRA servisi** için model oluşturmayı destekler.
- Model optimizasyon ve dağıtım görevlerini düzenlemek için YAML/JSON ile workflow oluşturma.
- **Hugging Face** ve **Azure AI** entegrasyonu.
- **Maliyet tasarrufu** sağlayan yerleşik **önbellekleme** mekanizması.

## Laboratuvar Talimatları

> [!NOTE]  
> Azure AI Hub ve Projenizi oluşturduğunuzdan ve Lab 1’e göre A100 hesaplamanızı yapılandırdığınızdan emin olun.

### Adım 0: Azure AI Compute’a Bağlanma

Azure AI compute’a **VS Code**’un uzak bağlantı özelliği ile bağlanacaksınız.

1. Masaüstü **VS Code** uygulamanızı açın:  
2. **Shift+Ctrl+P** ile komut paletini açın  
3. Komut paletinde **AzureML - remote: Connect to compute instance in New Window** arayın  
4. Azure Aboneliğinizi, Kaynak Grubunuzu, Projenizi ve Lab 1’de oluşturduğunuz Compute adını seçerek bağlantıyı tamamlayın  
5. Bağlandıktan sonra, Visual Code’un sol alt köşesinde `><Azure ML: Compute Name` görünecektir

### Adım 1: Bu repoyu klonlayın

VS Code’da yeni bir terminal açmak için **Ctrl+J** kullanın ve bu repoyu klonlayın:

Terminalde şu istemi görmelisiniz:

```
azureuser@computername:~/cloudfiles/code$ 
```  
Çözümü klonlayın  

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Adım 2: VS Code’da Klasörü Açın

Terminalde aşağıdaki komutu çalıştırarak ilgili klasörde yeni bir VS Code penceresi açabilirsiniz:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternatif olarak, **Dosya** > **Klasör Aç** seçeneğiyle klasörü açabilirsiniz.

### Adım 3: Bağımlılıklar

Azure AI Compute Instance’ınızda VS Code terminali açın (ipuç: **Ctrl+J**) ve bağımlılıkları yüklemek için aşağıdaki komutları çalıştırın:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> Tüm bağımlılıkların kurulması yaklaşık 5 dakika sürecektir.

Bu laboratuvarda modelleri Azure AI Model kataloğuna indirip yükleyeceksiniz. Model kataloğuna erişmek için Azure’a giriş yapmanız gerekir:

```bash
az login
```

> [!NOTE]  
> Giriş sırasında aboneliğinizi seçmeniz istenecek. Laboratuvar için sağlanan aboneliği seçtiğinizden emin olun.

### Adım 4: Olive komutlarını çalıştırma

Azure AI Compute Instance’ınızda VS Code terminali açın (ipuç: **Ctrl+J**) ve `olive-ai` conda ortamının aktif olduğundan emin olun:

```bash
conda activate olive-ai
```

Sonra aşağıdaki Olive komutlarını çalıştırın.

1. **Veriyi inceleyin:** Bu örnekte, seyahatle ilgili soruları yanıtlamaya özel Phi-3.5-Mini modelini ince ayar yapacaksınız. Aşağıdaki kod, JSON lines formatındaki veri setinin ilk birkaç kaydını gösterir:

    ```bash
    head data/data_sample_travel.jsonl
    ```

2. **Modeli kuantize edin:** Modeli eğitmeden önce, Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ adlı bir teknik kullanan aşağıdaki komutla kuantize edersiniz. AWQ, çıkarım sırasında oluşan aktivasyonları dikkate alarak model ağırlıklarını kuantize eder. Bu sayede kuantizasyon süreci, aktivasyonlardaki gerçek veri dağılımını göz önünde bulundurarak, geleneksel ağırlık kuantizasyon yöntemlerine kıyasla model doğruluğunu daha iyi korur.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ kuantizasyonu tamamlanması **~8 dakika** sürer ve model boyutunu **~7.5GB’den ~2.5GB’ye düşürür**.

    Bu laboratuvarda Hugging Face’den (örneğin: `microsoft/Phi-3.5-mini-instruct`) model almayı gösteriyoruz. Ancak Olive, `model_name_or_path` argümanını Azure AI varlık kimliği ile güncelleyerek Azure AI kataloğundan model almanıza da olanak tanır (örneğin: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

3. **Modeli eğitin:** Sonra, `olive finetune` komutu kuantize edilmiş modeli ince ayar yapar. Modeli ince ayar yapmadan önce kuantize etmek, ince ayar sürecinin kuantizasyondan kaynaklanan kaybı kısmen telafi etmesi nedeniyle daha iyi doğruluk sağlar.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    İnce ayar (100 adımla) tamamlanması **~6 dakika** sürer.

4. **Optimize edin:** Model eğitildikten sonra, Olive’ın `auto-opt` komutunu kullanarak modeli optimize edin. Bu komut ONNX grafiğini yakalar ve modeli sıkıştırarak ve füzyonlar yaparak CPU performansını artırmak için otomatik optimizasyonlar gerçekleştirir. Başka cihazlar (NPU veya GPU gibi) için optimize etmek isterseniz `--device` ve `--provider` argümanlarını güncelleyebilirsiniz; ancak bu laboratuvarda CPU kullanacağız.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    Optimizasyon tamamlanması **~5 dakika** sürer.

### Adım 5: Model çıkarımını hızlı test etme

Model çıkarımını test etmek için klasörünüzde **app.py** adlı bir Python dosyası oluşturun ve aşağıdaki kodu yapıştırın:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Kodu şu şekilde çalıştırın:

```bash
python app.py
```

### Adım 6: Modeli Azure AI’ya yükleme

Modeli Azure AI model deposuna yüklemek, modelinizi geliştirme ekibinizle paylaşmanızı sağlar ve modelin sürüm kontrolünü yönetir. Modeli yüklemek için aşağıdaki komutu çalıştırın:

> [!NOTE]  
> `{}` yer tutucularını kaynak grubunuzun ve Azure AI Proje Adınızın isimleriyle güncelleyin.

Kaynak grubunuzu ve Azure AI Proje adınızı öğrenmek için şu komutu çalıştırın:

```
az ml workspace show
```

Ya da +++ai.azure.com+++ adresine gidip **management center** > **project** > **overview** seçeneğini kullanabilirsiniz.

`{}` yer tutucularını kaynak grubunuzun ve Azure AI Proje Adınızın isimleriyle güncelleyin.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Yüklediğiniz modeli https://ml.azure.com/model/list adresinde görebilir ve dağıtabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.