<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-07T10:48:20+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ar"
}
-->
## **كيفية استخدام Model Builder لتكميم Phi-3.5**

يدعم Model Builder الآن تكميم نموذج ONNX لـ Phi-3.5 Instruct و Phi-3.5-Vision

### **Phi-3.5-Instruct**

**تحويل بتسريع المعالج المركزي (CPU) إلى تكميم INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**تحويل بتسريع CUDA إلى تكميم INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ضبط البيئة في الطرفية

```bash

mkdir models

cd models 

```

2. تحميل microsoft/Phi-3.5-vision-instruct في مجلد النماذج  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. يرجى تنزيل هذه الملفات إلى مجلد Phi-3.5-vision-instruct الخاص بك

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. تحميل هذا الملف إلى مجلد النماذج  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. اذهب إلى الطرفية

    تحويل دعم ONNX باستخدام FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **ملاحظة：**

1. يدعم Model Builder حالياً تحويل Phi-3.5-Instruct و Phi-3.5-Vision، لكنه لا يدعم Phi-3.5-MoE

2. لاستخدام نموذج ONNX المكمم، يمكنك استخدامه عبر Generative AI extensions لـ onnxruntime SDK

3. يجب أن نأخذ بعين الاعتبار مسؤولية الذكاء الاصطناعي، لذا يُنصح بإجراء اختبارات نتائج فعالة بعد تحويل تكميم النموذج

4. من خلال تكميم نموذج CPU INT4، يمكننا نشره على أجهزة الحافة (Edge Devices)، مما يتيح سيناريوهات تطبيق أفضل، لذلك أكملنا تكميم Phi-3.5-Instruct حول INT4

## **الموارد**

1. تعرف أكثر على Generative AI extensions لـ onnxruntime  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. مستودع GitHub لـ Generative AI extensions لـ onnxruntime  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.