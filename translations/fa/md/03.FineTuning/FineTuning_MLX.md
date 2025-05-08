<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-07T13:26:07+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "fa"
}
-->
# **تنظیم دقیق Phi-3 با چارچوب Apple MLX**

می‌توانیم تنظیم دقیق همراه با Lora را از طریق خط فرمان چارچوب Apple MLX انجام دهیم. (اگر می‌خواهید درباره عملکرد چارچوب MLX بیشتر بدانید، لطفاً [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) را مطالعه کنید)


## **1. آماده‌سازی داده‌ها**

به طور پیش‌فرض، چارچوب MLX فرمت jsonl برای train، test و eval را نیاز دارد و با Lora ترکیب می‌شود تا کارهای تنظیم دقیق را کامل کند.


### ***Note:***

1. فرمت داده jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. مثال ما از داده‌های [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) استفاده می‌کند، اما حجم داده‌ها نسبتاً کم است، بنابراین نتایج تنظیم دقیق لزوماً بهترین نیست. توصیه می‌شود یادگیرندگان بر اساس سناریوهای خود از داده‌های بهتری استفاده کنند تا کار را کامل کنند.

3. فرمت داده با قالب Phi-3 ترکیب شده است

لطفاً داده‌ها را از این [لینک](../../../../code/04.Finetuning/mlx) دانلود کنید، لطفاً تمام فایل‌های .jsonl موجود در پوشه ***data*** را شامل کنید


## **2. تنظیم دقیق در ترمینال شما**

لطفاً این دستور را در ترمینال اجرا کنید


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. این تنظیم دقیق LoRA است، چارچوب MLX نسخه QLoRA را منتشر نکرده است

2. می‌توانید با تنظیم config.yaml برخی آرگومان‌ها را تغییر دهید، مانند


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

لطفاً این دستور را در ترمینال اجرا کنید


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. اجرای آداپتور تنظیم دقیق برای تست**

می‌توانید آداپتور تنظیم دقیق را در ترمینال اجرا کنید، مانند این


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

و مدل اصلی را برای مقایسه نتایج اجرا کنید


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

می‌توانید نتایج تنظیم دقیق را با مدل اصلی مقایسه کنید


## **4. ادغام آداپتورها برای تولید مدل‌های جدید**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. اجرای مدل‌های تنظیم دقیق کم‌حجم با استفاده از ollama**

قبل از استفاده، لطفاً محیط llama.cpp خود را پیکربندی کنید


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. اکنون از تبدیل کوانتیزاسیون fp32، fp16 و INT 8 پشتیبانی می‌کند

2. مدل ادغام شده فاقد tokenizer.model است، لطفاً آن را از https://huggingface.co/microsoft/Phi-3-mini-4k-instruct دانلود کنید

یک [Ollma Model](https://ollama.com/) تنظیم کنید


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

دستور را در ترمینال اجرا کنید


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

تبریک می‌گوییم! استاد تنظیم دقیق با چارچوب MLX شدید

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.