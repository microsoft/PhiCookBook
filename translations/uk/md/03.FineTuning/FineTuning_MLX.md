<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T08:04:07+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "uk"
}
-->
# **Тонке налаштування Phi-3 за допомогою Apple MLX Framework**

Ми можемо виконати тонке налаштування у поєднанні з Lora через командний рядок Apple MLX Framework. (Якщо ви хочете дізнатися більше про роботу MLX Framework, будь ласка, прочитайте [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Підготовка даних**

За замовчуванням MLX Framework вимагає формат jsonl для train, test та eval, і використовується разом з Lora для виконання завдань тонкого налаштування.


### ***Примітка:***

1. Формат даних jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. У нашому прикладі використовується [дані TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), але обсяг даних відносно невеликий, тому результати тонкого налаштування можуть бути не найкращими. Рекомендується використовувати кращі дані, виходячи зі своїх сценаріїв.

3. Формат даних поєднується з шаблоном Phi-3

Будь ласка, завантажте дані за цим [посиланням](../../../../code/04.Finetuning/mlx), включаючи всі .jsonl файли у папці ***data***


## **2. Тонке налаштування у вашому терміналі**

Будь ласка, виконайте цю команду у терміналі


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Примітка:***

1. Це тонке налаштування LoRA, MLX Framework не публікує QLoRA

2. Ви можете змінити деякі параметри у config.yaml, наприклад


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

Будь ласка, виконайте цю команду у терміналі


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Запуск адаптера тонкого налаштування для тестування**

Ви можете запустити адаптер тонкого налаштування у терміналі, ось так 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

та запустити оригінальну модель для порівняння результатів 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Ви можете спробувати порівняти результати тонкого налаштування з оригінальною моделлю


## **4. Об’єднання адаптерів для створення нових моделей**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Запуск кількісно оптимізованих моделей тонкого налаштування за допомогою ollama**

Перед використанням, будь ласка, налаштуйте ваше середовище llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Примітка:*** 

1. Зараз підтримується конвертація квантованих моделей fp32, fp16 та INT 8

2. У об’єднаній моделі відсутній tokenizer.model, будь ласка, завантажте його з https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

налаштуйте [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

виконайте команду у терміналі


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Вітаємо! Ви опанували тонке налаштування з MLX Framework

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.