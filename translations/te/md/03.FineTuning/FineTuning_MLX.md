<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-12-21T18:51:34+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "te"
}
-->
# **Apple MLX ఫ్రేమ్‌వర్క్‌తో Phi-3 ఫైన్-ట్యూనింగ్**

మేము Apple MLX ఫ్రేమ్‌వర్క్ కమాండ్ లైన్ ద్వారా Lora తో కలిపిన ఫైన్-ట్యూనింగ్‌ను పూర్తి చేయవచ్చు. (MLX ఫ్రేమ్‌వర్క్ యొక్క ఆపరేషన్ గురించి మరింత తెలుసుకోవాలంటే, దయచేసి [Apple MLX ఫ్రేమ్‌వర్క్‌తో Phi-3 ఇన్ఫరన్స్](../03.FineTuning/03.Inference/MLX_Inference.md) చదవండి)


## **1. డేటా సిద్ధం**

డిఫాల్ట్‌గా, MLX ఫ్రేమ్‌వర్క్ ట్రైన్, టెస్ట్ మరియు ఇవాల్ కోసం jsonl ఫార్మాట్‌ను అవసరం పడుతుంది, మరియు ఫైన్-ట్యూనింగ్ పనులను పూర్తి చేయడానికి ఇది Lora తో మిళితం అవుతుంది.


### ***గమనిక:***

1. jsonl డేటా ఫార్మాట్ ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. మా ఉదాహరణలో [TruthfulQA డేటా](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ఉపయోగించబడింది , కానీ డేటా పరిమాణం సాపేక్షంగా తక్కువగా ఉండటం వల్ల ఫైన్-ట్యూనింగ్ ఫలితాలు తప్పనిసరిగా ఉత్తమంగా ఉండకపోవచ్చు. అభ్యర్థులకు వారి స్వంత సన్నివేశాల ఆధారంగా మెరుగైన డేటాను ఉపయోగించి పూర్తి చేయాలని సూచించబడుతుంది.

3. డేటా ఫార్మాట్ Phi-3 టెంప్లేట్‌తో కలిపి ఉంటుంది

దయచేసి ఈ [లింక్](../../../../code/04.Finetuning/mlx) నుండి డేటా డౌన్లోడ్ చేయండి, దయచేసి అన్ని .jsonl ఫైల్స్‌ను ***data*** ఫోల్డర్‌లో చేర్చండి


## **2. మీ టెర్మినల్‌లో ఫైన్-ట్యూనింగ్**

దయచేసి ఈ కమాండ్‌ను టెర్మినల్‌లో నడపండి


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***గమనిక:***

1. ఇది LoRA ఫైన్-ట్యూనింగ్, MLX ఫ్రేమ్‌వర్క్ ఇంకా QLoRAని ప్రచురించలేదు

2. మీరు config.yaml సెట్ చేయడం ద్వారా కొన్ని ఆర్గ్యుమెంట్లను మార్చవచ్చు, ఉదాహరణకి


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

దయచేసి ఈ కమాండ్‌ను టెర్మినల్‌లో నడపండి


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. ఫైన్-ట్యూనింగ్ అడాప్టర్‌ను పరీక్షించడానికి నడిపించండి**

మీరు టెర్మినల్‌లో ఫైన్-ట్యూనింగ్ అడాప్టర్‌ను ఇలా నడిపించవచ్చు


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

మరియు ఫలితాలను పోల్చడానికి ఒరిజినల్ మోడల్‌ను నడిపించండి


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

మీరు ఫైన్-ట్యూనింగ్ ఫలితాలను ఒరిజినల్ మోడల్‌తో పోల్చి చూడవచ్చు


## **4. అడాప్టర్లను విలీనం చేసి కొత్త మోడల్స్ తయారు చేయండి**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama ఉపయోగించి క్వాంటైజ్డ్ ఫైన్-ట్యూనింగ్ మోడల్స్ నడపడం**

ఉపయోగించడానికి ముందు, దయచేసి మీ llama.cpp పరిసరాన్ని కాన్ఫిగర్ చేయండి


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***గమనిక:*** 

1. ఇప్పుడు fp32, fp16 మరియు INT 8 యొక్క క్వాంటైజేషన్ మార్పిడిని మద్దతు ఇవ్వబడుతుంది

2. విలీనం చేయబడిన మోడల్‌లో tokenizer.model లేదు, దయచేసి దానిని https://huggingface.co/microsoft/Phi-3-mini-4k-instruct నుండి డౌన్లోడ్ చేయండి

ఒక [Ollama మోడల్](https://ollama.com/) సెట్ చేయండి


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

టెర్మినల్‌లో కమాండ్‌ను నడపండి


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

అభినందనలు! MLX ఫ్రేమ్‌వర్క్‌తో ఫైన్-ట్యూనింగ్‌లో నైపుణ్యం సాధించండి

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
డిస్క్లైమర్:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా అసంపూర్ణతలు ఉండే అవకాశం ఉన్నది అని దయచేసి గమనించండి. మూల పత్రాన్ని దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి ప్రొఫెషనల్ మానవ అనువాదం చేయించుకోవాలని సిఫార్సు చేస్తాం. ఈ అనువాదాన్ని ఉపయోగించడంవలన కలిగే ఏ అవగాహనా లోపాలు లేదా తప్పుగా అర్థం చేసుకోవడాలపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->