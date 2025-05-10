<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-05-09T19:11:16+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "ne"
}
-->
# **आफ्नै Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 परिवारसँग बनाउनुहोस्**

तपाईंले GitHub Copilot Chat मा workspace agent प्रयोग गर्नुभएको छ? के तपाईं आफ्नो टिमको कोड एजेन्ट बनाउन चाहनुहुन्छ? यो प्रयोगात्मक ल्याबले खुला स्रोत मोडेललाई समायोजन गरी उद्यम स्तरको कोड व्यवसाय एजेन्ट बनाउन सहयोग पुर्‍याउने आशा राख्छ।

## **आधार**

### **किन Microsoft Phi-3 रोज्ने**

Phi-3 एउटा परिवार हो, जसमा phi-3-mini, phi-3-small, र phi-3-medium समावेश छन्, जुन विभिन्न प्रशिक्षण प्यारामिटरहरूका आधारमा टेक्स्ट उत्पादन, संवाद पूरा गर्ने, र कोड निर्माणका लागि छन्। साथै, Vision आधारित phi-3-vision पनि छ। यो उद्यम वा विभिन्न टिमहरूलाई अफलाइन जेनेरेटिभ AI समाधानहरू बनाउन उपयुक्त छ।

यो लिंक पढ्न सिफारिस गरिन्छ [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat एक्सटेन्सनले तपाईंलाई एक च्याट इन्टरफेस दिन्छ जसले GitHub Copilot सँग अन्तरक्रिया गर्न र कोडिङ सम्बन्धी प्रश्नहरूको जवाफ VS Code भित्रै पाउन मद्दत गर्दछ, जसका लागि तपाईंलाई दस्तावेजहरू हेर्न वा अनलाइन फोरम खोज्न आवश्यक पर्दैन।

Copilot Chat ले उत्पन्न जवाफमा स्पष्टता थप्न सिन्ट्याक्स हाइलाइटिङ, इन्डेन्टेसन, र अन्य फर्म्याटिङ सुविधाहरू प्रयोग गर्न सक्छ। प्रयोगकर्ताको प्रश्नको प्रकार अनुसार, नतिजामा सन्दर्भका लागि लिंकहरू, जस्तै स्रोत कोड फाइलहरू वा दस्तावेजहरू, वा VS Code को कार्यक्षमता पहुँच गर्ने बटनहरू समावेश हुन सक्छ।

- Copilot Chat तपाईंको विकासकर्ताको प्रवाहमा समाहित हुन्छ र जहाँ आवश्यक हुन्छ सहयोग दिन्छ:

- सम्पादक वा टर्मिनलबाट सिधै इनलाइन च्याट सुरु गरेर कोडिङको समयमा सहयोग पाउनुहोस्

- Chat दृश्य प्रयोग गरेर AI सहायकलाई सधैं साथमा राख्नुहोस्

- Quick Chat सुरु गरेर छिटो प्रश्न सोध्नुहोस् र पुनः काममा फर्कनुहोस्

तपाईं GitHub Copilot Chat विभिन्न परिस्थितिहरूमा प्रयोग गर्न सक्नुहुन्छ, जस्तै:

- समस्याको उत्तम समाधान कसरी गर्ने भनेर कोडिङ प्रश्नहरूको जवाफ दिने

- अरूको कोड व्याख्या गर्ने र सुधार सुझाव दिने

- कोड सुधार प्रस्ताव गर्ने

- युनिट टेस्ट केसहरू उत्पादन गर्ने

- कोड दस्तावेजीकरण बनाउने

यो लिंक पढ्न सिफारिस गरिन्छ [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat मा **@workspace** प्रयोग गर्दा तपाईंले सम्पूर्ण कोडबेसका बारेमा प्रश्न गर्न सक्नुहुन्छ। प्रश्नको आधारमा, Copilot ले सान्दर्भिक फाइलहरू र प्रतीकहरू बुद्धिमानीपूर्वक खोज्छ र जवाफमा लिंक र कोड उदाहरणको रूपमा प्रस्तुत गर्छ।

तपाईंको प्रश्नको जवाफ दिन, **@workspace** ले VS Code मा विकासकर्ताले कोडबेस नेभिगेट गर्दा प्रयोग गर्ने स्रोतहरू खोज्छ:

- workspace भित्रका सबै फाइलहरू, तर .gitignore फाइलले बेवास्ता गरेका फाइलहरू बाहेक

- नेस्टेड फोल्डर र फाइल नामहरू सहितको डाइरेक्टरी संरचना

- यदि workspace GitHub रिपोजिटोरी हो र कोड सर्चले अनुक्रमित गरेको छ भने GitHub को कोड सर्च इन्डेक्स

- workspace भित्रका प्रतीकहरू र परिभाषाहरू

- सक्रिय सम्पादकमा हाल चयन गरिएको वा देखिने टेक्स्ट

ध्यान दिनुहोस्: .gitignore त्यागिनेछ यदि तपाईंले बेवास्ता गरिएको फाइल खोल्नुभएको छ वा त्यसमा टेक्स्ट चयन गर्नुभएको छ भने।

यो लिंक पढ्न सिफारिस गरिन्छ [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **यो ल्याबबारे थप जान्नुहोस्**

GitHub Copilot ले उद्यमहरूको प्रोग्रामिङ दक्षता धेरै सुधार गरेको छ, र प्रत्येक उद्यमले GitHub Copilot का सम्बन्धित कार्यहरू अनुकूलन गर्न चाहन्छ। धेरै उद्यमहरूले आफ्नै व्यापारिक परिदृश्य र खुला स्रोत मोडेलहरूमा आधारित GitHub Copilot जस्ता अनुकूलित एक्सटेन्सनहरू बनाएका छन्। उद्यमहरूका लागि, अनुकूलित एक्सटेन्सनहरू नियन्त्रण गर्न सजिलो हुन्छ, तर यसले प्रयोगकर्ता अनुभवमा असर पार्न सक्छ। आखिर, GitHub Copilot सामान्य परिदृश्य र व्यावसायिकतामा बलियो छ। यदि अनुभव सुसंगत राख्न सकिन्छ भने, आफ्नै उद्यमको एक्सटेन्सन अनुकूलन गर्नु राम्रो हुन्छ। GitHub Copilot Chat ले उद्यमहरूलाई च्याट अनुभव विस्तार गर्न सम्बन्धित API हरू प्रदान गर्दछ। सुसंगत अनुभव कायम राख्दै अनुकूलित कार्यहरू हुनु राम्रो प्रयोगकर्ता अनुभव हो।

यो ल्याब मुख्य रूपमा Phi-3 मोडेललाई स्थानीय NPU र Azure हाइब्रिडसँग मिलाएर GitHub Copilot Chat मा अनुकूलित एजेन्ट ***@PHI3*** निर्माण गर्छ, जसले उद्यम विकासकर्ताहरूलाई कोड निर्माणमा सहयोग गर्छ ***(@PHI3 /gen)*** र छविका आधारमा कोड उत्पादन गर्छ ***(@PHI3 /img)***।

![PHI3](../../../../../../../translated_images/cover.410a18b85555fad4ca8bfb8f0b1776a96ae7f8eae1132b8f0c09d4b92b8e3365.ne.png)

### ***Note:*** 

यो ल्याब हाल Intel CPU र Apple Silicon को AIPC मा कार्यान्वयन गरिएको छ। हामी Qualcomm NPU संस्करण पनि अपडेट गर्दै जानेछौं।

## **ल्याब**

| नाम | विवरण | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | सम्बन्धित वातावरण र स्थापना उपकरणहरू कन्फिगर र इन्स्टल गर्नुहोस् | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | AIPC / Apple Silicon सँग मिलाएर, स्थानीय NPU प्रयोग गरी Phi-3-mini मार्फत कोड निर्माण गर्नुहोस् | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Azure Machine Learning Service को मोडेल क्याटलग - Phi-3-vision छवि तैनाथ गरेर कोड उत्पादन गर्नुहोस् | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | GitHub Copilot Chat मा अनुकूलित Phi-3 एजेन्ट सिर्जना गरी कोड उत्पादन, ग्राफ निर्माण कोड, RAG आदि पूरा गर्नुहोस् | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | नमूना कोड डाउनलोड गर्नुहोस् | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **स्रोतहरू**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot को बारेमा थप जान्नुहोस् [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat को बारेमा थप जान्नुहोस् [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API को बारेमा थप जान्नुहोस् [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Foundry को बारेमा थप जान्नुहोस् [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI Foundry को Model Catalog को बारेमा थप जान्नुहोस् [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी सटीकताको लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धि हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।