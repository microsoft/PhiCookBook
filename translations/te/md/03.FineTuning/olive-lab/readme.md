<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-12-21T22:19:24+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "te"
}
-->
# ల్యాబ్. డివైస్‌లో ఇన్ఫరెన్స్ కోసం AI మోడల్స్‌ను ఆప్టిమైజ్ చేయండి

## పరిచయం 

> [!IMPORTANT]
> ఈ ల్యాబ్‌కు **Nvidia A10 or A100 GPU** మరియు సంబంధిత డ్రైవర్లు మరియు CUDA టూల్‌కిట్ (సంస్కరణ 12+) ఇన్స్టాల్ చేయబడివుండాలి.

> [!NOTE]
> ఇది ఒక **35-minute** ల్యాబ్, ఇది OLIVE ఉపయోగించి డివైస్‌లో ఇన్ఫరెన్స్ కోసం మోడల్స్‌ను ఆప్టిమైజ్ చేయడంపైన ఉన్న కోర్ కాన్సెప్ట్‌లపై హ్యాండ్స్-ఆన్ పరిచయాన్ని ఇస్తుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ ల్యాబ్ ముగిసేటప్పుడు, మీరు OLIVE ఉపయోగించి క్రింది పనులు చేయగలుగుతారు:

- AWQ క్వాంటైజేషన్ పద్ధతి ఉపయోగించి ఒక AI మోడల్‌ను క్వాంటైజ్ చేయడం.
- ఒక నిర్దిష్ట టాస్క్ కోసం AI మోడల్‌ను ఫైన్-ట్యూన్ చేయడం.
- ONNX Runtime పై డివైస్‌లో సమర్థవంతమైన ఇన్ఫరెన్స్ కోసం LoRA అడాప్టర్లను (ఫైన్-ట్యూన్ చేసిన మోడల్) జనరేట్ చేయడం.

### Olive అంటే ఏమిటి

Olive (*O*NNX *live*) ఒక మోడల్ ఆప్టిమైజేషన్ టూల్‌కిట్ మరియు అనుసంధాన CLI, ఇది మీకు ONNX runtime +++https://onnxruntime.ai+++ కోసం నాణ్యత మరియు పనితీరు కలిగిన మోడల్స్‌ను షిప్ చేయడానికి వీలు కల్పిస్తుంది.

![ఒలివ్ ఫ్లో](../../../../../translated_images/te/olive-flow.5daf97340275f8b6.png)

Oliveకి ఇన్పుట్ సాధారణంగా PyTorch లేదా Hugging Face మోడల్ ఉంటాయి మరియు అవుట్‌పుట్ ONNX runtime పై అమలు అయ్యే ఒక ఆప్టిమైజ్ చేసిన ONNX మోడల్ అవుతుంది. Olive deployment టార్గెట్ యొక్క AI యాక్సిలరేటర్ (NPU, GPU, CPU) కోసం మోడల్‌ను ఆప్టిమైజ్ చేస్తుంది, ఇవి Qualcomm, AMD, Nvidia లేదా Intel వంటి హార్డ్‌వేర్ వినియోగదారుల ద్వారా అందించబడతాయి.

Olive ఒక *workflow* ని అమలు చేస్తుంది, ఇది *passes* అని పిలవబడే వ్యక్తిగత మోడల్ ఆప్టిమైజేషన్ టాస్క్‌ల యొక్క క్రమబద్ధమైన శ్రేణి — ఉదాహరణగా passes లో model compression, graph capture, quantization, graph optimization ఉంటాయి. ప్రతి pass కి సెట్ అయిన కొన్ని పారామీటర్లు ఉంటాయి, వీటిని ఖచ్చితత్వం మరియు లేటెన్సీ వంటి బెస్ట్ మెట్రిక్స్ సాధించడానికి ట్యూన్ చేయవచ్చు, ఇవి సంబంధిత ఎవాల్యుయేటర్ ద్వారా మూల్యాంకనం చేయబడతాయి. Olive ప్రతి pass ను ఒక్కొక్కటిగా లేదా passes సమూహంగా కలిసి ఆటో-ట్యూన్ చేయడానికి సెర్చ్ అల్గోరిథమ్ ఉపయోగించే సెర్చ్ స్ట్రాటజీని అనుసరిస్తుంది.

#### Olive యొక్క ప్రయోజనాలు

- వివిధ graph optimization, compression మరియు quantization సాంకేతికతలతో ట్రయల్-అండ్-ఎర్రర్ మాన్యువల్ ప్రయోగాలలో కలిగే నిరాశను మరియు సమయాన్ని **తగ్గిస్తుంది**. మీ నాణ్యత మరియు పనితీరు పరిమితులను నిర్వచించి Olive ను ఉత్తమ మోడల్‌ను ఆటోమేటిగ్గా కనుగొనడానికి అనుమతించండి.
- **40+ built-in model optimization components** quantization, compression, graph optimization మరియు finetuning లో ఆధునిక సాంకేతికతలను కవర్ చేస్తాయి.
- సాధారణ మోడల్ ఆప్టిమైజేషన్ టాస్క్‌లకు ఉపయోగించడానికి సులభమైన **CLI**. ఉదాహరణకు, olive quantize, olive auto-opt, olive finetune.
- మోడల్ ప్యాకేజింగ్ మరియు డిప్లాయ్‌మెంట్ బిల్ట్-ఇన్.
- **Multi LoRA serving** కోసం మోడల్స్‌ను జనరేట్ చేయడానికి మద్దతు.
- YAML/JSON ఉపయోగించి workflows ను నిర్మించి మోడల్ ఆప్టిమైజేషన్ మరియు డిప్లాయ్‌మెంట్ టాస్క్‌లను ఒర్కెస్ట్రేట్ చేయగలగడం.
- **Hugging Face** మరియు **Azure AI** ఇంటిగ్రేషన్.
- ఖర్చులను **తగ్గించడానికి** బిల్ట్-ఇన్ **కాషింగ్** యాంత్రికత.

## ల్యాబ్ సూచనలు
> [!NOTE]
> దయచేసి మీరు మీ Azure AI Hub మరియు Project ని provision చేసి, Lab 1 ప్రకారం మీ A100 compute ను సెటప్ చేసినట్లు నిర్ధారించండి.

### దశ 0: మీ Azure AI Computeకు కనెక్ట్ అవ్వండి

మీరు **VS Code** లోని remote ఫీచర్ ఉపయోగించి Azure AI compute కు కనెక్ట్ అవుతారు. 

1. మీ **VS Code** డెస్క్‌టాప్ అప్లికేషన్‌ని ఓపెన్ చేయండి:
1. **Shift+Ctrl+P** ఉపయోగించి **command palette** తెరవండి
1. command palette లో **AzureML - remote: Connect to compute instance in New Window** కోసం శోధించండి.
1. Compute కు కనెక్ట్ అవ్వడానికి స్క్రీన్‌పై కనిపించే సూచనలను అనుసరించండి. ఇందులో మీరు Lab 1లో సెటప్ చేసిన Azure Subscription, Resource Group, Project మరియు Compute పేరును ఎంచుకోవడం ఉంటుంది.
1. ఒకసారి మీరు మీ Azure ML Compute node కు కనెక్ట్ అయిన తర్వాత ఇది **Visual Code యొక్క దిగువ ఎడమభాగంలో** `><Azure ML: Compute Name` గా చూడబడుతుంది

### దశ 1: ఈ రిపోను క్లోన్ చేయండి

VS Codeలో **Ctrl+J** తో కొత్త టెర్మినల్ ఓపెన్ చేసి ఈ రిపోను క్లోన్ చేయండి:

In the terminal you should see the prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
సొల్యూషన్‌ను క్లోన్ చేయండి 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### దశ 2: VS Codeలో ఫోల్డర్‌ని ఓపెన్ చేయండి

సంబంధిత ఫోల్డర్‌లో VS Code ను ఓపెన్ చేయడానికి టెర్మినల్‌లో క్రింది కమాండ్‌ను అమలు చేయండి, ఇది ఒక కొత్త విండోని ఓపెన్ చేస్తుంది:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

వికల్పంగా, **File** > **Open Folder** ఎంచుకుని ఫోల్డర్‌ను ఓపెన్ చేయవచ్చు। 

### దశ 3: డిపెండెన్సీలు

VS Codeలో మీ Azure AI Compute Instanceలో టెర్మినల్ విండో (సలహా: **Ctrl+J**) ఓపెన్ చేసి డిపెండెన్సీలను ఇన్‌స్టాల్ చేయడానికి క్రింద చూపిన కమాండ్స్‌ను అమలు చేయండి:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> అన్ని డిపెండెన్సీలు ఇన్‌స్టాల్ చేయడానికి సుమారు ~5mins పడుతుంది.

ఈ ల్యాబ్‌లో మీరు Azure AI Model catalog నుండి మోడల్స్‌ను డౌన్లోడ్ మరియు అప్లోడ్ చేస్తారు. కాబట్టి మీరు మోడల్ క్యాటలాగ్‌ను యాక్సెస్ చేయడానికి Azureలో లాగిన్ అవ్వాలి:

```bash
az login
```

> [!NOTE]
> లాగిన్ సమయంలో మీకు subscription ఎంచుకోవాలని అడగబడుతుంది. దయచేసి ఈ ల్యాబ్ కోసం ఇచ్చిన subscription ను ఎంచుకున్నారో నిర్ధారించండి.

### దశ 4: Olive కమాండ్స్ అమలు చేయండి 

VS Codeలో మీ Azure AI Compute Instanceలో టెర్మినల్ విండో (సలహా: **Ctrl+J**) ఓపెన్ చేసి `olive-ai` conda environment యాక్టివేట్ అయ్యిందో లేదో నిర్ధారించండి:

```bash
conda activate olive-ai
```

తరువాత, కింది Olive కమాండ్స్‌ను కమాండ్ లైన్‌లో అమలు చేయండి.

1. **Inspect the data:** ఈ ఉదాహరణలో, మీరు Phi-3.5-Mini మోడల్‌ను ప్రయాణ సంబంధిత ప్రశ్నలకు సమాధానం చెప్పడంలో ప్రత్యేకత కలిగించేలా ఫైన్-ట్యూన్ చేయబోతున్నారు. దిగువ కోడ్ డేటాసెట్ యొక్క మొదటి కొన్ని రికార్డులను చూపిస్తుంది, ఇవి JSON lines ఫార్మాట్‌లో ఉన్నాయి:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Quantize the model:** మోడల్‌ను ట్రెయినింగ్ చేయడానికి ముందు, మీరు క్రింది కమాండ్ ఉపయోగించి Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ అనే పద్ధతిని ఉపయోగించి క్వాంటైజ్ చేస్తారు. AWQ ఇన్ఫరెన్స్ సమయంలో ఉత్పత్తి అయ్యే యాక్టివేషన్లను పరిగణనలోకి తీసుకుని మోడల్ వెయిట్స్‌ను క్వాంటైజ్ చేస్తుంది. ఇది యాక్టివేషన్లలోని వాస్తవ డేటా పంపిణీని పరిగణలోకి తీసుకుని సంప్రదాయ వెయిట్ క్వాంటైజేషన్ పద్ధతులతో పోలిస్తే మోడల్ ఖచ్చితత్వాన్ని మెరుగ్గా పరిరక్షిస్తుంది.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    ఇది AWQ క్వాంటైజేషన్ పూర్తి చేయడానికి **~8mins** సమయం పడుతుంది, ఇది **మోడల్ పరిమాణాన్ని సుమారు ~7.5GB నుండి ~2.5GBకి తగ్గిస్తుంది**.
   
   ఈ ల్యాబ్‌లో, మేము Hugging Face నుండి మోడల్స్ ఇన్‌పుట్ చేయడం ఎలా చేయాలో చూపిస్తున్నాము (ఉదాహరణకు: `microsoft/Phi-3.5-mini-instruct`). అయితే, Olive ద్వారా మీరు `model_name_or_path` ఆర్గ్యుమెంట్‌ను Azure AI asset IDకి (ఉదాహరణకు:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) అప్డేట్ చేసి Azure AI క్యాటలాగ్ నుండి కూడా మోడల్స్ ఇన్‌పుట్ చేయవచ్చు। 

1. **Train the model:** తరువాత, `olive finetune` కమాండ్ క్వాంటైజ్ చేసిన మోడల్‌ను ఫైన్-ట్యూన్ చేస్తుంది. మోడల్‌ను ఫైన్-ట్యూనింగ్‌కు ముందు క్వాంటైజ్ చేయడం తరువాత క్వాంటైజ్ చేయడంవల్ల కంటే మెరుగైన ఖచ్చితత్వాన్ని ఇస్తుంది, ఎందుకంటే ఫైన్-ట్యూనింగ్ ప్రక్రియ క్వాంటైజేషన్ వల్ల జరిగిన కొంత నష్టాన్ని పునరుద్ధరిస్తుంది।
    
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
    
    ఫైన్-ట్యూనింగ్ (100 స్టెప్స్‌తో) పూర్తి చేయడానికి **~6mins** పడుతుంది।

1. **Optimize:** మోడల్ ట్రెయిన్ అయిన తర్వాత, Olive యొక్క `auto-opt` కమాండ్ ఉపయోగించి మీరు మోడల్‌ను ఆప్టిమైజ్ చేయవచ్చు. ఇది ONNX గ్రాఫ్‌ను క్యాప్చర్ చేసింది, మోడల్‌ను కంప్రెస్ చేసి ఫ్యూజన్లు చేయడం ద్వారా CPU కోసం పనితీరును మెరుగుపరచడానికి కొన్ని ఆప్టిమైజేషన్లు ఆటోమేటిగ్గా చేస్తుంది. గమనించదగ్గ విషయం ఏమిటంటే, మీరు కేవలం `--device` మరియు `--provider` ఆర్గ్యుమెంట్లను అప్డేట్ చేయడం ద్వారా NPU లేదా GPU వంటి ఇతర డివైస్‌ల కోసం కూడా ఆప్టిమైజ్ చేయవచ్చు — కానీ ఈ ల్యాబ్ కోసం మేము CPU ను ఉపయోగిస్తాము।
    
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
    
    ఆప్టిమైజేషన్ పూర్తి చేయడానికి **~5mins** పడుతుంది।

### దశ 5: మోడల్ ఇన్ఫరెన్స్ త్వ‌రిత పరీక్ష

మోడల్ ఇన్ఫరెన్స్‌ను పరీక్షించడానికి, మీ ఫోల్డర్‌లో **app.py** అనే Python ఫైల్‌ను సృష్టించి క్రింద ఇచ్చిన కోడ్‌ను కాపీ-పేస్ట్ చేయండి:

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

కోడ్‌ను అమలు చేయడానికి:

```bash
python app.py
```

### దశ 6: మోడల్‌ను Azure AI కు అప్లోడ్ చేయండి

మోడల్‌ను Azure AI మోడల్ రిపోజిటరీకి అప్లోడ్ చేయడం ద్వారా ఆ మోడల్‌ను మీ డెవలపర్ టీమ్ సభ్యులతో షేర్ చేయవచ్చు మరియు మోడల్ యొక్క వెర్షన్ నియంత్రణ కూడా నిర్వహించబడుతుంది. మోడల్‌ను అప్లోడ్ చేయడానికి క్రింద ఉన్న కమాండ్‌ను అమలు చేయండి:

> [!NOTE]
> `{}` ప్లేస్‌హోల্ডర్లను మీ resource group మరియు Azure AI Project పేరుతో అప్డేట్ చేయండి. 

మీ resource group `"resourceGroup"and Azure AI Project name కనుక్కోవడానికి, క్రింది కమాండ్‌ను అమలు చేయండి 

```
az ml workspace show
```

లేదా +++ai.azure.com+++ కి వెళ్లి **management center** **project** **overview**ను ఎంచుకోండి

`{}` প্লేస్‌హోల్డర్లను మీ రిసోర్స్ గ్రూప్ మరియు Azure AI ప్రాజెక్ట్ పేరుతో అప్డేట్ చేయండి।

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
మీ అప్లోడ్ చేసిన మోడల్‌ను మీరు తరువాత https://ml.azure.com/model/list వద్ద చూడవచ్చు మరియు మీ మోడల్‌ను అక్కడ డిప్లాయ్ చేయవచ్చు

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా అసమగ్రతలు ఉండవచ్చు అని దయచేసి గమనించండి. ప్రాథమిక భాషలోని అసలు డాక్యుమెంట్‌ను ప్రామాణిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి, నిపుణులైన మానవ అనువాదాన్ని సలహా గా సూచిస్తాము. ఈ అనువాదం ఉపయోగించడం వలన ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పు వ్యాఖ్యానాల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->