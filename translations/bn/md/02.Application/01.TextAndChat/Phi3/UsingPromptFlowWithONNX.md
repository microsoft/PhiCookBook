<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T02:58:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "bn"
}
-->
# Windows GPU ব্যবহার করে Phi-3.5-Instruct ONNX সহ Prompt flow সলিউশন তৈরি করা

নিম্নলিখিত ডকুমেন্টটি Phi-3 মডেলের উপর ভিত্তি করে AI অ্যাপ্লিকেশন তৈরি করার জন্য ONNX (Open Neural Network Exchange) সহ PromptFlow ব্যবহারের একটি উদাহরণ।

PromptFlow হল একটি ডেভেলপমেন্ট টুলসের স্যুট যা LLM-ভিত্তিক (Large Language Model) AI অ্যাপ্লিকেশনগুলোর সম্পূর্ণ ডেভেলপমেন্ট সাইকেলকে সহজতর করার জন্য ডিজাইন করা হয়েছে, আইডিয়া থেকে প্রোটোটাইপিং, টেস্টিং এবং মূল্যায়ন পর্যন্ত।

PromptFlow কে ONNX এর সাথে ইন্টিগ্রেট করে ডেভেলপাররা করতে পারেন:

- মডেল পারফরম্যান্স অপ্টিমাইজ করা: ONNX ব্যবহার করে দক্ষ মডেল ইনফারেন্স এবং ডিপ্লয়মেন্ট।
- ডেভেলপমেন্ট সহজতর করা: PromptFlow ব্যবহার করে ওয়ার্কফ্লো ম্যানেজ করা এবং পুনরাবৃত্তিমূলক কাজগুলো অটোমেট করা।
- সহযোগিতা বাড়ানো: একটি একক ডেভেলপমেন্ট পরিবেশ প্রদান করে টিম মেম্বারদের মধ্যে ভালো সহযোগিতা নিশ্চিত করা।

**Prompt flow** হল একটি ডেভেলপমেন্ট টুলসের স্যুট যা LLM-ভিত্তিক AI অ্যাপ্লিকেশনগুলোর সম্পূর্ণ ডেভেলপমেন্ট সাইকেলকে সহজতর করে, আইডিয়া, প্রোটোটাইপিং, টেস্টিং, মূল্যায়ন থেকে প্রোডাকশন ডিপ্লয়মেন্ট এবং মনিটরিং পর্যন্ত। এটি প্রম্পট ইঞ্জিনিয়ারিংকে অনেক সহজ করে তোলে এবং আপনাকে প্রোডাকশন মানের LLM অ্যাপ তৈরি করতে সাহায্য করে।

Prompt flow OpenAI, Azure OpenAI Service, এবং কাস্টমাইজযোগ্য মডেল (Huggingface, লোকাল LLM/SLM) এর সাথে সংযুক্ত হতে পারে। আমরা Phi-3.5 এর কোয়ান্টাইজড ONNX মডেল লোকাল অ্যাপ্লিকেশনে ডিপ্লয় করার আশা করছি। Prompt flow আমাদের ব্যবসা আরও ভালোভাবে পরিকল্পনা করতে এবং Phi-3.5 ভিত্তিক লোকাল সলিউশন সম্পন্ন করতে সাহায্য করবে। এই উদাহরণে, আমরা Windows GPU ভিত্তিক Prompt flow সলিউশন সম্পন্ন করতে ONNX Runtime GenAI লাইব্রেরি ব্যবহার করব।

## **ইনস্টলেশন**

### **Windows GPU এর জন্য ONNX Runtime GenAI**

Windows GPU এর জন্য ONNX Runtime GenAI সেটআপ করার নির্দেশিকা পড়তে [এখানে ক্লিক করুন](./ORTWindowGPUGuideline.md)

### **VSCode এ Prompt flow সেটআপ করা**

1. Prompt flow VS Code এক্সটেনশন ইনস্টল করুন

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbe.bn.png)

2. Prompt flow VS Code এক্সটেনশন ইনস্টল করার পর, এক্সটেনশনটি ক্লিক করুন এবং **Installation dependencies** নির্বাচন করুন, এই নির্দেশিকা অনুসরণ করে আপনার পরিবেশে Prompt flow SDK ইনস্টল করুন

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f.bn.png)

3. [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) ডাউনলোড করুন এবং VS Code দিয়ে এই স্যাম্পলটি খুলুন

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4.bn.png)

4. **flow.dag.yaml** খুলে আপনার Python পরিবেশ নির্বাচন করুন

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff.bn.png)

   **chat_phi3_ort.py** খুলে আপনার Phi-3.5-instruct ONNX মডেলের অবস্থান পরিবর্তন করুন

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45f.bn.png)

5. আপনার prompt flow চালিয়ে পরীক্ষা করুন

**flow.dag.yaml** খুলে ভিজ্যুয়াল এডিটর ক্লিক করুন

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603.bn.png)

এটি ক্লিক করার পর চালিয়ে পরীক্ষা করুন

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b.bn.png)

1. আপনি টার্মিনালে ব্যাচ রান করে আরও ফলাফল পরীক্ষা করতে পারেন


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

আপনি আপনার ডিফল্ট ব্রাউজারে ফলাফল দেখতে পারবেন


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cb.bn.png)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।