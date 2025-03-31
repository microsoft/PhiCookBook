<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T03:39:24+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "fr"
}
-->
# Ajuster Phi3 avec Olive

Dans cet exemple, vous utiliserez Olive pour :

1. Ajuster un adaptateur LoRA afin de classifier des phrases en Tristesse, Joie, Peur, Surprise.
1. Fusionner les poids de l'adaptateur avec le modèle de base.
1. Optimiser et quantifier le modèle dans `int4`.

Nous vous montrerons également comment effectuer une inférence avec le modèle ajusté en utilisant l'API Generate d'ONNX Runtime (ORT).

> **⚠️ Pour l'ajustement, vous devrez disposer d'un GPU adapté - par exemple, un A10, V100, A100.**

## 💾 Installation

Créez un nouvel environnement virtuel Python (par exemple, en utilisant `conda`) :

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ensuite, installez Olive et les dépendances nécessaires pour un flux de travail d'ajustement :

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajuster Phi3 avec Olive

Le [fichier de configuration Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contient un *flux de travail* avec les *étapes* suivantes :

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

À un niveau élevé, ce flux de travail effectuera les actions suivantes :

1. Ajuster Phi3 (pendant 150 étapes, que vous pouvez modifier) en utilisant les données du fichier [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fusionner les poids de l'adaptateur LoRA avec le modèle de base. Cela produira un artefact de modèle unique au format ONNX.
1. Model Builder optimisera le modèle pour l'exécution avec ONNX runtime *et* le quantifiera dans `int4`.

Pour exécuter le flux de travail, lancez :

```bash
olive run --config phrase-classification.json
```

Une fois Olive terminé, votre modèle Phi3 ajusté et optimisé `int4` sera disponible dans : `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Intégrer Phi3 ajusté dans votre application 

Pour exécuter l'application :

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La réponse devrait être une classification en un mot de la phrase (Tristesse/Joie/Peur/Surprise).

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.