# **ការសម្រួលលម្អិត Phi-3 ជាមួយក្របខ័ណ្ឌ Apple MLX**

យើងអាចបញ្ចប់ការសម្រួលលម្អិតរួមជាមួយ Lora តាមរយៈបន្ទាត់ពាក្យសម្ពាធរបស់ក្របខ័ណ្ឌ Apple MLX។ (បើអ្នកចង់ដឹងបន្ថែមអំពីប្រតិបត្តិការរបស់ក្របខ័ណ្ឌ MLX សូមអាន [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. ការរៀបចំប្រាក់ទិន្នន័យ**

ដោយលំនាំដើម ក្របខ័ណ្ឌ MLX ត្រូវការរូបមន្ត jsonl សម្រាប់ train, test, និង eval ហើយត្រូវបានរួមបញ្ចូលជាមួយ Lora ដើម្បីបញ្ចប់ការងារសម្រួលលម្អិត។


### ***ចំណាំ៖***

1. រូបមន្តទិន្នន័យ jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ឧទាហរណ៍របស់យើងប្រើ [ទិន្នន័យ TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ប៉ុន្តែបរិមាណទិន្នន័យមិនគ្រប់គ្រាន់ទេ ដូច្នេះលទ្ធផលសម្រួលលម្អិតមិនមានការធានាថាត្រូវល្អបំផុត។ គ្រោងអ្នករៀនគួរប្រើទិន្នន័យល្អជាងនេះដោយផ្អែកលើស្ថានភាពផ្ទាល់ខ្លួនដើម្បីបញ្ចប់។  

3. រូបមន្តទិន្នន័យត្រូវបានរួមបញ្ចូលជាមួយទម្រង់ Phi-3

សូមទាញយកទិន្នន័យពី [តំណភ្ជាប់នេះ](../../../../code/04.Finetuning/mlx), សូមរួមបញ្ចូលបណ្ណាល័យ .jsonl ទាំងអស់នៅក្នុងថត ***data***


## **2. ការសម្រួលលម្អិតនៅក្នុង terminal របស់អ្នក**

សូមរត់ពាក្យបញ្ជានេះនៅក្នុង terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***ចំណាំ៖***

1. នេះគឺជាការសម្រួលលម្អិត LoRA, ក្របខ័ណ្ឌ MLX មិនបានផ្សាយ QLoRA ទេ

2. អ្នកអាចកំណត់ config.yaml ដើម្បីផ្លាស់ប្ដូរតំលៃប៉ារ៉ាម៉ែត្រមួយចំនួន ដូចជា


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

សូមរត់ពាក្យបញ្ជានេះនៅក្នុង terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. រត់ Fine-tuning adapter ដើម្បីតេស្ត**

អ្នកអាចរត់ fine-tuning adapter នៅក្នុង terminal ដូច្នេះ 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ហើយរត់ម៉ូឌែលដើមដើម្បីប្រៀបធៀបទោលផល 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

អ្នកអាចសាកល្បងប្រៀបធៀបលទ្ធផលនៃ Fine-tuning ជាមួយម៉ូឌែលដើម


## **4. ការរួមបញ្ចូល adapters ដើម្បីបង្កើតម៉ូឌែលថ្មី**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. រត់ម៉ូឌែលសម្រួលលម្អិតដែលបានបន្លាយពី ollama**

មុនប្រើ សូមកំណត់តម្លៃបរិយាកាស llama.cpp របស់អ្នក


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***ចំណាំ:*** 

1. ឥឡូវគាំទ្រការបម្លែងការបន្លាយ fp32, fp16 និង INT 8

2. ម៉ូឌែលដែលបានរួមបញ្ចូលបាត់ tokenizer.model សូមទាញយកពី https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

កំណត់ [ម៉ូឌែល Ollma](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

រត់ពាក្យបញ្ជានៅក្នុង terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

អបអរគុណ! ជំនាញសម្រួលលម្អិតជាមួយក្របខ័ណ្ឌ MLX បានជោគជ័យ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបកប្រែដោយការប្រើប្រាស់សេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ពេលដែលយើងខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានចំណុចខុសឆ្គងឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាមូលដ្ឋានគួរត្រូវបានចងក្រងជាច្បាប់ច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ យើងណែនាំឱ្យបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនមានភារៈកាតព្វកិច្ចចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសចេញពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->