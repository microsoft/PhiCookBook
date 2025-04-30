<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5b3df6e1a9927e93cda92801eec65d33",
  "translation_date": "2025-04-04T17:48:09+00:00",
  "source_file": "md\\01.Introduction\\03\\Jetson_Inference.md",
  "language_code": "hi"
}
-->
# **Nvidia Jetson में Phi-3 का निष्कर्षण**

Nvidia Jetson, Nvidia की ओर से एम्बेडेड कंप्यूटिंग बोर्ड्स की एक श्रृंखला है। Jetson TK1, TX1 और TX2 मॉडल्स में Nvidia का Tegra प्रोसेसर (या SoC) होता है, जो ARM आर्किटेक्चर आधारित सेंट्रल प्रोसेसिंग यूनिट (CPU) को एकीकृत करता है। Jetson एक लो-पावर सिस्टम है और इसे मशीन लर्निंग एप्लिकेशन को तेज़ करने के लिए डिज़ाइन किया गया है। Nvidia Jetson का उपयोग पेशेवर डेवलपर्स द्वारा सभी उद्योगों में क्रांतिकारी AI उत्पाद बनाने के लिए और छात्रों व उत्साही लोगों द्वारा AI सीखने और अद्भुत प्रोजेक्ट्स बनाने के लिए किया जाता है। SLM को Jetson जैसे एज डिवाइसों में तैनात किया जाता है, जिससे औद्योगिक जनरेटिव AI एप्लिकेशन परिदृश्यों का बेहतर कार्यान्वयन संभव हो सके।

## NVIDIA Jetson पर तैनाती:
स्वायत्त रोबोटिक्स और एम्बेडेड डिवाइसों पर काम करने वाले डेवलपर्स Phi-3 Mini का लाभ उठा सकते हैं। Phi-3 का अपेक्षाकृत छोटा आकार इसे एज डिप्लॉयमेंट के लिए आदर्श बनाता है। प्रशिक्षण के दौरान पैरामीटर्स को सावधानीपूर्वक ट्यून किया गया है, जिससे प्रतिक्रियाओं में उच्च सटीकता सुनिश्चित होती है।

### TensorRT-LLM अनुकूलन:
NVIDIA का [TensorRT-LLM लाइब्रेरी](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) बड़े भाषा मॉडल निष्कर्षण को अनुकूलित करती है। यह Phi-3 Mini की लंबी संदर्भ विंडो का समर्थन करती है, जिससे थ्रूपुट और लेटेंसी दोनों में सुधार होता है। अनुकूलन तकनीकों में LongRoPE, FP8 और इनफ्लाइट बैचिंग जैसी विधियां शामिल हैं।

### उपलब्धता और तैनाती:
डेवलपर्स [NVIDIA के AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) पर 128K संदर्भ विंडो के साथ Phi-3 Mini का पता लगा सकते हैं। इसे NVIDIA NIM के रूप में पैक किया गया है, जो एक मानक API के साथ माइक्रोसर्विस है और कहीं भी तैनात किया जा सकता है। इसके अलावा, [GitHub पर TensorRT-LLM इम्प्लीमेंटेशन](https://github.com/NVIDIA/TensorRT-LLM) भी उपलब्ध हैं।

## **1. तैयारी**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Jetson में Phi-3 चलाना**

हम [Ollama](https://ollama.com) या [LlamaEdge](https://llamaedge.com) का चयन कर सकते हैं।

यदि आप gguf को क्लाउड और एज डिवाइसों पर एक साथ उपयोग करना चाहते हैं, तो LlamaEdge को WasmEdge के रूप में समझा जा सकता है (WasmEdge एक हल्का, उच्च-प्रदर्शन, स्केलेबल WebAssembly रनटाइम है, जो क्लाउड नेटिव, एज और विकेंद्रीकृत एप्लिकेशन के लिए उपयुक्त है। यह सर्वरलेस एप्लिकेशन, एम्बेडेड फंक्शन्स, माइक्रोसर्विसेज, स्मार्ट कॉन्ट्रैक्ट्स और IoT डिवाइसों का समर्थन करता है। आप gguf के क्वांटिटेटिव मॉडल को LlamaEdge के माध्यम से एज डिवाइस और क्लाउड पर तैनात कर सकते हैं।)

![llamaedge](../../../../../translated_images/llamaedge.1356a35c809c5e9d89d8168db0c92161e87f5e2c34831f2fad800f00fc4e74dc.hi.jpg)

यहां उपयोग के चरण दिए गए हैं:

1. संबंधित लाइब्रेरी और फाइल्स इंस्टॉल और डाउनलोड करें

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**नोट**: llama-api-server.wasm और chatbot-ui को एक ही डायरेक्टरी में होना चाहिए।

2. टर्मिनल में स्क्रिप्ट्स चलाएं

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

यहां चलने का परिणाम है:

![llamaedgerun](../../../../../translated_images/llamaedgerun.66eb2acd7f14e814437879522158b9531ae7c955014d48d0708d0e4ce6ac94a6.hi.png)

***उदाहरण कोड*** [Phi-3 Mini WASM नोटबुक उदाहरण](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

सारांश में, Phi-3 Mini भाषा मॉडलिंग में एक बड़ी प्रगति का प्रतिनिधित्व करता है, जिसमें दक्षता, संदर्भ जागरूकता और NVIDIA की अनुकूलन क्षमता शामिल है। चाहे आप रोबोट्स बना रहे हों या एज एप्लिकेशन, Phi-3 Mini एक शक्तिशाली उपकरण है जिसे नजरअंदाज नहीं किया जा सकता।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।