<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-03-27T07:52:15+00:00",
  "source_file": "md\\01.Introduction\\03\\overview.md",
  "language_code": "fr"
}
-->
Dans le contexte de Phi-3-mini, l'inférence fait référence au processus d'utilisation du modèle pour effectuer des prédictions ou générer des résultats basés sur des données d'entrée. Voici plus de détails sur Phi-3-mini et ses capacités d'inférence.

Phi-3-mini fait partie de la série de modèles Phi-3 publiée par Microsoft. Ces modèles sont conçus pour redéfinir ce qui est possible avec les Small Language Models (SLMs).

Voici quelques points clés concernant Phi-3-mini et ses capacités d'inférence :

## **Présentation de Phi-3-mini :**
- Phi-3-mini possède une taille de paramètre de 3,8 milliards.
- Il peut fonctionner non seulement sur des dispositifs informatiques traditionnels, mais aussi sur des dispositifs en périphérie tels que les appareils mobiles et les dispositifs IoT.
- La sortie de Phi-3-mini permet aux particuliers et aux entreprises de déployer des SLMs sur différents dispositifs matériels, notamment dans des environnements aux ressources limitées.
- Il prend en charge divers formats de modèles, notamment le format PyTorch traditionnel, la version quantifiée du format gguf et la version quantifiée basée sur ONNX.

## **Accéder à Phi-3-mini :**
Pour accéder à Phi-3-mini, vous pouvez utiliser [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) dans une application Copilot. Semantic Kernel est généralement compatible avec Azure OpenAI Service, les modèles open source sur Hugging Face, et les modèles locaux.  
Vous pouvez également utiliser [Ollama](https://ollama.com) ou [LlamaEdge](https://llamaedge.com) pour appeler des modèles quantifiés. Ollama permet aux utilisateurs individuels d'utiliser différents modèles quantifiés, tandis que LlamaEdge offre une disponibilité multiplateforme pour les modèles GGUF.

## **Modèles quantifiés :**
De nombreux utilisateurs préfèrent utiliser des modèles quantifiés pour l'inférence locale. Par exemple, vous pouvez exécuter directement Ollama run Phi-3 ou le configurer hors ligne à l'aide d'un Modelfile. Le Modelfile spécifie le chemin du fichier GGUF et le format de l'invite.

## **Possibilités de l'IA générative :**
La combinaison de SLMs comme Phi-3-mini ouvre de nouvelles possibilités pour l'IA générative. L'inférence n'est que la première étape ; ces modèles peuvent être utilisés pour diverses tâches dans des scénarios contraints par les ressources, la latence et les coûts.

## **Libérer le potentiel de l'IA générative avec Phi-3-mini : Un guide sur l'inférence et le déploiement**  
Apprenez à utiliser Semantic Kernel, Ollama/LlamaEdge et ONNX Runtime pour accéder aux modèles Phi-3-mini et les inférer, tout en explorant les possibilités de l'IA générative dans divers scénarios d'application.

**Fonctionnalités**  
Inférence du modèle Phi-3-mini dans :

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

En résumé, Phi-3-mini permet aux développeurs d'explorer différents formats de modèles et de tirer parti de l'IA générative dans divers scénarios d'application.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction par IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.