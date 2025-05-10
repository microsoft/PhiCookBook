<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:21:38+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "bn"
}
-->
## **কিভাবে Model Builder ব্যবহার করে Phi-3.5 কে কোয়ান্টাইজ করবেন**

Model Builder এখন Phi-3.5 Instruct এবং Phi-3.5-Vision এর জন্য ONNX মডেল কোয়ান্টাইজেশন সাপোর্ট করে।

### **Phi-3.5-Instruct**

**CPU ত্বরান্বিত কোয়ান্টাইজড INT 4 রূপান্তর**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA ত্বরান্বিত কোয়ান্টাইজড INT 4 রূপান্তর**

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

2. মডেল ফোল্ডারে microsoft/Phi-3.5-vision-instruct ডাউনলোড করুন  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. নিচের ফাইলগুলো আপনার Phi-3.5-vision-instruct ফোল্ডারে ডাউনলোড করুন

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. এই ফাইলটি models ফোল্ডারে ডাউনলোড করুন  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. টার্মিনালে যান

    FP32 সহ ONNX সাপোর্ট রূপান্তর করুন

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **দ্রষ্টব্য:**

1. Model Builder বর্তমানে Phi-3.5-Instruct এবং Phi-3.5-Vision এর রূপান্তর সাপোর্ট করে, কিন্তু Phi-3.5-MoE সমর্থন করে না।

2. ONNX এর কোয়ান্টাইজড মডেল ব্যবহার করতে, আপনি Generative AI extensions for onnxruntime SDK ব্যবহার করতে পারেন।

3. আমরা আরও দায়িত্বশীল AI বিবেচনা করতে চাই, তাই মডেল কোয়ান্টাইজেশন রূপান্তরের পর আরও কার্যকর ফলাফল পরীক্ষা করার পরামর্শ দেওয়া হয়।

4. CPU INT4 মডেল কোয়ান্টাইজ করে আমরা এটি Edge ডিভাইসে ডিপ্লয় করতে পারি, যা আরও ভালো অ্যাপ্লিকেশন সিচুয়েশন তৈরি করে, তাই আমরা Phi-3.5-Instruct এর INT 4 এর আশেপাশে কাজ সম্পন্ন করেছি।

## **সম্পদসমূহ**

1. Generative AI extensions for onnxruntime সম্পর্কে আরও জানুন [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub রিপোজিটরি [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**বিস্তারিত বিবৃতি**:  
এই ডকুমেন্টটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ডকুমেন্টের স্থানীয় ভাষার সংস্করণকে কর্তৃপক্ষ হিসাবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।