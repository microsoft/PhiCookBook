<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:47:24+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "tl"
}
-->
# **Fine-tuning ng Phi-3 gamit ang Lora**

Pag-fine-tune ng Microsoft Phi-3 Mini language model gamit ang [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) sa isang custom na chat instruction dataset.

Makakatulong ang LORA para mapabuti ang pag-unawa sa usapan at paggawa ng mga sagot.

## Hakbang-hakbang na gabay kung paano i-fine-tune ang Phi-3 Mini:

**Mga Import at Setup**

Pag-install ng loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Simulan sa pag-import ng mga kailangang library tulad ng datasets, transformers, peft, trl, at torch. I-set up ang logging para masubaybayan ang proseso ng training.

Pwede mong piliing i-adapt ang ilang layers sa pamamagitan ng pagpapalit nito sa mga katumbas na implementasyon sa loralib. Sa ngayon, sinusuportahan lang namin ang nn.Linear, nn.Embedding, at nn.Conv2d. Mayroon din kaming MergedLinear para sa mga kaso kung saan ang isang nn.Linear ay kumakatawan sa higit sa isang layer, tulad ng sa ilang implementasyon ng attention qkv projection (tingnan ang Additional Notes para sa karagdagang detalye).

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

Bago magsimula ang training loop, itakda na trainable lang ang mga LoRA parameters.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Kapag nagsa-save ng checkpoint, gumawa ng state_dict na naglalaman lang ng mga LoRA parameters.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Kapag naglo-load ng checkpoint gamit ang load_state_dict, siguraduhing naka-set ang strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Ngayon, puwede nang magpatuloy ang training gaya ng dati.

**Mga Hyperparameters**

Mag-define ng dalawang dictionaries: training_config at peft_config. Kasama sa training_config ang mga hyperparameters para sa training, gaya ng learning rate, batch size, at mga setting sa logging.

Ang peft_config naman ay naglalaman ng mga LoRA-related na parameters tulad ng rank, dropout, at task type.

**Pag-load ng Model at Tokenizer**

Itakda ang path papunta sa pre-trained na Phi-3 model (halimbawa, "microsoft/Phi-3-mini-4k-instruct"). I-configure ang mga setting ng model, kasama na ang paggamit ng cache, data type (bfloat16 para sa mixed precision), at implementasyon ng attention.

**Training**

I-fine-tune ang Phi-3 model gamit ang custom chat instruction dataset. Gamitin ang LoRA settings mula sa peft_config para sa mas epektibong adaptation. Subaybayan ang progreso ng training gamit ang itinakdang logging strategy.

**Evaluation at Pag-save:** Suriin ang fine-tuned na model. Mag-save ng mga checkpoints habang nagta-train para magamit sa susunod.

**Mga Sample**
- [Matuto Pa Gamit ang sample notebook na ito](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Halimbawa ng Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Halimbawa ng Hugging Face Hub Fine Tuning gamit ang LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Halimbawa ng Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Halimbawa ng Hugging Face Hub Fine Tuning gamit ang QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng salin na ito.