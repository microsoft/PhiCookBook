# Microsoft Foundry में Microsoft के Responsible AI सिद्धांतों पर ध्यान केंद्रित करते हुए Fine-tuned Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें

यह एंड-टू-एंड (E2E) नमूना Microsoft Tech Community के "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" गाइड पर आधारित है।

## अवलोकन

### Microsoft Foundry में Fine-tuned Phi-3 / Phi-3.5 मॉडल की सुरक्षा और प्रदर्शन का आप कैसे मूल्यांकन कर सकते हैं?

किसी मॉडल को फाइन-ट्यून करने से कभी-कभी अनचाहे या अवांछित उत्तर उत्पन्न हो सकते हैं। यह सुनिश्चित करने के लिए कि मॉडल सुरक्षित और प्रभावी रहता है, यह महत्वपूर्ण है कि मॉडल की हानिकारक सामग्री उत्पन्न करने की क्षमता और सटीक, प्रासंगिक, और सक्षम उत्तर प्रदान करने की क्षमता को मूल्यांकित किया जाए। इस ट्यूटोरियल में, आप सीखेंगे कि Microsoft Foundry में Prompt flow के साथ एकीकृत Fine-tuned Phi-3 / Phi-3.5 मॉडल की सुरक्षा और प्रदर्शन का कैसे मूल्यांकन करें।

यहाँ Microsoft Foundry की मूल्यांकन प्रक्रिया है।

![Architecture of tutorial.](../../../../../../translated_images/hi/architecture.10bec55250f5d6a4.webp)

*छवि स्रोत: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 के बारे में और अधिक विस्तृत जानकारी और अतिरिक्त संसाधनों का अन्वेषण करने के लिए कृपया [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) देखें।

### आवश्यकताएँ

- [Python](https://www.python.org/downloads)
- [Azure सदस्यता](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 मॉडल

### विषय सूची

1. [**परिदृश्य 1: Microsoft Foundry के Prompt flow मूल्यांकन का परिचय**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [सुरक्षा मूल्यांकन का परिचय](#सुरक्षा-मूल्यांकन-का-परिचय)
    - [प्रदर्शन मूल्यांकन का परिचय](#प्रदर्शन-मूल्यांकन-का-परिचय)

1. [**परिदृश्य 2: Microsoft Foundry में Phi-3 / Phi-3.5 मॉडल का मूल्यांकन**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [शुरू करने से पहले](#शुरू-करने-से-पहले)
    - [Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए Azure OpenAI को तैनात करें](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Microsoft Foundry के Prompt flow मूल्यांकन का उपयोग करते हुए Fine-tuned Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [बधाई हो!](#बधाई-हो)

## **परिदृश्य 1: Microsoft Foundry के Prompt flow मूल्यांकन का परिचय**

### सुरक्षा मूल्यांकन का परिचय

यह सुनिश्चित करने के लिए कि आपका AI मॉडल नैतिक और सुरक्षित है, यह महत्वपूर्ण है कि आप इसे Microsoft के Responsible AI सिद्धांतों के अनुसार मूल्यांकन करें। Microsoft Foundry में, सुरक्षा मूल्यांकन आपको अपने मॉडल की jailbreak हमलों के प्रति संवेदनशीलता और हानिकारक सामग्री उत्पन्न करने की क्षमता का मूल्यांकन करने की अनुमति देता है, जो सीधे इन सिद्धांतों के साथ मेल खाता है।

![Safaty evaluation.](../../../../../../translated_images/hi/safety-evaluation.083586ec88dfa950.webp)

*छवि स्रोत: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft के Responsible AI सिद्धांत

तकनीकी कदम शुरू करने से पहले, Microsoft के Responsible AI सिद्धांतों को समझना आवश्यक है, जो AI प्रणालियों के जिम्मेदार विकास, तैनाती और संचालन के लिए एक नैतिक ढांचा प्रदान करते हैं। ये सिद्धांत AI प्रणालियों के जिम्मेदार डिजाइन, विकास और तैनाती का मार्गदर्शन करते हैं, जो यह सुनिश्चित करते हैं कि AI तकनीकें न्यायसंगत, पारदर्शी और समावेशी तरीके से बनाई जाएं। ये सिद्धांत AI मॉडलों की सुरक्षा का मूल्यांकन करने की नींव हैं।

Microsoft के Responsible AI सिद्धांतों में शामिल हैं:

- **न्याय और समावेशन**: AI प्रणालियों को सभी के प्रति निष्पक्ष व्यवहार करना चाहिए और समान परिस्थितियों में लोगों के समूहों के साथ भेदभाव नहीं करना चाहिए। उदाहरण के लिए, जब AI प्रणाली चिकित्सा उपचार, ऋण आवेदन या रोजगार पर मार्गदर्शन प्रदान करती हैं, तो उन्हें समान लक्षणों, वित्तीय स्थिति या व्यावसायिक योग्यताओं वाले सभी लोगों के लिए समान सिफारिशें करनी चाहिए।

- **विश्वसनीयता और सुरक्षा**: विश्वास बनाना आवश्यक है, इसलिए AI प्रणालियों को विश्वसनीयता, सुरक्षा और सुसंगतता के साथ काम करना चाहिए। ये प्रणालियाँ वैसे ही काम करनी चाहिए जैसे उन्हें मूल रूप से डिज़ाइन किया गया था, अप्रत्याशित स्थितियों के प्रति सुरक्षित प्रतिक्रिया देनी चाहिए, और हानिकारक हेरफेर का सामना कर सकें। उनका व्यवहार और वे किन स्थितियों को संभाल सकते हैं, यह उन परिस्थितियों और परिदृश्यों की विविधता को दर्शाता है जिन्हें डेवलपर्स ने डिज़ाइन और परीक्षण के दौरान अनुमानित किया।

- **पारदर्शिता**: जब AI प्रणालियाँ ऐसे निर्णय लेने में मदद करती हैं जिनका लोगों के जीवन पर गहरा प्रभाव पड़ता है, तो यह आवश्यक है कि लोग समझें कि वे निर्णय कैसे लिए गए। उदाहरण के लिए, एक बैंक AI प्रणाली का उपयोग यह तय करने के लिए कर सकता है कि कोई व्यक्ति क्रेडिट योग्य है या नहीं। एक कंपनी AI प्रणाली का उपयोग सर्वाधिक योग्य उम्मीदवारों का चयन करने के लिए कर सकती है।

- **गोपनीयता और सुरक्षा**: जैसे-जैसे AI व्यापक होता जा रहा है, गोपनीयता की सुरक्षा और व्यक्तिगत व व्यवसायिक सूचना की सुरक्षा और अधिक महत्वपूर्ण और जटिल होती जा रही है। AI के साथ, गोपनीयता और डेटा सुरक्षा विशेष ध्यान की आवश्यकता है क्योंकि AI प्रणालियों के लिए सटीक और सूचित भविष्यवाणियाँ व निर्णय लेने हेतु डेटा का उपयोग आवश्यक होता है।

- **जवाबदेही**: जो लोग AI प्रणालियों को डिज़ाइन और तैनात करते हैं, उन्हें उनके संचालन के लिए जवाबदेह होना चाहिए। संगठन उद्योग मानकों का उपयोग करके जवाबदेही मानदंड विकसित कर सकते हैं। ये मानदंड यह सुनिश्चित कर सकते हैं कि AI प्रणाली लोगों के जीवन को प्रभावित करने वाले किसी भी निर्णय पर अंतिम प्राधिकार न हो। ये यह भी सुनिश्चित कर सकते हैं कि मनुष्य उच्च स्वायत्त AI प्रणालियों पर सार्थक नियंत्रण बनाए रखें।

![Fill hub.](../../../../../../translated_images/hi/responsibleai2.c07ef430113fad8c.webp)

*छवि स्रोत: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft के Responsible AI सिद्धांतों के बारे में अधिक जानने के लिए, [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) देखें।

#### सुरक्षा मेट्रिक्स

इस ट्यूटोरियल में, आप Microsoft Foundry की सुरक्षा मेट्रिक्स का उपयोग करके Fine-tuned Phi-3 मॉडल की सुरक्षा का मूल्यांकन करेंगे। ये मेट्रिक्स आपको मॉडल की हानिकारक सामग्री उत्पन्न करने की क्षमता और jailbreak हमलों के प्रति इसकी संवेदनशीलता का मूल्यांकन करने में मदद करती हैं। सुरक्षा मेट्रिक्स में शामिल हैं:

- **स्व-हानि संबंधित सामग्री**: यह मूल्यांकन करता है कि क्या मॉडल में स्व-हानि संबंधित सामग्री उत्पन्न करने की प्रवृत्ति है।
- **घृणास्पद और अनुचित सामग्री**: यह मूल्यांकन करता है कि क्या मॉडल में घृणास्पद या अनुचित सामग्री उत्पन्न करने की प्रवृत्ति है।
- **हिंसात्मक सामग्री**: यह मूल्यांकन करता है कि क्या मॉडल में हिंसक सामग्री उत्पन्न करने की प्रवृत्ति है।
- **यौन सामग्री**: यह मूल्यांकन करता है कि क्या मॉडल में अनुचित यौन सामग्री उत्पन्न करने की प्रवृत्ति है।

इन पहलुओं का मूल्यांकन यह सुनिश्चित करता है कि AI मॉडल हानिकारक या आपत्तिजनक सामग्री का उत्पादन न करे, और यह सामाजिक मूल्यों और नियामक मानकों के अनुरूप हो।

![Evaluate based on safety.](../../../../../../translated_images/hi/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### प्रदर्शन मूल्यांकन का परिचय

यह सुनिश्चित करने के लिए कि आपका AI मॉडल अपेक्षित प्रदर्शन कर रहा है, इसके प्रदर्शन को प्रदर्शन मेट्रिक्स के विरुद्ध मूल्यांकित करना महत्वपूर्ण है। Microsoft Foundry में, प्रदर्शन मूल्यांकन आपको सटीक, प्रासंगिक, और सक्षम उत्तर उत्पन्न करने में मॉडल की प्रभावशीलता का मूल्यांकन करने की अनुमति देते हैं।

![Safaty evaluation.](../../../../../../translated_images/hi/performance-evaluation.48b3e7e01a098740.webp)

*छवि स्रोत: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### प्रदर्शन मेट्रिक्स

इस ट्यूटोरियल में, आप Microsoft Foundry की प्रदर्शन मेट्रिक्स का उपयोग करके Fine-tuned Phi-3 / Phi-3.5 मॉडल के प्रदर्शन का मूल्यांकन करेंगे। ये मेट्रिक्स आपको मॉडल की प्रभावशीलता का मूल्यांकन करने में मदद करती हैं कि वह कितनी सटीक, प्रासंगिक, और सक्षम उत्तर उत्पन्न करता है। प्रदर्शन मेट्रिक्स में शामिल हैं:

- **ग्राउंडेडनेस**: यह मूल्यांकन करता है कि उत्पन्न उत्तर इनपुट स्रोत की जानकारी के कितने अनुरूप हैं।
- **प्रासंगिकता**: यह मूल्यांकन करता है कि उत्पन्न उत्तर प्रश्नों के लिए कितने उपयुक्त हैं।
- **सुसंगतता**: यह मूल्यांकन करता है कि उत्पन्न पाठ कितनी सहजता से प्रवाहित होता है, प्राकृतिक पढ़ाई जैसा लगता है, और मानवीय भाषा जैसा प्रतीत होता है।
- **फ्लुएंसी**: यह मूल्यांकन करता है कि उत्पन्न पाठ की भाषा दक्षता कैसी है।
- **GPT समानता**: यह उत्पन्न उत्तर की तुलना ग्राउंड ट्रुथ से करता है समानता के लिए।
- **F1 स्कोर**: उत्पन्न उत्तर और स्रोत डेटा के बीच साझा शब्दों के अनुपात की गणना करता है।

ये मेट्रिक्स आपको मॉडल की सटीक, प्रासंगिक और सुसंगत उत्तर उत्पन्न करने की क्षमता का मूल्यांकन करने में मदद करती हैं।

![Evaluate based on performance.](../../../../../../translated_images/hi/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **परिदृश्य 2: Microsoft Foundry में Phi-3 / Phi-3.5 मॉडल का मूल्यांकन**

### शुरू करने से पहले

यह ट्यूटोरियल पिछली ब्लॉग पोस्टों, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" और "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" का अनुसरण है। इन पोस्टों में, हमने Microsoft Foundry में Phi-3 / Phi-3.5 मॉडल को फाइन-ट्यून करने और इसे Prompt flow के साथ एकीकृत करने की प्रक्रिया का वर्णन किया।

इस ट्यूटोरियल में, आप Microsoft Foundry में एक अलगक Azure OpenAI मॉडल तैनात करेंगे और इसे अपने Fine-tuned Phi-3 / Phi-3.5 मॉडल के मूल्यांकन के लिए उपयोग करेंगे।

इस ट्यूटोरियल को शुरू करने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित आवश्यकताएँ हैं, जैसा कि पिछली ट्यूटोरियल्स में वर्णित है:

1. Fine-tuned Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए तैयार डेटासेट।
1. Phi-3 / Phi-3.5 मॉडल जिसे फाइन-ट्यून कर Azure Machine Learning में तैनात किया गया हो।
1. Microsoft Foundry में आपके Fine-tuned Phi-3 / Phi-3.5 मॉडल के साथ एकीकृत Prompt flow।

> [!NOTE]
> आप *test_data.jsonl* फ़ाइल का उपयोग करेंगे, जो पहले के ब्लॉग पोस्टों में डाउनलोड किए गए **ULTRACHAT_200k** डेटासेट के डेटा फोल्डर में स्थित है, Fine-tuned Phi-3 / Phi-3.5 मॉडल के मूल्यांकन के लिए डेटासेट के रूप में।

#### Microsoft Foundry में Prompt flow के साथ कस्टम Phi-3 / Phi-3.5 मॉडल का एकीकरण (कोड प्रथम दृष्टिकोण)

> [!NOTE]
> यदि आपने "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" में वर्णित लो-कोड दृष्टिकोण का पालन किया है, तो आप इस अभ्यास को छोड़कर अगले अभ्यास पर जा सकते हैं।
> हालाँकि, यदि आपने "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" में वर्णित कोड-प्रथम दृष्टिकोण का पालन करके अपना Phi-3 / Phi-3.5 मॉडल फाइन-ट्यून और तैनात किया है, तो Prompt flow से अपने मॉडल को कनेक्ट करने की प्रक्रिया थोड़ी अलग होगी। आप इस अभ्यास में यह प्रक्रिया सीखेंगे।

आगे बढ़ने के लिए, आपको अपने Fine-tuned Phi-3 / Phi-3.5 मॉडल को Microsoft Foundry में Prompt flow में एकीकृत करना होगा।

#### Microsoft Foundry Hub बनाएं

परियोजना बनाने से पहले आपको एक Hub बनाना होगा। एक Hub एक Resource Group की तरह कार्य करता है, जो आपको Microsoft Foundry के भीतर कई परियोजनाओं को व्यवस्थित और प्रबंधित करने की सुविधा देता है।
1. साइन इन करें [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) में।

1. बाईं ओर के टैब से **All hubs** चुनें।

1. नेविगेशन मेनू से **+ New hub** चुनें।

    ![Create hub.](../../../../../../translated_images/hi/create-hub.5be78fb1e21ffbf1.webp)

1. निम्नलिखित कार्य करें:

    - **Hub name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
    - अपना Azure **Subscription** चुनें।
    - उपयोग करने के लिए **Resource group** चुनें (यदि आवश्यक हो तो नया बनाएँ)।
    - अपनी पसंद का **Location** चुनें।
    - उपयोग करने के लिए **Connect Azure AI Services** चुनें (यदि आवश्यक हो तो नया बनाएँ)।
    - **Connect Azure AI Search** को **Skip connecting** पर सेट करें।

    ![Fill hub.](../../../../../../translated_images/hi/fill-hub.baaa108495c71e34.webp)

1. **Next** चुनें।

#### Microsoft Foundry प्रोजेक्ट बनाएं

1. आपने जो Hub बनाया है, उसमें बाईं ओर के टैब से **All projects** चुनें।

1. नेविगेशन मेनू से **+ New project** चुनें।

    ![Select new project.](../../../../../../translated_images/hi/select-new-project.cd31c0404088d7a3.webp)

1. **Project name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।

    ![Create project.](../../../../../../translated_images/hi/create-project.ca3b71298b90e420.webp)

1. **Create a project** चुनें।

#### फ़ाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल के लिए कस्टम कनेक्शन जोड़ें

अपने कस्टम Phi-3 / Phi-3.5 मॉडल को Prompt flow के साथ एकीकृत करने के लिए, आपको मॉडल के endpoint और key को एक कस्टम कनेक्शन में सहेजना होगा। यह सेटअप सुनिश्चित करता है कि Prompt flow में आपके कस्टम Phi-3 / Phi-3.5 मॉडल तक पहुंच हो।

#### फ़ाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल का api key और endpoint uri सेट करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएँ।

1. उस Azure Machine learning workspace पर जाएँ जिसे आपने बनाया है।

1. बाईं ओर के टैब से **Endpoints** चुनें।

    ![Select endpoints.](../../../../../../translated_images/hi/select-endpoints.ee7387ecd68bd18d.webp)

1. आपने जो endpoint बनाया है, उसे चुनें।

    ![Select endpoints.](../../../../../../translated_images/hi/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. नेविगेशन मेनू से **Consume** चुनें।

1. अपना **REST endpoint** और **Primary key** कॉपी करें।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/hi/copy-endpoint-key.0650c3786bd646ab.webp)

#### कस्टम कनेक्शन जोड़ें

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) पर जाएँ।

1. उस Microsoft Foundry प्रोजेक्ट पर जाएँ जिसे आपने बनाया है।

1. अपने बनाए गए प्रोजेक्ट में, बाईं ओर के टैब से **Settings** चुनें।

1. **+ New connection** चुनें।

    ![Select new connection.](../../../../../../translated_images/hi/select-new-connection.fa0f35743758a74b.webp)

1. नेविगेशन मेनू से **Custom keys** चुनें।

    ![Select custom keys.](../../../../../../translated_images/hi/select-custom-keys.5a3c6b25580a9b67.webp)

1. निम्न कार्य करें:

    - **+ Add key value pairs** चुनें।
    - key नाम के रूप में **endpoint** दर्ज करें और Azure ML Studio से कॉपी किया हुआ endpoint value फ़ील्ड में पेस्ट करें।
    - फिर से **+ Add key value pairs** चुनें।
    - key नाम के रूप में **key** दर्ज करें और Azure ML Studio से कॉपी किया हुआ key value फ़ील्ड में पेस्ट करें।
    - keys जोड़ने के बाद, key को एक्सपोज़ होने से रोकने के लिए **is secret** चुनें।

    ![Add connection.](../../../../../../translated_images/hi/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection** चुनें।

#### Prompt flow बनाएं

आपने Microsoft Foundry में कस्टम कनेक्शन जोड़ लिया है। अब, निम्न चरणों का उपयोग करके एक Prompt flow बनाएं। फिर, आप इस Prompt flow को कस्टम कनेक्शन से जोड़ेंगे ताकि आप Prompt flow के भीतर अपने फ़ाइन-ट्यून मॉडल का उपयोग कर सकें।

1. उस Microsoft Foundry प्रोजेक्ट पर जाएँ जिसे आपने बनाया है।

1. बाईं ओर के टैब से **Prompt flow** चुनें।

1. नेविगेशन मेनू से **+ Create** चुनें।

    ![Select Promptflow.](../../../../../../translated_images/hi/select-promptflow.18ff2e61ab9173eb.webp)

1. नेविगेशन मेनू से **Chat flow** चुनें।

    ![Select chat flow.](../../../../../../translated_images/hi/select-flow-type.28375125ec9996d3.webp)

1. उपयोग करने के लिए **Folder name** दर्ज करें।

    ![Select chat flow.](../../../../../../translated_images/hi/enter-name.02ddf8fb840ad430.webp)

1. **Create** चुनें।

#### अपने कस्टम Phi-3 / Phi-3.5 मॉडल के साथ चैट करने के लिए Prompt flow सेट करें

आपको फ़ाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल को Prompt flow में एकीकृत करना होगा। हालांकि, प्रदान किया गया मौजूदा Prompt flow इस उद्देश्य के लिए डिज़ाइन नहीं किया गया है। इसलिए, आपको कस्टम मॉडल के एकीकरण को सक्षम करने के लिए Prompt flow को पुनः डिज़ाइन करना होगा।

1. Prompt flow में, मौजूदा flow को फिर से बनाने के लिए निम्न कार्य करें:

    - **Raw file mode** चुनें।
    - *flow.dag.yml* फ़ाइल में सभी मौजूदा कोड को हटा दें।
    - *flow.dag.yml* में निम्न कोड जोड़ें।

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **Save** चुनें।

    ![Select raw file mode.](../../../../../../translated_images/hi/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Prompt flow में कस्टम Phi-3 / Phi-3.5 मॉडल का उपयोग करने के लिए *integrate_with_promptflow.py* में निम्न कोड जोड़ें।

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # लॉगिंग सेटअप
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" कस्टम कनेक्शन का नाम है, "endpoint", "key" कस्टम कनेक्शन की चाबियाँ हैं
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # पूर्ण JSON प्रतिक्रिया लॉग करें
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/hi/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry में Prompt flow का उपयोग करने के बारे में अधिक विस्तृत जानकारी के लिए, आप [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) देख सकते हैं।

1. अपने मॉडल के साथ चैट सक्षम करने के लिए **Chat input**, **Chat output** चुनें।

    ![Select Input Output.](../../../../../../translated_images/hi/select-input-output.c187fc58f25fbfc3.webp)

1. अब आप अपने कस्टम Phi-3 / Phi-3.5 मॉडल के साथ चैट करने के लिए तैयार हैं। अगले अभ्यास में, आप सीखेंगे कि Prompt flow कैसे शुरू करें और इसे अपने फ़ाइन-ट्यून किए हुए Phi-3 / Phi-3.5 मॉडल के साथ चैट के लिए कैसे उपयोग करें।

> [!NOTE]
>
> पुनर्निर्मित फ्लो नीचे दी गई छवि जैसा होना चाहिए:
>
> ![Flow example](../../../../../../translated_images/hi/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow शुरू करें

1. Prompt flow शुरू करने के लिए **Start compute sessions** चुनें।

    ![Start compute session.](../../../../../../translated_images/hi/start-compute-session.9acd8cbbd2c43df1.webp)

1. पैरामीटर अपडेट करने के लिए **Validate and parse input** चुनें।

    ![Validate input.](../../../../../../translated_images/hi/validate-input.c1adb9543c6495be.webp)

1. आपने जो कस्टम कनेक्शन बनाया है, उसकी **connection** वैल्यू चुनें। उदाहरण के लिए, *connection*।

    ![Connection.](../../../../../../translated_images/hi/select-connection.1f2b59222bcaafef.webp)

#### अपने कस्टम Phi-3 / Phi-3.5 मॉडल के साथ चैट करें

1. **Chat** चुनें।

    ![Select chat.](../../../../../../translated_images/hi/select-chat.0406bd9687d0c49d.webp)

1. यहाँ परिणामों का उदाहरण है: अब आप अपने कस्टम Phi-3 / Phi-3.5 मॉडल के साथ चैट कर सकते हैं। यह सुझाव दिया जाता है कि आप फाइन-ट्यूनिंग के लिए उपयोग किए गए डेटा के आधार पर प्रश्न पूछें।

    ![Chat with prompt flow.](../../../../../../translated_images/hi/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए Azure OpenAI तैनात करें

Microsoft Foundry में Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए, आपको एक Azure OpenAI मॉडल तैनात करना होगा। इस मॉडल का उपयोग Phi-3 / Phi-3.5 मॉडल के प्रदर्शन का मूल्यांकन करने के लिए किया जाएगा।

#### Azure OpenAI तैनात करें

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) में साइन इन करें।

1. उस Microsoft Foundry प्रोजेक्ट पर जाएँ जिसे आपने बनाया है।

    ![Select Project.](../../../../../../translated_images/hi/select-project-created.5221e0e403e2c9d6.webp)

1. अपने बनाए हुए प्रोजेक्ट में, बाईं ओर के टैब से **Deployments** चुनें।

1. नेविगेशन मेनू से **+ Deploy model** चुनें।

1. **Deploy base model** चुनें।

    ![Select Deployments.](../../../../../../translated_images/hi/deploy-openai-model.95d812346b25834b.webp)

1. उपयोग करने के लिए Azure OpenAI मॉडल चुनें। उदाहरण के लिए, **gpt-4o**।

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/hi/select-openai-model.959496d7e311546d.webp)

1. **Confirm** चुनें।

### Microsoft Foundry के Prompt flow मूल्यांकन का उपयोग करके फ़ाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें

### नया मूल्यांकन प्रारंभ करें

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) पर जाएँ।

1. उस Microsoft Foundry प्रोजेक्ट पर जाएँ जिसे आपने बनाया है।

    ![Select Project.](../../../../../../translated_images/hi/select-project-created.5221e0e403e2c9d6.webp)

1. अपने बनाए हुए प्रोजेक्ट में, बाईं ओर के टैब से **Evaluation** चुनें।

1. नेविगेशन मेनू से **+ New evaluation** चुनें।

    ![Select evaluation.](../../../../../../translated_images/hi/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** मूल्यांकन चुनें।

    ![Select Prompt flow evaluation.](../../../../../../translated_images/hi/promptflow-evaluation.cb9758cc19b4760f.webp)

1. निम्न कार्य करें:

    - मूल्यांकन नाम दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
    - कार्य प्रकार के रूप में **Question and answer without context** चुनें। क्योंकि इस ट्यूटोरियल में प्रयुक्त **UlTRACHAT_200k** डेटासेट में संदर्भ नहीं है।
    - उस prompt flow का चयन करें जिसे आप मूल्यांकन करना चाहते हैं।

    ![Prompt flow evaluation.](../../../../../../translated_images/hi/evaluation-setting1.4aa08259ff7a536e.webp)

1. **Next** चुनें।

1. निम्न कार्य करें:

    - **Add your dataset** चुनें और अपना डेटासेट अपलोड करें। उदाहरण के लिए, आप परीक्षण डेटासेट फ़ाइल जैसे *test_data.json1* अपलोड कर सकते हैं, जो **ULTRACHAT_200k** डेटासेट के साथ शामिल है।
    - अपने डेटासेट से मेल खाने वाला उचित **Dataset column** चुनें। उदाहरण के लिए, यदि आप **ULTRACHAT_200k** डेटासेट का उपयोग कर रहे हैं, तो **${data.prompt}** को डेटासेट कॉलम के रूप में चुनें।

    ![Prompt flow evaluation.](../../../../../../translated_images/hi/evaluation-setting2.07036831ba58d64e.webp)

1. **Next** चुनें।

1. प्रदर्शन और गुणवत्ता मेट्रिक्स कॉन्फ़िगर करने के लिए निम्न कार्य करें:

    - उपयोग करने के लिए प्रदर्शन और गुणवत्ता मेट्रिक्स चुनें।
    - मूल्यांकन के लिए आपने जो Azure OpenAI मॉडल बनाया है, उसे चुनें। उदाहरण के लिए, **gpt-4o**।

    ![Prompt flow evaluation.](../../../../../../translated_images/hi/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. जोखिम और सुरक्षा मेट्रिक्स कॉन्फ़िगर करने के लिए निम्न कार्य करें:

    - उपयोग करने के लिए जोखिम और सुरक्षा मेट्रिक्स चुनें।
    - दोष दर गणना के लिए थ्रेशोल्ड चुनें। उदाहरण के लिए, **Medium**।
    - **question** के लिए, **Data source** को **{$data.prompt}** पर सेट करें।
    - **answer** के लिए, **Data source** को **{$run.outputs.answer}** पर सेट करें।
    - **ground_truth** के लिए, **Data source** को **{$data.message}** पर सेट करें।

    ![Prompt flow evaluation.](../../../../../../translated_images/hi/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **Next** चुनें।

1. मूल्यांकन शुरू करने के लिए **Submit** चुनें।

1. मूल्यांकन पूरा होने में कुछ समय लगेगा। आप इसके प्रगति की निगरानी **Evaluation** टैब में कर सकते हैं।

### मूल्यांकन परिणामों की समीक्षा करें

> [!NOTE]
> नीचे प्रस्तुत परिणाम मूल्यांकन प्रक्रिया को स्पष्ट करने के लिए हैं। इस ट्यूटोरियल में, हमने अपेक्षाकृत छोटे डेटासेट पर फ़ाइन-ट्यून किए गए मॉडल का उपयोग किया है, जिससे उपयुक्त परिणाम नहीं भी मिल सकते हैं। वास्तविक परिणाम डेटासेट के आकार, गुणवत्ता और विविधता, साथ ही मॉडल की विशिष्ट कॉन्फ़िगरेशन पर काफी भिन्न हो सकते हैं।

मूल्यांकन पूरा होने के बाद, आप प्रदर्शन और सुरक्षा मेट्रिक्स दोनों के परिणामों की समीक्षा कर सकते हैं।
1. प्रदर्शन और गुणवत्ता मापदंड:

    - मॉडल की क्षमता का मूल्यांकन करें कि वह सुसंगत, प्रवाही, और संबंधित प्रतिक्रियाएं उत्पन्न करने में कितना प्रभावी है।

    ![Evaluation result.](../../../../../../translated_images/hi/evaluation-result-gpu.85f48b42dfb74254.webp)

1. जोखिम और सुरक्षा मापदंड:

    - सुनिश्चित करें कि मॉडल के आउटपुट सुरक्षित हैं और जिम्मेदार AI सिद्धांतों के अनुरूप हैं, जो किसी भी हानिकारक या अपमानजनक सामग्री से बचें।

    ![Evaluation result.](../../../../../../translated_images/hi/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. आप नीचे स्क्रॉल कर सकते हैं **विस्तृत मापदंड परिणाम** देखने के लिए।

    ![Evaluation result.](../../../../../../translated_images/hi/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. अपने कस्टम Phi-3 / Phi-3.5 मॉडल का प्रदर्शन और सुरक्षा मापदंड दोनों के खिलाफ मूल्यांकन करके, आप पुष्टि कर सकते हैं कि मॉडल न केवल प्रभावी है, बल्कि जिम्मेदार AI प्रथाओं का भी पालन करता है, जिससे यह वास्तविक दुनिया में उपयोग के लिए तैयार है।

## बधाई हो!

### आपने यह ट्यूटोरियल पूरा कर लिया है

आपने सफलतापूर्वक Microsoft Foundry में Prompt flow के साथ एकीकृत फाइन-ट्यून किए गए Phi-3 मॉडल का मूल्यांकन कर लिया है। यह एक महत्वपूर्ण कदम है यह सुनिश्चित करने के लिए कि आपके AI मॉडल न केवल अच्छा प्रदर्शन करते हैं, बल्कि Microsoft के जिम्मेदार AI सिद्धांतों का पालन भी करते हैं, जिससे आप भरोसेमंद और विश्वसनीय AI अनुप्रयोग बना सकें।

![Architecture.](../../../../../../translated_images/hi/architecture.10bec55250f5d6a4.webp)

## Azure संसाधनों की सफाई करें

अपने खाते में अतिरिक्त शुल्क से बचने के लिए अपने Azure संसाधनों को साफ करें। Azure पोर्टल पर जाएं और निम्नलिखित संसाधनों को हटाएं:

- Azure मशीन लर्निंग संसाधन।
- Azure मशीन लर्निंग मॉडल एंडपॉइंट।
- Microsoft Foundry प्रोजेक्ट संसाधन।
- Microsoft Foundry Prompt flow संसाधन।

### अगले कदम

#### दस्तावेज़ीकरण

- [जिम्मेदार AI डैशबोर्ड का उपयोग करके AI सिस्टम का मूल्यांकन करें](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [जनरेटिव AI के लिए मूल्यांकन और निगरानी मापदंड](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry दस्तावेज़ीकरण](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow दस्तावेज़ीकरण](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### प्रशिक्षण सामग्री

- [Microsoft के जिम्मेदार AI दृष्टिकोण का परिचय](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry का परिचय](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### संदर्भ

- [जिम्मेदार AI क्या है?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Azure AI में नए टूल का अनावरण जो आपकी मदद करते हैं अधिक सुरक्षित और विश्वसनीय जनरेटिव AI अनुप्रयोग बनाने में](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [जनरेटिव AI अनुप्रयोगों का मूल्यांकन](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या गलतियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->