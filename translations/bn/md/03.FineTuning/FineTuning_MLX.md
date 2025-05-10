<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:41:41+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "bn"
}
-->
# **Apple MLX Framework দিয়ে Phi-3 ফাইন-টিউনিং**

Apple MLX Framework কমান্ড লাইন ব্যবহার করে আমরা Lora এর সাথে মিলিয়ে ফাইন-টিউনিং সম্পন্ন করতে পারি। (যদি আপনি MLX Framework এর কাজ সম্পর্কে আরও জানতে চান, অনুগ্রহ করে পড়ুন [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **১. ডেটা প্রস্তুতি**

ডিফল্টভাবে, MLX Framework ট্রেন, টেস্ট, এবং ইভ্যাল এর জন্য jsonl ফরম্যাট চায়, এবং এটি Lora এর সাথে মিলিয়ে ফাইন-টিউনিং কাজ সম্পন্ন করে।


### ***Note:***

১. jsonl ডেটা ফরম্যাট ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

২. আমাদের উদাহরণে [TruthfulQA এর ডেটা](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ব্যবহার করা হয়েছে, কিন্তু ডেটার পরিমাণ তুলনামূলকভাবে কম হওয়ায় ফাইন-টিউনিং ফলাফল সর্বোত্তম নাও হতে পারে। শিক্ষার্থীদের তাদের নিজস্ব পরিস্থিতির ভিত্তিতে উন্নত ডেটা ব্যবহার করে কাজ সম্পন্ন করার পরামর্শ দেওয়া হয়।

৩. ডেটা ফরম্যাট Phi-3 টেমপ্লেটের সাথে মিলিয়ে তৈরি করা হয়েছে।

এই [লিঙ্ক](../../../../code/04.Finetuning/mlx) থেকে ডেটা ডাউনলোড করুন, ***data*** ফোল্ডারের সমস্ত .jsonl অন্তর্ভুক্ত করতে ভুলবেন না।


## **২. আপনার টার্মিনালে ফাইন-টিউনিং চালানো**

টার্মিনালে নিচের কমান্ডটি চালান


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

১. এটি LoRA ফাইন-টিউনিং, MLX Framework QLoRA প্রকাশ করেনি

২. আপনি config.yaml এ কিছু আর্গুমেন্ট পরিবর্তন করতে পারেন, যেমন


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

টার্মিনালে নিচের কমান্ডটি চালান


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **৩. ফাইন-টিউনিং অ্যাডাপ্টার টেস্ট চালানো**

টার্মিনালে ফাইন-টিউনিং অ্যাডাপ্টার এইভাবে চালাতে পারেন


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

এবং ফলাফল তুলনা করার জন্য মূল মডেল চালান


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

আপনি ফাইন-টিউনিং ফলাফল এবং মূল মডেলের ফলাফল তুলনা করতে পারেন


## **৪. নতুন মডেল তৈরি করতে অ্যাডাপ্টার মার্জ করা**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **৫. ollama ব্যবহার করে কোয়ান্টাইজড ফাইন-টিউনিং মডেল চালানো**

ব্যবহারের আগে, অনুগ্রহ করে আপনার llama.cpp পরিবেশ কনফিগার করুন


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

১. এখন fp32, fp16 এবং INT 8 কোয়ান্টাইজেশন রূপান্তর সমর্থিত

২. মার্জ করা মডেলে tokenizer.model নেই, এটি https://huggingface.co/microsoft/Phi-3-mini-4k-instruct থেকে ডাউনলোড করুন

একটি [Ollma Model](https://ollama.com/) সেট করুন


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

টার্মিনালে কমান্ড চালান


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

অভিনন্দন! MLX Framework দিয়ে ফাইন-টিউনিং মাস্টার করলেন

**দ্রষ্টব্য**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।