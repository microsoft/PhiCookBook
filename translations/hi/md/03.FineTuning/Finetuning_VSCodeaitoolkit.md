<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:05:58+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "hi"
}
-->
## VS Code के लिए AI Toolkit में आपका स्वागत है

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) Azure AI Studio Catalog और Hugging Face जैसे अन्य कैटलॉग से विभिन्न मॉडल को एक साथ लाता है। यह टूलकिट जनरेटिव AI टूल्स और मॉडलों के साथ AI ऐप्स बनाने के सामान्य विकास कार्यों को सरल बनाता है, जैसे:
- मॉडल खोज और प्लेग्राउंड से शुरुआत करें।
- स्थानीय कंप्यूटिंग संसाधनों का उपयोग करके मॉडल फाइन-ट्यूनिंग और इनफेरेंस।
- Azure संसाधनों का उपयोग करके रिमोट फाइन-ट्यूनिंग और इनफेरेंस।

[VSCode के लिए AI Toolkit इंस्टॉल करें](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.7157953df04812dc.hi.png)

**[Private Preview]** Azure Container Apps के लिए वन-क्लिक प्रोविजनिंग, जिससे क्लाउड में मॉडल फाइन-ट्यूनिंग और इनफेरेंस चलाया जा सके।

अब चलिए आपके AI ऐप विकास में आगे बढ़ते हैं:

- [VS Code के लिए AI Toolkit में आपका स्वागत है](../../../../md/03.FineTuning)
- [स्थानीय विकास](../../../../md/03.FineTuning)
  - [तैयारी](../../../../md/03.FineTuning)
  - [Conda सक्रिय करें](../../../../md/03.FineTuning)
  - [केवल बेस मॉडल फाइन-ट्यूनिंग](../../../../md/03.FineTuning)
  - [मॉडल फाइन-ट्यूनिंग और इनफेरेंस](../../../../md/03.FineTuning)
  - [मॉडल फाइन-ट्यूनिंग](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [फाइन-ट्यूनिंग के नमूने और संसाधन](../../../../md/03.FineTuning)
- [**\[Private Preview\]** रिमोट विकास](../../../../md/03.FineTuning)
  - [पूर्वापेक्षाएँ](../../../../md/03.FineTuning)
  - [रिमोट विकास प्रोजेक्ट सेटअप](../../../../md/03.FineTuning)
  - [Azure संसाधनों का प्रोविजन करें](../../../../md/03.FineTuning)
  - [\[वैकल्पिक\] Azure Container App Secret में Huggingface टोकन जोड़ें](../../../../md/03.FineTuning)
  - [फाइन-ट्यूनिंग चलाएं](../../../../md/03.FineTuning)
  - [इनफेरेंस एंडपॉइंट प्रोविजन करें](../../../../md/03.FineTuning)
  - [इनफेरेंस एंडपॉइंट डिप्लॉय करें](../../../../md/03.FineTuning)
  - [उन्नत उपयोग](../../../../md/03.FineTuning)

## स्थानीय विकास
### तैयारी

1. सुनिश्चित करें कि होस्ट में NVIDIA ड्राइवर इंस्टॉल है।
2. यदि आप HF का उपयोग कर रहे हैं तो `huggingface-cli login` चलाएं।
3. `Olive` की सेटिंग्स मेमोरी उपयोग को प्रभावित करने वाले किसी भी बदलाव के लिए व्याख्या करें।

### Conda सक्रिय करें
चूंकि हम WSL वातावरण का उपयोग कर रहे हैं और यह साझा है, इसलिए आपको मैन्युअली conda वातावरण को सक्रिय करना होगा। इस चरण के बाद आप फाइन-ट्यूनिंग या इनफेरेंस चला सकते हैं।

```bash
conda activate [conda-env-name] 
```

### केवल बेस मॉडल फाइन-ट्यूनिंग
यदि आप बिना फाइन-ट्यूनिंग के केवल बेस मॉडल आज़माना चाहते हैं, तो conda सक्रिय करने के बाद यह कमांड चलाएं।

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### मॉडल फाइन-ट्यूनिंग और इनफेरेंस

जब वर्कस्पेस एक dev कंटेनर में खुल जाए, तो टर्मिनल खोलें (डिफ़ॉल्ट पथ प्रोजेक्ट रूट है), फिर नीचे दिया गया कमांड चलाकर चयनित डेटासेट पर LLM को फाइन-ट्यून करें।

```bash
python finetuning/invoke_olive.py 
```

चेकपॉइंट और अंतिम मॉडल `models` फ़ोल्डर में सेव होंगे।

फिर फाइन-ट्यून किए गए मॉडल के साथ `console`, `web browser` या `prompt flow` में चैट के माध्यम से इनफेरेंस चलाएं।

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

VS Code में `prompt flow` का उपयोग करने के लिए, कृपया इस [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html) को देखें।

### मॉडल फाइन-ट्यूनिंग

इसके बाद, अपने डिवाइस पर GPU उपलब्धता के आधार पर निम्नलिखित मॉडल डाउनलोड करें।

QLoRA का उपयोग करके स्थानीय फाइन-ट्यूनिंग सत्र शुरू करने के लिए, हमारे कैटलॉग से वह मॉडल चुनें जिसे आप फाइन-ट्यून करना चाहते हैं।
| प्लेटफ़ॉर्म | GPU उपलब्ध | मॉडल नाम | आकार (GB) |
|---------|---------|--------|--------|
| Windows | हाँ | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | हाँ | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | नहीं | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_नोट_** मॉडल डाउनलोड करने के लिए आपको Azure अकाउंट की आवश्यकता नहीं है।

Phi3-mini (int4) मॉडल का आकार लगभग 2GB-3GB है। आपके नेटवर्क की गति के अनुसार डाउनलोड में कुछ मिनट लग सकते हैं।

सबसे पहले प्रोजेक्ट का नाम और स्थान चुनें।
फिर मॉडल कैटलॉग से एक मॉडल चुनें। आपको प्रोजेक्ट टेम्पलेट डाउनलोड करने के लिए कहा जाएगा। इसके बाद आप "Configure Project" पर क्लिक करके विभिन्न सेटिंग्स समायोजित कर सकते हैं।

### Microsoft Olive

हम [Olive](https://microsoft.github.io/Olive/why-olive.html) का उपयोग PyTorch मॉडल पर QLoRA फाइन-ट्यूनिंग चलाने के लिए करते हैं। सभी सेटिंग्स डिफ़ॉल्ट मानों के साथ पहले से सेट होती हैं ताकि फाइन-ट्यूनिंग प्रक्रिया स्थानीय रूप से मेमोरी के अनुकूल तरीके से चले, लेकिन इन्हें आपकी स्थिति के अनुसार समायोजित किया जा सकता है।

### फाइन-ट्यूनिंग के नमूने और संसाधन

- [फाइन-ट्यूनिंग शुरू करने की गाइड](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [HuggingFace Dataset के साथ फाइन-ट्यूनिंग](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [सरल Dataset के साथ फाइन-ट्यूनिंग](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** रिमोट विकास

### पूर्वापेक्षाएँ

1. अपने रिमोट Azure Container App वातावरण में मॉडल फाइन-ट्यूनिंग चलाने के लिए, सुनिश्चित करें कि आपकी सब्सक्रिप्शन में पर्याप्त GPU क्षमता हो। अपनी एप्लिकेशन के लिए आवश्यक क्षमता का अनुरोध करने हेतु [सपोर्ट टिकट](https://azure.microsoft.com/support/create-ticket/) सबमिट करें। [GPU क्षमता के बारे में अधिक जानकारी](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. यदि आप HuggingFace पर प्राइवेट डेटासेट का उपयोग कर रहे हैं, तो सुनिश्चित करें कि आपके पास [HuggingFace अकाउंट](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) है और आपने [एक्सेस टोकन जनरेट](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo) किया है।
3. AI Toolkit for VS Code में Remote Fine-tuning और Inference फीचर फ्लैग सक्षम करें:
   1. VS Code सेटिंग्स खोलें: *File -> Preferences -> Settings*।
   2. *Extensions* में जाएं और *AI Toolkit* चुनें।
   3. *"Enable Remote Fine-tuning And Inference"* विकल्प चुनें।
   4. प्रभावी होने के लिए VS Code को रीलोड करें।

- [रिमोट फाइन-ट्यूनिंग](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### रिमोट विकास प्रोजेक्ट सेटअप
1. कमांड पैलेट में `AI Toolkit: Focus on Resource View` चलाएं।
2. *Model Fine-tuning* पर जाएं और मॉडल कैटलॉग एक्सेस करें। अपने प्रोजेक्ट का नाम और मशीन पर स्थान चुनें। फिर *"Configure Project"* बटन दबाएं।
3. प्रोजेक्ट कॉन्फ़िगरेशन
    1. *"Fine-tune locally"* विकल्प को सक्षम न करें।
    2. Olive कॉन्फ़िगरेशन सेटिंग्स डिफ़ॉल्ट मानों के साथ दिखेंगी। आवश्यकतानुसार इन्हें समायोजित और भरें।
    3. *Generate Project* पर जाएं। यह चरण WSL का उपयोग करता है और एक नया Conda वातावरण सेटअप करता है, भविष्य में Dev Containers के लिए तैयारी करता है।
4. *"Relaunch Window In Workspace"* पर क्लिक करें ताकि आपका रिमोट विकास प्रोजेक्ट खुल जाए।

> **नोट:** यह प्रोजेक्ट वर्तमान में AI Toolkit for VS Code में या तो स्थानीय या रिमोट रूप से काम करता है। यदि आप प्रोजेक्ट निर्माण के दौरान *"Fine-tune locally"* चुनते हैं, तो यह केवल WSL में चलेगा और रिमोट विकास सक्षम नहीं होगा। यदि आप इसे सक्षम नहीं करते, तो प्रोजेक्ट केवल रिमोट Azure Container App वातावरण तक सीमित रहेगा।

### Azure संसाधनों का प्रोविजन करें
शुरू करने के लिए, रिमोट फाइन-ट्यूनिंग के लिए Azure संसाधन प्रोविजन करें। इसके लिए कमांड पैलेट से `AI Toolkit: Provision Azure Container Apps job for fine-tuning` चलाएं।

प्रोविजन की प्रगति को आउटपुट चैनल में दिखाए गए लिंक के माध्यम से मॉनिटर करें।

### [वैकल्पिक] Azure Container App Secret में Huggingface टोकन जोड़ें
यदि आप प्राइवेट HuggingFace डेटासेट का उपयोग कर रहे हैं, तो HuggingFace टोकन को एक पर्यावरण चर के रूप में सेट करें ताकि Hugging Face Hub पर मैन्युअल लॉगिन की आवश्यकता न हो।
यह आप `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning` कमांड के जरिए कर सकते हैं। इस कमांड में आप सीक्रेट का नाम [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) रख सकते हैं और अपने Hugging Face टोकन को सीक्रेट वैल्यू के रूप में उपयोग कर सकते हैं।

### फाइन-ट्यूनिंग चलाएं
रिमोट फाइन-ट्यूनिंग जॉब शुरू करने के लिए, `AI Toolkit: Run fine-tuning` कमांड चलाएं।

सिस्टम और कंसोल लॉग देखने के लिए, आप आउटपुट पैनल में दिए लिंक से Azure पोर्टल पर जा सकते हैं ([Azure पर लॉग देखें और क्वेरी करें](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure))। या, आप VSCode आउटपुट पैनल में सीधे `AI Toolkit: Show the running fine-tuning job streaming logs` कमांड चलाकर कंसोल लॉग देख सकते हैं।  
> **नोट:** संसाधनों की कमी के कारण जॉब कतार में हो सकता है। यदि लॉग नहीं दिख रहा है, तो `AI Toolkit: Show the running fine-tuning job streaming logs` कमांड चलाएं, कुछ समय प्रतीक्षा करें और फिर से कमांड चलाएं ताकि स्ट्रीमिंग लॉग से पुनः कनेक्ट हो सके।

इस प्रक्रिया के दौरान, QLoRA का उपयोग फाइन-ट्यूनिंग के लिए किया जाएगा, और मॉडल के लिए LoRA एडाप्टर बनाए जाएंगे जो इनफेरेंस के दौरान उपयोग होंगे।  
फाइन-ट्यूनिंग के परिणाम Azure Files में संग्रहित होंगे।

### इनफेरेंस एंडपॉइंट प्रोविजन करें
रिमोट वातावरण में एडाप्टर ट्रेन हो जाने के बाद, मॉडल के साथ इंटरैक्ट करने के लिए एक सरल Gradio एप्लिकेशन का उपयोग करें।  
फाइन-ट्यूनिंग प्रक्रिया की तरह, रिमोट इनफेरेंस के लिए Azure संसाधन सेटअप करने हेतु कमांड पैलेट से `AI Toolkit: Provision Azure Container Apps for inference` चलाएं।

डिफ़ॉल्ट रूप से, सब्सक्रिप्शन और रिसोर्स ग्रुप फाइन-ट्यूनिंग में उपयोग किए गए समान होने चाहिए। इनफेरेंस उसी Azure Container App Environment का उपयोग करेगा और Azure Files में संग्रहित मॉडल और मॉडल एडाप्टर तक पहुंच बनाएगा, जो फाइन-ट्यूनिंग चरण के दौरान बनाए गए थे।

### इनफेरेंस एंडपॉइंट डिप्लॉय करें
यदि आप इनफेरेंस कोड संशोधित करना चाहते हैं या इनफेरेंस मॉडल को पुनः लोड करना चाहते हैं, तो `AI Toolkit: Deploy for inference` कमांड चलाएं। यह आपके नवीनतम कोड को Azure Container App के साथ सिंक्रनाइज़ करेगा और रिप्लिका को पुनः शुरू करेगा।

डिप्लॉयमेंट सफलतापूर्वक पूरा होने के बाद, आप VSCode नोटिफिकेशन में दिख रहे "*Go to Inference Endpoint*" बटन पर क्लिक करके इनफेरेंस API तक पहुंच सकते हैं।  
या, वेब API एंडपॉइंट `ACA_APP_ENDPOINT` के अंतर्गत `./infra/inference.config.json` और आउटपुट पैनल में पाया जा सकता है। अब आप इस एंडपॉइंट का उपयोग करके मॉडल का मूल्यांकन कर सकते हैं।

### उन्नत उपयोग
AI Toolkit के साथ रिमोट विकास के बारे में अधिक जानकारी के लिए, कृपया [रिमोट फाइन-ट्यूनिंग मॉडल](https://aka.ms/ai-toolkit/remote-provision) और [फाइन-ट्यून किए गए मॉडल के साथ इनफेरेंस](https://aka.ms/ai-toolkit/remote-inference) दस्तावेज़ देखें।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।