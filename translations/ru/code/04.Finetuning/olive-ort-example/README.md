<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T04:00:51+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "ru"
}
-->
# Настройка Phi3 с помощью Olive

В этом примере вы будете использовать Olive для:

1. Настройки адаптера LoRA для классификации фраз на категории: Грусть, Радость, Страх, Удивление.
1. Объединения весов адаптера с базовой моделью.
1. Оптимизации и квантования модели в `int4`.

Мы также покажем, как использовать дообученную модель для вывода с помощью API Generate в ONNX Runtime (ORT).

> **⚠️ Для настройки потребуется подходящий GPU, например, A10, V100, A100.**

## 💾 Установка

Создайте новую виртуальную среду Python (например, используя `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Затем установите Olive и зависимости для рабочего процесса настройки:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Настройка Phi3 с помощью Olive

[Файл конфигурации Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) содержит *рабочий процесс* с следующими *этапами*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

На высоком уровне этот рабочий процесс выполняет:

1. Настройку Phi3 (150 шагов, которые можно изменить) с использованием данных из [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Объединение весов адаптера LoRA с базовой моделью. Это создаст единый артефакт модели в формате ONNX.
1. Model Builder оптимизирует модель для ONNX runtime *и* квантует модель в `int4`.

Чтобы запустить рабочий процесс, выполните:

```bash
olive run --config phrase-classification.json
```

После завершения работы Olive оптимизированная модель Phi3 в формате `int4` будет доступна здесь: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Интеграция настроенной Phi3 в ваше приложение

Чтобы запустить приложение:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ответ должен быть однословной классификацией фразы (Грусть/Радость/Страх/Удивление).

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, следует учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.