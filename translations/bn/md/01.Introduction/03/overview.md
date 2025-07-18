<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:08:33+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "bn"
}
-->
Phi-3-mini এর প্রসঙ্গে, inference বলতে বোঝায় মডেল ব্যবহার করে ইনপুট ডেটার ভিত্তিতে পূর্বাভাস দেওয়া বা আউটপুট তৈরি করার প্রক্রিয়া। আমি Phi-3-mini এবং এর inference ক্ষমতা সম্পর্কে আরও বিস্তারিত জানাচ্ছি।

Phi-3-mini Microsoft কর্তৃক প্রকাশিত Phi-3 সিরিজের একটি অংশ। এই মডেলগুলো Small Language Models (SLMs) এর সম্ভাবনাকে নতুনভাবে সংজ্ঞায়িত করার জন্য ডিজাইন করা হয়েছে।

Phi-3-mini এবং এর inference ক্ষমতা সম্পর্কে কিছু মূল বিষয়:

## **Phi-3-mini পরিচিতি:**
- Phi-3-mini এর প্যারামিটার সাইজ ৩.৮ বিলিয়ন।
- এটি কেবলমাত্র প্রচলিত কম্পিউটিং ডিভাইসেই নয়, মোবাইল ডিভাইস এবং IoT ডিভাইসের মতো edge ডিভাইসেও চালানো যায়।
- Phi-3-mini এর মুক্তির মাধ্যমে ব্যক্তি এবং প্রতিষ্ঠানগুলো বিভিন্ন হার্ডওয়্যার ডিভাইসে, বিশেষ করে সীমিত সম্পদের পরিবেশে SLMs ডিপ্লয় করতে পারবে।
- এটি বিভিন্ন মডেল ফরম্যাট সমর্থন করে, যেমন প্রচলিত PyTorch ফরম্যাট, gguf ফরম্যাটের কোয়ান্টাইজড সংস্করণ, এবং ONNX ভিত্তিক কোয়ান্টাইজড সংস্করণ।

## **Phi-3-mini অ্যাক্সেস করা:**
Phi-3-mini অ্যাক্সেস করতে, আপনি Copilot অ্যাপ্লিকেশনে [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ব্যবহার করতে পারেন। Semantic Kernel সাধারণত Azure OpenAI Service, Hugging Face এর ওপেন সোর্স মডেল এবং লোকাল মডেলগুলোর সাথে সামঞ্জস্যপূর্ণ।
আপনি কোয়ান্টাইজড মডেল কল করার জন্য [Ollama](https://ollama.com) বা [LlamaEdge](https://llamaedge.com) ব্যবহার করতেও পারেন। Ollama ব্যক্তিগত ব্যবহারকারীদের বিভিন্ন কোয়ান্টাইজড মডেল কল করার সুযোগ দেয়, আর LlamaEdge GGUF মডেলগুলোর জন্য ক্রস-প্ল্যাটফর্ম সাপোর্ট প্রদান করে।

## **কোয়ান্টাইজড মডেল:**
অনেক ব্যবহারকারী লোকাল inference এর জন্য কোয়ান্টাইজড মডেল ব্যবহার করতে পছন্দ করেন। উদাহরণস্বরূপ, আপনি সরাসরি Ollama ব্যবহার করে Phi-3 চালাতে পারেন অথবা Modelfile ব্যবহার করে অফলাইন কনফিগার করতে পারেন। Modelfile এ GGUF ফাইলের পাথ এবং প্রম্পট ফরম্যাট উল্লেখ থাকে।

## **Generative AI সম্ভাবনা:**
Phi-3-mini এর মতো SLMs একত্রিত করে generative AI এর নতুন সম্ভাবনা উন্মোচিত হয়। Inference কেবল প্রথম ধাপ; এই মডেলগুলো সীমিত সম্পদ, লেটেন্সি সীমাবদ্ধ এবং খরচ সীমাবদ্ধ পরিস্থিতিতে বিভিন্ন কাজের জন্য ব্যবহার করা যেতে পারে।

## **Phi-3-mini দিয়ে Generative AI উন্মোচন: Inference এবং ডিপ্লয়মেন্টের গাইড**  
Semantic Kernel, Ollama/LlamaEdge, এবং ONNX Runtime ব্যবহার করে Phi-3-mini মডেল অ্যাক্সেস এবং inference করার পদ্ধতি শিখুন, এবং বিভিন্ন অ্যাপ্লিকেশন ক্ষেত্রে generative AI এর সম্ভাবনা অন্বেষণ করুন।

**বৈশিষ্ট্যসমূহ**  
Phi-3-mini মডেল inference করা যায়:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

সারসংক্ষেপে, Phi-3-mini ডেভেলপারদের বিভিন্ন মডেল ফরম্যাট অন্বেষণ এবং বিভিন্ন অ্যাপ্লিকেশন ক্ষেত্রে generative AI ব্যবহার করার সুযোগ দেয়।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।