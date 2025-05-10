<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:44:31+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "tl"
}
-->
# **Pag-fine-tune ng Phi-3 gamit ang Apple MLX Framework**

Maaari nating tapusin ang Fine-tuning na pinagsama sa Lora gamit ang Apple MLX framework sa command line. (Kung nais mong malaman pa ang tungkol sa operasyon ng MLX Framework, pakibasa ang [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. Paghahanda ng Data**

Sa default, kailangan ng MLX Framework ang jsonl na format para sa train, test, at eval, at pinagsasama ito sa Lora para matapos ang fine-tuning na trabaho.

### ***Note:***

1. jsonl na format ng data ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Ang halimbawa namin ay gumagamit ng [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), ngunit medyo kulang ang dami ng data, kaya hindi tiyak na pinakamaganda ang resulta ng fine-tuning. Inirerekomenda na gumamit ang mga nag-aaral ng mas magandang data ayon sa kanilang sariling sitwasyon para matapos ito.

3. Ang format ng data ay pinagsama sa Phi-3 template

Pakidownload ang data mula sa [link na ito](../../../../code/04.Finetuning/mlx), isama lahat ng .jsonl sa ***data*** folder

## **2. Fine-tuning sa iyong terminal**

Patakbuhin ang command na ito sa terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Ito ay LoRA fine-tuning, hindi pa nailalabas ng MLX framework ang QLoRA

2. Maaari mong baguhin ang config.yaml para i-adjust ang ilang mga argumento, tulad ng


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

Patakbuhin ang command na ito sa terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Patakbuhin ang Fine-tuning adapter para subukan**

Maaari mong patakbuhin ang fine-tuning adapter sa terminal, ganito 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

at patakbuhin ang orihinal na modelo para ikumpara ang resulta 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Maaari mong subukang ikumpara ang mga resulta ng Fine-tuning at ng orihinal na modelo

## **4. Pagsamahin ang mga adapter para gumawa ng bagong mga modelo**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Pagpapatakbo ng quantified fine-tuning models gamit ang ollama**

Bago gamitin, pakiconfigure ang iyong llama.cpp environment


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Ngayon ay sinusuportahan ang quantization conversion ng fp32, fp16, at INT 8

2. Nawawala ang tokenizer.model sa pinagsamang modelo, pakidownload ito mula sa https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

Mag-set ng [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Patakbuhin ang command sa terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Congrats! Masterin mo na ang fine-tuning gamit ang MLX Framework

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinakapinagkukunan ng katotohanan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.