<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2a7aaeb42235207ba74581473b305581",
  "translation_date": "2025-04-04T12:14:44+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingLlamacppQuantifyingPhi.md",
  "language_code": "mo"
}
-->
# **Phi परिवार को llama.cpp का उपयोग करके क्वांटाइज़ करना**

## **llama.cpp क्या है**

llama.cpp एक ओपन-सोर्स सॉफ़्टवेयर लाइब्रेरी है, जो मुख्य रूप से C++ में लिखी गई है और विभिन्न बड़े भाषा मॉडल्स (LLMs) जैसे Llama पर इन्फ़ेरेंस करती है। इसका मुख्य उद्देश्य न्यूनतम सेटअप के साथ विभिन्न हार्डवेयर पर अत्याधुनिक प्रदर्शन प्रदान करना है। इसके अलावा, इस लाइब्रेरी के लिए Python बाइंडिंग्स भी उपलब्ध हैं, जो टेक्स्ट कंप्लीशन और OpenAI संगत वेब सर्वर के लिए एक उच्च-स्तरीय API प्रदान करती हैं।

llama.cpp का मुख्य लक्ष्य न्यूनतम सेटअप के साथ और अत्याधुनिक प्रदर्शन के साथ स्थानीय और क्लाउड दोनों में विभिन्न प्रकार के हार्डवेयर पर LLM इन्फ़ेरेंस सक्षम करना है।

- बिना किसी डिपेंडेंसी के सरल C/C++ इम्प्लीमेंटेशन
- Apple silicon को प्राथमिकता - ARM NEON, Accelerate और Metal फ्रेमवर्क्स के माध्यम से अनुकूलित
- x86 आर्किटेक्चर के लिए AVX, AVX2 और AVX512 समर्थन
- तेज़ इन्फ़ेरेंस और कम मेमोरी उपयोग के लिए 1.5-बिट, 2-बिट, 3-बिट, 4-बिट, 5-बिट, 6-बिट और 8-बिट इंटेजर क्वांटाइज़ेशन
- NVIDIA GPUs पर LLMs चलाने के लिए कस्टम CUDA कर्नल्स (AMD GPUs के लिए HIP समर्थन)
- Vulkan और SYCL बैकएंड समर्थन
- CPU+GPU हाइब्रिड इन्फ़ेरेंस, जो कुल VRAM क्षमता से बड़े मॉडल्स को आंशिक रूप से तेज़ करता है

## **Phi-3.5 को llama.cpp से क्वांटाइज़ करना**

Phi-3.5-Instruct मॉडल को llama.cpp का उपयोग करके क्वांटाइज़ किया जा सकता है, लेकिन Phi-3.5-Vision और Phi-3.5-MoE अभी समर्थित नहीं हैं। llama.cpp द्वारा परिवर्तित फॉर्मेट GGUF है, जो सबसे व्यापक रूप से उपयोग किया जाने वाला क्वांटाइज़ेशन फॉर्मेट भी है।

Hugging Face पर GGUF फॉर्मेट में कई क्वांटाइज़्ड मॉडल्स उपलब्ध हैं। AI Foundry, Ollama, और LlamaEdge llama.cpp पर निर्भर करते हैं, इसलिए GGUF मॉडल्स का उपयोग अक्सर किया जाता है।

### **GGUF क्या है**

GGUF एक बाइनरी फॉर्मेट है, जो मॉडल्स को तेज़ी से लोड और सेव करने के लिए अनुकूलित है, जिससे यह इन्फ़ेरेंस उद्देश्यों के लिए अत्यधिक कुशल बनता है। GGUF को GGML और अन्य एक्सीक्यूटर्स के साथ उपयोग के लिए डिज़ाइन किया गया है। GGUF को @ggerganov द्वारा विकसित किया गया था, जो llama.cpp के डेवलपर भी हैं, एक लोकप्रिय C/C++ LLM इन्फ़ेरेंस फ्रेमवर्क। PyTorch जैसे फ्रेमवर्क्स में विकसित मॉडल्स को GGUF फॉर्मेट में परिवर्तित किया जा सकता है ताकि वे इन इंजनों के साथ उपयोग किए जा सकें।

### **ONNX बनाम GGUF**

ONNX एक पारंपरिक मशीन लर्निंग/डीप लर्निंग फॉर्मेट है, जो विभिन्न AI फ्रेमवर्क्स में अच्छी तरह से समर्थित है और एज डिवाइसेस में उपयोग के अच्छे परिदृश्य प्रदान करता है। GGUF, llama.cpp पर आधारित है और इसे GenAI युग में उत्पादित माना जा सकता है। दोनों के उपयोग समान हैं। यदि आप एंबेडेड हार्डवेयर और एप्लिकेशन लेयर में बेहतर प्रदर्शन चाहते हैं, तो ONNX आपका विकल्प हो सकता है। यदि आप llama.cpp के डेरिवेटिव फ्रेमवर्क और तकनीक का उपयोग करते हैं, तो GGUF बेहतर हो सकता है।

### **Phi-3.5-Instruct को llama.cpp से क्वांटाइज़ करना**

**1. पर्यावरण सेटअप**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. क्वांटाइज़ेशन**

llama.cpp का उपयोग करके Phi-3.5-Instruct को FP16 GGUF में बदलना


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 को INT4 में क्वांटाइज़ करना


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. परीक्षण**

llama-cpp-python स्थापित करें


```bash

pip install llama-cpp-python -U

```

***नोट*** 

यदि आप Apple Silicon का उपयोग करते हैं, तो कृपया llama-cpp-python इस तरह स्थापित करें


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

परीक्षण 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **संसाधन**

1. llama.cpp के बारे में और जानें [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GGUF के बारे में और जानें [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

It seems you are asking for a translation into "mo." Could you clarify what "mo" refers to? For example, are you asking for a translation into Māori, Marshallese, or another language?