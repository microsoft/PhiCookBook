Dans le contexte de Phi-3-mini, l'inférence désigne le processus d'utilisation du modèle pour faire des prédictions ou générer des résultats à partir de données d'entrée. Permettez-moi de vous donner plus de détails sur Phi-3-mini et ses capacités d'inférence.

Phi-3-mini fait partie de la série Phi-3 de modèles lancés par Microsoft. Ces modèles sont conçus pour redéfinir ce qui est possible avec les Small Language Models (SLM).

Voici quelques points clés concernant Phi-3-mini et ses capacités d'inférence :

## **Présentation de Phi-3-mini :**
- Phi-3-mini compte 3,8 milliards de paramètres.
- Il peut fonctionner non seulement sur des appareils informatiques traditionnels, mais aussi sur des dispositifs edge tels que les appareils mobiles et les objets connectés (IoT).
- La sortie de Phi-3-mini permet aux particuliers et aux entreprises de déployer des SLM sur différents matériels, notamment dans des environnements aux ressources limitées.
- Il prend en charge plusieurs formats de modèles, y compris le format PyTorch traditionnel, la version quantifiée du format gguf, ainsi que la version quantifiée basée sur ONNX.

## **Accéder à Phi-3-mini :**
Pour accéder à Phi-3-mini, vous pouvez utiliser [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) dans une application Copilot. Semantic Kernel est généralement compatible avec Azure OpenAI Service, les modèles open source sur Hugging Face, ainsi que les modèles locaux.  
Vous pouvez également utiliser [Ollama](https://ollama.com) ou [LlamaEdge](https://llamaedge.com) pour appeler des modèles quantifiés. Ollama permet aux utilisateurs individuels d’appeler différents modèles quantifiés, tandis que LlamaEdge offre une disponibilité multiplateforme pour les modèles GGUF.

## **Modèles quantifiés :**
De nombreux utilisateurs préfèrent utiliser des modèles quantifiés pour l'inférence locale. Par exemple, vous pouvez directement exécuter Ollama run Phi-3 ou le configurer hors ligne à l’aide d’un Modelfile. Le Modelfile spécifie le chemin du fichier GGUF ainsi que le format du prompt.

## **Possibilités de l’IA générative :**
La combinaison de SLM comme Phi-3-mini ouvre de nouvelles perspectives pour l’IA générative. L’inférence n’est que la première étape ; ces modèles peuvent être utilisés pour diverses tâches dans des scénarios où les ressources, la latence et les coûts sont limités.

## **Déverrouiller l’IA générative avec Phi-3-mini : Guide d’inférence et de déploiement**  
Découvrez comment utiliser Semantic Kernel, Ollama/LlamaEdge et ONNX Runtime pour accéder aux modèles Phi-3-mini et effectuer des inférences, et explorez les possibilités de l’IA générative dans différents cas d’usage.

**Fonctionnalités**  
Inférence du modèle phi3-mini dans :

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

En résumé, Phi-3-mini permet aux développeurs d’explorer différents formats de modèles et de tirer parti de l’IA générative dans divers scénarios d’application.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.