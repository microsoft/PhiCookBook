<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:45:02+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "sk"
}
-->
# **Doladenie Phi-3 pomocou Apple MLX Frameworku**

Doladenie v kombinácii s Lora môžeme dokončiť cez príkazový riadok Apple MLX frameworku. (Ak chcete vedieť viac o fungovaní MLX Frameworku, prečítajte si [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Príprava dát**

Štandardne MLX Framework vyžaduje jsonl formát pre train, test a eval a v kombinácii s Lora dokončuje doladenie.


### ***Note:***

1. jsonl formát dát ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Náš príklad používa [TruthfulQA dáta](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), ale množstvo dát je relatívne nedostatočné, preto výsledky doladenia nemusia byť najlepšie. Odporúča sa, aby si študenti na základe svojich scenárov použili lepšie dáta.

3. Formát dát je kombinovaný s Phi-3 šablónou

Prosím stiahnite dáta z tohto [linku](../../../../code/04.Finetuning/mlx), zahŕňajúce všetky .jsonl v ***data*** priečinku


## **2. Doladenie v termináli**

Spustite tento príkaz v termináli


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Toto je LoRA doladenie, MLX framework nezverejnil QLoRA

2. Môžete upraviť config.yaml na zmenu niektorých argumentov, napríklad


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

Spustite tento príkaz v termináli


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Spustenie doladeného adaptéra na testovanie**

Doladený adaptér môžete spustiť v termináli takto


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

a spustiť pôvodný model na porovnanie výsledkov


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Môžete skúsiť porovnať výsledky doladenia s pôvodným modelom


## **4. Zlúčenie adaptérov na vytvorenie nových modelov**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Spustenie kvantovaných doladených modelov pomocou ollama**

Pred použitím si nakonfigurujte svoje prostredie llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:***

1. Teraz podporuje kvantizáciu fp32, fp16 a INT 8

2. Zlúčený model nemá tokenizer.model, stiahnite si ho z https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

nastavte [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

spustite príkaz v termináli


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Gratulujeme! Ovládli ste doladenie s MLX Frameworkom

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.