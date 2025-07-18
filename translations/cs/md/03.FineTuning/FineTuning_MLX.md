<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T08:02:39+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "cs"
}
-->
# **Doladění Phi-3 pomocí Apple MLX Frameworku**

Doladění v kombinaci s Lora můžeme provést přes příkazový řádek Apple MLX frameworku. (Pokud chcete vědět více o fungování MLX Frameworku, přečtěte si prosím [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Příprava dat**

Výchozí požadavek MLX Frameworku je formát jsonl pro tréninková, testovací a evaluační data, která se kombinují s Lora pro dokončení doladění.


### ***Poznámka:***

1. formát jsonl dat ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Náš příklad používá [data TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), ale množství dat je relativně nedostatečné, takže výsledky doladění nemusí být nejlepší. Doporučujeme, aby si uživatelé na základě svých scénářů připravili lepší data.

3. Formát dat je kombinován s šablonou Phi-3

Prosím stáhněte data z tohoto [odkazu](../../../../code/04.Finetuning/mlx), zahrňte všechny .jsonl soubory ve složce ***data***


## **2. Doladění v terminálu**

Spusťte tento příkaz v terminálu


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Poznámka:***

1. Jedná se o LoRA doladění, MLX framework nezveřejnil QLoRA

2. Můžete upravit config.yaml a změnit některé argumenty, například


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

Spusťte tento příkaz v terminálu


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Spuštění doladěného adaptéru pro testování**

Doladěný adaptér můžete spustit v terminálu takto


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

a spusťte původní model pro porovnání výsledků


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Můžete zkusit porovnat výsledky doladění s původním modelem


## **4. Sloučení adaptérů pro vytvoření nových modelů**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Spuštění kvantovaných doladěných modelů pomocí ollama**

Před použitím si prosím nastavte své prostředí llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Poznámka:*** 

1. Nyní je podporována kvantizace z fp32, fp16 a INT 8

2. Sloučený model postrádá tokenizer.model, stáhněte si ho prosím z https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

nastavte [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

spusťte příkaz v terminálu


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Gratulujeme! Ovládli jste doladění s MLX Frameworkem

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.