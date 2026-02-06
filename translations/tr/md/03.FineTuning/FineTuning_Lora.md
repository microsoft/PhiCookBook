# **Phi-3'ü Lora ile İnce Ayar Yapma**

Microsoft'un Phi-3 Mini dil modelini, özel bir sohbet talimat veri seti üzerinde [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) kullanarak ince ayar yapma.

LORA, konuşma anlayışını ve yanıt üretimini geliştirmeye yardımcı olacak.

## Phi-3 Mini'yi ince ayar yapmak için adım adım rehber:

**İçe Aktarmalar ve Kurulum**

loralib kurulumu

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets, transformers, peft, trl ve torch gibi gerekli kütüphaneleri içe aktararak başlayın.  
Eğitim sürecini takip etmek için logging ayarlarını yapın.

Bazı katmanları, loralib ile uygulanmış karşılıklarıyla değiştirerek uyarlamayı tercih edebilirsiniz. Şu anda sadece nn.Linear, nn.Embedding ve nn.Conv2d desteklenmektedir. Ayrıca, bazı dikkat qkv projeksiyonu uygulamalarında olduğu gibi, tek bir nn.Linear birden fazla katmanı temsil ettiğinde kullanılmak üzere MergedLinear desteğimiz de vardır (daha fazla bilgi için Ek Notlara bakınız).

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

Eğitim döngüsü başlamadan önce, sadece LoRA parametrelerini eğitilebilir olarak işaretleyin.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Bir checkpoint kaydederken, sadece LoRA parametrelerini içeren bir state_dict oluşturun.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict kullanarak checkpoint yüklerken, strict=False olarak ayarlamayı unutmayın.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Artık eğitim normal şekilde devam edebilir.

**Hiperparametreler**

İki sözlük tanımlayın: training_config ve peft_config. training_config, öğrenme hızı, batch boyutu ve logging ayarları gibi eğitim hiperparametrelerini içerir.

peft_config ise rank, dropout ve görev türü gibi LoRA ile ilgili parametreleri belirtir.

**Model ve Tokenizer Yükleme**

Önceden eğitilmiş Phi-3 modelinin yolunu belirtin (örneğin, "microsoft/Phi-3-mini-4k-instruct"). Model ayarlarını yapılandırın; önbellek kullanımı, veri tipi (karışık hassasiyet için bfloat16) ve dikkat uygulaması gibi.

**Eğitim**

Özel sohbet talimat veri seti kullanarak Phi-3 modelini ince ayar yapın. Verimli uyarlama için peft_config içindeki LoRA ayarlarını kullanın. Belirtilen logging stratejisi ile eğitim ilerlemesini izleyin.  
Değerlendirme ve Kaydetme: İnce ayarlanmış modeli değerlendirin.  
Eğitim sırasında daha sonra kullanmak üzere checkpoint’ler kaydedin.

**Örnekler**
- [Bu örnek not defteri ile Daha Fazla Bilgi Edinin](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python İnce Ayar Örneği](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub’da LORA ile İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Model Kartı Örneği - LORA İnce Ayar Örneği](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub’da QLORA ile İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.