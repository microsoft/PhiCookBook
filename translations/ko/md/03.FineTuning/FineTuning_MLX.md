<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b1ec18a3db0bb90ba8483eceade60031",
  "translation_date": "2025-04-04T07:10:02+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_MLX.md",
  "language_code": "ko"
}
-->
# **Apple MLX 프레임워크로 Phi-3 미세 조정**

Apple MLX 프레임워크 명령어를 통해 Lora와 결합하여 미세 조정을 완료할 수 있습니다. (MLX 프레임워크의 작동 방식에 대해 더 알고 싶다면 [Apple MLX 프레임워크로 Phi-3 추론하기](../03.FineTuning/03.Inference/MLX_Inference.md)를 읽어보세요.)

## **1. 데이터 준비**

기본적으로 MLX 프레임워크는 train, test, eval의 jsonl 형식을 요구하며, Lora와 결합하여 미세 조정 작업을 완료합니다.

### ***참고:***

1. jsonl 데이터 형식：

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 예제에서는 [TruthfulQA 데이터](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)를 사용하지만 데이터 양이 비교적 부족하기 때문에 미세 조정 결과가 반드시 최상의 결과를 보장하지는 않습니다. 학습자들은 자신만의 시나리오에 맞는 더 나은 데이터를 사용하여 작업을 완료하는 것을 권장합니다.

3. 데이터 형식은 Phi-3 템플릿과 결합됩니다.

데이터를 이 [링크](../../../../code/04.Finetuning/mlx)에서 다운로드하세요. ***data*** 폴더에 있는 모든 .jsonl 파일을 포함해야 합니다.

## **2. 터미널에서 미세 조정 실행**

터미널에서 아래 명령어를 실행하세요.

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***참고:***

1. 이는 LoRA 미세 조정이며, MLX 프레임워크는 아직 QLoRA를 제공하지 않습니다.

2. config.yaml 파일을 설정하여 몇 가지 매개변수를 변경할 수 있습니다. 예를 들어:

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

터미널에서 아래 명령어를 실행하세요.

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. 미세 조정 어댑터 테스트 실행**

터미널에서 미세 조정 어댑터를 실행할 수 있습니다. 아래와 같이:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

그리고 원본 모델을 실행하여 결과를 비교해 보세요.

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Fine-tuning 결과와 원본 모델 결과를 비교해 보세요.

## **4. 어댑터 병합하여 새 모델 생성**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ollama를 사용하여 양자화된 미세 조정 모델 실행**

사용하기 전에 llama.cpp 환경을 설정하세요.

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***참고:*** 

1. 현재 fp32, fp16 및 INT 8의 양자화 변환을 지원합니다.

2. 병합된 모델에는 tokenizer.model이 없으므로 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct에서 다운로드하세요.

[Ollama 모델](https://ollama.com/)을 설정하세요.

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

터미널에서 명령어를 실행하세요.

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

축하합니다! MLX 프레임워크를 사용한 미세 조정을 마스터했습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원어로 작성된 원본 문서를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.