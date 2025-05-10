<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:05:23+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "bn"
}
-->
# **llama.cpp ব্যবহার করে Phi ফ্যামিলি কোয়ান্টাইজেশন**

## **llama.cpp কী**

llama.cpp হলো একটি ওপেন-সোর্স সফটওয়্যার লাইব্রেরি যা প্রধানত C++ ভাষায় লেখা এবং বিভিন্ন বড় ভাষা মডেলের (LLMs) উপর ইনফারেন্স করে, যেমন Llama। এর প্রধান উদ্দেশ্য হলো কম সেটআপের মাধ্যমে বিভিন্ন হার্ডওয়্যারে সর্বাধুনিক পারফরম্যান্স দিয়ে LLM ইনফারেন্স প্রদান করা। এছাড়াও, এই লাইব্রেরির জন্য পাইথন বাইন্ডিংস রয়েছে, যা টেক্সট কমপ্লিশনের জন্য উচ্চস্তরের API এবং OpenAI-সঙ্গত ওয়েব সার্ভার প্রদান করে।

llama.cpp এর মূল লক্ষ্য হলো কম সেটআপে এবং সর্বাধুনিক পারফরম্যান্সে স্থানীয় ও ক্লাউড উভয় পরিবেশে বিভিন্ন হার্ডওয়্যারে LLM ইনফারেন্স সক্ষম করা।

- কোন ডিপেন্ডেন্সি ছাড়া সরল C/C++ ইমপ্লিমেন্টেশন
- Apple silicon সম্পূর্ণ সাপোর্টেড - ARM NEON, Accelerate এবং Metal ফ্রেমওয়ার্ক ব্যবহার করে অপ্টিমাইজড
- x86 আর্কিটেকচারের জন্য AVX, AVX2 এবং AVX512 সাপোর্ট
- দ্রুত ইনফারেন্স এবং কম মেমোরি ব্যবহারের জন্য ১.৫-বিট, ২-বিট, ৩-বিট, ৪-বিট, ৫-বিট, ৬-বিট এবং ৮-বিট ইন্টিজার কোয়ান্টাইজেশন
- NVIDIA GPU তে LLM চালানোর জন্য কাস্টম CUDA কার্নেল (AMD GPU এর জন্য HIP সাপোর্ট)
- Vulkan এবং SYCL ব্যাকএন্ড সাপোর্ট
- মোট VRAM ক্যাপাসিটির চেয়ে বড় মডেলগুলোর জন্য CPU+GPU হাইব্রিড ইনফারেন্স আংশিক ত্বরান্বিত করতে

## **llama.cpp দিয়ে Phi-3.5 কোয়ান্টাইজেশন**

Phi-3.5-Instruct মডেলটি llama.cpp ব্যবহার করে কোয়ান্টাইজ করা যায়, তবে Phi-3.5-Vision এবং Phi-3.5-MoE এখনও সাপোর্টেড নয়। llama.cpp দ্বারা রূপান্তরিত ফরম্যাট হলো gguf, যা সবচেয়ে বেশি ব্যবহৃত কোয়ান্টাইজেশন ফরম্যাট।

Hugging face এ অনেক কোয়ান্টাইজড GGUF ফরম্যাট মডেল পাওয়া যায়। AI Foundry, Ollama এবং LlamaEdge llama.cpp এর উপর নির্ভরশীল, তাই GGUF মডেলগুলোও প্রায়শই ব্যবহৃত হয়।

### **GGUF কী**

GGUF হলো একটি বাইনারি ফরম্যাট যা মডেল লোড এবং সেভ করার জন্য অপ্টিমাইজড, ফলে ইনফারেন্সের জন্য খুবই কার্যকর। GGUF GGML এবং অন্যান্য এক্সিকিউটরদের জন্য ডিজাইন করা হয়েছে। GGUF তৈরি করেছেন @ggerganov, যিনি llama.cpp এর ডেভেলপারও। PyTorch-এর মতো ফ্রেমওয়ার্কে প্রথমে তৈরি মডেলগুলো GGUF ফরম্যাটে রূপান্তরিত করে এই ইঞ্জিনগুলোতে ব্যবহার করা যায়।

### **ONNX বনাম GGUF**

ONNX হলো একটি প্রচলিত মেশিন লার্নিং/ডিপ লার্নিং ফরম্যাট, যা বিভিন্ন AI ফ্রেমওয়ার্কে ভালো সাপোর্টেড এবং এজ ডিভাইসে ব্যবহারের জন্য উপযোগী। GGUF হলো llama.cpp ভিত্তিক এবং বলা যায় এটি GenAI যুগে তৈরি। দুটির ব্যবহার অনেকটা মিল। এমবেডেড হার্ডওয়্যার এবং অ্যাপ্লিকেশন স্তরে ভালো পারফরম্যান্স চাইলে ONNX ভালো বিকল্প। আর llama.cpp এর ডেরিভেটিভ ফ্রেমওয়ার্ক এবং প্রযুক্তি ব্যবহার করলে GGUF বেটার হতে পারে।

### **llama.cpp দিয়ে Phi-3.5-Instruct কোয়ান্টাইজেশন**

**১. পরিবেশ কনফিগারেশন**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**২. কোয়ান্টাইজেশন**

llama.cpp ব্যবহার করে Phi-3.5-Instruct কে FP16 GGUF তে রূপান্তর করুন


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 কে INT4 তে কোয়ান্টাইজ করা


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**৩. টেস্টিং**

llama-cpp-python ইনস্টল করুন


```bash

pip install llama-cpp-python -U

```

***Note*** 

যদি Apple Silicon ব্যবহার করেন, তাহলে llama-cpp-python এর ইনস্টলেশন এভাবে করুন


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

টেস্টিং 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **সংশ্লিষ্ট রিসোর্স**

1. llama.cpp সম্পর্কে আরও জানুন [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. onnxruntime সম্পর্কে আরও জানুন [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. GGUF সম্পর্কে আরও জানুন [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**অস্বীকারোক্তি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।