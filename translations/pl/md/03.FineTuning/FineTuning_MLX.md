<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:42:47+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "pl"
}
-->
# **Dostrajanie Phi-3 za pomocą Apple MLX Framework**

Możemy wykonać dostrajanie połączone z Lora za pomocą wiersza poleceń Apple MLX Framework. (Jeśli chcesz dowiedzieć się więcej o działaniu MLX Framework, przeczytaj [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Przygotowanie danych**

Domyślnie MLX Framework wymaga formatu jsonl dla train, test i eval, i jest połączony z Lora, aby ukończyć zadania dostrajania.


### ***Note:***

1. format danych jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Nasz przykład wykorzystuje [dane TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), jednak ilość danych jest stosunkowo niewielka, więc wyniki dostrajania nie muszą być najlepsze. Zalecamy, aby użytkownicy korzystali z lepszych danych dopasowanych do swoich scenariuszy.

3. Format danych jest zgodny z szablonem Phi-3

Proszę pobrać dane z tego [linku](../../../../code/04.Finetuning/mlx), uwzględniając wszystkie pliki .jsonl w folderze ***data***


## **2. Dostrajanie w terminalu**

Proszę uruchomić to polecenie w terminalu


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. To jest dostrajanie LoRA, MLX Framework nie opublikował QLoRA

2. Możesz zmienić niektóre argumenty w config.yaml, na przykład


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

Proszę uruchomić to polecenie w terminalu


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Uruchom adapter dostrajania, aby przetestować**

Możesz uruchomić adapter dostrajania w terminalu, tak jak poniżej


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

i uruchomić oryginalny model, aby porównać wyniki


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Możesz spróbować porównać wyniki dostrajania z oryginalnym modelem


## **4. Scal adaptery, aby wygenerować nowe modele**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Uruchamianie skwantowanych modeli dostrajania za pomocą ollama**

Przed użyciem skonfiguruj swoje środowisko llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Obecnie obsługiwane są konwersje kwantyzacji fp32, fp16 i INT8

2. Połączony model nie zawiera tokenizer.model, pobierz go z https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

ustaw [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

uruchom polecenie w terminalu


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Gratulacje! Opanowałeś dostrajanie z MLX Framework

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym należy uważać za wiarygodne źródło informacji. W przypadku istotnych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.