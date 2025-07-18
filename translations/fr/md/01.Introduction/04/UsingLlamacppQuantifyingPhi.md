<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:05:24+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "fr"
}
-->
# **Quantification de la famille Phi avec llama.cpp**

## **Qu'est-ce que llama.cpp**

llama.cpp est une bibliothèque logicielle open-source principalement écrite en C++ qui réalise l'inférence sur divers grands modèles de langage (LLM), comme Llama. Son objectif principal est d'offrir des performances de pointe pour l'inférence LLM sur une large gamme de matériels avec une configuration minimale. De plus, des liaisons Python sont disponibles pour cette bibliothèque, offrant une API de haut niveau pour la complétion de texte ainsi qu’un serveur web compatible OpenAI.

Le but principal de llama.cpp est de permettre l'inférence LLM avec une configuration minimale et des performances de pointe sur une grande variété de matériels, localement ou dans le cloud.

- Implémentation pure en C/C++ sans aucune dépendance
- Apple silicon est pleinement pris en charge - optimisé via ARM NEON, Accelerate et Metal
- Support AVX, AVX2 et AVX512 pour architectures x86
- Quantification entière en 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit et 8-bit pour une inférence plus rapide et une utilisation mémoire réduite
- Kernels CUDA personnalisés pour exécuter les LLM sur GPU NVIDIA (support des GPU AMD via HIP)
- Support des backends Vulkan et SYCL
- Inférence hybride CPU+GPU pour accélérer partiellement les modèles plus grands que la capacité totale de VRAM

## **Quantification de Phi-3.5 avec llama.cpp**

Le modèle Phi-3.5-Instruct peut être quantifié avec llama.cpp, mais Phi-3.5-Vision et Phi-3.5-MoE ne sont pas encore pris en charge. Le format converti par llama.cpp est gguf, qui est également le format de quantification le plus utilisé.

Il existe un grand nombre de modèles quantifiés au format GGUF sur Hugging Face. AI Foundry, Ollama et LlamaEdge s’appuient sur llama.cpp, donc les modèles GGUF sont également fréquemment utilisés.

### **Qu'est-ce que GGUF**

GGUF est un format binaire optimisé pour un chargement et une sauvegarde rapides des modèles, ce qui le rend très efficace pour l’inférence. GGUF est conçu pour être utilisé avec GGML et d’autres moteurs d’exécution. GGUF a été développé par @ggerganov, également créateur de llama.cpp, un framework populaire d’inférence LLM en C/C++. Les modèles initialement développés dans des frameworks comme PyTorch peuvent être convertis au format GGUF pour être utilisés avec ces moteurs.

### **ONNX vs GGUF**

ONNX est un format traditionnel de machine learning/deep learning, bien supporté dans différents frameworks IA et adapté à de nombreux cas d’usage sur des appareils embarqués. Quant à GGUF, il est basé sur llama.cpp et peut être considéré comme un format né à l’ère de la GenAI. Les deux ont des usages similaires. Si vous cherchez de meilleures performances sur du matériel embarqué et dans les couches applicatives, ONNX peut être votre choix. Si vous utilisez le framework dérivé et la technologie de llama.cpp, alors GGUF sera probablement plus adapté.

### **Quantification de Phi-3.5-Instruct avec llama.cpp**

**1. Configuration de l’environnement**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantification**

Conversion de Phi-3.5-Instruct en FP16 GGUF avec llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantification de Phi-3.5 en INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Tests**

Installation de llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Note*** 

Si vous utilisez Apple Silicon, veuillez installer llama-cpp-python de cette façon


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Tests


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Ressources**

1. En savoir plus sur llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. En savoir plus sur onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. En savoir plus sur GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.