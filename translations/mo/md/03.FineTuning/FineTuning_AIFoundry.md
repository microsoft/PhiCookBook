<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94e7d7ab455720bab75ead5c28521c97",
  "translation_date": "2025-04-04T13:09:08+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_AIFoundry.md",
  "language_code": "mo"
}
-->
# Fine-tuning Phi-3 with Azure AI Foundry

Explorez comment affiner le modèle linguistique Phi-3 Mini de Microsoft en utilisant Azure AI Foundry. L’affinage permet d’adapter Phi-3 Mini à des tâches spécifiques, le rendant encore plus puissant et pertinent.

## Considérations

- **Capacités :** Quels modèles peuvent être affinés ? Que peut accomplir le modèle de base une fois ajusté ?
- **Coût :** Quel est le modèle de tarification pour l’affinage ?
**Personnalisation :** Dans quelle mesure puis-je modifier le modèle de base – et de quelles façons ?
- **Praticité :** Comment se déroule concrètement l’affinage – faut-il écrire du code personnalisé ? Dois-je fournir mes propres ressources de calcul ?
- **Sécurité :** Les modèles affinés présentent des risques de sécurité – existe-t-il des mesures pour prévenir les effets indésirables ?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.mo.png)

## Préparation à l’affinage

### Prérequis

> [!NOTE]
> Pour les modèles de la famille Phi-3, l’offre d’affinage à la demande est uniquement disponible dans les hubs créés dans les régions **East US 2**.

- Une souscription Azure. Si vous n’avez pas de souscription, créez un [compte Azure payant](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) pour commencer.

- Un [projet AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Les contrôles d’accès basés sur les rôles Azure (Azure RBAC) sont utilisés pour accorder l’accès aux opérations dans Azure AI Foundry. Pour effectuer les étapes de cet article, votre compte utilisateur doit être assigné au rôle __Azure AI Developer__ sur le groupe de ressources.

### Enregistrement du fournisseur de souscription

Vérifiez que la souscription est enregistrée auprès du fournisseur de ressources `Microsoft.Network`.

1. Connectez-vous au [portail Azure](https://portal.azure.com).
1. Sélectionnez **Souscriptions** dans le menu de gauche.
1. Choisissez la souscription que vous souhaitez utiliser.
1. Sélectionnez **Paramètres du projet AI** > **Fournisseurs de ressources** dans le menu de gauche.
1. Confirmez que **Microsoft.Network** figure dans la liste des fournisseurs de ressources. Sinon, ajoutez-le.

### Préparation des données

Préparez vos données d’entraînement et de validation pour affiner votre modèle. Vos ensembles de données d’entraînement et de validation doivent inclure des exemples d’entrée et de sortie correspondant aux performances souhaitées du modèle.

Assurez-vous que tous vos exemples d’entraînement respectent le format attendu pour l’inférence. Pour un affinage efficace, il est essentiel de disposer d’un ensemble de données équilibré et diversifié.

Cela implique de maintenir un équilibre dans les données, d’inclure divers scénarios et de raffiner périodiquement les données d’entraînement pour correspondre aux attentes du monde réel, ce qui conduit à des réponses plus précises et équilibrées du modèle.

Différents types de modèles nécessitent des formats de données d’entraînement différents.

### Chat Completion

Les données d’entraînement et de validation utilisées **doivent** être formatées sous forme de document JSON Lines (JSONL). Pour `Phi-3-mini-128k-instruct`, l’ensemble de données d’affinage doit être structuré dans le format conversationnel utilisé par l’API Chat completions.

### Exemple de format de fichier

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Le type de fichier pris en charge est JSON Lines. Les fichiers sont téléchargés sur le stockage par défaut et mis à disposition dans votre projet.

## Affinage de Phi-3 avec Azure AI Foundry

Azure AI Foundry vous permet de personnaliser les modèles linguistiques à grande échelle en fonction de vos ensembles de données grâce à un processus appelé affinage. L’affinage offre une valeur significative en permettant une personnalisation et une optimisation pour des tâches et des applications spécifiques. Il améliore les performances, réduit les coûts, diminue la latence et génère des résultats adaptés.

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.mo.png)

### Créer un nouveau projet

1. Connectez-vous à [Azure AI Foundry](https://ai.azure.com).

1. Sélectionnez **+Nouveau projet** pour créer un nouveau projet dans Azure AI Foundry.

    ![FineTuneSelect](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.mo.png)

1. Effectuez les tâches suivantes :

    - Nom du **Hub du projet**. Il doit être une valeur unique.
    - Sélectionnez le **Hub** à utiliser (créez-en un nouveau si nécessaire).

    ![FineTuneSelect](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.mo.png)

1. Effectuez les tâches suivantes pour créer un nouveau hub :

    - Entrez un **Nom de hub**. Il doit être une valeur unique.
    - Sélectionnez votre **Souscription Azure**.
    - Choisissez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez la **Localisation** souhaitée.
    - Sélectionnez les **Services Azure AI** à connecter (créez-en un nouveau si nécessaire).
    - Sélectionnez **Connecter Azure AI Search** pour **Ignorer la connexion**.

    ![FineTuneSelect](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.mo.png)

1. Sélectionnez **Suivant**.
1. Sélectionnez **Créer un projet**.

### Préparation des données

Avant l’affinage, rassemblez ou créez un ensemble de données pertinent pour votre tâche, tel que des instructions de chat, des paires de questions-réponses ou tout autre texte pertinent. Nettoyez et prétraitez ces données en supprimant le bruit, en gérant les valeurs manquantes et en tokenisant le texte.

### Affiner les modèles Phi-3 dans Azure AI Foundry

> [!NOTE]
> L’affinage des modèles Phi-3 est actuellement pris en charge dans les projets situés dans East US 2.

1. Sélectionnez **Catalogue de modèles** dans l’onglet de gauche.

1. Tapez *phi-3* dans la **barre de recherche** et sélectionnez le modèle phi-3 que vous souhaitez utiliser.

    ![FineTuneSelect](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.mo.png)

1. Sélectionnez **Affiner**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.mo.png)

1. Entrez le **Nom du modèle affiné**.

    ![FineTuneSelect](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.mo.png)

1. Sélectionnez **Suivant**.

1. Effectuez les tâches suivantes :

    - Choisissez le **type de tâche** comme **Chat completion**.
    - Sélectionnez les **Données d’entraînement** que vous souhaitez utiliser. Vous pouvez les télécharger via Azure AI Foundry ou depuis votre environnement local.

    ![FineTuneSelect](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.mo.png)

1. Sélectionnez **Suivant**.

1. Téléchargez les **Données de validation** que vous souhaitez utiliser, ou sélectionnez **Division automatique des données d’entraînement**.

    ![FineTuneSelect](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.mo.png)

1. Sélectionnez **Suivant**.

1. Effectuez les tâches suivantes :

    - Choisissez le **Multiplicateur de taille de lot** que vous souhaitez utiliser.
    - Sélectionnez le **Taux d’apprentissage** souhaité.
    - Choisissez le nombre d’**Époques** à utiliser.

    ![FineTuneSelect](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.mo.png)

1. Sélectionnez **Soumettre** pour lancer le processus d’affinage.

    ![FineTuneSelect](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.mo.png)

1. Une fois votre modèle affiné, son statut sera affiché comme **Terminé**, comme indiqué dans l’image ci-dessous. Vous pouvez maintenant déployer le modèle et l’utiliser dans votre propre application, dans le playground ou dans prompt flow. Pour plus d’informations, consultez [Comment déployer les modèles de la famille Phi-3 avec Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.mo.png)

> [!NOTE]
> Pour des informations détaillées sur l’affinage de Phi-3, veuillez consulter [Affiner les modèles Phi-3 dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Nettoyage des modèles affinés

Vous pouvez supprimer un modèle affiné depuis la liste des modèles d’affinage dans [Azure AI Foundry](https://ai.azure.com) ou depuis la page de détails du modèle. Sélectionnez le modèle affiné à supprimer depuis la page d’affinage, puis cliquez sur le bouton Supprimer pour le supprimer.

> [!NOTE]
> Vous ne pouvez pas supprimer un modèle personnalisé s’il a un déploiement existant. Vous devez d’abord supprimer le déploiement avant de pouvoir supprimer le modèle.

## Coût et quotas

### Considérations sur le coût et les quotas pour les modèles Phi-3 affinés en tant que service

Les modèles Phi affinés en tant que service sont proposés par Microsoft et intégrés à Azure AI Foundry pour utilisation. Vous pouvez consulter les tarifs lors du [déploiement](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) ou de l’affinage des modèles sous l’onglet Tarification et conditions dans l’assistant de déploiement.

## Filtrage de contenu

Les modèles déployés en tant que service avec paiement à l’utilisation sont protégés par Azure AI Content Safety. Lorsqu’ils sont déployés sur des points de terminaison en temps réel, vous pouvez désactiver cette fonctionnalité. Avec Azure AI Content Safety activé, à la fois l’invite et la réponse passent par un ensemble de modèles de classification visant à détecter et prévenir la génération de contenu nuisible. Le système de filtrage de contenu détecte et agit sur des catégories spécifiques de contenu potentiellement nuisible dans les invites et les réponses. Pour en savoir plus, consultez [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configuration d’affinage**

Hyperparamètres : Définissez des hyperparamètres tels que le taux d’apprentissage, la taille des lots et le nombre d’époques d’entraînement.

**Fonction de perte**

Choisissez une fonction de perte adaptée à votre tâche (par ex., entropie croisée).

**Optimiseur**

Sélectionnez un optimiseur (par ex., Adam) pour les mises à jour de gradient pendant l’entraînement.

**Processus d’affinage**

- Charger le modèle pré-entraîné : Chargez le checkpoint Phi-3 Mini.
- Ajouter des couches personnalisées : Ajoutez des couches spécifiques à la tâche (par ex., une tête de classification pour les instructions de chat).

**Entraîner le modèle**
Affinez le modèle en utilisant votre ensemble de données préparé. Surveillez les progrès de l’entraînement et ajustez les hyperparamètres si nécessaire.

**Évaluation et validation**

Ensemble de validation : Divisez vos données en ensembles d’entraînement et de validation.

**Évaluer les performances**

Utilisez des métriques telles que la précision, le F1-score ou la perplexité pour évaluer les performances du modèle.

## Sauvegarder le modèle affiné

**Checkpoint**
Sauvegardez le checkpoint du modèle affiné pour une utilisation future.

## Déploiement

- Déployez en tant que service web : Déployez votre modèle affiné comme service web dans Azure AI Foundry.
- Testez le point de terminaison : Envoyez des requêtes de test au point de terminaison déployé pour vérifier son fonctionnement.

## Itération et amélioration

Itérez : Si les performances ne sont pas satisfaisantes, ajustez les hyperparamètres, ajoutez plus de données ou affinez pendant des époques supplémentaires.

## Surveillance et ajustement

Surveillez en continu le comportement du modèle et ajustez-le si nécessaire.

## Personnaliser et étendre

Tâches personnalisées : Phi-3 Mini peut être affiné pour diverses tâches au-delà des instructions de chat. Explorez d’autres cas d’utilisation !
Expérimentez : Essayez différentes architectures, combinaisons de couches et techniques pour améliorer les performances.

> [!NOTE]
> L’affinage est un processus itératif. Expérimentez, apprenez et adaptez votre modèle pour obtenir les meilleurs résultats pour votre tâche spécifique !

It seems you are requesting a translation to "mo." Could you clarify what "mo" refers to? Are you asking for translation to Maori, Mongolian, or another language? Please provide more context so I can assist you accurately.