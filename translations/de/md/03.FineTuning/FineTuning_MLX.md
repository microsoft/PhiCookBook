<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-03-27T14:55:42+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_MLX.md",
  "language_code": "de"
}
-->
# **Feinabstimmung von Phi-3 mit dem Apple MLX Framework**

Wir können die Feinabstimmung in Kombination mit Lora über die Befehlszeile des Apple MLX Frameworks durchführen. (Wenn Sie mehr über den Betrieb des MLX Frameworks erfahren möchten, lesen Sie bitte [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)).

## **1. Datenvorbereitung**

Standardmäßig erfordert das MLX Framework das jsonl-Format für Train-, Test- und Eval-Daten und wird in Kombination mit Lora verwendet, um Feinabstimmungsaufgaben abzuschließen.

### ***Hinweis:***

1. jsonl-Datenformat:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Unser Beispiel verwendet die [Daten von TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), jedoch ist die Datenmenge relativ gering, sodass die Ergebnisse der Feinabstimmung nicht unbedingt optimal sind. Es wird empfohlen, dass Lernende bessere Daten basierend auf ihren eigenen Szenarien verwenden, um die Feinabstimmung durchzuführen.

3. Das Datenformat wird mit der Phi-3-Vorlage kombiniert.

Bitte laden Sie die Daten von diesem [Link](../../../../code/04.Finetuning/mlx) herunter und stellen Sie sicher, dass alle .jsonl-Dateien im ***data***-Ordner enthalten sind.

## **2. Feinabstimmung im Terminal**

Führen Sie diesen Befehl im Terminal aus:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Hinweis:***

1. Dies ist eine LoRA-Feinabstimmung. Das MLX Framework hat QLoRA nicht veröffentlicht.

2. Sie können die Datei config.yaml bearbeiten, um einige Parameter zu ändern, wie z. B.:

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

Führen Sie diesen Befehl im Terminal aus:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Feinabstimmungs-Adapter testen**

Sie können den Feinabstimmungs-Adapter im Terminal ausführen, wie folgt:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

und das Originalmodell ausführen, um die Ergebnisse zu vergleichen:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Sie können versuchen, die Ergebnisse der Feinabstimmung mit denen des Originalmodells zu vergleichen.

## **4. Adapter zusammenführen, um neue Modelle zu generieren**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Quantifizierte Feinabstimmungsmodelle mit Ollama ausführen**

Konfigurieren Sie vor der Nutzung Ihre llama.cpp-Umgebung:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Hinweis:***

1. Unterstützt jetzt die Quantisierungsumwandlung von fp32, fp16 und INT8.

2. Das zusammengeführte Modell enthält keinen tokenizer.model. Bitte laden Sie diesen von https://huggingface.co/microsoft/Phi-3-mini-4k-instruct herunter.

Richten Sie ein [Ollama-Modell](https://ollama.com/) ein:

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Führen Sie den Befehl im Terminal aus:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Herzlichen Glückwunsch! Sie haben die Feinabstimmung mit dem MLX Framework gemeistert.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.