# **ضبط دقيق لـ Phi-3 باستخدام إطار عمل Apple MLX**

يمكننا إتمام الضبط الدقيق معًا مع Lora عبر سطر أوامر إطار عمل Apple MLX. (إذا كنت تريد معرفة المزيد عن تشغيل إطار عمل MLX، يرجى قراءة [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. إعداد البيانات**

بشكل افتراضي، يتطلب إطار عمل MLX تنسيق jsonl لملفات train و test و eval، ويُستخدم مع Lora لإكمال مهام الضبط الدقيق.


### ***ملاحظة:***

1. تنسيق بيانات jsonl:


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. يستخدم مثالنا بيانات [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ، ولكن حجم البيانات قليل نسبيًا، لذا قد لا تكون نتائج الضبط الدقيق الأفضل. يُنصح المتعلمين باستخدام بيانات أفضل بناءً على سيناريوهاتهم الخاصة لإكمال العملية.

3. تنسيق البيانات مدمج مع قالب Phi-3

يرجى تنزيل البيانات من هذا [الرابط](../../../../code/04.Finetuning/mlx) يرجى تضمين جميع ملفات .jsonl في مجلد ***data***


## **2. الضبط الدقيق في المحطة الطرفية الخاصة بك**

يرجى تشغيل هذا الأمر في المحطة الطرفية


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***ملاحظة:***

1. هذا ضبط دقيق باستخدام LoRA، إطار عمل MLX لا يدعم QLoRA بعد

2. يمكنك تعديل config.yaml لتغيير بعض المعاملات، مثل


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

يرجى تشغيل هذا الأمر في المحطة الطرفية


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. تشغيل ملحق الضبط الدقيق للاختبار**

يمكنك تشغيل ملحق الضبط الدقيق في المحطة الطرفية، كالتالي


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

وتشغيل النموذج الأصلي للمقارنة بالنتيجة


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

يمكنك محاولة مقارنة نتائج الضبط الدقيق مع النموذج الأصلي


## **4. دمج الملحقات لإنشاء نماذج جديدة**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. تشغيل نماذج الضبط الدقيق المكممة باستخدام ollama**

قبل الاستخدام، يرجى إعداد بيئة llama.cpp الخاصة بك


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***ملاحظة:*** 

1. الآن يدعم تحويل الكم لـ fp32 و fp16 و INT 8

2. النموذج المدمج يفتقد ملف tokenizer.model، يرجى تنزيله من https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

تعيين [نموذج Ollma](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

تشغيل الأمر في المحطة الطرفية


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

تهانينا! لقد أتقنت الضبط الدقيق باستخدام إطار عمل MLX

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->