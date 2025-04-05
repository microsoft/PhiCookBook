<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b909b4ac6465d33e81adb17df38deef3",
  "translation_date": "2025-04-04T17:44:55+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "hi"
}
-->
# **Android में Phi-3 पर इनफेरेंस**

आइए देखें कि आप Android डिवाइस पर Phi-3-mini के साथ इनफेरेंस कैसे कर सकते हैं। Phi-3-mini Microsoft की नई मॉडल श्रृंखला है, जो बड़े भाषा मॉडल (LLMs) को एज डिवाइस और IoT डिवाइस पर तैनात करने की सुविधा देती है।

## सेमांटिक कर्नल और इनफेरेंस

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) एक एप्लिकेशन फ्रेमवर्क है जो आपको Azure OpenAI Service, OpenAI मॉडल और यहां तक कि लोकल मॉडल के साथ संगत एप्लिकेशन बनाने की सुविधा देता है। यदि आप सेमांटिक कर्नल के लिए नए हैं, तो हम आपको [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) देखने की सलाह देते हैं।

### सेमांटिक कर्नल के माध्यम से Phi-3-mini तक पहुंचना

आप इसे सेमांटिक कर्नल में Hugging Face Connector के साथ जोड़ सकते हैं। इस [सैंपल कोड](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) को देखें।

डिफ़ॉल्ट रूप से, यह Hugging Face पर मॉडल ID से मेल खाता है। हालांकि, आप इसे लोकल रूप से बनाए गए Phi-3-mini मॉडल सर्वर से भी कनेक्ट कर सकते हैं।

### Ollama या LlamaEdge के साथ क्वांटाइज़्ड मॉडल कॉल करना

कई उपयोगकर्ता लोकल रूप से मॉडल चलाने के लिए क्वांटाइज़्ड मॉडल का उपयोग करना पसंद करते हैं। [Ollama](https://ollama.com/) और [LlamaEdge](https://llamaedge.com) व्यक्तिगत उपयोगकर्ताओं को विभिन्न क्वांटाइज़्ड मॉडल कॉल करने की अनुमति देते हैं:

#### Ollama

आप `ollama run Phi-3` को सीधे चला सकते हैं या इसे ऑफलाइन कॉन्फ़िगर कर सकते हैं `Modelfile` बनाकर, जिसमें आपके `.gguf` फाइल का पथ हो।

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[सैंपल कोड](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

यदि आप क्लाउड और एज डिवाइस पर एक साथ `.gguf` फाइल का उपयोग करना चाहते हैं, तो LlamaEdge एक शानदार विकल्प है। शुरू करने के लिए आप इस [सैंपल कोड](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) को देख सकते हैं।

### Android फोन पर इंस्टॉल और रन करें

1. **MLC Chat ऐप डाउनलोड करें** (मुफ्त) Android फोन के लिए।
2. APK फाइल (148MB) डाउनलोड करें और अपने डिवाइस पर इंस्टॉल करें।
3. MLC Chat ऐप लॉन्च करें। आपको AI मॉडल की सूची दिखाई देगी, जिसमें Phi-3-mini भी शामिल है।

सारांश में, Phi-3-mini एज डिवाइस पर जनरेटिव AI के लिए रोमांचक संभावनाएं खोलता है, और आप इसे Android पर एक्सप्लोर करना शुरू कर सकते हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या अशुद्धियां हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।