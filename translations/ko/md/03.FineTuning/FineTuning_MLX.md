<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T07:58:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "ko"
}
-->
# **Apple MLX 프레임워크로 Phi-3 미세 조정하기**

Apple MLX 프레임워크 명령어를 통해 Lora와 결합된 미세 조정을 완료할 수 있습니다. (MLX 프레임워크의 작동 방식에 대해 더 알고 싶다면 [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)를 참고하세요)


## **1. 데이터 준비**

기본적으로 MLX 프레임워크는 train, test, eval의 jsonl 형식을 요구하며, Lora와 결합하여 미세 조정 작업을 완료합니다.


### ***Note:***

1. jsonl 데이터 형식 ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 예제에서는 [TruthfulQA의 데이터](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)를 사용하지만, 데이터 양이 상대적으로 부족하여 미세 조정 결과가 반드시 최적은 아닙니다. 학습자는 자신의 시나리오에 맞는 더 좋은 데이터를 사용하여 진행하는 것을 권장합니다.

3. 데이터 형식은 Phi-3 템플릿과 결합되어 있습니다.

데이터는 이 [링크](../../../../code/04.Finetuning/mlx)에서 다운로드해 주세요. ***data*** 폴더 내 모든 .jsonl 파일을 포함해야 합니다.


## **2. 터미널에서 미세 조정 실행하기**

터미널에서 다음 명령어를 실행하세요


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. 이것은 LoRA 미세 조정이며, MLX 프레임워크는 QLoRA를 지원하지 않습니다.

2. config.yaml 파일을 수정하여 일부 인자를 변경할 수 있습니다. 예를 들어


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

터미널에서 다음 명령어를 실행하세요


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. 미세 조정 어댑터 테스트 실행**

터미널에서 미세 조정 어댑터를 다음과 같이 실행할 수 있습니다


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

원본 모델도 실행하여 결과를 비교해 보세요


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

미세 조정된 모델과 원본 모델의 결과를 비교해 볼 수 있습니다.


## **4. 어댑터 병합하여 새 모델 생성하기**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama를 사용한 양자화된 미세 조정 모델 실행**

사용 전 llama.cpp 환경을 설정해 주세요


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. 현재 fp32, fp16, INT 8 양자화 변환을 지원합니다.

2. 병합된 모델에 tokenizer.model이 누락되어 있으니 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 에서 다운로드해 주세요.

[Ollma Model](https://ollama.com/) 설정


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

터미널에서 명령어 실행


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

축하합니다! MLX 프레임워크로 미세 조정을 마스터하셨습니다

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.