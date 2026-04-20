# **ការត្រួតពិនិត្យលំអិត Phi-3 ជាមួយ Framework Apple MLX**

យើងអាចបញ្ចប់ការត្រួតពិនិត្យលំអិតរួមជាមួយ Lora តាមរយៈបញ្ជា Command line របស់ Framework Apple MLX។ (បើអ្នកចង់ដឹងបន្ថែមអំពីអំពើនៃ Framework MLX សូមអាន [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. ការរៀបចំទិន្នន័យ**

ដោយលំនាំដើម Framework MLX ត្រូវការរូបមន្ត jsonl សម្រាប់ train, test និង eval ហើយត្រូវបានបង្កប់ជាមួយ Lora ដើម្បីបញ្ចប់ការងារត្រួតពិនិត្យលំអិត។


### ***សម្គាល់៖***

1. រូបមន្តទិន្នន័យ jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ឧទាហរណ៍របស់យើងប្រើ [ទិន្នន័យ TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) , ប៉ុន្តែទិន្នន័យមិនគ្រប់គ្រាន់គេហើយនោះនាំឲ្យលទ្ធផលត្រួតពិនិត្យលំអិត មិនចាំបាច់ល្អបំផុត។ មានការផ្តល់អនុសាសន៍ឲ្យអ្នករៀនប្រើទិន្នន័យល្អប្រសើរជាដើមនៅលើស្ថានភាពផ្ទាល់ខ្លួនរបស់ពួកគេដើម្បីបញ្ចប់។

3. រូបមន្តទិន្នន័យត្រូវបានបង្កប់ជាមួយពុម្ព Phi-3

សូមទាញយកទិន្នន័យពីតំណរនេះ [link](../../../../code/04.Finetuning/mlx), សូមរួមបញ្ចូល .jsonl ទាំងអស់នៅក្នុងថត ***data***


## **2. ការត្រួតពិនិត្យលំអិតនៅក្នុង terminal របស់អ្នក**

សូមរត់បញ្ជានេះនៅក្នុង terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***សម្គាល់:***

1. នេះជាការត្រួតពិនិត្យលំអិត LoRA, Framework MLX មិនបានបោះពុម្ពផ្សាយ QLoRA ទេ

2. អ្នកអាចកំណត់ config.yaml ដើម្បីផ្លាស់ប្តូរការផ្សេងៗមួយចំនួន ដូចជា


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

សូមរត់បញ្ជានេះនៅក្នុង terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. រត់ Fine-tuning adapter ដើម្បីប្រើសាកល្បង**

អ្នកអាចរត់ fine-tuning adapter ក្នុង terminal ដូចខាងក្រោម


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ហើយរត់ម៉ូដែលដើមដើម្បីប្រៀបធៀបលទ្ធផល 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

អ្នកអាចព្យាយាមប្រៀបធៀបលទ្ធផលនៃ Fine-tuning ជាមួយម៉ូដែលដើម


## **4. ប្រមូលផ្តុំ adapters ដើម្បីបង្កើតម៉ូដែលថ្មី**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ដំណើរការ ម៉ូដែល fine-tuning ដែលបានវាស់កម្រិតដោយរបៀប ollama**

មុនប្រើ សូមកំណត់បរិយាកាស llama.cpp របស់អ្នកជាមុន


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***សម្គាល់៖*** 

1. ឥឡូវគាំទ្រការបំលែងវាស់កម្រិត fp32, fp16 និង INT 8

2. ម៉ូដែលដែលបានរួមបញ្ចូលគឺខ្វះ tokenizer.model, សូមទាញយកពី https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

កំណត់ [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

រត់បញ្ជានៅក្នុង terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

សូមអបអរសាទរ! អ្នកជាជំនាញក្នុងការត្រួតពិនិត្យលំអិតជាមួយ Framework MLX

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំធ្វើឱ្យបានត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬការមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទំនើប គួរត្រូវបានចាត់ទុកជាផ្លូវការជាចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរតែប្រើការបកប្រែដោយមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុស ដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->