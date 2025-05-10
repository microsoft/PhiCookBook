<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:47:21+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "bg"
}
-->
# Фина настройка на Phi3 с Olive

В този пример ще използвате Olive, за да:

1. Фина настройка на LoRA адаптер за класифициране на фрази в категории Тъга, Радост, Страх, Изненада.
1. Обедините теглата на адаптера с базовия модел.
1. Оптимизирате и квантизирате модела в `int4`.

Ще ви покажем и как да извършите инференс с фино настроения модел, използвайки ONNX Runtime (ORT) Generate API.

> **⚠️ За фина настройка ще ви е необходим подходящ GPU - например A10, V100, A100.**

## 💾 Инсталация

Създайте нов виртуален Python енвайрънмент (например с `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

След това инсталирайте Olive и зависимостите за фина настройка:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Фина настройка на Phi3 с Olive
[Olive конфигурационният файл](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) съдържа *workflow* със следните *етапи*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Накратко, този workflow ще:

1. Фино настрои Phi3 (за 150 стъпки, които можете да промените) с данните от [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Обедини теглата на LoRA адаптера с базовия модел, като по този начин получите един модел в ONNX формат.
1. ModelBuilder ще оптимизира модела за ONNX runtime *и* ще го квантизира в `int4`.

За да стартирате workflow-а, изпълнете:

```bash
olive run --config phrase-classification.json
```

След като Olive приключи, оптимизираният и фино настроен модел Phi3 в `int4` ще бъде наличен в: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Интегриране на фино настроения Phi3 във вашето приложение

За да стартирате приложението:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Отговорът трябва да бъде еднократна дума, класифицираща фразата (Sad/Joy/Fear/Surprise).

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни тълкувания, произтичащи от използването на този превод.