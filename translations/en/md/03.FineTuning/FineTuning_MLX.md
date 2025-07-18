<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T07:56:04+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "en"
}
-->
# **Fine-tuning Phi-3 with Apple MLX Framework**

We can perform fine-tuning combined with LoRA through the Apple MLX framework command line. (If you want to learn more about how the MLX Framework works, please read [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. Data preparation**

By default, the MLX Framework requires train, test, and eval data in jsonl format, and uses LoRA to complete fine-tuning tasks.

### ***Note:***

1. jsonl data format:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Our example uses [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), but the dataset is relatively small, so the fine-tuning results may not be optimal. We recommend learners use better data suited to their own scenarios.

3. The data format follows the Phi-3 template.

Please download the data from this [link](../../../../code/04.Finetuning/mlx), including all .jsonl files in the ***data*** folder.

## **2. Fine-tuning in your terminal**

Run this command in your terminal:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Note:***

1. This is LoRA fine-tuning; the MLX framework does not support QLoRA.

2. You can modify config.yaml to change some parameters, such as:

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

Run this command in your terminal:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Run fine-tuning adapter to test**

You can run the fine-tuning adapter in the terminal like this:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

And run the original model to compare results:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Try comparing the fine-tuned results with the original model.

## **4. Merge adapters to generate new models**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Running quantized fine-tuning models using ollama**

Before use, please set up your llama.cpp environment.

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:***

1. Currently supports quantization conversion for fp32, fp16, and INT8.

2. The merged model lacks tokenizer.model; please download it from https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

Set up an [Ollama Model](https://ollama.com/)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Run this command in the terminal:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Congratulations! You’ve mastered fine-tuning with the MLX Framework.

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.