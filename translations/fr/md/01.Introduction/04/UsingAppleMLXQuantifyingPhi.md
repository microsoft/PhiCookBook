# **Quantification de Phi-3.5 avec le framework Apple MLX**

MLX est un framework pour la recherche en apprentissage automatique sur les puces Apple Silicon, développé par l’équipe de recherche en machine learning d’Apple.

MLX a été conçu par des chercheurs en apprentissage automatique pour des chercheurs en apprentissage automatique. Le framework se veut à la fois simple d’utilisation et efficace pour entraîner et déployer des modèles. Sa conception est également simple sur le plan conceptuel. Nous souhaitons faciliter l’extension et l’amélioration de MLX par les chercheurs afin de permettre une exploration rapide de nouvelles idées.

Les LLMs peuvent être accélérés sur les appareils Apple Silicon grâce à MLX, et les modèles peuvent être exécutés localement de manière très pratique.

Désormais, le framework Apple MLX prend en charge la conversion en quantification de Phi-3.5-Instruct (**prise en charge par Apple MLX Framework**), Phi-3.5-Vision (**prise en charge par MLX-VLM Framework**), et Phi-3.5-MoE (**prise en charge par Apple MLX Framework**). Essayons cela maintenant :

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
| -------- | ----------- | ------- |
| 🚀 Lab-Présentation Phi-3.5 Instruct  | Apprenez à utiliser Phi-3.5 Instruct avec le framework Apple MLX   |  [Accéder](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Présentation Phi-3.5 Vision (image) | Apprenez à utiliser Phi-3.5 Vision pour analyser des images avec le framework Apple MLX     |  [Accéder](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Présentation Phi-3.5 Vision (moE)   | Apprenez à utiliser Phi-3.5 MoE avec le framework Apple MLX  |  [Accéder](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressources**

1. En savoir plus sur Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Dépôt GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Dépôt GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.