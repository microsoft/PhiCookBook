<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:43:21+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "sv"
}
-->
# **Finjustera Phi-3 med Apple MLX Framework**

Vi kan genomföra finjustering kombinerat med Lora via Apple MLX Frameworks kommandorad. (Om du vill veta mer om hur MLX Framework fungerar, läs [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Datapreparation**

Som standard kräver MLX Framework jsonl-format för train, test och eval, och kombineras med Lora för att slutföra finjusteringsjobb.


### ***Note:***

1. jsonl-dataformat ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Vårt exempel använder [TruthfulQA:s data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), men mängden data är relativt liten, så finjusteringsresultaten är inte nödvändigtvis de bästa. Vi rekommenderar att användare använder bättre data baserat på sina egna scenarier för att slutföra.

3. Dataformatet är anpassat till Phi-3-mallen

Ladda ner data från denna [länk](../../../../code/04.Finetuning/mlx), inkludera alla .jsonl i ***data***-mappen


## **2. Finjustering i din terminal**

Kör detta kommando i terminalen


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Detta är LoRA-finjustering, MLX Framework har inte publicerat QLoRA

2. Du kan ändra config.yaml för att justera vissa argument, till exempel


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

Kör detta kommando i terminalen


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Kör finjusteringsadapter för test**

Du kan köra finjusteringsadaptern i terminalen, så här 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

och kör originalmodellen för att jämföra resultatet 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Du kan försöka jämföra resultaten mellan finjusteringen och originalmodellen


## **4. Slå ihop adaptrar för att generera nya modeller**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Köra kvantifierade finjusteringsmodeller med ollama**

Innan användning, konfigurera din llama.cpp-miljö


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Stöder nu kvantisering för fp32, fp16 och INT 8

2. Den sammanslagna modellen saknar tokenizer.model, ladda ner den från https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

sätt upp en [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

kör kommando i terminalen


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Grattis! Bemästra finjustering med MLX Framework

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.