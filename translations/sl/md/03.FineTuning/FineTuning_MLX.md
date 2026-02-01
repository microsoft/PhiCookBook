# **Natančno prilagajanje Phi-3 z Apple MLX Framework**

Natančno prilagajanje v kombinaciji z Lora lahko izvedemo preko ukazne vrstice Apple MLX frameworka. (Če želite izvedeti več o delovanju MLX Frameworka, preberite [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Priprava podatkov**

Privzeto MLX Framework zahteva jsonl format za train, test in eval, ki se kombinira z Lora za izvedbo natančnega prilagajanja.


### ***Opomba:***

1. jsonl format podatkov ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. V našem primeru uporabljamo [TruthfulQA-jeve podatke](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), vendar je količina podatkov razmeroma majhna, zato rezultati natančnega prilagajanja niso nujno najboljši. Priporočamo, da uporabniki uporabijo boljše podatke glede na svoje scenarije.

3. Format podatkov je usklajen s Phi-3 predlogo

Prosimo, prenesite podatke s te [povezave](../../../../code/04.Finetuning/mlx), vključite vse .jsonl datoteke v ***data*** mapi


## **2. Natančno prilagajanje v terminalu**

Zaženite ta ukaz v terminalu


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Opomba:***

1. To je LoRA natančno prilagajanje, MLX framework ni objavil QLoRA

2. Lahko nastavite config.yaml za spremembo nekaterih argumentov, na primer


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

Zaženite ta ukaz v terminalu


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Zaženite natančno prilagajanje adapterja za testiranje**

Natančno prilagajanje adapterja lahko zaženete v terminalu, na primer tako


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

in za primerjavo zaženite izvirni model


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Lahko poskusite primerjati rezultate natančnega prilagajanja z izvirnim modelom


## **4. Združevanje adapterjev za ustvarjanje novih modelov**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Zagon kvantificiranih modelov natančnega prilagajanja z ollama**

Pred uporabo konfigurirajte okolje llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Opomba:*** 

1. Trenutno podprta kvantizacija za fp32, fp16 in INT 8

2. Združeni model nima tokenizer.model, prosimo, prenesite ga z https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

nastavite [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Zaženite ukaz v terminalu


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Čestitke! Obvladajte natančno prilagajanje z MLX Frameworkom

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.