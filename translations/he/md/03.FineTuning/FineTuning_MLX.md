<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:44:00+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "he"
}
-->
# **כיוונון מדויק של Phi-3 עם מסגרת Apple MLX**

ניתן להשלים כיוונון מדויק בשילוב עם Lora דרך שורת הפקודה של מסגרת Apple MLX. (אם תרצו לדעת יותר על פעולת מסגרת MLX, אנא קראו את [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. הכנת הנתונים**

ברירת המחדל, מסגרת MLX דורשת את פורמט ה-jsonl של train, test ו-eval, ומשולבת עם Lora להשלמת עבודות כיוונון מדויק.

### ***הערה:***

1. פורמט נתוני jsonl：

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. הדוגמה שלנו משתמשת בנתונים של [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), אך כמות הנתונים יחסית לא מספיקה, לכן תוצאות הכיוונון המדויק לא בהכרח הטובות ביותר. מומלץ שלומדים ישתמשו בנתונים טובים יותר בהתאם לתרחישים שלהם להשלמה.

3. פורמט הנתונים משולב עם תבנית Phi-3

אנא הורידו את הנתונים מה[קישור](../../../../code/04.Finetuning/mlx), יש לכלול את כל קבצי ה-.jsonl בתיקיית ***data***

## **2. כיוונון מדויק בטרמינל שלך**

אנא הריצו את הפקודה הזו בטרמינל

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***הערה:***

1. זהו כיוונון מדויק של LoRA, מסגרת MLX לא פרסמה QLoRA

2. ניתן להגדיר בקובץ config.yaml לשנות כמה פרמטרים, כמו

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

אנא הריצו את הפקודה הזו בטרמינל

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. הרצת מתאם כיוונון מדויק לבדיקה**

ניתן להריץ את מתאם הכיוונון המדויק בטרמינל, כך

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ולהריץ את המודל המקורי להשוואת התוצאה

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ניתן לנסות להשוות בין תוצאות הכיוונון המדויק לבין המודל המקורי

## **4. מיזוג מתאמים ליצירת מודלים חדשים**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. הרצת מודלים מכווננים מדויק כמותיים עם ollama**

לפני השימוש, אנא הגדירו את סביבת llama.cpp שלכם

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***הערה:***

1. כעת נתמכת המרה לכימות של fp32, fp16 ו-INT 8

2. המודל הממוזג חסר את tokenizer.model, אנא הורידו אותו מכתובת https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

הגדירו [Ollma Model](https://ollama.com/)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

הריצו את הפקודה בטרמינל

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

כל הכבוד! שלטתם בכיוונון מדויק עם מסגרת MLX

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לכל אי-הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.