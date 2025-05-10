<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-09T21:42:25+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "pt"
}
-->
# **Ajuste fino do Phi-3 com o Apple MLX Framework**

Podemos realizar o ajuste fino combinado com Lora através da linha de comando do Apple MLX Framework. (Se quiser saber mais sobre o funcionamento do MLX Framework, por favor leia [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Preparação dos dados**

Por padrão, o MLX Framework exige o formato jsonl para train, test e eval, e é combinado com Lora para completar os trabalhos de ajuste fino.


### ***Nota:***

1. Formato dos dados jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Nosso exemplo usa os dados do [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), mas a quantidade de dados é relativamente pequena, então os resultados do ajuste fino podem não ser os melhores. Recomendamos que os aprendizes usem dados melhores baseados em seus próprios cenários para realizar o ajuste.

3. O formato dos dados é combinado com o template do Phi-3

Por favor, baixe os dados neste [link](../../../../code/04.Finetuning/mlx), incluindo todos os arquivos .jsonl na pasta ***data***


## **2. Ajuste fino no seu terminal**

Por favor, execute este comando no terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Nota:***

1. Este é um ajuste fino LoRA, o MLX framework ainda não publicou QLoRA

2. Você pode configurar o config.yaml para alterar alguns argumentos, como


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

Por favor, execute este comando no terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Execute o adaptador de ajuste fino para testar**

Você pode rodar o adaptador de ajuste fino no terminal, assim 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

e rodar o modelo original para comparar os resultados 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Você pode tentar comparar os resultados do ajuste fino com o modelo original


## **4. Mesclar adaptadores para gerar novos modelos**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Executando modelos de ajuste fino quantizados usando ollama**

Antes de usar, por favor configure seu ambiente llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Nota:*** 

1. Agora suporta conversão de quantização para fp32, fp16 e INT 8

2. O modelo mesclado está sem o tokenizer.model, por favor baixe-o em https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

defina um [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

execute o comando no terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Parabéns! Você dominou o ajuste fino com o MLX Framework

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.