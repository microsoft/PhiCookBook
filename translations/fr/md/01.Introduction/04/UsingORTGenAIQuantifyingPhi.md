## **Comment utiliser Model Builder pour quantifier Phi-3.5**

Model Builder prend désormais en charge la quantification des modèles ONNX pour Phi-3.5 Instruct et Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Conversion accélérée CPU en INT4 quantifié**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversion accélérée CUDA en INT4 quantifié**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configurez l’environnement dans le terminal

```bash

mkdir models

cd models 

```

2. Téléchargez microsoft/Phi-3.5-vision-instruct dans le dossier models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Veuillez télécharger ces fichiers dans votre dossier Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Téléchargez ce fichier dans le dossier models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Ouvrez le terminal

    Convertissez le modèle ONNX avec support FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Note :**

1. Model Builder prend actuellement en charge la conversion de Phi-3.5-Instruct et Phi-3.5-Vision, mais pas Phi-3.5-MoE.

2. Pour utiliser le modèle quantifié ONNX, vous pouvez le faire via le SDK Generative AI extensions for onnxruntime.

3. Il est important de considérer une IA plus responsable, donc après la conversion de quantification du modèle, il est recommandé de réaliser des tests de résultats plus approfondis.

4. En quantifiant le modèle CPU INT4, nous pouvons le déployer sur des appareils Edge, ce qui offre de meilleures opportunités d’application. Ainsi, nous avons finalisé Phi-3.5-Instruct autour de INT4.

## **Ressources**

1. En savoir plus sur Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Dépôt GitHub de Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.