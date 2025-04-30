<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94e7d7ab455720bab75ead5c28521c97",
  "translation_date": "2025-04-04T18:49:32+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_AIFoundry.md",
  "language_code": "hi"
}
-->
# Phi-3 को Azure AI Foundry के साथ फाइन-ट्यून करना

चलो Microsoft के Phi-3 Mini भाषा मॉडल को Azure AI Foundry के माध्यम से फाइन-ट्यून करना सीखते हैं। फाइन-ट्यूनिंग आपको Phi-3 Mini को विशेष कार्यों के लिए अनुकूलित करने की सुविधा देता है, जिससे यह अधिक शक्तिशाली और संदर्भ-संवेदनशील बन जाता है।

## विचार करने योग्य बातें

- **क्षमताएं:** कौन से मॉडल फाइन-ट्यून किए जा सकते हैं? बेस मॉडल को किस प्रकार के कार्यों के लिए फाइन-ट्यून किया जा सकता है?
- **लागत:** फाइन-ट्यूनिंग के लिए मूल्य निर्धारण मॉडल क्या है?
- **कस्टमाइज़ेबिलिटी:** बेस मॉडल को कितना और किस प्रकार से संशोधित किया जा सकता है?
- **सुविधा:** फाइन-ट्यूनिंग कैसे किया जाता है – क्या मुझे कस्टम कोड लिखने की आवश्यकता है? क्या मुझे अपना कंप्यूट लाना होगा?
- **सुरक्षा:** फाइन-ट्यून किए गए मॉडल में सुरक्षा जोखिम हो सकते हैं – क्या अनजाने नुकसान से बचाव के लिए कोई उपाय हैं?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.hi.png)

## फाइन-ट्यूनिंग की तैयारी

### पूर्व आवश्यकताएं

> [!NOTE]
> Phi-3 परिवार के मॉडल के लिए, पे-एज़-यू-गो मॉडल फाइन-ट्यूनिंग सुविधा केवल **East US 2** क्षेत्रों में बनाए गए हब के साथ उपलब्ध है।

- एक Azure सदस्यता। यदि आपके पास Azure सदस्यता नहीं है, तो [पेड Azure अकाउंट](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) बनाएं और शुरू करें।

- एक [AI Foundry प्रोजेक्ट](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)।
- Azure रोल-आधारित एक्सेस कंट्रोल (Azure RBAC) का उपयोग Azure AI Foundry में ऑपरेशंस तक पहुंच प्रदान करने के लिए किया जाता है। इस लेख में दिए गए चरणों को पूरा करने के लिए, आपके उपयोगकर्ता खाते को __Azure AI Developer रोल__ में संसाधन समूह पर असाइन किया जाना चाहिए।

### सदस्यता प्रदाता पंजीकरण

सुनिश्चित करें कि सदस्यता `Microsoft.Network` संसाधन प्रदाता के लिए पंजीकृत है।

1. [Azure पोर्टल](https://portal.azure.com) में साइन इन करें।
1. बाएं मेनू से **Subscriptions** चुनें।
1. उस सदस्यता का चयन करें जिसे आप उपयोग करना चाहते हैं।
1. बाएं मेनू से **AI प्रोजेक्ट सेटिंग्स** > **Resource providers** चुनें।
1. सुनिश्चित करें कि **Microsoft.Network** संसाधन प्रदाताओं की सूची में है। अन्यथा इसे जोड़ें।

### डेटा तैयारी

अपने मॉडल को फाइन-ट्यून करने के लिए प्रशिक्षण और मान्यता डेटा तैयार करें। आपके प्रशिक्षण डेटा और मान्यता डेटा सेट में इनपुट और आउटपुट उदाहरण शामिल होने चाहिए कि आप मॉडल को कैसे प्रदर्शन करना चाहते हैं।

सुनिश्चित करें कि आपके सभी प्रशिक्षण उदाहरण अनुमान के लिए अपेक्षित प्रारूप का पालन करते हैं। मॉडल को प्रभावी ढंग से फाइन-ट्यून करने के लिए, एक संतुलित और विविध डेटा सेट सुनिश्चित करें।

इसमें डेटा संतुलन बनाए रखना, विभिन्न परिदृश्यों को शामिल करना, और वास्तविक दुनिया की अपेक्षाओं के साथ डेटा को सामंजस्यपूर्ण बनाने के लिए समय-समय पर प्रशिक्षण डेटा को परिष्कृत करना शामिल है, जो अंततः अधिक सटीक और संतुलित मॉडल प्रतिक्रियाओं की ओर ले जाता है।

विभिन्न प्रकार के मॉडल के लिए प्रशिक्षण डेटा का अलग-अलग प्रारूप आवश्यक होता है।

### चैट पूर्णता

आप जो प्रशिक्षण और मान्यता डेटा उपयोग करते हैं, उसे **JSON Lines (JSONL)** दस्तावेज़ के रूप में स्वरूपित किया जाना चाहिए। `Phi-3-mini-128k-instruct` के लिए, फाइन-ट्यूनिंग डेटा सेट को उसी संवादात्मक प्रारूप में स्वरूपित किया जाना चाहिए जो चैट पूर्णता API द्वारा उपयोग किया जाता है।

### उदाहरण फ़ाइल प्रारूप

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

समर्थित फ़ाइल प्रकार JSON Lines है। फ़ाइलें डिफ़ॉल्ट डेटा स्टोर में अपलोड की जाती हैं और आपके प्रोजेक्ट में उपलब्ध होती हैं।

## Azure AI Foundry के साथ Phi-3 को फाइन-ट्यून करना

Azure AI Foundry आपको एक प्रक्रिया का उपयोग करके बड़े भाषा मॉडल को अपने व्यक्तिगत डेटा सेट्स के साथ अनुकूलित करने देता है जिसे फाइन-ट्यूनिंग कहा जाता है। फाइन-ट्यूनिंग महत्वपूर्ण मूल्य प्रदान करता है क्योंकि यह विशिष्ट कार्यों और अनुप्रयोगों के लिए अनुकूलन और अनुकूलन को सक्षम बनाता है। यह बेहतर प्रदर्शन, लागत दक्षता, कम विलंबता, और अनुकूलित आउटपुट की ओर ले जाता है।

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.hi.png)

### नया प्रोजेक्ट बनाएं

1. [Azure AI Foundry](https://ai.azure.com) में साइन इन करें।

1. **+New project** चुनें ताकि Azure AI Foundry में नया प्रोजेक्ट बनाया जा सके।

    ![FineTuneSelect](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.hi.png)

1. निम्नलिखित कार्य करें:

    - प्रोजेक्ट **Hub name**। यह एक अद्वितीय मान होना चाहिए।
    - उपयोग करने के लिए **Hub** का चयन करें (यदि आवश्यक हो तो नया बनाएं)।

    ![FineTuneSelect](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.hi.png)

1. नया हब बनाने के लिए निम्नलिखित कार्य करें:

    - **Hub name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
    - अपना Azure **Subscription** चुनें।
    - उपयोग करने के लिए **Resource group** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - वह **Location** चुनें जिसे आप उपयोग करना चाहते हैं।
    - उपयोग करने के लिए **Connect Azure AI Services** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - **Connect Azure AI Search** चुनें ताकि **Skip connecting** हो।

    ![FineTuneSelect](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.hi.png)

1. **Next** चुनें।
1. **Create a project** चुनें।

### डेटा तैयारी

फाइन-ट्यूनिंग से पहले, अपने कार्य से संबंधित डेटा सेट एकत्र करें या बनाएं, जैसे चैट निर्देश, प्रश्न-उत्तर जोड़े, या अन्य संबंधित पाठ डेटा। इस डेटा को साफ करें और प्रीप्रोसेस करें, जिसमें शोर हटाना, गायब मानों को संभालना, और पाठ को टोकनाइज़ करना शामिल है।

### Azure AI Foundry में Phi-3 मॉडल को फाइन-ट्यून करना

> [!NOTE]
> Phi-3 मॉडल का फाइन-ट्यूनिंग वर्तमान में East US 2 में स्थित प्रोजेक्ट्स में समर्थित है।

1. बाएं साइड टैब से **Model catalog** चुनें।

1. **search bar** में *phi-3* टाइप करें और उस phi-3 मॉडल को चुनें जिसे आप उपयोग करना चाहते हैं।

    ![FineTuneSelect](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.hi.png)

1. **Fine-tune** चुनें।

    ![FineTuneSelect](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.hi.png)

1. **Fine-tuned model name** दर्ज करें।

    ![FineTuneSelect](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.hi.png)

1. **Next** चुनें।

1. निम्नलिखित कार्य करें:

    - **task type** को **Chat completion** पर सेट करें।
    - उपयोग करने के लिए **Training data** चुनें। आप इसे Azure AI Foundry के डेटा के माध्यम से या अपने स्थानीय वातावरण से अपलोड कर सकते हैं।

    ![FineTuneSelect](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.hi.png)

1. **Next** चुनें।

1. उपयोग करने के लिए **Validation data** अपलोड करें। या आप **Automatic split of training data** चुन सकते हैं।

    ![FineTuneSelect](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.hi.png)

1. **Next** चुनें।

1. निम्नलिखित कार्य करें:

    - उपयोग करने के लिए **Batch size multiplier** चुनें।
    - उपयोग करने के लिए **Learning rate** चुनें।
    - उपयोग करने के लिए **Epochs** चुनें।

    ![FineTuneSelect](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.hi.png)

1. फाइन-ट्यूनिंग प्रक्रिया शुरू करने के लिए **Submit** चुनें।

    ![FineTuneSelect](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.hi.png)

1. एक बार आपका मॉडल फाइन-ट्यून हो जाए, स्थिति **Completed** के रूप में प्रदर्शित होगी, जैसा कि नीचे दी गई छवि में दिखाया गया है। अब आप मॉडल को तैनात कर सकते हैं और इसे अपने एप्लिकेशन, प्लेग्राउंड, या प्रॉम्प्ट फ्लो में उपयोग कर सकते हैं। अधिक जानकारी के लिए, देखें [Phi-3 परिवार के छोटे भाषा मॉडल को Azure AI Foundry के साथ कैसे तैनात करें](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)।

    ![FineTuneSelect](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.hi.png)

> [!NOTE]
> Phi-3 को फाइन-ट्यून करने पर अधिक विस्तृत जानकारी के लिए कृपया देखें [Azure AI Foundry में Phi-3 मॉडल को फाइन-ट्यून करें](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini)।

## अपने फाइन-ट्यून किए गए मॉडल को साफ करना

आप [Azure AI Foundry](https://ai.azure.com) में फाइन-ट्यूनिंग मॉडल सूची या मॉडल विवरण पृष्ठ से फाइन-ट्यून किए गए मॉडल को हटा सकते हैं। फाइन-ट्यूनिंग पृष्ठ से हटाने के लिए फाइन-ट्यून किए गए मॉडल का चयन करें और फिर **Delete** बटन चुनें।

> [!NOTE]
> आप किसी कस्टम मॉडल को तब तक नहीं हटा सकते जब तक कि उसकी कोई मौजूदा तैनाती न हो। आपको पहले अपनी मॉडल तैनाती को हटाना होगा, फिर अपने कस्टम मॉडल को हटा सकते हैं।

## लागत और कोटा

### सेवा के रूप में फाइन-ट्यून किए गए Phi-3 मॉडल के लिए लागत और कोटा विचार

Phi मॉडल सेवा के रूप में फाइन-ट्यून किए गए Microsoft द्वारा प्रदान किए जाते हैं और उपयोग के लिए Azure AI Foundry के साथ एकीकृत होते हैं। आप [तैनाती](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) या मॉडल को फाइन-ट्यूनिंग करते समय मूल्य निर्धारण को तैनाती विज़ार्ड के Pricing and terms टैब के तहत देख सकते हैं।

## सामग्री फ़िल्टरिंग

पे-एज़-यू-गो के रूप में सेवा के रूप में तैनात मॉडल Azure AI Content Safety द्वारा सुरक्षित हैं। वास्तविक समय एंडपॉइंट्स पर तैनात होने पर, आप इस क्षमता से बाहर निकल सकते हैं। Azure AI Content Safety सक्षम होने पर, प्रॉम्प्ट और पूर्णता दोनों हानिकारक सामग्री के उत्पादन का पता लगाने और रोकने के उद्देश्य से वर्गीकरण मॉडल के एक समूह के माध्यम से गुजरते हैं। सामग्री फ़िल्टरिंग प्रणाली इनपुट प्रॉम्प्ट और आउटपुट पूर्णताओं में संभावित हानिकारक सामग्री की विशिष्ट श्रेणियों पर कार्रवाई करती है। अधिक जानें [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering)।

**फाइन-ट्यूनिंग कॉन्फ़िगरेशन**

हाइपरपैरामीटर्स: लर्निंग रेट, बैच साइज, और प्रशिक्षण एपॉक्स की संख्या जैसे हाइपरपैरामीटर्स को परिभाषित करें।

**लॉस फंक्शन**

अपने कार्य के लिए उपयुक्त लॉस फंक्शन चुनें (जैसे, क्रॉस-एंट्रोपी)।

**ऑप्टिमाइज़र**

ग्रेडिएंट अपडेट्स के दौरान प्रशिक्षण के लिए ऑप्टिमाइज़र (जैसे, Adam) चुनें।

**फाइन-ट्यूनिंग प्रक्रिया**

- प्री-ट्रेंड मॉडल लोड करें: Phi-3 Mini चेकपॉइंट लोड करें।
- कस्टम लेयर्स जोड़ें: कार्य-विशिष्ट लेयर्स जोड़ें (जैसे, चैट निर्देशों के लिए वर्गीकरण हेड)।

**मॉडल को प्रशिक्षित करें**
अपने तैयार डेटा सेट का उपयोग करके मॉडल को फाइन-ट्यून करें। प्रशिक्षण प्रगति की निगरानी करें और हाइपरपैरामीटर्स को आवश्यकतानुसार समायोजित करें।

**मूल्यांकन और मान्यता**

मान्यता सेट: अपने डेटा को प्रशिक्षण और मान्यता सेट में विभाजित करें।

**प्रदर्शन का मूल्यांकन करें**

सटीकता, F1-स्कोर, या पेरप्लेक्सिटी जैसे मेट्रिक्स का उपयोग करके मॉडल प्रदर्शन का मूल्यांकन करें।

## फाइन-ट्यून किए गए मॉडल को सहेजें

**चेकपॉइंट**
भविष्य में उपयोग के लिए फाइन-ट्यून किए गए मॉडल चेकपॉइंट को सहेजें।

## तैनाती

- वेब सेवा के रूप में तैनात करें: अपने फाइन-ट्यून किए गए मॉडल को Azure AI Foundry में वेब सेवा के रूप में तैनात करें।
- एंडपॉइंट का परीक्षण करें: तैनात एंडपॉइंट को सत्यापित करने के लिए परीक्षण क्वेरी भेजें।

## पुनरावृत्ति और सुधार करें

पुनरावृत्ति करें: यदि प्रदर्शन संतोषजनक नहीं है, तो हाइपरपैरामीटर्स को समायोजित करके, अधिक डेटा जोड़कर, या अतिरिक्त एपॉक्स के लिए फाइन-ट्यूनिंग करके पुनरावृत्ति करें।

## निगरानी और परिष्कृत करें

मॉडल के व्यवहार की लगातार निगरानी करें और आवश्यकतानुसार परिष्कृत करें।

## अनुकूलित करें और विस्तारित करें

कस्टम कार्य: Phi-3 Mini को चैट निर्देशों से परे विभिन्न कार्यों के लिए फाइन-ट्यून किया जा सकता है। अन्य उपयोग मामलों का अन्वेषण करें!
प्रयोग: प्रदर्शन को बढ़ाने के लिए विभिन्न आर्किटेक्चर, लेयर संयोजन, और तकनीकों को आजमाएं।

> [!NOTE]
> फाइन-ट्यूनिंग एक पुनरावृत्त प्रक्रिया है। प्रयोग करें, सीखें, और अपने मॉडल को अपने विशिष्ट कार्य के लिए सर्वश्रेष्ठ परिणाम प्राप्त करने के लिए अनुकूलित करें!

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।