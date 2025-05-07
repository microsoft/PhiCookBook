<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-07T13:28:35+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "fr"
}
-->
# Vue d'ensemble du projet Phi-3-Vision-128K-Instruct

## Le modèle

Le Phi-3-Vision-128K-Instruct, un modèle multimodal léger et à la pointe de la technologie, est au cœur de ce projet. Il fait partie de la famille de modèles Phi-3 et supporte une longueur de contexte allant jusqu’à 128 000 tokens. Le modèle a été entraîné sur un ensemble de données diversifié incluant des données synthétiques et des sites web publics soigneusement filtrés, mettant l’accent sur du contenu de haute qualité et nécessitant un raisonnement poussé. Le processus d’entraînement a inclus un affinage supervisé et une optimisation directe des préférences pour garantir une précision rigoureuse dans le respect des instructions, ainsi que des mesures de sécurité robustes.

## Pourquoi la création de données d’exemple est-elle cruciale ?

1. **Tests** : Les données d’exemple permettent de tester votre application dans différents scénarios sans affecter les données réelles. Cela est particulièrement important lors des phases de développement et de préproduction.

2. **Optimisation des performances** : Avec des données d’exemple qui reproduisent l’échelle et la complexité des données réelles, vous pouvez identifier les goulots d’étranglement et optimiser votre application en conséquence.

3. **Prototypage** : Les données d’exemple peuvent être utilisées pour créer des prototypes et des maquettes, ce qui aide à mieux comprendre les besoins des utilisateurs et à recueillir des retours.

4. **Analyse des données** : En science des données, les données d’exemple sont souvent utilisées pour l’analyse exploratoire, l’entraînement de modèles et le test d’algorithmes.

5. **Sécurité** : Utiliser des données d’exemple dans les environnements de développement et de test permet d’éviter les fuites accidentelles de données sensibles réelles.

6. **Apprentissage** : Si vous apprenez une nouvelle technologie ou un nouvel outil, travailler avec des données d’exemple offre un moyen pratique d’appliquer vos connaissances.

Gardez à l’esprit que la qualité de vos données d’exemple peut avoir un impact significatif sur ces activités. Elles doivent être aussi proches que possible des données réelles en termes de structure et de variabilité.

### Création de données d’exemple
[Generate DataSet Script](./CreatingSampleData.md)

## Jeu de données

Un bon exemple de jeu de données d’exemple est le [jeu de données DBQ/Burberry.Product.prices.United.States](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponible sur Huggingface).  
Le jeu de données d’exemple des produits Burberry avec les métadonnées sur la catégorie, le prix et le titre des produits comprend un total de 3 040 lignes, chacune représentant un produit unique. Ce jeu de données nous permet de tester la capacité du modèle à comprendre et interpréter les données visuelles, en générant des textes descriptifs qui capturent les détails visuels complexes et les caractéristiques spécifiques à la marque.

**Note :** Vous pouvez utiliser n’importe quel jeu de données incluant des images.

## Raisonnement complexe

Le modèle doit raisonner sur les prix et les noms à partir de l’image seule. Cela nécessite que le modèle reconnaisse non seulement les caractéristiques visuelles, mais aussi comprenne leurs implications en termes de valeur produit et d’image de marque. En synthétisant des descriptions textuelles précises à partir des images, le projet met en avant le potentiel de l’intégration des données visuelles pour améliorer la performance et la polyvalence des modèles dans des applications concrètes.

## Architecture Phi-3 Vision

L’architecture du modèle est une version multimodale d’un Phi-3. Il traite à la fois les données textuelles et visuelles, intégrant ces entrées en une séquence unifiée pour des tâches de compréhension et de génération complètes. Le modèle utilise des couches d’embedding distinctes pour le texte et les images. Les tokens textuels sont convertis en vecteurs denses, tandis que les images sont traitées via un modèle de vision CLIP pour extraire des embeddings de caractéristiques. Ces embeddings d’images sont ensuite projetés pour correspondre aux dimensions des embeddings textuels, garantissant une intégration fluide.

## Intégration des embeddings texte et image

Des tokens spéciaux dans la séquence textuelle indiquent où insérer les embeddings d’image. Lors du traitement, ces tokens spéciaux sont remplacés par les embeddings d’image correspondants, permettant au modèle de gérer texte et images comme une seule séquence. Le prompt pour notre jeu de données est formaté en utilisant le token spécial <|image|> comme suit :

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Exemple de code
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Exemple de tutoriel Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.