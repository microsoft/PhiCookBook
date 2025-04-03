<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b1ec18a3db0bb90ba8483eceade60031",
  "translation_date": "2025-04-03T08:17:50+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_MLX.md",
  "language_code": "ur"
}
-->
# **ایپل MLX فریم ورک کے ساتھ Phi-3 کی فائن ٹیوننگ**

ہم ایپل MLX فریم ورک کمانڈ لائن کے ذریعے Lora کے ساتھ فائن ٹیوننگ مکمل کر سکتے ہیں۔ (اگر آپ MLX فریم ورک کے کام کرنے کے بارے میں مزید جاننا چاہتے ہیں، تو براہ کرم [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) پڑھیں۔)

## **1. ڈیٹا کی تیاری**

عام طور پر، MLX فریم ورک ٹرین، ٹیسٹ، اور ایوال کے jsonl فارمیٹ کا مطالبہ کرتا ہے، اور اسے Lora کے ساتھ ملا کر فائن ٹیوننگ کے کام مکمل کیے جا سکتے ہیں۔

### ***نوٹ:***

1. jsonl ڈیٹا فارمیٹ:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ہمارا مثال [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) استعمال کرتا ہے، لیکن ڈیٹا کی مقدار نسبتا کم ہے، اس لیے فائن ٹیوننگ کے نتائج لازمی طور پر بہترین نہیں ہوں گے۔ سیکھنے والوں کو مشورہ دیا جاتا ہے کہ وہ اپنے حالات کے مطابق بہتر ڈیٹا استعمال کریں۔

3. ڈیٹا فارمیٹ Phi-3 ٹیمپلیٹ کے ساتھ ملا ہوا ہے۔

براہ کرم اس [لنک](../../../../code/04.Finetuning/mlx) سے ڈیٹا ڈاؤنلوڈ کریں، اور ***data*** فولڈر میں تمام .jsonl شامل کریں۔

## **2. فائن ٹیوننگ اپنے ٹرمینل میں**

براہ کرم یہ کمانڈ ٹرمینل میں چلائیں۔

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***نوٹ:***

1. یہ LoRA فائن ٹیوننگ ہے، MLX فریم ورک نے QLoRA کو پبلش نہیں کیا ہے۔

2. آپ config.yaml کو سیٹ کر سکتے ہیں تاکہ کچھ دلائل تبدیل کیے جا سکیں، جیسے:

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

براہ کرم یہ کمانڈ ٹرمینل میں چلائیں۔

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. فائن ٹیوننگ اڈاپٹر کو ٹیسٹ کریں**

آپ فائن ٹیوننگ اڈاپٹر کو ٹرمینل میں چلائیں، جیسے:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

اور اصل ماڈل چلائیں تاکہ نتیجہ کا موازنہ کریں۔

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

آپ فائن ٹیوننگ کے نتائج کا اصل ماڈل کے ساتھ موازنہ کرنے کی کوشش کر سکتے ہیں۔

## **4. اڈاپٹرز کو ملا کر نئے ماڈلز بنائیں**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. کوانٹیفائیڈ فائن ٹیوننگ ماڈلز کو Ollama کے ذریعے چلائیں**

استعمال سے پہلے، براہ کرم اپنی llama.cpp انوائرمنٹ کو کنفیگر کریں۔

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***نوٹ:***

1. اب fp32، fp16 اور INT 8 کی کوانٹائزیشن کنورژن کو سپورٹ کیا جاتا ہے۔

2. مرج شدہ ماڈل میں tokenizer.model موجود نہیں ہے، براہ کرم اسے https://huggingface.co/microsoft/Phi-3-mini-4k-instruct سے ڈاؤنلوڈ کریں۔

ایک [Ollma Model](https://ollama.com/) سیٹ کریں۔

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ٹرمینل میں کمانڈ چلائیں۔

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

مبارک ہو! آپ نے MLX فریم ورک کے ساتھ فائن ٹیوننگ کو ماسٹر کر لیا۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا بے ترتیبی ہو سکتی ہے۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔