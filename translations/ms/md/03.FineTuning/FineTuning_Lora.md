# **Penalaan Halus Phi-3 dengan Lora**

Penalaan halus model bahasa Phi-3 Mini Microsoft menggunakan [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) pada set data arahan sembang tersuai.

LORA akan membantu meningkatkan pemahaman perbualan dan penjanaan respons.

## Panduan langkah demi langkah untuk menala halus Phi-3 Mini:

**Import dan Persediaan**

Memasang loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Mulakan dengan mengimport perpustakaan yang diperlukan seperti datasets, transformers, peft, trl, dan torch.  
Sediakan logging untuk menjejak proses latihan.

Anda boleh memilih untuk menyesuaikan beberapa lapisan dengan menggantikannya dengan padanan yang dilaksanakan dalam loralib. Kami hanya menyokong nn.Linear, nn.Embedding, dan nn.Conv2d buat masa ini. Kami juga menyokong MergedLinear untuk kes di mana satu nn.Linear mewakili lebih daripada satu lapisan, seperti dalam beberapa pelaksanaan projeksi qkv perhatian (rujuk Nota Tambahan untuk maklumat lanjut).

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

Sebelum gelung latihan bermula, tandakan hanya parameter LoRA sebagai boleh dilatih.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Apabila menyimpan checkpoint, hasilkan state_dict yang hanya mengandungi parameter LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Apabila memuatkan checkpoint menggunakan load_state_dict, pastikan tetapkan strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sekarang latihan boleh diteruskan seperti biasa.

**Hiperparameter**

Tentukan dua kamus: training_config dan peft_config. training_config merangkumi hiperparameter untuk latihan, seperti kadar pembelajaran, saiz batch, dan tetapan logging.

peft_config menentukan parameter berkaitan LoRA seperti rank, dropout, dan jenis tugasan.

**Memuatkan Model dan Tokenizer**

Nyatakan laluan ke model Phi-3 yang telah dilatih sebelumnya (contoh, "microsoft/Phi-3-mini-4k-instruct"). Konfigurasikan tetapan model, termasuk penggunaan cache, jenis data (bfloat16 untuk ketepatan bercampur), dan pelaksanaan perhatian.

**Latihan**

Tala halus model Phi-3 menggunakan set data arahan sembang tersuai. Gunakan tetapan LoRA dari peft_config untuk penyesuaian yang cekap. Pantau kemajuan latihan menggunakan strategi logging yang ditetapkan.  
Penilaian dan Penyimpanan: Nilai model yang telah ditala halus.  
Simpan checkpoint semasa latihan untuk kegunaan kemudian.

**Contoh**  
- [Ketahui Lebih Lanjut dengan nota contoh ini](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Contoh Skrip Penalaan Halus Python](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Contoh Penalaan Halus Hugging Face Hub dengan LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Contoh Kad Model Hugging Face - Contoh Penalaan Halus LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Contoh Penalaan Halus Hugging Face Hub dengan QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.