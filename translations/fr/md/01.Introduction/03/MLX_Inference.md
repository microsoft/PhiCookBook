<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-07T14:37:02+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "fr"
}
-->
# **Inférence Phi-3 avec le framework Apple MLX**

## **Qu'est-ce que le framework MLX**

MLX est un framework de tableaux pour la recherche en apprentissage automatique sur les puces Apple, développé par l'équipe de recherche en apprentissage automatique d'Apple.

MLX est conçu par des chercheurs en apprentissage automatique pour des chercheurs en apprentissage automatique. Le framework vise à être facile d'utilisation tout en restant efficace pour l'entraînement et le déploiement des modèles. La conception du framework est également simple sur le plan conceptuel. Notre objectif est de permettre aux chercheurs d’étendre et d’améliorer MLX facilement afin d’explorer rapidement de nouvelles idées.

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

Le résultat (mon environnement est un Apple M1 Max, 64GB) est

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.fr.png)

### **3. Quantifier Phi-3-mini avec MLX dans le Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note :*** Le modèle peut être quantifié via mlx_lm.convert, la quantification par défaut étant en INT4. Cet exemple quantifie Phi-3-mini en INT4.

Le modèle peut être quantifié via mlx_lm.convert, la quantification par défaut étant en INT4. Cet exemple montre comment quantifier Phi-3-mini en INT4. Après quantification, il sera stocké dans le répertoire par défaut ./mlx_model

Nous pouvons tester le modèle quantifié avec MLX depuis le terminal


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Le résultat est

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.fr.png)


### **4. Exécuter Phi-3-mini avec MLX dans Jupyter Notebook**


![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.fr.png)

***Note :*** Veuillez consulter cet exemple [cliquer sur ce lien](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Ressources**

1. En savoir plus sur Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Dépôt GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.