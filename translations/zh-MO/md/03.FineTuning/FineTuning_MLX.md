# **使用 Apple MLX Framework 微調 Phi-3**

我們可以通過 Apple MLX Framework 的命令行完成結合 Lora 的微調工作。（如果您想了解更多關於 MLX Framework 的操作，請閱讀 [使用 Apple MLX Framework 進行 Phi-3 推論](../03.FineTuning/03.Inference/MLX_Inference.md)）


## **1. 數據準備**

MLX Framework 預設需要 train、test 及 eval 的 jsonl 格式數據，並結合 Lora 完成微調任務。


### ***注意：***

1. jsonl 數據格式 ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 我們的範例使用 [TruthfulQA 的數據](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)，但數據量相對不足，因此微調結果未必最佳。建議學習者依據自身場景使用更合適的數據完成微調。

3. 數據格式結合 Phi-3 模板

請從此 [連結](../../../../code/04.Finetuning/mlx) 下載數據，請確保 ***data*** 資料夾裡包含所有 .jsonl 檔案


## **2. 在終端執行微調**

請在終端執行此命令


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***注意：***

1. 這是 LoRA 微調，MLX Framework 尚未發布 QLoRA

2. 您可以透過 config.yaml 設定來更改部分參數，例如


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

請在終端執行此命令


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. 運行微調適配器進行測試**

您可以在終端運行微調適配器，如此 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

並運行原始模型進行結果比較 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

您可以嘗試比較微調後的結果與原始模型


## **4. 合併適配器生成新模型**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. 使用 ollama 運行量化微調模型**

使用前，請配置您的 llama.cpp 環境


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意：*** 

1. 現在支持 fp32、fp16 及 INT 8 的量化轉換

2. 合併的模型缺少 tokenizer.model，請從 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 下載

設置一個 [Ollma 模型](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

在終端運行命令


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

恭喜！掌握使用 MLX Framework 進行微調

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->