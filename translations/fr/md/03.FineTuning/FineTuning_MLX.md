<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-05-07T13:26:15+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "fr"
}
-->
# **Affinage de Phi-3 avec le framework Apple MLX**

Nous pouvons réaliser l’affinage combiné avec Lora via la ligne de commande du framework Apple MLX. (Si vous souhaitez en savoir plus sur le fonctionnement du framework MLX, veuillez lire [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. Préparation des données**

Par défaut, le framework MLX requiert un format jsonl pour train, test et eval, et s’associe avec Lora pour effectuer les tâches d’affinage.

### ***Note :***

1. Format des données jsonl :

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Notre exemple utilise les données de [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), mais la quantité de données est relativement limitée, donc les résultats d’affinage ne sont pas forcément optimaux. Il est recommandé aux apprenants d’utiliser des données plus adaptées à leurs propres cas d’usage.

3. Le format des données est combiné avec le template Phi-3.

Veuillez télécharger les données depuis ce [lien](../../../../code/04.Finetuning/mlx), en incluant tous les fichiers .jsonl dans le dossier ***data***.

## **2. Affinage dans votre terminal**

Veuillez exécuter cette commande dans le terminal :

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Note :***

1. Il s’agit d’un affinage LoRA, le framework MLX ne publie pas QLoRA.

2. Vous pouvez modifier config.yaml pour changer certains arguments, par exemple :

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

Veuillez exécuter cette commande dans le terminal :

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Tester l’adaptateur d’affinage**

Vous pouvez lancer l’adaptateur d’affinage dans le terminal, comme ceci :

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

et exécuter le modèle original pour comparer les résultats :

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Vous pouvez essayer de comparer les résultats de l’affinage avec le modèle original.

## **4. Fusionner les adaptateurs pour générer de nouveaux modèles**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Exécuter les modèles affinés quantifiés avec ollama**

Avant utilisation, veuillez configurer votre environnement llama.cpp

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note :***

1. La conversion de quantification supporte désormais fp32, fp16 et INT 8.

2. Le modèle fusionné ne contient pas tokenizer.model, veuillez le télécharger depuis https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

Configurez un [Ollama Model](https://ollama.com/)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Exécutez la commande dans le terminal :

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Félicitations ! Vous maîtrisez l’affinage avec le framework MLX.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables de tout malentendu ou mauvaise interprétation résultant de l’utilisation de cette traduction.