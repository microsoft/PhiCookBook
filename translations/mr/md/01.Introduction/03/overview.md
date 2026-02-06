Phi-3-mini च्या संदर्भात, inference म्हणजे इनपुट डेटावर आधारित अंदाज लावणे किंवा आउटपुट तयार करण्यासाठी मॉडेलचा वापर करण्याची प्रक्रिया. Phi-3-mini आणि त्याच्या inference क्षमतांविषयी अधिक माहिती देतो.

Phi-3-mini हा Microsoft कडून रिलीज झालेल्या Phi-3 मालिकेतील एक मॉडेल आहे. हे मॉडेल Small Language Models (SLMs) च्या शक्यतांना नव्याने परिभाषित करण्यासाठी तयार केले गेले आहे.

Phi-3-mini आणि त्याच्या inference क्षमतांविषयी काही महत्त्वाचे मुद्दे:

## **Phi-3-mini चे आढावा:**
- Phi-3-mini मध्ये 3.8 अब्ज पॅरामीटर्स आहेत.
- हे फक्त पारंपरिक संगणकीय उपकरणांवरच नव्हे तर मोबाइल आणि IoT सारख्या एज डिव्हाइसेसवरही चालू शकते.
- Phi-3-mini च्या रिलीजमुळे व्यक्ती आणि उद्योगांना विविध हार्डवेअर डिव्हाइसेसवर, विशेषतः संसाधन मर्यादित वातावरणात SLMs तैनात करण्याची संधी मिळाली आहे.
- हे पारंपरिक PyTorch फॉरमॅट, gguf फॉरमॅटचा क्वांटाइज्ड व्हर्जन, आणि ONNX-आधारित क्वांटाइज्ड व्हर्जन यांसह विविध मॉडेल फॉरमॅट्सना कव्हर करते.

## **Phi-3-mini कसे वापरावे:**
Phi-3-mini वापरण्यासाठी, तुम्ही Copilot अॅप्लिकेशनमध्ये [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) वापरू शकता. Semantic Kernel सामान्यतः Azure OpenAI Service, Hugging Face वरील ओपन-सोर्स मॉडेल्स, आणि लोकल मॉडेल्ससह सुसंगत आहे.  
तसेच, क्वांटाइज्ड मॉडेल्स कॉल करण्यासाठी तुम्ही [Ollama](https://ollama.com) किंवा [LlamaEdge](https://llamaedge.com) वापरू शकता. Ollama वैयक्तिक वापरकर्त्यांना विविध क्वांटाइज्ड मॉडेल्स कॉल करण्याची परवानगी देते, तर LlamaEdge GGUF मॉडेल्ससाठी क्रॉस-प्लॅटफॉर्म उपलब्धता पुरवते.

## **क्वांटाइज्ड मॉडेल्स:**
अनेक वापरकर्ते स्थानिक inference साठी क्वांटाइज्ड मॉडेल्स वापरणे पसंत करतात. उदाहरणार्थ, तुम्ही थेट Ollama वापरून Phi-3 चालवू शकता किंवा Modelfile वापरून ऑफलाइन कॉन्फिगर करू शकता. Modelfile मध्ये GGUF फाइलचा पथ आणि प्रॉम्प्ट फॉरमॅट दिलेला असतो.

## **जनरेटिव्ह AI च्या शक्यता:**
Phi-3-mini सारख्या SLMs चा वापर करून जनरेटिव्ह AI मध्ये नवीन शक्यता उघडतात. Inference हा फक्त पहिला टप्पा आहे; हे मॉडेल्स संसाधन मर्यादित, लेटन्सी-बाउंड आणि खर्च मर्यादित परिस्थितींमध्ये विविध कामांसाठी वापरले जाऊ शकतात.

## **Phi-3-mini सह जनरेटिव्ह AI अनलॉक करणे: Inference आणि Deployment साठी मार्गदर्शक**  
Semantic Kernel, Ollama/LlamaEdge, आणि ONNX Runtime वापरून Phi-3-mini मॉडेल्स कसे access आणि infer करायचे ते शिका, आणि विविध अॅप्लिकेशन परिस्थितींमध्ये जनरेटिव्ह AI च्या शक्यता एक्सप्लोर करा.

**वैशिष्ट्ये**  
Phi-3-mini मॉडेलचे inference खालील माध्यमांत करता येते:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

सारांश म्हणून, Phi-3-mini विकसकांना विविध मॉडेल फॉरमॅट्स एक्सप्लोर करण्याची आणि विविध अॅप्लिकेशन परिस्थितींमध्ये जनरेटिव्ह AI चा फायदा घेण्याची संधी देते.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.