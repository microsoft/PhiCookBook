<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:06:10+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "fa"
}
-->
# **کوانتایز کردن خانواده فی با استفاده از llama.cpp**

## **llama.cpp چیست**

llama.cpp یک کتابخانه نرم‌افزاری متن‌باز است که عمدتاً با زبان C++ نوشته شده و برای انجام استنتاج روی مدل‌های بزرگ زبان (LLM) مختلف مانند Llama استفاده می‌شود. هدف اصلی آن ارائه عملکرد پیشرفته برای استنتاج LLM روی طیف گسترده‌ای از سخت‌افزارها با حداقل تنظیمات است. علاوه بر این، بایندینگ‌های پایتون برای این کتابخانه موجود است که API سطح بالا برای تکمیل متن و یک وب‌سرور سازگار با OpenAI ارائه می‌دهد.

هدف اصلی llama.cpp این است که استنتاج LLM را با حداقل تنظیمات و عملکرد پیشرفته روی انواع مختلف سخت‌افزار، چه به صورت محلی و چه در فضای ابری، ممکن سازد.

- پیاده‌سازی ساده C/C++ بدون هیچ وابستگی
- پشتیبانی کامل از Apple silicon - بهینه‌شده با استفاده از ARM NEON، Accelerate و Metal frameworks
- پشتیبانی از AVX، AVX2 و AVX512 برای معماری‌های x86
- کوانتایز کردن عدد صحیح با دقت‌های 1.5 بیت، 2 بیت، 3 بیت، 4 بیت، 5 بیت، 6 بیت و 8 بیت برای استنتاج سریع‌تر و کاهش مصرف حافظه
- کرنل‌های سفارشی CUDA برای اجرای LLM روی GPUهای NVIDIA (پشتیبانی از GPUهای AMD از طریق HIP)
- پشتیبانی از بک‌اند Vulkan و SYCL
- استنتاج هیبریدی CPU+GPU برای تسریع جزئی مدل‌هایی که بزرگ‌تر از ظرفیت کل VRAM هستند

## **کوانتایز کردن Phi-3.5 با llama.cpp**

مدل Phi-3.5-Instruct را می‌توان با استفاده از llama.cpp کوانتایز کرد، اما Phi-3.5-Vision و Phi-3.5-MoE هنوز پشتیبانی نمی‌شوند. فرمت تبدیل شده توسط llama.cpp، gguf است که پرکاربردترین فرمت کوانتایز نیز محسوب می‌شود.

تعداد زیادی مدل کوانتایز شده با فرمت GGUF در Hugging Face موجود است. AI Foundry، Ollama و LlamaEdge بر پایه llama.cpp کار می‌کنند، بنابراین مدل‌های GGUF نیز به طور گسترده استفاده می‌شوند.

### **GGUF چیست**

GGUF یک فرمت باینری است که برای بارگذاری و ذخیره سریع مدل‌ها بهینه شده و برای استنتاج بسیار کارآمد است. GGUF برای استفاده با GGML و سایر اجراکننده‌ها طراحی شده است. GGUF توسط @ggerganov توسعه یافته که همچنین توسعه‌دهنده llama.cpp، فریمورک محبوب استنتاج LLM به زبان C/C++ است. مدل‌هایی که ابتدا در فریمورک‌هایی مانند PyTorch توسعه یافته‌اند، می‌توانند به فرمت GGUF تبدیل شوند تا با این موتور‌ها استفاده شوند.

### **ONNX در مقابل GGUF**

ONNX یک فرمت سنتی یادگیری ماشین/یادگیری عمیق است که در فریمورک‌های مختلف هوش مصنوعی به خوبی پشتیبانی می‌شود و کاربردهای خوبی در دستگاه‌های لبه‌ای دارد. اما GGUF بر پایه llama.cpp است و می‌توان گفت در عصر GenAI تولید شده است. هر دو کاربردهای مشابهی دارند. اگر به دنبال عملکرد بهتر در سخت‌افزارهای تعبیه‌شده و لایه‌های کاربردی هستید، ONNX ممکن است انتخاب شما باشد. اگر از فریمورک و فناوری مشتق شده از llama.cpp استفاده می‌کنید، GGUF ممکن است گزینه بهتری باشد.

### **کوانتایز کردن Phi-3.5-Instruct با استفاده از llama.cpp**

**1. پیکربندی محیط**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. کوانتایز کردن**

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