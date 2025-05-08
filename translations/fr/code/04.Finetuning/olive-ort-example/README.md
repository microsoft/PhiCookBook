<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-07T15:15:04+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "fr"
}
-->
# Affiner Phi3 avec Olive

Dans cet exemple, vous utiliserez Olive pour :

1. Affiner un adaptateur LoRA afin de classer des phrases en Tristesse, Joie, Peur, Surprise.
1. Fusionner les poids de l’adaptateur dans le modèle de base.
1. Optimiser et quantifier le modèle en `int4`.

Nous vous montrerons également comment effectuer une inférence avec le modèle affiné en utilisant l’API Generate d’ONNX Runtime (ORT).

> **⚠️ Pour l’affinage, vous devez disposer d’un GPU adapté - par exemple, un A10, V100, A100.**

## 💾 Installation

Créez un nouvel environnement virtuel Python (par exemple, avec `conda`) :

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ensuite, installez Olive et les dépendances nécessaires pour un workflow d’affinage :

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Affiner Phi3 avec Olive
Le [fichier de configuration Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contient un *workflow* avec les *étapes* suivantes :

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

De manière générale, ce workflow va :

1. Affiner Phi3 (pendant 150 étapes, modifiables) en utilisant les données de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fusionner les poids de l’adaptateur LoRA dans le modèle de base. Cela vous donnera un seul artefact modèle au format ONNX.
1. Model Builder optimisera le modèle pour l’exécution ONNX *et* quantifiera le modèle en `int4`.

Pour lancer le workflow, exécutez :

```bash
olive run --config phrase-classification.json
```

Une fois Olive terminé, votre modèle Phi3 affiné optimisé en `int4` est disponible dans : `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Intégrer Phi3 affiné dans votre application

Pour lancer l’application :

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La réponse doit être une classification en un seul mot de la phrase (Tristesse/Joie/Peur/Surprise).

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant foi. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.