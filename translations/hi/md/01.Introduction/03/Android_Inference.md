<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:12:10+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "hi"
}
-->
# **Android में Inference Phi-3**

आइए देखें कि आप Android डिवाइस पर Phi-3-mini के साथ inference कैसे कर सकते हैं। Phi-3-mini Microsoft की एक नई मॉडल श्रृंखला है जो एज डिवाइस और IoT डिवाइस पर Large Language Models (LLMs) को डिप्लॉय करने की सुविधा देती है।

## Semantic Kernel और Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) एक एप्लिकेशन फ्रेमवर्क है जो आपको Azure OpenAI Service, OpenAI मॉडल्स, और यहां तक कि लोकल मॉडल्स के साथ संगत एप्लिकेशन बनाने की अनुमति देता है। यदि आप Semantic Kernel में नए हैं, तो हम सुझाव देते हैं कि आप [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) देखें।

### Semantic Kernel के जरिए Phi-3-mini तक पहुंच

आप इसे Semantic Kernel में Hugging Face Connector के साथ जोड़ सकते हैं। इस [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) को देखें।

डिफ़ॉल्ट रूप से, यह Hugging Face पर मॉडल ID से जुड़ा होता है। हालांकि, आप लोकल रूप से बनाए गए Phi-3-mini मॉडल सर्वर से भी कनेक्ट कर सकते हैं।

### Ollama या LlamaEdge के साथ Quantized मॉडल कॉल करना

कई उपयोगकर्ता मॉडल्स को लोकली चलाने के लिए quantized मॉडल्स का उपयोग करना पसंद करते हैं। [Ollama](https://ollama.com/) और [LlamaEdge](https://llamaedge.com) व्यक्तिगत उपयोगकर्ताओं को विभिन्न quantized मॉडल्स कॉल करने की अनुमति देते हैं:

#### Ollama

आप सीधे `ollama run Phi-3` चला सकते हैं या अपने `.gguf` फाइल के पाथ के साथ एक `Modelfile` बनाकर इसे ऑफ़लाइन कॉन्फ़िगर कर सकते हैं।

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

यदि आप क्लाउड और एज डिवाइस दोनों पर एक साथ `.gguf` फाइलें इस्तेमाल करना चाहते हैं, तो LlamaEdge एक बेहतरीन विकल्प है। शुरू करने के लिए आप इस [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) को देख सकते हैं।

### Android फोन पर इंस्टॉल और चलाएं

1. **MLC Chat ऐप डाउनलोड करें** (फ्री) Android फोन के लिए।  
2. APK फाइल (148MB) डाउनलोड करें और अपने डिवाइस पर इंस्टॉल करें।  
3. MLC Chat ऐप लॉन्च करें। आपको AI मॉडल्स की एक सूची दिखेगी, जिसमें Phi-3-mini भी शामिल है।

संक्षेप में, Phi-3-mini एज डिवाइस पर जनरेटिव AI के लिए रोमांचक संभावनाएं खोलता है, और आप इसकी क्षमताओं को Android पर एक्सप्लोर करना शुरू कर सकते हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।