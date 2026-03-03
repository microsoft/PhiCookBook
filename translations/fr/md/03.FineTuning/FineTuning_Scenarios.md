## Scénarios de Raffinage

![FineTuning with MS Services](../../../../translated_images/fr/FinetuningwithMS.3d0cec8ae693e094.webp)

Cette section offre un aperçu des scénarios de raffinage dans les environnements Microsoft Foundry et Azure, y compris les modèles de déploiement, les couches d'infrastructure et les techniques d'optimisation couramment utilisées.

**Plateforme**  
Cela inclut les services gérés tels que Microsoft Foundry (anciennement Azure AI Foundry) et Azure Machine Learning, qui fournissent la gestion des modèles, l'orchestration, le suivi des expériences et les flux de travail de déploiement.

**Infrastructure**  
Le raffinage nécessite des ressources de calcul évolutives. Dans les environnements Azure, cela comprend généralement des machines virtuelles basées sur GPU et des ressources CPU pour les charges de travail légères, ainsi qu'un stockage évolutif pour les ensembles de données et les points de contrôle.

**Outils & Framework**  
Les flux de travail de raffinage s'appuient couramment sur des frameworks et des bibliothèques d'optimisation tels que Hugging Face Transformers, DeepSpeed et PEFT (Parameter-Efficient Fine-Tuning).

Le processus de raffinage avec les technologies Microsoft couvre les services de plateforme, l'infrastructure de calcul et les frameworks d'entraînement. En comprenant comment ces composants fonctionnent ensemble, les développeurs peuvent adapter efficacement les modèles de base à des tâches spécifiques et à des scénarios de production.

## Modèle en tant que Service

Affinez le modèle en utilisant le raffinage hébergé, sans besoin de créer et gérer le calcul.

![MaaS Fine Tuning](../../../../translated_images/fr/MaaSfinetune.3eee4630607aff0d.webp)

Le raffinage sans serveur est désormais disponible pour les familles de modèles Phi-3, Phi-3.5 et Phi-4, permettant aux développeurs de personnaliser rapidement et facilement les modèles pour des scénarios cloud et périphériques sans avoir à gérer le calcul.

## Modèle en tant que Plateforme

Les utilisateurs gèrent leur propre calcul afin d’affiner leurs modèles.

![Maap Fine Tuning](../../../../translated_images/fr/MaaPFinetune.fd3829c1122f5d1c.webp)

[Exemple de raffinage](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Comparaison des Techniques de Raffinage

|Scénario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Adapter des LLM pré-entraînés à des tâches ou domaines spécifiques|Oui|Oui|Oui|Oui|Oui|Oui|
|Raffinage pour les tâches NLP telles que la classification de texte, la reconnaissance d’entités nommées et la traduction automatique|Oui|Oui|Oui|Oui|Oui|Oui|
|Raffinage pour les tâches de QA|Oui|Oui|Oui|Oui|Oui|Oui|
|Raffinage pour générer des réponses semblables à celles des humains pour les chatbots|Oui|Oui|Oui|Oui|Oui|Oui|
|Raffinage pour générer de la musique, de l’art ou d’autres formes de créativité|Oui|Oui|Oui|Oui|Oui|Oui|
|Réduction des coûts computationnels et financiers|Oui|Oui|Oui|Oui|Oui|Oui|
|Réduction de l'utilisation mémoire|Oui|Oui|Oui|Oui|Oui|Oui|
|Utilisation de moins de paramètres pour un raffinage efficace|Oui|Oui|Oui|Non|Non|Oui|
|Forme efficace en mémoire du parallélisme des données qui donne accès à la mémoire GPU agrégée de tous les dispositifs GPU disponibles|Non|Non|Non|Oui|Oui|Non|

> [!NOTE]
> LoRA, QLoRA, PEFT et DoRA sont des méthodes de raffinage efficaces en paramètres, tandis que DeepSpeed et ZeRO se concentrent sur l'entraînement distribué et l'optimisation de la mémoire.

## Exemples de Performance de Raffinage

![Finetuning Performance](../../../../translated_images/fr/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source officielle. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->