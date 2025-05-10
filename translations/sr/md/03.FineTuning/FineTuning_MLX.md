<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:45:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "sr"
}
-->
# **Fino podešavanje Phi-3 sa Apple MLX Framework-om**

Fino podešavanje u kombinaciji sa Lora možemo završiti putem komandne linije Apple MLX framework-a. (Ako želite da saznate više o radu MLX Framework-a, molimo pročitajte [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Priprema podataka**

Po defaultu, MLX Framework zahteva jsonl format za train, test i eval, i kombinuje se sa Lora za završetak poslova fino podešavanja.


### ***Napomena:***

1. jsonl format podataka ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Naš primer koristi [TruthfulQA podatke](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), ali količina podataka je relativno nedovoljna, pa rezultati fino podešavanja nisu nužno najbolji. Preporučuje se da korisnici koriste bolje podatke prema sopstvenim scenarijima.

3. Format podataka je kombinovan sa Phi-3 šablonom

Molimo preuzmite podatke sa ovog [linka](../../../../code/04.Finetuning/mlx), uključite sve .jsonl fajlove u ***data*** folderu


## **2. Fino podešavanje u vašem terminalu**

Pokrenite ovu komandu u terminalu


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Napomena:***

1. Ovo je LoRA fino podešavanje, MLX framework nije objavio QLoRA

2. Možete podesiti config.yaml da promenite neke argumente, kao što su


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

Pokrenite ovu komandu u terminalu


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Pokretanje fino podešenog adaptera za testiranje**

Možete pokrenuti fino podešeni adapter u terminalu, ovako


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

i pokrenuti originalni model za poređenje rezultata


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Možete pokušati da uporedite rezultate fino podešavanja sa originalnim modelom


## **4. Spajanje adaptera za generisanje novih modela**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Pokretanje kvantizovanih fino podešenih modela koristeći ollama**

Pre upotrebe, molimo konfigurišite vaš llama.cpp okruženje


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Napomena:*** 

1. Sada je podržana kvantizacija konverzije fp32, fp16 i INT 8

2. Spojeni model nema tokenizer.model, molimo preuzmite ga sa https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

podesite [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

pokrenite komandu u terminalu


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Čestitamo! Savladali ste fino podešavanje sa MLX Framework-om

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала употребом овог превода.