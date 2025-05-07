<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-07T14:12:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "fr"
}
-->
# Affiner et Intégrer des modèles Phi-3 personnalisés avec Prompt flow dans Azure AI Foundry

Cet exemple de bout en bout (E2E) est basé sur le guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" de la communauté technique Microsoft. Il présente les étapes d’affinage, de déploiement et d’intégration des modèles Phi-3 personnalisés avec Prompt flow dans Azure AI Foundry. Contrairement à l’exemple E2E "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", qui nécessitait d’exécuter du code localement, ce tutoriel se concentre entièrement sur l’affinage et l’intégration de votre modèle dans Azure AI / ML Studio.

## Vue d’ensemble

Dans cet exemple E2E, vous apprendrez à affiner le modèle Phi-3 et à l’intégrer avec Prompt flow dans Azure AI Foundry. En utilisant Azure AI / ML Studio, vous établirez un flux de travail pour déployer et exploiter des modèles d’IA personnalisés. Cet exemple E2E est divisé en trois scénarios :

**Scénario 1 : Configurer les ressources Azure et préparer l’affinage**

**Scénario 2 : Affiner le modèle Phi-3 et déployer dans Azure Machine Learning Studio**

**Scénario 3 : Intégrer avec Prompt flow et discuter avec votre modèle personnalisé dans Azure AI Foundry**

Voici un aperçu de cet exemple E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.fr.png)

### Table des matières

1. **[Scénario 1 : Configurer les ressources Azure et préparer l’affinage](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Créer un espace de travail Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Demander des quotas GPU dans l’abonnement Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ajouter une affectation de rôle](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurer le projet](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Préparer le jeu de données pour l’affinage](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scénario 2 : Affiner le modèle Phi-3 et déployer dans Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Affiner le modèle Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Déployer le modèle Phi-3 affiné](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scénario 3 : Intégrer avec Prompt flow et discuter avec votre modèle personnalisé dans Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Intégrer le modèle Phi-3 personnalisé avec Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Discuter avec votre modèle Phi-3 personnalisé](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scénario 1 : Configurer les ressources Azure et préparer l’affinage

### Créer un espace de travail Azure Machine Learning

1. Tapez *azure machine learning* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Azure Machine Learning** parmi les options proposées.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.fr.png)

2. Sélectionnez **+ Create** dans le menu de navigation.

3. Sélectionnez **New workspace** dans le menu de navigation.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.fr.png)

4. Effectuez les tâches suivantes :

    - Sélectionnez votre **Subscription** Azure.
    - Sélectionnez le **Resource group** à utiliser (créez-en un nouveau si nécessaire).
    - Saisissez un **Workspace Name**. Il doit être unique.
    - Sélectionnez la **Region** que vous souhaitez utiliser.
    - Sélectionnez le **Storage account** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez le **Key vault** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez **Application insights** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez le **Container registry** à utiliser (créez-en un nouveau si nécessaire).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.fr.png)

5. Sélectionnez **Review + Create**.

6. Sélectionnez **Create**.

### Demander des quotas GPU dans l’abonnement Azure

Dans ce tutoriel, vous apprendrez à affiner et déployer un modèle Phi-3 en utilisant des GPU. Pour l’affinage, vous utiliserez le GPU *Standard_NC24ads_A100_v4*, qui nécessite une demande de quota. Pour le déploiement, vous utiliserez le GPU *Standard_NC6s_v3*, qui nécessite également une demande de quota.

> [!NOTE]
>
> Seules les subscriptions Pay-As-You-Go (type standard) sont éligibles à l’allocation GPU ; les subscriptions avantage ne sont pas prises en charge pour le moment.
>

1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Effectuez les opérations suivantes pour demander un quota *Standard NCADSA100v4 Family* :

    - Sélectionnez **Quota** dans l’onglet latéral gauche.
    - Sélectionnez la **Virtual machine family** à utiliser. Par exemple, sélectionnez **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, qui inclut le GPU *Standard_NC24ads_A100_v4*.
    - Sélectionnez **Request quota** dans le menu de navigation.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.fr.png)

    - Dans la page Request quota, saisissez la **New cores limit** que vous souhaitez. Par exemple, 24.
    - Dans la page Request quota, sélectionnez **Submit** pour envoyer la demande de quota GPU.

1. Effectuez les opérations suivantes pour demander un quota *Standard NCSv3 Family* :

    - Sélectionnez **Quota** dans l’onglet latéral gauche.
    - Sélectionnez la **Virtual machine family** à utiliser. Par exemple, sélectionnez **Standard NCSv3 Family Cluster Dedicated vCPUs**, qui inclut le GPU *Standard_NC6s_v3*.
    - Sélectionnez **Request quota** dans le menu de navigation.
    - Dans la page Request quota, saisissez la **New cores limit** que vous souhaitez. Par exemple, 24.
    - Dans la page Request quota, sélectionnez **Submit** pour envoyer la demande de quota GPU.

### Ajouter une affectation de rôle

Pour affiner et déployer vos modèles, vous devez d’abord créer une identité gérée attribuée par l’utilisateur (User Assigned Managed Identity - UAI) et lui attribuer les permissions appropriées. Cette UAI sera utilisée pour l’authentification lors du déploiement.

#### Créer une User Assigned Managed Identity (UAI)

1. Tapez *managed identities* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Managed Identities** parmi les options proposées.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.fr.png)

1. Sélectionnez **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.fr.png)

1. Effectuez les tâches suivantes :

    - Sélectionnez votre **Subscription** Azure.
    - Sélectionnez le **Resource group** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez la **Region** que vous souhaitez utiliser.
    - Saisissez un **Name**. Il doit être unique.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.fr.png)

1. Sélectionnez **Review + create**.

1. Sélectionnez **+ Create**.

#### Ajouter une affectation de rôle Contributor à la Managed Identity

1. Accédez à la ressource Managed Identity que vous avez créée.

1. Sélectionnez **Azure role assignments** dans l’onglet latéral gauche.

1. Sélectionnez **+ Add role assignment** dans le menu de navigation.

1. Dans la page Add role assignment, effectuez les tâches suivantes :
    - Sélectionnez le **Scope** sur **Resource group**.
    - Sélectionnez votre **Subscription** Azure.
    - Sélectionnez le **Resource group** à utiliser.
    - Sélectionnez le **Role** **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.fr.png)

2. Sélectionnez **Save**.

#### Ajouter une affectation de rôle Storage Blob Data Reader à la Managed Identity

1. Tapez *storage accounts* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Storage accounts** parmi les options proposées.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.fr.png)

1. Sélectionnez le compte de stockage associé à l’espace de travail Azure Machine Learning que vous avez créé. Par exemple, *finetunephistorage*.

1. Effectuez les opérations suivantes pour accéder à la page Add role assignment :

    - Accédez au compte de stockage Azure que vous avez créé.
    - Sélectionnez **Access Control (IAM)** dans l’onglet latéral gauche.
    - Sélectionnez **+ Add** dans le menu de navigation.
    - Sélectionnez **Add role assignment** dans le menu de navigation.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.fr.png)

1. Dans la page Add role assignment, effectuez les tâches suivantes :

    - Dans la page Role, tapez *Storage Blob Data Reader* dans la **barre de recherche** et sélectionnez **Storage Blob Data Reader** parmi les options proposées.
    - Dans la page Role, sélectionnez **Next**.
    - Dans la page Members, sélectionnez **Assign access to** **Managed identity**.
    - Dans la page Members, sélectionnez **+ Select members**.
    - Dans la page Select managed identities, sélectionnez votre **Subscription** Azure.
    - Dans la page Select managed identities, sélectionnez la **Managed identity** à **Manage Identity**.
    - Dans la page Select managed identities, sélectionnez la Managed Identity que vous avez créée. Par exemple, *finetunephi-managedidentity*.
    - Dans la page Select managed identities, sélectionnez **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.fr.png)

1. Sélectionnez **Review + assign**.

#### Ajouter une affectation de rôle AcrPull à la Managed Identity

1. Tapez *container registries* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Container registries** parmi les options proposées.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.fr.png)

1. Sélectionnez le registre de conteneurs associé à l’espace de travail Azure Machine Learning. Par exemple, *finetunephicontainerregistry*

1. Effectuez les opérations suivantes pour accéder à la page Add role assignment :

    - Sélectionnez **Access Control (IAM)** dans l’onglet latéral gauche.
    - Sélectionnez **+ Add** dans le menu de navigation.
    - Sélectionnez **Add role assignment** dans le menu de navigation.

1. Dans la page Add role assignment, effectuez les tâches suivantes :

    - Dans la page Role, tapez *AcrPull* dans la **barre de recherche** et sélectionnez **AcrPull** parmi les options proposées.
    - Dans la page Role, sélectionnez **Next**.
    - Dans la page Members, sélectionnez **Assign access to** **Managed identity**.
    - Dans la page Members, sélectionnez **+ Select members**.
    - Dans la page Select managed identities, sélectionnez votre **Subscription** Azure.
    - Dans la page Select managed identities, sélectionnez la **Managed identity** à **Manage Identity**.
    - Dans la page Select managed identities, sélectionnez la Managed Identity que vous avez créée. Par exemple, *finetunephi-managedidentity*.
    - Dans la page Select managed identities, sélectionnez **Select**.
    - Sélectionnez **Review + assign**.

### Configurer le projet

Pour télécharger les jeux de données nécessaires à l’affinage, vous allez configurer un environnement local.

Dans cet exercice, vous allez :

- Créer un dossier pour travailler à l’intérieur.
- Créer un environnement virtuel.
- Installer les packages requis.
- Créer un fichier *download_dataset.py* pour télécharger le jeu de données.

#### Créer un dossier pour travailler à l’intérieur

1. Ouvrez une fenêtre de terminal et tapez la commande suivante pour créer un dossier nommé *finetune-phi* dans le chemin par défaut.

    ```console
    mkdir finetune-phi
    ```

2. Tapez la commande suivante dans votre terminal pour naviguer vers le dossier *finetune-phi* que vous avez créé.

    ```console
    cd finetune-phi
    ```

#### Créer un environnement virtuel

1. Tapez la commande suivante dans votre terminal pour créer un environnement virtuel nommé *.venv*.

    ```console
    python -m venv .venv
    ```

2. Tapez la commande suivante dans votre terminal pour activer l’environnement virtuel.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Si cela fonctionne, vous devriez voir *(.venv)* avant l’invite de commande.

#### Installer les packages requis

1. Tapez les commandes suivantes dans votre terminal pour installer les packages requis.

    ```console
    pip install datasets==2.19.1
    ```

#### Créer `download_dataset.py`

> [!NOTE]
> Structure complète du dossier :
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Ouvrez **Visual Studio Code**.

1. Sélectionnez **File** dans la barre de menu.

1. Sélectionnez **Open Folder**.

1. Sélectionnez le dossier *finetune-phi* que vous avez créé, situé à *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.fr.png)

1. Dans le volet de gauche de Visual Studio Code, faites un clic droit et sélectionnez **New File** pour créer un nouveau fichier nommé *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.fr.png)

### Préparer le jeu de données pour l’affinage

Dans cet exercice, vous allez exécuter le fichier *download_dataset.py* pour télécharger les jeux de données *ultrachat_200k* dans votre environnement local. Vous utiliserez ensuite ces jeux de données pour affiner le modèle Phi-3 dans Azure Machine Learning.

Dans cet exercice, vous allez :

- Ajouter du code dans le fichier *download_dataset.py* pour télécharger les jeux de données.
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
> #### Remarque sur la taille du jeu de données et le temps d’affinage
>
> Dans ce tutoriel, vous n’utilisez que 1 % du jeu de données (`split='train[:1%]'`). Cela réduit considérablement la quantité de données, accélérant à la fois l’upload et l’affinage. Vous pouvez ajuster ce pourcentage pour trouver le bon équilibre entre le temps d’entraînement et la performance du modèle. Utiliser un sous-ensemble plus petit du jeu de données réduit le temps nécessaire à l’affinage, rendant le processus plus facile à gérer dans un tutoriel.

## Scénario 2 : Affiner le modèle Phi-3 et déployer dans Azure Machine Learning Studio

### Affiner le modèle Phi-3

Dans cet exercice, vous allez affiner le modèle Phi-3 dans Azure Machine Learning Studio.

Dans cet exercice, vous allez :

- Créer un cluster informatique pour l’affinage.
- Affiner le modèle Phi-3 dans Azure Machine Learning Studio.

#### Créer un cluster informatique pour l’affinage
1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Sélectionnez **Compute** dans l’onglet de gauche.

1. Sélectionnez **Compute clusters** dans le menu de navigation.

1. Cliquez sur **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.fr.png)

1. Effectuez les actions suivantes :

    - Choisissez la **Région** que vous souhaitez utiliser.
    - Sélectionnez le **Niveau de machine virtuelle** sur **Dedicated**.
    - Sélectionnez le **Type de machine virtuelle** sur **GPU**.
    - Filtrez la **Taille de machine virtuelle** sur **Select from all options**.
    - Sélectionnez la **Taille de machine virtuelle** sur **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.fr.png)

1. Cliquez sur **Next**.

1. Effectuez les actions suivantes :

    - Saisissez un **Nom du compute**. Il doit être unique.
    - Définissez le **Nombre minimum de nœuds** à **0**.
    - Définissez le **Nombre maximum de nœuds** à **1**.
    - Définissez le **Temps d’inactivité avant réduction d’échelle** à **120** secondes.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.fr.png)

1. Cliquez sur **Create**.

#### Affiner le modèle Phi-3

1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Sélectionnez l’espace de travail Azure Machine Learning que vous avez créé.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.fr.png)

1. Effectuez les actions suivantes :

    - Sélectionnez **Model catalog** dans l’onglet de gauche.
    - Tapez *phi-3-mini-4k* dans la **barre de recherche** et choisissez **Phi-3-mini-4k-instruct** parmi les options proposées.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.fr.png)

1. Sélectionnez **Fine-tune** dans le menu de navigation.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.fr.png)

1. Effectuez les actions suivantes :

    - Choisissez **Select task type** sur **Chat completion**.
    - Cliquez sur **+ Select data** pour importer les **données d’entraînement**.
    - Pour le type de données de validation, sélectionnez **Provide different validation data**.
    - Cliquez sur **+ Select data** pour importer les **données de validation**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.fr.png)

    > [!TIP]
    >
    > Vous pouvez sélectionner **Advanced settings** pour personnaliser des paramètres comme **learning_rate** et **lr_scheduler_type** afin d’optimiser le processus de fine-tuning selon vos besoins.

1. Cliquez sur **Finish**.

1. Dans cet exercice, vous avez affiné avec succès le modèle Phi-3 en utilisant Azure Machine Learning. Notez que le processus de fine-tuning peut prendre un certain temps. Après avoir lancé la tâche, il faut attendre sa complétion. Vous pouvez suivre l’état de la tâche dans l’onglet Jobs à gauche de votre espace de travail Azure Machine Learning. Dans la prochaine série, vous déploierez le modèle affiné et l’intégrerez avec Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.fr.png)

### Déployer le modèle Phi-3 affiné

Pour intégrer le modèle Phi-3 affiné avec Prompt flow, vous devez déployer le modèle afin qu’il soit accessible pour des inférences en temps réel. Ce processus comprend l’enregistrement du modèle, la création d’un endpoint en ligne, puis le déploiement du modèle.

Dans cet exercice, vous allez :

- Enregistrer le modèle affiné dans l’espace de travail Azure Machine Learning.
- Créer un endpoint en ligne.
- Déployer le modèle Phi-3 affiné enregistré.

#### Enregistrer le modèle affiné

1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Sélectionnez l’espace de travail Azure Machine Learning que vous avez créé.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.fr.png)

1. Sélectionnez **Models** dans l’onglet de gauche.
1. Cliquez sur **+ Register**.
1. Sélectionnez **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.fr.png)

1. Choisissez la tâche que vous avez créée.

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.fr.png)

1. Cliquez sur **Next**.

1. Choisissez **Model type** sur **MLflow**.

1. Vérifiez que **Job output** est sélectionné ; cela devrait être automatique.

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.fr.png)

2. Cliquez sur **Next**.

3. Cliquez sur **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.fr.png)

4. Vous pouvez consulter votre modèle enregistré en allant dans le menu **Models** à gauche.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.fr.png)

#### Déployer le modèle affiné

1. Accédez à l’espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans l’onglet de gauche.

1. Sélectionnez **Real-time endpoints** dans le menu de navigation.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.fr.png)

1. Cliquez sur **Create**.

1. Sélectionnez le modèle enregistré que vous avez créé.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.fr.png)

1. Cliquez sur **Select**.

1. Effectuez les actions suivantes :

    - Choisissez la **Machine virtuelle** *Standard_NC6s_v3*.
    - Sélectionnez le **Nombre d’instances** souhaité, par exemple *1*.
    - Pour **Endpoint**, choisissez **New** afin de créer un nouvel endpoint.
    - Saisissez un **Nom d’endpoint** unique.
    - Saisissez un **Nom de déploiement** unique.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.fr.png)

1. Cliquez sur **Deploy**.

> [!WARNING]
> Pour éviter des frais supplémentaires, pensez à supprimer l’endpoint créé dans l’espace de travail Azure Machine Learning lorsque vous n’en avez plus besoin.
>

#### Vérifier le statut du déploiement dans Azure Machine Learning Workspace

1. Accédez à l’espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans l’onglet de gauche.

1. Sélectionnez l’endpoint que vous avez créé.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.fr.png)

1. Sur cette page, vous pouvez gérer les endpoints pendant le déploiement.

> [!NOTE]
> Une fois le déploiement terminé, assurez-vous que le **Live traffic** est réglé à **100%**. Sinon, cliquez sur **Update traffic** pour ajuster le trafic. Notez que vous ne pouvez pas tester le modèle si le trafic est à 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.fr.png)
>

## Scénario 3 : Intégrer avec Prompt flow et discuter avec votre modèle personnalisé dans Azure AI Foundry

### Intégrer le modèle Phi-3 personnalisé avec Prompt flow

Après avoir déployé avec succès votre modèle affiné, vous pouvez maintenant l’intégrer à Prompt Flow pour l’utiliser dans des applications en temps réel, permettant ainsi diverses interactions avec votre modèle Phi-3 personnalisé.

Dans cet exercice, vous allez :

- Créer un Hub Azure AI Foundry.
- Créer un Projet Azure AI Foundry.
- Créer un Prompt flow.
- Ajouter une connexion personnalisée pour le modèle Phi-3 affiné.
- Configurer Prompt flow pour discuter avec votre modèle Phi-3 personnalisé.

> [!NOTE]
> Vous pouvez aussi intégrer Promptflow en utilisant Azure ML Studio. Le même processus d’intégration s’applique à Azure ML Studio.

#### Créer un Hub Azure AI Foundry

Vous devez créer un Hub avant de créer un Projet. Un Hub fonctionne comme un groupe de ressources, vous permettant d’organiser et de gérer plusieurs projets dans Azure AI Foundry.

1. Rendez-vous sur [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Sélectionnez **All hubs** dans l’onglet de gauche.

1. Cliquez sur **+ New hub** dans le menu de navigation.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.fr.png)

1. Effectuez les actions suivantes :

    - Saisissez un **Nom du Hub** unique.
    - Sélectionnez votre **Abonnement** Azure.
    - Choisissez le **Groupe de ressources** à utiliser (ou créez-en un nouveau).
    - Sélectionnez la **Région** souhaitée.
    - Sélectionnez les **Services Azure AI à connecter** (ou créez-en un nouveau).
    - Pour **Connect Azure AI Search**, choisissez **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.fr.png)

1. Cliquez sur **Next**.

#### Créer un Projet Azure AI Foundry

1. Dans le Hub que vous avez créé, sélectionnez **All projects** dans l’onglet de gauche.

1. Cliquez sur **+ New project** dans le menu de navigation.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.fr.png)

1. Saisissez un **Nom du projet** unique.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.fr.png)

1. Cliquez sur **Create a project**.

#### Ajouter une connexion personnalisée pour le modèle Phi-3 affiné

Pour intégrer votre modèle Phi-3 personnalisé avec Prompt flow, vous devez enregistrer l’endpoint et la clé du modèle dans une connexion personnalisée. Cette configuration garantit l’accès à votre modèle Phi-3 personnalisé dans Prompt flow.

#### Configurer la clé API et l’URI de l’endpoint du modèle Phi-3 affiné

1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Accédez à l’espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans l’onglet de gauche.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.fr.png)

1. Sélectionnez l’endpoint que vous avez créé.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.fr.png)

1. Sélectionnez **Consume** dans le menu de navigation.

1. Copiez votre **REST endpoint** et votre **clé primaire**.
![Copiez la clé API et l’URI de point de terminaison.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.fr.png)

#### Ajouter la connexion personnalisée

1. Rendez-vous sur [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Accédez au projet Azure AI Foundry que vous avez créé.

1. Dans le projet que vous avez créé, sélectionnez **Settings** dans l’onglet à gauche.

1. Sélectionnez **+ New connection**.

    ![Sélectionnez nouvelle connexion.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.fr.png)

1. Sélectionnez **Custom keys** dans le menu de navigation.

    ![Sélectionnez clés personnalisées.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.fr.png)

1. Effectuez les opérations suivantes :

    - Sélectionnez **+ Add key value pairs**.
    - Pour le nom de la clé, saisissez **endpoint** et collez le point de terminaison que vous avez copié depuis Azure ML Studio dans le champ de valeur.
    - Sélectionnez à nouveau **+ Add key value pairs**.
    - Pour le nom de la clé, saisissez **key** et collez la clé que vous avez copiée depuis Azure ML Studio dans le champ de valeur.
    - Après avoir ajouté les clés, cochez **is secret** pour empêcher que la clé soit exposée.

    ![Ajouter la connexion.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.fr.png)

1. Sélectionnez **Add connection**.

#### Créer un Prompt flow

Vous avez ajouté une connexion personnalisée dans Azure AI Foundry. Maintenant, créons un Prompt flow en suivant les étapes ci-dessous. Ensuite, vous connecterez ce Prompt flow à la connexion personnalisée afin de pouvoir utiliser le modèle affiné dans le Prompt flow.

1. Accédez au projet Azure AI Foundry que vous avez créé.

1. Sélectionnez **Prompt flow** dans l’onglet à gauche.

1. Sélectionnez **+ Create** dans le menu de navigation.

    ![Sélectionnez Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.fr.png)

1. Sélectionnez **Chat flow** dans le menu de navigation.

    ![Sélectionnez chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.fr.png)

1. Saisissez le **nom du dossier** à utiliser.

    ![Saisissez le nom.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.fr.png)

2. Sélectionnez **Create**.

#### Configurer le Prompt flow pour discuter avec votre modèle Phi-3 personnalisé

Vous devez intégrer le modèle Phi-3 affiné dans un Prompt flow. Cependant, le Prompt flow existant fourni n’est pas conçu pour cet usage. Vous devez donc repenser le Prompt flow pour permettre l’intégration du modèle personnalisé.

1. Dans le Prompt flow, effectuez les opérations suivantes pour reconstruire le flux existant :

    - Sélectionnez **Raw file mode**.
    - Supprimez tout le code existant dans le fichier *flow.dag.yml*.
    - Ajoutez le code suivant dans le fichier *flow.dag.yml*.

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

    - Sélectionnez **Save**.

    ![Sélectionnez le mode fichier brut.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.fr.png)

1. Ajoutez le code suivant dans le fichier *integrate_with_promptflow.py* pour utiliser le modèle Phi-3 personnalisé dans Prompt flow.

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

    ![Collez le code du prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.fr.png)

> [!NOTE]
> Pour plus d’informations détaillées sur l’utilisation de Prompt flow dans Azure AI Foundry, vous pouvez consulter [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Sélectionnez **Chat input**, **Chat output** pour activer la conversation avec votre modèle.

    ![Entrée et sortie.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.fr.png)

1. Vous êtes maintenant prêt à discuter avec votre modèle Phi-3 personnalisé. Dans l’exercice suivant, vous apprendrez comment démarrer Prompt flow et l’utiliser pour discuter avec votre modèle Phi-3 affiné.

> [!NOTE]
>
> Le flux reconstruit devrait ressembler à l’image ci-dessous :
>
> ![Exemple de flux.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.fr.png)
>

### Discuter avec votre modèle Phi-3 personnalisé

Maintenant que vous avez affiné et intégré votre modèle Phi-3 personnalisé avec Prompt flow, vous êtes prêt à commencer à interagir avec lui. Cet exercice vous guidera dans le processus de configuration et de démarrage d’une conversation avec votre modèle via Prompt flow. En suivant ces étapes, vous pourrez exploiter pleinement les capacités de votre modèle Phi-3 affiné pour diverses tâches et échanges.

- Discutez avec votre modèle Phi-3 personnalisé en utilisant Prompt flow.

#### Démarrer Prompt flow

1. Sélectionnez **Start compute sessions** pour lancer Prompt flow.

    ![Démarrer la session de calcul.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.fr.png)

1. Sélectionnez **Validate and parse input** pour actualiser les paramètres.

    ![Valider l’entrée.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.fr.png)

1. Sélectionnez la **Valeur** de la **connection** correspondant à la connexion personnalisée que vous avez créée. Par exemple, *connection*.

    ![Connexion.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.fr.png)

#### Discuter avec votre modèle personnalisé

1. Sélectionnez **Chat**.

    ![Sélectionnez chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.fr.png)

1. Voici un exemple de résultats : vous pouvez maintenant discuter avec votre modèle Phi-3 personnalisé. Il est recommandé de poser des questions basées sur les données utilisées pour l’affinage.

    ![Discussion avec prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.fr.png)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.