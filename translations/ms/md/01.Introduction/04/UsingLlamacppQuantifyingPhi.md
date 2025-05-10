<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:15:24+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "ms"
}
-->
# **كمية عائلة Phi باستخدام llama.cpp**

## **ما هو llama.cpp**

llama.cpp هو مكتبة برمجية مفتوحة المصدر مكتوبة بشكل رئيسي بلغة C++ تقوم بالتنفيذ على نماذج اللغة الكبيرة المختلفة (LLMs)، مثل Llama. الهدف الأساسي منها هو توفير أداء متقدم لتنفيذ LLM عبر مجموعة واسعة من الأجهزة مع إعداد بسيط. بالإضافة إلى ذلك، تتوفر روابط بايثون لهذه المكتبة، تقدم واجهة برمجة تطبيقات عالية المستوى لإكمال النص وخادم ويب متوافق مع OpenAI.

الهدف الرئيسي من llama.cpp هو تمكين تنفيذ LLM بأقل إعداد ممكن وأداء متقدم على مجموعة متنوعة من الأجهزة - محليًا وفي السحابة.

- تنفيذ بسيط بلغة C/C++ بدون أي تبعيات
- دعم متميز لمعالجات Apple silicon - محسن باستخدام ARM NEON، Accelerate و Metal frameworks
- دعم AVX، AVX2 و AVX512 لمعمارية x86
- كميات صحيحة بدقة 1.5-بت، 2-بت، 3-بت، 4-بت، 5-بت، 6-بت، و8-بت لتسريع التنفيذ وتقليل استخدام الذاكرة
- نوى CUDA مخصصة لتشغيل LLMs على بطاقات NVIDIA (دعم بطاقات AMD عبر HIP)
- دعم خلفيات Vulkan و SYCL
- تنفيذ هجين CPU+GPU لتسريع جزئي للنماذج الأكبر من سعة VRAM الكلية

## **كمية Phi-3.5 باستخدام llama.cpp**

يمكن تنفيذ كمية نموذج Phi-3.5-Instruct باستخدام llama.cpp، لكن نماذج Phi-3.5-Vision و Phi-3.5-MoE غير مدعومة حتى الآن. الصيغة التي يحولها llama.cpp هي gguf، وهي أيضًا صيغة الكمية الأكثر استخدامًا.

هناك عدد كبير من النماذج بكميات صيغة GGUF على Hugging face. تعتمد AI Foundry و Ollama و LlamaEdge على llama.cpp، لذلك تُستخدم نماذج GGUF بشكل متكرر.

### **ما هو GGUF**

GGUF هو صيغة ثنائية مصممة للتحميل والحفظ السريع للنماذج، مما يجعلها فعالة جدًا لأغراض التنفيذ. GGUF مصممة للاستخدام مع GGML وغيرها من المحركات. تم تطوير GGUF بواسطة @ggerganov الذي هو أيضًا مطور llama.cpp، إطار عمل شهير لتنفيذ LLM بلغة C/C++. يمكن تحويل النماذج التي تم تطويرها أولًا في أطر مثل PyTorch إلى صيغة GGUF لاستخدامها مع تلك المحركات.

### **ONNX مقابل GGUF**

ONNX هي صيغة تقليدية لتعلم الآلة / التعلم العميق، وتحظى بدعم جيد في أطر الذكاء الاصطناعي المختلفة ولها سيناريوهات استخدام جيدة في الأجهزة الطرفية. أما GGUF، فهي مبنية على llama.cpp ويمكن اعتبارها نتاج عصر GenAI. الاستخدامات متشابهة. إذا كنت تريد أداءً أفضل في الأجهزة المدمجة وطبقات التطبيقات، قد يكون ONNX خيارك. إذا كنت تستخدم إطار العمل والتقنيات المشتقة من llama.cpp، فقد تكون GGUF أفضل.

### **كمية Phi-3.5-Instruct باستخدام llama.cpp**

**1. إعداد البيئة**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. الكمية**

استخدام llama.cpp لتحويل Phi-3.5-Instruct إلى FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

كمية Phi-3.5 إلى INT4


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

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.