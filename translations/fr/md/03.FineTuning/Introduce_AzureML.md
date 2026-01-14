<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:32:53+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "fr"
}
-->
# **Présentation du service Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) est un service cloud conçu pour accélérer et gérer le cycle de vie des projets de machine learning (ML).

Les professionnels du ML, les data scientists et les ingénieurs peuvent l’utiliser dans leurs flux de travail quotidiens pour :

- Entraîner et déployer des modèles.  
- Gérer les opérations de machine learning (MLOps).  
- Vous pouvez créer un modèle dans Azure Machine Learning ou utiliser un modèle développé à partir d’une plateforme open source, comme PyTorch, TensorFlow ou scikit-learn.  
- Les outils MLOps vous aident à surveiller, réentraîner et redéployer les modèles.

## À qui s’adresse Azure Machine Learning ?

**Data Scientists et Ingénieurs ML**

Ils peuvent utiliser des outils pour accélérer et automatiser leurs tâches quotidiennes.  
Azure ML offre des fonctionnalités pour l’équité, l’explicabilité, le suivi et l’auditabilité.

**Développeurs d’applications**  
Ils peuvent intégrer les modèles dans des applications ou services de manière fluide.

**Développeurs de plateformes**

Ils ont accès à un ensemble robuste d’outils soutenus par des API durables d’Azure Resource Manager.  
Ces outils permettent de construire des solutions ML avancées.

**Entreprises**

En travaillant dans le cloud Microsoft Azure, les entreprises bénéficient d’une sécurité familière et d’un contrôle d’accès basé sur les rôles.  
Elles peuvent configurer des projets pour contrôler l’accès aux données protégées et aux opérations spécifiques.

## Productivité pour toute l’équipe  
Les projets ML nécessitent souvent une équipe aux compétences variées pour construire et maintenir les solutions.

Azure ML fournit des outils qui vous permettent de :  
- Collaborer avec votre équipe via des notebooks partagés, des ressources de calcul, du calcul sans serveur, des données et des environnements.  
- Développer des modèles avec équité, explicabilité, suivi et auditabilité pour répondre aux exigences de traçabilité et de conformité.  
- Déployer rapidement et facilement des modèles ML à grande échelle, et les gérer efficacement avec MLOps.  
- Exécuter des charges de travail de machine learning partout avec une gouvernance, une sécurité et une conformité intégrées.

## Outils multiplateformes compatibles

Chaque membre de l’équipe ML peut utiliser ses outils préférés pour accomplir ses tâches.  
Que vous réalisiez des expériences rapides, un réglage d’hyperparamètres, la construction de pipelines ou la gestion des inférences, vous pouvez utiliser des interfaces familières telles que :  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST APIs

Au fur et à mesure que vous affinez les modèles et collaborez tout au long du cycle de développement, vous pouvez partager et retrouver des ressources, des actifs et des métriques dans l’interface Azure Machine Learning studio.

## **LLM/SLM dans Azure ML**

Azure ML a intégré de nombreuses fonctions liées aux LLM/SLM, combinant LLMOps et SLMOps pour créer une plateforme technologique d’intelligence artificielle générative à l’échelle de l’entreprise.

### **Catalogue de modèles**

Les utilisateurs d’entreprise peuvent déployer différents modèles selon les scénarios métier via le Catalogue de modèles, et fournir des services sous forme de Model as Service pour que les développeurs ou utilisateurs d’entreprise y accèdent.

![models](../../../../translated_images/fr/models.e6c7ff50a51806fd.png)

Le Catalogue de modèles dans Azure Machine Learning studio est le centre pour découvrir et utiliser une large gamme de modèles permettant de construire des applications d’IA générative. Le catalogue propose des centaines de modèles provenant de fournisseurs tels que Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, ainsi que des modèles entraînés par Microsoft. Les modèles provenant de fournisseurs autres que Microsoft sont des Produits Non-Microsoft, tels que définis dans les Conditions d’utilisation des produits Microsoft, et soumis aux conditions associées au modèle.

### **Pipeline de tâches**

Le cœur d’un pipeline de machine learning consiste à diviser une tâche complète en un flux de travail en plusieurs étapes. Chaque étape est un composant gérable qui peut être développé, optimisé, configuré et automatisé individuellement. Les étapes sont reliées par des interfaces bien définies. Le service de pipeline Azure Machine Learning orchestre automatiquement toutes les dépendances entre les étapes.

Lors du fine-tuning de SLM / LLM, nous pouvons gérer nos données, l’entraînement et les processus de génération via Pipeline.

![finetuning](../../../../translated_images/fr/finetuning.6559da198851fa52.png)

### **Prompt flow**

Avantages de l’utilisation d’Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow offre plusieurs avantages qui aident les utilisateurs à passer de l’idéation à l’expérimentation, puis à des applications LLM prêtes pour la production :

**Agilité en ingénierie des prompts**

Expérience d’écriture interactive : Azure Machine Learning prompt flow fournit une représentation visuelle de la structure du flux, permettant aux utilisateurs de comprendre et naviguer facilement dans leurs projets. Il offre également une expérience de codage similaire à un notebook pour un développement et un débogage efficaces.  
Variantes pour l’ajustement des prompts : les utilisateurs peuvent créer et comparer plusieurs variantes de prompts, facilitant un processus d’affinement itératif.

Évaluation : des flux d’évaluation intégrés permettent aux utilisateurs d’évaluer la qualité et l’efficacité de leurs prompts et flux.

Ressources complètes : Azure Machine Learning prompt flow inclut une bibliothèque d’outils intégrés, d’exemples et de modèles qui servent de point de départ au développement, stimulant la créativité et accélérant le processus.

**Prêt pour l’entreprise pour les applications basées sur LLM**

Collaboration : Azure Machine Learning prompt flow supporte la collaboration en équipe, permettant à plusieurs utilisateurs de travailler ensemble sur des projets d’ingénierie des prompts, de partager leurs connaissances et de maintenir le contrôle des versions.

Plateforme tout-en-un : Azure Machine Learning prompt flow simplifie l’ensemble du processus d’ingénierie des prompts, du développement et de l’évaluation au déploiement et à la surveillance. Les utilisateurs peuvent déployer facilement leurs flux en tant que points de terminaison Azure Machine Learning et suivre leurs performances en temps réel, garantissant un fonctionnement optimal et une amélioration continue.

Solutions de préparation entreprise Azure Machine Learning : Prompt flow s’appuie sur les solutions robustes de préparation entreprise d’Azure Machine Learning, offrant une base sécurisée, évolutive et fiable pour le développement, l’expérimentation et le déploiement des flux.

Avec Azure Machine Learning prompt flow, les utilisateurs peuvent libérer leur agilité en ingénierie des prompts, collaborer efficacement et tirer parti de solutions de niveau entreprise pour réussir le développement et le déploiement d’applications basées sur LLM.

En combinant la puissance de calcul, les données et les différents composants d’Azure ML, les développeurs d’entreprise peuvent facilement créer leurs propres applications d’intelligence artificielle.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.