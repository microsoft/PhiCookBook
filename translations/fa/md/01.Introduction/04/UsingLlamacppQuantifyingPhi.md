<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-07T14:50:43+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "fa"
}
-->
# **کوانتایز کردن خانواده Phi با استفاده از llama.cpp**

## **llama.cpp چیست**

llama.cpp یک کتابخانه نرم‌افزاری متن‌باز است که عمدتاً با زبان C++ نوشته شده و برای انجام استنتاج روی مدل‌های بزرگ زبان (LLM) مختلف مانند Llama استفاده می‌شود. هدف اصلی آن ارائه عملکرد پیشرفته برای استنتاج LLM روی انواع سخت‌افزارها با کمترین نیاز به تنظیمات است. همچنین، این کتابخانه دارای بایندینگ‌های پایتون است که API سطح بالا برای تکمیل متن و یک سرور وب سازگار با OpenAI ارائه می‌دهد.

هدف اصلی llama.cpp فراهم کردن امکان استنتاج LLM با کمترین تنظیمات و عملکرد به‌روز در سخت‌افزارهای مختلف، چه به صورت محلی و چه در فضای ابری است.

- پیاده‌سازی ساده C/C++ بدون هیچ وابستگی
- پشتیبانی کامل از Apple silicon با بهینه‌سازی از طریق ARM NEON، Accelerate و Metal
- پشتیبانی از AVX، AVX2 و AVX512 برای معماری‌های x86
- کوانتایزیشن صحیح اعداد صحیح با 1.5 بیت، 2 بیت، 3 بیت، 4 بیت، 5 بیت، 6 بیت و 8 بیت برای سرعت بالاتر استنتاج و کاهش مصرف حافظه
- کرنل‌های سفارشی CUDA برای اجرای LLM روی GPUهای NVIDIA (پشتیبانی از GPUهای AMD از طریق HIP)
- پشتیبانی از بک‌اند Vulkan و SYCL
- استنتاج ترکیبی CPU+GPU برای تسریع مدل‌های بزرگ‌تر از ظرفیت کل VRAM

## **کوانتایز کردن Phi-3.5 با llama.cpp**

مدل Phi-3.5-Instruct را می‌توان با llama.cpp کوانتایز کرد، اما مدل‌های Phi-3.5-Vision و Phi-3.5-MoE هنوز پشتیبانی نمی‌شوند. فرمت تبدیل شده توسط llama.cpp، فرمت gguf است که پرکاربردترین فرمت کوانتایزیشن نیز محسوب می‌شود.

تعداد زیادی مدل کوانتایز شده با فرمت GGUF در Hugging Face موجود است. AI Foundry، Ollama و LlamaEdge بر پایه llama.cpp هستند، بنابراین مدل‌های GGUF نیز به طور گسترده استفاده می‌شوند.

### **GGUF چیست**

GGUF یک فرمت باینری است که برای بارگذاری و ذخیره سریع مدل‌ها بهینه شده و برای استنتاج بسیار کارآمد است. GGUF برای استفاده با GGML و سایر اجراکننده‌ها طراحی شده است. این فرمت توسط @ggerganov توسعه یافته که همچنین توسعه‌دهنده llama.cpp، فریم‌ورک محبوب استنتاج LLM در C/C++ است. مدل‌هایی که ابتدا در فریم‌ورک‌هایی مانند PyTorch ساخته شده‌اند، می‌توانند به فرمت GGUF تبدیل شوند تا با این موتور‌ها سازگار باشند.

### **ONNX در مقابل GGUF**

ONNX یک فرمت سنتی یادگیری ماشین/یادگیری عمیق است که در فریم‌ورک‌های مختلف هوش مصنوعی به خوبی پشتیبانی می‌شود و در دستگاه‌های لبه کاربردهای مناسبی دارد. اما GGUF بر پایه llama.cpp است و می‌توان گفت محصول دوران GenAI است. هر دو کاربردهای مشابهی دارند. اگر به دنبال عملکرد بهتر در سخت‌افزارهای تعبیه‌شده و لایه‌های اپلیکیشن هستید، ONNX گزینه شماست. اگر از فریم‌ورک و فناوری مشتق شده از llama.cpp استفاده می‌کنید، GGUF ممکن است بهتر باشد.

### **کوانتایز کردن Phi-3.5-Instruct با استفاده از llama.cpp**

**1. پیکربندی محیط**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. کوانتایزیشن**

تبدیل Phi-3.5-Instruct به FP16 GGUF با استفاده از llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

کوانتایز کردن Phi-3.5 به INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. تست**

نصب llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***توجه*** 

اگر از Apple Silicon استفاده می‌کنید، لطفاً llama-cpp-python را به این شکل نصب کنید


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

تست 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **منابع**

1. اطلاعات بیشتر درباره llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. اطلاعات بیشتر درباره onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. اطلاعات بیشتر درباره GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.