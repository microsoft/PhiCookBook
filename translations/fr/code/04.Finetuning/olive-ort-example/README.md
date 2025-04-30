<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T03:57:48+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "fr"
}
-->
# Affiner Phi3 avec Olive

Dans cet exemple, vous utiliserez Olive pour :

1. Affiner un adaptateur LoRA afin de classer des phrases en Sad, Joy, Fear, Surprise.
1. Fusionner les poids de l'adaptateur avec le modèle de base.
1. Optimiser et quantifier le modèle dans `int4`.

Nous vous montrerons également comment effectuer des inférences avec le modèle affiné en utilisant l'API Generate de ONNX Runtime (ORT).

> **⚠️ Pour l'affinage, vous devrez disposer d'un GPU adapté, comme un A10, V100, ou A100.**

## 💾 Installation

Créez un nouvel environnement virtuel Python (par exemple, en utilisant `conda`) :

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ensuite, installez Olive et les dépendances nécessaires au workflow d'affinage :

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Affiner Phi3 avec Olive
Le [fichier de configuration Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contient un *workflow* avec les *passes* suivantes :

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

À un niveau élevé, ce workflow permet de :

1. Affiner Phi3 (pendant 150 étapes, modifiables) en utilisant les données du fichier [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fusionner les poids de l'adaptateur LoRA avec le modèle de base. Cela vous donnera un artefact de modèle unique au format ONNX.
1. Model Builder optimisera le modèle pour ONNX Runtime *et* le quantifiera dans `int4`.

Pour exécuter le workflow, lancez :

```bash
olive run --config phrase-classification.json
```

Une fois Olive terminé, votre modèle Phi3 affiné et optimisé `int4` sera disponible ici : `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Intégrer Phi3 affiné dans votre application 

Pour exécuter l'application :

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La réponse devrait être une classification en un mot de la phrase (Sad/Joy/Fear/Surprise).

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.