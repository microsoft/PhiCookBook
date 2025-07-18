<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:21:31+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "uk"
}
-->
**Тонке налаштування Phi-3 за допомогою QLoRA**

Тонке налаштування мовної моделі Phi-3 Mini від Microsoft із використанням [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA допоможе покращити розуміння діалогів та генерацію відповідей.

Щоб завантажувати моделі у 4 біти за допомогою transformers і bitsandbytes, потрібно встановити accelerate та transformers із джерела і переконатися, що у вас найновіша версія бібліотеки bitsandbytes.

**Приклади**
- [Дізнатись більше з цього зразка ноутбука](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Приклад тонкого налаштування на Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Приклад тонкого налаштування на Hugging Face Hub з LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Приклад тонкого налаштування на Hugging Face Hub з QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.