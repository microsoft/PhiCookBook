## **কিভাবে Model Builder ব্যবহার করে Phi-3.5 কে কোয়ান্টাইজ করবেন**

Model Builder এখন Phi-3.5 Instruct এবং Phi-3.5-Vision এর জন্য ONNX মডেল কোয়ান্টাইজেশন সমর্থন করে।

### **Phi-3.5-Instruct**

**CPU ত্বরান্বিত কোয়ান্টাইজড INT4 রূপান্তর**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA ত্বরান্বিত কোয়ান্টাইজড INT4 রূপান্তর**

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

2. models ফোল্ডারে microsoft/Phi-3.5-vision-instruct ডাউনলোড করুন  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. নিচের ফাইলগুলো আপনার Phi-3.5-vision-instruct ফোল্ডারে ডাউনলোড করুন

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. models ফোল্ডারে এই ফাইলটি ডাউনলোড করুন  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. টার্মিনালে যান

    FP32 সহ ONNX সাপোর্ট রূপান্তর করুন

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **দ্রষ্টব্য:**

1. Model Builder বর্তমানে Phi-3.5-Instruct এবং Phi-3.5-Vision রূপান্তর সমর্থন করে, কিন্তু Phi-3.5-MoE সমর্থন করে না।

2. ONNX এর কোয়ান্টাইজড মডেল ব্যবহার করতে, আপনি Generative AI extensions for onnxruntime SDK এর মাধ্যমে এটি ব্যবহার করতে পারেন।

3. আরও দায়িত্বশীল AI বিবেচনা করার জন্য, মডেল কোয়ান্টাইজেশন রূপান্তরের পর আরও কার্যকর ফলাফল পরীক্ষা করার পরামর্শ দেওয়া হয়।

4. CPU INT4 মডেল কোয়ান্টাইজ করে আমরা এটিকে Edge Device এ ডিপ্লয় করতে পারি, যা আরও ভালো অ্যাপ্লিকেশন পরিস্থিতির জন্য উপযোগী, তাই আমরা Phi-3.5-Instruct এর INT4 এর আশেপাশে কাজ সম্পন্ন করেছি।

## **সংশ্লিষ্ট রিসোর্স**

1. Generative AI extensions for onnxruntime সম্পর্কে আরও জানুন [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub রিপোজিটরি [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।