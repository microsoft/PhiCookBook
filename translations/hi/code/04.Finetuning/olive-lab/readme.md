<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-16T16:11:42+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "hi"
}
-->
# लैब। ऑन-डिवाइस इन्फरेंस के लिए AI मॉडल्स का अनुकूलन करें

## परिचय

> [!IMPORTANT]  
> इस लैब के लिए **Nvidia A10 या A100 GPU** के साथ संबंधित ड्राइवर और CUDA टूलकिट (संस्करण 12+) इंस्टॉल होना आवश्यक है।

> [!NOTE]  
> यह एक **35 मिनट** की लैब है जो आपको OLIVE का उपयोग करके ऑन-डिवाइस इन्फरेंस के लिए मॉडल्स के अनुकूलन के मूल सिद्धांतों का व्यावहारिक परिचय देगी।

## सीखने के उद्देश्य

इस लैब के अंत तक, आप OLIVE का उपयोग करके निम्न कार्य कर सकेंगे:

- AWQ क्वांटाइजेशन विधि का उपयोग करके AI मॉडल को क्वांटाइज करना।
- किसी विशिष्ट कार्य के लिए AI मॉडल को फाइन-ट्यून करना।
- ONNX Runtime पर कुशल ऑन-डिवाइस इन्फरेंस के लिए LoRA एडाप्टर्स (फाइन-ट्यून मॉडल) जनरेट करना।

### Olive क्या है

Olive (*O*NNX *live*) एक मॉडल अनुकूलन टूलकिट है जिसमें CLI भी शामिल है, जो आपको ONNX runtime +++https://onnxruntime.ai+++ के लिए गुणवत्ता और प्रदर्शन के साथ मॉडल भेजने में सक्षम बनाता है।

![Olive Flow](../../../../../translated_images/olive-flow.c4f76d9142c579b2.hi.png)

Olive में इनपुट आमतौर पर PyTorch या Hugging Face मॉडल होता है और आउटपुट एक अनुकूलित ONNX मॉडल होता है जिसे ONNX runtime चलाने वाले डिवाइस (डिप्लॉयमेंट टारगेट) पर निष्पादित किया जाता है। Olive मॉडल को डिप्लॉयमेंट टारगेट के AI एक्सेलेरेटर (NPU, GPU, CPU) के लिए अनुकूलित करता है, जो Qualcomm, AMD, Nvidia या Intel जैसे हार्डवेयर विक्रेता द्वारा प्रदान किया जाता है।

Olive एक *वर्कफ़्लो* निष्पादित करता है, जो व्यक्तिगत मॉडल अनुकूलन कार्यों की एक क्रमबद्ध श्रृंखला होती है, जिन्हें *पास* कहा जाता है - उदाहरण के लिए पास में मॉडल कंप्रेशन, ग्राफ कैप्चर, क्वांटाइजेशन, ग्राफ ऑप्टिमाइजेशन शामिल हैं। प्रत्येक पास के पैरामीटर होते हैं जिन्हें सर्वोत्तम मेट्रिक्स, जैसे सटीकता और विलंबता, प्राप्त करने के लिए ट्यून किया जा सकता है, जिन्हें संबंधित इवैल्युएटर द्वारा मापा जाता है। Olive एक खोज रणनीति का उपयोग करता है जो प्रत्येक पास को एक-एक करके या पास के समूह को ऑटो-ट्यून करने के लिए खोज एल्गोरिदम का उपयोग करता है।

#### Olive के लाभ

- ग्राफ ऑप्टिमाइजेशन, कंप्रेशन और क्वांटाइजेशन के लिए विभिन्न तकनीकों के साथ मैनुअल ट्रायल-एंड-एरर प्रयोग में लगने वाले समय और निराशा को कम करें। अपनी गुणवत्ता और प्रदर्शन सीमाएं निर्धारित करें और Olive को आपके लिए सर्वश्रेष्ठ मॉडल खोजने दें।
- क्वांटाइजेशन, कंप्रेशन, ग्राफ ऑप्टिमाइजेशन और फाइनट्यूनिंग में अत्याधुनिक तकनीकों को कवर करने वाले **40+ बिल्ट-इन मॉडल अनुकूलन घटक**।
- सामान्य मॉडल अनुकूलन कार्यों के लिए उपयोग में आसान CLI। उदाहरण के लिए, olive quantize, olive auto-opt, olive finetune।
- मॉडल पैकेजिंग और डिप्लॉयमेंट अंतर्निर्मित।
- **मल्टी LoRA सर्विंग** के लिए मॉडल जनरेट करने का समर्थन।
- YAML/JSON का उपयोग करके वर्कफ़्लो बनाएं ताकि मॉडल अनुकूलन और डिप्लॉयमेंट कार्यों का समन्वय किया जा सके।
- **Hugging Face** और **Azure AI** इंटीग्रेशन।
- लागत बचाने के लिए अंतर्निर्मित **कैशिंग** तंत्र।

## लैब निर्देश  
> [!NOTE]  
> कृपया सुनिश्चित करें कि आपने अपना Azure AI Hub और प्रोजेक्ट प्रोविजन किया है और लैब 1 के अनुसार अपना A100 कंप्यूट सेटअप किया है।

### चरण 0: अपने Azure AI Compute से कनेक्ट करें

आप **VS Code** में रिमोट फीचर का उपयोग करके Azure AI कंप्यूट से कनेक्ट करेंगे।

1. अपना **VS Code** डेस्कटॉप एप्लिकेशन खोलें:  
2. **Shift+Ctrl+P** दबाकर **कमांड पैलेट** खोलें।  
3. कमांड पैलेट में खोजें **AzureML - remote: Connect to compute instance in New Window**।  
4. स्क्रीन पर दिए गए निर्देशों का पालन करें ताकि आप Compute से कनेक्ट हो सकें। इसमें आपका Azure Subscription, Resource Group, Project और Compute नाम चुनना शामिल होगा जो आपने लैब 1 में सेट किया था।  
5. एक बार Azure ML Compute नोड से कनेक्ट हो जाने पर, यह **Visual Code के नीचे बाएं कोने** में दिखेगा `><Azure ML: Compute Name`।

### चरण 1: इस रिपॉजिटरी को क्लोन करें

VS Code में, आप **Ctrl+J** दबाकर नया टर्मिनल खोल सकते हैं और इस रिपॉजिटरी को क्लोन करें:

टर्मिनल में आपको प्रॉम्प्ट दिखेगा

```
azureuser@computername:~/cloudfiles/code$ 
```  
सॉल्यूशन क्लोन करें

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### चरण 2: VS Code में फोल्डर खोलें

संबंधित फोल्डर में VS Code खोलने के लिए टर्मिनल में निम्न कमांड चलाएं, जो एक नई विंडो खोलेगा:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

वैकल्पिक रूप से, आप **File** > **Open Folder** चुनकर भी फोल्डर खोल सकते हैं।

### चरण 3: डिपेंडेंसीज

VS Code में अपने Azure AI Compute इंस्टेंस में एक टर्मिनल विंडो खोलें (टिप: **Ctrl+J**) और डिपेंडेंसीज इंस्टॉल करने के लिए निम्न कमांड चलाएं:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> सभी डिपेंडेंसीज इंस्टॉल होने में लगभग 5 मिनट लगेंगे।

इस लैब में आप Azure AI मॉडल कैटलॉग से मॉडल डाउनलोड और अपलोड करेंगे। इसलिए मॉडल कैटलॉग तक पहुंचने के लिए आपको Azure में लॉगिन करना होगा:

```bash
az login
```

> [!NOTE]  
> लॉगिन के समय आपसे आपका सब्सक्रिप्शन चुनने के लिए कहा जाएगा। सुनिश्चित करें कि आपने इस लैब के लिए प्रदान किया गया सब्सक्रिप्शन चुना है।

### चरण 4: Olive कमांड्स चलाएं

VS Code में अपने Azure AI Compute इंस्टेंस में एक टर्मिनल विंडो खोलें (टिप: **Ctrl+J**) और सुनिश्चित करें कि `olive-ai` कोंडा एनवायरनमेंट सक्रिय है:

```bash
conda activate olive-ai
```

इसके बाद, कमांड लाइन में निम्न Olive कमांड्स चलाएं।

1. **डेटा निरीक्षण करें:** इस उदाहरण में, आप Phi-3.5-Mini मॉडल को फाइन-ट्यून करने जा रहे हैं ताकि यह यात्रा से संबंधित प्रश्नों का उत्तर देने में विशेषज्ञ हो जाए। नीचे दिया गया कोड JSON लाइन्स फॉर्मेट में डेटासेट के पहले कुछ रिकॉर्ड दिखाता है:

    ```bash
    head data/data_sample_travel.jsonl
    ```

2. **मॉडल क्वांटाइज करें:** मॉडल को ट्रेनिंग से पहले क्वांटाइज करने के लिए निम्न कमांड चलाएं, जो Active Aware Quantization (AWQ) तकनीक +++https://arxiv.org/abs/2306.00978+++ का उपयोग करता है। AWQ मॉडल के वेट्स को क्वांटाइज करता है, जिसमें इन्फरेंस के दौरान उत्पन्न एक्टिवेशन को ध्यान में रखा जाता है। इसका मतलब है कि क्वांटाइजेशन प्रक्रिया एक्टिवेशन में वास्तविक डेटा वितरण को ध्यान में रखती है, जिससे पारंपरिक वेट क्वांटाइजेशन विधियों की तुलना में मॉडल की सटीकता बेहतर बनी रहती है।

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ क्वांटाइजेशन पूरा होने में लगभग **8 मिनट** लगते हैं, जो मॉडल का आकार लगभग **7.5GB से घटाकर 2.5GB** कर देता है।

    इस लैब में हम आपको Hugging Face से मॉडल इनपुट करना दिखा रहे हैं (उदाहरण के लिए: `microsoft/Phi-3.5-mini-instruct`)। हालांकि, Olive आपको Azure AI कैटलॉग से मॉडल इनपुट करने की भी अनुमति देता है, बस `model_name_or_path` आर्गुमेंट को Azure AI एसेट ID (उदाहरण के लिए: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) में अपडेट करें।

3. **मॉडल ट्रेन करें:** इसके बाद, `olive finetune` कमांड क्वांटाइज्ड मॉडल को फाइन-ट्यून करता है। क्वांटाइजेशन के बाद फाइन-ट्यूनिंग की तुलना में पहले क्वांटाइजेशन करने से बेहतर सटीकता मिलती है क्योंकि फाइन-ट्यूनिंग प्रक्रिया क्वांटाइजेशन से हुए नुकसान को कुछ हद तक सुधारती है।

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

4. **ऑप्टिमाइज़ करें:** मॉडल ट्रेन हो जाने के बाद, आप Olive के `auto-opt` कमांड का उपयोग करके मॉडल को ऑप्टिमाइज़ करते हैं, जो ONNX ग्राफ को कैप्चर करता है और CPU के लिए मॉडल प्रदर्शन सुधारने के लिए कई ऑप्टिमाइजेशन जैसे कंप्रेशन और फ्यूजन स्वचालित रूप से करता है। ध्यान दें कि आप `--device` और `--provider` आर्गुमेंट्स को अपडेट करके NPU या GPU जैसे अन्य डिवाइस के लिए भी ऑप्टिमाइज़ कर सकते हैं - लेकिन इस लैब के लिए हम CPU का उपयोग करेंगे।

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

मॉडल इन्फरेंस का परीक्षण करने के लिए, अपने फोल्डर में **app.py** नामक एक पायथन फाइल बनाएं और निम्न कोड कॉपी-पेस्ट करें:

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

मॉडल को Azure AI मॉडल रिपॉजिटरी में अपलोड करने से मॉडल आपके विकास टीम के अन्य सदस्यों के साथ साझा किया जा सकता है और मॉडल का संस्करण नियंत्रण भी संभाला जाता है। मॉडल अपलोड करने के लिए निम्न कमांड चलाएं:

> [!NOTE]  
> `{}` प्लेसहोल्डर्स को अपने रिसोर्स ग्रुप और Azure AI प्रोजेक्ट नाम से अपडेट करें।

अपने रिसोर्स ग्रुप `"resourceGroup"` और Azure AI प्रोजेक्ट नाम जानने के लिए निम्न कमांड चलाएं:

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
आप फिर https://ml.azure.com/model/list पर जाकर अपने अपलोड किए गए मॉडल को देख सकते हैं और उसे डिप्लॉय कर सकते हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।