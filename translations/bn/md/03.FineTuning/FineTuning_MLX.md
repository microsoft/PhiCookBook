# **অ্যাপল MLX ফ্রেমওয়ার্ক দিয়ে Phi-3 ফাইন-টিউনিং**

আমরা অ্যাপল MLX ফ্রেমওয়ার্ক কমান্ড লাইনের মাধ্যমে লোরা সহিত ফাইন-টিউনিং সম্পন্ন করতে পারি। (আপনি যদি MLX ফ্রেমওয়ার্কের অপারেশন সম্পর্কে আরও জানতে চান, অনুগ্রহ করে পড়ুন [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **১. ডেটা প্রস্তুতি**

ডিফল্টরূপে, MLX ফ্রেমওয়ার্ক ট্রেন, টেস্ট এবং ইভ্যালের jsonl ফরম্যাট দাবি করে, এবং লোরা সহিত মিলিয়ে ফাইন-টিউনিং কাজ সম্পন্ন করে।


### ***বিঃদ্রঃ:***

১. jsonl ডেটা ফরম্যাট ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

২. আমাদের উদাহরণ ব্যবহার করেছে [TruthfulQA-এর ডেটা](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), কিন্তু ডেটার পরিমাণ অপেক্ষাকৃত কম, তাই ফাইন-টিউনিং ফলাফল সর্বোত্তম নাও হতে পারে। শেখানরদের জন্য সুপারিশ করা হয় যে তারা তাদের নিজস্ব পরিস্থিতির উপর ভিত্তি করে উন্নত ডেটা ব্যবহার করে কাজ সম্পন্ন করুন।

৩. ডেটা ফরম্যাট Phi-3 টেমপ্লেটের সাথে মিলেছে

অনুগ্রহ করে এই [লিঙ্ক](../../../../code/04.Finetuning/mlx) থেকে ডেটা ডাউনলোড করুন, ***data*** ফোল্ডারে সব .jsonl অন্তর্ভুক্ত থাকবে


## **২. আপনার টার্মিনালে ফাইন-টিউনিং**

অনুগ্রহ করে টার্মিনালে এই কমান্ড চালান


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***বিঃদ্রঃ:***

১. এটি LoRA ফাইন-টিউনিং, MLX ফ্রেমওয়ার্ক QLoRA প্রকাশ করেনি

২. আপনি config.yaml-এ কিছু আর্গুমেন্ট পরিবর্তন করতে পারেন, যেমন


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

অনুগ্রহ করে টার্মিনালে এই কমান্ড চালান


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **৩. ফাইন-টিউনিং অ্যাডাপ্টার পরীক্ষা চালান**

আপনি টার্মিনালে ফাইন-টিউনিং অ্যাডাপ্টার চালাতে পারেন, এই রকম


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

এবং ফলাফল তুলনা করতে মূল মডেল চালান


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

আপনি ফাইন-টিউনিং এবং মূল মডেলের ফলাফল তুলনা করতে পারেন


## **৪. নতুন মডেল তৈরির জন্য অ্যাডাপ্টার মার্জ করুন**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **৫. ollama ব্যবহার করে পরিমাণগত ফাইন-টিউনিং মডেল চালানো**

ব্যবহারের আগে, অনুগ্রহ করে আপনার llama.cpp পরিবেশ কনফিগার করুন


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***বিঃদ্রঃ:*** 

১. এখন fp32, fp16 এবং INT 8 এর পরিমাণগত রূপান্তর সমর্থিত

২. মার্জ করা মডেলটির tokenizer.model অনুপস্থিত, দয়া করে এটি https://huggingface.co/microsoft/Phi-3-mini-4k-instruct থেকে ডাউনলোড করুন

একটি [Ollma মডেল](https://ollama.com/) সেট করুন


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

টার্মিনালে কমান্ড চালান


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

অভিনন্দন! MLX ফ্রেমওয়ার্ক দিয়ে ফাইন-টিউনিং মাস্টার করুন

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->