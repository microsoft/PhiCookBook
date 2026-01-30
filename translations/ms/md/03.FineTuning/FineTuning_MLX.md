# **Penalaan Halus Phi-3 dengan Rangka Kerja Apple MLX**

Kita boleh menyelesaikan Penalaan Halus yang digabungkan dengan Lora melalui baris arahan rangka kerja Apple MLX. (Jika anda ingin mengetahui lebih lanjut tentang operasi Rangka Kerja MLX, sila baca [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Penyediaan Data**

Secara lalai, Rangka Kerja MLX memerlukan format jsonl untuk train, test, dan eval, dan digabungkan dengan Lora untuk menyelesaikan tugasan penalaan halus.


### ***Nota:***

1. format data jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Contoh kami menggunakan [data TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), tetapi jumlah data agak terhad, jadi hasil penalaan halus tidak semestinya terbaik. Disarankan agar pelajar menggunakan data yang lebih baik berdasarkan senario mereka sendiri untuk melengkapkan tugasan.

3. Format data digabungkan dengan templat Phi-3

Sila muat turun data dari [pautan ini](../../../../code/04.Finetuning/mlx), pastikan semua fail .jsonl dalam folder ***data*** disertakan


## **2. Penalaan Halus di terminal anda**

Sila jalankan arahan ini di terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Nota:***

1. Ini adalah penalaan halus LoRA, rangka kerja MLX tidak menerbitkan QLoRA

2. Anda boleh tetapkan config.yaml untuk mengubah beberapa argumen, seperti


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

Sila jalankan arahan ini di terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Jalankan penalaan halus adapter untuk ujian**

Anda boleh jalankan penalaan halus adapter di terminal, seperti ini 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

dan jalankan model asal untuk bandingkan keputusan 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Anda boleh cuba bandingkan keputusan Penalaan Halus dengan model asal


## **4. Gabungkan adapter untuk hasilkan model baru**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Menjalankan model penalaan halus berkuantiti menggunakan ollama**

Sebelum digunakan, sila konfigurasikan persekitaran llama.cpp anda


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Nota:*** 

1. Kini menyokong penukaran kuantisasi fp32, fp16 dan INT 8

2. Model gabungan tidak mempunyai tokenizer.model, sila muat turun dari https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

tetapkan [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

jalankan arahan di terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Tahniah! Kuasai penalaan halus dengan Rangka Kerja MLX

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.