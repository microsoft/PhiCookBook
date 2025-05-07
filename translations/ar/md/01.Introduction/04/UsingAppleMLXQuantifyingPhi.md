<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-07T10:46:35+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ar"
}
-->
# **تكميم Phi-3.5 باستخدام إطار عمل Apple MLX**

MLX هو إطار عمل للمصفوفات مخصص لأبحاث التعلم الآلي على شرائح Apple، مقدم من أبحاث التعلم الآلي في Apple.

تم تصميم MLX بواسطة باحثي التعلم الآلي لباحثي التعلم الآلي. الإطار يهدف لأن يكون سهل الاستخدام، لكنه فعال في تدريب ونشر النماذج. تصميم الإطار نفسه بسيط من الناحية المفهومية. نهدف لجعل الأمر سهلاً للباحثين لتوسيع وتحسين MLX بهدف استكشاف أفكار جديدة بسرعة.

يمكن تسريع نماذج LLMs على أجهزة Apple Silicon عبر MLX، ويمكن تشغيل النماذج محليًا بسهولة كبيرة.

الآن يدعم إطار عمل Apple MLX تحويل التكميم لنماذج Phi-3.5-Instruct(**دعم إطار عمل Apple MLX**)، Phi-3.5-Vision(**دعم إطار عمل MLX-VLM**)، و Phi-3.5-MoE(**دعم إطار عمل Apple MLX**). لنجرّبها لاحقًا:

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

### **🤖 عينات لـ Phi-3.5 مع Apple MLX**

| المختبرات    | مقدمة | انتقل |
| -------- | ------- |  ------- |
| 🚀 مقدمة مختبر Phi-3.5 Instruct  | تعلّم كيفية استخدام Phi-3.5 Instruct مع إطار عمل Apple MLX   |  [انتقل](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 مقدمة مختبر Phi-3.5 Vision (صور) | تعلّم كيفية استخدام Phi-3.5 Vision لتحليل الصور مع إطار عمل Apple MLX     |  [انتقل](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 مقدمة مختبر Phi-3.5 Vision (moE)   | تعلّم كيفية استخدام Phi-3.5 MoE مع إطار عمل Apple MLX  |  [انتقل](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **الموارد**

1. تعرّف على إطار عمل Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. مستودع Apple MLX على GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. مستودع MLX-VLM على GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**تنبيه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.