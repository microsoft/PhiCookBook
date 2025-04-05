<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76956c0c22e5686908a6d85ec72126af",
  "translation_date": "2025-04-04T19:13:20+00:00",
  "source_file": "md\\03.FineTuning\\olive-lab\\readme.md",
  "language_code": "hi"
}
-->
# लैब. ऑन-डिवाइस इन्फरेंस के लिए AI मॉडल को ऑप्टिमाइज़ करें

## परिचय 

> [!IMPORTANT]
> इस लैब के लिए **Nvidia A10 या A100 GPU** की आवश्यकता है, जिसमें संबंधित ड्राइवर और CUDA टूलकिट (संस्करण 12+) इंस्टॉल हो।

> [!NOTE]
> यह एक **35 मिनट** का लैब है जो आपको OLIVE का उपयोग करके ऑन-डिवाइस इन्फरेंस के लिए मॉडल को ऑप्टिमाइज़ करने की मुख्य अवधारणाओं का व्यावहारिक परिचय देगा।

## सीखने के उद्देश्य

इस लैब के अंत तक, आप OLIVE का उपयोग करके निम्नलिखित करने में सक्षम होंगे:

- AWQ क्वांटाइज़ेशन विधि का उपयोग करके AI मॉडल को क्वांटाइज़ करें।
- किसी विशेष कार्य के लिए AI मॉडल को फाइन-ट्यून करें।
- ONNX Runtime पर प्रभावी ऑन-डिवाइस इन्फरेंस के लिए LoRA एडॉप्टर (फाइन-ट्यून किया गया मॉडल) जनरेट करें।

### Olive क्या है

Olive (*O*NNX *live*) एक मॉडल ऑप्टिमाइज़ेशन टूलकिट है जिसमें CLI भी शामिल है, जो आपको ONNX runtime +++https://onnxruntime.ai+++ के लिए मॉडल शिप करने में सक्षम बनाता है।

![Olive Flow](../../../../../translated_images/olive-flow.9e6a284c256068568eb569a242b22dd2e7ec6e73f292d98272398739537ef513.hi.png)

Olive का इनपुट आमतौर पर PyTorch या Hugging Face मॉडल होता है और आउटपुट एक ऑप्टिमाइज़ किया गया ONNX मॉडल होता है जिसे ONNX runtime चलाने वाले डिवाइस (डिप्लॉयमेंट टारगेट) पर निष्पादित किया जाता है। Olive मॉडल को डिप्लॉयमेंट टारगेट के AI एक्सेलेरेटर (NPU, GPU, CPU) के लिए ऑप्टिमाइज़ करता है, जिसे Qualcomm, AMD, Nvidia या Intel जैसे हार्डवेयर विक्रेताओं द्वारा प्रदान किया जाता है।

Olive एक *workflow* को निष्पादित करता है, जो व्यक्तिगत मॉडल ऑप्टिमाइज़ेशन टास्क का क्रमबद्ध अनुक्रम होता है जिसे *passes* कहा जाता है - उदाहरण के लिए: मॉडल कंप्रेशन, ग्राफ कैप्चर, क्वांटाइज़ेशन, ग्राफ ऑप्टिमाइज़ेशन। प्रत्येक पास में ऐसे पैरामीटर होते हैं जिन्हें सर्वश्रेष्ठ मेट्रिक्स, जैसे कि सटीकता और विलंबता, प्राप्त करने के लिए ट्यून किया जा सकता है। Olive एक सर्च स्ट्रेटेजी का उपयोग करता है जो प्रत्येक पास को एक-एक करके या पास के सेट को एक साथ ऑटो-ट्यून करता है।

#### Olive के लाभ

- ग्राफ ऑप्टिमाइज़ेशन, कंप्रेशन और क्वांटाइज़ेशन के लिए विभिन्न तकनीकों के साथ ट्रायल-एंड-एरर मैनुअल प्रयोग के **समय और झुंझलाहट को कम करें**। अपनी गुणवत्ता और प्रदर्शन सीमाएं परिभाषित करें और Olive को आपके लिए सर्वश्रेष्ठ मॉडल खोजने दें।
- **40+ बिल्ट-इन मॉडल ऑप्टिमाइज़ेशन कंपोनेंट्स** जो क्वांटाइज़ेशन, कंप्रेशन, ग्राफ ऑप्टिमाइज़ेशन और फाइन-ट्यूनिंग में नवीनतम तकनीकों को कवर करते हैं।
- **आसान CLI** सामान्य मॉडल ऑप्टिमाइज़ेशन टास्क के लिए। उदाहरण: olive quantize, olive auto-opt, olive finetune।
- मॉडल पैकेजिंग और डिप्लॉयमेंट बिल्ट-इन।
- **मल्टी LoRA सर्विंग** के लिए मॉडल जनरेट करने का समर्थन।
- YAML/JSON का उपयोग करके वर्कफ़्लो बनाएं ताकि मॉडल ऑप्टिमाइज़ेशन और डिप्लॉयमेंट टास्क को व्यवस्थित किया जा सके।
- **Hugging Face** और **Azure AI** इंटीग्रेशन।
- **कैशिंग** तंत्र बिल्ट-इन ताकि **खर्च बचाया जा सके।**

## लैब निर्देश
> [!NOTE]
> कृपया सुनिश्चित करें कि आपने अपना Azure AI Hub और प्रोजेक्ट प्रोविजन किया है और Lab 1 के अनुसार अपना A100 कंप्यूट सेटअप किया है।

### स्टेप 0: अपने Azure AI Compute से कनेक्ट करें

आप **VS Code** में रिमोट फीचर का उपयोग करके Azure AI Compute से कनेक्ट करेंगे।

1. अपनी **VS Code** डेस्कटॉप एप्लिकेशन खोलें:
1. **Shift+Ctrl+P** का उपयोग करके **कमांड पैलेट** खोलें।
1. कमांड पैलेट में **AzureML - remote: Connect to compute instance in New Window** खोजें।
1. Compute से कनेक्ट करने के लिए ऑन-स्क्रीन निर्देशों का पालन करें। इसमें आपका Azure Subscription, Resource Group, Project और Compute नाम चुनना शामिल होगा जिसे आपने Lab 1 में सेट किया था।
1. एक बार जब आप अपने Azure ML Compute node से कनेक्ट हो जाते हैं, तो यह **Visual Code के नीचे बाएं** में प्रदर्शित होगा `><Azure ML: Compute Name`

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

संबंधित फ़ोल्डर में VS Code खोलने के लिए टर्मिनल में निम्नलिखित कमांड निष्पादित करें, जो एक नई विंडो खोलेगा:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

वैकल्पिक रूप से, आप **File** > **Open Folder** का चयन करके फ़ोल्डर खोल सकते हैं।

### स्टेप 3: डिपेंडेंसीज़

Azure AI Compute Instance में VS Code में एक टर्मिनल विंडो खोलें (टिप: **Ctrl+J**) और डिपेंडेंसीज़ इंस्टॉल करने के लिए निम्नलिखित कमांड निष्पादित करें:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> सभी डिपेंडेंसीज़ इंस्टॉल करने में ~5 मिनट लगेंगे।

इस लैब में आप Azure AI Model catalog में मॉडल को डाउनलोड और अपलोड करेंगे। मॉडल कैटलॉग तक पहुंचने के लिए, आपको Azure में लॉगिन करना होगा:

```bash
az login
```

> [!NOTE]
> लॉगिन के समय आपको अपनी सब्सक्रिप्शन चुनने के लिए कहा जाएगा। सुनिश्चित करें कि आप इस लैब के लिए प्रदान की गई सब्सक्रिप्शन सेट करें।

### स्टेप 4: Olive कमांड्स निष्पादित करें

Azure AI Compute Instance में VS Code में एक टर्मिनल विंडो खोलें (टिप: **Ctrl+J**) और सुनिश्चित करें कि `olive-ai` कोंडा एनवायरनमेंट सक्रिय है:

```bash
conda activate olive-ai
```

इसके बाद, निम्नलिखित Olive कमांड्स को कमांड लाइन में निष्पादित करें।

1. **डेटा का निरीक्षण करें:** इस उदाहरण में, आप Phi-3.5-Mini मॉडल को फाइन-ट्यून करेंगे ताकि यह यात्रा संबंधित सवालों का जवाब देने में विशेषज्ञ हो। नीचे दिया गया कोड डेटासेट के पहले कुछ रिकॉर्ड प्रदर्शित करता है, जो JSON लाइन्स फॉर्मेट में हैं:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **मॉडल को क्वांटाइज़ करें:** मॉडल को ट्रेन करने से पहले, आप निम्नलिखित कमांड का उपयोग करके इसे क्वांटाइज़ करते हैं, जो Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ नामक तकनीक का उपयोग करता है। AWQ मॉडल के वज़न को क्वांटाइज़ करता है, लेकिन इन्फरेंस के दौरान उत्पन्न होने वाले एक्टिवेशन को ध्यान में रखता है। इसका मतलब है कि क्वांटाइज़ेशन प्रक्रिया एक्टिवेशन में वास्तविक डेटा वितरण को ध्यान में रखती है, जिससे पारंपरिक वज़न क्वांटाइज़ेशन विधियों की तुलना में मॉडल सटीकता बेहतर होती है।

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ क्वांटाइज़ेशन पूरा होने में **~8 मिनट** लगते हैं, जो **मॉडल का आकार ~7.5GB से ~2.5GB तक कम करता है**।
   
   इस लैब में, हम आपको Hugging Face से मॉडल इनपुट करने का तरीका दिखा रहे हैं (उदाहरण: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` कमांड क्वांटाइज़ किए गए मॉडल को फाइन-ट्यून करता है। मॉडल को *पहले* क्वांटाइज़ करना और फिर फाइन-ट्यून करना बेहतर सटीकता देता है क्योंकि फाइन-ट्यूनिंग प्रक्रिया क्वांटाइज़ेशन से होने वाले कुछ नुकसान को रिकवर करती है।

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
    
    फाइन-ट्यूनिंग (100 स्टेप्स के साथ) पूरा होने में **~6 मिनट** लगते हैं।

1. **ऑप्टिमाइज़ करें:** मॉडल को ट्रेन करने के बाद, आप Olive के `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` आर्ग्युमेंट्स का उपयोग करके मॉडल को ऑप्टिमाइज़ करते हैं - लेकिन इस लैब के उद्देश्य के लिए हम CPU का उपयोग करेंगे।

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
    
    ऑप्टिमाइज़ेशन पूरा होने में **~5 मिनट** लगते हैं।

### स्टेप 5: मॉडल इन्फरेंस का त्वरित परीक्षण

मॉडल का इन्फरेंस परीक्षण करने के लिए, अपने फ़ोल्डर में **app.py** नामक एक Python फ़ाइल बनाएं और निम्नलिखित कोड को कॉपी-पेस्ट करें:

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

### स्टेप 6: मॉडल को Azure AI में अपलोड करें

मॉडल को Azure AI मॉडल रिपॉजिटरी में अपलोड करने से मॉडल को आपकी डेवलपमेंट टीम के अन्य सदस्यों के साथ साझा करना आसान हो जाता है और मॉडल के वर्जन कंट्रोल को भी संभालता है। मॉडल अपलोड करने के लिए निम्नलिखित कमांड चलाएं:

> [!NOTE]
> `{}` को अपने `resourceGroup` और Azure AI प्रोजेक्ट नाम से अपडेट करें, और निम्नलिखित कमांड चलाएं:

```
az ml workspace show
```

या +++ai.azure.com+++ पर जाकर **management center** > **project** > **overview** का चयन करें।

`{}` प्लेसहोल्डर्स को अपने resource group और Azure AI प्रोजेक्ट नाम से अपडेट करें।

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
इसके बाद आप अपने अपलोड किए गए मॉडल को देख सकते हैं और https://ml.azure.com/model/list पर जाकर अपने मॉडल को डिप्लॉय कर सकते हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। हालांकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।