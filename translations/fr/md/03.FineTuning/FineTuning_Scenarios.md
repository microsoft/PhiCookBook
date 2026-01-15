<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-07-17T08:21:49+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "fr"
}
-->
## Scénarios de Fine Tuning

![FineTuning with MS Services](../../../../translated_images/fr/FinetuningwithMS.3d0cec8ae693e094.png)

**Plateforme** Cela inclut diverses technologies telles que Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito et ONNX Runtime.

**Infrastructure** Cela comprend le CPU et le FPGA, qui sont essentiels pour le processus de fine-tuning. Laissez-moi vous montrer les icônes de chacune de ces technologies.

**Outils & Framework** Cela inclut ONNX Runtime et ONNX Runtime. Laissez-moi vous montrer les icônes de chacune de ces technologies.  
[Insérer les icônes pour ONNX Runtime et ONNX Runtime]

Le processus de fine-tuning avec les technologies Microsoft implique plusieurs composants et outils. En comprenant et en utilisant ces technologies, nous pouvons affiner efficacement nos applications et créer de meilleures solutions.

## Modèle en tant que Service

Affinez le modèle en utilisant le fine-tuning hébergé, sans avoir besoin de créer et gérer des ressources de calcul.

![MaaS Fine Tuning](../../../../translated_images/fr/MaaSfinetune.3eee4630607aff0d.png)

Le fine-tuning serverless est disponible pour les modèles Phi-3-mini et Phi-3-medium, permettant aux développeurs de personnaliser rapidement et facilement les modèles pour des scénarios cloud et edge sans avoir à gérer les ressources de calcul. Nous avons également annoncé que Phi-3-small est désormais disponible via notre offre Models-as-a-Service, permettant aux développeurs de démarrer rapidement et facilement le développement IA sans avoir à gérer l’infrastructure sous-jacente.

## Modèle en tant que Plateforme

Les utilisateurs gèrent leur propre infrastructure de calcul afin d’affiner leurs modèles.

![Maap Fine Tuning](../../../../translated_images/fr/MaaPFinetune.fd3829c1122f5d1c.png)

[Exemple de Fine Tuning](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Scénarios de Fine Tuning

| | | | | | | |
|-|-|-|-|-|-|-|
|Scénario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Adapter des LLM pré-entraînés à des tâches ou domaines spécifiques|Oui|Oui|Oui|Oui|Oui|Oui|
|Fine-tuning pour des tâches NLP telles que classification de texte, reconnaissance d’entités nommées et traduction automatique|Oui|Oui|Oui|Oui|Oui|Oui|
|Fine-tuning pour des tâches de QA|Oui|Oui|Oui|Oui|Oui|Oui|
|Fine-tuning pour générer des réponses humaines dans les chatbots|Oui|Oui|Oui|Oui|Oui|Oui|
|Fine-tuning pour générer de la musique, de l’art ou d’autres formes de créativité|Oui|Oui|Oui|Oui|Oui|Oui|
|Réduction des coûts computationnels et financiers|Oui|Oui|Non|Oui|Oui|Non|
|Réduction de l’utilisation mémoire|Non|Oui|Non|Oui|Oui|Oui|
|Utilisation de moins de paramètres pour un fine-tuning efficace|Non|Oui|Oui|Non|Non|Oui|
|Forme de parallélisme des données économe en mémoire donnant accès à la mémoire GPU agrégée de tous les dispositifs GPU disponibles|Non|Non|Non|Oui|Oui|Oui|

## Exemples de Performance de Fine Tuning

![Finetuning Performance](../../../../translated_images/fr/Finetuningexamples.a9a41214f8f5afc1.png)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.