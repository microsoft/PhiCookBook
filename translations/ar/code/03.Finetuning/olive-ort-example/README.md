<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T03:43:30+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "ar"
}
-->
# تحسين Phi3 باستخدام Olive

في هذا المثال، ستستخدم Olive للقيام بـ:

1. تحسين LoRA adapter لتصنيف العبارات إلى حزين، فرح، خوف، مفاجأة.
1. دمج أوزان المحول (adapter) مع النموذج الأساسي.
1. تحسين وتكميم النموذج إلى `int4`.

سنوضح أيضًا كيفية استخدام نموذج تم تحسينه باستخدام واجهة برمجة التطبيقات Generate في ONNX Runtime (ORT).

> **⚠️ لتحسين النموذج، ستحتاج إلى وجود وحدة معالجة رسومات (GPU) مناسبة - مثل A10 أو V100 أو A100.**

## 💾 التثبيت

قم بإنشاء بيئة افتراضية جديدة لـ Python (على سبيل المثال، باستخدام `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

بعد ذلك، قم بتثبيت Olive والاعتماديات اللازمة لعملية تحسين النموذج:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 تحسين Phi3 باستخدام Olive

يحتوي [ملف إعداد Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) على *عملية* تتضمن *مراحل* التالية:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

بشكل عام، ستقوم هذه العملية بـ:

1. تحسين Phi3 (لمدة 150 خطوة، ويمكنك تعديل ذلك) باستخدام بيانات [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. دمج أوزان LoRA adapter مع النموذج الأساسي. سينتج عن ذلك نموذج واحد بصيغة ONNX.
1. يقوم Model Builder بتحسين النموذج لتشغيله باستخدام ONNX runtime *وكذلك* تكميم النموذج إلى `int4`.

لتنفيذ العملية، قم بتشغيل:

```bash
olive run --config phrase-classification.json
```

عند انتهاء Olive، سيكون نموذج Phi3 المحسن `int4` متاحًا في: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 دمج Phi3 المحسن في تطبيقك

لتشغيل التطبيق:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

يجب أن تكون الاستجابة تصنيفًا واحدًا للكلمة (حزين/فرح/خوف/مفاجأة).

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الرسمي. للحصول على معلومات حساسة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ نتيجة استخدام هذه الترجمة.