<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-12-21T18:53:20+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "ml"
}
-->
# **Apple MLX Framework ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്**

Apple MLX ഫ്രെയിംവർക് കമാൻഡ് ലൈൻ വഴി Lora-യുമായി സംയോജിപ്പിച്ച ഫൈൻ-ട്യൂണിംഗ് പൂർത്തിയാക്കാം. (MLX Framework-ന്റെ പ്രവർത്തനത്തെക്കുറിച്ച് കൂടുതൽ അറിയാൻ, ദയവായി [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) വായിക്കുക)


## **1. ഡാറ്റ തയ്യാറാക്കൽ**

സ്വഭാവികമായി, MLX Framework ട്രെയിൻ, ടെസ്റ്റ്, eval എന്നിവയ്ക്ക് jsonl ഫോർമാറ്റ് ആവശ്യപ്പെടുന്നു, കൂടാതെ ഫൈൻ-ട്യൂണിംഗ് ജോബുകൾ പൂർത്തിയാക്കാൻ അതിനെ Lora-യുമായി സംയോജിപ്പിക്കുന്നു.


### ***കുറിപ്പ്:***

1. jsonl ഡാറ്റ ഫോർമാറ്റ് ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ഞങ്ങളുടെ ഉദാഹരണം [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ഉപയോഗിക്കുന്നു, പക്ഷേ ഡാറ്റയുടെ അളവ് സംബന്ധത്തിൽ കുറവാണ്, അതിനാൽ ഫൈൻ-ട്യൂണിംഗ് ഫലങ്ങൾ നിർണായകമായി മികച്ചതായിരിക്കണമെന്നില്ല. പഠിക്കാവുന്നവര്‍ക്ക് അവരുടെ സ്വന്തം സാഹചര്യങ്ങളെ അടിസ്ഥാനമാക്കി മികച്ച ഡാറ്റ ഉപയോഗിച്ച് പൂർത്തിയാക്കാൻ ശുപാർശ ചെയ്യുന്നു.

3. ഡാറ്റ ഫോർമാറ്റ് Phi-3 ടെംപ്ലേറ്റുമായി സംയോജിപ്പിച്ചിരിക്കുന്നു

ദയവായി ഈ [ലിങ്ക്](../../../../code/04.Finetuning/mlx) ൽ നിന്ന് ഡാറ്റ ഡൗൺലോഡ് ചെയ്യുക, ദയവായി ***data*** ഫോളഡറിൽ ഉള്ള എല്ലാ .jsonl ഫയലുകളും ഉൾപ്പെടുത്തുക


## **2. നിങ്ങളുടെ ടെർമിനലിൽ ഫൈൻ-ട്യൂണിംഗ്**

ദയവായി ഈ കമാൻഡ് ടെർമിനലിൽ പ്രവർത്തിപ്പിക്കുക


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***കുറിപ്പ്:***

1. ഇത് LoRA ഫൈൻ-ട്യൂണിംഗ് ആണ്, MLX framework QLoRA പുറത്തിറക്കിയിട്ടില്ല

2. ചില ആഗ്യുമെന്റ്‌സ് മാറ്റാൻ config.yaml ക്രമീകരിക്കാൻ കഴിയും, ഉദാഹരണത്തിന്


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

ദയവായി ഈ കമാൻഡ് ടെർമിനലിൽ പ്രവർത്തിപ്പിക്കുക


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. ടെസ്റ്റ് ചെയ്യാൻ ഫൈൻ-ട്യൂണിംഗ് അഡാപ്റ്റർ റൺ ചെയ്യുക**

നിങ്ങൾ ഫൈൻ-ട്യൂണിംഗ് അഡാപ്റ്റർ ടെർമിനലിൽ ഇങ്ങനെ റൺ ചെയ്യാം 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ഫലങ്ങൾ താരതമ്യം ചെയ്യാൻ ഒറിജിനൽ മോഡൽ റൺ ചെയ്യുക


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ഫൈൻ-ട്യൂണിംഗ് ഫലങ്ങളെ ഓറിജിനൽ മോഡലിന്റെ ഫലങ്ങളുമായി താരതമ്യം ചെയ്യാൻ നിങ്ങൾ ശ്രമിക്കാം


## **4. അഡാപ്റ്ററുകൾ ലയിപ്പിച്ച് പുതിയ മോഡലുകൾ ഉണ്ടാക്കൽ**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama ഉപയോഗിച്ച് ക്വാണ്ടൈസ്ഡ് ഫൈൻ-ട്യൂണിംഗ് മോഡലുകൾ റൺ ചെയ്യൽ**

ഉപയോഗിക്കുന്നതിന് മുമ്പ്, ദയവായി നിങ്ങളുടെ llama.cpp പരിസ്ഥിതി ക്രമീകരിക്കുക


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***കുറിപ്പ്:*** 

1. ഇപ്പോൾ fp32, fp16 மற்றும் INT 8 ന്റെ ക്വാണ്ടൈസേഷൻ കൺവേഴ്സൻ പിന്തുണക്കുന്നു

2. ലയിച്ച മോഡലിന് tokenizer.model ഇല്ല, ദയവായി അതിനെ https://huggingface.co/microsoft/Phi-3-mini-4k-instruct നിന്ന് ഡൗൺലോഡ് ചെയ്യുക

ഒരു [Ollma Model](https://ollama.com/) സജ്ജമാക്കുക


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ടെർമിനലിൽ കമാൻഡ് റൺ ചെയ്യുക


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

അഭിനന്ദനങ്ങൾ! MLX Framework ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ് നൈപുണ്യം കൈവരിച്ചു

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അറിയിപ്പ്:
ഈ പ്രമാണം AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. നാം കൃത്യതയ്ക്കായി ശ്രമിച്ചെങ്കിലും, ഓട്ടോമേറ്റ് ചെയ്ത പരിഭാഷകൾ തെറ്റുകൾ അല്ലെങ്കിൽ അപൂർവതകൾ ഉൾക്കൊള്ളാവുന്നതാണ് എന്ന് ദയവായി ശ്രദ്ധിക്കുക. മാതൃഭാഷയിലുള്ള യഥാർത്ഥ പ്രമാണം ആധികാരം ഉള്ള ഉറവിടമായി പരിഗണിക്കണം. നിർണായക വിവരങ്ങളേക്കാൾ പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ചതിൽ നിന്നുണ്ടാവുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും ദുർവ്യാഖ്യാനങ്ങൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->