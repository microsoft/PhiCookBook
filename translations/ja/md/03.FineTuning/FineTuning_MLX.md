<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b1ec18a3db0bb90ba8483eceade60031",
  "translation_date": "2025-04-04T13:25:32+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_MLX.md",
  "language_code": "ja"
}
-->
# **Apple MLXフレームワークを使用したPhi-3の微調整**

Apple MLXフレームワークのコマンドラインを使用して、Loraと組み合わせた微調整を完了することができます。（MLXフレームワークの操作について詳しく知りたい場合は、[Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)をお読みください）


## **1. データ準備**

デフォルトでは、MLXフレームワークはtrain、test、evalのjsonl形式を要求し、Loraと組み合わせて微調整を実行します。


### ***注:***

1. jsonlデータ形式：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 例として[TruthfulQAのデータ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)を使用していますが、データ量が比較的少ないため、微調整結果が必ずしも最適であるとは限りません。学習者は自身のシナリオに基づいてより良いデータを使用することをお勧めします。

3. データ形式はPhi-3テンプレートと組み合わせています。

この[リンク](../../../../code/04.Finetuning/mlx)からデータをダウンロードしてください。***data***フォルダ内のすべての.jsonlを含めてください。


## **2. ターミナルで微調整を実行**

ターミナルで以下のコマンドを実行してください。


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***注:***

1. これはLoRA微調整であり、MLXフレームワークはQLoRAを公開していません。

2. config.yamlを設定することで、以下のような引数を変更できます。


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

ターミナルで以下のコマンドを実行してください。


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. 微調整アダプターのテストを実行**

ターミナルで微調整アダプターを実行できます。以下のようにしてください。


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

その後、オリジナルモデルを実行して結果を比較します。


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

微調整結果とオリジナルモデルの結果を比較してみてください。


## **4. アダプターを統合して新しいモデルを生成**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```


## **5. ollamaを使用した量子化済み微調整モデルの実行**

使用前に、llama.cpp環境を構成してください。


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注:*** 

1. 現在、fp32、fp16、およびINT 8の量子化変換をサポートしています。

2. 統合されたモデルにはtokenizer.modelが欠けています。以下からダウンロードしてください：https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

[Ollma Model](https://ollama.com/)を設定してください。


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ターミナルで以下のコマンドを実行してください。


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

おめでとうございます！MLXフレームワークを使用した微調整を習得しました。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる場合がありますのでご了承ください。原文の母国語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や解釈の誤りについて、当社は一切の責任を負いません。