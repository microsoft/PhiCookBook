<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-07T10:14:10+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "ar"
}
-->
# تحسين Phi3 باستخدام Olive

في هذا المثال ستستخدم Olive من أجل:

1. تحسين محول LoRA لتصنيف العبارات إلى حزن، فرح، خوف، مفاجأة.
1. دمج أوزان المحول في النموذج الأساسي.
1. تحسين وتكميم النموذج إلى `int4`.

سنوضح أيضًا كيفية استنتاج النموذج المحسن باستخدام واجهة ONNX Runtime (ORT) Generate API.

> **⚠️ لتحسين النموذج، ستحتاج إلى وجود وحدة معالجة رسومات مناسبة - مثل A10، V100، A100.**

## 💾 التثبيت

أنشئ بيئة افتراضية جديدة للبايثون (على سبيل المثال، باستخدام `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

بعدها، قم بتثبيت Olive والاعتمادات الخاصة بسير عمل التحسين:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 تحسين Phi3 باستخدام Olive
يحتوي [ملف إعداد Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) على *سير عمل* يتضمن *المراحل* التالية:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

على المستوى العام، سيقوم هذا السير بالآتي:

1. تحسين Phi3 (لمدة 150 خطوة، يمكنك تعديلها) باستخدام بيانات [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. دمج أوزان محول LoRA في النموذج الأساسي. هذا سينتج نموذجًا واحدًا بصيغة ONNX.
1. سيقوم Model Builder بتحسين النموذج لتشغيل ONNX *وأيضًا* تكميم النموذج إلى `int4`.

لتنفيذ سير العمل، شغّل:

```bash
olive run --config phrase-classification.json
```

عند انتهاء Olive، سيكون نموذج Phi3 المحسن والمُكمم `int4` متاحًا في: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 دمج نموذج Phi3 المحسن في تطبيقك

لتشغيل التطبيق:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

يجب أن يكون الرد كلمة واحدة تصنف العبارة (حزن/فرح/خوف/مفاجأة).

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الحساسة أو الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.