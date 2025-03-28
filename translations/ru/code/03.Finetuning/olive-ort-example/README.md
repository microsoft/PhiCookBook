<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T03:42:28+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "ru"
}
-->
# Настройка Phi3 с помощью Olive

В этом примере вы будете использовать Olive для:

1. Настройки адаптера LoRA для классификации фраз на категории: Грусть, Радость, Страх, Удивление.
1. Объединения весов адаптера с базовой моделью.
1. Оптимизации и квантования модели в `int4`.

Мы также покажем, как выполнить инференс настроенной модели с использованием API Generate в ONNX Runtime (ORT).

> **⚠️ Для настройки потребуется подходящий GPU, например, A10, V100, A100.**

## 💾 Установка

Создайте новую виртуальную среду Python (например, с помощью `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Далее установите Olive и зависимости для выполнения настройки:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Настройка Phi3 с помощью Olive
[Файл конфигурации Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) содержит *рабочий процесс* с следующими *этапами*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

На высоком уровне этот рабочий процесс выполнит:

1. Настройку Phi3 (в течение 150 шагов, которые можно изменить) с использованием данных из [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Объединение весов адаптера LoRA с базовой моделью. В результате вы получите единый артефакт модели в формате ONNX.
1. Model Builder выполнит оптимизацию модели для ONNX Runtime *и* квантование модели в `int4`.

Чтобы выполнить рабочий процесс, запустите:

```bash
olive run --config phrase-classification.json
```

После завершения работы Olive оптимизированная настроенная модель Phi3 в формате `int4` будет доступна в: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Интеграция настроенной Phi3 в ваше приложение 

Чтобы запустить приложение:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ответ должен быть однословной классификацией фразы (Грусть/Радость/Страх/Удивление).

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.