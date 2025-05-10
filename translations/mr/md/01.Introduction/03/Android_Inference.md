<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:42:28+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "mr"
}
-->
# **Android मध्ये Phi-3 वापरून Inference**

चला पाहूया की Android डिव्हाइसेसवर Phi-3-mini वापरून inference कसे करता येते. Phi-3-mini ही Microsoft कडून आलेली नवीन मॉडेल्सची मालिका आहे जी Edge डिव्हाइसेस आणि IoT डिव्हाइसेसवर Large Language Models (LLMs) तैनात करण्यास सक्षम करते.

## Semantic Kernel आणि Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) हा एक application framework आहे जो तुम्हाला Azure OpenAI Service, OpenAI मॉडेल्स, आणि अगदी local मॉडेल्ससह सुसंगत अ‍ॅप्लिकेशन्स तयार करण्याची परवानगी देतो. जर तुम्ही Semantic Kernel बद्दल नवीन असाल, तर आम्ही तुम्हाला [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) पाहण्याचा सल्ला देतो.

### Semantic Kernel वापरून Phi-3-mini कसे Access कराल

तुम्ही ते Semantic Kernel मधील Hugging Face Connector सोबत एकत्र करू शकता. यासाठी हा [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) पाहा.

डिफॉल्टनं, हे Hugging Face वरील मॉडेल ID शी जुळते. पण तुम्ही locally तयार केलेल्या Phi-3-mini मॉडेल सर्व्हरशी देखील कनेक्ट करू शकता.

### Ollama किंवा LlamaEdge वापरून Quantized Models कॉल करणे

खूप वापरकर्ते quantized मॉडेल्स वापरून मॉडेल्स स्थानिक पद्धतीने चालवायला प्राधान्य देतात. [Ollama](https://ollama.com/) आणि [LlamaEdge](https://llamaedge.com) हे वैयक्तिक वापरकर्त्यांना वेगवेगळ्या quantized मॉडेल्स कॉल करण्याची परवानगी देतात:

#### Ollama

तुम्ही थेट `ollama run Phi-3` चालवू शकता किंवा offline मध्ये `Modelfile` तयार करून त्यात तुमच्या `.gguf` फाईलचा पथ देऊन कॉन्फिगर करू शकता.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

जर तुम्हाला क्लाउड आणि edge डिव्हाइसेसवर एकाच वेळी `.gguf` फाईल्स वापरायच्या असतील, तर LlamaEdge एक उत्तम पर्याय आहे. सुरुवात करण्यासाठी हा [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) पाहू शकता.

### Android फोनवर Install आणि Run करा

1. **MLC Chat अ‍ॅप डाउनलोड करा** (Free) Android फोनसाठी.
2. APK फाईल (148MB) डाउनलोड करून तुमच्या डिव्हाइसवर इंस्टॉल करा.
3. MLC Chat अ‍ॅप उघडा. तुम्हाला AI मॉडेल्सची यादी दिसेल, ज्यात Phi-3-mini देखील आहे.

सारांश म्हणून, Phi-3-mini edge डिव्हाइसेसवर generative AI साठी नवीन शक्यता उघडते, आणि तुम्ही Android वर त्याच्या क्षमता एक्सप्लोर करायला सुरुवात करू शकता.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, परंतु कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागीसाठी आम्ही जबाबदार नाही.