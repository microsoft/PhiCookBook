<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:12:25+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "bn"
}
-->
# **অ্যান্ড্রয়েডে Inference Phi-3**

চলুন দেখি কিভাবে আপনি অ্যান্ড্রয়েড ডিভাইসে Phi-3-mini দিয়ে inference করতে পারেন। Phi-3-mini হলো Microsoft-এর নতুন মডেল সিরিজ যা edge ডিভাইস এবং IoT ডিভাইসে Large Language Models (LLMs) ডিপ্লয়মেন্টের সুযোগ দেয়।

## Semantic Kernel এবং Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) একটি অ্যাপ্লিকেশন ফ্রেমওয়ার্ক যা আপনাকে Azure OpenAI Service, OpenAI মডেল এবং এমনকি লোকাল মডেলগুলোর সাথে সামঞ্জস্যপূর্ণ অ্যাপ্লিকেশন তৈরি করতে দেয়। যদি আপনি Semantic Kernel-এ নতুন হন, তাহলে আমরা আপনাকে [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) দেখার পরামর্শ দিই।

### Semantic Kernel ব্যবহার করে Phi-3-mini অ্যাক্সেস করার জন্য

আপনি এটি Semantic Kernel-এর Hugging Face Connector-এর সাথে মিলিয়ে ব্যবহার করতে পারেন। এই [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) দেখুন।

ডিফল্টভাবে, এটি Hugging Face-এর মডেল আইডির সাথে সংযুক্ত থাকে। তবে, আপনি লোকালি তৈরি করা Phi-3-mini মডেল সার্ভারের সাথেও সংযোগ করতে পারেন।

### Ollama বা LlamaEdge দিয়ে Quantized মডেল কল করা

অনেক ব্যবহারকারী মডেলগুলো লোকালি চালানোর জন্য quantized মডেল ব্যবহার করতে পছন্দ করেন। [Ollama](https://ollama.com/) এবং [LlamaEdge](https://llamaedge.com) ব্যক্তিগত ব্যবহারকারীদের বিভিন্ন quantized মডেল কল করার সুযোগ দেয়:

#### Ollama

আপনি সরাসরি `ollama run Phi-3` চালাতে পারেন অথবা `.gguf` ফাইলের পাথ সহ একটি `Modelfile` তৈরি করে অফলাইনে কনফিগার করতে পারেন।

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

যদি আপনি ক্লাউড এবং edge ডিভাইস উভয় জায়গায় `.gguf` ফাইল ব্যবহার করতে চান, তাহলে LlamaEdge একটি চমৎকার বিকল্প। শুরু করার জন্য এই [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) দেখুন।

### অ্যান্ড্রয়েড ফোনে ইনস্টল ও চালানো

1. **MLC Chat অ্যাপ (ফ্রি) ডাউনলোড করুন** অ্যান্ড্রয়েড ফোনের জন্য।
2. APK ফাইল (১৪৮MB) ডাউনলোড করে আপনার ডিভাইসে ইনস্টল করুন।
3. MLC Chat অ্যাপ চালু করুন। আপনি Phi-3-mini সহ বিভিন্ন AI মডেলের তালিকা দেখতে পাবেন।

সারাংশে, Phi-3-mini edge ডিভাইসে জেনারেটিভ AI-এর জন্য নতুন সম্ভাবনার দ্বার খুলে দিয়েছে, এবং আপনি অ্যান্ড্রয়েডে এর ক্ষমতা অন্বেষণ শুরু করতে পারেন।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।