<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:03:33+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "tr"
}
-->
# Olive kullanarak Phi3'ü ince ayar yapma

Bu örnekte Olive kullanarak:

1. LoRA adaptörünü cümleleri Üzgün, Mutlu, Korku, Şaşkın olarak sınıflandırmak için ince ayar yapacaksınız.
1. Adaptör ağırlıklarını temel modele birleştireceksiniz.
1. Modeli `int4` formatında optimize edip kuantize edeceksiniz.

Ayrıca, ince ayar yapılmış modeli ONNX Runtime (ORT) Generate API kullanarak nasıl çıkarım yapacağınızı göstereceğiz.

> **⚠️ İnce ayar için uygun bir GPU'ya ihtiyacınız olacak - örneğin, A10, V100, A100.**

## 💾 Kurulum

Yeni bir Python sanal ortamı oluşturun (örneğin, `conda` kullanarak):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Sonra, Olive ve ince ayar iş akışı için gerekli bağımlılıkları yükleyin:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive kullanarak Phi3'ü ince ayar yapma
[Olive yapılandırma dosyası](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) aşağıdaki *iş akışı* ve *adımları* içerir:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Yüksek seviyede, bu iş akışı şunları yapacak:

1. Phi3'ü [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) verisi kullanarak (150 adım boyunca, değiştirebilirsiniz) ince ayar yapacak.
1. LoRA adaptör ağırlıklarını temel modele birleştirecek. Bu, ONNX formatında tek bir model dosyası elde etmenizi sağlar.
1. Model Builder, modeli ONNX runtime için optimize edecek *ve* modeli `int4` formatında kuantize edecek.

İş akışını çalıştırmak için:

```bash
olive run --config phrase-classification.json
```

Olive tamamlandığında, optimize edilmiş `int4` ince ayar yapılmış Phi3 modeliniz şu konumda olacaktır: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 İnce ayar yapılmış Phi3'ü uygulamanıza entegre edin

Uygulamayı çalıştırmak için:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Bu yanıt, cümlenin tek kelimelik sınıflandırması olmalıdır (Üzgün/Mutlu/Korku/Şaşkın).

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.