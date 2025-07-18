<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:08:23+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "hi"
}
-->
Phi-3-mini के संदर्भ में, inference का मतलब है मॉडल का उपयोग करके इनपुट डेटा के आधार पर भविष्यवाणियाँ करना या आउटपुट जनरेट करना। आइए मैं आपको Phi-3-mini और इसकी inference क्षमताओं के बारे में और जानकारी देता हूँ।

Phi-3-mini Microsoft द्वारा जारी Phi-3 श्रृंखला के मॉडलों का हिस्सा है। ये मॉडल Small Language Models (SLMs) के साथ संभव चीज़ों को फिर से परिभाषित करने के लिए डिज़ाइन किए गए हैं।

यहाँ Phi-3-mini और इसकी inference क्षमताओं के बारे में कुछ मुख्य बिंदु हैं:

## **Phi-3-mini का अवलोकन:**
- Phi-3-mini का पैरामीटर आकार 3.8 बिलियन है।
- यह न केवल पारंपरिक कंप्यूटिंग डिवाइसों पर बल्कि मोबाइल डिवाइस और IoT डिवाइस जैसे एज डिवाइसों पर भी चल सकता है।
- Phi-3-mini के रिलीज़ से व्यक्ति और उद्यम विभिन्न हार्डवेयर डिवाइसों पर, विशेष रूप से संसाधन-सीमित वातावरण में, SLMs को तैनात कर सकते हैं।
- यह विभिन्न मॉडल फॉर्मैट को कवर करता है, जिनमें पारंपरिक PyTorch फॉर्मैट, gguf फॉर्मैट का क्वांटाइज़्ड संस्करण, और ONNX-आधारित क्वांटाइज़्ड संस्करण शामिल हैं।

## **Phi-3-mini तक पहुँच:**
Phi-3-mini तक पहुँचने के लिए, आप Copilot एप्लिकेशन में [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) का उपयोग कर सकते हैं। Semantic Kernel आमतौर पर Azure OpenAI Service, Hugging Face पर ओपन-सोर्स मॉडल, और स्थानीय मॉडलों के साथ संगत है।  
आप क्वांटाइज़्ड मॉडलों को कॉल करने के लिए [Ollama](https://ollama.com) या [LlamaEdge](https://llamaedge.com) का भी उपयोग कर सकते हैं। Ollama व्यक्तिगत उपयोगकर्ताओं को विभिन्न क्वांटाइज़्ड मॉडलों को कॉल करने की अनुमति देता है, जबकि LlamaEdge GGUF मॉडलों के लिए क्रॉस-प्लेटफ़ॉर्म उपलब्धता प्रदान करता है।

## **क्वांटाइज़्ड मॉडल:**
कई उपयोगकर्ता स्थानीय inference के लिए क्वांटाइज़्ड मॉडलों का उपयोग करना पसंद करते हैं। उदाहरण के लिए, आप सीधे Ollama run Phi-3 चला सकते हैं या इसे ऑफ़लाइन Modelfile के माध्यम से कॉन्फ़िगर कर सकते हैं। Modelfile में GGUF फ़ाइल पथ और प्रॉम्प्ट फॉर्मैट निर्दिष्ट होता है।

## **Generative AI की संभावनाएँ:**
Phi-3-mini जैसे SLMs को मिलाकर generative AI के नए अवसर खुलते हैं। inference केवल पहला कदम है; इन मॉडलों का उपयोग संसाधन-सीमित, लेटेंसी-बाउंड, और लागत-सीमित परिदृश्यों में विभिन्न कार्यों के लिए किया जा सकता है।

## **Phi-3-mini के साथ Generative AI को अनलॉक करना: Inference और Deployment के लिए एक मार्गदर्शिका**  
जानिए कि Semantic Kernel, Ollama/LlamaEdge, और ONNX Runtime का उपयोग करके Phi-3-mini मॉडलों तक कैसे पहुँचें और inference करें, और विभिन्न एप्लिकेशन परिदृश्यों में generative AI की संभावनाओं का अन्वेषण करें।

**विशेषताएँ**  
Phi-3-mini मॉडल में inference:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

संक्षेप में, Phi-3-mini डेवलपर्स को विभिन्न मॉडल फॉर्मैट का अन्वेषण करने और विभिन्न एप्लिकेशन परिदृश्यों में generative AI का लाभ उठाने की अनुमति देता है।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।