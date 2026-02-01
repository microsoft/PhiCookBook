# ল্যাব। ডিভাইস-ভিত্তিক ইনফারেন্সের জন্য AI মডেল অপ্টিমাইজ করুন

## পরিচিতি

> [!IMPORTANT]  
> এই ল্যাবের জন্য **Nvidia A10 বা A100 GPU** এবং সংশ্লিষ্ট ড্রাইভার ও CUDA টুলকিট (ভার্সন 12+) ইনস্টল থাকা আবশ্যক।

> [!NOTE]  
> এটি একটি **৩৫ মিনিটের** ল্যাব যা আপনাকে OLIVE ব্যবহার করে ডিভাইস-ভিত্তিক ইনফারেন্সের জন্য মডেল অপ্টিমাইজেশনের মূল ধারণাগুলো হাতে-কলমে শেখাবে।

## শেখার উদ্দেশ্য

এই ল্যাব শেষ করার পর, আপনি OLIVE ব্যবহার করে করতে পারবেন:

- AWQ কোয়ান্টাইজেশন পদ্ধতি ব্যবহার করে একটি AI মডেল কোয়ান্টাইজ করা।
- একটি নির্দিষ্ট কাজের জন্য AI মডেল ফাইন-টিউন করা।
- ONNX Runtime-এ দক্ষ ডিভাইস-ভিত্তিক ইনফারেন্সের জন্য LoRA অ্যাডাপ্টার (ফাইন-টিউন করা মডেল) তৈরি করা।

### Olive কী

Olive (*O*NNX *live*) একটি মডেল অপ্টিমাইজেশন টুলকিট যার সাথে CLI রয়েছে, যা আপনাকে ONNX runtime +++https://onnxruntime.ai+++ এর জন্য গুণগত মান এবং কর্মক্ষমতা সহ মডেল সরবরাহ করতে সাহায্য করে।

![Olive Flow](../../../../../translated_images/bn/olive-flow.5daf97340275f8b6.webp)

Olive-এ ইনপুট সাধারণত একটি PyTorch বা Hugging Face মডেল হয় এবং আউটপুট একটি অপ্টিমাইজড ONNX মডেল যা ONNX runtime চালানো ডিভাইসে (ডিপ্লয়মেন্ট টার্গেট) এক্সিকিউট হয়। Olive মডেলটিকে ডিপ্লয়মেন্ট টার্গেটের AI অ্যাক্সিলারেটর (NPU, GPU, CPU) অনুযায়ী অপ্টিমাইজ করবে, যা Qualcomm, AMD, Nvidia বা Intel-এর মতো হার্ডওয়্যার ভেন্ডার দ্বারা সরবরাহিত।

Olive একটি *ওয়ার্কফ্লো* চালায়, যা একটির পর একটি সাজানো মডেল অপ্টিমাইজেশন টাস্কের সিকোয়েন্স, যাদের *পাস* বলা হয় - উদাহরণস্বরূপ: মডেল কম্প্রেশন, গ্রাফ ক্যাপচার, কোয়ান্টাইজেশন, গ্রাফ অপ্টিমাইজেশন। প্রতিটি পাসের কিছু প্যারামিটার থাকে যা সেরা মেট্রিক্স (যেমন সঠিকতা ও লেটেন্সি) অর্জনের জন্য টিউন করা যায়, যা সংশ্লিষ্ট ইভ্যালুয়েটর দ্বারা মূল্যায়িত হয়। Olive একটি সার্চ স্ট্র্যাটেজি ব্যবহার করে যা প্রতিটি পাস এক এক করে বা একসাথে পাসের সেটকে অটো-টিউন করে।

#### Olive-এর সুবিধাসমূহ

- গ্রাফ অপ্টিমাইজেশন, কম্প্রেশন এবং কোয়ান্টাইজেশনের বিভিন্ন পদ্ধতির জন্য ম্যানুয়াল ট্রায়াল-এন্ড-এরর কমিয়ে সময় বাঁচায়। আপনার গুণগত মান ও কর্মক্ষমতার সীমা নির্ধারণ করুন এবং Olive স্বয়ংক্রিয়ভাবে সেরা মডেল খুঁজে দেবে।
- **৪০+ বিল্ট-ইন মডেল অপ্টিমাইজেশন কম্পোনেন্ট** যা কোয়ান্টাইজেশন, কম্প্রেশন, গ্রাফ অপ্টিমাইজেশন এবং ফাইনটিউনিং-এর আধুনিক পদ্ধতি কভার করে।
- সাধারণ মডেল অপ্টিমাইজেশন টাস্কের জন্য সহজে ব্যবহারযোগ্য CLI। যেমন, olive quantize, olive auto-opt, olive finetune।
- মডেল প্যাকেজিং ও ডিপ্লয়মেন্ট অন্তর্ভুক্ত।
- **মাল্টি LoRA সার্ভিং** এর জন্য মডেল তৈরি সমর্থন করে।
- YAML/JSON ব্যবহার করে ওয়ার্কফ্লো তৈরি করে মডেল অপ্টিমাইজেশন ও ডিপ্লয়মেন্ট টাস্ক পরিচালনা করা যায়।
- **Hugging Face** এবং **Azure AI** ইন্টিগ্রেশন।
- বিল্ট-ইন **ক্যাশিং** মেকানিজম যা **খরচ সাশ্রয় করে**।

## ল্যাব নির্দেশিকা

> [!NOTE]  
> নিশ্চিত করুন যে আপনি Azure AI Hub এবং Project প্রোভিশন করেছেন এবং Lab 1 অনুযায়ী আপনার A100 কম্পিউট সেটআপ করেছেন।

### ধাপ ০: Azure AI Compute-এ সংযোগ করুন

**VS Code** এর রিমোট ফিচার ব্যবহার করে Azure AI Compute-এ সংযোগ করবেন।

1. আপনার **VS Code** ডেস্কটপ অ্যাপ্লিকেশন খুলুন।  
2. **Shift+Ctrl+P** চাপ দিয়ে **command palette** খুলুন।  
3. কমান্ড প্যালেটে **AzureML - remote: Connect to compute instance in New Window** সার্চ করুন।  
4. স্ক্রিনে প্রদর্শিত নির্দেশনা অনুসরণ করে Compute-এ সংযোগ করুন। এর মধ্যে আপনার Azure Subscription, Resource Group, Project এবং Lab 1-এ সেট করা Compute নাম নির্বাচন করা থাকবে।  
5. সংযোগ সফল হলে Visual Code-এর **নীচের বাম কোণে** `><Azure ML: Compute Name` দেখাবে।

### ধাপ ১: এই রিপো ক্লোন করুন

VS Code-এ নতুন টার্মিনাল খুলতে **Ctrl+J** চাপুন এবং এই রিপো ক্লোন করুন:

টার্মিনালে আপনি প্রম্পট দেখতে পাবেন

```
azureuser@computername:~/cloudfiles/code$ 
```  
সলিউশন ক্লোন করুন

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### ধাপ ২: VS Code-এ ফোল্ডার খুলুন

টার্মিনালে নিচের কমান্ড চালিয়ে সংশ্লিষ্ট ফোল্ডারটি VS Code-এ খুলুন, যা একটি নতুন উইন্ডো খুলবে:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

অথবা, **File** > **Open Folder** নির্বাচন করেও ফোল্ডারটি খুলতে পারেন।

### ধাপ ৩: ডিপেন্ডেন্সি ইনস্টল করুন

VS Code-এ Azure AI Compute Instance-এ একটি টার্মিনাল উইন্ডো খুলুন (টিপ: **Ctrl+J**) এবং নিচের কমান্ডগুলো চালিয়ে ডিপেন্ডেন্সি ইনস্টল করুন:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> সব ডিপেন্ডেন্সি ইনস্টল করতে প্রায় ৫ মিনিট সময় লাগবে।

এই ল্যাবে আপনি Azure AI Model ক্যাটালগ থেকে মডেল ডাউনলোড ও আপলোড করবেন। মডেল ক্যাটালগ অ্যাক্সেস করার জন্য Azure-এ লগইন করতে হবে:

```bash
az login
```

> [!NOTE]  
> লগইন করার সময় আপনাকে সাবস্ক্রিপশন নির্বাচন করতে বলা হবে। নিশ্চিত করুন যে আপনি এই ল্যাবের জন্য প্রদত্ত সাবস্ক্রিপশনটি নির্বাচন করেছেন।

### ধাপ ৪: Olive কমান্ড চালান

VS Code-এ Azure AI Compute Instance-এ একটি টার্মিনাল উইন্ডো খুলুন (টিপ: **Ctrl+J**) এবং নিশ্চিত করুন `olive-ai` কন্ডা এনভায়রনমেন্ট সক্রিয় আছে:

```bash
conda activate olive-ai
```

এরপর নিচের Olive কমান্ডগুলো চালান।

1. **ডেটা পরিদর্শন করুন:** এই উদাহরণে, আপনি Phi-3.5-Mini মডেল ফাইন-টিউন করবেন যাতে এটি ভ্রমণ সম্পর্কিত প্রশ্নের উত্তর দিতে বিশেষায়িত হয়। নিচের কোডটি JSON lines ফরম্যাটে ডেটাসেটের প্রথম কয়েকটি রেকর্ড দেখায়:

    ```bash
    head data/data_sample_travel.jsonl
    ```

2. **মডেল কোয়ান্টাইজ করুন:** মডেল ট্রেনিংয়ের আগে, নিচের কমান্ড দিয়ে Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ পদ্ধতি ব্যবহার করে কোয়ান্টাইজেশন করবেন। AWQ মডেলের ওজন কোয়ান্টাইজ করে ইনফারেন্সের সময় উৎপন্ন অ্যাক্টিভেশন বিবেচনা করে। এর ফলে কোয়ান্টাইজেশন প্রক্রিয়া অ্যাক্টিভেশনের প্রকৃত ডেটা ডিস্ট্রিবিউশন বিবেচনা করে, যা প্রচলিত ওজন কোয়ান্টাইজেশন পদ্ধতির তুলনায় মডেলের সঠিকতা ভালোভাবে সংরক্ষণ করে।

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ কোয়ান্টাইজেশন সম্পন্ন হতে **প্রায় ৮ মিনিট** সময় লাগে, যা মডেলের সাইজ প্রায় **৭.৫GB থেকে ২.৫GB** এ কমিয়ে দেয়।

    এই ল্যাবে আমরা Hugging Face থেকে মডেল ইনপুট দেখাচ্ছি (যেমন: `microsoft/Phi-3.5-mini-instruct`)। তবে Olive Azure AI ক্যাটালগ থেকে মডেল ইনপুট নেওয়ার সুবিধাও দেয়, যেখানে `model_name_or_path` আর্গুমেন্টে Azure AI অ্যাসেট আইডি ব্যবহার করতে হবে (যেমন: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`)।

3. **মডেল ট্রেন করুন:** এরপর, `olive finetune` কমান্ড কোয়ান্টাইজড মডেল ফাইন-টিউন করবে। কোয়ান্টাইজেশনের পরে নয়, আগে ফাইন-টিউন করলে সঠিকতা ভালো হয় কারণ ফাইন-টিউনিং কোয়ান্টাইজেশন থেকে কিছু ক্ষতি পুনরুদ্ধার করে।

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    ফাইন-টিউনিং (১০০ স্টেপ) সম্পন্ন হতে **প্রায় ৬ মিনিট** সময় লাগে।

4. **অপ্টিমাইজ করুন:** মডেল ট্রেনিংয়ের পর, Olive-এর `auto-opt` কমান্ড ব্যবহার করে মডেল অপ্টিমাইজ করুন। এটি ONNX গ্রাফ ক্যাপচার করে এবং মডেল পারফরম্যান্স উন্নত করতে CPU-এর জন্য মডেল কম্প্রেশন ও ফিউশন স্বয়ংক্রিয়ভাবে করে। উল্লেখ্য, আপনি `--device` এবং `--provider` আর্গুমেন্ট পরিবর্তন করে NPU বা GPU-এর জন্যও অপ্টিমাইজ করতে পারেন, কিন্তু এই ল্যাবে CPU ব্যবহার করা হবে।

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    অপ্টিমাইজেশন সম্পন্ন হতে **প্রায় ৫ মিনিট** সময় লাগে।

### ধাপ ৫: মডেল ইনফারেন্স দ্রুত পরীক্ষা

মডেল ইনফারেন্স পরীক্ষা করার জন্য আপনার ফোল্ডারে **app.py** নামে একটি পাইথন ফাইল তৈরি করুন এবং নিচের কোড কপি-পেস্ট করুন:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

কোড চালাতে:

```bash
python app.py
```

### ধাপ ৬: মডেল Azure AI-তে আপলোড করুন

মডেল Azure AI মডেল রিপোজিটরিতে আপলোড করলে এটি আপনার ডেভেলপমেন্ট টিমের অন্যান্য সদস্যদের সাথে শেয়ারযোগ্য হয় এবং মডেলের ভার্সন কন্ট্রোলও সহজ হয়। মডেল আপলোড করতে নিচের কমান্ড চালান:

> [!NOTE]  
> `{}` প্লেসহোল্ডারগুলো আপনার রিসোর্স গ্রুপ এবং Azure AI প্রজেক্ট নাম দিয়ে আপডেট করুন।

আপনার রিসোর্স গ্রুপ `"resourceGroup"` এবং Azure AI প্রজেক্ট নাম জানতে নিচের কমান্ড চালান:

```
az ml workspace show
```

অথবা +++ai.azure.com+++ এ গিয়ে **management center** > **project** > **overview** থেকে দেখতে পারেন।

`{}` প্লেসহোল্ডারগুলো আপনার রিসোর্স গ্রুপ এবং Azure AI প্রজেক্ট নাম দিয়ে আপডেট করুন।

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

আপলোড করা মডেল দেখতে এবং ডিপ্লয় করতে https://ml.azure.com/model/list এ যান।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।