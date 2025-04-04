<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b1ec18a3db0bb90ba8483eceade60031",
  "translation_date": "2025-04-04T13:25:11+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_MLX.md",
  "language_code": "mo"
}
-->
# **Phi-3-ийг Apple MLX Framework ашиглан нарийвчлан тохируулах**

Apple MLX Framework-ийн командын мөрийг ашиглан LoRA-тай хослуулан нарийвчлан тохируулах ажлыг гүйцэтгэж болно. (Хэрэв та MLX Framework-ийн ажиллагааны талаар илүү ихийг мэдэхийг хүсвэл [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)-г уншина уу.)


## **1. Өгөгдөл бэлтгэх**

Анхдагч байдлаар, MLX Framework нь сургалт, шалгалт, үнэлгээний jsonl форматыг шаарддаг бөгөөд LoRA-тай хослуулан нарийвчлан тохируулах ажлыг гүйцэтгэдэг.


### ***Тэмдэглэл:***

1. jsonl өгөгдлийн формат :


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Бидний жишээнд [TruthfulQA-гийн өгөгдөл](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)-ийг ашигласан, гэхдээ өгөгдлийн хэмжээ харьцангуй бага тул нарийвчлалын үр дүн заавал хамгийн сайн байх албагүй. Суралцагчид өөрсдийн нөхцөл байдалд тохируулан илүү сайн өгөгдөл ашиглахыг зөвлөж байна.

3. Өгөгдлийн формат нь Phi-3 загварын загвартай хослуулсан

Энэ [холбоосоос](../../../../code/04.Finetuning/mlx) өгөгдлийг татаж авна уу, ***data*** хавтсанд байгаа бүх .jsonl файлуудыг оруулна уу.


## **2. Терминал дээр нарийвчлан тохируулах**

Терминал дээр дараах командыг ажиллуулна уу


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Тэмдэглэл:***

1. Энэ бол LoRA нарийвчлал, MLX Framework нь QLoRA-г гаргаагүй

2. config.yaml файлыг ашиглан зарим параметрүүдийг өөрчлөх боломжтой, жишээ нь:


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

Терминал дээр дараах командыг ажиллуулна уу


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Нарийвчилсан тохиргооны адаптерийг турших**

Терминал дээр нарийвчилсан тохиргооны адаптерийг дараах байдлаар ажиллуулна уу


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

дараа нь эх загварыг ажиллуулж үр дүнг харьцуулна уу


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Нарийвчилсан тохиргооны үр дүнг эх загвартай харьцуулахыг оролдож үзээрэй


## **4. Адаптеруудыг нэгтгэж шинэ загвар үүсгэх**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ollama ашиглан тоон нарийвчилсан загварыг ажиллуулах**

Хэрэглэхийн өмнө llama.cpp орчныг тохируулна уу


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Тэмдэглэл:*** 

1. Одоо fp32, fp16 болон INT 8-ийн тоон хувиргалтыг дэмжиж байна

2. Нэгтгэсэн загвар нь tokenizer.model байхгүй, үүнийг дараах хаягаас татаж авна уу: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

[Ollama загвар](https://ollama.com/)-ыг тохируулна уу


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Терминал дээр дараах командыг ажиллуулна уу


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Баяр хүргэе! MLX Framework-ийг ашиглан нарийвчлан тохируулах аргыг эзэмшлээ

It seems like you are requesting a translation into "mo." Could you clarify what "mo" refers to? Are you referring to a specific language or dialect? Examples include Maori, Montenegrin, or something else entirely. Please provide more context so I can assist you accurately!