<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-07-16T22:35:01+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "fr"
}
-->
# **Présentation de Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) est un outil d’automatisation visuelle des workflows qui permet aux utilisateurs de créer des flux de travail automatisés en utilisant des modèles préconçus et des connecteurs personnalisés. Il est conçu pour permettre aux développeurs et aux analystes métier de construire rapidement des processus automatisés pour des tâches telles que la gestion des données, la collaboration et l’optimisation des processus. Avec Prompt Flow, les utilisateurs peuvent facilement connecter différents services, applications et systèmes, et automatiser des processus métier complexes.

Microsoft Prompt Flow est conçu pour simplifier le cycle de développement complet des applications d’IA basées sur les Large Language Models (LLMs). Que vous soyez en phase d’idéation, de prototypage, de test, d’évaluation ou de déploiement d’applications basées sur des LLM, Prompt Flow facilite le processus et vous permet de créer des applications LLM de qualité production.

## Voici les principales fonctionnalités et avantages de Microsoft Prompt Flow :

**Expérience d’édition interactive**

Prompt Flow offre une représentation visuelle de la structure de votre flux, ce qui facilite la compréhension et la navigation dans vos projets.  
Il propose une expérience de codage similaire à un notebook pour un développement et un débogage efficaces des flux.

**Variantes de prompts et ajustements**

Créez et comparez plusieurs variantes de prompts pour faciliter un processus d’affinement itératif. Évaluez la performance des différents prompts et choisissez les plus efficaces.

**Flux d’évaluation intégrés**  
Évaluez la qualité et l’efficacité de vos prompts et flux grâce aux outils d’évaluation intégrés.  
Comprenez la performance de vos applications basées sur des LLM.

**Ressources complètes**

Prompt Flow inclut une bibliothèque d’outils intégrés, d’exemples et de modèles. Ces ressources servent de point de départ pour le développement, stimulent la créativité et accélèrent le processus.

**Collaboration et préparation entreprise**

Favorisez la collaboration en équipe en permettant à plusieurs utilisateurs de travailler ensemble sur des projets d’ingénierie de prompts.  
Maintenez le contrôle des versions et partagez efficacement les connaissances. Simplifiez l’ensemble du processus d’ingénierie des prompts, du développement et de l’évaluation au déploiement et à la surveillance.

## Évaluation dans Prompt Flow

Dans Microsoft Prompt Flow, l’évaluation joue un rôle crucial pour mesurer la performance de vos modèles d’IA. Voyons comment personnaliser les flux et métriques d’évaluation dans Prompt Flow :

![PFVizualise](../../../../../translated_images/fr/pfvisualize.c1d9ca75baa2a222.png)

**Comprendre l’évaluation dans Prompt Flow**

Dans Prompt Flow, un flux représente une séquence de nœuds qui traitent une entrée et génèrent une sortie. Les flux d’évaluation sont des types spéciaux de flux conçus pour mesurer la performance d’une exécution selon des critères et objectifs spécifiques.

**Fonctionnalités clés des flux d’évaluation**

Ils s’exécutent généralement après le flux testé, en utilisant ses sorties. Ils calculent des scores ou métriques pour mesurer la performance du flux testé. Les métriques peuvent inclure la précision, des scores de pertinence ou toute autre mesure pertinente.

### Personnalisation des flux d’évaluation

**Définition des entrées**

Les flux d’évaluation doivent recevoir les sorties de l’exécution testée. Définissez les entrées de la même manière que pour les flux standards.  
Par exemple, si vous évaluez un flux QnA, nommez une entrée "answer". Si vous évaluez un flux de classification, nommez une entrée "category". Des entrées de vérité terrain (par exemple, les étiquettes réelles) peuvent également être nécessaires.

**Sorties et métriques**

Les flux d’évaluation produisent des résultats qui mesurent la performance du flux testé. Les métriques peuvent être calculées en Python ou via LLM. Utilisez la fonction log_metric() pour enregistrer les métriques pertinentes.

**Utilisation des flux d’évaluation personnalisés**

Développez votre propre flux d’évaluation adapté à vos tâches et objectifs spécifiques. Personnalisez les métriques selon vos besoins d’évaluation.  
Appliquez ce flux d’évaluation personnalisé à des exécutions en lot pour des tests à grande échelle.

## Méthodes d’évaluation intégrées

Prompt Flow propose également des méthodes d’évaluation intégrées.  
Vous pouvez soumettre des exécutions en lot et utiliser ces méthodes pour évaluer la performance de votre flux sur de grands ensembles de données.  
Consultez les résultats d’évaluation, comparez les métriques et itérez selon les besoins.  
N’oubliez pas que l’évaluation est essentielle pour garantir que vos modèles d’IA répondent aux critères et objectifs souhaités. Consultez la documentation officielle pour des instructions détaillées sur le développement et l’utilisation des flux d’évaluation dans Microsoft Prompt Flow.

En résumé, Microsoft Prompt Flow permet aux développeurs de créer des applications LLM de haute qualité en simplifiant l’ingénierie des prompts et en fournissant un environnement de développement robuste. Si vous travaillez avec des LLM, Prompt Flow est un outil précieux à découvrir. Explorez les [Documents d’évaluation Prompt Flow](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) pour des instructions détaillées sur le développement et l’utilisation des flux d’évaluation dans Microsoft Prompt Flow.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.