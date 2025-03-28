<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-03-27T16:03:58+00:00",
  "source_file": "md\\03.FineTuning\\03.Inference\\MLX_Inference.md",
  "language_code": "fr"
}
-->
# **Inférence Phi-3 avec le framework Apple MLX**

## **Qu'est-ce que le framework MLX**

MLX est un framework dédié à la recherche en apprentissage automatique sur les puces Apple Silicon, développé par l'équipe de recherche en apprentissage automatique d'Apple.

MLX a été conçu par des chercheurs en apprentissage automatique pour des chercheurs en apprentissage automatique. Ce framework vise à être à la fois convivial et performant pour entraîner et déployer des modèles. Sa conception est également pensée pour être simple sur le plan conceptuel, facilitant ainsi son extension et son amélioration par les chercheurs afin d'explorer rapidement de nouvelles idées.

Les LLMs peuvent être accélérés sur les appareils Apple Silicon grâce à MLX, et les modèles peuvent être exécutés localement de manière très pratique.

## **Utiliser MLX pour inférer Phi-3-mini**

### **1. Configurer votre environnement MLX**

1. Python 3.11.x  
2. Installer la bibliothèque MLX  

```bash

pip install mlx-lm

```

### **2. Exécuter Phi-3-mini dans le Terminal avec MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Le résultat (mon environnement est un Apple M1 Max, 64 Go) est :

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.fr.png)

### **3. Quantifier Phi-3-mini avec MLX dans le Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Remarque :*** Le modèle peut être quantifié via `mlx_lm.convert`, et la quantification par défaut est en INT4. Cet exemple quantifie Phi-3-mini en INT4.

Le modèle peut être quantifié via `mlx_lm.convert`, avec une quantification par défaut en INT4. Dans cet exemple, Phi-3-mini est quantifié en INT4. Après quantification, il sera stocké dans le répertoire par défaut `./mlx_model`.

Nous pouvons tester le modèle quantifié avec MLX depuis le terminal :

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Le résultat est :

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.fr.png)

### **4. Exécuter Phi-3-mini avec MLX dans un Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.fr.png)

***Remarque :*** Veuillez consulter cet exemple [cliquez sur ce lien](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Ressources**

1. En savoir plus sur le framework Apple MLX [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)  

2. Dépôt GitHub d'Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore)  

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous fassions tout notre possible pour garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.