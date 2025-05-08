<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-08T05:14:28+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "hk"
}
-->
# **用 Apple MLX Framework 微調 Phi-3**

我哋可以透過 Apple MLX framework 命令行完成結合 Lora 嘅微調。（如果想了解 MLX Framework 嘅操作，請參考 [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)）

## **1. 數據準備**

MLX Framework 預設要求 train、test 同 eval 嘅 jsonl 格式，並結合 Lora 完成微調任務。

### ***Note:***

1. jsonl 數據格式：

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 我哋嘅例子用咗 [TruthfulQA嘅數據](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)，但數據量比較少，所以微調結果未必係最好。建議學習者根據自己嘅場景使用更合適嘅數據完成微調。

3. 數據格式係結合咗 Phi-3 模板。

請從呢個 [連結](../../../../code/04.Finetuning/mlx) 下載數據，請包含 ***data*** 文件夾入面嘅所有 .jsonl 文件。

## **2. 喺終端機做微調**

請喺終端機運行以下命令

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Note:***

1. 呢個係 LoRA 微調，MLX framework 未有發布 QLoRA。

2. 你可以透過 config.yaml 改啲參數，例如

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

請喺終端機運行以下命令

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. 運行微調 adapter 測試**

你可以喺終端機運行微調 adapter，做法係咁：

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

然後運行原始模型比較結果

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

你可以試下比較微調後同原始模型嘅結果。

## **4. 合併 adapters 生成新模型**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. 用 ollama 運行量化微調模型**

使用之前，請先配置好你嘅 llama.cpp 環境。

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:***

1. 而家支持 fp32、fp16 同 INT 8 嘅量化轉換。

2. 合併後嘅模型缺少 tokenizer.model，請從 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 下載。

設定一個 [Ollma Model](https://ollama.com/)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

喺終端機運行命令

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

恭喜！你已經掌握用 MLX Framework 微調嘅技巧。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應視為權威來源。對於重要資訊，建議採用專業人手翻譯。我哋對因使用本翻譯而引致嘅任何誤解或誤釋概不負責。