<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:20:03+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ms"
}
-->
**Penalaan Halus Phi-3 dengan QLoRA**

Penalaan halus model bahasa Phi-3 Mini Microsoft menggunakan [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA akan membantu meningkatkan pemahaman perbualan dan penjanaan respons.

Untuk memuatkan model dalam 4bit dengan transformers dan bitsandbytes, anda perlu memasang accelerate dan transformers dari sumber serta pastikan anda mempunyai versi terkini perpustakaan bitsandbytes.

**Contoh**
- [Ketahui Lebih Lanjut dengan buku nota contoh ini](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Contoh Penalaan Halus Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Contoh Penalaan Halus Hugging Face Hub dengan LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Contoh Penalaan Halus Hugging Face Hub dengan QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.