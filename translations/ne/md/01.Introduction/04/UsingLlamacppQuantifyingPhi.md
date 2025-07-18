<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:08:05+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "ne"
}
-->
# **llama.cpp प्रयोग गरेर Phi परिवार क्वान्टाइजिङ**

## **llama.cpp के हो**

llama.cpp एक खुला स्रोत सफ्टवेयर पुस्तकालय हो जुन मुख्य रूपमा C++ मा लेखिएको छ र विभिन्न ठूलो भाषा मोडेलहरू (LLMs) जस्तै Llama मा इन्फरेन्स गर्दछ। यसको मुख्य उद्देश्य न्यूनतम सेटअपमा विभिन्न हार्डवेयरमा LLM इन्फरेन्सका लागि अत्याधुनिक प्रदर्शन प्रदान गर्नु हो। साथै, यस पुस्तकालयका लागि Python बाइन्डिङहरू उपलब्ध छन्, जसले टेक्स्ट कम्प्लीसनका लागि उच्च-स्तरीय API र OpenAI अनुकूल वेब सर्भर प्रदान गर्छ।

llama.cpp को मुख्य लक्ष्य न्यूनतम सेटअप र अत्याधुनिक प्रदर्शनका साथ विभिन्न हार्डवेयरमा LLM इन्फरेन्स सक्षम पार्नु हो - स्थानीय रूपमा र क्लाउडमा।

- कुनै निर्भरता बिना साधारण C/C++ कार्यान्वयन
- Apple सिलिकनलाई पहिलो श्रेणीको नागरिकको रूपमा मानिन्छ - ARM NEON, Accelerate र Metal फ्रेमवर्कहरू मार्फत अनुकूलित
- x86 आर्किटेक्चरका लागि AVX, AVX2 र AVX512 समर्थन
- छिटो इन्फरेन्स र कम मेमोरी प्रयोगका लागि 1.5-बिट, 2-बिट, 3-बिट, 4-बिट, 5-बिट, 6-बिट, र 8-बिट पूर्णांक क्वान्टाइजेसन
- NVIDIA GPU मा LLM चलाउन कस्टम CUDA कर्नेलहरू (AMD GPU का लागि HIP समर्थन)
- Vulkan र SYCL ब्याकएन्ड समर्थन
- कुल VRAM क्षमताभन्दा ठूलो मोडेलहरूलाई आंशिक रूपमा छिटो बनाउन CPU+GPU हाइब्रिड इन्फरेन्स

## **llama.cpp प्रयोग गरेर Phi-3.5 क्वान्टाइजिङ**

Phi-3.5-Instruct मोडेललाई llama.cpp प्रयोग गरेर क्वान्टाइज गर्न सकिन्छ, तर Phi-3.5-Vision र Phi-3.5-MoE हालसम्म समर्थन गरिएको छैन। llama.cpp द्वारा रूपान्तरण गरिएको ढाँचा gguf हो, जुन सबैभन्दा व्यापक रूपमा प्रयोग हुने क्वान्टाइजेसन ढाँचा पनि हो।

Hugging face मा धेरै संख्यामा क्वान्टाइज गरिएको GGUF ढाँचाका मोडेलहरू छन्। AI Foundry, Ollama, र LlamaEdge ले llama.cpp मा निर्भर गर्छन्, त्यसैले GGUF मोडेलहरू पनि प्रायः प्रयोग गरिन्छ।

### **GGUF के हो**

GGUF एक बाइनरी ढाँचा हो जुन मोडेलहरू छिटो लोड र सेभ गर्नका लागि अनुकूलित गरिएको छ, जसले इन्फरेन्सका लागि अत्यधिक प्रभावकारी बनाउँछ। GGUF GGML र अन्य एक्जिक्युटरहरूसँग प्रयोगका लागि डिजाइन गरिएको हो। GGUF @ggerganov द्वारा विकास गरिएको हो, जो llama.cpp का विकासकर्ता पनि हुन्, जुन एक लोकप्रिय C/C++ LLM इन्फरेन्स फ्रेमवर्क हो। PyTorch जस्ता फ्रेमवर्कहरूमा सुरुमा विकास गरिएका मोडेलहरू GGUF ढाँचामा रूपान्तरण गरेर ती इन्जिनहरूसँग प्रयोग गर्न सकिन्छ।

### **ONNX र GGUF**

ONNX एक परम्परागत मेशिन लर्निङ/डीप लर्निङ ढाँचा हो, जुन विभिन्न AI फ्रेमवर्कहरूमा राम्रोसँग समर्थन गरिएको छ र एज उपकरणहरूमा राम्रो प्रयोगका परिदृश्यहरू छन्। GGUF भने llama.cpp मा आधारित छ र यसलाई GenAI युगमा उत्पादित भनिन सक्छ। दुवैको प्रयोग समान छ। यदि तपाईं एम्बेडेड हार्डवेयर र एप्लिकेसन तहहरूमा राम्रो प्रदर्शन चाहनुहुन्छ भने ONNX तपाईंको रोजाइ हुन सक्छ। यदि तपाईं llama.cpp को व्युत्पन्न फ्रेमवर्क र प्रविधि प्रयोग गर्नुहुन्छ भने GGUF राम्रो हुन सक्छ।

### **llama.cpp प्रयोग गरेर Phi-3.5-Instruct क्वान्टाइजेसन**

**1. वातावरण कन्फिगरेसन**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. क्वान्टाइजेसन**

llama.cpp प्रयोग गरेर Phi-3.5-Instruct लाई FP16 GGUF मा रूपान्तरण गर्नुहोस्


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 लाई INT4 मा क्वान्टाइज गर्नुहोस्


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. परीक्षण**

llama-cpp-python इन्स्टल गर्नुहोस्


```bash

pip install llama-cpp-python -U

```

***सूचना*** 

यदि तपाईं Apple Silicon प्रयोग गर्दै हुनुहुन्छ भने, कृपया यसरी llama-cpp-python इन्स्टल गर्नुहोस्


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

परीक्षण


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **स्रोतहरू**

1. llama.cpp बारे थप जान्न [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntime बारे थप जान्न [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUF बारे थप जान्न [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।