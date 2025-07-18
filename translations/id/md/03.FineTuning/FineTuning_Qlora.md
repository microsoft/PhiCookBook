<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:19:57+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "id"
}
-->
**Fine-tuning Phi-3 dengan QLoRA**

Fine-tuning model bahasa Phi-3 Mini dari Microsoft menggunakan [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA akan membantu meningkatkan pemahaman percakapan dan pembuatan respons.

Untuk memuat model dalam 4bit dengan transformers dan bitsandbytes, Anda harus menginstal accelerate dan transformers dari sumber serta memastikan Anda memiliki versi terbaru dari pustaka bitsandbytes.

**Contoh**
- [Pelajari Lebih Lanjut dengan notebook contoh ini](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Contoh FineTuning Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Contoh Fine Tuning Hugging Face Hub dengan LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Contoh Fine Tuning Hugging Face Hub dengan QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.