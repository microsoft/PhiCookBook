<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T04:01:53+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "ar"
}
-->
# ضبط Phi3 باستخدام Olive

في هذا المثال، ستستخدم Olive للقيام بـ:

1. ضبط محول LoRA لتصنيف العبارات إلى حزن، فرح، خوف، مفاجأة.
2. دمج أوزان المحول مع النموذج الأساسي.
3. تحسين وتكميم النموذج إلى `int4`.

سنوضح أيضًا كيفية استخدام نموذج تم ضبطه باستخدام واجهة برمجة التطبيقات Generate الخاصة بـ ONNX Runtime (ORT).

> **⚠️ لضبط النموذج، ستحتاج إلى وحدة معالجة رسومات (GPU) مناسبة - مثل A10، V100، A100.**

## 💾 التثبيت

قم بإنشاء بيئة افتراضية جديدة للـ Python (على سبيل المثال باستخدام `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

بعد ذلك، قم بتثبيت Olive والمتطلبات اللازمة لسير عمل ضبط النموذج:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 ضبط Phi3 باستخدام Olive
يحتوي [ملف إعداد Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) على *سير عمل* يتضمن *مراحل* كالتالي:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

بصورة عامة، يقوم سير العمل هذا بما يلي:

1. ضبط Phi3 (لمدة 150 خطوة، ويمكنك تعديلها) باستخدام بيانات [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. دمج أوزان محول LoRA مع النموذج الأساسي. سيؤدي ذلك إلى إنتاج نموذج واحد بصيغة ONNX.
3. يقوم Model Builder بتحسين النموذج لتشغيله مع ONNX runtime *وأيضًا* تكميم النموذج إلى `int4`.

لتنفيذ سير العمل، قم بتشغيل:

```bash
olive run --config phrase-classification.json
```

عند انتهاء Olive، سيكون النموذج المحسن `int4` والمضبوط Phi3 متاحًا في: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 دمج Phi3 المضبوط في تطبيقك

لتشغيل التطبيق:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

يجب أن تكون الاستجابة تصنيفًا بكلمة واحدة للعبارة (حزن/فرح/خوف/مفاجأة).

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حساسة أو مهمة، يُوصى باستخدام ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.