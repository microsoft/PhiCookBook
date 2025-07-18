<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:04:28+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "fr"
}
-->
# Vue d'ensemble du projet Phi-3-Vision-128K-Instruct

## Le modèle

Le Phi-3-Vision-128K-Instruct, un modèle multimodal léger et à la pointe de la technologie, est au cœur de ce projet. Il fait partie de la famille de modèles Phi-3 et supporte une longueur de contexte allant jusqu'à 128 000 tokens. Le modèle a été entraîné sur un ensemble de données diversifié incluant des données synthétiques et des sites web publics soigneusement filtrés, mettant l'accent sur un contenu de haute qualité et nécessitant un raisonnement poussé. Le processus d'entraînement a inclus un affinage supervisé et une optimisation directe des préférences pour garantir une adhérence précise aux instructions, ainsi que des mesures de sécurité robustes.

## La création de données d'exemple est cruciale pour plusieurs raisons :

1. **Tests** : Les données d'exemple permettent de tester votre application dans divers scénarios sans affecter les données réelles. Ceci est particulièrement important lors des phases de développement et de préproduction.

2. **Optimisation des performances** : Avec des données d'exemple qui imitent l’échelle et la complexité des données réelles, vous pouvez identifier les goulets d’étranglement en termes de performance et optimiser votre application en conséquence.

3. **Prototypage** : Les données d'exemple peuvent être utilisées pour créer des prototypes et des maquettes, ce qui aide à mieux comprendre les besoins des utilisateurs et à recueillir des retours.

4. **Analyse de données** : En science des données, les données d'exemple sont souvent utilisées pour l’analyse exploratoire, l’entraînement de modèles et le test d’algorithmes.

5. **Sécurité** : Utiliser des données d'exemple dans les environnements de développement et de test peut aider à prévenir les fuites accidentelles de données sensibles réelles.

6. **Apprentissage** : Si vous apprenez une nouvelle technologie ou un nouvel outil, travailler avec des données d'exemple offre une manière pratique d’appliquer ce que vous avez appris.

Gardez à l’esprit que la qualité de vos données d'exemple peut avoir un impact significatif sur ces activités. Elles doivent être aussi proches que possible des données réelles en termes de structure et de variabilité.

### Création de données d'exemple
[Generate DataSet Script](./CreatingSampleData.md)

## Jeu de données

Un bon exemple de jeu de données d'exemple est le [jeu de données DBQ/Burberry.Product.prices.United.States](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponible sur Huggingface).  
Le jeu de données d'exemple des produits Burberry comprend des métadonnées sur la catégorie des produits, le prix et le titre, avec un total de 3 040 lignes, chacune représentant un produit unique. Ce jeu de données nous permet de tester la capacité du modèle à comprendre et interpréter des données visuelles, en générant un texte descriptif qui capture des détails visuels complexes et des caractéristiques spécifiques à la marque.

**Note :** Vous pouvez utiliser n’importe quel jeu de données incluant des images.

## Raisonnement complexe

Le modèle doit raisonner sur les prix et les noms en se basant uniquement sur l’image. Cela nécessite que le modèle reconnaisse non seulement les caractéristiques visuelles, mais comprenne aussi leurs implications en termes de valeur du produit et de branding. En synthétisant des descriptions textuelles précises à partir des images, le projet met en lumière le potentiel d’intégration des données visuelles pour améliorer la performance et la polyvalence des modèles dans des applications réelles.

## Architecture Phi-3 Vision

L’architecture du modèle est une version multimodale d’un Phi-3. Il traite à la fois les données textuelles et visuelles, intégrant ces entrées dans une séquence unifiée pour des tâches de compréhension et de génération complètes. Le modèle utilise des couches d’embedding distinctes pour le texte et les images. Les tokens textuels sont convertis en vecteurs denses, tandis que les images sont traitées via un modèle de vision CLIP pour extraire des embeddings de caractéristiques. Ces embeddings d’images sont ensuite projetés pour correspondre aux dimensions des embeddings textuels, assurant une intégration fluide.

## Intégration des embeddings texte et image

Des tokens spéciaux dans la séquence textuelle indiquent où insérer les embeddings d’images. Lors du traitement, ces tokens spéciaux sont remplacés par les embeddings d’images correspondants, permettant au modèle de gérer texte et images comme une séquence unique. Le prompt pour notre jeu de données est formaté en utilisant le token spécial <|image|> comme suit :

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Exemple de code
- [Script d’entraînement Phi-3-Vision](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Exemple de walkthrough Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.