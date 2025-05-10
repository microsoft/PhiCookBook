<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:48:19+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "bg"
}
-->
# **Фина настройка на Phi-3 с Lora**

Фина настройка на езиковия модел Phi-3 Mini на Microsoft с помощта на [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) върху персонализиран набор от инструкции за чат.

LORA ще помогне за подобряване на разбирането в разговори и генерирането на отговори.

## Стъпка по стъпка как да направите фина настройка на Phi-3 Mini:

**Импорти и Настройка**

Инсталиране на loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Започнете с импортиране на необходимите библиотеки като datasets, transformers, peft, trl и torch.
Настройте логване, за да следите процеса на обучение.

Можете да изберете да адаптирате някои слоеве, като ги замените с еквиваленти, реализирани в loralib. В момента поддържаме само nn.Linear, nn.Embedding и nn.Conv2d. Също така поддържаме MergedLinear за случаи, когато един nn.Linear представя повече от един слой, например в някои реализации на проекцията на вниманието qkv (вижте Допълнителни бележки за повече информация).

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

Преди да започне цикълът на обучение, маркирайте само LoRA параметрите като трениращи се.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

При запазване на чекпойнт, генерирайте state_dict, който съдържа само LoRA параметрите.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

При зареждане на чекпойнт с load_state_dict, уверете се, че strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Сега обучението може да продължи както обикновено.

**Хиперпараметри**

Дефинирайте два речника: training_config и peft_config. training_config съдържа хиперпараметри за обучението, като скорост на учене, размер на партидата и настройки за логване.

peft_config определя LoRA-свързани параметри като rank, dropout и тип задача.

**Зареждане на Модел и Токенизатор**

Посочете пътя към предварително обучен модел Phi-3 (например "microsoft/Phi-3-mini-4k-instruct"). Конфигурирайте настройките на модела, включително използване на кеш, тип данни (bfloat16 за смесена прецизност) и имплементация на вниманието.

**Обучение**

Фина настройка на модела Phi-3 с помощта на персонализирания набор от инструкции за чат. Използвайте LoRA настройките от peft_config за ефективна адаптация. Следете напредъка на обучението чрез зададената стратегия за логване.  
Оценка и Запазване: Оценете фино настроения модел.  
Запазвайте чекпойнти по време на обучението за по-късна употреба.

**Примери**
- [Научете повече с този примерен тетрадка](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример за Python скрипт за фина настройка](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример за фина настройка с LORA в Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Примерен Model Card в Hugging Face - LORA фина настройка](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Пример за фина настройка с QLORA в Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни тълкувания, възникнали от използването на този превод.