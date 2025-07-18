<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T08:02:29+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "hu"
}
-->
# **Phi-3 finomhangolása az Apple MLX keretrendszerrel**

A finomhangolást Lora-val kombinálva az Apple MLX keretrendszer parancssorán keresztül végezhetjük el. (Ha többet szeretnél megtudni az MLX keretrendszer működéséről, kérlek olvasd el a [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) dokumentumot)


## **1. Adatelőkészítés**

Alapértelmezés szerint az MLX keretrendszer jsonl formátumot igényel a train, test és eval fájlokhoz, és Lora-val kombinálva végzi el a finomhangolási feladatokat.


### ***Megjegyzés:***

1. jsonl adatformátum ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Példánkban a [TruthfulQA adatait](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) használjuk, de az adatmennyiség viszonylag kevés, ezért a finomhangolás eredményei nem feltétlenül a legjobbak. Ajánlott, hogy a tanulók saját szcenáriójuk alapján jobb adatokat használjanak a finomhangoláshoz.

3. Az adatformátum a Phi-3 sablonnal van kombinálva

Kérlek töltsd le az adatokat erről a [linkről](../../../../code/04.Finetuning/mlx), kérjük, hogy az összes .jsonl fájl legyen benne a ***data*** mappában


## **2. Finomhangolás a terminálban**

Futtasd ezt a parancsot a terminálban


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Megjegyzés:***

1. Ez LoRA finomhangolás, az MLX keretrendszer nem publikált QLoRA-t

2. A config.yaml fájlban beállíthatsz néhány argumentumot, például


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

Futtasd ezt a parancsot a terminálban


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Finomhangolt adapter tesztelése**

A finomhangolt adaptert a terminálban így futtathatod


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

és az eredeti modellt is futtathatod az összehasonlításhoz


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Próbáld ki az összehasonlítást a finomhangolt és az eredeti modell között


## **4. Adapterek egyesítése új modellek létrehozásához**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Kvantált finomhangolt modellek futtatása ollama-val**

Használat előtt kérlek állítsd be a llama.cpp környezetedet


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Megjegyzés:*** 

1. Most támogatja az fp32, fp16 és INT 8 kvantálási átalakítást

2. Az egyesített modellből hiányzik a tokenizer.model, kérlek töltsd le innen: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

állíts be egy [Ollma Modelt](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

futtasd a parancsot a terminálban


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Gratulálunk! Most már mesterien kezeled a finomhangolást az MLX keretrendszerrel

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.