<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:18:57+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "bg"
}
-->
# **Квантоване на Phi Family с помощта на llama.cpp**

## **Какво е llama.cpp**

llama.cpp е софтуерна библиотека с отворен код, основно написана на C++, която извършва инференция върху различни големи езикови модели (LLMs), като Llama. Основната ѝ цел е да осигури най-съвременна производителност за инференция на LLM на разнообразен хардуер с минимална настройка. Освен това има налични Python обвивки за тази библиотека, които предлагат високо ниво API за допълване на текст и уеб сървър съвместим с OpenAI.

Основната цел на llama.cpp е да позволи инференция на LLM с минимална настройка и водеща в бранша производителност на широк спектър от хардуер – както локално, така и в облака.

- Чиста C/C++ реализация без зависимости
- Apple silicon е приоритет – оптимизирана чрез ARM NEON, Accelerate и Metal рамки
- Поддръжка на AVX, AVX2 и AVX512 за x86 архитектури
- Квантоване с 1.5, 2, 3, 4, 5, 6 и 8 бита за по-бърза инференция и намалена консумация на памет
- Специални CUDA ядра за изпълнение на LLM на NVIDIA GPU (поддръжка за AMD GPU чрез HIP)
- Поддръжка на Vulkan и SYCL бекенд
- Хибридна инференция CPU+GPU за частично ускорение на модели, по-големи от общия капацитет на VRAM

## **Квантоване на Phi-3.5 с llama.cpp**

Моделът Phi-3.5-Instruct може да бъде квантован с помощта на llama.cpp, но Phi-3.5-Vision и Phi-3.5-MoE все още не се поддържат. Форматът, конвертиран от llama.cpp, е gguf, който е и най-широко използваният формат за квантоване.

Има голям брой квантовани модели в GGUF формат в Hugging Face. AI Foundry, Ollama и LlamaEdge използват llama.cpp, затова GGUF моделите също са често използвани.

### **Какво е GGUF**

GGUF е двоичен формат, оптимизиран за бързо зареждане и записване на модели, което го прави много ефективен за инференция. GGUF е проектиран за работа с GGML и други изпълнители. GGUF е разработен от @ggerganov, който е и създател на llama.cpp – популярна C/C++ рамка за инференция на LLM. Модели, първоначално разработени във фреймуъркове като PyTorch, могат да бъдат конвертирани в GGUF формат за използване с тези изпълнители.

### **ONNX срещу GGUF**

ONNX е традиционен формат за машинно обучение/дълбоко обучение, който е добре поддържан в различни AI фреймуъркове и има добри приложения в устройства на ръба (edge devices). GGUF, от своя страна, е базиран на llama.cpp и може да се каже, че е създаден в ерата на GenAI. Двата формата имат сходни приложения. Ако търсите по-добра производителност на вградени хардуерни устройства и в приложни слоеве, ONNX може да е по-добрият избор. Ако използвате производни фреймуъркове и технологии на llama.cpp, тогава GGUF може да е по-подходящ.

### **Квантоване на Phi-3.5-Instruct с llama.cpp**

**1. Конфигуриране на средата**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Квантоване**

Използване на llama.cpp за конвертиране на Phi-3.5-Instruct в FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Квантоване на Phi-3.5 до INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Тестване**

Инсталиране на llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Note*** 

Ако използвате Apple Silicon, моля инсталирайте llama-cpp-python по следния начин


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Тестване 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Ресурси**

1. Научете повече за llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Научете повече за onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Научете повече за GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или погрешни тълкувания, произтичащи от използването на този превод.