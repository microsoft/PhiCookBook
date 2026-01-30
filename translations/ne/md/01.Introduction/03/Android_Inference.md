# **एन्ड्रोइडमा Inference Phi-3**

आउनुहोस्, हामीले कसरी Phi-3-mini सँग एन्ड्रोइड उपकरणहरूमा inference गर्न सकिन्छ भनेर अन्वेषण गरौं। Phi-3-mini माइक्रोसफ्टको नयाँ मोडेल श्रृंखला हो जसले edge उपकरणहरू र IoT उपकरणहरूमा Large Language Models (LLMs) को तैनाती सक्षम बनाउँछ।

## Semantic Kernel र Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) एउटा एप्लिकेशन फ्रेमवर्क हो जसले तपाईंलाई Azure OpenAI Service, OpenAI मोडेलहरू, र स्थानीय मोडेलहरूसँग मिल्ने एप्लिकेशनहरू बनाउन अनुमति दिन्छ। यदि तपाईं Semantic Kernel मा नयाँ हुनुहुन्छ भने, हामी तपाईंलाई [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) हेर्न सल्लाह दिन्छौं।

### Semantic Kernel प्रयोग गरी Phi-3-mini पहुँच गर्न

तपाईं यसलाई Semantic Kernel मा Hugging Face Connector सँग जोड्न सक्नुहुन्छ। यसका लागि यो [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) हेर्नुहोस्।

डिफल्ट रूपमा, यो Hugging Face मा मोडेल ID सँग मेल खान्छ। तर, तपाईंले स्थानीय रूपमा बनाएको Phi-3-mini मोडेल सर्भरमा पनि जडान गर्न सक्नुहुन्छ।

### Ollama वा LlamaEdge सँग Quantized मोडेलहरू कल गर्ने

धेरै प्रयोगकर्ताहरू मोडेलहरू स्थानीय रूपमा चलाउन quantized मोडेलहरू प्रयोग गर्न रुचाउँछन्। [Ollama](https://ollama.com/) र [LlamaEdge](https://llamaedge.com) ले व्यक्तिगत प्रयोगकर्ताहरूलाई विभिन्न quantized मोडेलहरू कल गर्न अनुमति दिन्छन्:

#### Ollama

तपाईं सिधै `ollama run Phi-3` चलाउन सक्नुहुन्छ वा आफ्नो `.gguf` फाइलको पथ सहित `Modelfile` बनाएर अफलाइन कन्फिगर गर्न सक्नुहुन्छ।

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

यदि तपाईंले क्लाउड र edge उपकरणहरूमा एकै समयमा `.gguf` फाइलहरू प्रयोग गर्न चाहनुहुन्छ भने, LlamaEdge उत्कृष्ट विकल्प हो। सुरु गर्न यो [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) हेर्न सक्नुहुन्छ।

### एन्ड्रोइड फोनमा इन्स्टल र चलाउने तरिका

1. **MLC Chat एप डाउनलोड गर्नुहोस्** (निःशुल्क) एन्ड्रोइड फोनका लागि।
2. APK फाइल (१४८MB) डाउनलोड गरी आफ्नो उपकरणमा इन्स्टल गर्नुहोस्।
3. MLC Chat एप खोल्नुहोस्। तपाईंले Phi-3-mini सहित विभिन्न AI मोडेलहरूको सूची देख्नुहुनेछ।

संक्षेपमा, Phi-3-mini ले edge उपकरणहरूमा जनरेटिभ AI का लागि रोचक सम्भावनाहरू खोल्छ, र तपाईं यसको क्षमता एन्ड्रोइडमा अन्वेषण गर्न सुरु गर्न सक्नुहुन्छ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।