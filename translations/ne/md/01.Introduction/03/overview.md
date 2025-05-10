<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:22:17+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "ne"
}
-->
Phi-3-mini को सन्दर्भमा, inference भनेको मोडेललाई इनपुट डाटाको आधारमा भविष्यवाणी गर्न वा आउटपुट उत्पादन गर्न प्रयोग गर्ने प्रक्रिया हो। म तपाईंलाई Phi-3-mini र यसको inference क्षमताहरूको बारेमा थप विवरण दिन्छु।

Phi-3-mini Microsoft द्वारा रिलिज गरिएको Phi-3 सिरिजको हिस्सा हो। यी मोडेलहरू साना भाषा मोडेलहरू (SLMs) मा सम्भावनाहरू पुनःपरिभाषित गर्न डिजाइन गरिएको हो।

यहाँ Phi-3-mini र यसको inference क्षमताहरूका केहि मुख्य बुँदाहरू छन्:

## **Phi-3-mini अवलोकन:**
- Phi-3-mini को प्यारामिटर साइज 3.8 बिलियन छ।
- यो परम्परागत कम्प्युटिङ उपकरणहरूमा मात्र होइन, मोबाइल उपकरणहरू र IoT उपकरणहरू जस्ता edge उपकरणहरूमा पनि चलाउन सकिन्छ।
- Phi-3-mini को रिलिजले व्यक्तिहरू र उद्यमहरूलाई विभिन्न हार्डवेयर उपकरणहरूमा SLM हरू डिप्लोय गर्न सक्षम बनाउँछ, विशेष गरी स्रोत सीमित वातावरणहरूमा।
- यसले विभिन्न मोडेल फर्म्याटहरू कभर गर्दछ, जसमा परम्परागत PyTorch फर्म्याट, gguf फर्म्याटको क्वान्टाइज्ड संस्करण, र ONNX आधारित क्वान्टाइज्ड संस्करण समावेश छन्।

## **Phi-3-mini पहुँच:**
Phi-3-mini पहुँच गर्न, तपाईं Copilot एप्लिकेशनमा [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) प्रयोग गर्न सक्नुहुन्छ। Semantic Kernel सामान्यतया Azure OpenAI Service, Hugging Face मा खुला स्रोत मोडेलहरू, र स्थानीय मोडेलहरूसँग अनुकूल हुन्छ।
तपाईं [Ollama](https://ollama.com) वा [LlamaEdge](https://llamaedge.com) मार्फत क्वान्टाइज्ड मोडेलहरू पनि कल गर्न सक्नुहुन्छ। Ollama व्यक्तिगत प्रयोगकर्ताहरूलाई विभिन्न क्वान्टाइज्ड मोडेलहरू कल गर्न अनुमति दिन्छ, जबकि LlamaEdge ले GGUF मोडेलहरूको क्रस-प्ल्याटफर्म उपलब्धता प्रदान गर्दछ।

## **क्वान्टाइज्ड मोडेलहरू:**
धेरै प्रयोगकर्ताहरू स्थानीय inference को लागि क्वान्टाइज्ड मोडेलहरू प्रयोग गर्न रुचाउँछन्। उदाहरणका लागि, तपाईं सिधै Ollama मार्फत Phi-3 चलाउन सक्नुहुन्छ वा Modelfile प्रयोग गरी अफलाइन कन्फिगर गर्न सक्नुहुन्छ। Modelfile ले GGUF फाइल पथ र प्रॉम्प्ट फर्म्याट निर्दिष्ट गर्दछ।

## **Generative AI सम्भावनाहरू:**
Phi-3-mini जस्ता SLM हरूको संयोजनले जनरेटिभ AI का नयाँ सम्भावनाहरू खोल्छ। inference मात्र पहिलो कदम हो; यी मोडेलहरू स्रोत सीमित, लेटेन्सी सीमित, र लागत सीमित अवस्थाहरूमा विभिन्न कार्यहरूका लागि प्रयोग गर्न सकिन्छ।

## **Phi-3-mini सँग जनरेटिभ AI अनलक गर्ने: Inference र Deployment को मार्गदर्शन**  
Semantic Kernel, Ollama/LlamaEdge, र ONNX Runtime प्रयोग गरी Phi-3-mini मोडेलहरू पहुँच र inference कसरी गर्ने सिक्नुहोस्, र विभिन्न अनुप्रयोग परिदृश्यहरूमा जनरेटिभ AI का सम्भावनाहरू अन्वेषण गर्नुहोस्।

**विशेषताहरू**  
phi3-mini मोडेलमा inference:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

सारांशमा, Phi-3-mini ले विकासकर्ताहरूलाई विभिन्न मोडेल फर्म्याटहरू अन्वेषण गर्न र विभिन्न अनुप्रयोग परिदृश्यहरूमा जनरेटिभ AI को उपयोग गर्न सक्षम बनाउँछ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको प्रयास गर्छौं, तर कृपया बुझ्नुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा गलतफहमीहरू हुन सक्छन्। मूल दस्तावेज यसको मूल भाषामा नै आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।