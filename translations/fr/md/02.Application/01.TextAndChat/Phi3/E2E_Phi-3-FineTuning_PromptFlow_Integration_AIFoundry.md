<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-03-27T10:11:08+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "fr"
}
-->
# Affiner et intégrer des modèles Phi-3 personnalisés avec Prompt Flow dans Azure AI Foundry

Cet exemple de bout en bout (E2E) est basé sur le guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" de la communauté technique de Microsoft. Il présente les processus d'ajustement, de déploiement et d'intégration des modèles Phi-3 personnalisés avec Prompt Flow dans Azure AI Foundry.  
Contrairement à l'exemple E2E "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", qui impliquait l'exécution de code en local, ce tutoriel se concentre entièrement sur l'ajustement et l'intégration de votre modèle dans Azure AI / ML Studio.

## Aperçu

Dans cet exemple E2E, vous apprendrez à ajuster le modèle Phi-3 et à l'intégrer avec Prompt Flow dans Azure AI Foundry. En exploitant Azure AI / ML Studio, vous établirez un flux de travail pour déployer et utiliser des modèles d'IA personnalisés. Cet exemple E2E est divisé en trois scénarios :

**Scénario 1 : Configurer les ressources Azure et se préparer à l'ajustement**

**Scénario 2 : Ajuster le modèle Phi-3 et le déployer dans Azure Machine Learning Studio**

**Scénario 3 : Intégrer avec Prompt Flow et discuter avec votre modèle personnalisé dans Azure AI Foundry**

Voici une vue d'ensemble de cet exemple E2E.

![Vue d'ensemble Phi-3-FineTuning_PromptFlow_Integration.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.fr.png)

### Table des matières

1. **[Scénario 1 : Configurer les ressources Azure et se préparer à l'ajustement](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Créer un espace de travail Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Demander des quotas GPU dans l'abonnement Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ajouter une attribution de rôle](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurer le projet](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Préparer le jeu de données pour l'ajustement](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scénario 2 : Ajuster le modèle Phi-3 et le déployer dans Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ajuster le modèle Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Déployer le modèle Phi-3 ajusté](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scénario 3 : Intégrer avec Prompt Flow et discuter avec votre modèle personnalisé dans Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Intégrer le modèle Phi-3 personnalisé avec Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Discuter avec votre modèle Phi-3 personnalisé](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scénario 1 : Configurer les ressources Azure et se préparer à l'ajustement

### Créer un espace de travail Azure Machine Learning

1. Tapez *azure machine learning* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Azure Machine Learning** parmi les options proposées.

    ![Tapez azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.fr.png)

2. Sélectionnez **+ Créer** dans le menu de navigation.

3. Sélectionnez **Nouvel espace de travail** dans le menu de navigation.

    ![Sélectionnez nouvel espace de travail.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.fr.png)

4. Effectuez les tâches suivantes :

    - Sélectionnez votre **Abonnement** Azure.
    - Sélectionnez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Entrez un **Nom d'espace de travail**. Celui-ci doit être unique.
    - Sélectionnez la **Région** que vous souhaitez utiliser.
    - Sélectionnez le **Compte de stockage** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez le **Key Vault** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez **Application Insights** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez le **Registre de conteneurs** à utiliser (créez-en un nouveau si nécessaire).

    ![Remplissez les informations Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.fr.png)

5. Sélectionnez **Vérifier + Créer**.

6. Sélectionnez **Créer**.

### Demander des quotas GPU dans l'abonnement Azure

Dans ce tutoriel, vous apprendrez à ajuster et déployer un modèle Phi-3 en utilisant des GPU. Pour l'ajustement, vous utiliserez le GPU *Standard_NC24ads_A100_v4*, qui nécessite une demande de quota. Pour le déploiement, vous utiliserez le GPU *Standard_NC6s_v3*, qui nécessite également une demande de quota.

> [!NOTE]
>
> Seuls les abonnements Pay-As-You-Go (le type d'abonnement standard) sont éligibles pour l'allocation GPU ; les abonnements avec avantages ne sont actuellement pas pris en charge.

1. Visitez [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Effectuez les tâches suivantes pour demander un quota pour la famille *Standard NCADSA100v4* :

    - Sélectionnez **Quota** dans l'onglet de gauche.
    - Sélectionnez la **Famille de machines virtuelles** à utiliser. Par exemple, sélectionnez **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, qui inclut le GPU *Standard_NC24ads_A100_v4*.
    - Sélectionnez **Demander un quota** dans le menu de navigation.

        ![Demander un quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.fr.png)

    - Sur la page de demande de quota, entrez la **Nouvelle limite de cœurs** que vous souhaitez utiliser. Par exemple, 24.
    - Sur la page de demande de quota, sélectionnez **Soumettre** pour demander le quota GPU.

1. Effectuez les tâches suivantes pour demander un quota pour la famille *Standard NCSv3* :

    - Sélectionnez **Quota** dans l'onglet de gauche.
    - Sélectionnez la **Famille de machines virtuelles** à utiliser. Par exemple, sélectionnez **Standard NCSv3 Family Cluster Dedicated vCPUs**, qui inclut le GPU *Standard_NC6s_v3*.
    - Sélectionnez **Demander un quota** dans le menu de navigation.
    - Sur la page de demande de quota, entrez la **Nouvelle limite de cœurs** que vous souhaitez utiliser. Par exemple, 24.
    - Sur la page de demande de quota, sélectionnez **Soumettre** pour demander le quota GPU.

### Ajouter une attribution de rôle

Pour ajuster et déployer vos modèles, vous devez d'abord créer une identité gérée affectée par l'utilisateur (UAI) et lui attribuer les autorisations appropriées. Cette UAI sera utilisée pour l'authentification lors du déploiement.

#### Créer une identité gérée affectée par l'utilisateur (UAI)

1. Tapez *identités gérées* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Identités gérées** parmi les options proposées.

    ![Tapez identités gérées.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.fr.png)

1. Sélectionnez **+ Créer**.

    ![Sélectionnez créer.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.fr.png)

1. Effectuez les tâches suivantes :

    - Sélectionnez votre **Abonnement** Azure.
    - Sélectionnez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez la **Région** que vous souhaitez utiliser.
    - Entrez le **Nom**. Celui-ci doit être unique.

    ![Remplissez les informations de l'identité gérée.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.fr.png)

1. Sélectionnez **Vérifier + créer**.

1. Sélectionnez **Créer**.

#### Ajouter le rôle de contributeur à l'identité gérée

1. Accédez à la ressource d'identité gérée que vous avez créée.

1. Sélectionnez **Attributions de rôle Azure** dans l'onglet de gauche.

1. Sélectionnez **+ Ajouter une attribution de rôle** dans le menu de navigation.

1. Sur la page Ajouter une attribution de rôle, effectuez les tâches suivantes :
    - Sélectionnez l'**Étendue** comme **Groupe de ressources**.
    - Sélectionnez votre **Abonnement** Azure.
    - Sélectionnez le **Groupe de ressources** à utiliser.
    - Sélectionnez le **Rôle** comme **Contributeur**.

    ![Remplissez les informations pour le rôle de contributeur.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.fr.png)

2. Sélectionnez **Enregistrer**.

#### Ajouter le rôle de lecteur de données de blob de stockage à l'identité gérée

1. Tapez *comptes de stockage* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Comptes de stockage** parmi les options proposées.

    ![Tapez comptes de stockage.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.fr.png)

1. Sélectionnez le compte de stockage associé à l'espace de travail Azure Machine Learning que vous avez créé. Par exemple, *finetunephistorage*.

1. Effectuez les tâches suivantes pour accéder à la page Ajouter une attribution de rôle :

    - Accédez au compte de stockage Azure que vous avez créé.
    - Sélectionnez **Contrôle d'accès (IAM)** dans l'onglet de gauche.
    - Sélectionnez **+ Ajouter** dans le menu de navigation.
    - Sélectionnez **Ajouter une attribution de rôle** dans le menu de navigation.

    ![Ajouter un rôle.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.fr.png)

1. Sur la page Ajouter une attribution de rôle, effectuez les tâches suivantes :

    - Sur la page Rôle, tapez *Lecteur de données de blob de stockage* dans la **barre de recherche** et sélectionnez **Lecteur de données de blob de stockage** parmi les options proposées.
    - Sur la page Rôle, sélectionnez **Suivant**.
    - Sur la page Membres, sélectionnez **Attribuer un accès à** **Identité gérée**.
    - Sur la page Membres, sélectionnez **+ Sélectionner des membres**.
    - Sur la page Sélectionner des identités gérées, sélectionnez votre **Abonnement** Azure.
    - Sur la page Sélectionner des identités gérées, sélectionnez l'**Identité gérée** comme **Identité gérée**.
    - Sur la page Sélectionner des identités gérées, sélectionnez l'identité gérée que vous avez créée. Par exemple, *finetunephi-managedidentity*.
    - Sur la page Sélectionner des identités gérées, sélectionnez **Sélectionner**.

    ![Sélectionnez l'identité gérée.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.fr.png)

1. Sélectionnez **Vérifier + attribuer**.

#### Ajouter le rôle AcrPull à l'identité gérée

1. Tapez *registres de conteneurs* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Registres de conteneurs** parmi les options proposées.

    ![Tapez registres de conteneurs.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.fr.png)

1. Sélectionnez le registre de conteneurs associé à l'espace de travail Azure Machine Learning. Par exemple, *finetunephicontainerregistry*.

1. Effectuez les tâches suivantes pour accéder à la page Ajouter une attribution de rôle :

    - Sélectionnez **Contrôle d'accès (IAM)** dans l'onglet de gauche.
    - Sélectionnez **+ Ajouter** dans le menu de navigation.
    - Sélectionnez **Ajouter une attribution de rôle** dans le menu de navigation.

1. Sur la page Ajouter une attribution de rôle, effectuez les tâches suivantes :

    - Sur la page Rôle, tapez *AcrPull* dans la **barre de recherche** et sélectionnez **AcrPull** parmi les options proposées.
    - Sur la page Rôle, sélectionnez **Suivant**.
    - Sur la page Membres, sélectionnez **Attribuer un accès à** **Identité gérée**.
    - Sur la page Membres, sélectionnez **+ Sélectionner des membres**.
    - Sur la page Sélectionner des identités gérées, sélectionnez votre **Abonnement** Azure.
    - Sur la page Sélectionner des identités gérées, sélectionnez l'**Identité gérée** comme **Identité gérée**.
    - Sur la page Sélectionner des identités gérées, sélectionnez l'identité gérée que vous avez créée. Par exemple, *finetunephi-managedidentity*.
    - Sur la page Sélectionner des identités gérées, sélectionnez **Sélectionner**.
    - Sélectionnez **Vérifier + attribuer**.

### Configurer le projet

Pour télécharger les jeux de données nécessaires à l'ajustement, vous allez configurer un environnement local.

Dans cet exercice, vous allez :

- Créer un dossier pour travailler à l'intérieur.
- Créer un environnement virtuel.
- Installer les packages requis.
- Créer un fichier *download_dataset.py* pour télécharger le jeu de données.

#### Créer un dossier pour travailler à l'intérieur

1. Ouvrez une fenêtre de terminal et tapez la commande suivante pour créer un dossier nommé *finetune-phi* dans le chemin par défaut.

    ```console
    mkdir finetune-phi
    ```

2. Tapez la commande suivante dans votre terminal pour accéder au dossier *finetune-phi* que vous avez créé.

    ```console
    cd finetune-phi
    ```

#### Créer un environnement virtuel

1. Tapez la commande suivante dans votre terminal pour créer un environnement virtuel nommé *.venv*.

    ```console
    python -m venv .venv
    ```

2. Tapez la commande suivante dans votre terminal pour activer l'environnement virtuel.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Si cela a fonctionné, vous devriez voir *(.venv)* avant l'invite de commande.

#### Installer les packages requis

1. Tapez les commandes suivantes dans votre terminal pour installer les packages requis.

    ```console
    pip install datasets==2.19.1
    ```

#### Créer `download_dataset.py`

> [!NOTE]
> Structure complète du dossier :
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Ouvrez **Visual Studio Code**.

1. Sélectionnez **Fichier** dans la barre de menu.

1. Sélectionnez **Ouvrir un dossier**.

1. Sélectionnez le dossier *finetune-phi* que vous avez créé, situé à *C:\Users\yourUserName\finetune-phi*.

    ![Sélectionnez le dossier que vous avez créé.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.fr.png)

1. Dans le volet gauche de Visual Studio Code, cliquez avec le bouton droit et sélectionnez **Nouveau fichier** pour créer un nouveau fichier nommé *download_dataset.py*.

    ![Créez un nouveau fichier.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.fr.png)

### Préparer le jeu de données pour l'ajustement

Dans cet exercice, vous exécuterez le fichier *download_dataset.py* pour télécharger les jeux de données *ultrachat_200k* dans votre environnement local. Vous utiliserez ensuite ces jeux de données pour ajuster le modèle Phi-3 dans Azure Machine Learning.

Dans cet exercice, vous allez :

- Ajouter du code au fichier *download_dataset.py* pour télécharger les jeux de données.
- Exécuter le fichier *download_dataset.py* pour télécharger les jeux de données dans votre environnement local.

#### Télécharger votre jeu de données avec *download_dataset.py*

1. Ouvrez le fichier *download_dataset.py* dans Visual Studio Code.

1. Ajoutez le code suivant dans le fichier *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Tapez la commande suivante dans votre terminal pour exécuter le script et télécharger le jeu de données dans votre environnement local.

    ```console
    python download_dataset.py
    ```

1. Vérifiez que les jeux de données ont été enregistrés avec succès dans votre répertoire local *finetune-phi/data*.

> [!NOTE]
>
> #### Remarque sur la taille du jeu de données et le temps d'ajustement
>
> Dans ce tutoriel, vous utilisez seulement 1 % du jeu de données (`split='train[:1%]'`). Cela réduit considérablement la quantité de données, accélérant à la fois le téléchargement et les processus d'ajustement. Vous pouvez ajuster le pourcentage pour trouver le bon équilibre entre
1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Sélectionnez **Compute** dans le menu latéral gauche.

1. Sélectionnez **Compute clusters** dans le menu de navigation.

1. Cliquez sur **+ New**.

    ![Sélectionnez compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.fr.png)

1. Effectuez les actions suivantes :

    - Sélectionnez la **Région** que vous souhaitez utiliser.
    - Réglez le **Niveau de machine virtuelle** sur **Dedicated**.
    - Réglez le **Type de machine virtuelle** sur **GPU**.
    - Appliquez le filtre **Taille de machine virtuelle** sur **Select from all options**.
    - Choisissez la **Taille de machine virtuelle** sur **Standard_NC24ads_A100_v4**.

    ![Créer un cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.fr.png)

1. Cliquez sur **Next**.

1. Effectuez les actions suivantes :

    - Entrez un **Nom de calcul**. Il doit être unique.
    - Réglez le **Nombre minimum de nœuds** sur **0**.
    - Réglez le **Nombre maximum de nœuds** sur **1**.
    - Réglez les **Secondes d'inactivité avant réduction d'échelle** sur **120**.

    ![Créer un cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.fr.png)

1. Cliquez sur **Create**.

#### Ajuster le modèle Phi-3

1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Sélectionnez l'espace de travail Azure Machine Learning que vous avez créé.

    ![Sélectionnez l'espace de travail que vous avez créé.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.fr.png)

1. Effectuez les actions suivantes :

    - Sélectionnez **Model catalog** dans le menu latéral gauche.
    - Tapez *phi-3-mini-4k* dans la **barre de recherche** et sélectionnez **Phi-3-mini-4k-instruct** parmi les options proposées.

    ![Tapez phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.fr.png)

1. Sélectionnez **Fine-tune** dans le menu de navigation.

    ![Sélectionnez fine-tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.fr.png)

1. Effectuez les actions suivantes :

    - Réglez **Select task type** sur **Chat completion**.
    - Cliquez sur **+ Select data** pour télécharger les **Données d'entraînement**.
    - Réglez le type de téléchargement des données de validation sur **Provide different validation data**.
    - Cliquez sur **+ Select data** pour télécharger les **Données de validation**.

    ![Remplir la page de fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.fr.png)

    > [!TIP]
    >
    > Vous pouvez sélectionner **Advanced settings** pour personnaliser des configurations comme **learning_rate** et **lr_scheduler_type** afin d'optimiser le processus d'ajustement selon vos besoins spécifiques.

1. Cliquez sur **Finish**.

1. Dans cet exercice, vous avez ajusté avec succès le modèle Phi-3 à l'aide d'Azure Machine Learning. Notez que le processus d'ajustement peut prendre un temps considérable. Après avoir lancé la tâche d'ajustement, vous devrez attendre qu'elle se termine. Vous pouvez surveiller l'état de la tâche en naviguant vers l'onglet Jobs dans le menu latéral de votre espace de travail Azure Machine Learning. Dans la prochaine série, vous déploierez le modèle ajusté et l'intégrerez à Prompt flow.

    ![Voir la tâche d'ajustement.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.fr.png)

### Déployer le modèle Phi-3 ajusté

Pour intégrer le modèle Phi-3 ajusté à Prompt flow, vous devez déployer le modèle pour le rendre accessible en inférence en temps réel. Ce processus implique l'enregistrement du modèle, la création d'un point de terminaison en ligne et le déploiement du modèle.

Dans cet exercice, vous allez :

- Enregistrer le modèle ajusté dans l'espace de travail Azure Machine Learning.
- Créer un point de terminaison en ligne.
- Déployer le modèle Phi-3 ajusté enregistré.

#### Enregistrer le modèle ajusté

1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Sélectionnez l'espace de travail Azure Machine Learning que vous avez créé.

    ![Sélectionnez l'espace de travail que vous avez créé.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.fr.png)

1. Sélectionnez **Models** dans le menu latéral gauche.
1. Cliquez sur **+ Register**.
1. Sélectionnez **From a job output**.

    ![Enregistrer le modèle.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.fr.png)

1. Sélectionnez la tâche que vous avez créée.

    ![Sélectionnez la tâche.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.fr.png)

1. Cliquez sur **Next**.

1. Réglez **Model type** sur **MLflow**.

1. Assurez-vous que **Job output** est sélectionné ; cela devrait être automatiquement le cas.

    ![Sélectionnez la sortie.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.fr.png)

2. Cliquez sur **Next**.

3. Cliquez sur **Register**.

    ![Cliquez sur register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.fr.png)

4. Vous pouvez consulter votre modèle enregistré en naviguant dans le menu **Models** depuis le menu latéral gauche.

    ![Modèle enregistré.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.fr.png)

#### Déployer le modèle ajusté

1. Accédez à l'espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans le menu latéral gauche.

1. Sélectionnez **Real-time endpoints** dans le menu de navigation.

    ![Créer un endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.fr.png)

1. Cliquez sur **Create**.

1. Sélectionnez le modèle enregistré que vous avez créé.

    ![Sélectionnez le modèle enregistré.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.fr.png)

1. Cliquez sur **Select**.

1. Effectuez les actions suivantes :

    - Réglez la **Machine virtuelle** sur *Standard_NC6s_v3*.
    - Choisissez le **Nombre d'instances** à utiliser, par exemple, *1*.
    - Réglez le **Endpoint** sur **New** pour créer un point de terminaison.
    - Entrez un **Nom de point de terminaison**. Il doit être unique.
    - Entrez un **Nom de déploiement**. Il doit être unique.

    ![Remplir les paramètres de déploiement.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.fr.png)

1. Cliquez sur **Deploy**.

> [!WARNING]
> Pour éviter des frais supplémentaires sur votre compte, veillez à supprimer le point de terminaison créé dans l'espace de travail Azure Machine Learning.
>

#### Vérifier l'état du déploiement dans l'espace de travail Azure Machine Learning

1. Accédez à l'espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans le menu latéral gauche.

1. Sélectionnez le point de terminaison que vous avez créé.

    ![Sélectionnez les endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.fr.png)

1. Sur cette page, vous pouvez gérer les points de terminaison pendant le processus de déploiement.

> [!NOTE]
> Une fois le déploiement terminé, assurez-vous que **Live traffic** est réglé sur **100%**. Si ce n'est pas le cas, sélectionnez **Update traffic** pour ajuster les paramètres de trafic. Notez que vous ne pouvez pas tester le modèle si le trafic est réglé sur 0%.
>
> ![Configurer le trafic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.fr.png)
>

## Scénario 3 : Intégrer à Prompt flow et interagir avec votre modèle personnalisé dans Azure AI Foundry

### Intégrer le modèle personnalisé Phi-3 avec Prompt flow

Après avoir déployé avec succès votre modèle ajusté, vous pouvez maintenant l'intégrer à Prompt Flow pour l'utiliser dans des applications en temps réel, permettant une variété de tâches interactives avec votre modèle personnalisé Phi-3.

Dans cet exercice, vous allez :

- Créer un Hub Azure AI Foundry.
- Créer un Projet Azure AI Foundry.
- Créer un Prompt flow.
- Ajouter une connexion personnalisée pour le modèle ajusté Phi-3.
- Configurer Prompt flow pour interagir avec votre modèle personnalisé Phi-3.

> [!NOTE]
> Vous pouvez également intégrer à Prompt flow en utilisant Azure ML Studio. Le même processus d'intégration peut être appliqué dans Azure ML Studio.

#### Créer un Hub Azure AI Foundry

Vous devez créer un Hub avant de créer le Projet. Un Hub agit comme un groupe de ressources, vous permettant d'organiser et de gérer plusieurs Projets au sein d'Azure AI Foundry.

1. Rendez-vous sur [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Sélectionnez **All hubs** dans le menu latéral gauche.

1. Cliquez sur **+ New hub** dans le menu de navigation.

    ![Créer un hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.fr.png)

1. Effectuez les actions suivantes :

    - Entrez un **Nom de hub**. Il doit être unique.
    - Sélectionnez votre **Abonnement Azure**.
    - Choisissez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez la **Localisation** que vous souhaitez utiliser.
    - Réglez **Connect Azure AI Services** à utiliser (créez-en un nouveau si nécessaire).
    - Réglez **Connect Azure AI Search** sur **Skip connecting**.

    ![Remplir le hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.fr.png)

1. Cliquez sur **Next**.

#### Créer un Projet Azure AI Foundry

1. Dans le Hub que vous avez créé, sélectionnez **All projects** dans le menu latéral gauche.

1. Cliquez sur **+ New project** dans le menu de navigation.

    ![Sélectionner un nouveau projet.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.fr.png)

1. Entrez un **Nom de projet**. Il doit être unique.

    ![Créer un projet.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.fr.png)

1. Cliquez sur **Create a project**.

#### Ajouter une connexion personnalisée pour le modèle ajusté Phi-3

Pour intégrer votre modèle personnalisé Phi-3 avec Prompt flow, vous devez enregistrer le point de terminaison et la clé du modèle dans une connexion personnalisée. Cette configuration garantit l'accès à votre modèle personnalisé Phi-3 dans Prompt flow.

#### Configurer la clé API et l'URI du point de terminaison du modèle ajusté Phi-3

1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Accédez à l'espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans le menu latéral gauche.

    ![Sélectionner les endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.fr.png)

1. Sélectionnez le point de terminaison que vous avez créé.

    ![Sélectionner les endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.fr.png)

1. Cliquez sur **Consume** dans le menu de navigation.

1. Copiez votre **REST endpoint** et votre **Primary key**.
![Copiez la clé API et l'URI de point de terminaison.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.fr.png)

#### Ajouter la connexion personnalisée

1. Visitez [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Accédez au projet Azure AI Foundry que vous avez créé.

1. Dans le projet que vous avez créé, sélectionnez **Paramètres** dans le menu latéral gauche.

1. Sélectionnez **+ Nouvelle connexion**.

    ![Sélectionnez nouvelle connexion.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.fr.png)

1. Sélectionnez **Clés personnalisées** dans le menu de navigation.

    ![Sélectionnez clés personnalisées.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.fr.png)

1. Effectuez les tâches suivantes :

    - Sélectionnez **+ Ajouter des paires clé-valeur**.
    - Pour le nom de la clé, entrez **endpoint** et collez le point de terminaison que vous avez copié depuis Azure ML Studio dans le champ de valeur.
    - Sélectionnez à nouveau **+ Ajouter des paires clé-valeur**.
    - Pour le nom de la clé, entrez **key** et collez la clé que vous avez copiée depuis Azure ML Studio dans le champ de valeur.
    - Après avoir ajouté les clés, sélectionnez **est secret** pour empêcher que la clé ne soit exposée.

    ![Ajouter connexion.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.fr.png)

1. Sélectionnez **Ajouter connexion**.

#### Créer un flux Prompt

Vous avez ajouté une connexion personnalisée dans Azure AI Foundry. Passons maintenant à la création d’un flux Prompt en suivant les étapes ci-dessous. Ensuite, vous connecterez ce flux Prompt à la connexion personnalisée pour pouvoir utiliser le modèle ajusté dans le flux Prompt.

1. Accédez au projet Azure AI Foundry que vous avez créé.

1. Sélectionnez **Flux Prompt** dans le menu latéral gauche.

1. Sélectionnez **+ Créer** dans le menu de navigation.

    ![Sélectionnez Flux Prompt.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.fr.png)

1. Sélectionnez **Flux de chat** dans le menu de navigation.

    ![Sélectionnez flux de chat.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.fr.png)

1. Entrez **Nom du dossier** à utiliser.

    ![Entrez le nom.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.fr.png)

2. Sélectionnez **Créer**.

#### Configurer le flux Prompt pour dialoguer avec votre modèle Phi-3 personnalisé

Vous devez intégrer le modèle Phi-3 ajusté dans un flux Prompt. Cependant, le flux Prompt existant fourni n'est pas conçu à cet effet. Vous devez donc redéfinir le flux Prompt pour permettre l'intégration du modèle personnalisé.

1. Dans le flux Prompt, effectuez les tâches suivantes pour reconstruire le flux existant :

    - Sélectionnez **Mode fichier brut**.
    - Supprimez tout le code existant dans le fichier *flow.dag.yml*.
    - Ajoutez le code suivant au fichier *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Sélectionnez **Enregistrer**.

    ![Sélectionnez mode fichier brut.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.fr.png)

1. Ajoutez le code suivant au fichier *integrate_with_promptflow.py* pour utiliser le modèle Phi-3 personnalisé dans le flux Prompt.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Collez le code du flux Prompt.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.fr.png)

> [!NOTE]
> Pour des informations plus détaillées sur l'utilisation de Prompt flow dans Azure AI Foundry, vous pouvez consulter [Prompt flow dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Sélectionnez **Entrée chat**, **Sortie chat** pour activer le dialogue avec votre modèle.

    ![Entrée Sortie.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.fr.png)

1. Vous êtes maintenant prêt à dialoguer avec votre modèle Phi-3 personnalisé. Dans l'exercice suivant, vous apprendrez à démarrer Prompt flow et à l'utiliser pour dialoguer avec votre modèle ajusté Phi-3.

> [!NOTE]
>
> Le flux reconstruit devrait ressembler à l'image ci-dessous :
>
> ![Exemple de flux.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.fr.png)
>

### Dialoguer avec votre modèle Phi-3 personnalisé

Maintenant que vous avez ajusté et intégré votre modèle Phi-3 personnalisé avec Prompt flow, vous êtes prêt à commencer à interagir avec lui. Cet exercice vous guidera dans le processus de configuration et de démarrage d’un dialogue avec votre modèle à l’aide de Prompt flow. En suivant ces étapes, vous pourrez exploiter pleinement les capacités de votre modèle Phi-3 ajusté pour diverses tâches et conversations.

- Dialoguez avec votre modèle Phi-3 personnalisé à l’aide de Prompt flow.

#### Démarrer Prompt flow

1. Sélectionnez **Démarrer les sessions de calcul** pour démarrer Prompt flow.

    ![Démarrer session de calcul.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.fr.png)

1. Sélectionnez **Valider et analyser l'entrée** pour renouveler les paramètres.

    ![Valider l'entrée.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.fr.png)

1. Sélectionnez la **Valeur** de la **connexion** vers la connexion personnalisée que vous avez créée. Par exemple, *connection*.

    ![Connexion.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.fr.png)

#### Dialoguer avec votre modèle personnalisé

1. Sélectionnez **Chat**.

    ![Sélectionnez chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.fr.png)

1. Voici un exemple des résultats : Vous pouvez maintenant dialoguer avec votre modèle Phi-3 personnalisé. Il est recommandé de poser des questions basées sur les données utilisées pour l’ajustement.

    ![Dialogue avec flux Prompt.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.fr.png)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.