<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-03-27T08:46:35+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ar"
}
-->
# **تحويل Phi Family باستخدام إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime**

## **ما هي إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime**

تساعد هذه الإضافات في تشغيل الذكاء الاصطناعي التوليدي باستخدام ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). توفر دورة الذكاء الاصطناعي التوليدي لنماذج ONNX، بما في ذلك الاستدلال باستخدام ONNX Runtime، معالجة logits، البحث وأخذ العينات، وإدارة ذاكرة التخزين المؤقت KV. يمكن للمطورين استدعاء طريقة عالية المستوى generate()، أو تشغيل كل تكرار للنموذج في حلقة، لإنشاء رمز واحد في كل مرة، مع إمكانية تعديل معلمات التوليد داخل الحلقة. تدعم الإضافات البحث الجشع/الشعاع وأخذ عينات TopP وTopK لإنشاء تسلسلات الرموز ومعالجة logits المدمجة مثل عقوبات التكرار. كما يمكنك بسهولة إضافة تقييم مخصص.

على مستوى التطبيقات، يمكنك استخدام إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime لبناء تطبيقات باستخدام C++/C#/Python. وعلى مستوى النماذج، يمكنك استخدامها لدمج النماذج التي تم تحسينها وتخصيصها وأداء العمل الكمي المرتبط بالنشر.

## **تحويل Phi-3.5 باستخدام إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime**

### **النماذج المدعومة**

تدعم إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime تحويل النماذج الكمية مثل Microsoft Phi، Google Gemma، Mistral، Meta LLaMA.

### **أداة بناء النماذج في إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime**

تعمل أداة بناء النماذج على تسريع إنشاء نماذج ONNX المحسّنة والمحوّلة كميًا التي تعمل مع واجهة برمجة التطبيقات generate() لـ ONNX Runtime.

من خلال أداة بناء النماذج، يمكنك تحويل النموذج إلى INT4، INT8، FP16، FP32، ودمج طرق تسريع الأجهزة المختلفة مثل CPU، CUDA، DirectML، Mobile، وغيرها.

للاستخدام، تحتاج إلى تثبيت:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

بعد التثبيت، يمكنك تشغيل سكريبت أداة بناء النماذج من الطرفية لتحويل صيغة النموذج والقيام بالتحويل الكمي.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

فهم المعلمات ذات الصلة:

1. **model_name** هذا هو النموذج الموجود على Hugging Face، مثل microsoft/Phi-3.5-mini-instruct، microsoft/Phi-3.5-vision-instruct، وغيرها. ويمكن أن يكون أيضًا المسار الذي تخزن فيه النموذج.

2. **path_to_output_folder** مسار حفظ التحويل الكمي.

3. **execution_provider** دعم تسريع الأجهزة المختلفة، مثل cpu، cuda، DirectML.

4. **cache_dir_to_save_hf_files** نقوم بتنزيل النموذج من Hugging Face وتخزينه محليًا.

***ملاحظة:***

## **كيفية استخدام أداة بناء النماذج لتحويل Phi-3.5**

تدعم أداة بناء النماذج الآن تحويل نماذج ONNX الكمية لـ Phi-3.5 Instruct وPhi-3.5-Vision.

### **Phi-3.5-Instruct**

**تحويل كمي INT4 باستخدام تسريع CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**تحويل كمي INT4 باستخدام تسريع CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. إعداد البيئة في الطرفية:

```bash

mkdir models

cd models 

```

2. تنزيل نموذج microsoft/Phi-3.5-vision-instruct في مجلد النماذج:
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. يرجى تنزيل هذه الملفات إلى مجلد Phi-3.5-vision-instruct الخاص بك:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. تنزيل هذا الملف إلى مجلد النماذج:
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. الانتقال إلى الطرفية:

تحويل دعم ONNX باستخدام FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **ملاحظة:**

1. تدعم أداة بناء النماذج حاليًا تحويل Phi-3.5-Instruct وPhi-3.5-Vision، ولكنها لا تدعم Phi-3.5-MoE.

2. لاستخدام النموذج الكمي لـ ONNX، يمكنك استخدامه من خلال SDK إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime.

3. يجب أن نأخذ بعين الاعتبار الذكاء الاصطناعي المسؤول بشكل أكبر، لذا بعد تحويل النموذج كميًا، يُوصى بإجراء اختبارات نتائج فعّالة.

4. من خلال تحويل نموذج CPU INT4 كميًا، يمكننا نشره على أجهزة الحافة، مما يوفر سيناريوهات تطبيق أفضل، لذا أكملنا Phi-3.5-Instruct حول INT4.

## **الموارد**

1. لمعرفة المزيد عن إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. مستودع GitHub لإضافات الذكاء الاصطناعي التوليدي لـ onnxruntime: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.