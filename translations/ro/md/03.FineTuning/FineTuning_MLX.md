<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:45:10+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "ro"
}
-->
# **Ajustarea fină a Phi-3 cu Apple MLX Framework**

Putem finaliza ajustarea fină combinată cu Lora prin linia de comandă a Apple MLX Framework. (Dacă vrei să afli mai multe despre funcționarea MLX Framework, te rugăm să citești [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. Pregătirea datelor**

Implicit, MLX Framework necesită formatul jsonl pentru train, test și eval, și se combină cu Lora pentru a finaliza sarcinile de ajustare fină.

### ***Note:***

1. Formatul de date jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Exemplul nostru folosește [datele TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), dar cantitatea de date este relativ insuficientă, deci rezultatele ajustării fine nu sunt neapărat cele mai bune. Se recomandă ca utilizatorii să folosească date mai bune, adaptate propriilor scenarii, pentru a finaliza procesul.

3. Formatul datelor este combinat cu șablonul Phi-3

Te rugăm să descarci datele de la acest [link](../../../../code/04.Finetuning/mlx), asigură-te că incluzi toate fișierele .jsonl din folderul ***data***


## **2. Ajustarea fină în terminalul tău**

Te rugăm să rulezi această comandă în terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Aceasta este ajustare fină LoRA, MLX framework nu a publicat QLoRA

2. Poți modifica config.yaml pentru a schimba unele argumente, cum ar fi


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

Te rugăm să rulezi această comandă în terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Rulează adaptorul de ajustare fină pentru testare**

Poți rula adaptorul de ajustare fină în terminal, astfel 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

și poți rula modelul original pentru a compara rezultatele


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Poți încerca să compari rezultatele ajustării fine cu modelul original


## **4. Combinarea adaptoarelor pentru a genera modele noi**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Rularea modelelor ajustate și cuantificate folosind ollama**

Înainte de utilizare, te rugăm să configurezi mediul llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Acum se suportă conversia de cuantificare pentru fp32, fp16 și INT 8

2. Modelul combinat nu include tokenizer.model, te rugăm să îl descarci de la https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

setează un [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

rulează comanda în terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Felicitări! Ai stăpânit ajustarea fină cu MLX Framework

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.