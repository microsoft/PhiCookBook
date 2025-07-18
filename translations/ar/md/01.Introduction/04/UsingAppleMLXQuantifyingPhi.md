<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:52:34+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ar"
}
-->
# **تكميم Phi-3.5 باستخدام إطار عمل Apple MLX**

MLX هو إطار عمل للمصفوفات مخصص لأبحاث التعلم الآلي على شرائح Apple، مقدم من أبحاث التعلم الآلي في Apple.

تم تصميم MLX بواسطة باحثي التعلم الآلي من أجل باحثي التعلم الآلي. الإطار يهدف لأن يكون سهل الاستخدام، لكنه في الوقت نفسه فعال لتدريب ونشر النماذج. تصميم الإطار نفسه بسيط من الناحية المفاهيمية. نهدف إلى تسهيل توسيع وتحسين MLX للباحثين بهدف استكشاف الأفكار الجديدة بسرعة.

يمكن تسريع نماذج LLMs على أجهزة Apple Silicon من خلال MLX، ويمكن تشغيل النماذج محليًا بسهولة كبيرة.

الآن يدعم إطار عمل Apple MLX تحويل التكميم لنماذج Phi-3.5-Instruct (**دعم إطار عمل Apple MLX**)، وPhi-3.5-Vision (**دعم إطار عمل MLX-VLM**)، وPhi-3.5-MoE (**دعم إطار عمل Apple MLX**). دعونا نجربها الآن:

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

| المختبرات    | التعريف | الذهاب |
| -------- | ------- |  ------- |
| 🚀 مختبر-تعريف Phi-3.5 Instruct  | تعلّم كيفية استخدام Phi-3.5 Instruct مع إطار عمل Apple MLX   |  [اذهب](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 مختبر-تعريف Phi-3.5 Vision (صورة) | تعلّم كيفية استخدام Phi-3.5 Vision لتحليل الصور مع إطار عمل Apple MLX     |  [اذهب](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 مختبر-تعريف Phi-3.5 Vision (moE)   | تعلّم كيفية استخدام Phi-3.5 MoE مع إطار عمل Apple MLX  |  [اذهب](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **الموارد**

1. تعرّف على إطار عمل Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. مستودع Apple MLX على GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. مستودع MLX-VLM على GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.