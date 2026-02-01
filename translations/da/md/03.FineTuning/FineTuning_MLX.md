# **Finjustering af Phi-3 med Apple MLX Framework**

Vi kan udføre finjustering kombineret med Lora via Apple MLX frameworkets kommandolinje. (Hvis du vil vide mere om, hvordan MLX Framework fungerer, kan du læse [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Forberedelse af data**

Som standard kræver MLX Framework jsonl-format for train, test og eval, og kombineres med Lora for at fuldføre finjusteringsopgaver.


### ***Note:***

1. jsonl dataformat ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Vores eksempel bruger [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), men datamængden er relativt begrænset, så finjusteringsresultaterne er ikke nødvendigvis de bedste. Det anbefales, at brugere anvender bedre data baseret på deres egne scenarier.

3. Dataformatet er kombineret med Phi-3 skabelonen

Download venligst data fra dette [link](../../../../code/04.Finetuning/mlx), sørg for at inkludere alle .jsonl filer i ***data*** mappen


## **2. Finjustering i din terminal**

Kør venligst denne kommando i terminalen


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Dette er LoRA finjustering, MLX framework har ikke udgivet QLoRA

2. Du kan ændre nogle argumenter ved at redigere config.yaml, for eksempel


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

Kør venligst denne kommando i terminalen


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Kør finjusteringsadapter til test**

Du kan køre finjusteringsadapteren i terminalen, sådan her 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

og køre den oprindelige model for at sammenligne resultaterne


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Du kan prøve at sammenligne resultaterne af finjusteringen med den oprindelige model


## **4. Sammenflet adaptere for at generere nye modeller**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Kør kvantificerede finjusteringsmodeller med ollama**

Før brug, konfigurer venligst dit llama.cpp miljø


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Understøtter nu kvantisering konvertering af fp32, fp16 og INT 8

2. Den sammenflettede model mangler tokenizer.model, hent den venligst fra https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

sæt en [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

kør kommando i terminalen


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Tillykke! Du mestrer finjustering med MLX Framework

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.