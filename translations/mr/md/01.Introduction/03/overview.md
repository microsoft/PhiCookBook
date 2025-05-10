<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:21:49+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "mr"
}
-->
Phi-3-mini च्या संदर्भात, inference म्हणजे इनपुट डेटावर आधारित अंदाज लावणे किंवा आउटपुट तयार करण्यासाठी मॉडेल वापरण्याची प्रक्रिया. Phi-3-mini आणि त्याच्या inference क्षमतांबद्दल मला तुम्हाला अधिक माहिती द्यायची आहे.

Phi-3-mini हा Microsoft कडून रिलीज केलेल्या Phi-3 मालिकेतील एक मॉडेल आहे. हे मॉडेल Small Language Models (SLMs) मध्ये नवीन शक्यता निर्माण करण्यासाठी डिझाइन केले आहे.

Phi-3-mini आणि त्याच्या inference क्षमतांबद्दल काही महत्त्वाचे मुद्दे:

## **Phi-3-mini चे आढावा:**
- Phi-3-mini चे पॅरामीटर साइज 3.8 अब्ज आहे.
- हे पारंपरिक संगणकीय उपकरणांवरच नाही तर मोबाइल आणि IoT सारख्या edge डिव्हाइसेसवरही चालू शकते.
- Phi-3-mini च्या रिलीजमुळे व्यक्ती आणि उद्योगांना वेगवेगळ्या हार्डवेअर डिव्हाइसेसवर SLMs deploy करता येतात, विशेषतः ज्या ठिकाणी संसाधने कमी आहेत अशा वातावरणात.
- हे विविध मॉडेल फॉरमॅट्सना कव्हर करते, जसे पारंपरिक PyTorch फॉरमॅट, gguf फॉरमॅटचा quantized व्हर्जन, आणि ONNX आधारित quantized व्हर्जन.

## **Phi-3-mini कसे Access करावे:**
Phi-3-mini access करण्यासाठी तुम्ही Copilot application मध्ये [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) वापरू शकता. Semantic Kernel सामान्यतः Azure OpenAI Service, Hugging Face वरील open-source मॉडेल्स, आणि लोकल मॉडेल्ससह सुसंगत आहे.
तसेच quantized मॉडेल्स कॉल करण्यासाठी [Ollama](https://ollama.com) किंवा [LlamaEdge](https://llamaedge.com) वापरू शकता. Ollama वैयक्तिक वापरकर्त्यांना वेगवेगळ्या quantized मॉडेल्स कॉल करण्याची मुभा देते, तर LlamaEdge GGUF मॉडेल्ससाठी cross-platform availability पुरवते.

## **Quantized मॉडेल्स:**
अनेक वापरकर्ते लोकल inference साठी quantized मॉडेल्स वापरणे पसंत करतात. उदाहरणार्थ, तुम्ही थेट Ollama मध्ये Phi-3 चालवू शकता किंवा offline वापरासाठी Modelfile कॉन्फिगर करू शकता. Modelfile मध्ये GGUF फाइलचा पथ आणि prompt फॉरमॅट दिलेला असतो.

## **Generative AI च्या शक्यता:**
Phi-3-mini सारख्या SLMs चा संगम generative AI मध्ये नवीन शक्यता उघडतो. Inference हा फक्त पहिला टप्पा आहे; हे मॉडेल्स संसाधन-आडचणी, latency-आधारित, आणि खर्च-आडचणीच्या परिस्थितीत विविध कामांसाठी वापरले जाऊ शकतात.

## **Phi-3-mini सह Generative AI unlock करणे: Inference आणि Deployment साठी मार्गदर्शन**
Semantic Kernel, Ollama/LlamaEdge, आणि ONNX Runtime वापरून Phi-3-mini मॉडेल्स access आणि infer कसे करायचे ते शिका, आणि विविध application scenarios मध्ये generative AI च्या शक्यतांचा शोध घ्या.

**Features**  
phi3-mini मॉडेल inference करता येते:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

सारांश म्हणून, Phi-3-mini विकसकांना विविध मॉडेल फॉरमॅट्स एक्सप्लोर करण्याची आणि विविध application scenarios मध्ये generative AI चा फायदा घेण्याची संधी देते.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीसाठी आम्ही जबाबदार नाही.