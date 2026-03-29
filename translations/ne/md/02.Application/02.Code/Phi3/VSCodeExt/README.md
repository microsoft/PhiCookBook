# **आफ्नै Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 परिवारसँग बनाउनुहोस्**

तपाईंले GitHub Copilot Chat मा workspace एजेन्ट प्रयोग गर्नुभएको छ? के तपाईं आफ्नो टोलीको कोड एजेन्ट बनाउन चाहनुहुन्छ? यो ह्यान्ड्स-ऑन ल्याबले खोलिएको स्रोत मोडललाई समेटेर एक उद्यम स्तरको कोड व्यवसायिक एजेन्ट बनाउन आशा राख्दछ।

## **आधार**

### **किन Microsoft Phi-3 छनोट गर्ने**

Phi-3 एक परिवार श्रृंखला हो, जसमा phi-3-mini, phi-3-small, र phi-3-medium समावेश छन् जुन पाठ उत्पादन, संवाद पूरा गर्ने, र कोड उत्पादनका लागि विभिन्न प्रशिक्षण प्यारामिटरहरूमा आधारित छन्। त्यहाँ Vision मा आधारित phi-3-vision पनि छ। यो उद्यम वा विभिन्न टोलीहरूले अफलाइन जेनेरेटिभ AI समाधानहरू सिर्जना गर्न उपयुक्त छ।

सिफारिस गरिएको पढ्न [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat एक्सटेन्सनले तपाईंलाई यस्तो च्याट इन्टरफेस दिन्छ जसले तपाईंलाई GitHub Copilot सँग अन्तरक्रिया गर्न र कोडिंग सम्बन्धी प्रश्नहरूको उत्तरहरू सीधै VS Code भित्र प्राप्त गर्न अनुमति दिन्छ, जसका लागि तपाईंले डक्युमेन्टेसनमा नेभिगेट गर्न वा अनलाइन फोरमहरू खोज्न आवश्यक पर्दैन।

Copilot Chat ले उत्पन्न गरिएको उत्तरमा स्पष्टता थप्न सिन्टेक्स हाइलाइटिङ, इन्डेन्टेसन र अन्य स्वरूपण सुविधाहरू प्रयोग गर्न सक्छ। प्रयोगकर्ताबाट आएको प्रश्नको प्रकारअनुसार, नतिजाले सन्दर्भका लागि Copilot ले प्रयोग गरेको स्रोत कोड फाइलहरू वा डक्युमेन्टेसन, वा VS Code को कार्यक्षमताहरू पहुँच गर्ने बटन्सहरू समावेश गर्न सक्छ।

- Copilot Chat तपाईंको विकासकर्ता प्रवाहसँग एकीकृत हुन्छ र तपाईंलाई जहाँ आवश्यक हुन्छ त्यहाँ सहायता दिन्छ:

- सम्पादक वा टर्मिनलबाट सिधा इनलाइन च्याट संवाद सुरु गर्नुहोस् जब तपाईं कोड गर्दै हुनुहुन्छ सहयोगका लागि

- कुनै पनि समयमा मद्दतका लागि साइडमा AI सहायक राख्न च्याट दृश्य प्रयोग गर्नुहोस्

- छिटो प्रश्न सोध्न र आफ्नो काममा फर्कन छिटो च्याट सुरु गर्नुहोस्

तपाईं GitHub Copilot Chat विभिन्न परिदृश्यहरूमा प्रयोग गर्न सक्नुहुन्छ, जस्तै:

- समस्याको उत्कृष्ट समाधान कसरी गर्ने भनेर कोडिङ प्रश्नहरूको उत्तर दिन

- अरूको कोड व्याख्या गर्ने र सुधार सुुझाव दिन

- कोड सुधार प्रस्ताव गर्ने

- युनिट टेस्ट केसहरू उत्पादन गर्ने

- कोड डक्युमेन्टेसन उत्पादन गर्ने

सिफारिस गरिएको पढ्न [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat मा **@workspace** लाई सन्दर्भ गर्दा तपाईंले आफ्नो सम्पूर्ण कोडबेस सम्बन्धी प्रश्नहरू सोध्न सक्नुहुन्छ। प्रश्नको आधारमा, Copilot ले सम्बद्ध फाइलहरू र प्रतीकहरू बुद्धिमत्तापूर्वक पुनः प्राप्त गर्दछ, जुन जवाफमा लिङ्कहरू र कोड उदाहरणहरूको रूपमा उल्लेख गर्दछ।

तपाईंको प्रश्नको उत्तर दिन, **@workspace** ले VS Code मा कोडबेस नेभिगेट गर्दा विकासकर्ताले प्रयोग गर्ने समान स्रोतहरू खोज्छ:

- .gitignore फाइलले नरहेको फाइलहरू बाहेक कार्यस्थानका सबै फाइलहरू

- फोल्डर भित्रको फोल्डर संरचना र फाइल नामहरू सहितको निर्देशिका संरचना

- यदि कार्यस्थान GitHub रिपोजिटोरी हो र कोड सर्चद्वारा सूचीबद्ध छ भने GitHub को कोड सर्च सूचीकरण

- कार्यस्थानमा प्रतीकहरू र परिभाषाहरू

- हाल चयन गरिएको पाठ वा सक्रिय सम्पादकमा देखिने पाठ

टिप्पणी: .gitignore लाई तब बेवास्ता गरिन्छ जब तपाईंले एउटा फाइल खोल्नु भएको छ वा निर्दिष्ट गरिएको फाइलभित्र पाठ चयन गर्नु भएको छ।

सिफारिस गरिएको पढ्न [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **यस ल्याबको बारेमा थप जान्नुहोस्**

GitHub Copilot ले उद्यमहरूको प्रोग्रामिङ दक्षतालाई राम्रोसँग सुधार गरेको छ, र हरेक उद्यमले GitHub Copilot को सम्बन्धित कार्यहरू अनुकूलित गर्न चाहन्छ। धेरै उद्यमहरूले आफ्नै व्यापारिक परिदृश्य र खुलेआम स्रोत मोडेलहरूमा आधारित GitHub Copilot जस्तै कस्टमाइज्ड एक्सटेन्सनहरू विकास गरेका छन्। उद्यमहरूको लागि कस्टमाइज्ड एक्सटेन्सनहरू नियन्त्रण गर्न सजिलो हुन्छ, तर यसले प्रयोगकर्ता अनुभवलाई प्रभाव पार्न सक्छ। अन्ततः, GitHub Copilot सामान्य परिदृश्य र व्यावसायिकतामा बलियो कार्यहरू गर्दछन्। यदि अनुभव निरन्तर राख्न सकियो भने, उद्यमको आफ्नै एक्सटेन्सनलाई अनुकूलन गर्नु राम्रो हुनेछ। GitHub Copilot Chat उद्यमहरूलाई च्याट अनुभवमा विस्तार गर्न सम्बन्धित API उपलब्ध गराउँछ। सुसंगत अनुभव कायम राख्नु र अनुकूलित कार्यहरू हुनु राम्रो प्रयोगकर्ता अनुभव हो।

यो ल्याब मुख्य रूपमा Phi-3 मोडललाई स्थानीय NPU र Azure हाइब्रिडसँग जोडेर GitHub Copilot Chat मा कस्टम एजेन्ट ***@PHI3*** निर्माण गर्न प्रयोग गर्दछ जसले उद्यम विकासकर्ताहरूलाई कोड उत्पादन पूरा गर्न ***(@PHI3 /gen)*** र तस्बिर आधारित कोड उत्पादन गर्न ***(@PHI3 /img)*** सहयोग गर्दछ।

![PHI3](../../../../../../../translated_images/ne/cover.1017ebc9a7c46d09.webp)

### ***टिप्पणी:***

यो ल्याब हाल Intel CPU र Apple Silicon को AIPC मा कार्यान्वयन गरिएको छ। हामी Qualcomm संस्करण NPU को लागि अपडेट जारी गर्नेछौँ।


## **ल्याब**


| नाम | वर्णन | AIPC | एप्पल |
| ------------ | ----------- | -------- |-------- |
| Lab0 - स्थापना(✅) | सम्बन्धित वातावरणहरू र स्थापना उपकरणहरू कन्फिगर र स्थापना गर्नुहोस् | [जानुहोस्](./HOL/AIPC/01.Installations.md) |[जानुहोस्](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini सँग Prompt flow चलाउनुहोस् (✅) | AIPC / Apple Silicon सँग मिलेर, स्थानीय NPU प्रयोग गरी Phi-3-mini मार्फत कोड उत्पादन सिर्जना गर्नुहोस् | [जानुहोस्](./HOL/AIPC/02.PromptflowWithNPU.md) |  [जानुहोस्](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning सेवा मा Phi-3-vision डिप्लॉय गर्नुहोस् (✅) | Azure Machine Learning सेवा को मोडेल क्याटलग - Phi-3-vision छवि डिप्लॉय गरेर कोड उत्पादन गर्नुहोस् | [जानुहोस्](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[जानुहोस्](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat मा @phi-3 एजेन्ट सिर्जना गर्नुहोस्(✅)  | GitHub Copilot Chat मा कस्टम Phi-3 एजेन्ट सिर्जना गरी कोड उत्पादन, ग्राफ उत्पादन कोड, RAG आदि पूरा गर्नुहोस् | [जानुहोस्](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [जानुहोस्](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| नमूना कोड (✅)  | नमूना कोड डाउनलोड गर्नुहोस् | [जानुहोस्](../../../../../../../code/07.Lab/01/AIPC) | [जानुहोस्](../../../../../../../code/07.Lab/01/Apple) |


## **संसाधनहरू**

1. Phi-3 कुकबुक [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot बारे थप जान्नुहोस् [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat बारे थप जान्नुहोस् [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API बारे थप जान्नुहोस् [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry बारे थप जान्नुहोस् [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry को मोडेल क्याटलग बारे थप जान्नुहोस् [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यस दस्तावेज़लाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुनसक्छन्। मूल दस्तावेज़ यसको स्वदेशी भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->