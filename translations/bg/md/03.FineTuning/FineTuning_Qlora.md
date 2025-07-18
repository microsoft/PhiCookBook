<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:20:56+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "bg"
}
-->
**Фина настройка на Phi-3 с QLoRA**

Фина настройка на езиковия модел Phi-3 Mini на Microsoft с помощта на [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA ще помогне за подобряване на разбирането в разговори и генерирането на отговори.

За да заредите модели в 4 бита с transformers и bitsandbytes, трябва да инсталирате accelerate и transformers от източник и да се уверите, че имате най-новата версия на библиотеката bitsandbytes.

**Примери**
- [Научете повече с този примерен тетрадка](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример за Python скрипт за фина настройка](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример за фина настройка с LORA от Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Пример за фина настройка с QLORA от Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия първичен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.