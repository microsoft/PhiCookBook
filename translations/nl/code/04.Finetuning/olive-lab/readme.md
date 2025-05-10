<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T04:39:45+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "nl"
}
-->
# Lab. Optimaliseer AI-modellen voor on-device inferentie

## Introductie

> [!IMPORTANT]  
> Deze lab vereist een **Nvidia A10 of A100 GPU** met bijbehorende drivers en CUDA toolkit (versie 12+) geïnstalleerd.

> [!NOTE]  
> Dit is een **35 minuten** durende lab die je een praktische introductie geeft in de kernconcepten van het optimaliseren van modellen voor on-device inferentie met OLIVE.

## Leerdoelen

Aan het einde van deze lab kun je met OLIVE:

- Een AI-model kwantiseren met de AWQ-kwantisatiemethode.  
- Een AI-model fijn afstemmen voor een specifieke taak.  
- LoRA-adapters genereren (fijn afgesteld model) voor efficiënte on-device inferentie op de ONNX Runtime.

### Wat is Olive

Olive (*O*NNX *live*) is een toolkit voor modeloptimalisatie met een bijbehorende CLI, waarmee je modellen kunt leveren voor de ONNX runtime +++https://onnxruntime.ai+++ met kwaliteit en performance.

![Olive Flow](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.nl.png)

De input voor Olive is meestal een PyTorch- of Hugging Face-model en de output is een geoptimaliseerd ONNX-model dat wordt uitgevoerd op een apparaat (deploydoel) met de ONNX runtime. Olive optimaliseert het model voor de AI-accelerator (NPU, GPU, CPU) van het deploydoel, geleverd door hardwarefabrikanten zoals Qualcomm, AMD, Nvidia of Intel.

Olive voert een *workflow* uit, een geordende reeks van individuele modeloptimalisatietaken, zogenaamde *passes* – voorbeelden van passes zijn: modelcompressie, graph capture, kwantisatie, graph optimalisatie. Elke pass heeft een set parameters die je kunt afstemmen om de beste metrics te bereiken, zoals nauwkeurigheid en latency, die geëvalueerd worden door de respectievelijke evaluator. Olive gebruikt een zoekstrategie die een algoritme inzet om elke pass één voor één of een set passes samen automatisch af te stemmen.

#### Voordelen van Olive

- **Vermindert frustratie en tijd** van trial-and-error handmatige experimenten met verschillende technieken voor graph optimalisatie, compressie en kwantisatie. Definieer je kwaliteits- en prestatie-eisen en laat Olive automatisch het beste model voor je vinden.  
- **Meer dan 40 ingebouwde modeloptimalisatiecomponenten** die geavanceerde technieken in kwantisatie, compressie, graph optimalisatie en fijn afstemming omvatten.  
- **Gebruiksvriendelijke CLI** voor veelvoorkomende modeloptimalisatietaken, zoals olive quantize, olive auto-opt, olive finetune.  
- Model packaging en deployment zijn ingebouwd.  
- Ondersteunt het genereren van modellen voor **Multi LoRA serving**.  
- Workflows samenstellen met YAML/JSON om modeloptimalisatie- en deploymenttaken te orkestreren.  
- Integratie met **Hugging Face** en **Azure AI**.  
- Ingebouwde **caching** om **kosten te besparen**.

## Lab Instructies

> [!NOTE]  
> Zorg dat je je Azure AI Hub en Project hebt ingericht en je A100 compute hebt ingesteld volgens Lab 1.

### Stap 0: Verbinden met je Azure AI Compute

Je maakt verbinding met de Azure AI compute via de remote-functie in **VS Code**.

1. Open je **VS Code** desktop applicatie:  
2. Open het **command palette** met **Shift+Ctrl+P**  
3. Zoek in het command palette naar **AzureML - remote: Connect to compute instance in New Window**.  
4. Volg de instructies op het scherm om verbinding te maken met de Compute. Dit houdt in dat je je Azure Subscription, Resource Group, Project en Compute naam selecteert die je in Lab 1 hebt ingesteld.  
5. Zodra je verbonden bent met je Azure ML Compute node, wordt dit weergegeven linksonder in Visual Code `><Azure ML: Compute Name`

### Stap 1: Clone deze repo

In VS Code kun je een nieuwe terminal openen met **Ctrl+J** en deze repo clonen:

In de terminal zie je de prompt

```
azureuser@computername:~/cloudfiles/code$ 
```  
Clone de oplossing

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Stap 2: Open map in VS Code

Om VS Code in de juiste map te openen, voer je de volgende opdracht uit in de terminal, dit opent een nieuw venster:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Je kunt ook de map openen via **File** > **Open Folder**.

### Stap 3: Dependencies

Open een terminalvenster in VS Code op je Azure AI Compute Instance (tip: **Ctrl+J**) en voer de volgende commando’s uit om de dependencies te installeren:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> Het installeren van alle dependencies duurt ongeveer 5 minuten.

In deze lab download en upload je modellen naar de Azure AI Model catalogus. Om toegang te krijgen tot de modelcatalogus moet je inloggen op Azure met:

```bash
az login
```

> [!NOTE]  
> Tijdens het inloggen wordt je gevraagd je subscription te selecteren. Zorg dat je de subscription kiest die voor deze lab is opgegeven.

### Stap 4: Voer Olive-commando’s uit

Open een terminalvenster in VS Code op je Azure AI Compute Instance (tip: **Ctrl+J**) en zorg dat de `olive-ai` conda-omgeving actief is:

```bash
conda activate olive-ai
```

Voer vervolgens de volgende Olive-commando’s uit in de command line.

1. **Inspecteer de data:** In dit voorbeeld ga je het Phi-3.5-Mini model fijn afstemmen zodat het gespecialiseerd is in het beantwoorden van reisgerelateerde vragen. De code hieronder toont de eerste paar records van de dataset, die in JSON lines formaat zijn:

    ```bash
    head data/data_sample_travel.jsonl
    ```  
2. **Kwantiseer het model:** Voordat je het model traint, kwantiseer je het eerst met het volgende commando dat een techniek gebruikt genaamd Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kwantiseert de gewichten van een model door rekening te houden met de activaties die tijdens inferentie worden geproduceerd. Dit betekent dat het kwantisatieproces de daadwerkelijke data-verdeling in de activaties meeneemt, wat leidt tot een betere behoud van modelnauwkeurigheid vergeleken met traditionele gewichtskwantisatiemethoden.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Het duurt ongeveer **8 minuten** om de AWQ-kwantisatie te voltooien, wat de modelgrootte zal **verminderen van ~7,5GB naar ~2,5GB**.

    In deze lab laten we zien hoe je modellen van Hugging Face invoert (bijvoorbeeld: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` commando stemt het gekwantiseerde model fijn af. Het model *vooraf* kwantiseren in plaats van achteraf geeft een betere nauwkeurigheid, omdat het fijn afstemmen een deel van het verlies door kwantisatie herstelt.

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

    Het fijn afstemmen duurt ongeveer **6 minuten** (met 100 stappen).

3. **Optimaliseer:** Nu het model getraind is, optimaliseer je het model met Olive’s `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` argumenten – maar voor deze lab gebruiken we CPU.

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

    Dit duurt ongeveer **5 minuten**.

### Stap 5: Sneltest model inferentie

Om de inferentie van het model te testen, maak je een Python-bestand in je map genaamd **app.py** en kopieer je onderstaande code erin:

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

Voer de code uit met:

```bash
python app.py
```

### Stap 6: Upload model naar Azure AI

Het uploaden van het model naar een Azure AI model repository maakt het model deelbaar met andere leden van je ontwikkelteam en beheert ook versiebeheer van het model. Voer het volgende commando uit om het model te uploaden:

> [!NOTE]  
> Werk de `{}` placeholders bij met de naam van je resourcegroep en Azure AI Project naam, en voer dan het volgende commando uit:

```
az ml workspace show
```

Of ga naar +++ai.azure.com+++ en selecteer **management center** > **project** > **overview**

Vul de `{}` placeholders in met de naam van je resourcegroep en Azure AI Project naam.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Je kunt je geüploade model dan bekijken en deployen op https://ml.azure.com/model/list

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.