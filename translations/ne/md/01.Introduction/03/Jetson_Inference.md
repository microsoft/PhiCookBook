<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:41:19+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "ne"
}
-->
# **Nvidia Jetson मा Inference Phi-3**

Nvidia Jetson Nvidia को एक श्रृंखला एम्बेडेड कम्प्युटिङ बोर्डहरू हुन्। Jetson TK1, TX1 र TX2 मोडेलहरू सबैमा Nvidia को Tegra प्रोसेसर (वा SoC) हुन्छ जुन ARM आर्किटेक्चरको सेंट्रल प्रोसेसिंग यूनिट (CPU) समाहित गर्दछ। Jetson कम पावर प्रणाली हो र मेशिन लर्निङ एप्लिकेसनहरू छिटो बनाउन डिजाइन गरिएको हो। Nvidia Jetson पेशेवर विकासकर्ताहरूले सबै उद्योगहरूमा क्रान्तिकारी AI उत्पादनहरू बनाउन प्रयोग गर्छन्, र विद्यार्थी तथा उत्साहीहरूले व्यावहारिक AI सिकाइ र अद्भुत परियोजनाहरू बनाउन प्रयोग गर्छन्। SLM Jetson जस्ता एज उपकरणहरूमा तैनाथ गरिएको छ, जसले औद्योगिक जेनेरेटिभ AI एप्लिकेसन परिदृश्यहरूको राम्रो कार्यान्वयन सक्षम बनाउँछ।

## NVIDIA Jetson मा तैनाथीकरण:
स्वायत्त रोबोटिक्स र एम्बेडेड उपकरणहरूमा काम गर्ने विकासकर्ताहरूले Phi-3 Mini को फाइदा लिन सक्छन्। Phi-3 को सानो आकारले यसलाई एज तैनाथीकरणका लागि उपयुक्त बनाउँछ। प्रशिक्षणको क्रममा प्यारामिटरहरू सावधानीपूर्वक समायोजन गरिएको छ, जसले प्रतिक्रियाहरूमा उच्च सटीकता सुनिश्चित गर्दछ।

### TensorRT-LLM अनुकूलन:
NVIDIA को [TensorRT-LLM लाइब्रेरी](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) ठूलो भाषा मोडेल इन्फरेन्सलाई अनुकूलित गर्छ। यसले Phi-3 Mini को लामो सन्दर्भ विन्डोलाई समर्थन गर्दछ, जसले थ्रूपुट र लेटेन्सी दुवै सुधार गर्दछ। अनुकूलनहरूमा LongRoPE, FP8, र inflight ब्याचिङ जस्ता प्रविधिहरू समावेश छन्।

### उपलब्धता र तैनाथीकरण:
विकासकर्ताहरूले Phi-3 Mini लाई 128K सन्दर्भ विन्डोसहित [NVIDIA को AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) मा अन्वेषण गर्न सक्छन्। यो NVIDIA NIM को रूपमा प्याकेज गरिएको छ, जुन एक माइक्रोसर्भिस हो र मानक API सहित जुन कहीं पनि तैनाथ गर्न सकिन्छ। थप रूपमा, [TensorRT-LLM को GitHub मा कार्यान्वयनहरू](https://github.com/NVIDIA/TensorRT-LLM) उपलब्ध छन्।

## **1. तयारी**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Jetson मा Phi-3 चलाउने**

हामी [Ollama](https://ollama.com) वा [LlamaEdge](https://llamaedge.com) छनोट गर्न सक्छौं।

यदि तपाईं क्लाउड र एज उपकरणहरूमा एकै समयमा gguf प्रयोग गर्न चाहनुहुन्छ भने, LlamaEdge लाई WasmEdge को रूपमा बुझ्न सकिन्छ (WasmEdge एक हल्का, उच्च प्रदर्शन, स्केलेबल WebAssembly रनटाइम हो जुन क्लाउड नेटिभ, एज र विकेन्द्रीकृत एप्लिकेसनहरूका लागि उपयुक्त छ। यसले सर्भरलेस एप्लिकेसनहरू, एम्बेडेड फंक्शनहरू, माइक्रोसर्भिसहरू, स्मार्ट कन्ट्र्याक्टहरू र IoT उपकरणहरूलाई समर्थन गर्दछ। तपाईं gguf को मात्रात्मक मोडेललाई LlamaEdge मार्फत एज उपकरणहरू र क्लाउडमा तैनाथ गर्न सक्नुहुन्छ।

![llamaedge](../../../../../translated_images/llamaedge.e9d6ff96dff11cf7.ne.jpg)

यहाँ प्रयोग गर्ने चरणहरू छन्:

1. सम्बन्धित लाइब्रेरीहरू र फाइलहरू इन्स्टल र डाउनलोड गर्नुहोस्

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Note**: llama-api-server.wasm र chatbot-ui एउटै डाइरेक्टरीमा हुनुपर्छ

2. टर्मिनलमा स्क्रिप्टहरू चलाउनुहोस्

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

यहाँ चलाएको परिणाम छ

![llamaedgerun](../../../../../translated_images/llamaedgerun.bed921516c9a821c.ne.png)

***नमूना कोड*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

सारांशमा, Phi-3 Mini भाषा मोडेलिङमा ठूलो प्रगति हो, जसले दक्षता, सन्दर्भ जागरूकता, र NVIDIA को अनुकूलन क्षमता संयोजन गर्दछ। तपाईं रोबोटहरू वा एज एप्लिकेसनहरू निर्माण गर्दै हुनुहुन्छ भने, Phi-3 Mini एक शक्तिशाली उपकरण हो जसलाई जान्न आवश्यक छ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।