<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-07T14:50:03+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "fr"
}
-->
# **Quantification de Phi-3.5 avec le framework Apple MLX**

MLX est un framework de tableaux pour la recherche en apprentissage automatique sur les puces Apple, développé par l'équipe de recherche en machine learning d'Apple.

MLX est conçu par des chercheurs en apprentissage automatique pour des chercheurs en apprentissage automatique. Le framework se veut convivial tout en restant efficace pour l'entraînement et le déploiement des modèles. Sa conception est également simple sur le plan conceptuel. Nous souhaitons faciliter l'extension et l'amélioration de MLX par les chercheurs afin de permettre une exploration rapide de nouvelles idées.

Les LLM peuvent être accélérés sur les appareils Apple Silicon grâce à MLX, et les modèles peuvent être exécutés localement de manière très pratique.

Le framework Apple MLX prend désormais en charge la conversion en quantification de Phi-3.5-Instruct (**support Apple MLX Framework**), Phi-3.5-Vision (**support MLX-VLM Framework**), et Phi-3.5-MoE (**support Apple MLX Framework**). Essayons cela :

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

| Labs    | Présentation | Accéder |
| -------- | ------- |  ------- |
| 🚀 Lab-Présentation Phi-3.5 Instruct  | Apprenez à utiliser Phi-3.5 Instruct avec le framework Apple MLX   |  [Accéder](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Présentation Phi-3.5 Vision (image) | Découvrez comment utiliser Phi-3.5 Vision pour analyser des images avec le framework Apple MLX     |  [Accéder](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Présentation Phi-3.5 Vision (moE)   | Apprenez à utiliser Phi-3.5 MoE avec le framework Apple MLX  |  [Accéder](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressources**

1. En savoir plus sur Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Dépôt GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Dépôt GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.