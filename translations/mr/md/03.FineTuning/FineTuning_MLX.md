# **Apple MLX Framework सह Phi-3 चे फाइन-ट्यूनिंग**

Apple MLX Framework च्या कमांड लाइनद्वारे Lora सह फाइन-ट्यूनिंग पूर्ण करू शकतो. (MLX Framework च्या ऑपरेशनबद्दल अधिक जाणून घेण्यासाठी, कृपया [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) वाचा)


## **1. डेटा तयारी**

डिफॉल्टनुसार, MLX Framework ला train, test, आणि eval चा jsonl फॉरमॅट आवश्यक असतो, आणि Lora सह एकत्रित करून फाइन-ट्यूनिंगचे काम पूर्ण केले जाते.


### ***Note:***

1. jsonl डेटा फॉरमॅट ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. आमच्या उदाहरणात [TruthfulQA चा डेटा](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) वापरला आहे, पण डेटाची मात्रा तुलनेने कमी आहे, त्यामुळे फाइन-ट्यूनिंगचे निकाल नेहमीच सर्वोत्तम असतीलच असे नाही. शिकणाऱ्यांनी त्यांच्या स्वतःच्या परिस्थितीनुसार चांगला डेटा वापरून पूर्ण करणे शिफारसीय आहे.

3. डेटा फॉरमॅट Phi-3 टेम्प्लेटसह एकत्रित आहे

कृपया या [लिंकवरून](../../../../code/04.Finetuning/mlx) डेटा डाउनलोड करा, ***data*** फोल्डरमधील सर्व .jsonl फाइल्स समाविष्ट करा


## **2. तुमच्या टर्मिनलमध्ये फाइन-ट्यूनिंग**

कृपया टर्मिनलमध्ये हा कमांड चालवा


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. हे LoRA फाइन-ट्यूनिंग आहे, MLX Framework ने QLoRA प्रकाशित केलेले नाही

2. तुम्ही config.yaml मध्ये काही आर्ग्युमेंट्स बदलू शकता, जसे की


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

कृपया टर्मिनलमध्ये हा कमांड चालवा


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. फाइन-ट्यूनिंग अडॅप्टर चालवून चाचणी करा**

तुम्ही टर्मिनलमध्ये फाइन-ट्यूनिंग अडॅप्टर असे चालवू शकता


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

आणि मूळ मॉडेल चालवून निकालांची तुलना करा


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

फाइन-ट्यूनिंग आणि मूळ मॉडेलचे निकाल तुलना करण्याचा प्रयत्न करा


## **4. अडॅप्टर्स मर्ज करून नवीन मॉडेल तयार करा**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama वापरून क्वांटिफाइड फाइन-ट्यूनिंग मॉडेल चालवणे**

वापरण्यापूर्वी, कृपया तुमचे llama.cpp पर्यावरण कॉन्फिगर करा


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. आता fp32, fp16 आणि INT 8 च्या क्वांटायझेशन रूपांतरणाला समर्थन आहे

2. मर्ज केलेल्या मॉडेलमध्ये tokenizer.model नाही, कृपया ते https://huggingface.co/microsoft/Phi-3-mini-4k-instruct वरून डाउनलोड करा

[Ollma Model](https://ollama.com/) सेट करा


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

टर्मिनलमध्ये कमांड चालवा


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

अभिनंदन! MLX Framework सह फाइन-ट्यूनिंगमध्ये पारंगत व्हा

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.