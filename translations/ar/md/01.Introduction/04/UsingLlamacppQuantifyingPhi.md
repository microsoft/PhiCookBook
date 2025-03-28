<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e5bb9190ef9d149d28037a768c6b62b2",
  "translation_date": "2025-03-27T08:39:16+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingLlamacppQuantifyingPhi.md",
  "language_code": "ar"
}
-->
# **تقليل حجم عائلة Phi باستخدام llama.cpp**

## **ما هو llama.cpp**

llama.cpp هي مكتبة برمجية مفتوحة المصدر مكتوبة بشكل رئيسي بلغة C++ وتُستخدم لتنفيذ الاستدلال على مجموعة متنوعة من نماذج اللغة الكبيرة (LLMs)، مثل Llama. الهدف الرئيسي لها هو توفير أداء متقدم للاستدلال على نماذج اللغة الكبيرة عبر مجموعة واسعة من الأجهزة مع إعداد بسيط للغاية. بالإضافة إلى ذلك، تتوفر روابط بلغة Python لهذه المكتبة، مما يوفر واجهة برمجية عالية المستوى لإكمال النص وخادم ويب متوافق مع OpenAI.

الهدف الرئيسي لـ llama.cpp هو تمكين استدلال نماذج اللغة الكبيرة بأقل إعداد ممكن وأداء متقدم على مجموعة متنوعة من الأجهزة - محليًا وفي السحابة.

- تنفيذ بسيط بلغة C/C++ بدون أي تبعيات
- دعم متميز لـ Apple silicon - مُحسن عبر تقنيات ARM NEON، Accelerate، وMetal
- دعم AVX، AVX2 وAVX512 للمعماريات x86
- تقليل حجم البيانات إلى 1.5-bit، 2-bit، 3-bit، 4-bit، 5-bit، 6-bit، و8-bit لزيادة سرعة الاستدلال وتقليل استخدام الذاكرة
- نوى CUDA مخصصة لتشغيل نماذج اللغة الكبيرة على وحدات معالجة الرسومات من NVIDIA (دعم وحدات معالجة الرسومات من AMD عبر HIP)
- دعم الخلفيات Vulkan وSYCL
- استدلال هجين بين CPU وGPU لتسريع النماذج الأكبر من إجمالي سعة VRAM

## **تقليل حجم Phi-3.5 باستخدام llama.cpp**

يمكن تقليل حجم نموذج Phi-3.5-Instruct باستخدام llama.cpp، ولكن النموذجين Phi-3.5-Vision وPhi-3.5-MoE غير مدعومين حاليًا. التنسيق الذي يتم تحويله بواسطة llama.cpp هو gguf، وهو أيضًا التنسيق الأكثر استخدامًا لتقليل الحجم.

هناك عدد كبير من النماذج بتنسيق GGUF المقلص على Hugging Face. تعتمد AI Foundry وOllama وLlamaEdge على llama.cpp، لذا يتم استخدام نماذج GGUF بشكل متكرر أيضًا.

### **ما هو GGUF**

GGUF هو تنسيق ثنائي مُحسن لتحميل وحفظ النماذج بسرعة، مما يجعله فعالًا للغاية لأغراض الاستدلال. تم تصميم GGUF للاستخدام مع GGML وغيرها من المنفذين. تم تطوير GGUF بواسطة @ggerganov الذي يُعد أيضًا مطورًا لمكتبة llama.cpp، وهي إطار عمل شهير للاستدلال على نماذج اللغة الكبيرة باستخدام C/C++. يمكن تحويل النماذج التي تم تطويرها في أطر عمل مثل PyTorch إلى تنسيق GGUF لاستخدامها مع تلك المحركات.

### **ONNX مقابل GGUF**

ONNX هو تنسيق تقليدي للتعلم الآلي/التعلم العميق، ويحظى بدعم جيد في مختلف أطر عمل الذكاء الاصطناعي وله سيناريوهات استخدام جيدة في الأجهزة الطرفية. أما بالنسبة لـ GGUF، فهو يعتمد على llama.cpp ويمكن القول إنه نتاج عصر GenAI. كلاهما له استخدامات متشابهة. إذا كنت تبحث عن أداء أفضل في الأجهزة المدمجة وطبقات التطبيقات، فقد يكون ONNX هو خيارك. إذا كنت تستخدم إطار العمل والتقنيات المشتقة من llama.cpp، فقد يكون GGUF أفضل.

### **تقليل حجم Phi-3.5-Instruct باستخدام llama.cpp**

**1. إعداد البيئة**  

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```  

**2. تقليل الحجم**  

استخدام llama.cpp لتحويل Phi-3.5-Instruct إلى FP16 GGUF  

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```  

تقليل حجم Phi-3.5 إلى INT4  

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

## **المصادر**

1. لمعرفة المزيد عن llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  

2. لمعرفة المزيد عن GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)  

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حيوية، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.