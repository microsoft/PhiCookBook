<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-03-27T14:53:36+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_MLX.md",
  "language_code": "fr"
}
-->
# **Affiner Phi-3 avec le framework Apple MLX**

Nous pouvons réaliser un ajustement fin combiné avec Lora via la ligne de commande du framework Apple MLX. (Si vous souhaitez en savoir plus sur le fonctionnement du framework MLX, veuillez lire [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)

## **1. Préparation des données**

Par défaut, le framework MLX nécessite le format jsonl pour les ensembles d'entraînement, de test et d'évaluation, et il est combiné avec Lora pour effectuer les tâches d'ajustement fin.

### ***Remarque :***

1. Format des données jsonl :

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Notre exemple utilise les [données de TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), mais la quantité de données est relativement insuffisante, donc les résultats de l'ajustement fin ne sont pas forcément optimaux. Il est recommandé aux apprenants d'utiliser des données de meilleure qualité adaptées à leurs propres scénarios.

3. Le format des données est combiné avec le modèle Phi-3.

Veuillez télécharger les données depuis ce [lien](../../../../code/04.Finetuning/mlx), et inclure tous les fichiers .jsonl dans le dossier ***data***.

## **2. Affiner via votre terminal**

Veuillez exécuter cette commande dans le terminal :

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Remarque :***

1. Ceci est un ajustement fin avec LoRA, le framework MLX ne prend pas encore en charge QLoRA.

2. Vous pouvez modifier config.yaml pour changer certains arguments, comme :

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

## **3. Tester l'adaptateur d'ajustement fin**

Vous pouvez exécuter l'adaptateur d'ajustement fin dans le terminal, comme ceci :

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

et exécuter le modèle original pour comparer les résultats :

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Vous pouvez essayer de comparer les résultats de l'ajustement fin avec ceux du modèle original.

## **4. Fusionner les adaptateurs pour générer de nouveaux modèles**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Exécuter des modèles affinés quantifiés avec Ollama**

Avant utilisation, veuillez configurer votre environnement llama.cpp.

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Remarque :***

1. La conversion quantifiée des formats fp32, fp16 et INT8 est maintenant prise en charge.

2. Le modèle fusionné ne contient pas tokenizer.model, veuillez le télécharger depuis https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Configurer un [modèle Ollama](https://ollama.com/).

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Exécutez la commande dans le terminal :

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Félicitations ! Vous maîtrisez désormais l'ajustement fin avec le framework MLX.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.