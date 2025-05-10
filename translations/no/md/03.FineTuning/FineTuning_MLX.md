<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:43:35+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "no"
}
-->
# **Finjustering av Phi-3 med Apple MLX-rammeverket**

Vi kan fullføre finjustering kombinert med Lora gjennom Apple MLX-rammeverkets kommandolinje. (Hvis du vil vite mer om hvordan MLX-rammeverket fungerer, vennligst les [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Datapreparasjon**

Som standard krever MLX-rammeverket jsonl-format for train, test og eval, og kombineres med Lora for å fullføre finjusteringsoppgaver.


### ***Note:***

1. jsonl dataformat ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Vårt eksempel bruker [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), men datamengden er relativt begrenset, så finjusteringsresultatene er ikke nødvendigvis optimale. Det anbefales at brukere benytter bedre data tilpasset egne scenarier for å fullføre prosessen.

3. Dataformatet er kombinert med Phi-3-malen

Vennligst last ned data fra denne [lenken](../../../../code/04.Finetuning/mlx), og inkluder alle .jsonl i ***data***-mappen


## **2. Finjustering i terminalen**

Kjør denne kommandoen i terminalen


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Dette er LoRA-finjustering, MLX-rammeverket har ikke publisert QLoRA

2. Du kan endre noen argumenter i config.yaml, for eksempel


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

Kjør denne kommandoen i terminalen


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Kjør finjusteringsadapter for testing**

Du kan kjøre finjusteringsadapteren i terminalen, slik:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

og kjøre originalmodellen for å sammenligne resultatet


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Du kan prøve å sammenligne resultatene fra finjusteringen med originalmodellen


## **4. Slå sammen adaptere for å generere nye modeller**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Kjøre kvantifiserte finjusteringsmodeller med ollama**

Før bruk, vennligst konfigurer ditt llama.cpp-miljø


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Støtter nå kvantisering og konvertering for fp32, fp16 og INT 8

2. Den sammenslåtte modellen mangler tokenizer.model, vennligst last den ned fra https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

sett opp en [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

kjør kommando i terminalen


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Gratulerer! Du har mestret finjustering med MLX-rammeverket

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.