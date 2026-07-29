# **تحويل فتيل عائلة Phi باستخدام امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime**

## **ما هي امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime**

تساعدك هذه الامتدادات على تشغيل الذكاء الاصطناعي التوليدي مع ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). توفر حلقة الذكاء الاصطناعي التوليدي لنماذج ONNX، بما في ذلك الاستدلال مع ONNX Runtime، ومعالجة اللوغاريتمات، والبحث والعينة، وإدارة ذاكرة التخزين المؤقتة KV. يمكن للمطورين استدعاء طريقة generate() عالية المستوى، أو تشغيل كل تكرار للنموذج في حلقة، وتوليد رمز واحد في كل مرة، واختيارياً تحديث معلمات التوليد داخل الحلقة. تدعم البحث الجشع/شعاع البحث وعينات TopP و TopK لتوليد تسلسلات الرموز ومعالجة اللوغاريتمات المدمجة مثل عقوبات التكرار. يمكنك أيضًا إضافة تقييم مخصص بسهولة.

على مستوى التطبيق، يمكنك استخدام امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime لبناء تطبيقات باستخدام C++ / C# / Python. وعلى مستوى النموذج، يمكنك استخدامها لدمج النماذج الدقيقة وإجراء العمل الكمي المتعلق بالنشر.


## **تحويل Phi-3.5 باستخدام امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime**

### **النماذج المدعومة**

تدعم امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime تحويل التحجيم الكمومي لنماذج Microsoft Phi و Google Gemma و Mistral و Meta LLaMA.


### **منشئ النموذج في امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime**

يسرع منشئ النموذج بشكل كبير من إنشاء نماذج ONNX المحسنة والمحجّمة التي تعمل مع واجهة generate() الخاصة بـ ONNX Runtime.

من خلال منشئ النموذج، يمكنك تحويل النموذج إلى INT4 و INT8 و FP16 و FP32، ودمج طرق تسريع الأجهزة المختلفة مثل CPU و CUDA و DirectML و Mobile وما إلى ذلك.

لاستخدام منشئ النموذج تحتاج إلى تثبيت

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

بعد التثبيت، يمكنك تشغيل سكريبت منشئ النموذج من الطرفية لإجراء تحويل صيغة النموذج والتحجيم الكمومي.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

فهم المعلمات ذات الصلة

1. **model_name** هذا هو النموذج الموجود على Hugging Face، مثل microsoft/Phi-3.5-mini-instruct و microsoft/Phi-3.5-vision-instruct، إلخ. يمكن أن يكون أيضًا المسار الذي تخزن فيه النموذج

2. **path_to_output_folder** مسار حفظ تحويل التحجيم الكمومي

3. **execution_provider** دعم تسريع الأجهزة المختلفة، مثل cpu و cuda و DirectML

4. **cache_dir_to_save_hf_files** نقوم بتنزيل النموذج من Hugging Face وتخزينه مؤقتًا محليًا




***ملاحظة：*** <ul>على الرغم من أن امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime في مرحلة المعاينة، إلا أنه تم دمجها في Microsoft Olive، ويمكنك أيضًا استدعاء وظائف منشئ النموذج امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime عبر Microsoft Olive.</ul>

## **كيفية استخدام منشئ النموذج لتحويل Phi-3.5**

يدعم منشئ النموذج الآن تحويل نماذج ONNX لـ Phi-3.5 Instruct و Phi-3.5-Vision

### **Phi-3.5-Instruct**


**تحويل محسن باستخدام CPU للتحجيم الكمومي INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**تحويل محسن باستخدام CUDA للتحجيم الكمومي INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. إعداد البيئة في الطرفية

```bash

mkdir models

cd models 

```

2. تنزيل microsoft/Phi-3.5-vision-instruct في مجلد النماذج
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. يرجى تنزيل هذه الملفات إلى مجلد Phi-3.5-vision-instruct الخاص بك

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. تنزيل هذا الملف إلى مجلد النماذج
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. انتقل إلى الطرفية

    تحويل دعم ONNX إلى FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **ملاحظة:**

1. يدعم منشئ النموذج حاليًا تحويل Phi-3.5-Instruct و Phi-3.5-Vision، لكنه لا يدعم Phi-3.5-MoE

2. لاستخدام نموذج ONNX المحجّم، يمكنك استخدامه عبر SDK امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime

3. نحتاج إلى المزيد من الاعتبارات المسؤولية في الذكاء الاصطناعي، لذا يُنصح بإجراء اختبار أكثر فاعلية للنتائج بعد تحويل تحجيم النموذج

4. من خلال تحجيم نموذج CPU INT4، يمكن نشره إلى أجهزة Edge، التي تقدم سيناريوهات تطبيق أفضل، ولذلك أكملنا Phi-3.5-Instruct حول INT 4


## **الموارد**

1. تعرف على المزيد حول امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. مستودع GitHub لامتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->