<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:06:21+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "ur"
}
-->
# **llama.cpp کے ذریعے Phi فیملی کی کوانٹائزنگ**

## **llama.cpp کیا ہے**

llama.cpp ایک اوپن سورس سافٹ ویئر لائبریری ہے جو بنیادی طور پر C++ میں لکھی گئی ہے اور مختلف بڑے زبان کے ماڈلز (LLMs) جیسے Llama پر انفرنس انجام دیتی ہے۔ اس کا بنیادی مقصد کم سے کم سیٹ اپ کے ساتھ وسیع ہارڈویئر پر جدید ترین کارکردگی فراہم کرنا ہے۔ اس کے علاوہ، اس لائبریری کے لیے Python بائنڈنگز بھی دستیاب ہیں جو ٹیکسٹ کمپلیشن کے لیے ہائی لیول API اور OpenAI کے مطابق ویب سرور فراہم کرتی ہیں۔

llama.cpp کا بنیادی مقصد کم سے کم سیٹ اپ کے ساتھ اور جدید ترین کارکردگی کے ساتھ مختلف ہارڈویئر پر LLM انفرنس کو ممکن بنانا ہے — مقامی طور پر اور کلاؤڈ میں۔

- بغیر کسی انحصار کے سادہ C/C++ امپلیمنٹیشن  
- Apple silicon کو مکمل سپورٹ — ARM NEON، Accelerate اور Metal فریم ورکس کے ذریعے بہتر بنایا گیا  
- x86 آرکیٹیکچرز کے لیے AVX، AVX2 اور AVX512 سپورٹ  
- تیز انفرنس اور کم میموری استعمال کے لیے 1.5-bit، 2-bit، 3-bit، 4-bit، 5-bit، 6-bit، اور 8-bit انٹیجر کوانٹائزیشن  
- NVIDIA GPUs پر LLMs چلانے کے لیے کسٹم CUDA کرنلز (AMD GPUs کے لیے HIP سپورٹ)  
- Vulkan اور SYCL بیک اینڈ سپورٹ  
- CPU+GPU ہائبرڈ انفرنس تاکہ کل VRAM کی گنجائش سے بڑی ماڈلز کو جزوی طور پر تیز کیا جا سکے  

## **llama.cpp کے ذریعے Phi-3.5 کی کوانٹائزنگ**

Phi-3.5-Instruct ماڈل کو llama.cpp کے ذریعے کوانٹائز کیا جا سکتا ہے، لیکن Phi-3.5-Vision اور Phi-3.5-MoE ابھی سپورٹ نہیں کرتے۔ llama.cpp کے ذریعے کنورٹ کیا گیا فارمیٹ gguf ہے، جو سب سے زیادہ استعمال ہونے والا کوانٹائزیشن فارمیٹ بھی ہے۔

Hugging Face پر کوانٹائزڈ GGUF فارمیٹ کے بہت سے ماڈلز موجود ہیں۔ AI Foundry، Ollama، اور LlamaEdge بھی llama.cpp پر انحصار کرتے ہیں، اس لیے GGUF ماڈلز اکثر استعمال ہوتے ہیں۔

### **GGUF کیا ہے**

GGUF ایک بائنری فارمیٹ ہے جو ماڈلز کو تیزی سے لوڈ اور سیو کرنے کے لیے بہتر بنایا گیا ہے، جس سے یہ انفرنس کے لیے بہت مؤثر ہے۔ GGUF کو GGML اور دیگر ایکزیکیوٹرز کے ساتھ استعمال کے لیے ڈیزائن کیا گیا ہے۔ GGUF کو @ggerganov نے تیار کیا ہے جو llama.cpp کے بھی ڈویلپر ہیں، جو ایک مقبول C/C++ LLM انفرنس فریم ورک ہے۔ PyTorch جیسے فریم ورکس میں بنائے گئے ماڈلز کو GGUF فارمیٹ میں تبدیل کیا جا سکتا ہے تاکہ انہیں ان انجنز کے ساتھ استعمال کیا جا سکے۔

### **ONNX بمقابلہ GGUF**

ONNX ایک روایتی مشین لرننگ/ڈیپ لرننگ فارمیٹ ہے، جو مختلف AI فریم ورکس میں اچھی طرح سپورٹڈ ہے اور ایج ڈیوائسز میں اس کے استعمال کے اچھے مواقع ہیں۔ GGUF، جو llama.cpp پر مبنی ہے، جدید GenAI دور میں تیار کیا گیا ہے۔ دونوں کے استعمالات ملتے جلتے ہیں۔ اگر آپ کو ایمبیڈڈ ہارڈویئر اور ایپلیکیشن لیئرز میں بہتر کارکردگی چاہیے تو ONNX آپ کا انتخاب ہو سکتا ہے۔ اگر آپ llama.cpp کے ڈیریویٹو فریم ورک اور ٹیکنالوجی استعمال کرتے ہیں تو GGUF بہتر ہو سکتا ہے۔

### **llama.cpp کے ذریعے Phi-3.5-Instruct کی کوانٹائزنگ**

**1. ماحول کی ترتیب**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. کوانٹائزنگ**

llama.cpp استعمال کرتے ہوئے Phi-3.5-Instruct کو FP16 GGUF میں تبدیل کریں


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 کو INT4 میں کوانٹائز کرنا


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. جانچ**

llama-cpp-python انسٹال کریں


```bash

pip install llama-cpp-python -U

```

***نوٹ*** 

اگر آپ Apple Silicon استعمال کر رہے ہیں، تو براہ کرم llama-cpp-python کو اس طرح انسٹال کریں


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

جانچ


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **وسائل**

1. llama.cpp کے بارے میں مزید جانیں [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. onnxruntime کے بارے میں مزید جانیں [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. GGUF کے بارے میں مزید جانیں [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔