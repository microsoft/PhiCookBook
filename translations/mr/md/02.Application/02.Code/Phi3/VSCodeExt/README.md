<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:36:50+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "mr"
}
-->
# **Microsoft Phi-3 कुटुंबासह आपला स्वतःचा Visual Studio Code GitHub Copilot Chat तयार करा**

GitHub Copilot Chat मध्ये workspace agent वापरला आहे का? आपली स्वतःची टीमची कोड एजंट तयार करू इच्छिता का? हा हँड्स-ऑन लॅब ओपन सोर्स मॉडेल वापरून एंटरप्राइझ-स्तरीय कोड बिझनेस एजंट तयार करण्याचा प्रयत्न करतो.

## **मूलतत्त्वे**

### **Microsoft Phi-3 का निवडावे**

Phi-3 ही एक कुटुंब मालिका आहे, ज्यात phi-3-mini, phi-3-small, आणि phi-3-medium यांचा समावेश आहे, जे वेगवेगळ्या प्रशिक्षण पॅरामीटर्सवर आधारित आहेत जसे की टेक्स्ट जनरेशन, संवाद पूर्ण करणे, आणि कोड जनरेशन. तसेच Vision आधारित phi-3-vision देखील आहे. हे एंटरप्राइझ किंवा वेगवेगळ्या टीमसाठी ऑफलाइन जनरेटिव्ह AI सोल्यूशन्स तयार करण्यासाठी योग्य आहे.

हे लिंक वाचण्याची शिफारस केली आहे [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat एक्सटेंशन तुम्हाला एक चॅट इंटरफेस देते ज्याद्वारे तुम्ही GitHub Copilot शी संवाद साधू शकता आणि VS Code मध्ये थेट कोडिंगशी संबंधित प्रश्नांची उत्तरे मिळवू शकता, ज्यासाठी तुम्हाला डॉक्युमेंटेशनमध्ये शोध घ्यावा किंवा ऑनलाइन फोरम्समध्ये जाण्याची गरज नाही.

Copilot Chat कदाचित सिंटॅक्स हायलाइटिंग, इंडेंटेशन, आणि इतर फॉरमॅटिंग वैशिष्ट्ये वापरून तयार केलेल्या उत्तराला अधिक स्पष्टता देऊ शकते. वापरकर्त्याच्या प्रश्नाच्या प्रकारानुसार, उत्तरात Copilot ने वापरलेल्या संदर्भांसाठी लिंक, जसे की सोर्स कोड फाइल्स किंवा डॉक्युमेंटेशन, किंवा VS Code फंक्शनॅलिटीसाठी बटणे असू शकतात.

- Copilot Chat तुमच्या डेव्हलपर फ्लोमध्ये समाकलित होतो आणि जिथे गरज आहे तिथे मदत करतो:

- कोडिंग करताना मदतीसाठी एडिटर किंवा टर्मिनलमधून थेट इनलाइन चॅट संभाषण सुरू करा

- Chat व्ह्यू वापरून कधीही AI सहाय्यक बाजूला ठेवा

- क्विक चॅट सुरू करा, जलद प्रश्न विचारा आणि पुन्हा तुमच्या कामात लागा

GitHub Copilot Chat विविध परिस्थितींमध्ये वापरू शकता, जसे की:

- एखाद्या समस्येचे सर्वोत्तम निराकरण कसे करावे याबाबत कोडिंग प्रश्नांची उत्तरे देणे

- दुसऱ्याच्या कोडचे स्पष्टीकरण देणे आणि सुधारणा सुचवणे

- कोड फिक्सेस सुचवणे

- युनिट टेस्ट केस तयार करणे

- कोड डॉक्युमेंटेशन तयार करणे

हे लिंक वाचण्याची शिफारस केली आहे [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat मध्ये **@workspace** चा संदर्भ देऊन तुम्ही तुमच्या संपूर्ण कोडबेसबद्दल प्रश्न विचारू शकता. प्रश्नानुसार, Copilot बुद्धिमत्तेने संबंधित फाइल्स आणि चिन्हे शोधून त्याचा संदर्भ उत्तरात लिंक आणि कोड उदाहरणे म्हणून देतो.

तुमच्या प्रश्नाचे उत्तर देण्यासाठी, **@workspace** VS Code मध्ये कोडबेसमध्ये नेव्हिगेट करताना डेव्हलपर वापरतो त्या स्रोतांमधून शोध घेतो:

- वर्कस्पेसमधील सर्व फाइल्स, .gitignore फाइलने वगळलेल्या फाइल्स वगळता

- डायरेक्टरी स्ट्रक्चरसह नेस्टेड फोल्डर आणि फाइल नावे

- GitHub चा कोड सर्च इंडेक्स, जर वर्कस्पेस GitHub रिपॉझिटरी असेल आणि कोड सर्चने इंडेक्स केलेले असेल तर

- वर्कस्पेसमधील चिन्हे आणि व्याख्या

- सध्या निवडलेला टेक्स्ट किंवा सक्रिय एडिटरमधील दृश्यमान टेक्स्ट

टीप: .gitignore वगळलेली फाइल उघडल्यास किंवा त्यातील टेक्स्ट निवडल्यास तो बायपास होतो.

हे लिंक वाचण्याची शिफारस केली आहे [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **या लॅबबद्दल अधिक जाणून घ्या**

GitHub Copilot ने एंटरप्राइझच्या प्रोग्रामिंग कार्यक्षमतेत मोठा सुधारणा केली आहे, आणि प्रत्येक एंटरप्राइझ GitHub Copilot च्या संबंधित फंक्शन्स सानुकूलित करण्याची अपेक्षा ठेवते. अनेक एंटरप्राइझनी त्यांच्या स्वतःच्या बिझनेस सीनारिओ आणि ओपन सोर्स मॉडेल्सवर आधारित GitHub Copilot सारखे सानुकूल एक्सटेंशन्स तयार केले आहेत. एंटरप्राइझसाठी, सानुकूल एक्सटेंशन्स नियंत्रित करणे सोपे असते, पण यामुळे वापरकर्ता अनुभवावर परिणाम होतो. शेवटी, GitHub Copilot सामान्य सीनारिओ आणि व्यावसायिकतेसाठी अधिक मजबूत फंक्शन्स देते. जर अनुभव सुसंगत ठेवता आला, तर एंटरप्राइझची स्वतःची एक्सटेंशन सानुकूलित करणे अधिक चांगले ठरेल. GitHub Copilot Chat एंटरप्राइझसाठी चॅट अनुभव वाढवण्यासाठी संबंधित API प्रदान करतो. सुसंगत अनुभव राखणे आणि सानुकूल फंक्शन्स असणे हा चांगला वापरकर्ता अनुभव आहे.

ही लॅब मुख्यतः Phi-3 मॉडेल वापरून स्थानिक NPU आणि Azure हायब्रिडसह GitHub Copilot Chat मध्ये सानुकूल एजंट ***@PHI3*** तयार करते, जे एंटरप्राइझ डेव्हलपर्सना कोड जनरेशन पूर्ण करण्यात मदत करते ***(@PHI3 /gen)*** आणि प्रतिमांवर आधारित कोड तयार करते ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/mr/cover.1017ebc9a7c46d09.png)

### ***टीप:***

ही लॅब सध्या Intel CPU आणि Apple Silicon च्या AIPC मध्ये राबवली जात आहे. आम्ही Qualcomm NPU चा आवृत्ती देखील अद्ययावत करत राहू.

## **लॅब**

| नाव | वर्णन | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | संबंधित वातावरण आणि इंस्टॉलेशन टूल्स कॉन्फिगर आणि इन्स्टॉल करा | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | AIPC / Apple Silicon सह स्थानिक NPU वापरून Phi-3-mini द्वारे कोड जनरेशन तयार करा | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Azure Machine Learning Service च्या Model Catalog - Phi-3-vision इमेज तैनात करून कोड जनरेट करा | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | GitHub Copilot Chat मध्ये सानुकूल Phi-3 एजंट तयार करा जे कोड जनरेशन, ग्राफ जनरेशन कोड, RAG इत्यादी पूर्ण करेल | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | सॅम्पल कोड डाउनलोड करा | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **संसाधने**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot बद्दल अधिक जाणून घ्या [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat बद्दल अधिक जाणून घ्या [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API बद्दल अधिक जाणून घ्या [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Foundry बद्दल अधिक जाणून घ्या [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI Foundry च्या Model Catalog बद्दल अधिक जाणून घ्या [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.