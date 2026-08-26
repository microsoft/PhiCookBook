# **Phi-3 tobulinimas naudojant Apple MLX Framework**

Galime užbaigti tobulinimą kartu su Lora naudodami Apple MLX framework komandinėje eilutėje. (Jei norite sužinoti daugiau apie MLX Framework veikimą, perskaitykite [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Duomenų paruošimas**

Pagal numatytuosius nustatymus, MLX Framework reikalauja treniruočių, testavimo ir įvertinimo duomenų jsonl formatu ir yra derinamas su Lora, kad užbaigtų tobulinimo užduotis.


### ***Pastaba:***

1. jsonl duomenų formatas:


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Mūsų pavyzdyje naudojami [TruthfulQA duomenys](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), tačiau duomenų kiekis yra pakankamai mažas, todėl tobulinimo rezultatai nebūtinai bus geriausi. Rekomenduojama besimokantiesiems naudotis geresniais duomenimis, atsižvelgiant į savo scenarijus.

3. Duomenų formatas suderintas su Phi-3 šablonu

Prašome atsisiųsti duomenis iš šios [nuorodos](../../../../code/04.Finetuning/mlx), įtraukite visus .jsonl failus į ***data*** katalogą.


## **2. Tobulinimas jūsų terminale**

Prašome paleisti šią komandą terminale


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Pastaba:***

1. Tai yra LoRA tobulinimas, MLX framework nepalaiko QLoRA

2. Galite nustatyti config.yaml failą, kad pakeistumėte kai kuriuos argumentus, pavyzdžiui


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

Prašome paleisti šią komandą terminale


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Tobulinimo adapterio paleidimas testavimui**

Galite paleisti tobulinimo adapterį terminale, kaip šitai


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ir paleisti pradinį modelį rezultatų palyginimui


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Galite pabandyti palyginti tobulinimo rezultatus su pradiniu modeliu


## **4. Adapterių sujungimas naujiems modeliams sukurti**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Kvantinių tobulinimo modelių paleidimas naudojant ollama**

Prieš naudodami, sukonfigūruokite savo llama.cpp aplinką


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Pastaba:*** 

1. Dabar palaikoma konvertavimas į kvantinį formatą fp32, fp16 ir INT 8

2. Sujungtame modelyje trūksta tokenizer.model, prašome jį atsisiųsti iš https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

nustatykite [Ollma modelį](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

paleiskite komandą terminale


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Sveikiname! Valdote tobulinimą su MLX Framework

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->