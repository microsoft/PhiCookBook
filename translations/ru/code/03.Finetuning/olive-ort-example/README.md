<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:01:07+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "ru"
}
-->
# Тонкая настройка Phi3 с помощью Olive

В этом примере вы используете Olive для:

1. Тонкой настройки адаптера LoRA для классификации фраз на Sad, Joy, Fear, Surprise.
1. Объединения весов адаптера с базовой моделью.
1. Оптимизации и квантизации модели в `int4`.

Мы также покажем, как выполнить инференс тонко настроенной модели с помощью ONNX Runtime (ORT) Generate API.

> **⚠️ Для тонкой настройки потребуется подходящая GPU — например, A10, V100, A100.**

## 💾 Установка

Создайте новое виртуальное окружение Python (например, с помощью `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Далее установите Olive и зависимости для процесса тонкой настройки:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Тонкая настройка Phi3 с помощью Olive
[Конфигурационный файл Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) содержит *workflow* с такими *этапами*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

В общих чертах, этот workflow выполнит:

1. Тонкую настройку Phi3 (150 шагов, можно изменить) на данных из [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Объединение весов адаптера LoRA с базовой моделью. В результате получится единый артефакт модели в формате ONNX.
1. Model Builder оптимизирует модель для ONNX runtime *и* выполнит квантизацию в `int4`.

Для запуска workflow выполните:

```bash
olive run --config phrase-classification.json
```

После завершения работы Olive, оптимизированная и тонко настроенная модель Phi3 в формате `int4` будет доступна по пути: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Интеграция тонко настроенной Phi3 в ваше приложение

Для запуска приложения выполните:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ответом будет одно слово — классификация фразы (Sad/Joy/Fear/Surprise).

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.