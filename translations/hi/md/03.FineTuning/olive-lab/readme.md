<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-08T05:24:32+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "hi"
}
-->
# Lab. ऑन-डिवाइस इन्फरेंस के लिए AI मॉडल्स को ऑप्टिमाइज़ करें

## परिचय

> [!IMPORTANT]
> इस लैब के लिए **Nvidia A10 या A100 GPU** के साथ संबंधित ड्राइवर और CUDA टूलकिट (संस्करण 12+) इंस्टॉल होना आवश्यक है।

> [!NOTE]
> यह एक **35 मिनट** की लैब है जो आपको OLIVE का उपयोग करके ऑन-डिवाइस इन्फरेंस के लिए मॉडल्स को ऑप्टिमाइज़ करने के मूल सिद्धांतों का व्यावहारिक परिचय देगी।

## सीखने के उद्देश्य

इस लैब के अंत तक, आप OLIVE का उपयोग करके:

- AWQ क्वांटाइजेशन मेथड का उपयोग करके AI मॉडल को क्वांटाइज़ कर पाएंगे।
- किसी विशिष्ट कार्य के लिए AI मॉडल को फाइन-ट्यून कर पाएंगे।
- ONNX Runtime पर कुशल ऑन-डिवाइस इन्फरेंस के लिए LoRA एडाप्टर्स (फाइन-ट्यून किया हुआ मॉडल) जनरेट कर पाएंगे।

### Olive क्या है

Olive (*O*NNX *live*) एक मॉडल ऑप्टिमाइज़ेशन टूलकिट है जिसमें CLI शामिल है, जो आपको ONNX runtime +++https://onnxruntime.ai+++ के लिए गुणवत्ता और प्रदर्शन के साथ मॉडल भेजने में सक्षम बनाता है।

![Olive Flow](../../../../../translated_images/olive-flow.5daf97340275f8b61397e91430ff02724a2547937b352e7fdfc2f669c56dcd35.hi.png)

Olive में इनपुट आमतौर पर PyTorch या Hugging Face मॉडल होता है और आउटपुट एक ऑप्टिमाइज़्ड ONNX मॉडल होता है जिसे उस डिवाइस (डिप्लॉयमेंट टारगेट) पर चलाया जाता है जहाँ ONNX runtime मौजूद होता है। Olive मॉडल को डिप्लॉयमेंट टारगेट के AI एक्सेलेरेटर (NPU, GPU, CPU) के अनुसार ऑप्टिमाइज़ करता है, जो Qualcomm, AMD, Nvidia या Intel जैसे हार्डवेयर विक्रेता द्वारा प्रदान किया जाता है।

Olive एक *वर्कफ़्लो* को निष्पादित करता है, जो व्यक्तिगत मॉडल ऑप्टिमाइज़ेशन टास्क की एक क्रमबद्ध श्रृंखला होती है, जिन्हें *पास* कहा जाता है - उदाहरण के लिए पास में मॉडल कंप्रेशन, ग्राफ कैप्चर, क्वांटाइजेशन, ग्राफ ऑप्टिमाइज़ेशन शामिल हैं। प्रत्येक पास के पैरामीटर होते हैं जिन्हें ट्यून करके सर्वश्रेष्ठ मेट्रिक्स, जैसे सटीकता और विलंबता, प्राप्त की जाती हैं, जिन्हें संबंधित इवैल्युएटर द्वारा मापा जाता है। Olive एक खोज रणनीति का उपयोग करता है जो प्रत्येक पास को एक-एक करके या पास के समूह को एक साथ ऑटो-ट्यून करता है।

#### Olive के लाभ

- ग्राफ ऑप्टिमाइज़ेशन, कंप्रेशन और क्वांटाइजेशन के लिए विभिन्न तकनीकों के साथ मैनुअल ट्रायल-एंड-एरर प्रयोग में होने वाली निराशा और समय को कम करता है। अपनी गुणवत्ता और प्रदर्शन सीमाएँ निर्धारित करें और Olive आपके लिए सर्वश्रेष्ठ मॉडल अपने आप खोज लेगा।
- क्वांटाइजेशन, कंप्रेशन, ग्राफ ऑप्टिमाइज़ेशन और फाइनट्यूनिंग में अत्याधुनिक तकनीकों को कवर करने वाले **40+ बिल्ट-इन मॉडल ऑप्टिमाइज़ेशन कॉम्पोनेंट्स**।
- सामान्य मॉडल ऑप्टिमाइज़ेशन कार्यों के लिए उपयोग में आसान CLI। उदाहरण के लिए, olive quantize, olive auto-opt, olive finetune।
- मॉडल पैकेजिंग और डिप्लॉयमेंट अंतर्निहित।
- **Multi LoRA सर्विंग** के लिए मॉडल जनरेशन का समर्थन।
- YAML/JSON का उपयोग करके वर्कफ़्लोज़ का निर्माण कर मॉडल ऑप्टिमाइज़ेशन और डिप्लॉयमेंट कार्यों का समन्वय।
- **Hugging Face** और **Azure AI** इंटीग्रेशन।
- लागत बचाने के लिए बिल्ट-इन **कैशिंग** मैकेनिज्म।

## लैब निर्देश
> [!NOTE]
> कृपया सुनिश्चित करें कि आपने अपना Azure AI Hub और प्रोजेक्ट प्रोविजन किया है और लैब 1 के अनुसार अपना A100 कंप्यूट सेटअप किया है।

### चरण 0: अपने Azure AI Compute से कनेक्ट करें

आप **VS Code** के रिमोट फीचर का उपयोग करके Azure AI कंप्यूट से कनेक्ट करेंगे।

1. अपना **VS Code** डेस्कटॉप एप्लिकेशन खोलें:
2. **Shift+Ctrl+P** दबाकर कमांड पैलेट खोलें।
3. कमांड पैलेट में **AzureML - remote: Connect to compute instance in New Window** खोजें।
4. ऑन-स्क्रीन निर्देशों का पालन करते हुए कंप्यूट से कनेक्ट करें। इसमें आपके Azure Subscription, Resource Group, Project और Lab 1 में सेट किए गए Compute नाम का चयन शामिल होगा।
5. एक बार जब आप Azure ML Compute नोड से कनेक्ट हो जाएं, तो यह Visual Code के **नीचे बाएं कोने** में दिखेगा `><Azure ML: Compute Name`

### चरण 1: इस रिपो को क्लोन करें

VS Code में, **Ctrl+J** दबाकर नया टर्मिनल खोलें और इस रिपॉजिटरी को क्लोन करें:

टर्मिनल में आपको प्रॉम्प्ट दिखेगा

```
azureuser@computername:~/cloudfiles/code$ 
```
सॉल्यूशन क्लोन करें

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### चरण 2: VS Code में फ़ोल्डर खोलें

संबंधित फ़ोल्डर में VS Code खोलने के लिए टर्मिनल में निम्न कमांड चलाएं, जिससे नई विंडो खुलेगी:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

या फिर आप **File** > **Open Folder** चुनकर भी फ़ोल्डर खोल सकते हैं।

### चरण 3: डिपेंडेंसीज

VS Code में अपने Azure AI Compute इंस्टेंस में टर्मिनल विंडो खोलें (टिप: **Ctrl+J**) और डिपेंडेंसीज इंस्टॉल करने के लिए निम्न कमांड चलाएं:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> सभी डिपेंडेंसीज इंस्टॉल होने में लगभग 5 मिनट लगेंगे।

इस लैब में आप Azure AI मॉडल कैटलॉग से मॉडल डाउनलोड और अपलोड करेंगे। मॉडल कैटलॉग तक पहुंचने के लिए आपको Azure में लॉगिन करना होगा:

```bash
az login
```

> [!NOTE]
> लॉगिन के समय आपको अपनी सब्सक्रिप्शन चुनने के लिए कहा जाएगा। सुनिश्चित करें कि आप लैब के लिए प्रदान की गई सब्सक्रिप्शन चुनें।

### चरण 4: Olive कमांड्स चलाएं

VS Code में अपने Azure AI Compute इंस्टेंस में टर्मिनल खोलें (टिप: **Ctrl+J**) और सुनिश्चित करें कि `olive-ai` कोंडा एनवायरनमेंट सक्रिय है:

```bash
conda activate olive-ai
```

इसके बाद, निम्न Olive कमांड्स कमांड लाइन में चलाएं।

1. **डेटा जांचें:** इस उदाहरण में, आप Phi-3.5-Mini मॉडल को फाइन-ट्यून करने जा रहे हैं ताकि यह यात्रा संबंधित सवालों के जवाब देने में विशेषज्ञ हो। नीचे दिया गया कोड JSON लाइन्स फॉर्मेट में डेटासेट के पहले कुछ रिकॉर्ड दिखाता है:

    ```bash
    head data/data_sample_travel.jsonl
    ```
2. **मॉडल को क्वांटाइज़ करें:** मॉडल को ट्रेनिंग से पहले क्वांटाइज़ करें, निम्न कमांड के साथ जो Active Aware Quantization (AWQ) तकनीक का उपयोग करता है +++https://arxiv.org/abs/2306.00978+++. AWQ मॉडल के वेट्स को क्वांटाइज़ करता है जो इन्फरेंस के दौरान उत्पन्न एक्टिवेशन को ध्यान में रखता है। इसका मतलब है कि क्वांटाइज़ेशन प्रक्रिया वास्तविक डेटा वितरण को ध्यान में रखती है, जिससे पारंपरिक वेट क्वांटाइज़ेशन की तुलना में मॉडल की सटीकता बेहतर बनी रहती है।

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ क्वांटाइज़ेशन पूरा होने में लगभग **8 मिनट** लगते हैं, जो मॉडल के आकार को लगभग **7.5GB से 2.5GB तक कम कर देता है**।

   इस लैब में, हम आपको दिखा रहे हैं कि कैसे Hugging Face से मॉडल इनपुट करें (उदाहरण के लिए: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` कमांड क्वांटाइज़्ड मॉडल को फाइन-ट्यून करता है। क्वांटाइज़ेशन के बाद नहीं बल्कि पहले फाइन-ट्यूनिंग करने से बेहतर सटीकता मिलती है क्योंकि फाइन-ट्यूनिंग क्वांटाइज़ेशन से हुए नुकसान को आंशिक रूप से सुधारता है।

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

    फाइन-ट्यूनिंग (100 स्टेप्स के साथ) पूरा होने में लगभग **6 मिनट** लगते हैं।

3. **ऑप्टिमाइज़ करें:** मॉडल ट्रेन हो जाने के बाद, अब आप Olive के `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` आर्गुमेंट्स का उपयोग करके मॉडल को ऑप्टिमाइज़ करेंगे - लेकिन इस लैब के लिए हम CPU का उपयोग करेंगे।

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

    ऑप्टिमाइज़ेशन पूरा होने में लगभग **5 मिनट** लगते हैं।

### चरण 5: मॉडल इन्फरेंस का त्वरित परीक्षण

मॉडल इन्फरेंस का परीक्षण करने के लिए, अपने फ़ोल्डर में **app.py** नाम की एक Python फाइल बनाएं और निम्न कोड कॉपी-पेस्ट करें:

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

कोड चलाने के लिए:

```bash
python app.py
```

### चरण 6: मॉडल को Azure AI पर अपलोड करें

मॉडल को Azure AI मॉडल रिपॉजिटरी में अपलोड करने से यह आपके विकास टीम के अन्य सदस्यों के साथ साझा किया जा सकता है और मॉडल का संस्करण नियंत्रण भी संभाला जाता है। मॉडल अपलोड करने के लिए निम्न कमांड चलाएं:

> [!NOTE]
> `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `` में अपना resourceGroup और Azure AI प्रोजेक्ट नाम अपडेट करें, फिर निम्न कमांड चलाएं

```
az ml workspace show
```

या +++ai.azure.com+++ पर जाकर **management center** > **project** > **overview** चुनें।

`{}` प्लेसहोल्डर्स को अपने resource group और Azure AI प्रोजेक्ट के नाम से बदलें।

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

आप फिर अपने अपलोड किए गए मॉडल को देख सकते हैं और https://ml.azure.com/model/list पर अपना मॉडल डिप्लॉय कर सकते हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।