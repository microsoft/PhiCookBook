<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:47:54+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "cs"
}
-->
# **Тонкая настройка Phi-3 с помощью Lora**

Тонкая настройка языковой модели Phi-3 Mini от Microsoft с использованием [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) на кастомном наборе данных с инструкциями для чата.

LORA поможет улучшить понимание диалогов и генерацию ответов.

## Пошаговое руководство по тонкой настройке Phi-3 Mini:

**Импорты и настройка**

Установка loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Начните с импорта необходимых библиотек, таких как datasets, transformers, peft, trl и torch.
Настройте логирование для отслеживания процесса обучения.

Вы можете адаптировать некоторые слои, заменяя их аналогами из loralib. Пока поддерживаются только nn.Linear, nn.Embedding и nn.Conv2d. Также поддерживается MergedLinear для случаев, когда один nn.Linear представляет сразу несколько слоев, например, в некоторых реализациях проекции qkv внимания (см. Дополнительные заметки).

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

Перед началом цикла обучения отметьте для тренировки только параметры LoRA.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

При сохранении чекпоинта формируйте state_dict, содержащий только параметры LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

При загрузке чекпоинта через load_state_dict обязательно укажите strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Теперь обучение можно запускать как обычно.

**Гиперпараметры**

Определите два словаря: training_config и peft_config. training_config содержит гиперпараметры обучения, такие как скорость обучения, размер батча и настройки логирования.

peft_config задаёт параметры LoRA, включая ранг, dropout и тип задачи.

**Загрузка модели и токенизатора**

Укажите путь к предобученной модели Phi-3 (например, "microsoft/Phi-3-mini-4k-instruct"). Настройте параметры модели, включая использование кеша, тип данных (bfloat16 для смешанной точности) и реализацию внимания.

**Обучение**

Тонко настройте модель Phi-3 на кастомном наборе инструкций для чата. Используйте параметры LoRA из peft_config для эффективной адаптации. Отслеживайте процесс обучения с помощью заданной стратегии логирования.

**Оценка и сохранение:** Оцените тонко настроенную модель. Сохраняйте чекпоинты во время обучения для последующего использования.

**Примеры**
- [Подробнее с этим примером ноутбука](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример скрипта тонкой настройки на Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример тонкой настройки с LORA на Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Пример карточки модели Hugging Face - пример тонкой настройки с LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Пример тонкой настройки с QLORA на Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.