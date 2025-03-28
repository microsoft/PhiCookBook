<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-03-27T14:59:45+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Phi-3-visionWandB.md",
  "language_code": "fr"
}
-->
# Aperçu du projet Phi-3-Vision-128K-Instruct

## Le modèle

Le Phi-3-Vision-128K-Instruct, un modèle multimodal léger et de pointe, est au cœur de ce projet. Il fait partie de la famille des modèles Phi-3 et prend en charge une longueur de contexte allant jusqu'à 128 000 tokens. Le modèle a été entraîné sur un ensemble de données diversifié comprenant des données synthétiques et des sites web publics soigneusement filtrés, en mettant l'accent sur du contenu de haute qualité nécessitant un raisonnement approfondi. Le processus d'entraînement inclut un ajustement supervisé et une optimisation directe des préférences afin de garantir une adhésion précise aux instructions, ainsi que des mesures de sécurité robustes.

## Créer des données d'exemple est crucial pour plusieurs raisons :

1. **Tests** : Les données d'exemple permettent de tester votre application dans divers scénarios sans affecter les données réelles. Cela est particulièrement important dans les phases de développement et de mise en scène.

2. **Optimisation des performances** : Avec des données d'exemple qui imitent l'échelle et la complexité des données réelles, vous pouvez identifier les goulots d'étranglement en termes de performances et optimiser votre application en conséquence.

3. **Prototypage** : Les données d'exemple peuvent être utilisées pour créer des prototypes et des maquettes, ce qui peut aider à comprendre les besoins des utilisateurs et à obtenir des retours.

4. **Analyse des données** : En science des données, les données d'exemple sont souvent utilisées pour l'analyse exploratoire, l'entraînement des modèles et les tests d'algorithmes.

5. **Sécurité** : Utiliser des données d'exemple dans les environnements de développement et de test peut aider à prévenir les fuites accidentelles de données sensibles réelles.

6. **Apprentissage** : Si vous apprenez une nouvelle technologie ou un nouvel outil, travailler avec des données d'exemple peut offrir un moyen pratique d'appliquer ce que vous avez appris.

Rappelez-vous, la qualité de vos données d'exemple peut avoir un impact significatif sur ces activités. Elles doivent être aussi proches que possible des données réelles en termes de structure et de variabilité.

### Création de données d'exemple
[Script de génération de jeu de données](./CreatingSampleData.md)

## Jeu de données

Un bon exemple de jeu de données d'exemple est [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponible sur Huggingface).  
Le jeu de données d'exemple des produits Burberry inclut des métadonnées sur la catégorie, le prix et le titre des produits, avec un total de 3 040 lignes, chacune représentant un produit unique. Ce jeu de données nous permet de tester la capacité du modèle à comprendre et interpréter des données visuelles, en générant des textes descriptifs qui capturent des détails visuels complexes et des caractéristiques spécifiques à la marque.

**Note** : Vous pouvez utiliser n'importe quel jeu de données incluant des images.

## Raisonnement complexe

Le modèle doit raisonner sur les prix et les noms uniquement à partir de l'image. Cela exige que le modèle ne se contente pas de reconnaître des caractéristiques visuelles, mais qu'il comprenne également leurs implications en termes de valeur du produit et de marque. En synthétisant des descriptions textuelles précises à partir d'images, le projet met en lumière le potentiel de l'intégration des données visuelles pour améliorer la performance et la polyvalence des modèles dans des applications concrètes.

## Architecture Phi-3 Vision

L'architecture du modèle est une version multimodale d'un Phi-3. Elle traite à la fois les données textuelles et les données visuelles, intégrant ces entrées dans une séquence unifiée pour des tâches de compréhension et de génération complètes. Le modèle utilise des couches d'embedding distinctes pour le texte et les images. Les tokens textuels sont convertis en vecteurs denses, tandis que les images sont traitées via un modèle de vision CLIP pour extraire des embeddings de caractéristiques. Ces embeddings d'image sont ensuite projetés pour correspondre aux dimensions des embeddings textuels, garantissant qu'ils puissent être intégrés de manière fluide.

## Intégration des embeddings texte et image

Des tokens spéciaux dans la séquence textuelle indiquent où les embeddings d'image doivent être insérés. Pendant le traitement, ces tokens spéciaux sont remplacés par les embeddings d'image correspondants, permettant au modèle de gérer le texte et les images comme une seule séquence. Le prompt pour notre jeu de données est formaté en utilisant le token spécial <|image|> comme suit :

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Exemple de code
- [Script d'entraînement Phi-3-Vision](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Exemple de walkthrough Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions de garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.