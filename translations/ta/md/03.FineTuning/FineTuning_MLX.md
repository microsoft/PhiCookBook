<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-10-11T11:50:14+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "ta"
}
-->
# **Phi-3 ஐ Apple MLX Framework மூலம் Fine-tuning செய்வது**

Apple MLX Framework கட்டளைக் கோவை மூலம் Lora உடன் Fine-tuning ஐ முடிக்கலாம். (MLX Framework இன் செயல்பாடுகளைப் பற்றி மேலும் அறிய விரும்பினால், [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) ஐப் படிக்கவும்)

## **1. தரவுகளைத் தயாரித்தல்**

MLX Framework இயல்பாக train, test, மற்றும் eval ஆகியவற்றின் jsonl வடிவத்தை தேவைப்படுத்துகிறது, மேலும் Lora உடன் இணைந்து Fine-tuning பணிகளை முடிக்கிறது.

### ***குறிப்பு:***

1. jsonl தரவுத் வடிவம்:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```


2. எங்கள் எடுத்துக்காட்டில் [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) பயன்படுத்தப்பட்டுள்ளது, ஆனால் தரவின் அளவு போதுமானதாக இல்லை, எனவே Fine-tuning முடிவுகள் அவசியமாக சிறந்ததாக இருக்காது. கற்றலாளர்கள் தங்களின் சொந்த சூழ்நிலைகளின் அடிப்படையில் சிறந்த தரவுகளைப் பயன்படுத்த பரிந்துரைக்கப்படுகிறது.

3. தரவுத் வடிவம் Phi-3 டெம்ப்ளேட்டுடன் இணைக்கப்பட்டுள்ளது.

இந்த [இணைப்பில்](../../../../code/04.Finetuning/mlx) இருந்து தரவுகளைப் பதிவிறக்கவும், ***data*** கோப்புறையில் உள்ள அனைத்து .jsonl கோப்புகளையும் சேர்க்கவும்.

## **2. உங்கள் டெர்மினலில் Fine-tuning செய்யவும்**

இந்தக் கட்டளையை டெர்மினலில் இயக்கவும்:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***குறிப்பு:***

1. இது LoRA Fine-tuning ஆகும், MLX Framework QLoRA ஐ வெளியிடவில்லை.

2. config.yaml ஐ அமைத்து சில arguments-ஐ மாற்றலாம், உதாரணமாக:

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


இந்தக் கட்டளையை டெர்மினலில் இயக்கவும்:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Fine-tuning adapter ஐ சோதிக்க இயக்கவும்**

Fine-tuning adapter ஐ டெர்மினலில் இயக்கலாம், இதுபோல:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```


மற்றும் முதன்மை மாடலை இயக்கி முடிவுகளை ஒப்பிடவும்:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```


Fine-tuning முடிவுகளை முதன்மை மாடலுடன் ஒப்பிட முயற்சிக்கவும்.

## **4. Adapters ஐ இணைத்து புதிய மாடல்களை உருவாக்கவும்**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```


## **5. Ollama ஐப் பயன்படுத்தி quantified fine-tuning மாடல்களை இயக்குதல்**

பயன்படுத்துவதற்கு முன், உங்கள் llama.cpp சூழலை அமைக்கவும்:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```


***குறிப்பு:*** 

1. தற்போது fp32, fp16 மற்றும் INT 8 இன் quantization மாற்றத்தை ஆதரிக்கிறது.

2. இணைக்கப்பட்ட மாடலில் tokenizer.model இல்லை, தயவுசெய்து அதை https://huggingface.co/microsoft/Phi-3-mini-4k-instruct இல் இருந்து பதிவிறக்கவும்.

ஒரு [Ollama Model](https://ollama.com/) அமைக்கவும்.

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```


டெர்மினலில் கட்டளையை இயக்கவும்:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```


வாழ்த்துக்கள்! MLX Framework உடன் Fine-tuning ஐ கற்றுக்கொண்டீர்கள்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாகக் கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.