<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:43:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "th"
}
-->
# **การปรับแต่ง Phi-3 ด้วย Apple MLX Framework**

เราสามารถทำการปรับแต่ง Fine-tuning ร่วมกับ Lora ผ่านคำสั่งใน Apple MLX Framework ได้ (ถ้าต้องการทราบรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน MLX Framework กรุณาอ่าน [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. การเตรียมข้อมูล**

โดยค่าเริ่มต้น MLX Framework ต้องการข้อมูลในรูปแบบ jsonl สำหรับ train, test และ eval และจะนำมารวมกับ Lora เพื่อทำงาน fine-tuning ให้เสร็จสมบูรณ์

### ***Note:***

1. รูปแบบข้อมูล jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ตัวอย่างของเราใช้ข้อมูลจาก [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) แต่ปริมาณข้อมูลยังไม่เพียงพอ จึงทำให้ผลลัพธ์จากการ fine-tuning อาจไม่ดีที่สุด แนะนำให้ผู้เรียนใช้ข้อมูลที่เหมาะสมกับสถานการณ์ของตัวเองเพื่อให้ได้ผลลัพธ์ที่ดีกว่า

3. รูปแบบข้อมูลจะรวมกับเทมเพลตของ Phi-3

กรุณาดาวน์โหลดข้อมูลจากลิงก์นี้ [link](../../../../code/04.Finetuning/mlx) โดยให้รวมไฟล์ .jsonl ทั้งหมดในโฟลเดอร์ ***data***


## **2. การ Fine-tuning ผ่าน terminal ของคุณ**

โปรดรันคำสั่งนี้ใน terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. นี่คือการ fine-tuning แบบ LoRA โดย MLX framework ยังไม่ได้ปล่อย QLoRA

2. คุณสามารถตั้งค่า config.yaml เพื่อเปลี่ยนแปลงอาร์กิวเมนต์บางส่วน เช่น


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

โปรดรันคำสั่งนี้ใน terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. รัน Fine-tuning adapter เพื่อทดสอบ**

คุณสามารถรัน fine-tuning adapter ใน terminal ได้แบบนี้


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

และรันโมเดลต้นฉบับเพื่อเปรียบเทียบผลลัพธ์


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

คุณสามารถลองเปรียบเทียบผลลัพธ์ของ Fine-tuning กับโมเดลต้นฉบับได้


## **4. รวม adapters เพื่อสร้างโมเดลใหม่**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. การรันโมเดล fine-tuning ที่ถูก quantized ด้วย ollama**

ก่อนใช้งาน กรุณาตั้งค่าสภาพแวดล้อม llama.cpp ของคุณให้เรียบร้อย


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. ตอนนี้รองรับการแปลง quantization สำหรับ fp32, fp16 และ INT 8

2. โมเดลที่รวมแล้วจะไม่มี tokenizer.model กรุณาดาวน์โหลดจาก https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

ตั้งค่า [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

รันคำสั่งใน terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

ยินดีด้วย! คุณชำนาญการ fine-tuning ด้วย MLX Framework แล้ว

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลฉบับนี้