<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-07T10:22:10+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "de"
}
-->
# **Feinabstimmung von Phi-3 mit dem Apple MLX Framework**

Wir können die Feinabstimmung in Kombination mit Lora über die Befehlszeile des Apple MLX Frameworks durchführen. (Wenn Sie mehr über die Funktionsweise des MLX Frameworks erfahren möchten, lesen Sie bitte [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Datenvorbereitung**

Standardmäßig erfordert das MLX Framework das jsonl-Format für train, test und eval und wird zusammen mit Lora verwendet, um Feinabstimmungsaufgaben abzuschließen.


### ***Note:***

1. jsonl-Datenformat ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Unser Beispiel verwendet die [TruthfulQA-Daten](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), aber die Datenmenge ist relativ gering, daher sind die Feinabstimmungsergebnisse nicht unbedingt optimal. Es wird empfohlen, dass Lernende bessere Daten basierend auf ihren eigenen Szenarien verwenden.

3. Das Datenformat ist an die Phi-3 Vorlage angepasst.

Bitte laden Sie die Daten von diesem [Link](../../../../code/04.Finetuning/mlx) herunter und stellen Sie sicher, dass alle .jsonl-Dateien im ***data***-Ordner enthalten sind.


## **2. Feinabstimmung im Terminal**

Bitte führen Sie diesen Befehl im Terminal aus


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Dies ist eine LoRA-Feinabstimmung, das MLX Framework hat QLoRA nicht veröffentlicht.

2. Sie können config.yaml anpassen, um einige Argumente zu ändern, zum Beispiel


```yaml


# The path to the local model directory or Hugging Face repo.
model: "microsoft/Phi-3-mini-4k-instruct"
# Whether or not to train (boolean)
train: true

# Directory with {train, valid, test}.jsonl files
data: "data"

# The PRNG seed
seed: 0

# Number of layers to fine-tune
lora_layers: 32

# Minibatch size.
batch_size: 1

# Iterations to train for.
iters: 1000

# Number of validation batches, -1 uses the entire validation set.
val_batches: 25

# Adam learning rate.
learning_rate: 1e-6

# Number of training steps between loss reporting.
steps_per_report: 10

# Number of training steps between validations.
steps_per_eval: 200

# Load path to resume training with the given adapter weights.
resume_adapter_file: null

# Save/load path for the trained adapter weights.
adapter_path: "adapters"

# Save the model every N iterations.
save_every: 1000

# Evaluate on the test set after training
test: false

# Number of test set batches, -1 uses the entire test set.
test_batches: 100

# Maximum sequence length.
max_seq_length: 2048

# Use gradient checkpointing to reduce memory use.
grad_checkpoint: true

# LoRA parameters can only be specified in a config file
lora_parameters:
  # The layer keys to apply LoRA to.
  # These will be applied for the last lora_layers
  keys: ["o_proj","qkv_proj"]
  rank: 64
  scale: 1
  dropout: 0.1


```

Bitte führen Sie diesen Befehl im Terminal aus


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Feinabstimmungsadapter zum Testen ausführen**

Sie können den Feinabstimmungsadapter im Terminal so ausführen:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

und das Originalmodell ausführen, um die Ergebnisse zu vergleichen


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Sie können versuchen, die Ergebnisse der Feinabstimmung mit dem Originalmodell zu vergleichen.


## **4. Adapter zusammenführen, um neue Modelle zu erzeugen**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Quantisierte Feinabstimmungsmodelle mit ollama ausführen**

Bitte konfigurieren Sie vor der Nutzung Ihre llama.cpp-Umgebung


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Unterstützt wird jetzt die Quantisierungskonvertierung von fp32, fp16 und INT 8

2. Dem zusammengeführten Modell fehlt tokenizer.model, bitte laden Sie es von https://huggingface.co/microsoft/Phi-3-mini-4k-instruct herunter

Richten Sie ein [Ollma Model](https://ollama.com/) ein


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Befehl im Terminal ausführen


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Herzlichen Glückwunsch! Sie beherrschen die Feinabstimmung mit dem MLX Framework

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.