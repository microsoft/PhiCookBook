<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b1ec18a3db0bb90ba8483eceade60031",
  "translation_date": "2025-04-04T19:00:50+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_MLX.md",
  "language_code": "hi"
}
-->
# **Apple MLX फ्रेमवर्क के साथ Phi-3 का फाइन-ट्यूनिंग**

हम Apple MLX फ्रेमवर्क के कमांड लाइन का उपयोग करके Lora के साथ संयुक्त फाइन-ट्यूनिंग पूरा कर सकते हैं। (यदि आप MLX फ्रेमवर्क के संचालन के बारे में अधिक जानना चाहते हैं, तो कृपया [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) पढ़ें।)

## **1. डेटा तैयारी**

डिफ़ॉल्ट रूप से, MLX फ्रेमवर्क को ट्रेन, टेस्ट और ईवाल के jsonl फॉर्मेट की आवश्यकता होती है और यह Lora के साथ संयुक्त होकर फाइन-ट्यूनिंग कार्यों को पूरा करता है।

### ***नोट:***

1. jsonl डेटा फॉर्मेट:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. हमारे उदाहरण में [TruthfulQA के डेटा](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) का उपयोग किया गया है, लेकिन डेटा की मात्रा अपेक्षाकृत कम है, इसलिए फाइन-ट्यूनिंग के परिणाम जरूरी नहीं कि सबसे अच्छे हों। यह अनुशंसा की जाती है कि शिक्षार्थी अपने स्वयं के परिदृश्यों के आधार पर बेहतर डेटा का उपयोग करके पूरा करें।

3. डेटा फॉर्मेट Phi-3 टेम्पलेट के साथ संयुक्त है।

कृपया इस [लिंक](../../../../code/04.Finetuning/mlx) से डेटा डाउनलोड करें, कृपया ***data*** फ़ोल्डर में सभी .jsonl को शामिल करें।

## **2. अपने टर्मिनल में फाइन-ट्यूनिंग**

कृपया इस कमांड को टर्मिनल में चलाएं:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***नोट:***

1. यह LoRA फाइन-ट्यूनिंग है, MLX फ्रेमवर्क ने अभी तक QLoRA को प्रकाशित नहीं किया है।

2. आप config.yaml सेट करके कुछ तर्कों को बदल सकते हैं, जैसे:

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

कृपया इस कमांड को टर्मिनल में चलाएं:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. फाइन-ट्यूनिंग एडेप्टर को टेस्ट करना**

आप टर्मिनल में फाइन-ट्यूनिंग एडेप्टर को चला सकते हैं, जैसे:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

और मूल मॉडल को चलाकर परिणाम की तुलना करें:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

आप फाइन-ट्यूनिंग के परिणामों की तुलना मूल मॉडल के साथ कर सकते हैं।

## **4. एडेप्टर को मर्ज करके नए मॉडल बनाना**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ollama का उपयोग करके क्वांटिफाइड फाइन-ट्यूनिंग मॉडल चलाना**

उपयोग से पहले, कृपया अपने llama.cpp पर्यावरण को कॉन्फ़िगर करें:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***नोट:*** 

1. अब fp32, fp16 और INT 8 के क्वांटाइजेशन कन्वर्जन का समर्थन करता है।

2. मर्ज किए गए मॉडल में tokenizer.model गायब है, कृपया इसे https://huggingface.co/microsoft/Phi-3-mini-4k-instruct से डाउनलोड करें।

एक [Ollama Model](https://ollama.com/) सेट करें।

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

टर्मिनल में कमांड चलाएं:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

बधाई हो! आपने MLX फ्रेमवर्क के साथ फाइन-ट्यूनिंग को मास्टर कर लिया है।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या गलतियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।