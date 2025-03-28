<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-03-27T08:22:53+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "fr"
}
-->
# **Quantification de Phi-3.5 avec le Framework Apple MLX**

MLX est un framework matriciel pour la recherche en apprentissage automatique sur les puces Apple Silicon, développé par l'équipe de recherche en apprentissage automatique d'Apple.

MLX est conçu par des chercheurs en apprentissage automatique pour des chercheurs en apprentissage automatique. Le framework se veut convivial tout en restant efficace pour entraîner et déployer des modèles. Sa conception est également conceptuellement simple. Nous visons à faciliter l'extension et l'amélioration de MLX par les chercheurs afin d'explorer rapidement de nouvelles idées.

Les LLM peuvent être accélérés sur les appareils équipés d'Apple Silicon grâce à MLX, et les modèles peuvent être exécutés localement de manière très pratique.

Désormais, le Framework Apple MLX prend en charge la conversion quantifiée de Phi-3.5-Instruct (**support du Framework Apple MLX**), Phi-3.5-Vision (**support du Framework MLX-VLM**), et Phi-3.5-MoE (**support du Framework Apple MLX**). Essayons cela :

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Exemples pour Phi-3.5 avec Apple MLX**

| Laboratoires    | Présentation | Accéder |
| -------- | ------- |  ------- |
| 🚀 Présentation Phi-3.5 Instruct  | Apprenez à utiliser Phi-3.5 Instruct avec le framework Apple MLX   |  [Accéder](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Présentation Phi-3.5 Vision (image) | Apprenez à utiliser Phi-3.5 Vision pour analyser des images avec le framework Apple MLX     |  [Accéder](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Présentation Phi-3.5 Vision (moE)   | Apprenez à utiliser Phi-3.5 MoE avec le framework Apple MLX  |  [Accéder](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressources**

1. En savoir plus sur le Framework Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Dépôt GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Dépôt GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.