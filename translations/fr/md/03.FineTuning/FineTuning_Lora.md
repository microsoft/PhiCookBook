<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-03-27T13:55:44+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "fr"
}
-->
# **Ajustement fin de Phi-3 avec Lora**

Ajustement fin du modèle linguistique Phi-3 Mini de Microsoft en utilisant [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) sur un jeu de données personnalisé d'instructions de chat.

LoRA permettra d'améliorer la compréhension conversationnelle et la génération de réponses.

## Guide étape par étape pour ajuster Phi-3 Mini :

**Imports et Configuration**

Installation de loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Commencez par importer les bibliothèques nécessaires comme datasets, transformers, peft, trl, et torch. Configurez le logging pour suivre le processus d'entraînement.

Vous pouvez choisir d'adapter certaines couches en les remplaçant par des équivalents implémentés dans loralib. Nous ne supportons actuellement que nn.Linear, nn.Embedding, et nn.Conv2d. Nous supportons également un MergedLinear pour les cas où un seul nn.Linear représente plusieurs couches, comme dans certaines implémentations de la projection attention qkv (voir Notes supplémentaires pour plus d'informations).

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

Avant de commencer la boucle d'entraînement, marquez uniquement les paramètres LoRA comme entraînables.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Lors de la sauvegarde d'un checkpoint, générez un state_dict contenant uniquement les paramètres LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Lors du chargement d'un checkpoint avec load_state_dict, assurez-vous de définir strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

L'entraînement peut maintenant se dérouler comme d'habitude.

**Hyperparamètres**

Définissez deux dictionnaires : training_config et peft_config. training_config inclut les hyperparamètres pour l'entraînement, comme le taux d'apprentissage, la taille des lots, et les paramètres de journalisation.

peft_config spécifie les paramètres liés à LoRA tels que le rang, le dropout, et le type de tâche.

**Chargement du modèle et du tokenizer**

Spécifiez le chemin vers le modèle Phi-3 pré-entraîné (par exemple, "microsoft/Phi-3-mini-4k-instruct"). Configurez les paramètres du modèle, notamment l'utilisation du cache, le type de données (bfloat16 pour la précision mixte), et l'implémentation de l'attention.

**Entraînement**

Ajustez le modèle Phi-3 en utilisant le jeu de données personnalisé d'instructions de chat. Utilisez les paramètres LoRA définis dans peft_config pour une adaptation efficace. Surveillez les progrès de l'entraînement grâce à la stratégie de journalisation spécifiée.

**Évaluation et Sauvegarde** : Évaluez le modèle ajusté. Sauvegardez les checkpoints pendant l'entraînement pour une utilisation ultérieure.

**Exemples**
- [En savoir plus avec cet exemple de notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemple de script Python pour l'ajustement fin](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exemple d'ajustement fin avec LORA sur Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemple de fiche modèle Hugging Face - Ajustement fin avec LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Exemple d'ajustement fin avec QLORA sur Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations découlant de l'utilisation de cette traduction.