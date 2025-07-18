<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T08:03:10+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "bg"
}
-->
# **Фина настройка на Phi-3 с Apple MLX Framework**

Можем да извършим фина настройка в комбинация с Lora чрез командния ред на Apple MLX Framework. (Ако искате да научите повече за работата на MLX Framework, моля прочетете [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Подготовка на данните**

По подразбиране MLX Framework изисква jsonl формат за train, test и eval, и се комбинира с Lora за завършване на задачите за фина настройка.


### ***Забележка:***

1. jsonl формат на данните ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Нашият пример използва [данни от TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), но количеството данни е сравнително малко, затова резултатите от фина настройка не са непременно най-добрите. Препоръчва се обучаващите се да използват по-добри данни, съобразени със собствените им сценарии.

3. Форматът на данните е съвместим с шаблона на Phi-3

Моля, изтеглете данните от този [линк](../../../../code/04.Finetuning/mlx), включително всички .jsonl файлове в папката ***data***


## **2. Фина настройка в терминала**

Моля, изпълнете тази команда в терминала


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Забележка:***

1. Това е LoRA фина настройка, MLX framework не е публикувал QLoRA

2. Можете да промените някои аргументи в config.yaml, например


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

Моля, изпълнете тази команда в терминала


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Стартиране на адаптер за фина настройка за тест**

Можете да стартирате адаптера за фина настройка в терминала, както следва 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

и да стартирате оригиналния модел за сравнение на резултатите 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Можете да опитате да сравните резултатите от фина настройка с оригиналния модел


## **4. Сливане на адаптери за генериране на нови модели**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Стартиране на квантифицирани модели за фина настройка с ollama**

Преди употреба, моля конфигурирайте вашата llama.cpp среда


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Забележка:*** 

1. В момента се поддържа конверсия на квантизация за fp32, fp16 и INT 8

2. Слятият модел няма tokenizer.model, моля изтеглете го от https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

настройте [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

изпълнете командата в терминала


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Поздравления! Владеете фина настройка с MLX Framework

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.