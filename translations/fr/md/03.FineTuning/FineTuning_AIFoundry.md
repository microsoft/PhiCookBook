<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-03-27T13:36:42+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_AIFoundry.md",
  "language_code": "fr"
}
-->
# Ajustement de Phi-3 avec Azure AI Foundry

Explorons comment ajuster le modèle linguistique Phi-3 Mini de Microsoft en utilisant Azure AI Foundry. L’ajustement permet d’adapter Phi-3 Mini à des tâches spécifiques, le rendant encore plus puissant et contextuellement pertinent.

## Considérations

- **Capacités :** Quels modèles peuvent être ajustés ? Que peut-on obtenir en ajustant le modèle de base ?
- **Coût :** Quel est le modèle de tarification pour l’ajustement ?
- **Personnalisation :** Dans quelle mesure puis-je modifier le modèle de base – et comment ?
- **Commodité :** Comment se déroule concrètement l’ajustement – dois-je écrire du code personnalisé ? Dois-je fournir mes propres ressources de calcul ?
- **Sécurité :** Les modèles ajustés présentent des risques en matière de sécurité – y a-t-il des garde-fous pour prévenir des conséquences involontaires ?

![Modèles AIFoundry](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.fr.png)

## Préparation à l’ajustement

### Prérequis

> [!NOTE]
> Pour les modèles de la famille Phi-3, l’offre d’ajustement en mode paiement à l’utilisation est uniquement disponible avec des hubs créés dans les régions **East US 2**.

- Une souscription Azure. Si vous n’avez pas de souscription Azure, créez un [compte Azure payant](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) pour commencer.

- Un [projet AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Les contrôles d’accès basés sur les rôles Azure (Azure RBAC) sont utilisés pour accorder l’accès aux opérations dans Azure AI Foundry. Pour effectuer les étapes de cet article, votre compte utilisateur doit disposer du rôle __Azure AI Developer__ sur le groupe de ressources.

### Enregistrement du fournisseur de souscription

Vérifiez que la souscription est enregistrée auprès du fournisseur de ressources `Microsoft.Network`.

1. Connectez-vous au [portail Azure](https://portal.azure.com).
1. Sélectionnez **Souscriptions** dans le menu de gauche.
1. Sélectionnez la souscription que vous souhaitez utiliser.
1. Sélectionnez **Paramètres du projet AI** > **Fournisseurs de ressources** dans le menu de gauche.
1. Confirmez que **Microsoft.Network** figure dans la liste des fournisseurs de ressources. Sinon, ajoutez-le.

### Préparation des données

Préparez vos données d’entraînement et de validation pour ajuster votre modèle. Vos ensembles de données d’entraînement et de validation doivent inclure des exemples d’entrée et de sortie pour illustrer les performances souhaitées du modèle.

Assurez-vous que tous vos exemples d’entraînement respectent le format attendu pour l’inférence. Pour ajuster les modèles efficacement, garantissez un jeu de données équilibré et diversifié.

Cela implique de maintenir un équilibre des données, d’inclure divers scénarios, et de raffiner périodiquement les données d’entraînement pour refléter les attentes du monde réel, ce qui conduit à des réponses plus précises et équilibrées du modèle.

Différents types de modèles nécessitent des formats de données d’entraînement différents.

### Complétion de chat

Les données d’entraînement et de validation que vous utilisez **doivent** être formatées en tant que document JSON Lines (JSONL). Pour `Phi-3-mini-128k-instruct`, le jeu de données d’ajustement doit être formaté dans le format conversationnel utilisé par l’API de complétion de chat.

### Exemple de format de fichier

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Le type de fichier pris en charge est JSON Lines. Les fichiers sont téléchargés dans le magasin de données par défaut et mis à disposition dans votre projet.

## Ajustement de Phi-3 avec Azure AI Foundry

Azure AI Foundry vous permet de personnaliser les modèles linguistiques de grande taille à l’aide de vos propres jeux de données via un processus appelé ajustement. L’ajustement offre une valeur significative en permettant la personnalisation et l’optimisation pour des tâches et applications spécifiques. Cela améliore les performances, réduit les coûts, diminue la latence et génère des résultats adaptés.

![Ajustement AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.fr.png)

### Créer un nouveau projet

1. Connectez-vous à [Azure AI Foundry](https://ai.azure.com).

1. Sélectionnez **+Nouveau projet** pour créer un nouveau projet dans Azure AI Foundry.

    ![Sélection Ajustement](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.fr.png)

1. Effectuez les tâches suivantes :

    - Nom du **Hub du projet**. Il doit être unique.
    - Sélectionnez le **Hub** à utiliser (créez-en un nouveau si nécessaire).

    ![Sélection Ajustement](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.fr.png)

1. Effectuez les tâches suivantes pour créer un nouveau hub :

    - Entrez le **Nom du hub**. Il doit être unique.
    - Sélectionnez votre **Souscription Azure**.
    - Sélectionnez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez la **Localisation** que vous souhaitez utiliser.
    - Sélectionnez **Connecter les services Azure AI** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez **Connecter Azure AI Search** à **Ignorer la connexion**.

    ![Sélection Ajustement](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.fr.png)

1. Sélectionnez **Suivant**.
1. Sélectionnez **Créer un projet**.

### Préparation des données

Avant l’ajustement, rassemblez ou créez un jeu de données pertinent pour votre tâche, comme des instructions de chat, des paires questions-réponses ou tout autre texte pertinent. Nettoyez et prétraitez ces données en supprimant les bruits, en gérant les valeurs manquantes et en tokenisant le texte.

### Ajuster les modèles Phi-3 dans Azure AI Foundry

> [!NOTE]
> L’ajustement des modèles Phi-3 est actuellement pris en charge dans les projets situés dans East US 2.

1. Sélectionnez **Catalogue de modèles** dans l’onglet latéral gauche.

1. Tapez *phi-3* dans la **barre de recherche** et sélectionnez le modèle phi-3 que vous souhaitez utiliser.

    ![Sélection Ajustement](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.fr.png)

1. Sélectionnez **Ajuster**.

    ![Sélection Ajustement](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.fr.png)

1. Entrez le **Nom du modèle ajusté**.

    ![Sélection Ajustement](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.fr.png)

1. Sélectionnez **Suivant**.

1. Effectuez les tâches suivantes :

    - Sélectionnez le **type de tâche** à **Complétion de chat**.
    - Sélectionnez les **Données d’entraînement** que vous souhaitez utiliser. Vous pouvez les télécharger via les données Azure AI Foundry ou depuis votre environnement local.

    ![Sélection Ajustement](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.fr.png)

1. Sélectionnez **Suivant**.

1. Téléchargez les **Données de validation** que vous souhaitez utiliser ou sélectionnez **Division automatique des données d’entraînement**.

    ![Sélection Ajustement](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.fr.png)

1. Sélectionnez **Suivant**.

1. Effectuez les tâches suivantes :

    - Sélectionnez le **Multiplicateur de taille de lot** que vous souhaitez utiliser.
    - Sélectionnez le **Taux d’apprentissage** que vous souhaitez utiliser.
    - Sélectionnez le nombre d’**Époques** que vous souhaitez utiliser.

    ![Sélection Ajustement](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.fr.png)

1. Sélectionnez **Soumettre** pour lancer le processus d’ajustement.

    ![Sélection Ajustement](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.fr.png)

1. Une fois votre modèle ajusté, son statut sera affiché comme **Terminé**, comme illustré ci-dessous. Vous pouvez désormais déployer le modèle et l’utiliser dans votre propre application, dans le bac à sable ou dans un flux de prompts. Pour plus d’informations, consultez [Comment déployer la famille de modèles Phi-3 avec Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![Sélection Ajustement](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.fr.png)

> [!NOTE]
> Pour des informations plus détaillées sur l’ajustement de Phi-3, consultez [Ajuster les modèles Phi-3 dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Nettoyage des modèles ajustés

Vous pouvez supprimer un modèle ajusté depuis la liste des modèles ajustés dans [Azure AI Foundry](https://ai.azure.com) ou depuis la page des détails du modèle. Sélectionnez le modèle ajusté à supprimer depuis la page d’ajustement, puis sélectionnez le bouton Supprimer pour le supprimer.

> [!NOTE]
> Vous ne pouvez pas supprimer un modèle personnalisé s’il a un déploiement actif. Vous devez d’abord supprimer le déploiement du modèle avant de pouvoir supprimer le modèle personnalisé.

## Coût et quotas

### Considérations sur le coût et les quotas pour les modèles Phi-3 ajustés en tant que service

Les modèles Phi ajustés en tant que service sont proposés par Microsoft et intégrés à Azure AI Foundry pour leur utilisation. Vous pouvez consulter les tarifs lors du [déploiement](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) ou de l’ajustement des modèles sous l’onglet Tarifs et conditions dans l’assistant de déploiement.

## Filtrage de contenu

Les modèles déployés en tant que service avec paiement à l’utilisation sont protégés par Azure AI Content Safety. Lorsqu’ils sont déployés sur des points de terminaison en temps réel, vous pouvez désactiver cette fonctionnalité. Avec Azure AI Content Safety activé, les prompts et les complétions passent par un ensemble de modèles de classification visant à détecter et à prévenir la génération de contenu nuisible. Le système de filtrage de contenu détecte et agit sur des catégories spécifiques de contenu potentiellement nuisible dans les prompts d’entrée et les complétions de sortie. En savoir plus sur [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configuration de l’ajustement**

Hyperparamètres : Définissez des hyperparamètres tels que le taux d’apprentissage, la taille de lot et le nombre d’époques d’entraînement.

**Fonction de perte**

Choisissez une fonction de perte appropriée pour votre tâche (par ex., entropie croisée).

**Optimiseur**

Sélectionnez un optimiseur (par ex., Adam) pour les mises à jour de gradient durant l’entraînement.

**Processus d’ajustement**

- Charger le modèle pré-entraîné : Chargez le point de contrôle de Phi-3 Mini.
- Ajouter des couches personnalisées : Ajoutez des couches spécifiques à la tâche (par ex., tête de classification pour des instructions de chat).

**Entraînez le modèle**
Ajustez le modèle en utilisant votre jeu de données préparé. Surveillez la progression de l’entraînement et ajustez les hyperparamètres si nécessaire.

**Évaluation et validation**

Ensemble de validation : Divisez vos données en ensembles d’entraînement et de validation.

**Évaluez les performances**

Utilisez des métriques telles que la précision, le score F1 ou la perplexité pour évaluer les performances du modèle.

## Sauvegarde du modèle ajusté

**Point de contrôle**
Sauvegardez le point de contrôle du modèle ajusté pour une utilisation future.

## Déploiement

- Déployez en tant que service Web : Déployez votre modèle ajusté en tant que service Web dans Azure AI Foundry.
- Testez le point de terminaison : Envoyez des requêtes de test au point de terminaison déployé pour vérifier son fonctionnement.

## Itérer et améliorer

Itération : Si les performances ne sont pas satisfaisantes, itérez en ajustant les hyperparamètres, en ajoutant plus de données ou en ajustant pour des époques supplémentaires.

## Surveiller et affiner

Surveillez en continu le comportement du modèle et affinez-le au besoin.

## Personnaliser et étendre

Tâches personnalisées : Phi-3 Mini peut être ajusté pour diverses tâches au-delà des instructions de chat. Explorez d’autres cas d’utilisation !
Expérimentez : Essayez différentes architectures, combinaisons de couches et techniques pour améliorer les performances.

> [!NOTE]
> L’ajustement est un processus itératif. Expérimentez, apprenez et adaptez votre modèle pour obtenir les meilleurs résultats pour votre tâche spécifique !

**Avertissement** :  
Ce document a été traduit en utilisant le service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.