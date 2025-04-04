<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7302d85639441c7cedbae09795e6b9a6",
  "translation_date": "2025-04-04T18:29:47+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi3\\VSCodeExt\\README.md",
  "language_code": "hi"
}
-->
# **अपना खुद का Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 Family के साथ बनाएं**

क्या आपने GitHub Copilot Chat में वर्कस्पेस एजेंट का उपयोग किया है? क्या आप अपनी टीम के लिए कोड एजेंट बनाना चाहते हैं? यह हैंड्स-ऑन लैब ओपन सोर्स मॉडल को मिलाकर एक एंटरप्राइज-लेवल कोड बिजनेस एजेंट बनाने की कोशिश करता है।

## **आधारभूत जानकारी**

### **Microsoft Phi-3 क्यों चुनें**

Phi-3 एक फैमिली सीरीज है, जिसमें phi-3-mini, phi-3-small, और phi-3-medium शामिल हैं, जो टेक्स्ट जनरेशन, डायलॉग कंप्लीशन और कोड जनरेशन के लिए अलग-अलग ट्रेनिंग पैरामीटर पर आधारित हैं। इसके अलावा Vision पर आधारित phi-3-vision भी है। यह एंटरप्राइज या विभिन्न टीमों के लिए ऑफलाइन जनरेटिव AI समाधान बनाने के लिए उपयुक्त है।

इस लिंक को पढ़ने की सलाह दी जाती है [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat एक्सटेंशन आपको एक चैट इंटरफ़ेस देता है, जिससे आप GitHub Copilot के साथ बातचीत कर सकते हैं और सीधे VS Code में कोडिंग से संबंधित प्रश्नों के उत्तर प्राप्त कर सकते हैं, बिना डॉक्यूमेंटेशन या ऑनलाइन फोरम्स पर खोज किए।

Copilot Chat सिंटैक्स हाइलाइटिंग, इंडेंटेशन और अन्य फॉर्मेटिंग फीचर्स का उपयोग करके जवाब को स्पष्ट बनाने में मदद कर सकता है। उपयोगकर्ता के प्रश्न के प्रकार के आधार पर, परिणाम में वह संदर्भ शामिल हो सकता है जिसे Copilot ने उत्तर जनरेट करने के लिए उपयोग किया, जैसे कि सोर्स कोड फाइलें या डॉक्यूमेंटेशन, या VS Code की कार्यक्षमता तक पहुंचने के लिए बटन।

- Copilot Chat आपके डेवलपर फ्लो में एकीकृत होता है और आपको वहीं सहायता देता है जहाँ इसकी आवश्यकता होती है:

- संपादक या टर्मिनल से सीधे इनलाइन चैट वार्तालाप शुरू करें ताकि कोडिंग के दौरान मदद मिल सके

- चैट व्यू का उपयोग करें ताकि आपके पास हमेशा एक AI असिस्टेंट उपलब्ध हो

- क्विक चैट लॉन्च करें, एक त्वरित प्रश्न पूछें और अपने काम में वापस लौटें

GitHub Copilot Chat का उपयोग विभिन्न परिदृश्यों में किया जा सकता है, जैसे:

- समस्या को हल करने के सर्वोत्तम तरीके पर कोडिंग प्रश्नों का उत्तर देना

- किसी और के कोड को समझाना और सुधार सुझाना

- कोड फिक्स का प्रस्ताव देना

- यूनिट टेस्ट केस जनरेट करना

- कोड डॉक्यूमेंटेशन जनरेट करना

इस लिंक को पढ़ने की सलाह दी जाती है [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat में **@workspace** का संदर्भ देकर आप अपने पूरे कोडबेस के बारे में प्रश्न पूछ सकते हैं। प्रश्न के आधार पर, Copilot प्रासंगिक फाइलें और प्रतीकात्मक तत्वों को बुद्धिमानी से पुनः प्राप्त करता है, जिन्हें वह अपने उत्तर में लिंक और कोड उदाहरण के रूप में संदर्भित करता है।

आपके प्रश्न का उत्तर देने के लिए, **@workspace** उन्हीं स्रोतों के माध्यम से खोज करता है जिनका उपयोग एक डेवलपर VS Code में कोडबेस नेविगेट करते समय करता है:

- वर्कस्पेस में सभी फाइलें, सिवाय उन फाइलों के जिन्हें .gitignore फाइल द्वारा नजरअंदाज किया गया है

- डायरेक्टरी संरचना जिसमें नेस्टेड फोल्डर और फाइल नाम शामिल हैं

- GitHub का कोड सर्च इंडेक्स, यदि वर्कस्पेस एक GitHub रिपॉजिटरी है और कोड सर्च द्वारा इंडेक्स किया गया है

- वर्कस्पेस में प्रतीक और परिभाषाएँ

- सक्रिय संपादक में चयनित टेक्स्ट या दिखाई देने वाला टेक्स्ट

नोट: यदि आपने एक फाइल खोली है या एक नजरअंदाज की गई फाइल के भीतर टेक्स्ट का चयन किया है, तो .gitignore को बायपास किया जाता है।

इस लिंक को पढ़ने की सलाह दी जाती है [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **इस लैब के बारे में अधिक जानकारी**

GitHub Copilot ने एंटरप्राइज की प्रोग्रामिंग दक्षता में काफी सुधार किया है, और हर एंटरप्राइज GitHub Copilot के संबंधित कार्यों को कस्टमाइज़ करना चाहता है। कई एंटरप्राइज ने अपने बिजनेस परिदृश्यों और ओपन सोर्स मॉडल के आधार पर GitHub Copilot जैसे एक्सटेंशन को कस्टमाइज़ किया है। एंटरप्राइज के लिए, कस्टमाइज़ किए गए एक्सटेंशन को नियंत्रित करना आसान होता है, लेकिन यह उपयोगकर्ता अनुभव को प्रभावित करता है। आखिरकार, GitHub Copilot सामान्य परिदृश्यों और पेशेवरता से निपटने में अधिक मजबूत है। यदि अनुभव को सुसंगत रखा जा सके, तो एंटरप्राइज के अपने एक्सटेंशन को कस्टमाइज़ करना बेहतर होगा। GitHub Copilot Chat एंटरप्राइज को चैट अनुभव में विस्तार के लिए संबंधित API प्रदान करता है। सुसंगत अनुभव बनाए रखना और कस्टमाइज़ किए गए कार्य रखना एक बेहतर उपयोगकर्ता अनुभव है।

यह लैब मुख्य रूप से Phi-3 मॉडल का उपयोग करके स्थानीय NPU और Azure हाइब्रिड के साथ GitHub Copilot Chat में एक कस्टम एजेंट ***@PHI3*** बनाने के लिए है, जो एंटरप्राइज डेवलपर्स को कोड जनरेशन***(@PHI3 /gen)*** और इमेज आधारित कोड जनरेट करने में मदद करता है ***(@PHI3 /img)***।

![PHI3](../../../../../../../translated_images/cover.410a18b85555fad4ca8bfb8f0b1776a96ae7f8eae1132b8f0c09d4b92b8e3365.hi.png)

### ***नोट:*** 

यह लैब वर्तमान में Intel CPU और Apple Silicon के AIPC में लागू किया गया है। हम Qualcomm संस्करण के NPU को अपडेट करना जारी रखेंगे।

## **लैब**

| नाम | विवरण | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - इंस्टॉलेशन(✅) | संबंधित पर्यावरण और इंस्टॉलेशन टूल्स को कॉन्फ़िगर और इंस्टॉल करें | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini के साथ Prompt flow चलाएं (✅) | AIPC / Apple Silicon के साथ मिलकर, Phi-3-mini के माध्यम से स्थानीय NPU का उपयोग करके कोड जनरेशन बनाएं | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning Service पर Phi-3-vision को तैनात करें (✅) | Azure Machine Learning Service के Model Catalog - Phi-3-vision इमेज को तैनात करके कोड जनरेट करें | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat में @phi-3 एजेंट बनाएं (✅)  | GitHub Copilot Chat में एक कस्टम Phi-3 एजेंट बनाएं ताकि कोड जनरेशन, ग्राफ जनरेशन कोड, RAG आदि पूरा किया जा सके | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| सैंपल कोड (✅)  | सैंपल कोड डाउनलोड करें | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **संसाधन**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot के बारे में अधिक जानें [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat के बारे में अधिक जानें [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API के बारे में अधिक जानें [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Foundry के बारे में अधिक जानें [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI Foundry के Model Catalog के बारे में अधिक जानें [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की अनुशंसा की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।