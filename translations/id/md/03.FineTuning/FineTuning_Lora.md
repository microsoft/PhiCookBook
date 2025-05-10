<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:47:08+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "id"
}
-->
# **Fine-tuning Phi-3 dengan Lora**

Fine-tuning model bahasa Phi-3 Mini dari Microsoft menggunakan [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) pada dataset instruksi chat kustom.

LORA akan membantu meningkatkan pemahaman percakapan dan pembuatan respons.

## Panduan langkah demi langkah cara fine-tune Phi-3 Mini:

**Imports dan Setup**

Menginstal loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Mulailah dengan mengimpor library yang diperlukan seperti datasets, transformers, peft, trl, dan torch.  
Siapkan logging untuk memantau proses pelatihan.

Anda dapat memilih untuk mengadaptasi beberapa layer dengan menggantinya menggunakan implementasi loralib. Saat ini kami hanya mendukung nn.Linear, nn.Embedding, dan nn.Conv2d. Kami juga mendukung MergedLinear untuk kasus di mana satu nn.Linear mewakili lebih dari satu layer, seperti pada beberapa implementasi proyeksi qkv attention (lihat Catatan Tambahan untuk informasi lebih lanjut).

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

Sebelum loop pelatihan dimulai, tandai hanya parameter LoRA yang dapat dilatih.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Saat menyimpan checkpoint, buat state_dict yang hanya berisi parameter LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Saat memuat checkpoint menggunakan load_state_dict, pastikan untuk mengatur strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sekarang pelatihan dapat dilanjutkan seperti biasa.

**Hyperparameter**

Tentukan dua dictionary: training_config dan peft_config. training_config berisi hyperparameter untuk pelatihan, seperti learning rate, batch size, dan pengaturan logging.

peft_config menentukan parameter terkait LoRA seperti rank, dropout, dan tipe tugas.

**Model dan Tokenizer Loading**

Tentukan path ke model Phi-3 yang sudah dilatih sebelumnya (misalnya, "microsoft/Phi-3-mini-4k-instruct"). Konfigurasikan pengaturan model, termasuk penggunaan cache, tipe data (bfloat16 untuk mixed precision), dan implementasi attention.

**Pelatihan**

Fine-tune model Phi-3 menggunakan dataset instruksi chat kustom. Gunakan pengaturan LoRA dari peft_config untuk adaptasi yang efisien. Pantau kemajuan pelatihan menggunakan strategi logging yang sudah ditentukan.  
Evaluasi dan Penyimpanan: Evaluasi model yang sudah di-fine-tune.  
Simpan checkpoint selama pelatihan untuk digunakan nanti.

**Contoh**  
- [Pelajari Lebih Lanjut dengan notebook contoh ini](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Contoh Sample FineTuning Python](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Contoh Fine Tuning Hugging Face Hub dengan LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Contoh Model Card Hugging Face - Sample Fine Tuning LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Contoh Fine Tuning Hugging Face Hub dengan QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.