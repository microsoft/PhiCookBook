<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-07T10:17:41+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "ar"
}
-->
# ضبط دقيق لـ Phi3 باستخدام Olive

في هذا المثال ستستخدم Olive من أجل:

1. ضبط دقيق لمحول LoRA لتصنيف العبارات إلى حزن، فرح، خوف، مفاجأة.
1. دمج أوزان المحول في النموذج الأساسي.
1. تحسين وتكميم النموذج إلى `int4`.

سنوضح أيضًا كيفية استنتاج النموذج المضبوط باستخدام واجهة ONNX Runtime (ORT) Generate API.

> **⚠️ لضبط الدقيق، ستحتاج إلى وجود وحدة معالجة رسومات مناسبة - مثل A10، V100، A100.**

## 💾 التثبيت

أنشئ بيئة افتراضية جديدة للبايثون (على سبيل المثال، باستخدام `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

بعد ذلك، قم بتثبيت Olive والاعتمادات اللازمة لسير عمل الضبط الدقيق:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 ضبط دقيق لـ Phi3 باستخدام Olive  
يحتوي [ملف تكوين Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) على *سير عمل* يتضمن *المراحل* التالية:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

على مستوى عالٍ، سيقوم هذا السير بـ:

1. ضبط دقيق لـ Phi3 (لمدة 150 خطوة، يمكن تعديلها) باستخدام بيانات [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. دمج أوزان محول LoRA في النموذج الأساسي. سيعطيك هذا نموذجًا واحدًا بصيغة ONNX.
1. سيقوم Model Builder بتحسين النموذج لتشغيل ONNX *وكذلك* تكميم النموذج إلى `int4`.

لتنفيذ سير العمل، شغّل:

```bash
olive run --config phrase-classification.json
```

عند اكتمال Olive، سيكون نموذج Phi3 المضبوط والمُحسّن بتنسيق `int4` متاحًا في: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 دمج Phi3 المضبوط في تطبيقك

لتشغيل التطبيق:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

يجب أن يكون الرد عبارة عن كلمة واحدة تصنف العبارة (حزن/فرح/خوف/مفاجأة).

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الحساسة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.