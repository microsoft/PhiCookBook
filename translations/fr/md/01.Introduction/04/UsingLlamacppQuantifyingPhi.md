<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e5bb9190ef9d149d28037a768c6b62b2",
  "translation_date": "2025-03-27T08:35:09+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingLlamacppQuantifyingPhi.md",
  "language_code": "fr"
}
-->
# **Quantification de la famille Phi avec llama.cpp**

## **Qu'est-ce que llama.cpp**

llama.cpp est une bibliothèque logicielle open-source principalement écrite en C++ qui réalise des inférences sur divers modèles de langage à grande échelle (LLMs), tels que Llama. Son objectif principal est d'offrir des performances de pointe pour l'inférence de LLM sur une large gamme de matériel avec une configuration minimale. De plus, des liaisons Python sont disponibles pour cette bibliothèque, fournissant une API de haut niveau pour la complétion de texte et un serveur web compatible OpenAI.

Le principal objectif de llama.cpp est de permettre l'inférence des LLM avec une configuration minimale et des performances de pointe sur une grande variété de matériels - localement et dans le cloud.

- Implémentation en C/C++ sans dépendances
- Les puces Apple sont des citoyens de première classe - optimisées via ARM NEON, Accelerate et Metal frameworks
- Support AVX, AVX2 et AVX512 pour les architectures x86
- Quantification entière en 1,5 bits, 2 bits, 3 bits, 4 bits, 5 bits, 6 bits et 8 bits pour une inférence plus rapide et une utilisation réduite de la mémoire
- Noyaux CUDA personnalisés pour exécuter des LLM sur des GPU NVIDIA (support pour les GPU AMD via HIP)
- Support des backends Vulkan et SYCL
- Inférence hybride CPU+GPU pour accélérer partiellement les modèles plus grands que la capacité totale de VRAM

## **Quantification de Phi-3.5 avec llama.cpp**

Le modèle Phi-3.5-Instruct peut être quantifié en utilisant llama.cpp, mais Phi-3.5-Vision et Phi-3.5-MoE ne sont pas encore pris en charge. Le format converti par llama.cpp est gguf, qui est également le format de quantification le plus largement utilisé.

Il existe un grand nombre de modèles au format GGUF quantifiés sur Hugging Face. AI Foundry, Ollama et LlamaEdge s'appuient sur llama.cpp, ce qui fait que les modèles GGUF sont également souvent utilisés.

### **Qu'est-ce que GGUF**

GGUF est un format binaire optimisé pour un chargement et une sauvegarde rapides des modèles, ce qui le rend très efficace pour les inférences. GGUF est conçu pour être utilisé avec GGML et d'autres exécutants. GGUF a été développé par @ggerganov, qui est également le créateur de llama.cpp, un framework populaire d'inférence LLM en C/C++. Les modèles initialement développés dans des frameworks comme PyTorch peuvent être convertis au format GGUF pour être utilisés avec ces moteurs.

### **ONNX vs GGUF**

ONNX est un format traditionnel de machine learning/deep learning, bien pris en charge par différents frameworks d'IA et offrant de bons scénarios d'utilisation sur des appareils périphériques. Quant à GGUF, il est basé sur llama.cpp et peut être considéré comme un produit de l'ère GenAI. Les deux ont des usages similaires. Si vous recherchez de meilleures performances sur du matériel embarqué et dans les couches applicatives, ONNX pourrait être votre choix. Si vous utilisez le framework dérivé et la technologie de llama.cpp, alors GGUF pourrait être préférable.

### **Quantification de Phi-3.5-Instruct avec llama.cpp**

**1. Configuration de l'environnement**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantification**

Utilisation de llama.cpp pour convertir Phi-3.5-Instruct en FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantification de Phi-3.5 en INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Tests**

Installer llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Note*** 

Si vous utilisez une puce Apple, installez llama-cpp-python comme suit


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Tests 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Ressources**

1. En savoir plus sur llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. En savoir plus sur GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.