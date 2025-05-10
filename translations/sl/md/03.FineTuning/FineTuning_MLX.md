<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:45:43+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "sl"
}
-->
# **Fine-tuning Phi-3 s Apple MLX Framework**

Lahko izvedemo fine-tuning v kombinaciji z Lora preko ukazne vrstice Apple MLX frameworka. (Če želite izvedeti več o delovanju MLX Frameworka, prosim preberite [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. Priprava podatkov**

Privzeto MLX Framework zahteva jsonl format za train, test in eval, ter se kombinira z Loro za izvedbo fine-tuninga.

### ***Note:***

1. jsonl format podatkov：

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Naš primer uporablja [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), vendar je količina podatkov relativno majhna, zato rezultati fine-tuninga niso nujno najboljši. Priporočamo, da uporabniki uporabijo boljše podatke, prilagojene svojim scenarijem.

3. Format podatkov je skladen s Phi-3 predlogo

Prosimo, prenesite podatke s te [povezave](../../../../code/04.Finetuning/mlx), vključite vse .jsonl datoteke v ***data*** mapi

## **2. Fine-tuning v terminalu**

Zaženite ta ukaz v terminalu

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Note:***

1. To je LoRA fine-tuning, MLX framework ni objavil QLoRA

2. Lahko nastavite config.yaml za spremembo nekaterih argumentov, na primer

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

Zaženite ta ukaz v terminalu

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Zaženite fine-tuning adapter za testiranje**

Fine-tuning adapter lahko zaženete v terminalu, na primer tako

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

in zaženite originalni model za primerjavo rezultatov

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Lahko poskusite primerjati rezultate fine-tuninga z originalnim modelom

## **4. Združevanje adapterjev za generiranje novih modelov**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Zagon kvantificiranih fine-tuning modelov z ollama**

Pred uporabo nastavite vaše llama.cpp okolje

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:***

1. Sedaj podpira kvantizacijo fp32, fp16 in INT 8

2. Združeni model nima tokenizer.model, prosim prenesite ga s https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

nastavite [Ollma Model](https://ollama.com/)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Zaženite ukaz v terminalu

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Čestitke! Obvladajte fine-tuning z MLX Frameworkom

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za kakršnekoli nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.