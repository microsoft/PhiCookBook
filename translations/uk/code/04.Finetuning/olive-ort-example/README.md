<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-09T20:13:54+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "uk"
}
-->
# Тонке налаштування Phi3 за допомогою Olive

У цьому прикладі ви використаєте Olive, щоб:

1. Тонко налаштувати LoRA адаптер для класифікації фраз на Sad, Joy, Fear, Surprise.
1. Об’єднати ваги адаптера з базовою моделлю.
1. Оптимізувати та квантувати модель у `int4`.

Також ми покажемо, як робити інференс тонко налаштованої моделі за допомогою ONNX Runtime (ORT) Generate API.

> **⚠️ Для тонкого налаштування потрібен відповідний GPU, наприклад, A10, V100, A100.**

## 💾 Встановлення

Створіть нове віртуальне середовище Python (наприклад, за допомогою `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Далі встановіть Olive та залежності для процесу тонкого налаштування:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Тонке налаштування Phi3 за допомогою Olive
[Конфігураційний файл Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) містить *workflow* з такими *етапами*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

На високому рівні цей workflow виконає:

1. Тонке налаштування Phi3 (150 кроків, які можна змінити) на даних з [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Об’єднання ваг LoRA адаптера з базовою моделлю. В результаті отримаєте єдиний артефакт моделі у форматі ONNX.
1. Model Builder оптимізує модель для ONNX runtime *та* квантує її у `int4`.

Щоб запустити workflow, виконайте:

```bash
olive run --config phrase-classification.json
```

Після завершення Olive, оптимізована `int4` тонко налаштована модель Phi3 буде доступна за адресою: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Інтеграція тонко налаштованої Phi3 у ваш додаток

Щоб запустити додаток:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Відповідь має бути однословною класифікацією фрази (Sad/Joy/Fear/Surprise).

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.