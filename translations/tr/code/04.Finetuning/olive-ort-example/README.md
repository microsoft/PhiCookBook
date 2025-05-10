<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:45:07+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "tr"
}
-->
# Olive kullanarak Phi3'ü ince ayarlama

Bu örnekte Olive'ı kullanarak:

1. LoRA adaptörünü cümleleri Üzgün, Neşeli, Korku, Şaşkın olarak sınıflandırmak için ince ayarlayacaksınız.  
1. Adaptör ağırlıklarını temel modele birleştireceksiniz.  
1. Modeli `int4` formatında optimize edip kuantize edeceksiniz.  

Ayrıca, ONNX Runtime (ORT) Generate API kullanarak ince ayarlanmış modeli nasıl çalıştıracağınızı göstereceğiz.

> **⚠️ İnce ayar için uygun bir GPU’ya ihtiyacınız olacak - örneğin, A10, V100, A100.**

## 💾 Kurulum

Yeni bir Python sanal ortamı oluşturun (örneğin, `conda` kullanarak):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Sonra, Olive ve ince ayar iş akışı için gereken bağımlılıkları yükleyin:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive kullanarak Phi3'ü ince ayarlama  
[Olive yapılandırma dosyası](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) şu *iş akışı* ve *adımları* içerir:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Yüksek seviyede, bu iş akışı şunları yapacak:

1. Phi3'ü (150 adım boyunca, değiştirilebilir) [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) verisiyle ince ayarlayacak.  
1. LoRA adaptör ağırlıklarını temel modele birleştirecek. Böylece ONNX formatında tek bir model dosyanız olacak.  
1. Model Builder, modeli ONNX runtime için optimize edecek *ve* modeli `int4` formatında kuantize edecek.  

İş akışını çalıştırmak için:

```bash
olive run --config phrase-classification.json
```

Olive tamamlandığında, optimize edilmiş `int4` formatındaki ince ayarlı Phi3 modeliniz şu dizinde hazır olacak: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 İnce ayarlı Phi3'ü uygulamanıza entegre edin

Uygulamayı çalıştırmak için:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Bu yanıt, cümlenin tek kelimelik sınıflandırması olmalıdır (Sad/Joy/Fear/Surprise).

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.