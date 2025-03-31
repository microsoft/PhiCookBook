<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-03-27T13:18:14+00:00",
  "source_file": "md\\02.QuickStart\\AzureAIFoundry_QuickStart.md",
  "language_code": "fr"
}
-->
# **Utiliser Phi-3 dans Azure AI Foundry**

Avec le développement de l'IA générative, nous espérons utiliser une plateforme unifiée pour gérer différents modèles de langage (LLM et SLM), l'intégration des données d'entreprise, les opérations de fine-tuning/RAG, et l'évaluation des différentes activités d'entreprise après l'intégration des LLM et SLM, afin que les applications intelligentes basées sur l'IA générative soient mieux mises en œuvre. [Azure AI Foundry](https://ai.azure.com) est une plateforme d'applications d'IA générative destinée aux entreprises.

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.fr.png)

Avec Azure AI Foundry, vous pouvez évaluer les réponses des modèles de langage (LLM) et orchestrer les composants d'application de prompt grâce au flux de prompt pour obtenir de meilleures performances. La plateforme facilite la mise à l'échelle des concepts de preuve vers une production complète avec simplicité. La surveillance continue et l'affinement garantissent un succès à long terme.

Nous pouvons rapidement déployer le modèle Phi-3 sur Azure AI Foundry grâce à des étapes simples, puis utiliser Azure AI Foundry pour effectuer des tâches liées à Phi-3 comme Playground/Chat, Fine-tuning, évaluation, et autres travaux associés.

## **1. Préparation**

Si vous avez déjà installé le [CLI Azure Developer](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) sur votre machine, utiliser ce modèle est aussi simple que de lancer cette commande dans un nouveau répertoire.

## Création manuelle

Créer un projet et un hub Microsoft Azure AI Foundry est un excellent moyen d'organiser et de gérer vos travaux d'IA. Voici un guide étape par étape pour commencer :

### Créer un projet dans Azure AI Foundry

1. **Accéder à Azure AI Foundry** : Connectez-vous au portail Azure AI Foundry.
2. **Créer un projet** :
   - Si vous êtes dans un projet, sélectionnez "Azure AI Foundry" en haut à gauche de la page pour accéder à la page d'accueil.
   - Sélectionnez "+ Créer un projet".
   - Entrez un nom pour le projet.
   - Si vous avez un hub, il sera sélectionné par défaut. Si vous avez accès à plusieurs hubs, vous pouvez en choisir un autre dans le menu déroulant. Si vous souhaitez créer un nouveau hub, sélectionnez "Créer un nouveau hub" et fournissez un nom.
   - Sélectionnez "Créer".

### Créer un hub dans Azure AI Foundry

1. **Accéder à Azure AI Foundry** : Connectez-vous avec votre compte Azure.
2. **Créer un hub** :
   - Sélectionnez le Centre de gestion dans le menu de gauche.
   - Sélectionnez "Tous les ressources", puis cliquez sur la flèche à côté de "+ Nouveau projet" et choisissez "+ Nouveau hub".
   - Dans la boîte de dialogue "Créer un nouveau hub", entrez un nom pour votre hub (par exemple, contoso-hub) et modifiez les autres champs selon vos besoins.
   - Sélectionnez "Suivant", examinez les informations, puis cliquez sur "Créer".

Pour des instructions plus détaillées, vous pouvez consulter la [documentation officielle de Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Après une création réussie, vous pouvez accéder au studio que vous avez créé via [ai.azure.com](https://ai.azure.com/).

Un AI Foundry peut contenir plusieurs projets. Créez un projet dans AI Foundry pour préparer votre travail.

Créer des [QuickStarts Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code).

## **2. Déployer un modèle Phi dans Azure AI Foundry**

Cliquez sur l'option Explorer du projet pour accéder au catalogue de modèles et sélectionnez Phi-3.

Choisissez Phi-3-mini-4k-instruct.

Cliquez sur 'Déployer' pour installer le modèle Phi-3-mini-4k-instruct.

> [!NOTE]
>
> Vous pouvez sélectionner la puissance de calcul lors du déploiement.

## **3. Playground Chat Phi dans Azure AI Foundry**

Accédez à la page de déploiement, sélectionnez Playground, et discutez avec Phi-3 sur Azure AI Foundry.

## **4. Déployer le modèle depuis Azure AI Foundry**

Pour déployer un modèle depuis le catalogue de modèles Azure, vous pouvez suivre ces étapes :

- Connectez-vous à Azure AI Foundry.
- Choisissez le modèle que vous souhaitez déployer dans le catalogue de modèles Azure AI Foundry.
- Sur la page de détails du modèle, sélectionnez Déployer, puis choisissez l'API Serverless avec Azure AI Content Safety.
- Sélectionnez le projet dans lequel vous souhaitez déployer vos modèles. Pour utiliser l'offre API Serverless, votre espace de travail doit être situé dans la région East US 2 ou Sweden Central. Vous pouvez personnaliser le nom du déploiement.
- Dans l'assistant de déploiement, sélectionnez les tarifs et conditions pour en savoir plus sur les prix et les conditions d'utilisation.
- Cliquez sur Déployer. Attendez que le déploiement soit prêt et que vous soyez redirigé vers la page Déploiements.
- Sélectionnez Ouvrir dans Playground pour commencer à interagir avec le modèle.
- Vous pouvez revenir à la page Déploiements, sélectionner le déploiement, et noter l'URL cible de l'endpoint ainsi que la clé secrète, que vous pouvez utiliser pour appeler le déploiement et générer des complétions.
- Vous pouvez toujours retrouver les détails de l'endpoint, l'URL et les clés d'accès en naviguant vers l'onglet Build et en sélectionnant Déploiements dans la section Composants.

> [!NOTE]
> Veuillez noter que votre compte doit avoir les permissions de rôle Azure AI Developer sur le groupe de ressources pour effectuer ces étapes.

## **5. Utiliser l'API Phi dans Azure AI Foundry**

Vous pouvez accéder à https://{Nom de votre projet}.region.inference.ml.azure.com/swagger.json via une requête GET dans Postman et le combiner avec la clé pour découvrir les interfaces fournies.

Vous pouvez obtenir très facilement les paramètres de requête ainsi que les paramètres de réponse.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.