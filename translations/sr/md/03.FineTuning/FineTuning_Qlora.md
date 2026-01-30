**Фино подешавање Phi-3 помоћу QLoRA**

Фино подешавање Microsoft-овог језичког модела Phi-3 Mini користећи [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA ће помоћи у побољшању разумевања разговора и генерисања одговора.

Да бисте учитали моделе у 4бита са transformers и bitsandbytes, потребно је да инсталирате accelerate и transformers из извора и да се уверите да имате најновију верзију bitsandbytes библиотеке.

**Примери**
- [Сазнајте више уз овај пример нотебука](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример Python скрипте за фино подешавање](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример фино подешавања са Hugging Face Hub користећи LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Пример фино подешавања са Hugging Face Hub користећи QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Одрицање одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.