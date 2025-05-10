<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T04:23:40+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "it"
}
-->
# Lab. Ottimizza modelli AI per l'inferenza on-device

## Introduzione

> [!IMPORTANT]
> Questo laboratorio richiede una **GPU Nvidia A10 o A100** con i driver associati e il toolkit CUDA (versione 12+) installati.

> [!NOTE]
> Questo è un laboratorio di **35 minuti** che ti fornirà un’introduzione pratica ai concetti base dell’ottimizzazione dei modelli per l’inferenza on-device usando OLIVE.

## Obiettivi di apprendimento

Al termine di questo laboratorio, sarai in grado di usare OLIVE per:

- Quantizzare un modello AI utilizzando il metodo di quantizzazione AWQ.
- Effettuare il fine-tuning di un modello AI per un compito specifico.
- Generare adattatori LoRA (modello fine-tuned) per un’inferenza efficiente on-device su ONNX Runtime.

### Cos’è Olive

Olive (*O*NNX *live*) è un toolkit di ottimizzazione modelli con CLI integrata che ti permette di distribuire modelli per ONNX runtime +++https://onnxruntime.ai+++ con qualità e prestazioni elevate.

![Olive Flow](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.it.png)

L’input di Olive è tipicamente un modello PyTorch o Hugging Face, mentre l’output è un modello ONNX ottimizzato eseguito su un dispositivo (target di deployment) che utilizza ONNX runtime. Olive ottimizza il modello per l’acceleratore AI del target di deployment (NPU, GPU, CPU) fornito da un vendor hardware come Qualcomm, AMD, Nvidia o Intel.

Olive esegue un *workflow*, ovvero una sequenza ordinata di singoli compiti di ottimizzazione del modello chiamati *passaggi* (passes) - esempi di passaggi includono: compressione modello, cattura del grafo, quantizzazione, ottimizzazione del grafo. Ogni passaggio ha un set di parametri che possono essere regolati per ottenere le migliori metriche, come accuratezza e latenza, valutate dal rispettivo evaluator. Olive utilizza una strategia di ricerca con un algoritmo che auto-regola ogni passaggio uno per uno o un insieme di passaggi insieme.

#### Vantaggi di Olive

- **Riduce frustrazione e tempo** dovuti a sperimentazioni manuali di prova ed errore con diverse tecniche di ottimizzazione del grafo, compressione e quantizzazione. Definisci i tuoi vincoli di qualità e prestazioni e lascia che Olive trovi automaticamente il modello migliore per te.
- **Oltre 40 componenti di ottimizzazione modello integrati** che coprono tecniche all’avanguardia in quantizzazione, compressione, ottimizzazione del grafo e fine-tuning.
- **CLI facile da usare** per attività comuni di ottimizzazione modello. Ad esempio, olive quantize, olive auto-opt, olive finetune.
- Packaging e deployment del modello integrati.
- Supporto per la generazione di modelli per **Multi LoRA serving**.
- Costruzione di workflow usando YAML/JSON per orchestrare attività di ottimizzazione e deployment.
- Integrazione con **Hugging Face** e **Azure AI**.
- Meccanismo di **caching** integrato per **ridurre i costi**.

## Istruzioni del laboratorio

> [!NOTE]
> Assicurati di aver predisposto il tuo Azure AI Hub e Project e configurato il tuo calcolo A100 come descritto nel Laboratorio 1.

### Passo 0: Connettersi al tuo Azure AI Compute

Ti connetterai al compute Azure AI usando la funzione remota in **VS Code**.

1. Apri l’app desktop **VS Code**:
1. Apri la **command palette** con **Shift+Ctrl+P**
1. Nella command palette cerca **AzureML - remote: Connect to compute instance in New Window**.
1. Segui le istruzioni a schermo per connetterti al Compute. Dovrai selezionare la tua Azure Subscription, Resource Group, Project e il nome del Compute configurato nel Laboratorio 1.
1. Una volta connesso al nodo Azure ML Compute, questo sarà mostrato in basso a sinistra di Visual Studio Code `><Azure ML: Compute Name`

### Passo 1: Clona questo repo

In VS Code, apri un terminale con **Ctrl+J** e clona questo repository:

Nel terminale vedrai il prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Clona la soluzione

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Passo 2: Apri la cartella in VS Code

Per aprire VS Code nella cartella corretta esegui il comando seguente nel terminale, che aprirà una nuova finestra:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

In alternativa, puoi aprire la cartella selezionando **File** > **Open Folder**.

### Passo 3: Dipendenze

Apri un terminale in VS Code nella tua Azure AI Compute Instance (consiglio: **Ctrl+J**) ed esegui i seguenti comandi per installare le dipendenze:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> L’installazione di tutte le dipendenze richiederà circa 5 minuti.

In questo laboratorio scaricherai e caricherai modelli nel catalogo modelli Azure AI. Per accedere al catalogo modelli, devi effettuare il login ad Azure con:

```bash
az login
```

> [!NOTE]
> Al momento del login ti verrà chiesto di selezionare la subscription. Assicurati di impostare la subscription fornita per questo laboratorio.

### Passo 4: Esegui i comandi Olive

Apri un terminale in VS Code nella tua Azure AI Compute Instance (consiglio: **Ctrl+J**) e assicurati che l’ambiente conda `olive-ai` sia attivato:

```bash
conda activate olive-ai
```

Successivamente, esegui i seguenti comandi Olive da linea di comando.

1. **Ispeziona i dati:** In questo esempio, effettuerai il fine-tuning del modello Phi-3.5-Mini per specializzarlo nel rispondere a domande legate ai viaggi. Il codice qui sotto mostra i primi record del dataset, che sono in formato JSON lines:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Quantizza il modello:** Prima di addestrare il modello, quantizzalo con il comando seguente che utilizza una tecnica chiamata Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ quantizza i pesi di un modello tenendo conto delle attivazioni generate durante l’inferenza. Questo significa che il processo di quantizzazione considera la distribuzione reale dei dati nelle attivazioni, garantendo una migliore conservazione dell’accuratezza rispetto ai metodi tradizionali di quantizzazione dei pesi.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    L’operazione di quantizzazione AWQ richiede circa **8 minuti** e riduce la dimensione del modello da circa 7.5GB a circa 2.5GB.
   
   In questo laboratorio ti mostriamo come importare modelli da Hugging Face (per esempio: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` esegue il fine-tuning del modello quantizzato. Quantizzare il modello *prima* del fine-tuning invece che dopo garantisce una migliore accuratezza, poiché il fine-tuning recupera parte della perdita dovuta alla quantizzazione.
    
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
    
    Il fine-tuning richiede circa **6 minuti** (con 100 step).

1. **Ottimizza:** Con il modello addestrato, ora ottimizza il modello usando il comando `auto-opt` di Olive con gli argomenti `--device` e `--provider` - ma per questo laboratorio useremo la CPU.

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
    
    L’ottimizzazione richiede circa **5 minuti**.

### Passo 5: Test rapido di inferenza del modello

Per testare l’inferenza del modello, crea un file Python nella tua cartella chiamato **app.py** e incolla il seguente codice:

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

Esegui il codice con:

```bash
python app.py
```

### Passo 6: Carica il modello su Azure AI

Caricare il modello nel repository modelli di Azure AI rende il modello condivisibile con altri membri del team di sviluppo e gestisce anche il controllo delle versioni. Per caricare il modello esegui il comando seguente:

> [!NOTE]
> Aggiorna i placeholder `{}` per `resourceGroup` e nome del progetto Azure AI, poi esegui il comando:

```
az ml workspace show
```

Oppure vai su +++ai.azure.com+++ e seleziona **management center** > **project** > **overview**

Aggiorna i placeholder `{}` con il nome del tuo resource group e del progetto Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Potrai quindi vedere il modello caricato e distribuirlo su https://ml.azure.com/model/list

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.