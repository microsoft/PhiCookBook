# **অ্যান্ড্রয়েডে ইনফারেন্স Phi-3**

চলুন দেখি কিভাবে আপনি অ্যান্ড্রয়েড ডিভাইসে Phi-3-mini দিয়ে ইনফারেন্স করতে পারেন। Phi-3-mini হলো মাইক্রোসফটের একটি নতুন সিরিজের মডেল যা এজ ডিভাইস এবং IoT ডিভাইসে বড় ভাষার মডেল (LLMs) ব্যবহারের সুযোগ করে দেয়।

## সেমান্টিক কার্নেল এবং ইনফারেন্স

[সেমান্টিক কার্নেল](https://github.com/microsoft/semantic-kernel) একটি অ্যাপ্লিকেশন ফ্রেমওয়ার্ক যা আপনাকে Azure OpenAI সার্ভিস, OpenAI মডেল এবং এমনকি লোকাল মডেলের সঙ্গে সামঞ্জস্যপূর্ণ অ্যাপ্লিকেশন তৈরি করতে দেয়। যদি আপনি সেমান্টিক কার্নেল নিয়ে নতুন হন, আমরা আপনাকে [সেমান্টিক কার্নেল কুকবুক](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) দেখার পরামর্শ দিচ্ছি।

### সেমান্টিক কার্নেল ব্যবহার করে Phi-3-mini অ্যাক্সেস করার জন্য

আপনি এটি সেমান্টিক কার্নেলের Hugging Face Connector এর সাথে মিলিয়ে ব্যবহার করতে পারেন। এই [সাম্পল কোড](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) দেখুন।

ডিফল্টভাবে, এটি Hugging Face এ মডেল আইডির সাথে সামঞ্জস্যপূর্ণ। তবে, আপনি স্থানীয়ভাবে তৈরি Phi-3-mini মডেল সার্ভারের সঙ্গেও সংযোগ করতে পারেন।

### Ollama বা LlamaEdge দিয়ে কোয়ান্টাইজড মডেল কল করা

অনেক ব্যবহারকারী মডেলগুলো লোকালি চালানোর জন্য কোয়ান্টাইজড মডেল ব্যবহার করতে পছন্দ করেন। [Ollama](https://ollama.com/) এবং [LlamaEdge](https://llamaedge.com) পৃথক কোয়ান্টাইজড মডেলগুলো কল করার সুবিধা দেয়:

#### Ollama

আপনি সরাসরি `ollama run Phi-3` চালাতে পারেন অথবা আপনার `.gguf` ফাইলের পাথ সহ `Modelfile` তৈরি করে অফলাইন কনফিগার করতে পারেন।

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[সাম্পল কোড](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

একই সময়ে ক্লাউড এবং এজ ডিভাইসে `.gguf` ফাইল ব্যবহার করতে চাইলে, LlamaEdge একটি দারুণ বিকল্প। শুরু করতে এই [সাম্পল কোড](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) দেখতে পারেন।

### অ্যান্ড্রয়েড ফোনে ইনস্টল ও চালানো

1. **মাসিক চ্যাট অ্যাপ ডাউনলোড করুন** (ফ্রি) অ্যান্ড্রয়েড ফোনের জন্য।
2. APK ফাইল (১৪৮এমবি) ডাউনলোড করে ডিভাইসে ইনস্টল করুন।
3. মাসিক চ্যাট অ্যাপ চালু করুন। আপনি Phi-3-mini সহ এআই মডেলগুলোর একটি তালিকা দেখতে পাবেন।

### LiteRT-LM সহ Phi-4-mini-reasoning চালানো

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) সম্প্রদায়-রূপান্তরিত int4 `.litertlm` বান্ডিল হিসেবে গুগলের [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) অন-ডিভাইস রানটাইমের জন্য উপলব্ধ। অ্যান্ড্রয়েডে এটি CPU বা GPU তে [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) অ্যাপের মাধ্যমে (অ্যাপের মধ্যে Hugging Face থেকে বান্ডিল ইমপোর্ট করুন) অথবা LiteRT-LM Kotlin API দিয়ে চলে; একই বান্ডিল iOS, macOS, Linux এবং Windows -এও চলে। মডেল কার্ডে পরিমাপকৃত গতি এবং রান কমান্ড সমূহ দেওয়া আছে।

সংক্ষেপে, Phi-3-mini এজ ডিভাইসে জেনেরেটিভ AI এর জন্য উত্তেজনাকর সুযোগ সৃষ্টি করে এবং আপনি অ্যান্ড্রয়েডে এর ক্ষমতাগুলো অন্বেষণ শুরু করতে পারেন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->