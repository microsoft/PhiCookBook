# **使用 Apple MLX 框架微調 Phi-3**

我們可以透過 Apple MLX 框架命令行來完成結合 Lora 的微調工作。（如果想了解更多 MLX 框架的操作，請閱讀 [使用 Apple MLX 框架推論 Phi-3](../03.FineTuning/03.Inference/MLX_Inference.md)）


## **1. 數據準備**

MLX 框架預設需要 train、test 和 eval 的 jsonl 格式數據，並結合 Lora 完成微調任務。


### ***注意:***

1. jsonl 數據格式 ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 我們的示例使用了 [TruthfulQA 的數據](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)，但數據量相對不足，因此微調結果不一定最佳。建議學習者依照自身場景使用更優質的數據完成。

3. 數據格式結合了 Phi-3 模板

請從此 [連結](../../../../code/04.Finetuning/mlx) 下載數據，請包含 ***data*** 資料夾中的所有 .jsonl


## **2. 在終端機執行微調**

請在終端機執行此指令


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***注意:***

1. 這是 LoRA 微調，MLX 框架尚未發布 QLoRA

2. 你可以設定 config.yaml 改變部分參數，例如


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

請在終端機執行此指令


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. 運行微調適配器測試**

你可以在終端機運行微調適配器，類似這樣


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

並運行原始模型來比較結果


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

你可以嘗試比較微調後與原始模型的結果


## **4. 合併適配器生成新模型**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. 使用 ollama 執行量化微調模型**

使用前請先配置你的 llama.cpp 環境


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意:*** 

1. 目前支援 fp32、fp16 和 INT 8 的量化轉換

2. 合併模型缺少 tokenizer.model，請從 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 下載

設定一個 [Ollma 模型](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

在終端機運行指令


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

恭喜！你已掌握使用 MLX 框架進行微調

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->