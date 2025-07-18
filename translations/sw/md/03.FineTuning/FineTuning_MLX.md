<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T08:02:17+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "sw"
}
-->
# **Kufinywa kwa Phi-3 kwa kutumia Apple MLX Framework**

Tunaweza kumaliza kufinywa kwa pamoja na Lora kupitia mstari wa amri wa Apple MLX framework. (Kama unataka kujifunza zaidi kuhusu jinsi MLX Framework inavyofanya kazi, tafadhali soma [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Maandalizi ya data**

Kwa kawaida, MLX Framework inahitaji data katika muundo wa jsonl kwa ajili ya train, test, na eval, na inachanganywa na Lora kumaliza kazi za kufinywa.


### ***Note:***

1. Muundo wa data jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Mfano wetu unatumia [data ya TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), lakini kiasi cha data ni kidogo, hivyo matokeo ya kufinywa hayahakikishi kuwa bora zaidi. Inapendekezwa wanafunzi watumie data bora kulingana na mazingira yao ili kumaliza kazi.

3. Muundo wa data umeunganishwa na templeti ya Phi-3

Tafadhali pakua data kutoka [kiungo hiki](../../../../code/04.Finetuning/mlx), hakikisha unajumuisha faili zote za .jsonl katika folda ya ***data***


## **2. Kufinywa kwenye terminal yako**

Tafadhali endesha amri hii kwenye terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Hii ni kufinywa kwa LoRA, MLX framework haijatoa QLoRA

2. Unaweza kubadilisha config.yaml kubadilisha baadhi ya hoja, kama vile


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

Tafadhali endesha amri hii kwenye terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Endesha fine-tuning adapter kujaribu**

Unaweza kuendesha fine-tuning adapter kwenye terminal, kama hii 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

na endesha modeli ya asili kulinganisha matokeo 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Unaweza kujaribu kulinganisha matokeo ya Fine-tuning na modeli ya asili


## **4. Unganisha adapters kuunda modeli mpya**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Kuendesha modeli za kufinywa zilizopimwa kwa kutumia ollama**

Kabla ya kutumia, tafadhali sanidi mazingira yako ya llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Sasa inasaidia mabadiliko ya quantization ya fp32, fp16 na INT 8

2. Modeli iliyounganishwa haijajumuisha tokenizer.model, tafadhali pakua kutoka https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

weka [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

endesha amri kwenye terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Hongera! Jifunze kufinywa kwa kina kwa kutumia MLX Framework

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.