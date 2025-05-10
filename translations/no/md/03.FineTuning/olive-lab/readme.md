<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T22:37:55+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "no"
}
-->
# Lab. Optimaliser AI-modeller for inferens på enhet

## Introduksjon

> [!IMPORTANT]  
> Dette laboratoriet krever et **Nvidia A10 eller A100 GPU** med tilhørende drivere og CUDA toolkit (versjon 12+) installert.

> [!NOTE]  
> Dette er et **35-minutters** lab som gir deg en praktisk introduksjon til kjernebegrepene for optimalisering av modeller for inferens på enhet ved bruk av OLIVE.

## Læringsmål

Ved slutten av dette laboratoriet vil du kunne bruke OLIVE til å:

- Kvantisere en AI-modell ved hjelp av AWQ kvantiseringsmetode.  
- Finjustere en AI-modell for en spesifikk oppgave.  
- Generere LoRA-adaptere (finjustert modell) for effektiv inferens på enhet med ONNX Runtime.

### Hva er Olive

Olive (*O*NNX *live*) er et verktøy for modelloptimalisering med tilhørende CLI som lar deg distribuere modeller for ONNX runtime +++https://onnxruntime.ai+++ med høy kvalitet og ytelse.

![Olive Flow](../../../../../translated_images/olive-flow.9e6a284c256068568eb569a242b22dd2e7ec6e73f292d98272398739537ef513.no.png)

Input til Olive er vanligvis en PyTorch- eller Hugging Face-modell, og output er en optimalisert ONNX-modell som kjøres på en enhet (distribusjonsmål) med ONNX runtime. Olive optimaliserer modellen for AI-akseleratoren til distribusjonsmålet (NPU, GPU, CPU) levert av en maskinvareleverandør som Qualcomm, AMD, Nvidia eller Intel.

Olive kjører et *workflow*, som er en sekvens av individuelle modelloptimaliseringsoppgaver kalt *passes* – eksempler på passes inkluderer: modellkomprimering, graffangst, kvantisering, grafoptimalisering. Hver pass har et sett med parametere som kan justeres for å oppnå de beste målene, for eksempel nøyaktighet og latenstid, som evalueres av en evaluator. Olive bruker en søkestrategi som benytter en søkealgoritme for å auto-tune hver pass én etter én eller et sett med passes samtidig.

#### Fordeler med Olive

- **Reduser frustrasjon og tid** brukt på prøving og feiling med ulike teknikker for grafoptimalisering, komprimering og kvantisering. Definer dine kvalitets- og ytelseskrav, og la Olive automatisk finne den beste modellen for deg.  
- **40+ innebygde modelloptimaliseringskomponenter** som dekker banebrytende teknikker innen kvantisering, komprimering, grafoptimalisering og finjustering.  
- **Brukervennlig CLI** for vanlige modelloptimaliseringsoppgaver, for eksempel olive quantize, olive auto-opt, olive finetune.  
- Modellpakking og distribusjon innebygd.  
- Støtter generering av modeller for **Multi LoRA serving**.  
- Lag workflows med YAML/JSON for å orkestrere modelloptimalisering og distribusjonsoppgaver.  
- **Hugging Face** og **Azure AI** integrasjon.  
- Innebygd **caching** for å **spare kostnader**.

## Lab instruksjoner

> [!NOTE]  
> Sørg for at du har opprettet din Azure AI Hub og prosjekt, og satt opp A100 compute i henhold til Lab 1.

### Steg 0: Koble til Azure AI Compute

Du kobler til Azure AI compute ved hjelp av fjernfunksjonen i **VS Code**.

1. Åpne **VS Code** skrivebordsapplikasjonen:  
1. Åpne **command palette** med **Shift+Ctrl+P**  
1. Søk i command palette etter **AzureML - remote: Connect to compute instance in New Window**.  
1. Følg instruksjonene på skjermen for å koble til Compute. Dette innebærer å velge Azure Subscription, Resource Group, Project og Compute-navnet du opprettet i Lab 1.  
1. Når du er koblet til Azure ML Compute-noden vises dette i **nederst til venstre i Visual Code** `><Azure ML: Compute Name`

### Steg 1: Klon dette repoet

I VS Code kan du åpne en ny terminal med **Ctrl+J** og klone dette repoet:

I terminalen vil du se prompten

```
azureuser@computername:~/cloudfiles/code$ 
```  
Klon løsningen

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Steg 2: Åpne mappe i VS Code

For å åpne VS Code i riktig mappe, kjør følgende kommando i terminalen som åpner et nytt vindu:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativt kan du åpne mappen ved å velge **File** > **Open Folder**.

### Steg 3: Avhengigheter

Åpne en terminal i VS Code på din Azure AI Compute-instans (tips: **Ctrl+J**) og kjør følgende kommandoer for å installere avhengigheter:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> Det tar ca. 5 minutter å installere alle avhengigheter.

I dette laboratoriet laster du ned og laster opp modeller til Azure AI Model-katalogen. For å få tilgang til modellkatalogen må du logge inn på Azure med:

```bash
az login
```

> [!NOTE]  
> Ved innlogging blir du bedt om å velge abonnement. Sørg for å sette abonnementet til det som er oppgitt for dette lab.

### Steg 4: Kjør Olive-kommandoer

Åpne en terminal i VS Code på din Azure AI Compute-instans (tips: **Ctrl+J**) og sørg for at `olive-ai` conda-miljøet er aktivert:

```bash
conda activate olive-ai
```

Kjør deretter følgende Olive-kommandoer i terminalen.

1. **Inspiser dataene:** I dette eksempelet skal du finjustere Phi-3.5-Mini-modellen slik at den blir spesialisert på å svare på reiserelaterte spørsmål. Koden under viser de første postene i datasettet, som er i JSON lines-format:

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **Kvantisér modellen:** Før trening kvantiserer du modellen med følgende kommando som bruker en teknikk kalt Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kvantiserer vektene i en modell ved å ta hensyn til aktivasjonene som produseres under inferens. Det betyr at kvantiseringsprosessen tar hensyn til den faktiske datadistribusjonen i aktivasjonene, noe som gir bedre bevaring av modellens nøyaktighet sammenlignet med tradisjonelle vektskvantiseringsmetoder.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Kvantiseringen tar **ca. 8 minutter** og vil **redusere modellstørrelsen fra ca. 7,5GB til ca. 2,5GB**.

    I dette lab viser vi hvordan du kan hente modeller fra Hugging Face (for eksempel: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune`-kommandoen finjusterer den kvantiserte modellen. Kvantisering *før* finjustering gir bedre nøyaktighet, da finjusteringsprosessen gjenoppretter noe av tapet fra kvantiseringen.

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

    Finjusteringen tar **ca. 6 minutter** (med 100 steg).

1. **Optimaliser:** Når modellen er trent, optimaliserer du modellen med Olive's `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` argumenter – men for dette lab bruker vi CPU.

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

    Optimaliseringen tar **ca. 5 minutter**.

### Steg 5: Rask test av modell-inferens

For å teste inferens av modellen, lag en Python-fil i mappen din kalt **app.py** og lim inn følgende kode:

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

Kjør koden med:

```bash
python app.py
```

### Steg 6: Last opp modell til Azure AI

Å laste opp modellen til et Azure AI modellarkiv gjør modellen delbar med andre i utviklingsteamet ditt og håndterer også versjonskontroll. For å laste opp modellen, kjør følgende kommando:

> [!NOTE]  
> Oppdater `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` og Azure AI prosjektets navn, kjør så følgende kommando:

```
az ml workspace show
```

Alternativt kan du gå til +++ai.azure.com+++ og velge **management center** > **project** > **overview**

Oppdater `{}`-plassholderne med navnet på din resource group og Azure AI prosjekt.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Du kan deretter se den opplastede modellen og distribuere den på https://ml.azure.com/model/list

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruk av denne oversettelsen.