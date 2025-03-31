<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-03-27T13:58:48+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "ru"
}
-->
# **Тонкая настройка Phi-3 с помощью Lora**

Тонкая настройка языковой модели Microsoft Phi-3 Mini с использованием [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) на пользовательском наборе данных с инструкциями для чата.

LoRA поможет улучшить понимание в диалогах и генерацию ответов.

## Пошаговое руководство по настройке Phi-3 Mini:

**Импорты и настройка**

Установка loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Начните с импорта необходимых библиотек, таких как datasets, transformers, peft, trl и torch. Настройте логирование для отслеживания процесса обучения.

Вы можете адаптировать некоторые слои, заменив их на аналоги, реализованные в loralib. На данный момент поддерживаются nn.Linear, nn.Embedding и nn.Conv2d. Также поддерживается MergedLinear для случаев, когда один nn.Linear представляет собой несколько слоев, например, в некоторых реализациях проекции внимания qkv (см. дополнительные заметки для подробностей).

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

Перед началом цикла обучения отметьте только параметры LoRA как обучаемые.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

При сохранении контрольной точки создайте state_dict, который содержит только параметры LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

При загрузке контрольной точки с использованием load_state_dict обязательно установите strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Теперь обучение может продолжаться как обычно.

**Гиперпараметры**

Определите два словаря: training_config и peft_config. training_config включает гиперпараметры для обучения, такие как скорость обучения, размер пакета и настройки логирования.

peft_config задает параметры, связанные с LoRA, такие как rank, dropout и тип задачи.

**Загрузка модели и токенизатора**

Укажите путь к предварительно обученной модели Phi-3 (например, "microsoft/Phi-3-mini-4k-instruct"). Настройте параметры модели, включая использование кэша, тип данных (bfloat16 для смешанной точности) и реализацию внимания.

**Обучение**

Тонкая настройка модели Phi-3 с использованием пользовательского набора данных с инструкциями для чата. Используйте настройки LoRA из peft_config для эффективной адаптации. Отслеживайте процесс обучения с помощью заданной стратегии логирования.

**Оценка и сохранение**

Оцените тонко настроенную модель. Сохраняйте контрольные точки во время обучения для дальнейшего использования.

**Примеры**
- [Узнайте больше с этим примером блокнота](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример скрипта тонкой настройки на Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример настройки с использованием Hugging Face Hub и LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Пример карточки модели Hugging Face - тонкая настройка с LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Пример настройки с использованием Hugging Face Hub и QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.