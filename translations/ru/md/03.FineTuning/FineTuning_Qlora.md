<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:16:38+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ru"
}
-->
**Тонкая настройка Phi-3 с помощью QLoRA**

Тонкая настройка языковой модели Phi-3 Mini от Microsoft с использованием [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA поможет улучшить понимание диалогов и генерацию ответов.

Чтобы загружать модели в 4-битном формате с помощью transformers и bitsandbytes, необходимо установить accelerate и transformers из исходников и убедиться, что у вас установлена последняя версия библиотеки bitsandbytes.

**Примеры**
- [Узнайте больше с помощью этого примерного ноутбука](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример скрипта тонкой настройки на Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример тонкой настройки с LORA через Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Пример тонкой настройки с QLORA через Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.