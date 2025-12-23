<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-12-21T16:42:21+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "te"
}
-->
# ల్యాబ్. డివైస్‌పై ఇన్ఫరెన్స్ కోసం AI మోడల్స్‌ను ఆప్టిమైజ్ చేయండి

## పరిచయం 

> [!IMPORTANT]
> ఈ ల్యాబ్‌కు సంబంధిత డ్రైవర్లు మరియు CUDA టూల్‌కిట్ (వర్షన్ 12+) ఇన్‌స్టాల్ చేసిన **Nvidia A10 లేదా A100 GPU** అవసరం.

> [!NOTE]
> ఇది OLIVE ఉపయోగించి డివైస్‌పై ఇన్ఫరెన్స్ కోసం మోడల్స్‌ను ఆప్టిమైజ్ చేసే ముఖ్య ఆలోచనలకు ప్రాక్టికల్ పరిచయం ఇచ్చే **35-నిమిషాల** ల్యాబ్.

## నేర్చుకోవాల్సిన లక్ష్యాలు

ఈ ల్యాబ్ ముగిసే వరకు, మీరు OLIVE ఉపయోగించి చేయగలిగే పనులు:

- AWQ క్వాంటైజేషన్ పద్ధతిని ఉపయోగించి AI మోడల్‌ను క్వాంటైజ్ చేయడం.
- నిర్దిష్ట టాస్క్ కోసం AI మోడల్‌ను ఫైన్-ట్యూన్ చేయడం.
- ONNX Runtime పై సామర్ధ్యవంతమైన డివైస్-ఆధారిత ఇన్ఫరెన్స్ కోసం LoRA అడాప్టర్లు (ఫైన్-ట్యూన్ చేసిన మోడల్) సృష్టించడం.

### Olive అంటే ఏమిటి

Olive (*O*NNX *live*) అనేది ఒక మోడల్ ఆప్టిమైజేషన్ టూల్‌కిట్ మరియు సహాయక CLI కలిగిన ప్యాకేజ్, ఇది నాణ్యత మరియు ప్రదర్శనతో ONNX runtime +++https://onnxruntime.ai+++ కోసం మోడల్స్‌ను పంపించడానికి మీకు సౌకర్యం కలిగిస్తుంది.

![Olive ప్రవాహం](../../../../../translated_images/olive-flow.a47985655a756dcba73521511ea42eef359509a3a33cbd4b9ac04ba433287b80.te.png)

Oliveకు ఇన్పుట్ సాధారణంగా PyTorch లేదా Hugging Face మోడల్ ఉంటది మరియు అవుట్‌పుట్ అనేది ఒక ఆప్టిమైజ్ చేసిన ONNX మోడల్, ఇది ONNX runtime నడిచే డివైస్ (డిప్లాయ్‌మెంట్ టార్గెట్) పై ఎగ్జిక్యూట్ అవుతుంది. Olive డిప్లాయ్‌మెంట్ టార్గెట్ యొక్క AI ఆక్సిలరేటర్ (NPU, GPU, CPU) కోసం మోడల్‌ను ఆప్టిమైజ్ చేస్తుంది — వీటిని Qualcomm, AMD, Nvidia లేదా Intel వంటి హార్డ్‌వేర్ వెండర్ అందిస్తారు.

Olive ఒక *workflow* నిర్వహిస్తుంది, ఇది సీరియల్‌గా అమలయ్యే వ్యక్తిగత మోడల్ ఆప్టిమైజేషన్ పనుల సరఫరా అయిన *passes* అనే అర్ధం కలిగిన పరిధుల సమాహారం — ఉదాహరణకు passes లో ఉంటాయి: మోడల్ కంప్రెషన్, గ్రాఫ్ క్యాప్చర్, క్వాంటైజేషన్, గ్రాఫ్ ఆప్టిమైజేషన్. ప్రతి pass కు కొన్ని పనితీరు పారామీటర్లు ఉంటాయి, వీటిని సరైన మెట్రిక్స్ (ఉదాహరణకి ఖచ్చితత్వం మరియు లేటెన్సీ) సాధించడానికి ట్యూన్ చేయవచ్చు, ఇవి సంబంధిత ఎవాలుయేటర్ ద్వారా మూల్యాంకనం చేయబడతాయి. Olive ప్రతి pass ను ఒకదానికొకటి లేదా కొన్ని passes ను కలిసి ఆటో-ట్యూన్ చేయడానికి సెర్చ్ అల్గోరిథమ్ ఉపయోగించే సెర్చ్ స్ట్రాటజీని అమలు చేస్తుంది.

#### Olive యొక్క లాభాలు

- **వేధన మరియు సమయం తగ్గింపు**: గ్రాఫ్ ఆప్టిమైజేషన్, కంప్రెషన్ మరియు క్వాంటైజేషన్ వంటి విభిన్న సాంకేతికతలతో ట్రయల్-అండ్-ఎర్రర్ మాన్యువల్ ప్రయోగాలలోని అసహనాన్ని మరియు సమయంలో నష్టాన్ని తగ్గిస్తుంది. మీ నాణ్యత మరియు ప్రదర్శన పరిమితులను నిర్వచించి Olive మీ కోసం ఉత్తమ మోడల్‌ను ఆటోమేటిక్‌గా కనుగొనటానికి అవకాశం ఇస్తుంది.
- **40+ బిల్ట్-ఇన్ మోడల్ ఆప్టిమైజేషన్ కంపోనెంట్లు** క్వాంటైజేషన్, కంప్రెషన్, గ్రాఫ్ ఆప్టిమైజేషన్ మరియు ఫైన్‌ట్యూనింగ్‌లో ఆధునిక సాంకేతికతలను కవర్ చేస్తాయి.
- సాధారణ మోడల్ ఆప్టిమైజేషన్ పనుల కోసం **వాడుకోవడానికి సులభమైన CLI**. ఉదాహరణకు, olive quantize, olive auto-opt, olive finetune.
- మోడల్ ప్యాకేజింగ్ మరియు డిప్లాయ్‌మెంట్ బిల్ట్-ఇన్.
- **Multi LoRA serving** కోసం మోడల్స్ ఉత్పత్తి చేయడం మద్దతు.
- YAML/JSON ఉపయోగించి వర్క్‌ఫ్లోల్ని నిర్మించి మోడల్ ఆప్టిమైజేషన్ మరియు డిప్లాయ్‌మెంట్ పనులను ఆర్కెస్ట్రేట్ చేయగలదు.
- **Hugging Face** మరియు **Azure AI** ఇంటిగ్రేషన్.
- **కెస్టింగ్** మెకానిజం బిల్ట్-ఇన్ ద్వారా ఖర్చులు తగ్గించడం.

## ల్యాబ్ సూచనలు
> [!NOTE]
> దయచేసి మీరు మీ Azure AI Hub మరియు ప్రాజెక్టును ప్రొవిషన్ చేసి Lab 1 ప్రకారం మీ A100 కంప్యూట్ సెటప్ చేశారో లేదో నిర్ధారించుకోండి.

### దశ 0: మీ Azure AI Compute కు కనెక్ట్ చేయండి

మీరు **VS Code** లోని remote ఫీచర్ ఉపయోగించి Azure AI compute కు కనెక్ట్ అవుతారు. 

1. మీ **VS Code** డెస్క్‌టాప్ అప్లికేషన్‌ను ఓపెన్ చేయండి:
1. **Shift+Ctrl+P** ఉపయోగించి **command palette** ఓపెన్ చేయండి
1. కమాండ్ ప్యాలెట్‌లో **AzureML - remote: Connect to compute instance in New Window** కోసం శోధించండి.
1. Compute కు కనెక్ట్ కావడానికి స్క్రీన్ లోని సూచనలను అనుసరించండి. ఇందులో మీ Azure Subscription, Resource Group, Project మరియు Lab 1లో మీరు సెట్ చేసిన Compute పేరు ఎంచుకోవడం ఉంటుంది.
1. మీ Azure ML Compute నోడ్కు కనెక్ట్ అయిన వెంటనే ఇది **Visual Code** యొక్క దిగువ ఎడమలో `><Azure ML: Compute Name`గా ప్రదర్శించబడుతుంది

### దశ 1: ఈ repo ను క్లోన్ చేయండి

VS Code లో, మీరు **Ctrl+J** తో ఒక కొత్త టెర్మినల్ ఓపెన్ చేయగలరు మరియు ఈ repo ను క్లోన్ చేయండి:

In the terminal you should see the prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
సొల్యూషన్‌ను క్లోన్ చేయండి 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### దశ 2: VS Code లో ఫోల్డర్ ఓపెన్ చేయండి

సంబంధిత ఫోల్డర్‌లో VS Code ను ఓపెన్ చేయడానికి టెర్మినల్‌లో క్రింది కమాండ్‌ను అమలు చేయండి, ఇది ఒక కొత్త విండోని ఓపెన్ చేస్తుంది:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

మర alternatively, మీరు **File** > **Open Folder** ఎంచుకుని ఫోల్డర్‌ను ఓపెన్ చేయవచ్చు. 

### దశ 3: డిపెండెన్సీలు

మీ Azure AI Compute ఇన్స్టాన్స్‌లో VS Code లో ఒక టెర్మినల్ విండో (సూచి: **Ctrl+J**) ఓపెన్ చేసి డిపెండెన్సీలు ఇన్‌స్టాల్ చేయడానికి క్రింది కమాండ్స్‌ను అమలు చేయండి:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> అన్ని డిపెండెన్సీలు ఇన్‌స్టాల్ అవడానికి సుమారు ~5 నిమిషాలు పట్టొచ్చు.

ఈ ల్యాబ్‌లో మీరు మోడల్స్‌ను Azure AI Model క్యాటలాగ్‌కు డౌన్లోడ్ మరియు అప్‌లోడ్ చేస్తారు. కనుక మోడల్ క్యాటలాగ్‌కు ప్రాప్తి పొందడానికి, మీరు Azureలో లాగిన్ కావలసి ఉంటుంది:

```bash
az login
```

> [!NOTE]
> లాగిన్ సమయంలో మీకు మీ సబ్‌స్క్రిప్షన్ ఎంచుకోవడానికి అడగబడుతుంది. ఈ ల్యాబ్ కోసం అందించిన సబ్‌స్క్రిప్షన్‌ను సెట్చేసుకున్నారని నిర్ధారించండి.

### దశ 4: Olive కమాండ్స్ అమలు చేయండి 

మీ Azure AI Compute ఇన్స్టాన్స్‌లో VS Code లో ఒక టెర్మినల్ విండో (సూచి: **Ctrl+J**) ఓపెన్ చేసి `olive-ai` conda ఎన్‌విరాన్‌మెంట్ యాక్టివేట్ అయ్యిందో లేదో చూసుకోండి:

```bash
conda activate olive-ai
```

తర్వాత, క‌మాండ్ లైన్‌లో క్రింది Olive కమాండ్స్‌ను అమలు చేయండి.

1. **డేటాను పరిశీలించండి:** ఈ ఉదాహరణలో, మీరు Phi-3.5-Mini మోడల్‌ను ఫైన్-ట్యూన్ చేయబోతున్నారు, తద్వారా అది ట్రావెల్‌కు సంబంధించిన ప్రశ్నలకు సమాధానాలపై ప్రత్యేకమైనదిగా ఉంటుంది. క్రింది కోడ్ డేటాసెట్ యొక్క మొదటి కొన్ని రికార్డులను ప్రదర్శిస్తుంది, ఇవి JSON లైన్స్ ఫార్మాట్‌లో ఉంటాయి:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **మోడల్‌ను క్వాంటైజ్ చేయండి:** మోడల్‌ను శిక్షణించేముందు, క్రింది కమాండ్ ద్వారా Active Aware Quantization (AWQ) అనే పద్ధతి ఉపయోగించి ముందుగా క్వాంటైజ్ చేస్తారు +++https://arxiv.org/abs/2306.00978+++. AWQ ఇన్ఫరెన్స్ సమయంలో ఉత్పత్తి అయ్యే ఆక్టివేషన్లను పరిగణనలోకి తీసుకుని మోడల్ యొక్క వెయిట్స్‌ను క్వాంటైజ్ చేస్తుంది. అంటే, క్వాంటైజేషన్ ప్రక్రియ ఆక్టివేషన్లలోని వాస్తవ డేటా పంపిణీని పరిగణలోకి తీసుకుంటుంది, ఫలితంగా సంప్రదాయ వెయిట్ క్వాంటైజేషన్ పద్ధతులతో పోలిస్తే మోడల్ ఖచ్చితత్వాన్ని మెరుగ్గా պահպանిస్తుంది.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ క్వాంటైజేషన్ పూర్తి కావడానికి సుమారు **~8 నిమిషాలు** పడుతుంది, ఇది **మోడల్ సైజ్‌ను సుమారు ~7.5GB నుండి ~2.5GB**కి తగ్గిస్తుంది.
   
   ఈ ల్యాబ్‌లో, మేము Hugging Face నుండి మోడల్స్ ఎలా ఇన్పుట్ చేయాలో చూపిస్తున్నాం (ఉదాహరణకు: `microsoft/Phi-3.5-mini-instruct`). అయితే, Olive మీకు Azure AI క్యాటలాగ్ నుండి కూడా మోడల్స్ ఇన్పుట్ చేయడానికి అనుమతిస్తుంది — అందుకోసం `model_name_or_path` ఆర్గ్యుమెంట్‌ను Azure AI ఆస్తి ID‌గా (ఉదాహరణకి: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) అప్‌డేట్ చేయండి। 

1. **మోడల్‌ను శిక్షణ ఇవ్వండి:** తర్వాత, `olive finetune` కమాండ్ క్వాంటైజ్ చేసిన మోడల్‌ను ఫైన్-ట్యూన్ చేస్తుంది. క్వాంటైజింగ్‌ను ఫైన్-ట్యూనింగ్‌కు ముందు చేయడం తరువాత కాకుండా చేయడం వల్ల మెరుగైన ఖచ్చితత్వం వస్తుంది, ఎందుకంటే ఫైన్-ట్యూనింగ్ ప్రక్రియ క్వాంటైజేషన్ వల్ల జరిగాన్న కొంత నష్టాన్ని పునరావృతం చేస్తుంది.
    
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
    
    ఫైన్-ట్యూనింగ్ పూర్తి చేయడానికి (100 స్టెప్స్‌తో) సుమారు **~6 నిమిషాలు** పడుతుంది।

1. **ఆప్టిమైజ్ చేయండి:** మోడల్ శిక్షణ పొందిన తర్వాత, మీరు Olive యొక్క `auto-opt` కమాండ్ ఉపయోగించి మోడల్‌ను ఆప్టిమైజ్ చేస్తారు, ఇది ONNX గ్రాఫ్‌ను క్యాప్చర్ చేసి CPU కోసం మోడల్ పనితీరును మెరుగుపరచడానికి కొన్ని ఆప్టిమైజేషన్లు స్వయంచాలకంగా చేస్తుంది — మోడల్‌ను కంప్రెస్ చేయడం మరియు ఫ్యూజన్లను చేయడం ద్వారా. గమనించదగ్గ విషయం ఏమిటంటే, మీరు `--device` మరియు `--provider` ఆర్గ్యుమెంట్లను మార్చించి ఇతర డివైసుల కోసం (ఉదా: NPU లేదా GPU) కూడా ఆప్టిమైజ్ చేయవచ్చు — కానీ ఈ ల్యాబ్ కోసం మనం CPU ని ఉపయోగిస్తాం.
    
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
    
    ఆప్టిమైజేషన్ పూర్తి చేయడానికి సుమారు **~5 నిమిషాలు** పడుతుంది।

### దశ 5: మోడల్ ఇన్ఫరెన్స్ త్వరిత పరీక్ష

మోడల్ ఇన్ఫరెన్సును పరీక్షించడానికి, మీ ఫోల్డర్‌లో **app.py** అనే ఒక Python ఫైల్ క్రియేట్ చేసి క్రింద ఇవ్వబడిన కోడ్‌ను కాపీ చేసి పేస్ట్ చేయండి:

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

### దశ 6: మోడల్‌ను Azure AIకు అప్లోడ్ చేయండి

మోడల్‌ను Azure AI మోడల్ రిపాజిటరీకి అప్లోడ్ చేయడం ద్వారా ఆ మోడల్‌ను మీ డెవలప్‌మెంట్ టీమ్ సభ్యులతో షేర్ చేయగలుగుతారు మరియు మోడల్ యొక్క వెర్షన్ నియంత్రణను కూడా నిర్వహించవచ్చు. మోడల్‌ను అప్లోడ్ చేయడానికి క్రింది కమాండ్‌ను అమలు చేయండి:

> [!NOTE]
> `{}` ప్లేస్‌హోల్డర్లు మీ రిసోర్స్ గ్రూప్ మరియు Azure AI ప్రాజెక్ట్ పేరుతో అప్డేట్ చేయండి. 

మీ resource group `"resourceGroup"and Azure AI Project name కనుగొనడానికి, క్రింది కమాండ్‌ను అమలు చేయండి 

```
az ml workspace show
```

లేదా +++ai.azure.com+++ కు వెళ్ళి **management center** **project** **overview** ఎంచుకోవచ్చు

`{}` ప్లేస్‌హోల్డర్లను మీ రిసోర్స్ గ్రూప్ మరియు Azure AI ప్రాజెక్ట్ పేరుతో అప్డేట్ చేయండి.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
మీరు అప్పుడు మీ అప్లోడ్ చేయబడిన మోడల్‌ను చూడగలరని మరియు మీ మోడల్‌ను https://ml.azure.com/model/list వద్ద డిప్లాయ్ చేయవచ్చు

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ Co-op Translator (https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి విజృంభించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండే అవకాశం ఉందని దయచేసి గమనించండి. మూల భాషలోని అసలు పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి, వృత్తిపరమైన మానవ అనువాదంను సిఫార్సు చేస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల ఏర్పడే ఏవైనా అపార్థాలు లేదా తప్పుదోషాల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->