# **Apple MLX Framework দিয়ে Phi-3 ফাইন-টিউনিং**

আমরা Apple MLX ফ্রেমওয়ার্কের কমান্ড লাইন ব্যবহার করে Lora এর সাথে মিলিয়ে ফাইন-টিউনিং সম্পন্ন করতে পারি। (যদি আপনি MLX Framework এর কাজ সম্পর্কে আরও জানতে চান, অনুগ্রহ করে [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) পড়ুন)

## **1. ডেটা প্রস্তুতি**

ডিফল্ট হিসেবে, MLX Framework ট্রেন, টেস্ট, এবং ইভ্যাল এর জন্য jsonl ফরম্যাট চায়, এবং এটি Lora এর সাথে মিলিয়ে ফাইন-টিউনিং কাজ সম্পন্ন করে।

### ***Note:***

1. jsonl ডেটা ফরম্যাটঃ

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. আমাদের উদাহরণে [TruthfulQA এর ডেটা](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ব্যবহার করা হয়েছে, কিন্তু ডেটার পরিমাণ তুলনামূলকভাবে কম, তাই ফাইন-টিউনিং এর ফলাফল সর্বোত্তম নাও হতে পারে। শিক্ষার্থীদের পরামর্শ দেওয়া হয় তাদের নিজস্ব পরিস্থিতির ভিত্তিতে ভালো ডেটা ব্যবহার করে কাজ সম্পন্ন করতে।

3. ডেটা ফরম্যাট Phi-3 টেমপ্লেটের সাথে মিলিয়ে তৈরি করা হয়েছে।

অনুগ্রহ করে এই [লিঙ্ক](../../../../code/04.Finetuning/mlx) থেকে ডেটা ডাউনলোড করুন, ***data*** ফোল্ডারের সব .jsonl ফাইল অন্তর্ভুক্ত করতে ভুলবেন না।

## **2. টার্মিনালে ফাইন-টিউনিং করা**

টার্মিনালে নিচের কমান্ডটি চালান

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Note:***

1. এটি LoRA ফাইন-টিউনিং, MLX ফ্রেমওয়ার্ক QLoRA প্রকাশ করেনি।

2. আপনি config.yaml এ কিছু আর্গুমেন্ট পরিবর্তন করতে পারেন, যেমন

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

## **3. ফাইন-টিউনিং অ্যাডাপ্টার টেস্ট করা**

টার্মিনালে ফাইন-টিউনিং অ্যাডাপ্টার চালাতে পারেন, যেমন

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

এবং ফলাফল তুলনা করার জন্য মূল মডেল চালান

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

আপনি ফাইন-টিউনিং এবং মূল মডেলের ফলাফল তুলনা করে দেখতে পারেন।

## **4. নতুন মডেল তৈরির জন্য অ্যাডাপ্টার মার্জ করা**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama দিয়ে কোয়ান্টাইজড ফাইন-টিউনিং মডেল চালানো**

ব্যবহারের আগে, আপনার llama.cpp পরিবেশ কনফিগার করুন

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:***

1. এখন fp32, fp16 এবং INT 8 কোয়ান্টাইজেশন রূপান্তর সমর্থিত।

2. মার্জ করা মডেলে tokenizer.model নেই, এটি https://huggingface.co/microsoft/Phi-3-mini-4k-instruct থেকে ডাউনলোড করুন।

একটি [Ollma Model](https://ollama.com/) সেট করুন।

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

টার্মিনালে কমান্ড চালান

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

অভিনন্দন! MLX Framework দিয়ে ফাইন-টিউনিং আয়ত্ত করেছেন।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।