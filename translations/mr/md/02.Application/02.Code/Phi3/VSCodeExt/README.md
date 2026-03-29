# **तुमचा स्वतःचा Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 कुटुंबासह तयार करा**

तुम्ही GitHub Copilot Chat मध्ये वर्कस्पेस एजंट वापरला आहे का? तुम्हाला तुमच्या टीमचा स्वतःचा कोड एजंट तयार करायचा आहे का? हा हँड्स-ऑन लॅब एंटरप्राइझ-स्तरीय कोड व्यवसाय एजंट तयार करण्यासाठी ओपन सोर्स मॉडेल एकत्र करायचा आहे.

## **पायाभूत**

### **मायक्रोसॉफ्ट Phi-3 का निवडावे**

Phi-3 हा एक कुटुंब मालिका आहे, ज्यात phi-3-mini, phi-3-small, आणि phi-3-medium यांचा समावेश आहे जे वेगवेगळ्या प्रशिक्षण पॅरामीटर्सवर आधारित आहेत, जसे की टेक्स्ट जनरेशन, संवाद पूर्ण करणे, आणि कोड जनरेशन. तसेच Vision आधारित phi-3-vision ही आहे. हे एंटरप्राइझ किंवा विविध टीमसाठी ऑफलाइन जनरेटिव्ह AI सोल्यूशन्स तयार करण्यासाठी योग्य आहे.

हे दुवा वाचण्याची शिफारस केली जाते [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **मायक्रोसॉफ्ट GitHub Copilot Chat**

GitHub Copilot Chat विस्तार तुम्हाला एक चैट इंटरफेस देते ज्याद्वारे तुम्ही GitHub Copilot सोबत संवाद साधू शकता आणि VS Code मधून थेट कोडिंग संबंधित प्रश्नांची उत्तरे मिळवू शकता, ज्यासाठी तुम्हाला डोक्युमेंटेशनमध्ये फिरावे किंवा ऑनलाइन फोरममध्ये शोध घ्यावा लागत नाही.

Copilot Chat जनरेट झालेल्या प्रतिसादाला स्पष्टता देण्यासाठी सिंटॅक्स हायलाईटिंग, इंडेंटेशन, आणि इतर फॉरमॅटिंग वैशिष्ट्यांचा वापर करू शकतो. वापरकर्त्याच्या प्रश्नाच्या प्रकारावर अवलंबून, निकालात Copilot ने प्रतिसाद तयार करण्यासाठी वापरलेले संदर्भ जसे की सोर्स कोड फाइल्स किंवा डोक्युमेंटेशनची लिंक किंवा VS Code वैशिष्ट्ये वापरण्याचे बटणे असू शकतात.

- Copilot Chat तुमच्या विकासक प्रवाहामध्ये जोडलेला असून तुम्हाला आवश्यक तेथे मदत देते:

- कोडिंग करताना मदतीसाठी एडिटर किंवा टर्मिनलमधून थेट इनलाइन चैट संभाषण सुरू करा

- कोणत्याही वेळी मदत घेण्यासाठी Chat व्ह्यूमध्ये AI सहाय्यक वापरा

- जलद प्रश्न विचारण्यासाठी Quick Chat सुरू करा आणि लगेचच तुमच्या कामात परत जा

GitHub Copilot Chat तुम्ही विविध परिस्थितींमध्ये वापरू शकता, जसे:

- समस्येचे सर्वोत्तम निराकरण कसे करावे याच्या संदर्भातील कोडिंग प्रश्नांची उत्तरे देणे

- दुसऱ्याच्या कोडचे स्पष्टीकरण देणे आणि सुधारणा सुचवणे

- कोड फिक्सेस सुचवणे

- युनिट टेस्ट केसेस तयार करणे

- कोड डोक्युमेंटेशन तयार करणे

हे दुवा वाचण्याची शिफारस केली जाते [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **मायक्रोसॉफ्ट GitHub Copilot Chat @workspace**

Copilot Chat मधील **@workspace** चा संदर्भ तुम्हाला तुमच्या संपूर्ण कोडबेससंदर्भातील प्रश्न विचारण्याची परवानगी देतो. प्रश्नावर आधारित, Copilot संबंधित फायली आणि चिन्हे बुद्धिमत्तेने शोधून त्याचा संदर्भ प्रतिसादात दुवे आणि कोड उदाहरणे म्हणून देतो.

तुमच्या प्रश्नाचे उत्तर देण्यासाठी, **@workspace** हे VS Code मध्ये कोडबेस नेव्हिगेट करण्यात वापरल्या जाणाऱ्या स्त्रोतांमधून शोध घेतो:

- वर्कस्पेसमधील सर्व फायली, .gitignore फाइलने दुर्लक्षित फाइलांशिवाय

- डायरेक्टरीची रचना ज्यात नेस्टेड फोल्डर आणि फाइल नावे असतात

- GitHub चा कोड शोध निर्देशांक, जर वर्कस्पेस GitHub रिपॉझिटरी असेल आणि कोड शोधाद्वारे निर्देशांकित असेल तर

- वर्कस्पेसमधील चिन्हे आणि व्याख्याने

- सध्याचे निवडलेले मजकूर किंवा अॅक्टिव्ह एडिटरमधील दृश्यमान मजकूर

टीप: .gitignore फायलीने दुर्लक्षित केलेल्या फाइलमध्ये जर तुम्ही फाइल उघडी असेल किंवा मजकूर निवडला असेल तर .gitignore पार करा.

हे दुवा वाचण्याची शिफारस केली जाते [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **या लॅबविषयी अधिक माहिती**

GitHub Copilot ने एंटरप्राइझच्या प्रोग्रामिंग कार्यक्षमतेत मोठी सुधारणा केली आहे, आणि प्रत्येक एंटरप्राइझ GitHub Copilot चे संबंधित कार्ये सानुकूलित करण्याची आशा ठेवते. अनेक एंटरप्राइझ त्यांच्या स्वतःच्या व्यवसायाच्या परिस्थितीनुसार आणि ओपन सोर्स मॉडेल्सवर आधारित GitHub Copilot सारखे कस्टमाइज्ड एक्सटेंशन्स तयार करत आहेत. एंटरप्राइझसाठी कस्टमाइज्ड एक्सटेंशन्स नियंत्रित करणे सोपे असते, परंतु हे वापरकर्ता अनुभवावर परिणाम करु शकते. शेवटी, GitHub Copilot सामान्य परिस्थिती आणि व्यावसायिकतेशी निगडित कार्यांमध्ये अधिक मजबूत आहे. जर अनुभव सुसंगत ठेवता आला, तर एंटरप्राइझच्या स्वतःच्या एक्सटेंशनचे सानुकूलन करणे अधिक चांगले ठरते. GitHub Copilot Chat एंटरप्राइझसाठी चैट अनुभव विस्तारण्यासाठी संबंधित API पुरवतो. सुसंगत अनुभव राखणे आणि सानुकूलित कार्ये असणे हे एक चांगला वापरकर्ता अनुभव आहे.

हा लॅब मुख्यतः Phi-3 मॉडेल वापरून स्थानिक NPU आणि Azure हायब्रिडसहित GitHub Copilot Chat मध्ये कस्टम एजंट ***@PHI3*** तयार करतो, जो एंटरप्राइझ विकासकांना कोड जनरेशन पूर्ण करण्यात ***(@PHI3 /gen)*** आणि प्रतिमा आधारित कोड जनरेशन करण्यास ***(@PHI3 /img)*** मदत करतो.

![PHI3](../../../../../../../translated_images/mr/cover.1017ebc9a7c46d09.webp)

### ***टीप:*** 

हा लॅब सध्या Intel CPU आणि Apple Silicon च्या AIPC मध्ये अमलात आणला आहे. आम्ही Qualcomm चा NPU आवृत्ती अद्ययावत करत राहू.


## **लॅब**


| नाव | वर्णन | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - इंस्टॉलेशन्स(✅) | संबंधित पर्यावरणे आणि इंस्टॉलेशन टूल्स कॉन्फिगर आणि इन्स्टॉल करा | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini सह प्रॉम्प्ट फ्लो चालवा (✅) | AIPC / Apple Silicon सह संयोजन करून, स्थानिक NPU वापरून Phi-3-mini द्वारे कोड जनरेशन तयार करा | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning Service वर Phi-3-vision तैनात करा(✅) | Azure Machine Learning Service च्या मॉडेल कॅटलॉग - Phi-3-vision इमेज तैनात करून कोड जनरेट करा | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat मध्ये @phi-3 एजंट तयार करा(✅)  | GitHub Copilot Chat मध्ये सानुकूल Phi-3 एजंट तयार करा जे कोड जनरेशन, ग्राफ जनरेशन कोड, RAG इत्यादी पूर्ण करेल | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | नमुना कोड डाउनलोड करा | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **संसाधने**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot बद्दल अधिक जाणून घ्या [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat बद्दल अधिक जाणून घ्या [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API बद्दल अधिक जाणून घ्या [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry बद्दल अधिक जाणून घ्या [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry च्या मॉडेल कॅटलॉग बद्दल अधिक जाणून घ्या [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्न करत असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अयोग्यतेचा समावेश असू शकतो. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती साठी व्यावसायिक मानवी अनुवाद शिफारस केली जाते. या अनुवादाचा वापर करून झालेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->