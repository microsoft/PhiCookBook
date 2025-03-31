<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-03-27T14:58:43+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_MLX.md",
  "language_code": "fa"
}
-->
# **فاین تیون کردن Phi-3 با استفاده از Apple MLX Framework**

ما می‌توانیم فاین تیون کردن ترکیبی با Lora را از طریق خط فرمان Apple MLX Framework انجام دهیم. (اگر می‌خواهید اطلاعات بیشتری درباره عملکرد MLX Framework کسب کنید، لطفاً [Inference Phi-3 با Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) را مطالعه کنید.)

## **۱. آماده‌سازی داده‌ها**

به طور پیش‌فرض، MLX Framework نیاز به فرمت jsonl برای داده‌های train، test، و eval دارد و با Lora ترکیب می‌شود تا فرآیند فاین تیون کردن را کامل کند.

### ***توجه:***

۱. فرمت داده jsonl:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

۲. مثال ما از [داده‌های TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) استفاده می‌کند، اما مقدار داده نسبتاً کم است، بنابراین نتایج فاین تیون کردن لزوماً بهترین نیستند. پیشنهاد می‌شود که یادگیرندگان از داده‌های بهتر بر اساس سناریوهای خود استفاده کنند.

۳. فرمت داده با قالب Phi-3 ترکیب شده است.

لطفاً داده‌ها را از این [لینک](../../../../code/04.Finetuning/mlx) دانلود کنید و تمام فایل‌های .jsonl را در پوشه ***data*** قرار دهید.

## **۲. فاین تیون کردن در ترمینال**

لطفاً این دستور را در ترمینال اجرا کنید:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***توجه:***

۱. این فاین تیون کردن با استفاده از LoRA است؛ MLX Framework هنوز QLoRA را منتشر نکرده است.

۲. شما می‌توانید فایل config.yaml را تنظیم کنید تا برخی آرگومان‌ها را تغییر دهید، مانند:

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

لطفاً این دستور را در ترمینال اجرا کنید:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **۳. اجرای آداپتور فاین تیون برای تست**

شما می‌توانید آداپتور فاین تیون را در ترمینال اجرا کنید، مانند این:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

و مدل اصلی را اجرا کنید تا نتایج را مقایسه کنید:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

شما می‌توانید نتایج فاین تیون را با مدل اصلی مقایسه کنید.

## **۴. ادغام آداپتورها برای تولید مدل‌های جدید**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **۵. اجرای مدل‌های فاین تیون شده با کمیت‌گذاری از طریق ollama**

قبل از استفاده، لطفاً محیط llama.cpp خود را پیکربندی کنید:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***توجه:*** 

۱. اکنون تبدیل کمیت‌گذاری fp32، fp16 و INT 8 پشتیبانی می‌شود.

۲. مدل ادغام‌شده فاقد tokenizer.model است؛ لطفاً آن را از https://huggingface.co/microsoft/Phi-3-mini-4k-instruct دانلود کنید.

یک [مدل Ollama](https://ollama.com/) تنظیم کنید:

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

دستور زیر را در ترمینال اجرا کنید:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

تبریک! شما فاین تیون کردن با MLX Framework را یاد گرفتید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت ترجمه را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.