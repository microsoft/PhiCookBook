<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:47:16+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "ms"
}
-->
# **Настройка Phi-3 с помощью Lora**

Настройка языковой модели Phi-3 Mini от Microsoft с использованием [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) на основе пользовательского набора данных с инструкциями для чата.

LORA поможет улучшить понимание диалогов и генерацию ответов.

## Пошаговое руководство по настройке Phi-3 Mini:

**Импорты и настройка**

Установка loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Начните с импорта необходимых библиотек, таких как datasets, transformers, peft, trl и torch.  
Настройте логирование для отслеживания процесса обучения.

Вы можете выбрать адаптацию некоторых слоев, заменяя их на аналоги из loralib. На данный момент поддерживаются nn.Linear, nn.Embedding и nn.Conv2d. Также поддерживается MergedLinear для случаев, когда один nn.Linear представляет несколько слоев, например, в некоторых реализациях проекции qkv внимания (см. дополнительные примечания).

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

При сохранении контрольной точки формируйте state_dict, который содержит только параметры LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

При загрузке контрольной точки с помощью load_state_dict обязательно установите strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Теперь обучение можно продолжать в обычном режиме.

**Гиперпараметры**

Определите два словаря: training_config и peft_config. training_config содержит гиперпараметры обучения, такие как скорость обучения, размер батча и настройки логирования.

peft_config задаёт параметры, связанные с LoRA, например, ранг, dropout и тип задачи.

**Загрузка модели и токенизатора**

Укажите путь к предобученной модели Phi-3 (например, "microsoft/Phi-3-mini-4k-instruct"). Настройте параметры модели, включая использование кэша, тип данных (bfloat16 для смешанной точности) и реализацию внимания.

**Обучение**

Настраивайте модель Phi-3 на пользовательском наборе данных с инструкциями для чата. Используйте настройки LoRA из peft_config для эффективной адаптации. Следите за ходом обучения с помощью выбранной стратегии логирования.  
Оценка и сохранение: проведите оценку настроенной модели.  
Сохраняйте контрольные точки во время обучения для дальнейшего использования.

**Примеры**
- [Подробнее с этим примером ноутбука](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Пример Python скрипта для тонкой настройки](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Пример тонкой настройки с LORA на Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Пример карточки модели Hugging Face - пример тонкой настройки LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Пример тонкой настройки с QLORA на Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.