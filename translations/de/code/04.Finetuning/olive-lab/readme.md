<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-03-27T03:49:38+00:00",
  "source_file": "code\\04.Finetuning\\olive-lab\\readme.md",
  "language_code": "de"
}
-->
# Lab. Optimieren von KI-Modellen für die gerätebasierte Inferenz

## Einführung

> [!IMPORTANT]
> Dieses Lab erfordert eine **Nvidia A10 oder A100 GPU** mit zugehörigen Treibern und installiertem CUDA-Toolkit (Version 12+).

> [!NOTE]
> Dieses Lab dauert **35 Minuten** und bietet eine praktische Einführung in die Kernkonzepte der Optimierung von Modellen für die gerätebasierte Inferenz mithilfe von OLIVE.

## Lernziele

Am Ende dieses Labs können Sie OLIVE verwenden, um:

- Ein KI-Modell mit der AWQ-Quantisierungsmethode zu quantisieren.
- Ein KI-Modell für eine spezifische Aufgabe zu feintunen.
- LoRA-Adapter (feingetuntes Modell) für effiziente gerätebasierte Inferenz auf der ONNX Runtime zu erstellen.

### Was ist Olive?

Olive (*O*NNX *live*) ist ein Toolkit zur Modelloptimierung mit zugehöriger CLI, das Ihnen ermöglicht, Modelle für die ONNX Runtime +++https://onnxruntime.ai+++ mit hoher Qualität und Performance bereitzustellen.

![Olive Flow](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.de.png)

Das Input für Olive ist typischerweise ein PyTorch- oder Hugging Face-Modell, und das Output ist ein optimiertes ONNX-Modell, das auf einem Gerät (Bereitstellungsziel) läuft, auf dem die ONNX Runtime ausgeführt wird. Olive optimiert das Modell für den KI-Beschleuniger des Bereitstellungsziels (NPU, GPU, CPU), der von einem Hardwareanbieter wie Qualcomm, AMD, Nvidia oder Intel bereitgestellt wird.

Olive führt einen *Workflow* aus, der eine geordnete Abfolge einzelner Modelloptimierungsaufgaben namens *Passes* ist – Beispiele für Passes sind: Modellkompression, Graph-Capture, Quantisierung, Graph-Optimierung. Jeder Pass hat eine Reihe von Parametern, die abgestimmt werden können, um die besten Metriken, wie Genauigkeit und Latenz, zu erreichen, die vom jeweiligen Evaluator bewertet werden. Olive verwendet eine Suchstrategie, die einen Suchalgorithmus einsetzt, um jeden Pass einzeln oder eine Gruppe von Passes zusammen automatisch zu optimieren.

#### Vorteile von Olive

- **Reduziert Frustration und Zeit** durch manuelles Experimentieren mit verschiedenen Techniken zur Graph-Optimierung, Kompression und Quantisierung. Definieren Sie Ihre Qualitäts- und Performance-Anforderungen, und Olive findet automatisch das beste Modell für Sie.
- **Über 40 eingebaute Modelloptimierungskomponenten**, die moderne Techniken in Quantisierung, Kompression, Graph-Optimierung und Feintuning abdecken.
- **Einfach zu bedienende CLI** für gängige Modelloptimierungsaufgaben, z. B. olive quantize, olive auto-opt, olive finetune.
- Eingebaute Modellverpackung und Bereitstellung.
- Unterstützung für die Erstellung von Modellen für **Multi LoRA-Serving**.
- Workflows mit YAML/JSON erstellen, um Modelloptimierungs- und Bereitstellungsaufgaben zu orchestrieren.
- Integration von **Hugging Face** und **Azure AI**.
- Eingebauter **Caching-Mechanismus**, um **Kosten zu sparen**.

## Lab-Anweisungen

> [!NOTE]
> Stellen Sie sicher, dass Sie Ihr Azure AI Hub und Projekt bereitgestellt und Ihre A100-Compute-Instanz gemäß Lab 1 eingerichtet haben.

### Schritt 0: Verbinden Sie sich mit Ihrer Azure AI Compute-Instanz

Sie verbinden sich mit der Azure AI Compute-Instanz über die Remote-Funktion in **VS Code.**

1. Öffnen Sie Ihre **VS Code**-Desktopanwendung:
1. Öffnen Sie die **Befehlspalette** mit **Shift+Ctrl+P**.
1. Suchen Sie in der Befehlspalette nach **AzureML - remote: Connect to compute instance in New Window**.
1. Folgen Sie den Anweisungen auf dem Bildschirm, um die Compute-Instanz zu verbinden. Dies umfasst die Auswahl Ihres Azure-Abonnements, Ressourcengruppes, Projekts und Compute-Namens, die Sie in Lab 1 eingerichtet haben.
1. Sobald Sie mit Ihrer Azure ML Compute-Instanz verbunden sind, wird dies **unten links in Visual Code** angezeigt `><Azure ML: Compute Name`.

### Schritt 1: Klonen Sie dieses Repository

In VS Code können Sie ein neues Terminal mit **Ctrl+J** öffnen und dieses Repository klonen:

Im Terminal sollten Sie die Eingabeaufforderung sehen

```
azureuser@computername:~/cloudfiles/code$ 
```
Klonen Sie die Lösung

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Schritt 2: Ordner in VS Code öffnen

Um VS Code im relevanten Ordner zu öffnen, führen Sie den folgenden Befehl im Terminal aus. Dadurch wird ein neues Fenster geöffnet:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativ können Sie den Ordner öffnen, indem Sie **Datei** > **Ordner öffnen** auswählen.

### Schritt 3: Abhängigkeiten

Öffnen Sie ein Terminalfenster in VS Code auf Ihrer Azure AI Compute-Instanz (Tipp: **Ctrl+J**) und führen Sie die folgenden Befehle aus, um die Abhängigkeiten zu installieren:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Die Installation aller Abhängigkeiten dauert ~5 Minuten.

In diesem Lab werden Sie Modelle in den Azure AI Model-Katalog herunterladen und hochladen. Damit Sie auf den Modellkatalog zugreifen können, müssen Sie sich bei Azure anmelden:

```bash
az login
```

> [!NOTE]
> Während der Anmeldung werden Sie aufgefordert, Ihr Abonnement auszuwählen. Stellen Sie sicher, dass Sie das für dieses Lab bereitgestellte Abonnement verwenden.

### Schritt 4: Olive-Befehle ausführen

Öffnen Sie ein Terminalfenster in VS Code auf Ihrer Azure AI Compute-Instanz (Tipp: **Ctrl+J**) und stellen Sie sicher, dass die `olive-ai` Conda-Umgebung aktiviert ist:

```bash
conda activate olive-ai
```

Führen Sie anschließend die folgenden Olive-Befehle in der Befehlszeile aus.

1. **Daten inspizieren:** In diesem Beispiel werden Sie das Modell Phi-3.5-Mini feintunen, damit es sich auf das Beantworten von reisebezogenen Fragen spezialisiert. Der folgende Code zeigt die ersten Datensätze des Datasets an, die im JSON-Lines-Format vorliegen:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Modell quantisieren:** Bevor Sie das Modell trainieren, quantisieren Sie es mit dem folgenden Befehl, der eine Technik namens Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ verwendet. AWQ quantisiert die Gewichte eines Modells, indem die während der Inferenz erzeugten Aktivierungen berücksichtigt werden. Dies bedeutet, dass der Quantisierungsprozess die tatsächliche Datenverteilung in den Aktivierungen berücksichtigt, was zu einer besseren Erhaltung der Modellgenauigkeit im Vergleich zu herkömmlichen Methoden der Gewichtquantisierung führt.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Die AWQ-Quantisierung dauert **~8 Minuten** und reduziert die Modellgröße von **~7,5 GB auf ~2,5 GB**.
   
   In diesem Lab zeigen wir Ihnen, wie Sie Modelle von Hugging Face (z. B. `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune`) eingeben können. Das Quantisieren des Modells *vor* dem Feintuning statt danach führt zu besserer Genauigkeit, da der Feintuning-Prozess einige der Verluste aus der Quantisierung wiederherstellt.
    
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
    
    Das Feintuning dauert **~6 Minuten** (mit 100 Schritten).

1. **Optimieren:** Nachdem das Modell trainiert wurde, optimieren Sie das Modell mit Olives `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider`-Argumenten – für dieses Lab verwenden wir jedoch die CPU.

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
    
    Die Optimierung dauert **~5 Minuten**.

### Schritt 5: Modell-Inferenz Schnelltest

Um das Modell zu testen, erstellen Sie eine Python-Datei in Ihrem Ordner namens **app.py** und kopieren Sie den folgenden Code:

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

Führen Sie den Code aus mit:

```bash
python app.py
```

### Schritt 6: Modell in Azure AI hochladen

Das Hochladen des Modells in ein Azure AI-Modell-Repository macht das Modell für andere Mitglieder Ihres Entwicklungsteams teilbar und übernimmt auch die Versionskontrolle des Modells. Um das Modell hochzuladen, führen Sie den folgenden Befehl aus:

> [!NOTE]
> Aktualisieren Sie die `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group ``-Platzhalter mit dem Namen Ihrer Ressourcengruppe und des Azure AI-Projekts, und führen Sie den folgenden Befehl aus:

```
az ml workspace show
```

Oder gehen Sie zu +++ai.azure.com+++ und wählen Sie **Management Center** > **Projekt** > **Übersicht**.

Aktualisieren Sie die `{}`-Platzhalter mit dem Namen Ihrer Ressourcengruppe und Ihres Azure AI-Projekts.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Anschließend können Sie Ihr hochgeladenes Modell sehen und Ihr Modell unter https://ml.azure.com/model/list bereitstellen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.