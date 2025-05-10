<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T04:38:55+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "da"
}
-->
# Lab. Optimer AI-modeller til inferens på enheden

## Introduktion

> [!IMPORTANT]  
> Dette lab kræver et **Nvidia A10 eller A100 GPU** med tilhørende drivere og CUDA toolkit (version 12+) installeret.

> [!NOTE]  
> Dette er et **35-minutters** lab, som giver dig en praktisk introduktion til de grundlæggende koncepter for optimering af modeller til inferens på enheden ved hjælp af OLIVE.

## Læringsmål

Når du er færdig med dette lab, vil du kunne bruge OLIVE til at:

- Kvantisere en AI-model ved hjælp af AWQ-kvantisering.
- Finjustere en AI-model til en specifik opgave.
- Generere LoRA-adaptere (finjusteret model) til effektiv inferens på enheden med ONNX Runtime.

### Hvad er Olive

Olive (*O*NNX *live*) er et værktøj til modeloptimering med tilhørende CLI, der gør det muligt at levere modeller til ONNX runtime +++https://onnxruntime.ai+++ med høj kvalitet og ydeevne.

![Olive Flow](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.da.png)

Input til Olive er typisk en PyTorch- eller Hugging Face-model, og output er en optimeret ONNX-model, som køres på en enhed (deploymentsmål) med ONNX runtime. Olive optimerer modellen til deploymentsmålets AI-accelerator (NPU, GPU, CPU) leveret af hardwareleverandører som Qualcomm, AMD, Nvidia eller Intel.

Olive udfører et *workflow*, som er en sekvens af individuelle modeloptimeringsopgaver kaldet *passes* – eksempelvis modelkomprimering, grafoptagelse, kvantisering, grafoptimering. Hver pass har et sæt parametre, der kan justeres for at opnå de bedste målinger, som f.eks. nøjagtighed og latenstid, som evalueres af den respektive evaluator. Olive anvender en søgestrategi, der bruger en søgealgoritme til automatisk at finjustere hver pass én efter én eller en gruppe passes sammen.

#### Fordele ved Olive

- **Reducer frustration og tid** ved manuel prøve-og-fejl eksperimentering med forskellige teknikker til grafoptimering, komprimering og kvantisering. Definér dine kvalitets- og ydelseskrav, og lad Olive automatisk finde den bedste model for dig.  
- **40+ indbyggede modeloptimeringskomponenter** der dækker avancerede teknikker inden for kvantisering, komprimering, grafoptimering og finjustering.  
- **Brugervenlig CLI** til almindelige modeloptimeringsopgaver. For eksempel: olive quantize, olive auto-opt, olive finetune.  
- Indbygget modelpakning og deployment.  
- Understøtter generering af modeller til **Multi LoRA serving**.  
- Byg workflows med YAML/JSON til at orkestrere modeloptimering og deploymentopgaver.  
- **Hugging Face** og **Azure AI** integration.  
- Indbygget **caching** mekanisme til at **sænke omkostninger**.

## Lab Instruktioner

> [!NOTE]  
> Sørg for at have provisioneret dit Azure AI Hub og Project og sat din A100 compute op som beskrevet i Lab 1.

### Trin 0: Forbind til din Azure AI Compute

Du forbinder til Azure AI compute ved hjælp af remote-funktionen i **VS Code.**

1. Åbn din **VS Code** desktop applikation:  
2. Åbn **command palette** med **Shift+Ctrl+P**  
3. Søg i command palette efter **AzureML - remote: Connect to compute instance in New Window**.  
4. Følg instruktionerne på skærmen for at forbinde til Compute. Det indebærer at vælge dit Azure Subscription, Resource Group, Project og Compute-navnet, du opsatte i Lab 1.  
5. Når du er forbundet til din Azure ML Compute node, vises det i **nederste venstre hjørne af Visual Code** `><Azure ML: Compute Name`

### Trin 1: Klon dette repo

I VS Code kan du åbne et nyt terminalvindue med **Ctrl+J** og klone dette repo:

I terminalen bør du se prompten

```
azureuser@computername:~/cloudfiles/code$ 
```  
Klon løsningen  

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Trin 2: Åbn mappe i VS Code

For at åbne VS Code i den relevante mappe, kør følgende kommando i terminalen, som åbner et nyt vindue:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativt kan du åbne mappen ved at vælge **File** > **Open Folder**.

### Trin 3: Afhængigheder

Åbn et terminalvindue i VS Code på din Azure AI Compute Instance (tip: **Ctrl+J**) og kør følgende kommandoer for at installere afhængighederne:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> Det tager ca. 5 minutter at installere alle afhængigheder.

I dette lab downloader og uploader du modeller til Azure AI Model kataloget. For at få adgang til modelkataloget skal du logge ind på Azure med:

```bash
az login
```

> [!NOTE]  
> Ved login bliver du bedt om at vælge dit abonnement. Sørg for at vælge det abonnement, der er angivet til dette lab.

### Trin 4: Kør Olive-kommandoer

Åbn et terminalvindue i VS Code på din Azure AI Compute Instance (tip: **Ctrl+J**) og sørg for, at `olive-ai` conda-miljøet er aktiveret:

```bash
conda activate olive-ai
```

Kør derefter følgende Olive-kommandoer i terminalen.

1. **Undersøg dataene:** I dette eksempel finjusterer du Phi-3.5-Mini modellen, så den bliver specialiseret i at besvare rejserelaterede spørgsmål. Koden nedenfor viser de første par poster i datasættet, som er i JSON lines format:

   ```bash
    head data/data_sample_travel.jsonl
    ```

1. **Kvantisér modellen:** Før træning kvantiserer du modellen med følgende kommando, som bruger en teknik kaldet Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kvantiserer modellens vægte ved at tage højde for aktiveringerne, der produceres under inferens. Det betyder, at kvantiseringsprocessen tager hensyn til den faktiske datadistribution i aktiveringerne, hvilket bevarer modellens nøjagtighed bedre sammenlignet med traditionelle vægtkvantiseringsmetoder.

   ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

   Det tager **ca. 8 minutter** at gennemføre AWQ-kvantiseringen, som vil **reducere modelstørrelsen fra ca. 7,5GB til ca. 2,5GB**.

   I dette lab viser vi, hvordan du kan hente modeller fra Hugging Face (for eksempel: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` kommandoen finjusterer den kvantiserede model. At kvantisere modellen *før* finjustering i stedet for efter giver bedre nøjagtighed, da finjusteringen genvinder noget af det tab, der opstår ved kvantisering.

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

   Det tager **ca. 6 minutter** at gennemføre finjusteringen (med 100 steps).

1. **Optimer:** Når modellen er trænet, optimerer du den ved hjælp af Olives `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` argumenter – men til dette lab bruger vi CPU.

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

   Det tager **ca. 5 minutter** at gennemføre optimeringen.

### Trin 5: Hurtig test af modelinferens

For at teste inferensen af modellen, opret en Python-fil i din mappe kaldet **app.py** og kopier følgende kode ind:

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

Kør koden med:

```bash
python app.py
```

### Trin 6: Upload model til Azure AI

At uploade modellen til et Azure AI modelrepository gør modellen delbar med andre på dit udviklingsteam og håndterer også versionsstyring af modellen. For at uploade modellen, kør følgende kommando:

> [!NOTE]  
> Opdater `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` og Azure AI Project navn, og kør derefter kommandoen

```
az ml workspace show
```

Eller gå til +++ai.azure.com+++ og vælg **management center** > **project** > **overview**

Opdater `{}` pladsholderne med navnet på din resource group og Azure AI Project navn.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Du kan derefter se din uploadede model og deploye den på https://ml.azure.com/model/list

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For vigtig information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.