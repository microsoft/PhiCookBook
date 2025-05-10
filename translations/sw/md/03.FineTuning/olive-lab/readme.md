<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T22:39:57+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "sw"
}
-->
# Lab. Optimize AI models for on-device inference

## Introduction 

> [!IMPORTANT]
> Lab hii inahitaji **Nvidia A10 au A100 GPU** pamoja na madereva yake na CUDA toolkit (toleo 12+) imewekwa.

> [!NOTE]
> Huu ni mafunzo ya **dakika 35** yatakayokupa ufahamu wa vitendo kuhusu dhana kuu za kuboresha modeli kwa ajili ya on-device inference ukitumia OLIVE.

## Malengo ya Kujifunza

Mwisho wa mafunzo haya, utaweza kutumia OLIVE kufanya:

- Kuquantize AI Model kwa kutumia njia ya AWQ quantization.
- Kufanya fine-tune ya AI modeli kwa kazi maalum.
- Kutengeneza LoRA adapters (modeli iliyofinyangwa) kwa inference bora kwenye kifaa kwa kutumia ONNX Runtime.

### Olive ni Nini

Olive (*O*NNX *live*) ni kifaa cha kuboresha modeli chenye CLI kinachokuwezesha kusafirisha modeli kwa ONNX runtime +++https://onnxruntime.ai+++ kwa ubora na utendaji.

![Olive Flow](../../../../../translated_images/olive-flow.9e6a284c256068568eb569a242b22dd2e7ec6e73f292d98272398739537ef513.sw.png)

Kuingia kwa Olive kawaida ni modeli ya PyTorch au Hugging Face na matokeo ni modeli ya ONNX iliyoboreshwa ambayo inatekelezwa kwenye kifaa kinachotumia ONNX runtime. Olive itaboresha modeli kwa ajili ya AI accelerator ya kifaa hicho (NPU, GPU, CPU) kinachotolewa na muuzaji wa vifaa kama Qualcomm, AMD, Nvidia au Intel.

Olive hufanya *workflow*, ambayo ni mfuatano wa kazi za kuboresha modeli zinazoitwa *passes* - mifano ya passes ni: kubana modeli, kunasa grafu, quantization, kuboresha grafu. Kila pass ina seti ya vigezo vinavyoweza kubadilishwa ili kupata viwango bora, kama usahihi na latency, vinavyopimwa na evaluator husika. Olive hutumia mkakati wa utafutaji kwa kutumia algorithm ya utafutaji kurekebisha kila pass moja baada ya nyingine au seti ya passes pamoja.

#### Manufaa ya Olive

- **Punguza usumbufu na muda** wa majaribio ya majaribio kwa mikono ya mbinu tofauti za kuboresha grafu, kubana na quantization. Eleza viwango vyako vya ubora na utendaji na uweke Olive iupate modeli bora kwako moja kwa moja.
- **Vipengele 40+ vya kuboresha modeli** vinavyohusisha mbinu za kisasa za quantization, kubana, kuboresha grafu na fine-tuning.
- **CLI rahisi kutumia** kwa kazi za kawaida za kuboresha modeli. Mfano, olive quantize, olive auto-opt, olive finetune.
- Ufungaji na usambazaji wa modeli umejumuishwa.
- Inasaidia kuzalisha modeli kwa ajili ya **Multi LoRA serving**.
- Tengeneza workflows kwa kutumia YAML/JSON kuongoza kazi za kuboresha na kusambaza modeli.
- Uunganisho na **Hugging Face** na **Azure AI**.
- Mfumo wa **caching** umejumuishwa ili **kuokoa gharama**.

## Maelekezo ya Mafunzo
> [!NOTE]
> Tafadhali hakikisha umeandaa Azure AI Hub na Mradi wako na umeanzisha A100 compute kama ilivyoelezwa katika Lab 1.

### Hatua 0: Unganisha na Azure AI Compute yako

Utaungana na Azure AI compute kwa kutumia kipengele cha remote katika **VS Code.** 

1. Fungua programu ya **VS Code** kwenye desktop:
1. Fungua **command palette** kwa kutumia **Shift+Ctrl+P**
1. Katika command palette tafuta **AzureML - remote: Connect to compute instance in New Window**.
1. Fuata maelekezo kwenye skrini kuungana na Compute. Hii itahusisha kuchagua Azure Subscription yako, Resource Group, Mradi na Jina la Compute uliloanzisha katika Lab 1.
1. Mara utakapounganishwa na Azure ML Compute node itajitokeza upande wa **chini kushoto wa Visual Code** `><Azure ML: Compute Name`

### Hatua 1: Clone repo hii

Katika VS Code, unaweza kufungua terminal mpya kwa **Ctrl+J** na ukaclone repo hii:

Katika terminal utaona prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Clone suluhisho

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Hatua 2: Fungua Folda katika VS Code

Ili kufungua VS Code katika folda husika tumia amri ifuatayo kwenye terminal, itafungua dirisha jipya:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Vinginevyo, unaweza kufungua folda kwa kuchagua **File** > **Open Folder**. 

### Hatua 3: Dependencies

Fungua terminal katika VS Code kwenye Azure AI Compute Instance yako (kumbuka: **Ctrl+J**) na fanya amri zifuatazo kusakinisha dependencies:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Itachukua takriban dakika 5 kusakinisha dependencies zote.

Katika mafunzo haya utapakua na kupakia modeli kwenye Azure AI Model catalog. Ili kupata katalogi ya modeli, itabidi uingie Azure kwa kutumia:

```bash
az login
```

> [!NOTE]
> Wakati wa kuingia utaombwa kuchagua subscription yako. Hakikisha unachagua subscription iliyotolewa kwa mafunzo haya.

### Hatua 4: Endesha amri za Olive

Fungua terminal katika VS Code kwenye Azure AI Compute Instance yako (kumbuka: **Ctrl+J**) na hakikisha mazingira ya conda `olive-ai` yamewashwa:

```bash
conda activate olive-ai
```

Kisha, endesha amri zifuatazo za Olive kwenye mstari wa amri.

1. **Kagua data:** Katika mfano huu, utafanya fine-tune ya modeli ya Phi-3.5-Mini ili iwe maalum kujibu maswali yanayohusiana na usafiri. Msimbo huu unaonyesha rekodi za mwanzo za dataset, ambazo ziko katika muundo wa JSON lines:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Quantize modeli:** Kabla ya kufundisha modeli, kwanza unafanya quantize kwa kutumia amri ifuatayo inayotumia mbinu inayoitwa Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ huchanganua uzito wa modeli kwa kuzingatia aktivishaji zinazozalishwa wakati wa inference. Hii ina maana mchakato wa quantization unazingatia usambazaji halisi wa data katika aktivishaji, na hivyo kuhifadhi usahihi wa modeli zaidi ikilinganishwa na mbinu za jadi za quantization ya uzito.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Inachukua takriban **dakika 8** kumaliza AWQ quantization, ambayo itapunguza ukubwa wa modeli kutoka takriban ~7.5GB hadi ~2.5GB.
   
   Katika mafunzo haya, tunaonyesha jinsi ya kuingiza modeli kutoka Hugging Face (mfano: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` amri hufinyanga modeli iliyoqantizewa. Kuquantize modeli *kabla* ya fine-tuning badala ya baada yake hutoa usahihi bora kwa kuwa mchakato wa fine-tuning hurudisha baadhi ya hasara iliyosababishwa na quantization.
    
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
    
    Inachukua takriban **dakika 6** kumaliza Fine-tuning (kwa hatua 100).

1. **Boresha:** Baada ya kufundisha modeli, sasa boresha modeli kwa kutumia amri za Olive `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` - lakini kwa mafunzo haya tutatumia CPU.

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
    
    Inachukua takriban **dakika 5** kumaliza uboreshaji.

### Hatua 5: Jaribio la haraka la inference ya modeli

Ili kujaribu inference ya modeli, tengeneza faili la Python katika folda yako linaloitwa **app.py** na nakili na ubandike msimbo ufuatao:

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

Endesha msimbo kwa kutumia:

```bash
python app.py
```

### Hatua 6: Pakia modeli kwenye Azure AI

Kuweka modeli kwenye hifadhidata ya modeli ya Azure AI kunafanya modeli iweze kushirikiwa na wanachama wengine wa timu yako ya maendeleo na pia hurekodi toleo la modeli. Ili kupakia modeli tumia amri ifuatayo:

> [!NOTE]
> Sasisha `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` na jina la Mradi wa Azure AI, kisha tumia amri ifuatayo 

```
az ml workspace show
```

Au kwa kwenda +++ai.azure.com+++ na kuchagua **management center** **project** **overview**

Sasisha nafasi za `{}` kwa jina la resource group yako na Azure AI Project Name.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Baada ya hapo utaweza kuona modeli uliyoipakia na kuitumia kusambaza kwenye https://ml.azure.com/model/list

**Kiasi cha Majaribio**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asilia katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.