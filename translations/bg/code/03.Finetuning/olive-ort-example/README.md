<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:34:24+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "bg"
}
-->
# Финна настройка на Phi3 с Olive

В този пример ще използвате Olive, за да:

1. Финна настроите LoRA адаптер за класифициране на фрази в категории Тъга, Радост, Страх, Изненада.
1. Слеете теглата на адаптера с базовия модел.
1. Оптимизирате и квантизирате модела в `int4`.

Ще ви покажем и как да използвате финно настроения модел с ONNX Runtime (ORT) Generate API.

> **⚠️ За финна настройка ще ви е необходим подходящ GPU - например A10, V100, A100.**

## 💾 Инсталиране

Създайте нов Python виртуален енвайрънмънт (например с `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

След това инсталирайте Olive и зависимостите за работния процес по финна настройка:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Финна настройка на Phi3 с Olive
[Olive конфигурационният файл](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) съдържа *workflow* със следните *стъпки*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Накратко, този работен процес ще:

1. Финно настрои Phi3 (за 150 стъпки, които можете да промените) с данните от [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Слее теглата на LoRA адаптера с базовия модел. Така ще получите един модел артефакт във формат ONNX.
1. ModelBuilder ще оптимизира модела за ONNX runtime *и* ще го квантизира в `int4`.

За да стартирате работния процес, изпълнете:

```bash
olive run --config phrase-classification.json
```

След като Olive приключи, оптимизираният `int4` финно настроен модел Phi3 ще е наличен в: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Интегриране на финно настроения Phi3 в приложението ви

За да стартирате приложението:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Отговорът трябва да е еднократна класификация на фразата (Sad/Joy/Fear/Surprise).

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия оригинален език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.