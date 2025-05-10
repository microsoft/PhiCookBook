<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:53:07+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ms"
}
-->
**Тонкая настройка Phi-3 с помощью QLoRA**

Тонкая настройка языковой модели Microsoft Phi-3 Mini с использованием [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA поможет улучшить понимание диалогов и генерацию ответов.

Для загрузки моделей в 4 бита с помощью transformers и bitsandbytes необходимо установить accelerate и transformers из исходников и убедиться, что у вас установлена последняя версия библиотеки bitsandbytes.

**Примеры**
- [Подробнее с этим примером ноутбука](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример Python скрипта для тонкой настройки](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример тонкой настройки с LORA через Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Пример тонкой настройки с QLORA через Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.