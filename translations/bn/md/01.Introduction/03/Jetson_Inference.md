<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:40:56+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "bn"
}
-->
# **Nvidia Jetson-এ Inference Phi-3**

Nvidia Jetson হলো Nvidia-এর একটি এমবেডেড কম্পিউটিং বোর্ড সিরিজ। Jetson TK1, TX1 এবং TX2 মডেলগুলোতে Nvidia-এর Tegra প্রসেসর (বা SoC) থাকে, যা ARM আর্কিটেকচারের সিপিইউ অন্তর্ভুক্ত করে। Jetson একটি কম পাওয়ার সিস্টেম এবং মেশিন লার্নিং অ্যাপ্লিকেশন দ্রুততর করার জন্য ডিজাইন করা হয়েছে। Nvidia Jetson পেশাদার ডেভেলপাররা বিভিন্ন শিল্পে অগ্রণী AI পণ্য তৈরি করতে ব্যবহার করেন, এবং শিক্ষার্থী ও উৎসাহীদের হাতে-কলমে AI শেখার ও চমৎকার প্রকল্প তৈরির জন্য ব্যবহৃত হয়। SLM Jetson-এর মতো এজ ডিভাইসগুলোতে মোতায়েন করা হয়, যা শিল্প ভিত্তিক জেনারেটিভ AI অ্যাপ্লিকেশন সিচুয়েশনগুলো আরও ভালোভাবে বাস্তবায়ন করতে সাহায্য করে।

## NVIDIA Jetson-এ মোতায়েন:
স্বয়ংক্রিয় রোবোটিক্স এবং এমবেডেড ডিভাইস নিয়ে কাজ করা ডেভেলপাররা Phi-3 Mini ব্যবহার করতে পারেন। Phi-3 এর ছোট আকার এটিকে এজ ডিপ্লয়মেন্টের জন্য আদর্শ করে তোলে। প্রশিক্ষণের সময় প্যারামিটারগুলো খুবই যত্নসহকারে টিউন করা হয়েছে, যা সঠিকতার উচ্চ মাত্রা নিশ্চিত করে।

### TensorRT-LLM অপ্টিমাইজেশন:
NVIDIA-এর [TensorRT-LLM লাইব্রেরি](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) বড় ভাষা মডেলের ইনফারেন্স অপ্টিমাইজ করে। এটি Phi-3 Mini-এর দীর্ঘ কনটেক্সট উইন্ডোকে সাপোর্ট করে, যা থ্রুপুট এবং লেটেন্সি উভয়ই উন্নত করে। অপ্টিমাইজেশনের মধ্যে রয়েছে LongRoPE, FP8, এবং ইনফ্লাইট ব্যাচিংয়ের মতো প্রযুক্তি।

### উপলব্ধতা এবং মোতায়েন:
ডেভেলপাররা Phi-3 Mini-এর 128K কনটেক্সট উইন্ডো [NVIDIA-এর AI পোর্টালে](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) অন্বেষণ করতে পারেন। এটি NVIDIA NIM হিসেবে প্যাকেজ করা হয়েছে, যা একটি মাইক্রোসার্ভিস এবং স্ট্যান্ডার্ড API সহ যেকোনো জায়গায় মোতায়েন করা যায়। এছাড়াও, [TensorRT-LLM এর GitHub ইমপ্লিমেন্টেশন](https://github.com/NVIDIA/TensorRT-LLM) পাওয়া যাবে।

## **১. প্রস্তুতি**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **২. Jetson-এ Phi-3 চালানো**

আমরা [Ollama](https://ollama.com) অথবা [LlamaEdge](https://llamaedge.com) বেছে নিতে পারি।

যদি আপনি ক্লাউড এবং এজ ডিভাইস উভয়েই gguf ব্যবহার করতে চান, তাহলে LlamaEdge কে WasmEdge হিসেবে বুঝতে পারেন (WasmEdge হলো একটি হালকা, উচ্চ কর্মক্ষমতা সম্পন্ন, স্কেলেবল WebAssembly রানটাইম যা ক্লাউড নেটিভ, এজ এবং ডেসেন্ট্রালাইজড অ্যাপ্লিকেশনের জন্য উপযুক্ত। এটি সার্ভারলেস অ্যাপ্লিকেশন, এমবেডেড ফাংশন, মাইক্রোসার্ভিস, স্মার্ট কন্ট্রাক্ট এবং IoT ডিভাইস সাপোর্ট করে। আপনি gguf এর কোয়ান্টিটেটিভ মডেল LlamaEdge এর মাধ্যমে এজ ডিভাইস এবং ক্লাউডে মোতায়েন করতে পারবেন।

![llamaedge](../../../../../translated_images/llamaedge.e9d6ff96dff11cf7.bn.jpg)

ব্যবহারের ধাপগুলো:

1. সংশ্লিষ্ট লাইব্রেরি এবং ফাইল ডাউনলোড ও ইনস্টল করুন

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**দ্রষ্টব্য**: llama-api-server.wasm এবং chatbot-ui একই ডিরেক্টরিতে থাকতে হবে

2. টার্মিনালে স্ক্রিপ্ট চালান

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

এখানে চালানোর ফলাফল দেখানো হলো

![llamaedgerun](../../../../../translated_images/llamaedgerun.bed921516c9a821c.bn.png)

***নমুনা কোড*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

সারসংক্ষেপে, Phi-3 Mini ভাষা মডেলিংয়ে একটি বড় অগ্রগতি, যা দক্ষতা, প্রসঙ্গ সচেতনতা এবং NVIDIA-এর অপ্টিমাইজেশন ক্ষমতাকে একত্রিত করে। আপনি রোবট তৈরি করুন বা এজ অ্যাপ্লিকেশন, Phi-3 Mini একটি শক্তিশালী টুল যা জানা জরুরি।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।