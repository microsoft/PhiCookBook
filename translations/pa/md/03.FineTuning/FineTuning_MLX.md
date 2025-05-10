<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:42:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "pa"
}
-->
# **Apple MLX Framework ਨਾਲ Phi-3 ਦੀ Fine-tuning**

ਅਸੀਂ Apple MLX Framework ਦੇ ਕਮਾਂਡ ਲਾਈਨ ਰਾਹੀਂ Lora ਦੇ ਨਾਲ ਮਿਲਾ ਕੇ Fine-tuning ਕਰ ਸਕਦੇ ਹਾਂ। (ਜੇ ਤੁਹਾਨੂੰ MLX Framework ਦੇ ਚਾਲੂ ਹੋਣ ਬਾਰੇ ਹੋਰ ਜਾਣਨਾ ਹੈ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) ਪੜ੍ਹੋ)


## **1. ਡਾਟਾ ਤਿਆਰੀ**

ਡਿਫਾਲਟ ਰੂਪ ਵਿੱਚ, MLX Framework train, test, ਅਤੇ eval ਲਈ jsonl ਫਾਰਮੈਟ ਦੀ ਮੰਗ ਕਰਦਾ ਹੈ, ਅਤੇ Lora ਨਾਲ ਮਿਲਾ ਕੇ fine-tuning ਕੰਮ ਮੁਕੰਮਲ ਕਰਦਾ ਹੈ।


### ***Note:***

1. jsonl ਡਾਟਾ ਫਾਰਮੈਟ ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ਸਾਡਾ ਉਦਾਹਰਨ [TruthfulQA ਦਾ ਡਾਟਾ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ਵਰਤਦਾ ਹੈ, ਪਰ ਡਾਟਾ ਦੀ ਮਾਤਰਾ ਥੋੜ੍ਹੀ ਹੈ, ਇਸ ਲਈ fine-tuning ਦੇ ਨਤੀਜੇ ਜ਼ਰੂਰੀ ਨਹੀਂ ਕਿ ਸਭ ਤੋਂ ਵਧੀਆ ਹੋਣ। ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਸਿੱਖਣ ਵਾਲੇ ਆਪਣੇ ਸੰਦਰਭ ਅਨੁਸਾਰ ਵਧੀਆ ਡਾਟਾ ਵਰਤਣ।

3. ਡਾਟਾ ਫਾਰਮੈਟ Phi-3 ਟੈਮਪਲੇਟ ਨਾਲ ਮਿਲਾ ਕੇ ਹੈ

ਕਿਰਪਾ ਕਰਕੇ ਇਸ [ਲਿੰਕ](../../../../code/04.Finetuning/mlx) ਤੋਂ ਡਾਟਾ ਡਾਊਨਲੋਡ ਕਰੋ, ਅਤੇ ***data*** ਫੋਲਡਰ ਵਿੱਚ ਸਾਰੇ .jsonl ਸ਼ਾਮਲ ਕਰੋ


## **2. ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ Fine-tuning**

ਕਿਰਪਾ ਕਰਕੇ ਟਰਮੀਨਲ ਵਿੱਚ ਇਹ ਕਮਾਂਡ ਚਲਾਓ


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. ਇਹ LoRA fine-tuning ਹੈ, MLX framework ਨੇ QLoRA ਜਾਰੀ ਨਹੀਂ ਕੀਤਾ

2. ਤੁਸੀਂ config.yaml ਵਿੱਚ ਕੁਝ arguments ਬਦਲ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ


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

ਕਿਰਪਾ ਕਰਕੇ ਟਰਮੀਨਲ ਵਿੱਚ ਇਹ ਕਮਾਂਡ ਚਲਾਓ


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Fine-tuning adapter ਨੂੰ ਟੈਸਟ ਕਰਨ ਲਈ ਚਲਾਓ**

ਤੁਸੀਂ ਟਰਮੀਨਲ ਵਿੱਚ fine-tuning adapter ਇਸ ਤਰ੍ਹਾਂ ਚਲਾ ਸਕਦੇ ਹੋ


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ਅਤੇ ਨਤੀਜੇ ਦੀ ਤੁਲਨਾ ਕਰਨ ਲਈ ਅਸਲ ਮਾਡਲ ਚਲਾਓ


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ਤੁਸੀਂ Fine-tuning ਦੇ ਨਤੀਜੇ ਅਸਲ ਮਾਡਲ ਨਾਲ ਤੁਲਨਾ ਕਰ ਸਕਦੇ ਹੋ


## **4. ਨਵੇਂ ਮਾਡਲ ਬਣਾਉਣ ਲਈ adapters ਨੂੰ ਮਰਜ ਕਰੋ**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama ਵਰਤ ਕੇ quantified fine-tuning ਮਾਡਲ ਚਲਾਉਣਾ**

ਵਰਤੋਂ ਤੋਂ ਪਹਿਲਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਆਪਣਾ llama.cpp ਵਾਤਾਵਰਣ ਸੈਟ ਕਰੋ


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. ਹੁਣ fp32, fp16 ਅਤੇ INT 8 ਦੀ quantization conversion ਸਹਾਇਤਾ ਕਰਦਾ ਹੈ

2. ਮਰਜ ਕੀਤਾ ਮਾਡਲ tokenizer.model ਗੁੰਮ ਹੈ, ਕਿਰਪਾ ਕਰਕੇ ਇਸਨੂੰ https://huggingface.co/microsoft/Phi-3-mini-4k-instruct ਤੋਂ ਡਾਊਨਲੋਡ ਕਰੋ

[Ollma Model](https://ollama.com/) ਸੈਟ ਕਰੋ


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ਟਰਮੀਨਲ ਵਿੱਚ ਕਮਾਂਡ ਚਲਾਓ


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

ਵਧਾਈ ਹੋਵੇ! MLX Framework ਨਾਲ fine-tuning 'ਚ ਮਾਹਰ ਬਣੋ

**ਡਿਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਹੀਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।