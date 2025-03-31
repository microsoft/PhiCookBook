<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-03-27T07:50:07+00:00",
  "source_file": "md\\01.Introduction\\03\\MLX_Inference.md",
  "language_code": "ar"
}
-->
# **استخدام Phi-3 مع إطار عمل Apple MLX**

## **ما هو إطار عمل MLX**

MLX هو إطار عمل مخصص لأبحاث التعلم الآلي على معالجات Apple silicon، مقدم من فريق أبحاث التعلم الآلي في Apple.

تم تصميم MLX بواسطة باحثي التعلم الآلي من أجل باحثي التعلم الآلي. الإطار مصمم ليكون سهل الاستخدام، ولكنه يظل فعالًا لتدريب النماذج ونشرها. كما أن تصميم الإطار نفسه بسيط من الناحية المفاهيمية. هدفنا هو تسهيل عملية توسيع وتحسين MLX للباحثين بهدف استكشاف الأفكار الجديدة بسرعة.

يمكن تسريع النماذج اللغوية الكبيرة (LLMs) على أجهزة Apple Silicon باستخدام MLX، ويمكن تشغيل النماذج محليًا بكل سهولة.

## **استخدام MLX لتشغيل Phi-3-mini**

### **1. إعداد بيئة MLX**

1. Python 3.11.x  
2. تثبيت مكتبة MLX  

```bash

pip install mlx-lm

```

### **2. تشغيل Phi-3-mini في الطرفية باستخدام MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

النتيجة (بيئتي هي Apple M1 Max، و64GB) هي:

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.ar.png)

### **3. تحويل Phi-3-mini إلى نموذج مكثف باستخدام MLX في الطرفية**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***ملاحظة:*** يمكن تحويل النموذج إلى نسخة مكثفة باستخدام mlx_lm.convert، ويكون التحويل الافتراضي إلى INT4. في هذا المثال يتم تحويل Phi-3-mini إلى INT4.

يتم تخزين النموذج المكثف في الدليل الافتراضي ./mlx_model. بعد التحويل، يمكننا اختبار النموذج المكثف باستخدام MLX من خلال الطرفية:

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

النتيجة هي:

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.ar.png)

### **4. تشغيل Phi-3-mini باستخدام MLX في Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.ar.png)

***ملاحظة:*** يرجى قراءة هذا المثال [اضغط هنا](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **الموارد**

1. تعرف على إطار عمل Apple MLX [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)  

2. مستودع Apple MLX على GitHub [https://github.com/ml-explore](https://github.com/ml-explore)  

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حساسة أو هامة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.