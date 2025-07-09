<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-09T18:56:44+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "my"
}
-->
# **Apple MLX Framework ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း**

Apple MLX framework command line မှတဆင့် Lora နှင့်ပေါင်းစပ်ပြီး Fine-tuning ကို ပြီးမြောက်စွာ ဆောင်ရွက်နိုင်ပါသည်။ (MLX Framework ၏ လည်ပတ်ပုံကို ပိုမိုသိရှိလိုပါက [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) ကို ဖတ်ရှုပါ)


## **1. ဒေတာ ပြင်ဆင်ခြင်း**

ပုံမှန်အားဖြင့် MLX Framework သည် train, test, eval အတွက် jsonl ဖော်မတ်ကို လိုအပ်ပြီး Lora နှင့်ပေါင်းစပ်၍ fine-tuning အလုပ်များကို ပြီးမြောက်စေပါသည်။


### ***Note:***

1. jsonl ဒေတာဖော်မတ် ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ဥပမာအနေဖြင့် [TruthfulQA ၏ ဒေတာ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ကို အသုံးပြုထားသော်လည်း ဒေတာအရေအတွက် မလုံလောက်သဖြင့် fine-tuning ရလဒ်များသည် အကောင်းဆုံး မဖြစ်နိုင်ပါ။ သင်ယူသူများသည် ကိုယ်ပိုင်အခြေအနေများအပေါ် မူတည်၍ ပိုမိုကောင်းမွန်သော ဒေတာများကို အသုံးပြု၍ ပြီးမြောက်စေရန် အကြံပြုပါသည်။

3. ဒေတာဖော်မတ်သည် Phi-3 template နှင့် ပေါင်းစပ်ထားသည်

ဒီ [link](../../../../code/04.Finetuning/mlx) မှ ဒေတာများကို ဒေါင်းလုပ်လုပ်ပါ၊ ***data*** ဖိုလ်ဒါအတွင်းရှိ .jsonl ဖိုင်အားလုံးပါဝင်ရန် သေချာပါစေ


## **2. သင့် terminal တွင် Fine-tuning ပြုလုပ်ခြင်း**

terminal တွင် အောက်ပါ command ကို ပြေးပါ


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. ၎င်းမှာ LoRA fine-tuning ဖြစ်ပြီး MLX framework သည် QLoRA ကို မထုတ်ပြန်သေးပါ

2. config.yaml တွင် အချို့သော argument များကို ပြောင်းလဲနိုင်ပါသည်၊ ဥပမာ -


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

terminal တွင် အောက်ပါ command ကို ပြေးပါ


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Fine-tuning adapter ကို စမ်းသပ်ရန် ပြေးခြင်း**

terminal တွင် fine-tuning adapter ကို အောက်ပါအတိုင်း ပြေးနိုင်ပါသည် 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

နောက်ပြီး မူရင်းမော်ဒယ်ကို ပြေးပြီး ရလဒ်များကို နှိုင်းယှဉ်ပါ 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Fine-tuning ရလဒ်များနှင့် မူရင်းမော်ဒယ်ရလဒ်များကို နှိုင်းယှဉ်ကြည့်နိုင်ပါသည်


## **4. Adapter များကို ပေါင်းစပ်၍ မော်ဒယ်အသစ်များ ဖန်တီးခြင်း**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama ဖြင့် quantified fine-tuning မော်ဒယ်များကို ပြေးခြင်း**

အသုံးပြုမည့်အရင် llama.cpp ပတ်ဝန်းကျင်ကို ပြင်ဆင်ထားပါ


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. ယခု fp32, fp16 နှင့် INT 8 ၏ quantization ပြောင်းလဲမှုကို ထောက်ပံ့သည်

2. ပေါင်းစပ်ထားသော မော်ဒယ်တွင် tokenizer.model မပါရှိသဖြင့် https://huggingface.co/microsoft/Phi-3-mini-4k-instruct မှ ဒေါင်းလုပ်လုပ်ပါ

[Ollma Model](https://ollama.com/) တစ်ခု သတ်မှတ်ပါ


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

terminal တွင် command ကို ပြေးပါ


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

ဂုဏ်ယူပါတယ်! MLX Framework ဖြင့် fine-tuning ကို ကျွမ်းကျင်စွာ လေ့လာပြီးပါပြီ။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။