# Microsoft Foundry के साथ Phi-3 को फाइन-ट्यून करना

आइए देखें कि Microsoft Foundry का उपयोग करके Microsoft के Phi-3 Mini भाषा मॉडल को कैसे फाइन-ट्यून किया जाए। फाइन-ट्यूनिंग आपको Phi-3 Mini को विशिष्ट कार्यों के लिए अनुकूलित करने की अनुमति देता है, जिससे यह और भी अधिक शक्तिशाली और संदर्भ-सम्मत हो जाता है।

## विचार करने योग्य बातें

- **क्षमताएँ:** कौन से मॉडल फाइन-ट्यून करने योग्य हैं? बेस मॉडल को क्या-क्या करने के लिए फाइन-ट्यून किया जा सकता है?
- **लागत:** फाइन-ट्यूनिंग का मूल्य निर्धारण मॉडल क्या है?
- **कस्टमाइजेबिलिटी:** मैं बेस मॉडल को कितना और किन तरीकों से संशोधित कर सकता हूँ?
- **सुविधा:** फाइन-ट्यूनिंग वास्तव में कैसे होती है – क्या मुझे कस्टम कोड लिखना होगा? क्या मुझे अपनी कंप्यूटिंग लाना होगा?
- **सुरक्षा:** फाइन-ट्यून किए गए मॉडल में सुरक्षा जोखिम होते हैं – क्या दुर्घटनावश हानि से बचाने के लिए कोई गार्डराइल्स मौजूद हैं?

![AIFoundry Models](../../../../translated_images/hi/AIFoundryModels.0e1b16f7d0b09b73.webp)

## फाइन-ट्यूनिंग के लिए तैयारी

### आवश्यकताएँ

> [!NOTE]
> Phi-3 परिवार के मॉडलों के लिए, पे-एज़-यू-गो मॉडल फाइन-ट्यून ऑफ़र केवल **East US 2** क्षेत्रों में बनाए गए हब्स के साथ उपलब्ध है।

- एक Azure सब्सक्रिप्शन। यदि आपके पास Azure सब्सक्रिप्शन नहीं है, तो शुरू करने के लिए एक [पेड Azure खाता](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) बनाएं।

- एक [AI Foundry प्रोजेक्ट](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)।
- Azure रोल-आधारित एक्सेस कंट्रोल (Azure RBAC) का उपयोग Microsoft Foundry में ऑपरेशन तक पहुँच प्रदान करने के लिए किया जाता है। इस लेख में दिए गए चरणों को करने के लिए, आपके उपयोगकर्ता खाते को संसाधन समूह पर __Azure AI Developer रोल__ सौंपा जाना चाहिए।

### सब्सक्रिप्शन प्रदाता पंजीकरण

सुनिष्चित करें कि सब्सक्रिप्शन `Microsoft.Network` संसाधन प्रदाता के लिए पंजीकृत है।

1. [Azure पोर्टल](https://portal.azure.com) में साइन इन करें।
1. बाएं मेनू से **Subscriptions** चुनें।
1. उपयोग करने के लिए सब्सक्रिप्शन चुनें।
1. बाएं मेनू से **AI project settings** > **Resource providers** चुनें।
1. पुष्टि करें कि **Microsoft.Network** संसाधन प्रदाताओं की सूची में है। यदि नहीं, तो इसे जोड़ें।

### डेटा तैयारी

अपने मॉडल को फाइन-ट्यून करने के लिए प्रशिक्षण और मान्यकरण डेटा तैयार करें। आपके प्रशिक्षण डेटा और मान्यकरण डेटा सेट में इनपुट और आउटपुट उदाहरण होते हैं कि आप मॉडल से मॉडल को कैसे प्रदर्शन करना चाहते हैं।

सुनिश्चित करें कि आपके सभी प्रशिक्षण उदाहरण अपेक्षित प्रारूप में हैं। मॉडल को प्रभावी ढंग से फाइन-ट्यून करने के लिए, संतुलित और विविध डेटा सेट सुनिश्चित करें।

इसमें डेटा संतुलन बनाए रखना, विभिन्न परिदृश्यों को शामिल करना, और समय-समय पर प्रशिक्षण डेटा को वास्तविक दुनिया की अपेक्षाओं के अनुसार संशोधित करना शामिल है, जो अंततः अधिक सटीक और संतुलित मॉडल प्रतिक्रियाओं की ओर ले जाता है।

विभिन्न मॉडल प्रकार के लिए प्रशिक्षण डेटा का अलग प्रारूप आवश्यक होता है।

### चैट पूर्णता

आपका प्रशिक्षण और मान्यकरण डेटा JSON Lines (JSONL) दस्तावेज़ के रूप में तैयार होना **अनिवार्य** है। `Phi-3-mini-128k-instruct` के लिए फाइन-ट्यूनिंग डेटासेट को चैट पूर्णता API द्वारा उपयोग किए जाने वाले संवाद प्रारूप में होना चाहिए।

### उदाहरण फ़ाइल प्रारूप

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

समर्थित फ़ाइल प्रकार JSON Lines है। फाइलें डिफ़ॉल्ट डाटास्टोर में अपलोड की जाती हैं और आपके प्रोजेक्ट में उपलब्ध कराई जाती हैं।

## Microsoft Foundry के साथ Phi-3 को फाइन-ट्यून करना

Microsoft Foundry आपको बड़े भाषा मॉडलों को अपनी व्यक्तिगत डेटासेट के अनुकूल बनाने की अनुमति देता है, जिसे फाइन-ट्यूनिंग कहा जाता है। फाइन-ट्यूनिंग विशेष कार्यों और अनुप्रयोगों के लिए अनुकूलन और अनुकूलन सक्षम करके महत्वपूर्ण मूल्य प्रदान करता है। इससे प्रदर्शन में सुधार, लागत दक्षता, कम विलंबता और अनुकूलित आउटपुट होते हैं।

![Finetune AI Foundry](../../../../translated_images/hi/AIFoundryfinetune.193aaddce48d553c.webp)

### नया प्रोजेक्ट बनाएं

1. [Microsoft Foundry](https://ai.azure.com) में साइन इन करें।

1. Microsoft Foundry में नया प्रोजेक्ट बनाने के लिए **+New project** चुनें।

    ![FineTuneSelect](../../../../translated_images/hi/select-new-project.cd31c0404088d7a3.webp)

1. निम्न कार्य करें:

    - प्रोजेक्ट का **Hub name**। यह एक अद्वितीय मान होना चाहिए।
    - उपयोग के लिए **Hub** चुनें (आवश्यक होने पर नया बनाएँ)।

    ![FineTuneSelect](../../../../translated_images/hi/create-project.ca3b71298b90e420.webp)

1. नया हब बनाने के लिए निम्न कार्य करें:

    - **Hub name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
    - अपना Azure **Subscription** चुनें।
    - उपयोग के लिए **Resource group** चुनें (आवश्यक होने पर नया बनाएँ)।
    - उपयोग के लिए **Location** चुनें।
    - उपयोग के लिए **Connect Azure AI Services** चुनें (आवश्यक होने पर नया बनाएँ)।
    - **Connect Azure AI Search** चुनें और **Skip connecting** चुनें।

    ![FineTuneSelect](../../../../translated_images/hi/create-hub.49e53d235e80779e.webp)

1. **Next** चुनें।
1. **Create a project** चुनें।

### डेटा तैयारी

फाइन-ट्यूनिंग से पहले, ऐसे डेटासेट इकट्ठा करें या बनाएं जो आपके कार्य से संबंधित हों, जैसे चैट निर्देश, प्रश्न-उत्तर जोड़ी, या अन्य कोई प्रासंगिक टेक्स्ट डेटा। इस डेटा को साफ़ करें और पूर्वसंसाधित करें, जिसमें शोर हटाना, अनुपस्थित मानों को संभालना, और टेक्स्ट को टोकनाइज करना शामिल है।

### Microsoft Foundry में Phi-3 मॉडलों को फाइन-ट्यून करें

> [!NOTE]
> Phi-3 मॉडलों का फाइन-ट्यूनिंग वर्तमान में East US 2 में स्थित प्रोजेक्ट्स में समर्थित है।

1. बाएं साइड टैब से **Model catalog** चुनें।

1. **search bar** में *phi-3* टाइप करें और वह phi-3 मॉडल चुनें जिसे आप उपयोग करना चाहते हैं।

    ![FineTuneSelect](../../../../translated_images/hi/select-model.60ef2d4a6a3cec57.webp)

1. **Fine-tune** चुनें।

    ![FineTuneSelect](../../../../translated_images/hi/select-finetune.a976213b543dd9d8.webp)

1. **Fine-tuned model name** दर्ज करें।

    ![FineTuneSelect](../../../../translated_images/hi/finetune1.c2b39463f0d34148.webp)

1. **Next** चुनें।

1. निम्न कार्य करें:

    - **task type** के लिए **Chat completion** चुनें।
    - उपयोग करने के लिए **Training data** चुनें। आप इसे Microsoft Foundry के डेटा से या अपनी स्थानीय वातावरण से अपलोड कर सकते हैं।

    ![FineTuneSelect](../../../../translated_images/hi/finetune2.43cb099b1a94442d.webp)

1. **Next** चुनें।

1. उपयोग करने के लिए **Validation data** अपलोड करें, या आप **Automatic split of training data** चुन सकते हैं।

    ![FineTuneSelect](../../../../translated_images/hi/finetune3.fd96121b67dcdd92.webp)

1. **Next** चुनें।

1. निम्न कार्य करें:

    - उपयोग करने के लिए **Batch size multiplier** चुनें।
    - उपयोग करने के लिए **Learning rate** चुनें।
    - उपयोग करने के लिए **Epochs** चुनें।

    ![FineTuneSelect](../../../../translated_images/hi/finetune4.e18b80ffccb5834a.webp)

1. फाइन-ट्यूनिंग प्रक्रिया शुरू करने के लिए **Submit** चुनें।

    ![FineTuneSelect](../../../../translated_images/hi/select-submit.0a3802d581bac271.webp)


1. एक बार जब आपका मॉडल फाइन-ट्यून हो जाता है, तो स्थिति **Completed** के रूप में दिखेगी, जैसा कि नीचे की छवि में दिखाया गया है। अब आप मॉडल को डिप्लॉय कर सकते हैं और इसे अपनी खुद की एप्लिकेशन, प्लेग्राउंड, या प्रॉम्प्ट फ्लो में उपयोग कर सकते हैं। अधिक जानकारी के लिए देखें [Microsoft Foundry के साथ Phi-3 परिवार के छोटे भाषा मॉडलों को कैसे डिप्लॉय करें](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)।

    ![FineTuneSelect](../../../../translated_images/hi/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Phi-3 के फाइन-ट्यूनिंग पर अधिक विस्तृत जानकारी के लिए कृपया देखें [Microsoft Foundry में Phi-3 मॉडलों को फाइन-ट्यून करना](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini)।

## अपने फाइन-ट्यून किए गए मॉडलों को साफ़ करना

आप [Microsoft Foundry](https://ai.azure.com) में फाइन-ट्यून मॉडल सूची या मॉडल विवरण पृष्ठ से किसी भी फाइन-ट्यून मॉडल को हटा सकते हैं। फाइन-ट्यून पेज से हटाने के लिए फाइन-ट्यून मॉडल को चुनें, फिर हटाने के लिए Delete बटन चुनें।

> [!NOTE]
> यदि किसी कस्टम मॉडल की मौजूदा डिप्लॉयमेंट है, तो आप उसे डिलीट नहीं कर सकते। कृपया पहले अपने मॉडल डिप्लॉयमेंट को हटा दें, उसके बाद ही आप अपने कस्टम मॉडल को हटा सकते हैं।

## लागत और क्वोटा

### Phi-3 मॉडलों के लिए सेवा के रूप में फाइन-ट्यूनिंग की लागत और कोटा विचार

Phi मॉडल, जो सेवा के रूप में फाइन-ट्यून किए गए हैं, Microsoft द्वारा प्रदान किए जाते हैं और Microsoft Foundry के साथ एकीकृत हैं। मूल्य निर्धारण आप मॉडल को [डिप्लॉय](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) या फाइन-ट्यून करते समय डिप्लॉयमेंट विज़ार्ड में Pricing and terms टैब के तहत देख सकते हैं।

## सामग्री फ़िल्टरिंग

पे-एज़-यू-गो के साथ सेवा के रूप में डिप्लॉय किए गए मॉडलों को Azure AI Content Safety द्वारा सुरक्षा दी जाती है। जब इन्हें रियल-टाइम एंडपॉइंट्स पर डिप्लॉय किया जाता है, तो आप इस सुविधा से बाहर निकल सकते हैं। Azure AI कंटेंट सुरक्षा सक्षम होने पर, प्रॉम्प्ट और पूर्णता दोनों एक वर्गीकरण मॉडलों के समूह से गुजरते हैं जो हानिकारक सामग्री के आउटपुट का पता लगाने और रोकने का प्रयास करते हैं। सामग्री फ़िल्टरिंग सिस्टम इनपुट प्रॉम्प्ट्स और आउटपुट पूर्णताओं दोनों में संभावित हानिकारक सामग्री की विशिष्ट श्रेणियों का पता लगाता है और उस पर कार्रवाई करता है। Azure AI Content Safety के बारे में अधिक जानें [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering)।

**फाइन-ट्यूनिंग सेटअप**

हाइपरपैरामीटर: सीखने की दर, बैच आकार, और प्रशिक्षण इपॉक्स की संख्या जैसे हाइपरपैरामीटर परिभाषित करें।

**लॉस फ़ंक्शन**

अपने कार्य के लिए उपयुक्त लॉस फ़ंक्शन चुनें (जैसे, क्रॉस-एंट्रॉपी)।

**ऑप्टिमाइज़र**

प्रशिक्षण के दौरान ग्रेडिएंट अपडेट्स के लिए ऑप्टिमाइज़र चुनें (जैसे, Adam)।

**फाइन-ट्यूनिंग प्रक्रिया**

- पूर्व-प्रशिक्षित मॉडल लोड करें: Phi-3 Mini चेकपॉइंट लोड करें।
- कस्टम लेयर्स जोड़ें: कार्य-विशिष्ट लेयर्स जोड़ें (जैसे, चैट निर्देशों के लिए वर्गीकरण हेड)।

**मॉडल को प्रशिक्षित करें**
अपने तैयार किए गए डेटासेट का उपयोग करके मॉडल को फाइन-ट्यून करें। प्रशिक्षण प्रगति की निगरानी करें और जरूरत के अनुसार हाइपरपैरामीटर समायोजित करें।

**मूल्यांकन और मान्यकरण**

मान्यकरण सेट: अपने डेटा को प्रशिक्षण और मान्यकरण सेटों में विभाजित करें।

**प्रदर्शन का मूल्यांकन करें**

मॉडल के प्रदर्शन का आकलन करने के लिए सटीकता, F1-स्कोर, या पर्प्लेक्सिटी जैसे मेट्रिक्स का उपयोग करें।

## फाइन-ट्यून मॉडल को सहेजें

**चेकपॉइंट**
भविष्य के उपयोग के लिए फाइन-ट्यून किए गए मॉडल चेकपॉइंट को सहेजें।

## डिप्लॉयमेंट

- वेब सेवा के रूप में डिप्लॉय करें: अपना फाइन-ट्यून मॉडल Microsoft Foundry में वेब सेवा के रूप में डिप्लॉय करें।
- एंडपॉइंट का परीक्षण करें: डिप्लॉय किए गए एंडपॉइंट पर परीक्षण क्वेरी भेजकर इसकी कार्यक्षमता सत्यापित करें।

## पुनरावृत्ति और सुधार करें

पुनरावृत्ति करें: यदि प्रदर्शन संतोषजनक नहीं है, तो हाइपरपैरामीटर समायोजित करके, अधिक डेटा जोड़कर, या अतिरिक्त इपॉक्स के लिए फाइन-ट्यून करके पुनरावृत्ति करें।

## निगरानी और सुधार करें

लगातार मॉडल के व्यवहार पर नजर रखें और आवश्यकतानुसार सुधार करें।

## अनुकूलित करें और विस्तार करें

कस्टम कार्य: Phi-3 Mini को चैट निर्देशों के अलावा विभिन्न कार्यों के लिए भी फाइन-ट्यून किया जा सकता है। अन्य उपयोग मामलों का अन्वेषण करें!
प्रयोग करें: प्रदर्शन बढ़ाने के लिए विभिन्न आर्किटेक्चर, लेयर संयोजन, और तकनीकों को आज़माएं।

> [!NOTE]
> फाइन-ट्यूनिंग एक पुनरावृत्तिक प्रक्रिया है। प्रयोग करें, सीखें, और अपने विशिष्ट कार्य के लिए सर्वोत्तम परिणाम प्राप्त करने के लिए अपने मॉडल को अनुकूलित करें!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। यद्यपि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या असंगतियां हो सकती हैं। मूल भाषा में मूल दस्तावेज़ को प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->