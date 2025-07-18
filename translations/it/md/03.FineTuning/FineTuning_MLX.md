<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T07:59:40+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "it"
}
-->
# **Fine-tuning di Phi-3 con Apple MLX Framework**

Possiamo completare il fine-tuning combinato con Lora tramite la riga di comando del framework Apple MLX. (Se vuoi saperne di più sul funzionamento del MLX Framework, leggi [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Preparazione dei dati**

Di default, il MLX Framework richiede il formato jsonl per train, test ed eval, e si combina con Lora per completare i lavori di fine-tuning.


### ***Nota:***

1. Formato dati jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Nel nostro esempio utilizziamo i dati di [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), ma la quantità di dati è relativamente limitata, quindi i risultati del fine-tuning potrebbero non essere ottimali. Si consiglia agli utenti di utilizzare dati migliori basati sui propri scenari per completare il processo.

3. Il formato dei dati è combinato con il template di Phi-3

Scarica i dati da questo [link](../../../../code/04.Finetuning/mlx), assicurati di includere tutti i file .jsonl nella cartella ***data***


## **2. Fine-tuning nel terminale**

Esegui questo comando nel terminale


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Nota:***

1. Questo è un fine-tuning LoRA, il framework MLX non ha pubblicato QLoRA

2. Puoi modificare config.yaml per cambiare alcuni argomenti, ad esempio


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

Esegui questo comando nel terminale


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Esegui il fine-tuning adapter per il test**

Puoi eseguire il fine-tuning adapter nel terminale, così 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

e lanciare il modello originale per confrontare i risultati 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Puoi provare a confrontare i risultati del fine-tuning con quelli del modello originale


## **4. Unire gli adapter per generare nuovi modelli**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Esecuzione di modelli di fine-tuning quantizzati con ollama**

Prima dell’uso, configura il tuo ambiente llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Nota:*** 

1. Ora supporta la conversione di quantizzazione per fp32, fp16 e INT 8

2. Il modello unito manca di tokenizer.model, scaricalo da https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

imposta un [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Esegui il comando nel terminale


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Congratulazioni! Hai padroneggiato il fine-tuning con il MLX Framework

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.