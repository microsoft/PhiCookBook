<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76956c0c22e5686908a6d85ec72126af",
  "translation_date": "2025-04-04T17:12:12+00:00",
  "source_file": "code\\03.Finetuning\\olive-lab\\readme.md",
  "language_code": "hi"
}
-->
# लैब. ऑन-डिवाइस इन्फरेंस के लिए AI मॉडल्स को ऑप्टिमाइज़ करें

## परिचय 

> [!IMPORTANT]
> इस लैब के लिए **Nvidia A10 या A100 GPU** की आवश्यकता है, जिसके साथ संबंधित ड्राइवर्स और CUDA टूलकिट (संस्करण 12+) इंस्टॉल होना चाहिए।

> [!NOTE]
> यह एक **35 मिनट** का लैब है जो आपको OLIVE का उपयोग करके ऑन-डिवाइस इन्फरेंस के लिए मॉडल्स को ऑप्टिमाइज़ करने की मुख्य अवधारणाओं का व्यावहारिक परिचय देगा।

## सीखने के उद्देश्य

इस लैब के अंत तक, आप OLIVE का उपयोग करके निम्नलिखित कार्य कर पाएंगे:

- AWQ क्वांटाइज़ेशन विधि का उपयोग करके एक AI मॉडल को क्वांटाइज़ करें।
- किसी विशिष्ट कार्य के लिए AI मॉडल को फाइन-ट्यून करें।
- ONNX Runtime पर कुशल ऑन-डिवाइस इन्फरेंस के लिए LoRA एडाप्टर्स (फाइन-ट्यून किया गया मॉडल) जनरेट करें।

### Olive क्या है

Olive (*O*NNX *live*) एक मॉडल ऑप्टिमाइज़ेशन टूलकिट है जिसमें CLI शामिल है, जो आपको ONNX runtime +++https://onnxruntime.ai+++ के लिए मॉडल्स तैयार करने में मदद करता है।

![Olive Flow](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.hi.png)

Olive में इनपुट आमतौर पर PyTorch या Hugging Face मॉडल होता है और आउटपुट एक ऑप्टिमाइज़ किया गया ONNX मॉडल होता है, जिसे ONNX runtime चलाने वाले डिवाइस (डिप्लॉयमेंट टारगेट) पर निष्पादित किया जाता है। Olive मॉडल को हार्डवेयर वेंडर (जैसे Qualcomm, AMD, Nvidia, या Intel) द्वारा प्रदान किए गए डिप्लॉयमेंट टारगेट के AI एक्सेलेरेटर (NPU, GPU, CPU) के लिए ऑप्टिमाइज़ करता है।

Olive एक *workflow* को निष्पादित करता है, जो व्यक्तिगत मॉडल ऑप्टिमाइज़ेशन कार्यों की एक क्रमबद्ध श्रृंखला होती है जिसे *passes* कहा जाता है - उदाहरण के लिए: मॉडल कंप्रेशन, ग्राफ कैप्चर, क्वांटाइज़ेशन, ग्राफ ऑप्टिमाइज़ेशन। प्रत्येक पास में ऐसे पैरामीटर होते हैं जिन्हें सर्वश्रेष्ठ मेट्रिक्स (जैसे सटीकता और विलंबता) प्राप्त करने के लिए ट्यून किया जा सकता है। Olive एक सर्च रणनीति का उपयोग करता है जो एक-एक पास या पास के सेट को ऑटो-ट्यून करता है।

#### Olive के लाभ

- **परीक्षण-त्रुटि वाले मैनुअल प्रयोग में लगने वाले समय और झंझट को कम करें।** अपनी गुणवत्ता और प्रदर्शन सीमाएं परिभाषित करें और Olive को आपके लिए सर्वश्रेष्ठ मॉडल खोजने दें।
- **40+ इन-बिल्ट मॉडल ऑप्टिमाइज़ेशन घटक** जो क्वांटाइज़ेशन, कंप्रेशन, ग्राफ ऑप्टिमाइज़ेशन और फाइन-ट्यूनिंग में अत्याधुनिक तकनीकों को कवर करते हैं।
- सामान्य मॉडल ऑप्टिमाइज़ेशन कार्यों के लिए **आसान-से-उपयोग CLI**। उदाहरण: olive quantize, olive auto-opt, olive finetune।
- मॉडल पैकेजिंग और डिप्लॉयमेंट इन-बिल्ट।
- **मल्टी LoRA सर्विंग** के लिए मॉडल जनरेट करने का समर्थन करता है।
- YAML/JSON का उपयोग करके वर्कफ़्लो बनाएं ताकि मॉडल ऑप्टिमाइज़ेशन और डिप्लॉयमेंट कार्यों को ऑर्केस्ट्रेट किया जा सके।
- **Hugging Face** और **Azure AI** इंटीग्रेशन।
- लागत बचाने के लिए इन-बिल्ट **कैशिंग** तंत्र।

## लैब निर्देश
> [!NOTE]
> कृपया सुनिश्चित करें कि आपने Azure AI Hub और प्रोजेक्ट को प्रोविजन कर लिया है और Lab 1 के अनुसार अपना A100 कंप्यूट सेटअप कर लिया है।

### स्टेप 0: अपने Azure AI Compute से कनेक्ट करें

आप **VS Code** में रिमोट फीचर का उपयोग करके Azure AI Compute से कनेक्ट करेंगे।

1. अपने **VS Code** डेस्कटॉप एप्लिकेशन को खोलें:
1. **Shift+Ctrl+P** का उपयोग करके **कमांड पैलेट** खोलें।
1. कमांड पैलेट में **AzureML - remote: Connect to compute instance in New Window** खोजें।
1. Compute से कनेक्ट करने के लिए ऑन-स्क्रीन निर्देशों का पालन करें। इसमें आपके Azure Subscription, Resource Group, Project और Compute नाम का चयन करना शामिल होगा जिसे आपने Lab 1 में सेटअप किया था।
1. एक बार जब आप Azure ML Compute नोड से कनेक्ट हो जाते हैं, तो यह **Visual Code के नीचे बाएं कोने में** प्रदर्शित होगा `><Azure ML: Compute Name`

### स्टेप 1: इस रिपॉजिटरी को क्लोन करें

VS Code में, आप **Ctrl+J** का उपयोग करके एक नया टर्मिनल खोल सकते हैं और इस रिपॉजिटरी को क्लोन कर सकते हैं:

टर्मिनल में आपको निम्नलिखित प्रॉम्प्ट दिखाई देगा:

```
azureuser@computername:~/cloudfiles/code$ 
```
सॉल्यूशन को क्लोन करें 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### स्टेप 2: VS Code में फ़ोल्डर खोलें

संबंधित फ़ोल्डर में VS Code खोलने के लिए, टर्मिनल में निम्नलिखित कमांड निष्पादित करें, जो एक नई विंडो खोलेगा:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

वैकल्पिक रूप से, आप **File** > **Open Folder** का चयन करके फ़ोल्डर खोल सकते हैं।

### स्टेप 3: डिपेंडेंसीज़

Azure AI Compute Instance में VS Code में एक टर्मिनल विंडो खोलें (टिप: **Ctrl+J**) और डिपेंडेंसीज़ इंस्टॉल करने के लिए निम्नलिखित कमांड्स निष्पादित करें:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> सभी डिपेंडेंसीज़ इंस्टॉल होने में ~5 मिनट लगेंगे।

इस लैब में आप मॉडल्स को Azure AI Model कैटलॉग में डाउनलोड और अपलोड करेंगे। ताकि आप मॉडल कैटलॉग तक पहुंच सकें, आपको Azure में लॉगिन करना होगा:

```bash
az login
```

> [!NOTE]
> लॉगिन करते समय आपको अपना सब्सक्रिप्शन चुनने के लिए कहा जाएगा। सुनिश्चित करें कि आपने इस लैब के लिए प्रदान किए गए सब्सक्रिप्शन को सेट किया है।

### स्टेप 4: Olive कमांड्स निष्पादित करें 

Azure AI Compute Instance में VS Code में एक टर्मिनल विंडो खोलें (टिप: **Ctrl+J**) और सुनिश्चित करें कि `olive-ai` कोंडा एनवायरनमेंट सक्रिय है:

```bash
conda activate olive-ai
```

अब, कमांड लाइन में निम्नलिखित Olive कमांड्स निष्पादित करें।

1. **डेटा का निरीक्षण करें:** इस उदाहरण में, आप Phi-3.5-Mini मॉडल को फाइन-ट्यून करेंगे ताकि यह यात्रा संबंधित प्रश्नों का उत्तर देने में विशेषज्ञता प्राप्त कर सके। नीचे दिया गया कोड डेटासेट के पहले कुछ रिकॉर्ड्स प्रदर्शित करता है, जो JSON लाइन्स फॉर्मेट में हैं:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **मॉडल को क्वांटाइज़ करें:** मॉडल को ट्रेन करने से पहले, आप निम्नलिखित कमांड का उपयोग करके Active Aware Quantization (AWQ) तकनीक के साथ इसे क्वांटाइज़ करेंगे +++https://arxiv.org/abs/2306.00978+++। AWQ मॉडल के वज़न को इन्फरेंस के दौरान उत्पन्न एक्टिवेशन्स को ध्यान में रखकर क्वांटाइज़ करता है। इसका मतलब है कि क्वांटाइज़ेशन प्रक्रिया एक्टिवेशन्स में वास्तविक डेटा वितरण को ध्यान में रखती है, जिससे पारंपरिक वज़न क्वांटाइज़ेशन विधियों की तुलना में मॉडल की सटीकता बेहतर बनी रहती है।

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ क्वांटाइज़ेशन को पूरा होने में **~8 मिनट** लगते हैं, जो **मॉडल का आकार ~7.5GB से ~2.5GB तक कम कर देता है**।

    इस लैब में, हम आपको Hugging Face से मॉडल्स इनपुट करने का तरीका दिखा रहे हैं (उदाहरण: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` कमांड क्वांटाइज़ किए गए मॉडल को फाइन-ट्यून करता है। मॉडल को *क्वांटाइज़ करने के बाद* फाइन-ट्यून करने की बजाय *पहले* क्वांटाइज़ करना बेहतर सटीकता देता है क्योंकि फाइन-ट्यूनिंग प्रक्रिया क्वांटाइज़ेशन से होने वाले कुछ नुकसान की भरपाई करती है।

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    फाइन-ट्यूनिंग (100 स्टेप्स के साथ) को पूरा होने में **~6 मिनट** लगते हैं।

1. **ऑप्टिमाइज़ करें:** मॉडल को ट्रेन करने के बाद, अब आप Olive के `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` आर्गुमेंट्स का उपयोग करके मॉडल को ऑप्टिमाइज़ करेंगे - लेकिन इस लैब के लिए हम CPU का उपयोग करेंगे।

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    ऑप्टिमाइज़ेशन को पूरा होने में **~5 मिनट** लगते हैं।

### स्टेप 5: मॉडल इन्फरेंस का त्वरित परीक्षण

मॉडल का इन्फरेंस परीक्षण करने के लिए, अपने फ़ोल्डर में एक Python फ़ाइल **app.py** नामक बनाएं और निम्नलिखित कोड कॉपी-पेस्ट करें:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

कोड को निष्पादित करें:

```bash
python app.py
```

### स्टेप 6: मॉडल को Azure AI पर अपलोड करें

मॉडल को Azure AI मॉडल रिपॉजिटरी में अपलोड करने से यह आपकी डेवलपमेंट टीम के अन्य सदस्यों के साथ साझा करने योग्य बन जाता है और मॉडल का संस्करण नियंत्रण भी संभालता है। मॉडल को अपलोड करने के लिए निम्नलिखित कमांड चलाएं:

> [!NOTE]
> `{}`` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group ` में `resourceGroup` और Azure AI प्रोजेक्ट नाम अपडेट करें और निम्नलिखित कमांड चलाएं 

```
az ml workspace show
```

या +++ai.azure.com+++ पर जाकर **management center** > **project** > **overview** चुनें।

`{}` प्लेसहोल्डर्स को अपने रिसोर्स ग्रुप और Azure AI प्रोजेक्ट नाम से अपडेट करें।

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
आप अपने अपलोड किए गए मॉडल को देख सकते हैं और https://ml.azure.com/model/list पर मॉडल को डिप्लॉय कर सकते हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद का उपयोग करने से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।