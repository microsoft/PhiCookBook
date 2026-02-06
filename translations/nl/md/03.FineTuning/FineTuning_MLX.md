# **Fine-tunen van Phi-3 met Apple MLX Framework**

We kunnen fine-tunen in combinatie met Lora voltooien via de Apple MLX framework commandoregel. (Als je meer wilt weten over de werking van het MLX Framework, lees dan [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Voorbereiding van data**

Standaard vereist het MLX Framework het jsonl-formaat voor train, test en eval, en wordt gecombineerd met Lora om fine-tuning taken uit te voeren.


### ***Note:***

1. jsonl dataformaat ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Ons voorbeeld gebruikt [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), maar de hoeveelheid data is relatief beperkt, dus de fine-tuning resultaten zijn niet per se optimaal. Het wordt aanbevolen dat gebruikers betere data gebruiken op basis van hun eigen scenario’s om fine-tuning te voltooien.

3. Het dataformaat is gecombineerd met de Phi-3 template

Download de data via deze [link](../../../../code/04.Finetuning/mlx), zorg dat je alle .jsonl bestanden in de ***data*** map hebt


## **2. Fine-tunen in je terminal**

Voer dit commando uit in de terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Dit is LoRA fine-tuning, het MLX framework heeft QLoRA nog niet uitgebracht

2. Je kunt config.yaml aanpassen om enkele argumenten te wijzigen, zoals


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

Voer dit commando uit in de terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Fine-tuning adapter testen**

Je kunt de fine-tuning adapter in de terminal draaien, bijvoorbeeld zo 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

en het originele model draaien om de resultaten te vergelijken 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Je kunt proberen de resultaten van fine-tuning te vergelijken met het originele model


## **4. Adapters samenvoegen om nieuwe modellen te genereren**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Gequantificeerde fine-tuning modellen draaien met ollama**

Configureer eerst je llama.cpp omgeving


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Ondersteunt nu quantisatieconversie van fp32, fp16 en INT 8

2. Het samengevoegde model mist tokenizer.model, download deze via https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

stel een [Ollma Model](https://ollama.com/) in


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

voer het commando uit in de terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Gefeliciteerd! Je beheerst fine-tuning met het MLX Framework

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.