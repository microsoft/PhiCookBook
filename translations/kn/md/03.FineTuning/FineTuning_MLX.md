<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-12-21T18:54:06+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "kn"
}
-->
# **Apple MLX ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ Phi-3 ಫೈನ್‑ಟ್ಯೂನಿಂಗ್**

ನಾವು Apple MLX ಫ್ರೇಮ್ವರ್ಕ್ ಕಮಾಂಡ್ ಲೈನ್ ಮೂಲಕ Lora ಜೊತೆಗೆ ಫೈನ್‑ಟ್ಯೂನಿಂಗ್ ಅನ್ನು ಪೂರ್ಣಗೊಳಿಸಬಹುದು. (MLX ಫ್ರೇಮ್ವರ್ಕ್‌ನ ಕಾರ್ಯವೈಖರಿ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ಮಾಹಿತಿ ಬೇಕಿದ್ದರೆ, ದಯವಿಟ್ಟು [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) ಓದಿರಿ)


## **1. ಡೇಟಾ ತಯಾರಿ**

ಡೀಫಾಲ್ಟ್ ಆಗಿ, MLX ಫ್ರೇಮ್ವರ್ಕ್‌ಗೆ train, test, ಮತ್ತು eval ಗಾಗಿ jsonl ಫಾರ್ಮ್ಯಾಟ್ ಬೇಕಾಗುತ್ತದೆ, ಮತ್ತು ಇದು Lora ಜೊತೆಗೆ ಸಂಯೋಜಿಸಿ ಫೈನ್‑ಟ್ಯೂನಿಂಗ್ ಕೆಲಸಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸುತ್ತದೆ.


### ***ಗಮನಿಸಿ:***

1. jsonl ಡೇಟಾ ಫಾರ್ಮ್ಯಾಟ್ ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ನಮ್ಮ ಉದಾಹರಣೆಗೆ [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ಅನ್ನು ಬಳಸಲಾಗಿದೆ, ಆದರೆ ಡೇಟಾ ಪ್ರಮಾಣ relatively ಕಡಿಮೆ ಇದೆ, ಆದ್ದರಿಂದ ಫೈನ್‑ಟ್ಯೂನಿಂಗ್ ಫಲಿತಾಂಶಗಳು ಅಗತ್ಯವಾಗಿ ಅತ್ಯುತ್ತಮವಾಗಿರಲಾರವು. ಕಲಿತವರು ತಮ್ಮದೇ ಸನ್ನಿವೇಶಗಳ ಆಧಾರದ ಮೇಲೆ ಉತ್ತಮ ಡೇಟಾವನ್ನು ಬಳಸುವುದನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ.

3. ಡೇಟಾ ಫಾರ್ಮ್ಯಾಟ್ ಅನ್ನು Phi-3 ಟೆಂಪ್ಲೇಟಿನೊಂದಿಗೆ ಸಂಯೋಜಿಸಲಾಗಿದೆ

ದಯವಿಟ್ಟು ಈ [ಲಿಂಕ್](../../../../code/04.Finetuning/mlx) ರಿಂದ ಡೇಟಾವನ್ನು ಡೌನ್‌‌ಲೋಡ್ ಮಾಡಿ, ದಯವಿಟ್ಟು ಎಲ್ಲಾ .jsonl ಫೈಲ್‌ಗಳನ್ನು ***data*** ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಸೇರಿಸಿ


## **2. ನಿಮ್ಮ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಫೈನ್‑ಟ್ಯೂನಿಂಗ್**

ದಯವಿಟ್ಟು ಈ ಕಮಾಂಡ್ ಅನ್ನು ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಚಲಾಯಿಸಿ


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***ಗಮನಿಸಿ:***

1. ಇದು LoRA ಫೈನ್‑ಟ್ಯೂನಿಂಗ್ ಆಗಿದೆ, MLX ಫ್ರೇಮ್ವರ್ಕ್ QLoRA ಅನ್ನು ಪ್ರಕಟಿಸಿಲ್ಲ

2. ನೀವು config.yaml ಅನ್ನು ಸೆಟ್ ಮಾಡಿ ಕೆಲವು ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಬದಲಾಯಿಸಬಹುದು, ಉದಾಹರಣೆಗೆ


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

ದಯವಿಟ್ಟು ಈ ಕಮಾಂಡ್ ಅನ್ನು ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಚಲಾಯಿಸಿ


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. ಟೆಸ್ಟ್ ಮಾಡಲು ಫೈನ್‑ಟ್ಯೂನಿಂಗ್ ಅಡಾಪ್ಟರ್ ಅನ್ನು ರನ್ ಮಾಡಿ**

ನೀವು ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಫೈನ್‑ಟ್ಯೂನಿಂಗ್ ಅಡಾಪ್ಟರ್ ಅನ್ನು ರನ್ ಮಾಡಬಹುದು, ಹೀಗೆ


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

and run original model  to compare result 
```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ನೀವು ಫೈನ್‑ಟ್ಯೂನಿಂಗ್‌ನ ಫಲಿತಾಂಶಗಳನ್ನು ಮೂಲ ಮಾದರಿಯೊಂದಿಗೆ ಹೋಲಿಸಲು ಪ್ರಯತ್ನಿಸಬಹುದು


## **4. ಹೊಸ ಮಾದರಿಗಳನ್ನು ರಚಿಸಲು ಅಡಾಪ್ಟರ್ ಗಳನ್ನು ಮರ್ಜ್ ಮಾಡಿ**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama ಬಳಸಿ ಕ್ವಾಂಟೈಜ್ಡ್ ಫೈನ್‑ಟ್ಯೂನಿಂಗ್ ಮಾದರಿಗಳನ್ನು ಚಲಾಯಿಸುವುದು**

ಬಳಕೆಗಿಂತ ಮೊದಲು, ದಯವಿಟ್ಟು ನಿಮ್ಮ llama.cpp ಪರಿಸರವನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***ಗಮನಿಸಿ:*** 

1. ಈಗ fp32, fp16 ಮತ್ತು INT 8 ಗಳು ಕ್ವಾಂಟೈಜೆಶನ್ ಪರಿವರ್ತನೆಯನ್ನು ಬೆಂಬಲಿಸುತ್ತವೆ

2. ಮರ್ಜ್ ಮಾಡಿದ ಮಾದರಿಯಲ್ಲಿ tokenizer.model ಕಾಣುತ್ತಿಲ್ಲ, ದಯವಿಟ್ಟು ಇದನ್ನು https://huggingface.co/microsoft/Phi-3-mini-4k-instruct ರಿಂದ ಡೌನ್‌‌ಲೋಡ್ ಮಾಡಿ

ಒಂದು [Ollma Model](https://ollama.com/) ಅನ್ನು ಸೆಟ್ ಮಾಡಿ


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕಮಾಂಡ್ ಅನ್ನು ರನ್ ಮಾಡಿ


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

ಅಭಿನಂದನೆಗಳು! MLX ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ ಫೈನ್‑ಟ್ಯೂನಿಂಗ್‌ನಲ್ಲಿ ಪರಿಣತಿ ಸಾಧಿಸಿದ್ದೀರಿ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯನ್ನು ಕಾಯ್ದುಕೊಳ್ಳಲು ಪ್ರಯತ್ನಿಸುವುದಲ್ಲದೆ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅನಿಖಲತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲದಸ್ತಾವೇಜನ್ನು ಅದರ ಮೂಲ ಭಾಷೆಯಲ್ಲಿಯೇ ಆಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗೊಳ್ಳುವಿಕೆಗಳಿಗೆ ಅಥವಾ ತಪ್ಪಾಗಿ ವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->