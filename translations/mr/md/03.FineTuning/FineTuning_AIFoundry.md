# Microsoft Foundry सह Phi-3 चे फाइन-ट्यूनिंग

चला Microsoft Foundry वापरून Microsoft च्या Phi-3 Mini भाषा मॉडेलचे फाइन-ट्यूनिंग कसे करायचे ते पाहूया. फाइन-ट्यूनिंगमुळे तुम्ही Phi-3 Mini ला विशिष्ट कामांसाठी सानुकूलित करू शकता, ज्यामुळे ते अधिक सामर्थ्यवान आणि संदर्भासह सज्ज होते.

## विचार करण्याचे मुद्दे

- **क्षमता:** कोणते मॉडेल्स फाइन ट्यून करू शकतात? बेस मॉडेल फाइन ट्यून करून काय करता येऊ शकते?
- **खर्च:** फाइन ट्यूनिंगसाठी किंमत मॉडेल काय आहे?
- **सानुकूलता:** बेस मॉडेल कितपत सुधारता येऊ शकते – आणि कोणत्या प्रकारे?
- **सुविधा:** फाइन ट्यूनिंग प्रत्यक्ष कशी होते – मला सानुकूल कोड लिहावा लागेल का? मला माझा स्वतःचा कम्युट आणावा लागेल का?
- **सुरक्षितता:** फाइन ट्यून केलेल्या मॉडेल्सना सुरक्षिततेच्या जोखमी असल्याचे ज्ञात आहे – अनपेक्षित नुकसान टाळण्यासाठी कोणतेही सुरक्षा उपाय आहेत का?

![AIFoundry Models](../../../../translated_images/mr/AIFoundryModels.0e1b16f7d0b09b73.webp)

## फाइन-ट्यूनिंगसाठी तयारी

### पूर्वअटी

> [!NOTE]
> Phi-3 कौटुंबिक मॉडेल्ससाठी, Pay-as-you-go फाइन-ट्यूनिंग सेवा **East US 2** क्षेत्रांमध्ये तयार केलेल्या हब्ससाठीच उपलब्ध आहे.

- Azure सदस्यता. तुमच्याकडे Azure सदस्यता नसेल तर, सुरू करण्यासाठी [पेड Azure खाते](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) तयार करा.

- एक [AI Foundry प्रोजेक्ट](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Microsoft Foundry मधील ऑपरेशन्ससाठी प्रवेश देण्यासाठी Azure भूमिका-आधारित प्रवेश नियंत्रण (Azure RBAC) वापरले जातात. या लेखातील टप्पे पूर्ण करण्यासाठी तुमच्या वापरकर्त्याला संसाधन गटावर __Azure AI Developer भूमिका__ असणे आवश्यक आहे.

### सदस्यता प्रदाता नोंदणी

सदस्यता `Microsoft.Network` रिसोर्स प्रोव्हायडरसाठी नोंदणीकृत आहे का ते तपासा.

1. [Azure पोर्टल](https://portal.azure.com) मध्ये साइन इन करा.
1. डाव्या मेनूमधून **Subscriptions** निवडा.
1. तुम्ही वापरायची सदस्यता निवडा.
1. डाव्या मेनूमधून **AI project settings** > **Resource providers** निवडा.
1. **Microsoft.Network** रिसोर्स प्रोव्हायडर्स सूचीमध्ये आहे का ते पुष्टी करा. नसेल तर त्याला जोडा.

### डेटा तयारी

तुमच्या मॉडेलचे फाइन-ट्यूनिंग करण्यासाठी प्रशिक्षण आणि पडताळणी डेटा तयार करा. तुमच्या प्रशिक्षण व पडताळणी डेटासेट्समध्ये मॉडेल कसे काम करावे याचे इनपुट व आउटपुट उदाहरणे असावीत.

तुमची सर्व प्रशिक्षण उदाहरणे अपेक्षित फॉरमॅटमध्ये आहेत याची खात्री करा. मॉडेल फाइन-ट्यून करणे प्रभावी करण्यासाठी डेटासेट संतुलित आणि विविध असावे.

यामध्ये डेटा संतुलन राखणे, विविध परिस्थितींचा समावेश करणे, व प्रशिक्षण डेटाला वेळ-वेळी सुधारून वास्तविक जगातील अपेक्षांशी जुळविणे यांचा समावेश आहे, ज्यामुळे अधिक अचूक व संतुलित मॉडेल प्रतिसाद मिळतात.

विविध मॉडेल प्रकारांसाठी प्रशिक्षण डेटाचा वेगळा फॉरमॅट आवश्यक असतो.

### चैट पूर्णता

तुम्ही वापरणारा प्रशिक्षण व पडताळणी डेटा **JSON Lines (JSONL)** दस्तऐवज स्वरूपात असणे **आवश्यक** आहे. `Phi-3-mini-128k-instruct` साठी फाइन-ट्यूनिंग डेटा कॉन्व्हर्सेशनल स्वरूपात असला पाहिजे जो Chat completions API द्वारा वापरला जातो.

### उदाहरण फाइल फॉरमॅट

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

समर्थित फाइल प्रकार JSON Lines आहे. फाइल्स डीफॉल्ट डेटास्टोअरमध्ये अपलोड केल्या जातात आणि तुमच्या प्रोजेक्टमध्ये उपलब्ध होतात.

## Microsoft Foundry सह Phi-3 चे फाइन-ट्यूनिंग

Microsoft Foundry तुम्हाला फाइन-ट्यूनिंग नावाच्या प्रक्रियेद्वारे मोठ्या भाषा मॉडेल्सला तुमच्या वैयक्तिक डेटासेटसाठी सानुकूल करण्याची परवानगी देते. फाइन-ट्यूनिंग विशिष्ट कामांसाठी व अनुप्रयोगांसाठी सानुकूलता व ऑप्टिमायझेशन सक्षम करून मोठी मूल्ये प्रदान करते. त्यामुळे कार्यक्षमता सुधारते, खर्च कमी होतो, विलंब कमी होतो, व अनुरूप आउटपुट मिळतात.

![Finetune AI Foundry](../../../../translated_images/mr/AIFoundryfinetune.193aaddce48d553c.webp)

### नवीन प्रोजेक्ट तयार करा

1. [Microsoft Foundry](https://ai.azure.com) मध्ये साइन इन करा.

1. नवीन प्रोजेक्ट तयार करण्यासाठी **+New project** निवडा.

    ![FineTuneSelect](../../../../translated_images/mr/select-new-project.cd31c0404088d7a3.webp)

1. खालील टप्पे पूर्ण करा:

    - प्रोजेक्ट **Hub नांव** द्या. हे एक वैशिष्ट्यपूर्ण मूल्य असले पाहिजे.
    - वापरण्यासाठी **Hub** निवडा (आवश्यक असल्यास नवीन तयार करा).

    ![FineTuneSelect](../../../../translated_images/mr/create-project.ca3b71298b90e420.webp)

1. नवीन हब तयार करण्यासाठी खालील टप्पे पूर्ण करा:

    - **Hub नांव** टाका. त्याला वैशिष्ट्यपूर्ण असणे आवश्यक आहे.
    - तुमची Azure **Subscription** निवडा.
    - वापरण्यासाठी **Resource group** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - तुम्हाला पाहिजे त्या **Location** ची निवड करा.
    - वापरण्यासाठी **Connect Azure AI Services** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - **Connect Azure AI Search** साठी **Skip connecting** निवडा.

    ![FineTuneSelect](../../../../translated_images/mr/create-hub.49e53d235e80779e.webp)

1. **Next** निवडा.
1. **Create a project** निवडा.

### डेटा तयारी

फाइन-ट्यूनिंगपूर्वी, तुमच्या कामाशी संबंधित डेटासेट गोळा करा किंवा तयार करा, जसे की चॅट सुचना, प्रश्न-उत्तर जोड्या, किंवा इतर संबंधित मजकूर डेटा. या डेटाला स्वच्छ करा आणि पूर्वप्रक्रिया करा, जसे ध्वनी काढून टाकणे, हरवलेल्या मूल्यांची हाताळणी, आणि मजकूर टोकनाइज करणे.

### Microsoft Foundry मध्ये Phi-3 मॉडेल्स फाइन-ट्यून करा

> [!NOTE]
> Phi-3 मॉडेल्सचे फाइन-ट्यूनिंग सध्या East US 2 मध्ये असलेल्या प्रोजेक्टसाठी समर्थित आहे.

1. डाव्या बाजूच्या टॅबमधून **Model catalog** निवडा.

1. **search bar** मध्ये *phi-3* टाइप करा आणि वापरायचे phi-3 मॉडेल निवडा.

    ![FineTuneSelect](../../../../translated_images/mr/select-model.60ef2d4a6a3cec57.webp)

1. **Fine-tune** निवडा.

    ![FineTuneSelect](../../../../translated_images/mr/select-finetune.a976213b543dd9d8.webp)

1. **Fine-tuned model name** टाका.

    ![FineTuneSelect](../../../../translated_images/mr/finetune1.c2b39463f0d34148.webp)

1. **Next** निवडा.

1. खालील टप्पे पार पाडा:

    - **task type** म्हणून **Chat completion** निवडा.
    - वापरण्यासाठी **Training data** निवडा. तुम्ही Microsoft Foundry च्या डेटामुळे किंवा स्थानिक वातावरणातून अपलोड करू शकता.

    ![FineTuneSelect](../../../../translated_images/mr/finetune2.43cb099b1a94442d.webp)

1. **Next** निवडा.

1. वापरण्यासाठी **Validation data** अपलोड करा किंवा **Automatic split of training data** निवडा.

    ![FineTuneSelect](../../../../translated_images/mr/finetune3.fd96121b67dcdd92.webp)

1. **Next** निवडा.

1. खालील टप्पे पार पाडा:

    - वापरण्यासाठी **Batch size multiplier** निवडा.
    - वापरण्यासाठी **Learning rate** निवडा.
    - वापरण्यासाठी **Epochs** निवडा.

    ![FineTuneSelect](../../../../translated_images/mr/finetune4.e18b80ffccb5834a.webp)

1. फाइन-ट्यूनिंग प्रक्रिया सुरू करण्यासाठी **Submit** निवडा.

    ![FineTuneSelect](../../../../translated_images/mr/select-submit.0a3802d581bac271.webp)

1. तुमचे मॉडेल फाइन-ट्यून झाले की स्थिती **Completed** अशी दिसेल, खालील चित्रात दाखवल्याप्रमाणे. आता तुम्ही मॉडेल डिप्लॉय करू शकता आणि ते तुमच्या अनुप्रयोगात, प्लेग्राउंड मध्ये किंवा प्रॉम्प्ट फ्लोमध्ये वापरू शकता. अधिक माहितीसाठी पहा [Microsoft Foundry सह Phi-3 कुटुंबातील लहान भाषा मॉडेल्स कसे डिप्लॉय करायचे](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/mr/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Phi-3 चे फाइन-ट्यूनिंगबद्दल अधिक तपशीलवार माहितीकरिता कृपया भेट द्या [Microsoft Foundry मध्ये Phi-3 मॉडेल्स फाइन-ट्यून करा](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## तुमच्या फाइन-ट्यून केलेल्या मॉडेल्सचे साफसफाई करणे

तुम्ही [Microsoft Foundry](https://ai.azure.com) मधील फाइन-ट्यूनिंग मॉडेल यादीतून किंवा मॉडेल तपशील पृष्ठावरून फाइन-ट्यून केलेला मॉडेल हटवू शकता. फाइन-ट्यून पृष्ठातून हटवायचा मॉडेल निवडा, नंतर Delete बटण दाबुन तो हटवा.

> [!NOTE]
> जर तुमच्या कस्टम मॉडेलला आधीपासून डिप्लॉयमेंट असेल तर तुम्ही ते मॉडेल हटवू शकत नाही. आधी तुमची मॉडेल डिप्लॉयमेंट हटवावी लागेल, त्यानंतरच कस्टम मॉडेल हटविता येईल.

## खर्च आणि कोटा

### सेवा म्हणून फाइन-ट्यून केलेल्या Phi-3 मॉडेल्ससाठी खर्च आणि कोटा विचारणा

Phi मॉडेल्स जे सेवा म्हणून फाइन-ट्यून केलेले आहेत ते Microsoft कडून प्रदान केले जातात व Microsoft Foundry मध्ये समाकलित असतात. तुम्ही [डिप्लॉय](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) किंवा फाइन-ट्यून करताना किंमती पाहू शकता, त्यासाठी डिप्लॉयमेंट विजार्डमधील Pricing and terms टॅब पहा.

## कंटेंट फिल्टरिंग

सेवा म्हणून pay-as-you-go मॉडेल्सना Azure AI Content Safety द्वारे संरक्षित केले जाते. वास्तविक वेळेच्या एन्डपॉइंट्सवर डिप्लॉय केल्यावर तुम्ही या सुविधेतून बाहेर पडू शकता. Azure AI content safety सक्षम केल्याने, प्रॉम्प्ट व पूर्णता एकत्रित वर्गीकरण मॉडेल्सच्या अनुक्रमावरून जातात ज्यांचा उद्देश हानिकारक सामग्रीचा शोध घेणे आणि प्रतिबंध करणे आहे. कंटेंट फिल्टरिंग सिस्टम विशिष्ट प्रकारच्या संभाव्य हानिकारक सामग्रीवर लक्ष ठेवते व इनपुट प्रॉम्प्ट्स व आउटपुट पूर्णतांमध्ये कारवाई करते. अधिक जाणून घ्या [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**फाइन-ट्यूनिंग संरचना**

हायपरपॅरामिटर्स: शिक्षण दर, बॅच साईज, आणि प्रशिक्षण इपॉक्सची संख्या यांसारखे हायपरपॅरामिटर्स निश्चित करा.

**लॉस फंक्शन**

तुमच्या कामासाठी योग्य लॉस फंक्शन निवडा (उदा., क्रॉस-एंट्रॉपी).

**ऑप्टिमायझर**

प्रशिक्षणादरम्यान ग्रेडियंट अद्यतनांसाठी ऑप्टिमायझर निवडा (उदा., Adam).

**फाइन-ट्यूनिंग प्रक्रिया**

- प्री-ट्रेन्ड मॉडेल लोड करा: Phi-3 Mini चेकपॉइंट लोड करा.
- कस्टम लेयर्स जोडा: कामासpecific लेयर्स जोडा (उदा., चॅट सूचनांसाठी वर्गीकरण हेड).

**मॉडेल ट्रेन करा**
तयार केलेल्या डेटासेटसह मॉडेल फाइन-ट्यून करा. प्रशिक्षण प्रगतीवर लक्ष ठेवा व हायपरपॅरामिटर्स समायोजित करा.

**मूल्यांकन आणि पडताळणी**

पडताळणी सेट: तुमचा डेटा प्रशिक्षण व पडताळणी सेटमध्ये विभाजित करा.

**कामगिरीचे मूल्यमापन**

मॉडेल कामगिरीसाठी अचूकता, F1-स्कोर, किंवा पेर्प्लेक्सिटी सारखे मेट्रिक्स वापरा.

## फाइन-ट्यून केलेले मॉडेल जतन करा

**चेकपॉइंट**
पुढील वापरासाठी फाइन-ट्यून केलेला मॉडेल चेकपॉइंट जतन करा.

## डिप्लॉयमेंट

- वेब सेवा म्हणून डिप्लॉय करा: तुमचे फाइन-ट्यून केलेले मॉडेल Microsoft Foundry मध्ये वेब सेवा म्हणून डिप्लॉय करा.
- एन्डपॉइंटची चाचणी करा: डिप्लॉय केलेल्या एन्डपॉइंटवर चाचणी क्वेरीज पाठवून त्याची कार्यक्षमता तपासा.

## पुनरावलोकन आणि सुधारणा करा

पुनरावृत्ती करा: जर कामगिरी समाधानकारक नसेल तर हायपरपॅरामिटर्स समायोजित करा, अधिक डेटा जोडा किंवा जास्त इपॉक्ससाठी फाइन-ट्यून करा.

## मॉनिटर आणि सुधारित करा

मॉडेलच्या वर्तनावर सतत लक्ष ठेवा आणि आवश्यकतेनुसार सुधारणा करा.

## सानुकूल आणि विस्तार करा

सानुकूल कामे: Phi-3 Mini चॅट सूचनांपेक्षा इतर विविध कामांसाठीही फाइन-ट्यून केला जाऊ शकतो. इतर वापर प्रकरणे शोधा!
प्रयोग करा: कामगिरी वाढविण्यासाठी विविध आर्किटेक्चर, लेयर संयोजन आणि तंत्रे वापरून पहा.

> [!NOTE]
> फाइन-ट्यूनिंग ही पुनरावृत्तीची प्रक्रिया आहे. प्रयोग करा, शिका आणि तुमच्या विशिष्ट कामासाठी सर्वोत्तम निकाल साध्य करण्यासाठी मॉडेल सानुकूल करा!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत म्हणून मानले जावे. महत्त्वाच्या माहितीकरिता, व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थाचा आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->