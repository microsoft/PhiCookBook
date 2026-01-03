<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-17T10:20:40+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "sv"
}
-->
# Lab. Optimera AI-modeller för inferens på enheten

## Introduktion

> [!IMPORTANT]  
> Denna labb kräver ett **Nvidia A10 eller A100 GPU** med tillhörande drivrutiner och CUDA toolkit (version 12+) installerade.

> [!NOTE]  
> Detta är en **35-minuters** labb som ger dig en praktisk introduktion till kärnkoncepten för att optimera modeller för inferens på enheten med hjälp av OLIVE.

## Lärandemål

I slutet av denna labb kommer du att kunna använda OLIVE för att:

- Kvantisera en AI-modell med AWQ-kvantisering.
- Finjustera en AI-modell för en specifik uppgift.
- Generera LoRA-adaptrar (finjusterad modell) för effektiv inferens på enheten med ONNX Runtime.

### Vad är Olive

Olive (*O*NNX *live*) är ett verktyg för modelloptimering med tillhörande CLI som gör det möjligt att leverera modeller för ONNX runtime +++https://onnxruntime.ai+++ med hög kvalitet och prestanda.

![Olive Flow](../../../../../translated_images/olive-flow.5daf97340275f8b6.sv.png)

Inmatningen till Olive är vanligtvis en PyTorch- eller Hugging Face-modell och utmatningen är en optimerad ONNX-modell som körs på en enhet (distributionsmål) med ONNX runtime. Olive optimerar modellen för distributionsmålets AI-accelerator (NPU, GPU, CPU) från en hårdvaruleverantör som Qualcomm, AMD, Nvidia eller Intel.

Olive kör ett *arbetsflöde*, vilket är en ordnad sekvens av individuella modelloptimeringsuppgifter kallade *passes* – exempel på passes är: modellkomprimering, grafinspelning, kvantisering, grafoptimering. Varje pass har en uppsättning parametrar som kan justeras för att uppnå bästa möjliga mått, till exempel noggrannhet och latens, som utvärderas av respektive evaluator. Olive använder en sökstrategi som använder en sökalgoritm för att automatiskt finjustera varje pass en efter en eller flera passes tillsammans.

#### Fördelar med Olive

- **Minska frustration och tid** för manuella försök och fel med olika tekniker för grafoptimering, komprimering och kvantisering. Definiera dina kvalitets- och prestandakrav och låt Olive automatiskt hitta den bästa modellen åt dig.
- **40+ inbyggda komponenter för modelloptimering** som täcker de senaste teknikerna inom kvantisering, komprimering, grafoptimering och finjustering.
- **Enkel CLI** för vanliga modelloptimeringsuppgifter. Till exempel, olive quantize, olive auto-opt, olive finetune.
- Inbyggd paketering och distribution av modeller.
- Stöd för att generera modeller för **Multi LoRA serving**.
- Bygg arbetsflöden med YAML/JSON för att orkestrera modelloptimering och distributionsuppgifter.
- **Hugging Face** och **Azure AI** integration.
- Inbyggd **cache-mekanism** för att **spara kostnader**.

## Labbinstruktioner

> [!NOTE]  
> Säkerställ att du har provisionerat din Azure AI Hub och projekt samt konfigurerat din A100-beräkning enligt Lab 1.

### Steg 0: Anslut till din Azure AI Compute

Du ansluter till Azure AI compute med fjärrfunktionen i **VS Code**.

1. Öppna din **VS Code** desktop-applikation:  
2. Öppna **kommandopaletten** med **Shift+Ctrl+P**  
3. Sök i kommandopaletten efter **AzureML - remote: Connect to compute instance in New Window**.  
4. Följ instruktionerna på skärmen för att ansluta till Compute. Detta innebär att du väljer din Azure-prenumeration, resursgrupp, projekt och Compute-namn som du satte upp i Lab 1.  
5. När du är ansluten till din Azure ML Compute-nod visas detta längst ner till vänster i Visual Code `><Azure ML: Compute Name`

### Steg 1: Klona detta repo

I VS Code kan du öppna en ny terminal med **Ctrl+J** och klona detta repo:

I terminalen bör du se prompten

```
azureuser@computername:~/cloudfiles/code$ 
```  
Klona lösningen

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Steg 2: Öppna mappen i VS Code

För att öppna VS Code i rätt mapp, kör följande kommando i terminalen, vilket öppnar ett nytt fönster:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativt kan du öppna mappen genom att välja **File** > **Open Folder**.

### Steg 3: Beroenden

Öppna ett terminalfönster i VS Code på din Azure AI Compute-instans (tips: **Ctrl+J**) och kör följande kommandon för att installera beroenden:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> Det tar cirka 5 minuter att installera alla beroenden.

I denna labb kommer du att ladda ner och ladda upp modeller till Azure AI Model-katalogen. För att kunna komma åt modellkatalogen behöver du logga in i Azure med:

```bash
az login
```

> [!NOTE]  
> Vid inloggning kommer du att bli ombedd att välja din prenumeration. Se till att du väljer den prenumeration som tillhandahålls för denna labb.

### Steg 4: Kör Olive-kommandon

Öppna ett terminalfönster i VS Code på din Azure AI Compute-instans (tips: **Ctrl+J**) och se till att `olive-ai` conda-miljön är aktiverad:

```bash
conda activate olive-ai
```

Kör sedan följande Olive-kommandon i kommandoraden.

1. **Inspektera datan:** I detta exempel ska du finjustera Phi-3.5-Mini-modellen så att den specialiseras på att svara på rese-relaterade frågor. Koden nedan visar de första posterna i datasetet, som är i JSON lines-format:

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **Kvantisera modellen:** Innan du tränar modellen kvantiserar du den med följande kommando som använder en teknik kallad Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kvantiserar modellens vikter genom att ta hänsyn till de aktiveringar som produceras under inferens. Det innebär att kvantiseringsprocessen tar hänsyn till den faktiska datadistributionen i aktiveringarna, vilket leder till bättre bevarande av modellens noggrannhet jämfört med traditionella viktskvantiseringsmetoder.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Det tar **cirka 8 minuter** att slutföra AWQ-kvantiseringen, vilket **minskar modellstorleken från cirka 7,5 GB till cirka 2,5 GB**.

    I denna labb visar vi hur du kan mata in modeller från Hugging Face (till exempel: `microsoft/Phi-3.5-mini-instruct`). Olive tillåter också att du matar in modeller från Azure AI-katalogen genom att uppdatera argumentet `model_name_or_path` till en Azure AI asset ID (till exempel: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

1. **Träna modellen:** Nästa steg är att `olive finetune` finjusterar den kvantiserade modellen. Att kvantisera modellen *innan* finjustering ger bättre noggrannhet eftersom finjusteringsprocessen återhämtar en del av förlusten från kvantiseringen.

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

    Det tar **cirka 6 minuter** att slutföra finjusteringen (med 100 steg).

1. **Optimera:** När modellen är tränad optimerar du den med Olives `auto-opt`-kommando, som fångar ONNX-grafen och automatiskt utför flera optimeringar för att förbättra modellens prestanda för CPU genom att komprimera modellen och göra fusioner. Det bör noteras att du även kan optimera för andra enheter som NPU eller GPU genom att bara uppdatera argumenten `--device` och `--provider` – men för denna labb använder vi CPU.

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

    Det tar **cirka 5 minuter** att slutföra optimeringen.

### Steg 5: Snabbtest av modellinferens

För att testa inferens av modellen, skapa en Python-fil i din mapp som heter **app.py** och kopiera in följande kod:

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

Kör koden med:

```bash
python app.py
```

### Steg 6: Ladda upp modell till Azure AI

Att ladda upp modellen till ett Azure AI-modellförråd gör modellen delbar med andra i ditt utvecklingsteam och hanterar även versionskontroll av modellen. För att ladda upp modellen kör följande kommando:

> [!NOTE]  
> Uppdatera `{}`-platshållarna med namnet på din resursgrupp och Azure AI-projektnamn.

För att hitta din resursgrupp `"resourceGroup"` och Azure AI-projektnamn, kör följande kommando

```
az ml workspace show
```

Eller gå till +++ai.azure.com+++ och välj **management center** > **project** > **overview**

Uppdatera `{}`-platshållarna med namnet på din resursgrupp och Azure AI-projektnamn.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Du kan sedan se din uppladdade modell och distribuera den på https://ml.azure.com/model/list

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.