<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T08:03:34+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "hr"
}
-->
# **Fino podešavanje Phi-3 s Apple MLX Frameworkom**

Fino podešavanje u kombinaciji s Lora možemo izvršiti putem naredbenog retka Apple MLX Frameworka. (Ako želite saznati više o radu MLX Frameworka, molimo pročitajte [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Priprema podataka**

Po defaultu, MLX Framework zahtijeva jsonl format za train, test i eval, a u kombinaciji s Lora dovršava zadatke fino podešavanja.


### ***Note:***

1. jsonl format podataka ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. U našem primjeru koristimo [TruthfulQA podatke](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), no količina podataka je relativno nedovoljna, stoga rezultati fino podešavanja nisu nužno najbolji. Preporučuje se da korisnici koriste kvalitetnije podatke prilagođene vlastitim scenarijima.

3. Format podataka je usklađen s Phi-3 predloškom

Molimo preuzmite podatke s ovog [linka](../../../../code/04.Finetuning/mlx), uključite sve .jsonl datoteke u ***data*** mapu


## **2. Fino podešavanje u vašem terminalu**

Pokrenite ovu naredbu u terminalu


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Ovo je LoRA fino podešavanje, MLX framework nije objavio QLoRA

2. Možete podesiti config.yaml za promjenu nekih argumenata, kao što su


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

Pokrenite ovu naredbu u terminalu


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Pokretanje fino podešenog adaptera za testiranje**

Fino podešeni adapter možete pokrenuti u terminalu, ovako 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

i pokrenuti originalni model za usporedbu rezultata 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Možete pokušati usporediti rezultate fino podešavanja s originalnim modelom


## **4. Spajanje adaptera za generiranje novih modela**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Pokretanje kvantiziranih fino podešenih modela pomoću ollama**

Prije korištenja, konfigurirajte svoj llama.cpp okoliš


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Sada je podržana kvantizacija za fp32, fp16 i INT 8

2. Spojeni model nema tokenizer.model, molimo preuzmite ga s https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

postavite [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

pokrenite naredbu u terminalu


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Čestitamo! Savladali ste fino podešavanje s MLX Frameworkom

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.