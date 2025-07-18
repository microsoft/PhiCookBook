<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T07:56:22+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "es"
}
-->
# **Ajuste fino de Phi-3 con el framework Apple MLX**

Podemos completar el ajuste fino combinado con Lora a través de la línea de comandos del framework Apple MLX. (Si quieres saber más sobre el funcionamiento del framework MLX, por favor lee [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Preparación de datos**

Por defecto, el framework MLX requiere el formato jsonl para train, test y eval, y se combina con Lora para completar los trabajos de ajuste fino.


### ***Note:***

1. Formato de datos jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Nuestro ejemplo usa los datos de [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), pero la cantidad de datos es relativamente insuficiente, por lo que los resultados del ajuste fino no son necesariamente los mejores. Se recomienda que los usuarios utilicen datos mejores basados en sus propios escenarios para completar el proceso.

3. El formato de datos está combinado con la plantilla de Phi-3

Por favor descarga los datos desde este [enlace](../../../../code/04.Finetuning/mlx), incluye todos los archivos .jsonl en la carpeta ***data***


## **2. Ajuste fino en tu terminal**

Por favor ejecuta este comando en la terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Este es un ajuste fino con LoRA, el framework MLX no ha publicado QLoRA

2. Puedes configurar config.yaml para cambiar algunos argumentos, como


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

Por favor ejecuta este comando en la terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Ejecutar el adaptador de ajuste fino para probar**

Puedes ejecutar el adaptador de ajuste fino en la terminal, así:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

y ejecutar el modelo original para comparar resultados


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Puedes intentar comparar los resultados del ajuste fino con el modelo original


## **4. Fusionar adaptadores para generar nuevos modelos**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ejecutar modelos de ajuste fino cuantificados usando ollama**

Antes de usar, por favor configura tu entorno llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Ahora soporta conversión de cuantización para fp32, fp16 e INT 8

2. El modelo fusionado no incluye tokenizer.model, por favor descárgalo desde https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

configura un [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ejecuta el comando en la terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

¡Felicidades! Domina el ajuste fino con el framework MLX

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.