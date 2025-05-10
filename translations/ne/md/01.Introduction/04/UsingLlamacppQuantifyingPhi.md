<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:06:36+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "ne"
}
-->
# **llama.cpp प्रयोग गरी Phi परिवारलाई क्वान्टाइज गर्ने**

## **llama.cpp के हो**

llama.cpp एक खुला स्रोत सफ्टवेयर पुस्तकालय हो जुन मुख्य रूपमा C++ मा लेखिएको छ र विभिन्न ठूलो भाषा मोडेलहरू (LLMs) जस्तै Llama मा इन्फरेन्स गर्ने काम गर्छ। यसको मुख्य उद्देश्य न्यूनतम सेटअपमा विभिन्न हार्डवेयरहरूमा LLM इन्फरेन्सका लागि अत्याधुनिक प्रदर्शन प्रदान गर्नु हो। यसका साथै, यो पुस्तकालयका लागि Python बाइन्डिङहरू पनि उपलब्ध छन्, जसले टेक्स्ट कम्प्लीसनका लागि उच्च-स्तरीय API र OpenAI अनुकूल वेब सर्भर प्रदान गर्छ।

llama.cpp को मुख्य लक्ष्य न्यूनतम सेटअपमा र विभिन्न प्रकारका हार्डवेयरमा—स्थानीय र क्लाउड दुवैमा—LLM इन्फरेन्स सक्षम पार्नु हो।

- कुनै निर्भरता बिना साधारण C/C++ कार्यान्वयन
- Apple silicon लाई प्राथमिकता दिइएको छ—ARM NEON, Accelerate र Metal फ्रेमवर्कहरू मार्फत अनुकूलित
- x86 आर्किटेक्चरका लागि AVX, AVX2 र AVX512 समर्थन
- छिटो इन्फरेन्स र कम मेमोरी प्रयोगका लागि 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, र 8-bit पूर्णांक क्वान्टाइजेसन
- NVIDIA GPU मा LLM चलाउनका लागि कस्टम CUDA कर्नेलहरू (AMD GPU का लागि HIP समर्थन)
- Vulkan र SYCL ब्याकएन्ड समर्थन
- CPU+GPU हाइब्रिड इन्फरेन्स जसले कुल VRAM क्षमताभन्दा ठूलो मोडेलहरूलाई आंशिक रूपमा छिटो बनाउँछ

## **llama.cpp प्रयोग गरी Phi-3.5 क्वान्टाइज गर्ने**

Phi-3.5-Instruct मोडेललाई llama.cpp प्रयोग गरी क्वान्टाइज गर्न सकिन्छ, तर Phi-3.5-Vision र Phi-3.5-MoE अहिले सम्म समर्थन गरिएको छैन। llama.cpp द्वारा रूपान्तरण गरिएको ढाँचा gguf हो, जुन सबैभन्दा व्यापक रूपमा प्रयोग हुने क्वान्टाइजेसन ढाँचा पनि हो।

Hugging Face मा धेरै क्वान्टाइज गरिएको GGUF ढाँचाका मोडेलहरू उपलब्ध छन्। AI Foundry, Ollama, र LlamaEdge ले llama.cpp मा भर पर्छन्, त्यसैले GGUF मोडेलहरू पनि प्रायः प्रयोग गरिन्छन्।

### **GGUF के हो**

GGUF एक द्विआधारी (बाइनरी) ढाँचा हो जुन मोडेलहरू छिटो लोड र सेभ गर्नका लागि अनुकूलित गरिएको छ, जसले इन्फरेन्सका लागि अत्यधिक दक्षता प्रदान गर्छ। GGUF GGML र अन्य इग्जिक्युटरहरूसँग प्रयोगको लागि डिजाइन गरिएको हो। GGUF लाई @ggerganov द्वारा विकास गरिएको हो, जो llama.cpp का विकासकर्ता पनि हुन्, जुन लोकप्रिय C/C++ LLM इन्फरेन्स फ्रेमवर्क हो। PyTorch जस्ता फ्रेमवर्कमा विकास भएका मोडेलहरूलाई GGUF ढाँचामा रूपान्तरण गरी ती इन्जिनहरूसँग प्रयोग गर्न सकिन्छ।

### **ONNX र GGUF को तुलना**

ONNX एक पारम्परिक मेसिन लर्निङ/डीप लर्निङ ढाँचा हो, जुन विभिन्न AI फ्रेमवर्कहरूमा राम्रोसँग समर्थन गरिएको छ र एज उपकरणहरूमा राम्रो प्रयोगका अवसरहरू छन्। GGUF भने llama.cpp मा आधारित छ र यसलाई GenAI युगमा उत्पादित मान्न सकिन्छ। दुवैको प्रयोग क्षेत्र मिल्दोजुल्दो छ। यदि तपाईं इम्बेडेड हार्डवेयर र एप्लिकेशन तहमा राम्रो प्रदर्शन चाहनुहुन्छ भने ONNX उपयुक्त हुन सक्छ। यदि तपाईं llama.cpp को व्युत्पन्न फ्रेमवर्क र प्रविधि प्रयोग गर्नुहुन्छ भने GGUF उत्तम हुन सक्छ।

### **llama.cpp प्रयोग गरी Phi-3.5-Instruct क्वान्टाइजेसन**

**1. वातावरण सेटअप**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. क्वान्टाइजेसन**

llama.cpp प्रयोग गरी Phi-3.5-Instruct लाई FP16 GGUF मा रूपान्तरण गर्ने


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 लाई INT4 मा क्वान्टाइज गर्ने


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. परीक्षण**

llama-cpp-python इन्स्टल गर्ने


```bash

pip install llama-cpp-python -U

```

***Note*** 

यदि तपाईं Apple Silicon प्रयोग गर्दै हुनुहुन्छ भने, कृपया यसरी llama-cpp-python इन्स्टल गर्नुहोस्


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

परीक्षण गर्ने


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **स्रोतहरू**

1. llama.cpp को बारेमा थप जान्न [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntime को बारेमा थप जान्न [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUF को बारेमा थप जान्न [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा असंगतिहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याहरूको लागि हामी जिम्मेवार छैनौं।