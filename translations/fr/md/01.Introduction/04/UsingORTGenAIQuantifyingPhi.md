<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-03-27T08:41:18+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "fr"
}
-->
## **Quantification de la famille Phi avec les extensions d'IA générative pour onnxruntime**

## **Qu'est-ce que les extensions d'IA générative pour onnxruntime**

Ces extensions vous aident à exécuter de l'IA générative avec ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Elles fournissent une boucle d'IA générative pour les modèles ONNX, y compris l'inférence avec ONNX Runtime, le traitement des logits, la recherche et l'échantillonnage, ainsi que la gestion du cache KV. Les développeurs peuvent appeler une méthode generate() de haut niveau ou exécuter chaque itération du modèle dans une boucle, générant un token à la fois et, éventuellement, en mettant à jour les paramètres de génération dans la boucle. Elles prennent en charge les recherches gloutonnes (greedy/beam search) et l'échantillonnage TopP, TopK pour générer des séquences de tokens, ainsi que des traitements intégrés des logits comme les pénalités de répétition. Vous pouvez également ajouter facilement des scores personnalisés.

Au niveau de l'application, vous pouvez utiliser les extensions d'IA générative pour onnxruntime pour construire des applications en C++/C#/Python. Au niveau du modèle, vous pouvez les utiliser pour fusionner des modèles ajustés et effectuer des déploiements quantitatifs associés.

## **Quantification de Phi-3.5 avec les extensions d'IA générative pour onnxruntime**

### **Modèles pris en charge**

Les extensions d'IA générative pour onnxruntime prennent en charge la conversion quantifiée des modèles Microsoft Phi, Google Gemma, Mistral et Meta LLaMA.

### **Créateur de modèle dans les extensions d'IA générative pour onnxruntime**

Le créateur de modèle accélère considérablement la création de modèles ONNX optimisés et quantifiés qui fonctionnent avec l'API generate() d'ONNX Runtime.

Grâce au créateur de modèle, vous pouvez quantifier le modèle en INT4, INT8, FP16, FP32 et combiner différentes méthodes d'accélération matérielle telles que CPU, CUDA, DirectML, Mobile, etc.

Pour utiliser le créateur de modèle, vous devez installer :

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Après l'installation, vous pouvez exécuter le script du créateur de modèle depuis le terminal pour effectuer la conversion de format et de quantification du modèle.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Comprendre les paramètres pertinents :

1. **model_name** : Il s'agit du modèle sur Hugging Face, tel que microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. Cela peut aussi être le chemin où vous stockez le modèle.

2. **path_to_output_folder** : Chemin où enregistrer la conversion quantifiée.

3. **execution_provider** : Support pour différentes accélérations matérielles, telles que cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** : Nous téléchargeons le modèle depuis Hugging Face et le mettons en cache localement.

***Remarque :***

## **Comment utiliser le créateur de modèle pour quantifier Phi-3.5**

Le créateur de modèle prend désormais en charge la quantification des modèles ONNX pour Phi-3.5 Instruct et Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Conversion en INT4 accélérée par CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversion en INT4 accélérée par CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configurez l'environnement dans le terminal :

```bash

mkdir models

cd models 

```

2. Téléchargez microsoft/Phi-3.5-vision-instruct dans le dossier models :  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Téléchargez ces fichiers dans votre dossier Phi-3.5-vision-instruct :  

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Téléchargez ce fichier dans le dossier models :  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Dans le terminal :

    Convertissez le modèle ONNX avec support FP32 :

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Remarque :**

1. Le créateur de modèle prend actuellement en charge la conversion de Phi-3.5-Instruct et Phi-3.5-Vision, mais pas de Phi-3.5-MoE.

2. Pour utiliser le modèle quantifié d'ONNX, vous pouvez l'utiliser via le SDK des extensions d'IA générative pour onnxruntime.

3. Nous devons prendre en compte une IA plus responsable. Ainsi, après la conversion de quantification du modèle, il est recommandé de réaliser des tests de résultats plus efficaces.

4. En quantifiant le modèle CPU INT4, nous pouvons le déployer sur des appareils Edge, ce qui offre de meilleurs scénarios d'application. Nous avons donc finalisé Phi-3.5-Instruct en INT4.

## **Ressources**

1. En savoir plus sur les extensions d'IA générative pour onnxruntime :  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Dépôt GitHub des extensions d'IA générative pour onnxruntime :  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle effectuée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.