# **onnxruntime এর জন্য Generative AI এক্সটেনশন ব্যবহার করে Phi পরিবার কোয়ান্টাইজ করা**

## **onnxruntime এর জন্য Generative AI এক্সটেনশন কি?**

এই এক্সটেনশনটি আপনাকে ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) দিয়ে জেনারেটিভ AI চালাতে সাহায্য করে। এটি ONNX মডেলগুলোর জন্য জেনারেটিভ AI লুপ প্রদান করে, যার মধ্যে রয়েছে ONNX Runtime ইনফারেন্স, লগিট প্রসেসিং, সার্চ এবং স্যাম্পলিং, এবং KV ক্যাশ ম্যানেজমেন্ট। ডেভেলপাররা একটি উচ্চ স্তরের generate() মেথড কল করতে পারেন, অথবা মডেলের প্রতিটি পুনরাবৃত্তি লুপে চালাতে পারেন, এক সময়ে একটি টোকেন জেনারেট করে, এবং প্রয়োজনে লুপের মধ্যে জেনারেশন প্যারামিটারগুলো আপডেট করতে পারেন। এতে greedy/beam সার্চ এবং TopP, TopK স্যাম্পলিং সমর্থন রয়েছে টোকেন সিকোয়েন্স জেনারেট করার জন্য এবং ইনবিল্ট লগিট প্রসেসিং যেমন repetition penalties রয়েছে। আপনি সহজেই কাস্টম স্কোরিংও যোগ করতে পারেন।

অ্যাপ্লিকেশন স্তরে, আপনি C++/ C# / Python ব্যবহার করে Generative AI এক্সটেনশন দিয়ে অ্যাপ্লিকেশন তৈরি করতে পারেন। মডেল স্তরে, আপনি এটি ব্যবহার করে ফাইন-টিউনড মডেলগুলো মের্জ করতে এবং সংশ্লিষ্ট কোয়ান্টিটেটিভ ডিপ্লয়মেন্ট কাজ করতে পারেন।


## **onnxruntime এর জন্য Generative AI এক্সটেনশন ব্যবহার করে Phi-3.5 কোয়ান্টাইজ করা**

### **সমর্থিত মডেল**

onnxruntime এর জন্য Generative AI এক্সটেনশন Microsoft Phi, Google Gemma, Mistral, Meta LLaMA এর কোয়ান্টাইজেশন রূপান্তর সমর্থন করে।


### **onnxruntime এর জন্য Generative AI এক্সটেনশনের Model Builder**

Model Builder অনেক দ্রুততর করে অপ্টিমাইজড এবং কোয়ান্টাইজড ONNX মডেল তৈরি করতে যা ONNX Runtime generate() API দিয়ে চালানো যায়।

Model Builder এর মাধ্যমে, আপনি মডেলকে INT4, INT8, FP16, FP32 তে কোয়ান্টাইজ করতে পারেন এবং CPU, CUDA, DirectML, Mobile ইত্যাদি বিভিন্ন হার্ডওয়্যার অ্যাক্সিলারেশন পদ্ধতির সংমিশ্রণ করতে পারেন।

Model Builder ব্যবহার করতে হলে আপনাকে ইনস্টল করতে হবে

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

ইনস্টলেশনের পরে, আপনি টার্মিনাল থেকে Model Builder স্ক্রিপ্ট চালিয়ে মডেল ফরম্যাট এবং কোয়ান্টাইজেশন রূপান্তর করতে পারেন।


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

প্রাসঙ্গিক প্যারামিটারগুলো বুঝুন

1. **model_name** এটি Hugging face এর মডেল, যেমন microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct ইত্যাদি। এটি আপনার মডেলের সংরক্ষিত পথও হতে পারে।

2. **path_to_output_folder** কোয়ান্টাইজড রূপান্তরের সংরক্ষণের পথ

3. **execution_provider** বিভিন্ন হার্ডওয়্যার অ্যাক্সিলারেশন সমর্থন, যেমন cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** আমরা মডেলটি Hugging face থেকে ডাউনলোড করি এবং স্থানীয়ভাবে ক্যাশ করি




***মন্তব্যঃ*** <ul>যদিও onnxruntime এর জন্য Generative AI এক্সটেনশন প্রিভিউ অবস্থায় রয়েছে, এগুলো Microsoft Olive এ অন্তর্ভুক্ত করা হয়েছে, এবং আপনি Microsoft Olive এর মাধ্যমে Generative AI এক্সটেনশন Model Builder ফাংশনগুলো কল করতে পারেন।</ul>

## **Model Builder দিয়ে Phi-3.5 কোয়ান্টাইজ করা কিভাবে করবেন**

Model Builder এখন Phi-3.5 Instruct এবং Phi-3.5-Vision এর ONNX মডেল কোয়ান্টাইজেশন সমর্থন করে

### **Phi-3.5-Instruct**


**কোয়ান্টাইজড INT 4 এর CPU অ্যাক্সিলারেটেড রূপান্তর**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**কোয়ান্টাইজড INT 4 এর CUDA অ্যাক্সিলারেটেড রূপান্তর**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. টার্মিনালে পরিবেশ সেট করুন

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct মডেল ফোল্ডারে ডাউনলোড করুন
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. নিম্নলিখিত ফাইলগুলো আপনার Phi-3.5-vision-instruct ফোল্ডারে ডাউনলোড করুন

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. এই ফাইলটি মডেল ফোল্ডারে ডাউনলোড করুন
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. টার্মিনালে যান

    FP32 দিয়ে ONNX সমর্থন রূপান্তর করুন


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **মন্তব্যঃ**

1. Model Builder বর্তমানে Phi-3.5-Instruct এবং Phi-3.5-Vision রূপান্তর সমর্থন করে, কিন্তু Phi-3.5-MoE সমর্থন করে না

2. ONNX এর কোয়ান্টাইজড মডেল ব্যবহার করতে, আপনি এটিকে Generative AI এক্সটেনশন for onnxruntime SDK-এর মাধ্যমে ব্যবহার করতে পারেন

3. আমাদের আরও জবাবদিহি AI বিবেচনা করতে হবে, সুতরাং মডেল কোয়ান্টাইজেশন রূপান্তরের পর অধিক কার্যকর ফলাফল পরীক্ষার পরামর্শ দেওয়া হয়

4. CPU INT4 মডেল কোয়ান্টাইজ করে আমরা এটিকে Edge ডিভাইসে ডিপ্লয় করতে পারি, যা ভালো অ্যাপ্লিকেশন স্কেনারিও রয়েছে, তাই আমরা Phi-3.5-Instruct INT 4 এর আশেপাশে সম্পন্ন করেছি


## **উপকরণ সমূহ**

1. onnxruntime এর জন্য Generative AI এক্সটেনশন সম্পর্কে আরো জানুন [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime এর জন্য Generative AI এক্সটেনশন GitHub রিপো [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->