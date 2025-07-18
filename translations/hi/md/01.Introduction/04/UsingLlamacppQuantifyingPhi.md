<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:07:30+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "hi"
}
-->
# **llama.cpp का उपयोग करके Phi परिवार का क्वांटाइजेशन**

## **llama.cpp क्या है**

llama.cpp एक ओपन-सोर्स सॉफ़्टवेयर लाइब्रेरी है, जो मुख्य रूप से C++ में लिखी गई है और विभिन्न बड़े भाषा मॉडल (LLMs) जैसे Llama पर इन्फेरेंस करती है। इसका मुख्य उद्देश्य न्यूनतम सेटअप के साथ विभिन्न हार्डवेयर पर LLM इन्फेरेंस के लिए अत्याधुनिक प्रदर्शन प्रदान करना है। इसके अलावा, इस लाइब्रेरी के लिए Python बाइंडिंग्स भी उपलब्ध हैं, जो टेक्स्ट कंप्लीशन के लिए उच्च स्तरीय API और OpenAI संगत वेब सर्वर प्रदान करती हैं।

llama.cpp का मुख्य लक्ष्य न्यूनतम सेटअप के साथ और विभिन्न हार्डवेयर पर - लोकल और क्लाउड दोनों में - अत्याधुनिक प्रदर्शन के साथ LLM इन्फेरेंस सक्षम करना है।

- बिना किसी निर्भरता के सादा C/C++ इम्प्लीमेंटेशन
- Apple सिलिकॉन को प्राथमिकता - ARM NEON, Accelerate और Metal फ्रेमवर्क के माध्यम से ऑप्टिमाइज़्ड
- x86 आर्किटेक्चर के लिए AVX, AVX2 और AVX512 सपोर्ट
- तेज़ इन्फेरेंस और कम मेमोरी उपयोग के लिए 1.5-बिट, 2-बिट, 3-बिट, 4-बिट, 5-बिट, 6-बिट, और 8-बिट इंटीजर क्वांटाइजेशन
- NVIDIA GPUs पर LLM चलाने के लिए कस्टम CUDA कर्नेल (AMD GPUs के लिए HIP सपोर्ट)
- Vulkan और SYCL बैकएंड सपोर्ट
- CPU+GPU हाइब्रिड इन्फेरेंस, जो कुल VRAM क्षमता से बड़े मॉडल को आंशिक रूप से तेज़ करता है

## **llama.cpp के साथ Phi-3.5 का क्वांटाइजेशन**

Phi-3.5-Instruct मॉडल को llama.cpp के माध्यम से क्वांटाइज़ किया जा सकता है, लेकिन Phi-3.5-Vision और Phi-3.5-MoE अभी समर्थित नहीं हैं। llama.cpp द्वारा कनवर्ट किया गया फॉर्मेट gguf है, जो सबसे व्यापक रूप से उपयोग किया जाने वाला क्वांटाइजेशन फॉर्मेट भी है।

Hugging Face पर क्वांटाइज़्ड GGUF फॉर्मेट के कई मॉडल उपलब्ध हैं। AI Foundry, Ollama, और LlamaEdge llama.cpp पर निर्भर करते हैं, इसलिए GGUF मॉडल भी अक्सर उपयोग किए जाते हैं।

### **GGUF क्या है**

GGUF एक बाइनरी फॉर्मेट है जो मॉडल को जल्दी लोड और सेव करने के लिए ऑप्टिमाइज़्ड है, जिससे इन्फेरेंस के लिए यह बहुत प्रभावी बनता है। GGUF को GGML और अन्य एक्सेक्यूटर्स के साथ उपयोग के लिए डिज़ाइन किया गया है। GGUF को @ggerganov ने विकसित किया है, जो llama.cpp के डेवलपर भी हैं, जो एक लोकप्रिय C/C++ LLM इन्फेरेंस फ्रेमवर्क है। PyTorch जैसे फ्रेमवर्क में विकसित मॉडल को GGUF फॉर्मेट में कनवर्ट करके उन इंजन के साथ उपयोग किया जा सकता है।

### **ONNX बनाम GGUF**

ONNX एक पारंपरिक मशीन लर्निंग/डीप लर्निंग फॉर्मेट है, जिसे विभिन्न AI फ्रेमवर्क में अच्छी तरह सपोर्ट किया जाता है और यह एज डिवाइसेस में उपयोग के लिए उपयुक्त है। वहीं GGUF, llama.cpp पर आधारित है और इसे GenAI युग में विकसित कहा जा सकता है। दोनों के उपयोग समान हैं। यदि आप एम्बेडेड हार्डवेयर और एप्लिकेशन लेयर में बेहतर प्रदर्शन चाहते हैं, तो ONNX आपके लिए बेहतर विकल्प हो सकता है। यदि आप llama.cpp के डेरिवेटिव फ्रेमवर्क और तकनीक का उपयोग करते हैं, तो GGUF बेहतर हो सकता है।

### **llama.cpp का उपयोग करके Phi-3.5-Instruct का क्वांटाइजेशन**

**1. पर्यावरण कॉन्फ़िगरेशन**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. क्वांटाइजेशन**

llama.cpp का उपयोग करके Phi-3.5-Instruct को FP16 GGUF में कनवर्ट करें


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 को INT4 में क्वांटाइज़ करें


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. परीक्षण**

llama-cpp-python इंस्टॉल करें


```bash

pip install llama-cpp-python -U

```

***Note*** 

यदि आप Apple Silicon का उपयोग कर रहे हैं, तो कृपया llama-cpp-python इस प्रकार इंस्टॉल करें


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

परीक्षण 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **संसाधन**

1. llama.cpp के बारे में अधिक जानें [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntime के बारे में अधिक जानें [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUF के बारे में अधिक जानें [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।