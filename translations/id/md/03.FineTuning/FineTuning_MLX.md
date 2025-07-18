<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T08:01:49+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "id"
}
-->
# **Fine-tuning Phi-3 dengan Apple MLX Framework**

Kita dapat menyelesaikan Fine-tuning yang dikombinasikan dengan Lora melalui command line Apple MLX framework. (Jika Anda ingin tahu lebih banyak tentang cara kerja MLX Framework, silakan baca [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Persiapan Data**

Secara default, MLX Framework membutuhkan format jsonl untuk train, test, dan eval, dan dikombinasikan dengan Lora untuk menyelesaikan pekerjaan fine-tuning.


### ***Catatan:***

1. Format data jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Contoh kami menggunakan [data TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), namun jumlah datanya relatif kurang, sehingga hasil fine-tuning tidak selalu optimal. Disarankan agar pembelajar menggunakan data yang lebih baik sesuai dengan skenario masing-masing untuk menyelesaikan.

3. Format data dikombinasikan dengan template Phi-3

Silakan unduh data dari [tautan ini](../../../../code/04.Finetuning/mlx), pastikan semua file .jsonl ada di folder ***data***


## **2. Fine-tuning di terminal Anda**

Silakan jalankan perintah ini di terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Catatan:***

1. Ini adalah fine-tuning LoRA, MLX framework belum merilis QLoRA

2. Anda dapat mengatur config.yaml untuk mengubah beberapa argumen, seperti


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

Silakan jalankan perintah ini di terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Jalankan Fine-tuning adapter untuk pengujian**

Anda dapat menjalankan fine-tuning adapter di terminal, seperti ini 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

dan jalankan model asli untuk membandingkan hasilnya 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Anda bisa mencoba membandingkan hasil Fine-tuning dengan model asli


## **4. Gabungkan adapter untuk menghasilkan model baru**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Menjalankan model fine-tuning terkuantisasi menggunakan ollama**

Sebelum digunakan, silakan konfigurasikan lingkungan llama.cpp Anda


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Catatan:*** 

1. Sekarang mendukung konversi kuantisasi fp32, fp16, dan INT 8

2. Model yang digabungkan tidak menyertakan tokenizer.model, silakan unduh dari https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

setel [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

jalankan perintah di terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Selamat! Kuasai fine-tuning dengan MLX Framework

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.