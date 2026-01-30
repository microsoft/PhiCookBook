# **تكميم عائلة Phi باستخدام llama.cpp**

## **ما هو llama.cpp**

llama.cpp هو مكتبة برمجية مفتوحة المصدر مكتوبة أساسًا بلغة C++ تقوم بتنفيذ الاستدلال على نماذج اللغة الكبيرة المختلفة (LLMs)، مثل Llama. الهدف الرئيسي منها هو تقديم أداء متقدم لاستدلال نماذج اللغة الكبيرة عبر مجموعة واسعة من الأجهزة مع إعداد بسيط للغاية. بالإضافة إلى ذلك، هناك روابط بايثون متاحة لهذه المكتبة توفر واجهة برمجة تطبيقات عالية المستوى لإكمال النص وخادم ويب متوافق مع OpenAI.

الهدف الأساسي من llama.cpp هو تمكين استدلال نماذج اللغة الكبيرة بأقل إعداد ممكن وبأداء متطور على مجموعة متنوعة من الأجهزة - محليًا وفي السحابة.

- تنفيذ بسيط بلغة C/C++ بدون أي تبعيات
- دعم متميز لأجهزة Apple silicon - محسّن عبر أطر ARM NEON وAccelerate وMetal
- دعم AVX وAVX2 وAVX512 لمعمارية x86
- تكميم صحيح 1.5-بت، 2-بت، 3-بت، 4-بت، 5-بت، 6-بت، و8-بت لتسريع الاستدلال وتقليل استهلاك الذاكرة
- نوى CUDA مخصصة لتشغيل نماذج اللغة الكبيرة على بطاقات NVIDIA (ودعم بطاقات AMD عبر HIP)
- دعم خلفيات Vulkan وSYCL
- استدلال هجين CPU+GPU لتسريع جزئي للنماذج الأكبر من سعة VRAM الكلية

## **تكميم Phi-3.5 باستخدام llama.cpp**

يمكن تكميم نموذج Phi-3.5-Instruct باستخدام llama.cpp، لكن نماذج Phi-3.5-Vision وPhi-3.5-MoE غير مدعومة حتى الآن. التنسيق الذي يحوله llama.cpp هو gguf، وهو أيضًا أكثر تنسيقات التكميم استخدامًا.

هناك عدد كبير من النماذج بتنسيق GGUF المكمم على Hugging Face. تعتمد AI Foundry وOllama وLlamaEdge على llama.cpp، لذا تُستخدم نماذج GGUF بشكل متكرر.

### **ما هو GGUF**

GGUF هو تنسيق ثنائي مُحسّن للتحميل والحفظ السريع للنماذج، مما يجعله فعالًا جدًا لأغراض الاستدلال. تم تصميم GGUF للاستخدام مع GGML ومنفذات أخرى. تم تطوير GGUF بواسطة @ggerganov، وهو أيضًا مطور llama.cpp، إطار عمل شهير للاستدلال على نماذج اللغة الكبيرة بلغة C/C++. يمكن تحويل النماذج التي تم تطويرها في أُطُر مثل PyTorch إلى تنسيق GGUF لاستخدامها مع هذه المحركات.

### **ONNX مقابل GGUF**

ONNX هو تنسيق تقليدي للتعلم الآلي/التعلم العميق، ويحظى بدعم جيد في أُطُر الذكاء الاصطناعي المختلفة وله سيناريوهات استخدام جيدة في الأجهزة الطرفية. أما GGUF، فهو مبني على llama.cpp ويمكن اعتباره نتاج عصر الذكاء الاصطناعي التوليدي. كلاهما له استخدامات متشابهة. إذا كنت تبحث عن أداء أفضل في الأجهزة المدمجة وطبقات التطبيقات، فقد يكون ONNX خيارك. أما إذا كنت تستخدم إطار العمل والتقنية المشتقة من llama.cpp، فقد يكون GGUF أفضل.

### **تكميم Phi-3.5-Instruct باستخدام llama.cpp**

**1. إعداد البيئة**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. التكميم**

استخدام llama.cpp لتحويل Phi-3.5-Instruct إلى FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

تكميم Phi-3.5 إلى INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. الاختبار**

تثبيت llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***ملاحظة*** 

إذا كنت تستخدم Apple Silicon، يرجى تثبيت llama-cpp-python بهذه الطريقة


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

الاختبار


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **الموارد**

1. تعرف أكثر على llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. تعرف أكثر على onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. تعرف أكثر على GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.