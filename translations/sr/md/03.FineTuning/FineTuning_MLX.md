<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T08:03:21+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "sr"
}
-->
# **Фајн-тунинг Phi-3 уз Apple MLX Framework**

Фајн-тунинг у комбинацији са Lora можемо извршити преко командне линије Apple MLX Framework-а. (Ако желите да сазнате више о раду MLX Framework-а, молимо прочитајте [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. Припрема података**

Подразумевано, MLX Framework захтева jsonl формат за train, test и eval, и користи се у комбинацији са Lora за извршење фајн-тунинг задатака.

### ***Note:***

1. jsonl формат података ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. У нашем примеру користимо [TruthfulQA податке](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), али количина података је релативно мала, па резултати фајн-тунинга не морају бити најбољи. Препоручује се да корисници користе боље податке прилагођене својим сценаријима.

3. Формат података је усклађен са Phi-3 шаблоном

Молимо преузмите податке са овог [линка](../../../../code/04.Finetuning/mlx), укључујући све .jsonl фајлове у ***data*** фолдеру

## **2. Фајн-тунинг у вашем терминалу**

Покрените ову команду у терминалу


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Ово је LoRA фајн-тунинг, MLX framework није објавио QLoRA

2. Можете подесити config.yaml да промените неке параметре, као што су


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

Покрените ову команду у терминалу


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Покретање фајн-тунинг адаптера за тестирање**

Фајн-тунинг адаптер можете покренути у терминалу, овако


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

и покрените оригинални модел за поређење резултата


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Можете упоредити резултате фајн-тунинга са оригиналним моделом

## **4. Споји адаптере да бисте генерисали нове моделе**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Покретање квантованих фајн-тунинг модела уз помоћ ollama**

Пре коришћења, молимо конфигуришите ваше llama.cpp окружење


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Сада је подржана квантизација конверзије fp32, fp16 и INT 8

2. Спојени модел нема tokenizer.model, молимо преузмите га са https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

подесите [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

покрените команду у терминалу


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Честитамо! Савладали сте фајн-тунинг уз MLX Framework

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.