<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-03-27T15:08:56+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "ru"
}
-->
**Тонкая настройка Phi-3 с использованием QLoRA**

Тонкая настройка языковой модели Microsoft Phi-3 Mini с использованием [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA поможет улучшить понимание диалогов и генерацию ответов.

Чтобы загружать модели в формате 4bits с помощью transformers и bitsandbytes, необходимо установить accelerate и transformers из исходного кода, а также убедиться, что у вас установлена последняя версия библиотеки bitsandbytes.

**Примеры**
- [Узнайте больше с этим примером ноутбука](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример скрипта тонкой настройки на Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример тонкой настройки с LORA на Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Пример тонкой настройки с QLORA на Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, обратите внимание, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования этого перевода.