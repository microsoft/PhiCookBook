<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-07T13:30:09+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "fr"
}
-->
# **Affinage de Phi-3 avec Lora**

Affinage du modèle de langage Phi-3 Mini de Microsoft en utilisant [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) sur un jeu de données personnalisé d'instructions de chat.

LORA permettra d'améliorer la compréhension conversationnelle et la génération de réponses.

## Guide étape par étape pour affiner Phi-3 Mini :

**Imports et Configuration**

Installation de loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Commencez par importer les bibliothèques nécessaires telles que datasets, transformers, peft, trl et torch.  
Configurez la journalisation pour suivre le processus d'entraînement.

Vous pouvez choisir d’adapter certaines couches en les remplaçant par des équivalents implémentés dans loralib. Nous supportons pour l’instant nn.Linear, nn.Embedding et nn.Conv2d. Nous prenons également en charge un MergedLinear pour les cas où un seul nn.Linear représente plusieurs couches, comme dans certaines implémentations de la projection qkv de l’attention (voir Notes supplémentaires pour plus de détails).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Avant de commencer la boucle d’entraînement, marquez uniquement les paramètres LoRA comme entraînables.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Lors de la sauvegarde d’un checkpoint, générez un state_dict ne contenant que les paramètres LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Lors du chargement d’un checkpoint avec load_state_dict, veillez à définir strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

L’entraînement peut maintenant se dérouler normalement.

**Hyperparamètres**

Définissez deux dictionnaires : training_config et peft_config. training_config contient les hyperparamètres d’entraînement, tels que le taux d’apprentissage, la taille des lots et les paramètres de journalisation.

peft_config précise les paramètres liés à LoRA comme le rang, le dropout et le type de tâche.

**Chargement du Modèle et du Tokenizer**

Indiquez le chemin vers le modèle pré-entraîné Phi-3 (par exemple, "microsoft/Phi-3-mini-4k-instruct"). Configurez les paramètres du modèle, y compris l’utilisation du cache, le type de données (bfloat16 pour la précision mixte) et l’implémentation de l’attention.

**Entraînement**

Affinez le modèle Phi-3 avec le jeu de données personnalisé d’instructions de chat. Utilisez les paramètres LoRA définis dans peft_config pour une adaptation efficace. Surveillez la progression de l’entraînement grâce à la stratégie de journalisation spécifiée.  
Évaluation et sauvegarde : évaluez le modèle affiné.  
Sauvegardez les checkpoints pendant l’entraînement pour une utilisation ultérieure.

**Exemples**  
- [En savoir plus avec ce notebook d’exemple](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Exemple de script Python pour FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Exemple de Fine Tuning sur Hugging Face Hub avec LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Exemple de fiche modèle Hugging Face - Exemple de Fine Tuning LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Exemple de Fine Tuning sur Hugging Face Hub avec QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.