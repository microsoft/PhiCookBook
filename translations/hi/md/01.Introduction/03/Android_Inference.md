# **एंड्रॉइड में इनफ़ेरेंस Phi-3**

आइए देखें कि आप कैसे Phi-3-mini के साथ एंड्रॉइड डिवाइसों पर इनफ़ेरेंस कर सकते हैं। Phi-3-mini माइक्रोसॉफ्ट की एक नई मॉडल श्रृंखला है जो एज डिवाइसों और IoT डिवाइसों पर बड़े भाषा मॉडल (LLMs) की तैनाती सक्षम बनाती है।

## सिमेंटिक कर्नल और इनफ़ेरेंस

[सिमेंटिक कर्नल](https://github.com/microsoft/semantic-kernel) एक एप्लिकेशन फ्रेमवर्क है जो आपको Azure OpenAI सेवा, OpenAI मॉडल, और यहां तक कि स्थानीय मॉडल के साथ संगत एप्लिकेशन बनाने की अनुमति देता है। यदि आप सिमेंटिक कर्नल के नए हैं, तो हम सुझाव देते हैं कि आप [सिमेंटिक कर्नल कुकबुक](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) देखें।

### सिमेंटिक कर्नल का उपयोग करके Phi-3-mini तक पहुँचने के लिए

आप इसे सिमेंटिक कर्नल में हगिंग फेस कनेक्टर के साथ जोड़ सकते हैं। इस [सैंपल कोड](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) को देखें।

डिफ़ॉल्ट रूप से, यह हगिंग फेस पर मॉडल आईडी के अनुरूप होता है। हालांकि, आप एक स्थानीय रूप से बनाए गए Phi-3-mini मॉडल सर्वर से भी जुड़ सकते हैं।

### Ollama या LlamaEdge के साथ क्वांटाइज़्ड मॉडल कॉल करना

कई उपयोगकर्ता स्थानीय रूप से मॉडल चलाने के लिए क्वांटाइज़्ड मॉडलों का उपयोग करना पसंद करते हैं। [Ollama](https://ollama.com/) और [LlamaEdge](https://llamaedge.com) व्यक्तिगत उपयोगकर्ताओं को विभिन्न क्वांटाइज़्ड मॉडल कॉल करने की अनुमति देते हैं:

#### Ollama

आप सीधे `ollama run Phi-3` चला सकते हैं या अपनी `.gguf` फ़ाइल के पथ के साथ एक `Modelfile` बनाकर इसे ऑफ़लाइन कॉन्फ़िगर कर सकते हैं।

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[सैंपल कोड](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

यदि आप क्लाउड और एज डिवाइसों पर एक साथ `.gguf` फ़ाइलों का उपयोग करना चाहते हैं, तो LlamaEdge एक उत्कृष्ट विकल्प है। शुरुआत करने के लिए आप इस [सैंपल कोड](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) को देख सकते हैं।

### एंड्रॉइड फोन पर इंस्टॉल करें और चलाएं

1. **MLC चैट ऐप डाउनलोड करें** (मुफ्त) एंड्रॉइड फोन के लिए।
2. APK फ़ाइल (148MB) डाउनलोड करें और इसे अपने डिवाइस पर इंस्टॉल करें।
3. MLC चैट ऐप लॉन्च करें। आपको AI मॉडल्स की सूची दिखाई देगी, जिसमें Phi-3-mini भी शामिल है।

### LiteRT-LM के साथ Phi-4-mini-रीज़निंग चलाएं

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) एक समुदाय-परिवर्तित int4 `.litertlm` बंडल के रूप में उपलब्ध है जो Google के [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) ऑन-डिवाइस रनटाइम के लिए है। एंड्रॉइड पर यह CPU या GPU पर [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) ऐप के माध्यम से चलता है (ऐप के अंदर Hugging Face से बंडल इम्पोर्ट करें) या LiteRT-LM Kotlin API के माध्यम से; वही बंडल iOS, macOS, Linux और Windows पर भी चलता है। मॉडल कार्ड में मापी गई गति और रन कमांड शामिल हैं।

संक्षेप में, Phi-3-mini एज डिवाइसों पर जनरेटिव AI के लिए रोमांचक संभावनाएं खोलता है, और आप इसके फ़ीचर्स को एंड्रॉइड पर एक्सप्लोर करना शुरू कर सकते हैं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->