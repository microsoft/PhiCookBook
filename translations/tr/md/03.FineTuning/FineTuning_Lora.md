<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:45:29+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "tr"
}
-->
# **Phi-3 Mini'yi Lora ile İnce Ayar Yapma**

Microsoft'un Phi-3 Mini dil modelini, özel bir sohbet talimat veri seti üzerinde [LoRA (Düşük Dereceli Uyarlama)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) kullanarak ince ayar yapma.

LORA, sohbet anlayışını ve yanıt üretimini geliştirmeye yardımcı olacak.

## Phi-3 Mini'yi ince ayar yapmak için adım adım rehber:

**İçe Aktarma ve Kurulum**

loralib'in kurulumu

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets, transformers, peft, trl ve torch gibi gerekli kütüphaneleri içe aktararak başlayın.
Eğitim sürecini takip etmek için logging ayarlayın.

Bazı katmanları, loralib ile uygulanmış karşılıklarıyla değiştirerek uyarlamayı tercih edebilirsiniz. Şu anda sadece nn.Linear, nn.Embedding ve nn.Conv2d desteklenmektedir. Ayrıca, bazı attention qkv projeksiyon uygulamalarında olduğu gibi birden fazla katmanı temsil eden tek bir nn.Linear için MergedLinear desteğimiz de vardır (daha fazla bilgi için Ek Notlara bakınız).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Eğitim döngüsü başlamadan önce, yalnızca LoRA parametrelerini eğitim için işaretleyin.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Bir kontrol noktası kaydederken, yalnızca LoRA parametrelerini içeren bir state_dict oluşturun.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict kullanarak bir kontrol noktası yüklerken strict=False olarak ayarlamayı unutmayın.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Artık eğitim normal şekilde devam edebilir.

**Hiperparametreler**

İki sözlük tanımlayın: training_config ve peft_config. training_config, öğrenme hızı, batch boyutu ve logging ayarları gibi eğitim hiperparametrelerini içerir.

peft_config ise rank, dropout ve görev tipi gibi LoRA ile ilgili parametreleri belirtir.

**Model ve Tokenizer Yükleme**

Önceden eğitilmiş Phi-3 modelinin yolunu belirtin (örneğin, "microsoft/Phi-3-mini-4k-instruct"). Model ayarlarını, önbellek kullanımı, veri tipi (karma hassasiyet için bfloat16) ve attention uygulaması dahil olmak üzere yapılandırın.

**Eğitim**

Özel sohbet talimat veri setini kullanarak Phi-3 modelini ince ayar yapın. Verimli uyarlama için peft_config'ten LoRA ayarlarını kullanın. Belirtilen logging stratejisi ile eğitim ilerlemesini takip edin.
Değerlendirme ve Kaydetme: İnce ayarlanmış modeli değerlendirin.
Daha sonra kullanmak üzere eğitim sırasında kontrol noktalarını kaydedin.

**Örnekler**
- [Bu örnek defter ile Daha Fazla Bilgi Edinin](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning Örneği](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub'da LORA ile Fine Tuning Örneği](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Model Kartı Örneği - LORA Fine Tuning Örneği](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub'da QLORA ile Fine Tuning Örneği](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan dolayı sorumluluk kabul edilmemektedir.