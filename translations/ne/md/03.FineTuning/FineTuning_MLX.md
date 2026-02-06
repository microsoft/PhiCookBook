# **Apple MLX Framework सँग Phi-3 को Fine-tuning**

हामी Apple MLX framework को कमाण्ड लाइन मार्फत Lora सँग मिलाएर Fine-tuning पूरा गर्न सक्छौं। (यदि तपाईं MLX Framework को सञ्चालनबारे थप जान्न चाहनुहुन्छ भने, कृपया [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) पढ्नुहोस्)


## **1. डाटा तयारी**

डिफल्ट रूपमा, MLX Framework ले train, test, र eval को jsonl फर्म्याट आवश्यक पर्छ, र Lora सँग मिलाएर fine-tuning काम पूरा गर्छ।


### ***Note:***

1. jsonl डाटा फर्म्याट ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. हाम्रो उदाहरणमा [TruthfulQA को डाटा](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) प्रयोग गरिएको छ, तर डाटाको मात्रा तुलनात्मक रूपमा कम छ, त्यसैले fine-tuning को नतिजा सधैं उत्कृष्ट नहुन सक्छ। सिक्नेहरूले आफ्ना परिदृश्यहरूमा आधारित राम्रो डाटा प्रयोग गर्न सिफारिस गरिन्छ।

3. डाटा फर्म्याट Phi-3 टेम्प्लेटसँग मिलाइएको छ

कृपया यो [लिंक](../../../../code/04.Finetuning/mlx) बाट डाटा डाउनलोड गर्नुहोस्, ***data*** फोल्डरमा सबै .jsonl समावेश गर्नुहोस्


## **2. तपाईँको टर्मिनलमा Fine-tuning**

कृपया टर्मिनलमा यो कमाण्ड चलाउनुहोस्


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. यो LoRA fine-tuning हो, MLX framework ले QLoRA प्रकाशित गरेको छैन

2. तपाईं config.yaml मा केही आर्गुमेन्टहरू परिवर्तन गर्न सक्नुहुन्छ, जस्तै


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

कृपया टर्मिनलमा यो कमाण्ड चलाउनुहोस्


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Fine-tuning adapter चलाएर परीक्षण गर्नुहोस्**

तपाईं टर्मिनलमा fine-tuning adapter यसरी चलाउन सक्नुहुन्छ 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

र मूल मोडेल चलाएर नतिजा तुलना गर्नुहोस् 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

तपाईं Fine-tuning को नतिजा र मूल मोडेलको नतिजा तुलना गर्न प्रयास गर्न सक्नुहुन्छ


## **4. नयाँ मोडेल बनाउन adapters मर्ज गर्नुहोस्**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama प्रयोग गरेर quantified fine-tuning मोडेल चलाउने**

प्रयोग गर्नु अघि, कृपया आफ्नो llama.cpp वातावरण कन्फिगर गर्नुहोस्


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. अहिले fp32, fp16 र INT 8 को quantization रूपान्तरण समर्थन गरिएको छ

2. मर्ज गरिएको मोडेलमा tokenizer.model हराइरहेको छ, कृपया यसलाई https://huggingface.co/microsoft/Phi-3-mini-4k-instruct बाट डाउनलोड गर्नुहोस्

[Ollma Model](https://ollama.com/) सेट गर्नुहोस्


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

टर्मिनलमा कमाण्ड चलाउनुहोस्


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

बधाई छ! MLX Framework सँग fine-tuning मा दक्ष हुनुहोस्

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।