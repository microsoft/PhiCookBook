# **Apple MLX Framework ile Phi-3 İnce Ayarı**

Apple MLX framework komut satırı üzerinden Lora ile birleştirilmiş ince ayarı tamamlayabiliriz. (MLX Framework’ün çalışma prensibini daha iyi anlamak isterseniz, lütfen [Apple MLX Framework ile Phi-3 Çıkarımı](../03.FineTuning/03.Inference/MLX_Inference.md) dosyasını okuyun)


## **1. Veri hazırlığı**

Varsayılan olarak, MLX Framework eğitim, test ve değerlendirme için jsonl formatını gerektirir ve Lora ile birleştirilerek ince ayar işleri tamamlanır.


### ***Not:***

1. jsonl veri formatı ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Örneğimizde [TruthfulQA verisi](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) kullanılmıştır, ancak veri miktarı nispeten yetersiz olduğundan ince ayar sonuçları mutlaka en iyi olmayabilir. Öğrenenlerin kendi senaryolarına göre daha iyi veriler kullanmaları önerilir.

3. Veri formatı Phi-3 şablonuyla uyumludur

Lütfen verileri bu [linkten](../../../../code/04.Finetuning/mlx) indirin, ***data*** klasöründeki tüm .jsonl dosyalarını dahil edin


## **2. Terminalde ince ayar**

Lütfen terminalde şu komutu çalıştırın


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Not:***

1. Bu LoRA ince ayarıdır, MLX framework QLoRA’yı yayınlamamıştır

2. Bazı argümanları değiştirmek için config.yaml dosyasını ayarlayabilirsiniz, örneğin


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

Lütfen terminalde şu komutu çalıştırın


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. İnce ayar adaptörünü test etmek için çalıştırma**

Terminalde ince ayar adaptörünü şu şekilde çalıştırabilirsiniz


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ve sonuçları karşılaştırmak için orijinal modeli çalıştırın


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

İnce ayar sonuçlarını orijinal modelle karşılaştırmayı deneyebilirsiniz


## **4. Adaptörleri birleştirerek yeni modeller oluşturma**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ollama kullanarak nicelenmiş ince ayar modellerini çalıştırma**

Kullanmadan önce, lütfen llama.cpp ortamınızı yapılandırın


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Not:*** 

1. Şu anda fp32, fp16 ve INT 8 nicelleştirme dönüşümü desteklenmektedir

2. Birleştirilmiş modelde tokenizer.model eksik, lütfen https://huggingface.co/microsoft/Phi-3-mini-4k-instruct adresinden indirin

Bir [Ollama Modeli](https://ollama.com/) ayarlayın


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Terminalde komutu çalıştırın


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Tebrikler! MLX Framework ile ince ayarı ustalıkla tamamladınız

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.