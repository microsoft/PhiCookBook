<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:06:41+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "bn"
}
-->
## VS Code এর জন্য AI Toolkit এ স্বাগতম

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) Azure AI Studio Catalog এবং Hugging Face-এর মতো অন্যান্য ক্যাটালগ থেকে বিভিন্ন মডেল একত্রিত করে। এই টুলকিটটি জেনারেটিভ AI টুলস এবং মডেল ব্যবহার করে AI অ্যাপ তৈরি করার সাধারণ ডেভেলপমেন্ট কাজগুলোকে সহজ করে তোলে:
- মডেল আবিষ্কার এবং প্লেগ্রাউন্ড দিয়ে শুরু করুন।
- স্থানীয় কম্পিউটিং রিসোর্স ব্যবহার করে মডেল ফাইন-টিউনিং এবং ইনফারেন্স।
- Azure রিসোর্স ব্যবহার করে রিমোট ফাইন-টিউনিং এবং ইনফারেন্স।

[VSCode এর জন্য AI Toolkit ইনস্টল করুন](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.7157953df04812dc.bn.png)

**[Private Preview]** ক্লাউডে মডেল ফাইন-টিউনিং এবং ইনফারেন্স চালানোর জন্য Azure Container Apps এর এক-ক্লিক প্রোভিশনিং।

এখন চলুন আপনার AI অ্যাপ ডেভেলপমেন্ট শুরু করি:

- [VS Code এর জন্য AI Toolkit এ স্বাগতম](../../../../md/03.FineTuning)
- [স্থানীয় ডেভেলপমেন্ট](../../../../md/03.FineTuning)
  - [প্রস্তুতি](../../../../md/03.FineTuning)
  - [কন্ডা সক্রিয়করণ](../../../../md/03.FineTuning)
  - [শুধুমাত্র বেস মডেল ফাইন-টিউনিং](../../../../md/03.FineTuning)
  - [মডেল ফাইন-টিউনিং এবং ইনফারেন্স](../../../../md/03.FineTuning)
  - [মডেল ফাইন-টিউনিং](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [ফাইন টিউনিং স্যাম্পল এবং রিসোর্স](../../../../md/03.FineTuning)
- [**\[Private Preview\]** রিমোট ডেভেলপমেন্ট](../../../../md/03.FineTuning)
  - [প্রয়োজনীয়তা](../../../../md/03.FineTuning)
  - [রিমোট ডেভেলপমেন্ট প্রজেক্ট সেটআপ](../../../../md/03.FineTuning)
  - [Azure রিসোর্স প্রোভিশন করুন](../../../../md/03.FineTuning)
  - [\[ঐচ্ছিক\] Azure Container App Secret-এ Huggingface Token যোগ করুন](../../../../md/03.FineTuning)
  - [ফাইন-টিউনিং চালান](../../../../md/03.FineTuning)
  - [ইনফারেন্স এন্ডপয়েন্ট প্রোভিশন করুন](../../../../md/03.FineTuning)
  - [ইনফারেন্স এন্ডপয়েন্ট ডিপ্লয় করুন](../../../../md/03.FineTuning)
  - [উন্নত ব্যবহার](../../../../md/03.FineTuning)

## স্থানীয় ডেভেলপমেন্ট
### প্রস্তুতি

1. নিশ্চিত করুন হোস্টে NVIDIA ড্রাইভার ইনস্টল করা আছে।
2. যদি HF dataset ব্যবহার করেন, তাহলে `huggingface-cli login` চালান।
3. `Olive` কী সেটিংস ব্যাখ্যা করে যা মেমোরি ব্যবহারে পরিবর্তন আনে।

### কন্ডা সক্রিয়করণ
আমরা WSL পরিবেশ ব্যবহার করছি এবং এটি শেয়ার করা, তাই আপনাকে ম্যানুয়ালি কন্ডা পরিবেশ সক্রিয় করতে হবে। এই ধাপের পর আপনি ফাইন-টিউনিং বা ইনফারেন্স চালাতে পারবেন।

```bash
conda activate [conda-env-name] 
```

### শুধুমাত্র বেস মডেল ফাইন-টিউনিং
শুধুমাত্র বেস মডেল চেষ্টা করতে চাইলে কন্ডা সক্রিয় করার পর নিচের কমান্ডটি চালান।

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### মডেল ফাইন-টিউনিং এবং ইনফারেন্স

যখন ডেভ কন্টেইনারে ওয়ার্কস্পেস খোলা হবে, একটি টার্মিনাল খুলুন (ডিফল্ট পাথ হলো প্রজেক্ট রুট), তারপর নিচের কমান্ডটি চালিয়ে নির্বাচিত dataset এ LLM ফাইন-টিউন করুন।

```bash
python finetuning/invoke_olive.py 
```

চেকপয়েন্ট এবং চূড়ান্ত মডেল `models` ফোল্ডারে সংরক্ষিত হবে।

এরপর ফাইন-টিউন করা মডেল দিয়ে `console`, `web browser` বা `prompt flow` এর মাধ্যমে ইনফারেন্স চালান।

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

VS Code এ `prompt flow` ব্যবহার করতে, এই [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html) দেখুন।

### মডেল ফাইন-টিউনিং

এরপর, আপনার ডিভাইসে GPU এর উপস্থিতি অনুযায়ী নিচের মডেলটি ডাউনলোড করুন।

QLoRA ব্যবহার করে স্থানীয় ফাইন-টিউনিং সেশন শুরু করতে, আমাদের ক্যাটালগ থেকে ফাইন-টিউন করতে চান এমন মডেল নির্বাচন করুন।
| প্ল্যাটফর্ম | GPU আছে | মডেল নাম | সাইজ (GB) |
|---------|---------|--------|--------|
| Windows | আছে | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | আছে | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | নেই | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_দ্রষ্টব্য_** মডেল ডাউনলোড করতে Azure Account এর প্রয়োজন নেই।

Phi3-mini (int4) মডেল প্রায় ২GB-৩GB সাইজের। আপনার নেটওয়ার্ক স্পিড অনুযায়ী ডাউনলোডে কয়েক মিনিট লাগতে পারে।

প্রথমে একটি প্রজেক্ট নাম এবং অবস্থান নির্বাচন করুন।
এরপর মডেল ক্যাটালগ থেকে একটি মডেল নির্বাচন করুন। আপনাকে প্রজেক্ট টেমপ্লেট ডাউনলোড করতে বলা হবে। তারপর "Configure Project" ক্লিক করে বিভিন্ন সেটিংস সামঞ্জস্য করুন।

### Microsoft Olive

আমরা [Olive](https://microsoft.github.io/Olive/why-olive.html) ব্যবহার করি আমাদের ক্যাটালগ থেকে PyTorch মডেলে QLoRA ফাইন-টিউনিং চালানোর জন্য। সব সেটিংস ডিফল্ট মানে প্রিসেট করা থাকে যাতে মেমোরি অপ্টিমাইজ করে স্থানীয়ভাবে ফাইন-টিউনিং প্রক্রিয়া চালানো যায়, তবে আপনার প্রয়োজন অনুযায়ী এটি পরিবর্তন করা যেতে পারে।

### ফাইন টিউনিং স্যাম্পল এবং রিসোর্স

- [ফাইন টিউনিং শুরু করার গাইড](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [HuggingFace Dataset দিয়ে ফাইন টিউনিং](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [সহজ Dataset দিয়ে ফাইন টিউনিং](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** রিমোট ডেভেলপমেন্ট

### প্রয়োজনীয়তা

1. আপনার রিমোট Azure Container App পরিবেশে মডেল ফাইন-টিউনিং চালাতে, নিশ্চিত করুন আপনার সাবস্ক্রিপশনে পর্যাপ্ত GPU ক্যাপাসিটি আছে। আপনার অ্যাপ্লিকেশনের জন্য প্রয়োজনীয় ক্যাপাসিটি পেতে একটি [সাপোর্ট টিকিট](https://azure.microsoft.com/support/create-ticket/) জমা দিন। [GPU ক্যাপাসিটি সম্পর্কে আরও তথ্য](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. যদি আপনি HuggingFace এর প্রাইভেট dataset ব্যবহার করেন, নিশ্চিত করুন আপনার একটি [HuggingFace অ্যাকাউন্ট](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) আছে এবং [একটি access token তৈরি করেছেন](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. AI Toolkit for VS Code এ Remote Fine-tuning এবং Inference ফিচার ফ্ল্যাগ সক্রিয় করুন
   1. VS Code সেটিংস খুলুন *File -> Preferences -> Settings* থেকে।
   2. *Extensions* এ যান এবং *AI Toolkit* নির্বাচন করুন।
   3. *"Enable Remote Fine-tuning And Inference"* অপশনটি নির্বাচন করুন।
   4. পরিবর্তন কার্যকর করতে VS Code রিলোড করুন।

- [রিমোট ফাইন টিউনিং](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### রিমোট ডেভেলপমেন্ট প্রজেক্ট সেটআপ
1. কমান্ড প্যালেট থেকে `AI Toolkit: Focus on Resource View` চালান।
2. *Model Fine-tuning* এ যান মডেল ক্যাটালগ অ্যাক্সেস করতে। আপনার প্রজেক্টের জন্য একটি নাম দিন এবং আপনার মেশিনে অবস্থান নির্বাচন করুন। তারপর *"Configure Project"* বাটনে ক্লিক করুন।
3. প্রজেক্ট কনফিগারেশন
    1. *"Fine-tune locally"* অপশনটি সক্রিয় করবেন না।
    2. Olive কনফিগারেশন সেটিংস ডিফল্ট মান সহ প্রদর্শিত হবে। প্রয়োজন অনুযায়ী এগুলো পরিবর্তন ও পূরণ করুন।
    3. *Generate Project* এ যান। এই ধাপে WSL ব্যবহার করে নতুন Conda পরিবেশ তৈরি করা হবে, যা ভবিষ্যতে Dev Containers আপডেটের জন্য প্রস্তুত।
4. *"Relaunch Window In Workspace"* ক্লিক করে আপনার রিমোট ডেভেলপমেন্ট প্রজেক্ট খুলুন।

> **দ্রষ্টব্য:** এই প্রজেক্ট বর্তমানে AI Toolkit for VS Code এ স্থানীয় বা রিমোট উভয়ভাবেই কাজ করে। যদি প্রজেক্ট তৈরির সময় *"Fine-tune locally"* নির্বাচন করেন, তাহলে এটি শুধুমাত্র WSL এ চলবে এবং রিমোট ডেভেলপমেন্ট সাপোর্ট করবে না। অন্যদিকে, যদি *"Fine-tune locally"* সক্রিয় না করেন, প্রজেক্টটি শুধুমাত্র রিমোট Azure Container App পরিবেশে সীমাবদ্ধ থাকবে।

### Azure রিসোর্স প্রোভিশন করুন
শুরু করতে, রিমোট ফাইন-টিউনিং এর জন্য Azure রিসোর্স প্রোভিশন করতে হবে। কমান্ড প্যালেট থেকে `AI Toolkit: Provision Azure Container Apps job for fine-tuning` চালান।

আউটপুট চ্যানেলে প্রদর্শিত লিঙ্ক থেকে প্রোভিশনিং প্রগ্রেস মনিটর করুন।

### [ঐচ্ছিক] Azure Container App Secret-এ Huggingface Token যোগ করুন
আপনি যদি প্রাইভেট HuggingFace dataset ব্যবহার করেন, তাহলে HuggingFace টোকেনটি একটি পরিবেশ ভেরিয়েবল হিসেবে সেট করুন যাতে ম্যানুয়ালি লগইন করার প্রয়োজন না হয়।
`AI Toolkit: Add Azure Container Apps Job secret for fine-tuning` কমান্ড ব্যবহার করে আপনি সিক্রেট নাম [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) সেট করতে পারেন এবং আপনার Hugging Face টোকেন সিক্রেট মান হিসেবে ব্যবহার করতে পারেন।

### ফাইন-টিউনিং চালান
রিমোট ফাইন-টিউনিং কাজ শুরু করতে `AI Toolkit: Run fine-tuning` কমান্ড চালান।

সিস্টেম এবং কনসোল লগ দেখতে, আউটপুট প্যানেলে প্রদর্শিত লিঙ্ক থেকে Azure পোর্টালে যান (আরো তথ্যের জন্য [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure) দেখুন)। অথবা, VSCode আউটপুট প্যানেলে সরাসরি লগ দেখতে `AI Toolkit: Show the running fine-tuning job streaming logs` কমান্ড চালান।  
> **দ্রষ্টব্য:** পর্যাপ্ত রিসোর্স না থাকায় কাজটি কিউতে থাকতে পারে। যদি লগ না দেখায়, `AI Toolkit: Show the running fine-tuning job streaming logs` কমান্ড চালিয়ে কিছুক্ষণ অপেক্ষা করুন এবং পুনরায় কমান্ড চালান স্ট্রিমিং লগ পুনরায় সংযোগের জন্য।

এই প্রক্রিয়ায় QLoRA ব্যবহার করে ফাইন-টিউনিং হবে এবং মডেলের জন্য LoRA অ্যাডাপ্টার তৈরি করা হবে ইনফারেন্সের সময় ব্যবহারের জন্য।  
ফাইন-টিউনিং এর ফলাফল Azure Files এ সংরক্ষিত হবে।

### ইনফারেন্স এন্ডপয়েন্ট প্রোভিশন করুন
রিমোট পরিবেশে অ্যাডাপ্টার প্রশিক্ষণের পর, মডেলের সাথে ইন্টারঅ্যাক্ট করতে একটি সহজ Gradio অ্যাপ্লিকেশন ব্যবহার করুন।  
ফাইন-টিউনিং এর মতো, রিমোট ইনফারেন্সের জন্য Azure রিসোর্স সেটআপ করতে কমান্ড প্যালেট থেকে `AI Toolkit: Provision Azure Container Apps for inference` চালান।

ডিফল্টভাবে, সাবস্ক্রিপশন এবং রিসোর্স গ্রুপ ফাইন-টিউনিং এর জন্য ব্যবহৃত সেটিংসের সাথে মিলে যাবে। ইনফারেন্স একই Azure Container App Environment ব্যবহার করবে এবং Azure Files এ সংরক্ষিত মডেল ও মডেল অ্যাডাপ্টার অ্যাক্সেস করবে, যা ফাইন-টিউনিং ধাপে তৈরি হয়েছিল।

### ইনফারেন্স এন্ডপয়েন্ট ডিপ্লয় করুন
আপনি যদি ইনফারেন্স কোড সংশোধন বা ইনফারেন্স মডেল রিলোড করতে চান, তাহলে `AI Toolkit: Deploy for inference` কমান্ড চালান। এটি আপনার সর্বশেষ কোড Azure Container App এর সাথে সিঙ্ক্রোনাইজ করবে এবং রেপ্লিকা রিস্টার্ট করবে।

ডিপ্লয়মেন্ট সফল হলে, VSCode নোটিফিকেশনে প্রদর্শিত "*Go to Inference Endpoint*" বাটনে ক্লিক করে ইনফারেন্স API অ্যাক্সেস করতে পারবেন। অথবা, ওয়েব API এন্ডপয়েন্ট `ACA_APP_ENDPOINT` এ পাওয়া যাবে `./infra/inference.config.json` ফাইলে এবং আউটপুট প্যানেলে। এখন আপনি এই এন্ডপয়েন্ট ব্যবহার করে মডেল মূল্যায়ন করতে প্রস্তুত।

### উন্নত ব্যবহার
AI Toolkit দিয়ে রিমোট ডেভেলপমেন্ট সম্পর্কে আরও তথ্যের জন্য, [Fine-Tuning models remotely](https://aka.ms/ai-toolkit/remote-provision) এবং [Inferencing with the fine-tuned model](https://aka.ms/ai-toolkit/remote-inference) ডকুমেন্টেশন দেখুন।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।