<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-03-27T14:57:42+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_MLX.md",
  "language_code": "ar"
}
-->
# **تخصيص Phi-3 باستخدام إطار عمل Apple MLX**

يمكننا إكمال التخصيص بالتكامل مع Lora عبر سطر أوامر إطار عمل Apple MLX. (إذا كنت تريد معرفة المزيد عن تشغيل إطار عمل MLX، يرجى قراءة [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. إعداد البيانات**

يتطلب إطار عمل MLX بشكل افتراضي تنسيق jsonl لبيانات التدريب والاختبار والتقييم، ويتم دمجها مع Lora لإكمال مهام التخصيص.

### ***ملاحظة:***

1. تنسيق بيانات jsonl :

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. مثالنا يستخدم [بيانات TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)، ولكن كمية البيانات غير كافية نسبيًا، لذلك قد لا تكون نتائج التخصيص هي الأفضل. يُوصى بأن يستخدم المتعلمون بيانات أفضل بناءً على السيناريوهات الخاصة بهم.

3. يتم دمج تنسيق البيانات مع قالب Phi-3.

يرجى تنزيل البيانات من هذا [الرابط](../../../../code/04.Finetuning/mlx)، يرجى تضمين جميع ملفات .jsonl في مجلد ***data***.

## **2. التخصيص عبر الطرفية**

يرجى تشغيل هذا الأمر في الطرفية:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***ملاحظة:***

1. هذا تخصيص باستخدام LoRA، إطار MLX لم ينشر QLoRA بعد.

2. يمكنك تعديل ملف config.yaml لتغيير بعض الوسائط، مثل:

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

يرجى تشغيل هذا الأمر في الطرفية:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. تشغيل محول التخصيص للاختبار**

يمكنك تشغيل محول التخصيص في الطرفية كما يلي:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ثم تشغيل النموذج الأصلي للمقارنة:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

يمكنك محاولة مقارنة نتائج التخصيص مع النموذج الأصلي.

## **4. دمج المحولات لإنشاء نماذج جديدة**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. تشغيل نماذج التخصيص المحسّنة باستخدام Ollama**

قبل الاستخدام، يرجى تكوين بيئة llama.cpp الخاصة بك:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***ملاحظة:*** 

1. يدعم الآن تحويل الكمية لـ fp32، fp16 وINT 8.

2. النموذج المدمج يفتقد tokenizer.model، يرجى تنزيله من https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

قم بإعداد [نموذج Ollama](https://ollama.com/):

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

قم بتشغيل الأمر في الطرفية:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

تهانينا! لقد أتقنت التخصيص باستخدام إطار عمل MLX.

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى جاهدين لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.