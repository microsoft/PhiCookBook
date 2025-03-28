<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-03-27T08:26:58+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ar"
}
-->
# **تكميم Phi-3.5 باستخدام إطار عمل Apple MLX**

MLX هو إطار عمل للمصفوفات مخصص لأبحاث التعلم الآلي على أجهزة Apple Silicon، مقدم من فريق أبحاث التعلم الآلي في Apple.

تم تصميم MLX من قبل باحثي التعلم الآلي لصالح باحثي التعلم الآلي. الإطار مصمم ليكون سهل الاستخدام، ولكنه في نفس الوقت فعال لتدريب ونشر النماذج. تصميم الإطار نفسه بسيط من الناحية المفاهيمية. نحن نسعى لجعل الأمر سهلاً على الباحثين لتوسيع وتحسين MLX بهدف استكشاف الأفكار الجديدة بسرعة.

يمكن تسريع النماذج اللغوية الكبيرة (LLMs) على أجهزة Apple Silicon باستخدام MLX، ويمكن تشغيل النماذج محليًا بسهولة كبيرة.

الآن يدعم إطار عمل Apple MLX تحويل التكميم لـ Phi-3.5-Instruct(**دعم إطار عمل Apple MLX**)، Phi-3.5-Vision(**دعم إطار عمل MLX-VLM**)، وPhi-3.5-MoE(**دعم إطار عمل Apple MLX**). دعونا نجرب ذلك الآن:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 عينات لـ Phi-3.5 باستخدام Apple MLX**

| المختبرات | الوصف | الانتقال |
| -------- | ------- | ------- |
| 🚀 مختبر - تقديم Phi-3.5 Instruct | تعلم كيفية استخدام Phi-3.5 Instruct مع إطار عمل Apple MLX | [انتقال](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb) |
| 🚀 مختبر - تقديم Phi-3.5 Vision (الصورة) | تعلم كيفية استخدام Phi-3.5 Vision لتحليل الصور باستخدام إطار عمل Apple MLX | [انتقال](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb) |
| 🚀 مختبر - تقديم Phi-3.5 Vision (MoE) | تعلم كيفية استخدام Phi-3.5 MoE باستخدام إطار عمل Apple MLX | [انتقال](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb) |

## **المصادر**

1. تعرف على إطار عمل Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. مستودع GitHub لـ Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. مستودع GitHub لـ MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق. للحصول على معلومات حساسة، يُوصى بالاستعانة بخدمات ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ نتيجة استخدام هذه الترجمة.