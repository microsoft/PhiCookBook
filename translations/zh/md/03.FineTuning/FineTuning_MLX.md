<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T07:57:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "zh"
}
-->
# **使用 Apple MLX 框架微调 Phi-3**

我们可以通过 Apple MLX 框架的命令行完成结合 Lora 的微调。（如果想了解更多关于 MLX 框架的操作，请阅读 [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)）

## **1. 数据准备**

默认情况下，MLX 框架要求训练、测试和评估数据为 jsonl 格式，并结合 Lora 完成微调任务。

### ***Note:***

1. jsonl 数据格式：

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 我们的示例使用了 [TruthfulQA 的数据](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)，但数据量相对较少，因此微调效果不一定最佳。建议学习者根据自身场景使用更优质的数据完成微调。

3. 数据格式需结合 Phi-3 模板

请从此[链接](../../../../code/04.Finetuning/mlx)下载数据，确保包含 ***data*** 文件夹中的所有 .jsonl 文件。

## **2. 在终端进行微调**

请在终端运行以下命令：

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Note:***

1. 这是 LoRA 微调，MLX 框架尚未发布 QLoRA

2. 你可以通过修改 config.yaml 来调整部分参数，例如：

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

请在终端运行以下命令：

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. 运行微调适配器进行测试**

你可以在终端运行微调适配器，命令如下：

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

也可以运行原始模型进行结果对比：

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

你可以尝试比较微调模型与原始模型的结果差异。

## **4. 合并适配器生成新模型**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. 使用 ollama 运行量化微调模型**

使用前，请先配置好你的 llama.cpp 环境。

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:***

1. 目前支持 fp32、fp16 和 INT8 的量化转换

2. 合并后的模型缺少 tokenizer.model，请从 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 下载

设置一个 [Ollma Model](https://ollama.com/)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

在终端运行命令：

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

恭喜！你已掌握使用 MLX 框架进行微调的方法。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。