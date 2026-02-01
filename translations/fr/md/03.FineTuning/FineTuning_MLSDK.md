## Comment utiliser les composants de chat-completion du registre système Azure ML pour affiner un modèle

Dans cet exemple, nous allons effectuer un fine tuning du modèle Phi-3-mini-4k-instruct pour compléter une conversation entre 2 personnes en utilisant le jeu de données ultrachat_200k.

![MLFineTune](../../../../translated_images/fr/MLFineTune.928d4c6b3767dd35.webp)

Cet exemple vous montrera comment réaliser un fine tuning avec le SDK Azure ML et Python, puis déployer le modèle affiné sur un endpoint en ligne pour des inférences en temps réel.

### Données d'entraînement

Nous utiliserons le jeu de données ultrachat_200k. Il s'agit d'une version fortement filtrée du jeu UltraChat, utilisé pour entraîner Zephyr-7B-β, un modèle de chat 7b à la pointe de la technologie.

### Modèle

Nous utiliserons le modèle Phi-3-mini-4k-instruct pour montrer comment un utilisateur peut affiner un modèle pour une tâche de chat-completion. Si vous avez ouvert ce notebook depuis une fiche modèle spécifique, pensez à remplacer le nom du modèle.

### Tâches

- Choisir un modèle à affiner.
- Sélectionner et explorer les données d'entraînement.
- Configurer le job de fine tuning.
- Lancer le job de fine tuning.
- Examiner les métriques d'entraînement et d'évaluation.
- Enregistrer le modèle affiné.
- Déployer le modèle affiné pour des inférences en temps réel.
- Nettoyer les ressources.

## 1. Configuration des prérequis

- Installer les dépendances
- Se connecter à l’espace de travail AzureML. Pour en savoir plus, consultez la configuration de l’authentification SDK. Remplacez <WORKSPACE_NAME>, <RESOURCE_GROUP> et <SUBSCRIPTION_ID> ci-dessous.
- Se connecter au registre système azureml
- Définir un nom d’expérience optionnel
- Vérifier ou créer un compute.

> [!NOTE]
> Les exigences : un nœud GPU unique peut contenir plusieurs cartes GPU. Par exemple, un nœud Standard_NC24rs_v3 possède 4 GPU NVIDIA V100 tandis qu’un Standard_NC12s_v3 en possède 2. Consultez la documentation pour plus d’informations. Le nombre de cartes GPU par nœud est défini dans le paramètre gpus_per_node ci-dessous. Bien configurer cette valeur garantit l’utilisation de tous les GPU du nœud. Les SKU de compute GPU recommandés sont disponibles ici et ici.

### Bibliothèques Python

Installez les dépendances en exécutant la cellule ci-dessous. Cette étape n’est pas optionnelle si vous travaillez dans un nouvel environnement.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interaction avec Azure ML

1. Ce script Python sert à interagir avec le service Azure Machine Learning (Azure ML). Voici ce qu’il fait :

    - Il importe les modules nécessaires des packages azure.ai.ml, azure.identity et azure.ai.ml.entities. Il importe aussi le module time.

    - Il tente de s’authentifier avec DefaultAzureCredential(), qui simplifie l’authentification pour démarrer rapidement le développement d’applications dans le cloud Azure. En cas d’échec, il utilise InteractiveBrowserCredential(), qui propose une connexion interactive via navigateur.

    - Il essaie ensuite de créer une instance MLClient via la méthode from_config, qui lit la configuration dans le fichier config.json par défaut. En cas d’échec, il crée manuellement une instance MLClient en fournissant subscription_id, resource_group_name et workspace_name.

    - Il crée une autre instance MLClient, cette fois pour le registre Azure ML nommé "azureml". Ce registre stocke les modèles, pipelines de fine tuning et environnements.

    - Il définit experiment_name à "chat_completion_Phi-3-mini-4k-instruct".

    - Il génère un timestamp unique en convertissant le temps actuel (en secondes depuis l’époque, en float) en entier puis en chaîne. Ce timestamp peut servir à créer des noms et versions uniques.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. Choisir un modèle de base à affiner

1. Phi-3-mini-4k-instruct est un modèle léger de 3,8 milliards de paramètres, à la pointe, construit à partir des jeux de données utilisés pour Phi-2. Ce modèle appartient à la famille Phi-3, et la version Mini existe en deux variantes 4K et 128K, correspondant à la longueur de contexte (en tokens) qu’il peut gérer. Il faut affiner le modèle pour notre usage spécifique. Vous pouvez parcourir ces modèles dans le catalogue de modèles d’AzureML Studio, en filtrant par tâche de chat-completion. Dans cet exemple, nous utilisons Phi-3-mini-4k-instruct. Si vous avez ouvert ce notebook pour un autre modèle, remplacez le nom et la version du modèle en conséquence.

    > [!NOTE]
    > la propriété model id du modèle. Elle sera passée en entrée au job de fine tuning. Elle est aussi disponible dans le champ Asset ID de la page de détails du modèle dans le catalogue AzureML Studio.

2. Ce script Python interagit avec le service Azure Machine Learning (Azure ML). Voici ce qu’il fait :

    - Il définit model_name à "Phi-3-mini-4k-instruct".

    - Il utilise la méthode get de la propriété models de l’objet registry_ml_client pour récupérer la dernière version du modèle avec ce nom dans le registre Azure ML. La méthode get est appelée avec deux arguments : le nom du modèle et un label indiquant de récupérer la dernière version.

    - Il affiche un message dans la console indiquant le nom, la version et l’id du modèle utilisé pour le fine tuning. La méthode format de la chaîne insère ces valeurs. Le nom, la version et l’id sont accessibles via les propriétés de foundation_model.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Créer un compute à utiliser pour le job

Le job de fine tuning fonctionne UNIQUEMENT avec un compute GPU. La taille du compute dépend de la taille du modèle et il est souvent difficile de choisir le compute adapté. Dans cette cellule, nous guidons l’utilisateur pour sélectionner le compute adéquat.

> [!NOTE]
> Les computes listés ci-dessous fonctionnent avec la configuration la plus optimisée. Toute modification peut entraîner une erreur Cuda Out Of Memory. Dans ce cas, essayez de passer à un compute plus puissant.

> [!NOTE]
> Lors du choix de compute_cluster_size ci-dessous, assurez-vous que le compute est disponible dans votre groupe de ressources. Si un compute n’est pas disponible, vous pouvez faire une demande d’accès aux ressources compute.

### Vérification du support du modèle pour le fine tuning

1. Ce script Python interagit avec un modèle Azure Machine Learning (Azure ML). Voici ce qu’il fait :

    - Il importe le module ast, qui fournit des fonctions pour traiter les arbres de la grammaire abstraite Python.

    - Il vérifie si l’objet foundation_model (qui représente un modèle dans Azure ML) possède un tag nommé finetune_compute_allow_list. Les tags dans Azure ML sont des paires clé-valeur que vous pouvez créer et utiliser pour filtrer et trier les modèles.

    - Si le tag finetune_compute_allow_list est présent, il utilise ast.literal_eval pour analyser en toute sécurité la valeur du tag (une chaîne) en une liste Python. Cette liste est assignée à computes_allow_list. Il affiche ensuite un message indiquant qu’un compute doit être créé à partir de cette liste.

    - Si le tag n’est pas présent, il définit computes_allow_list à None et affiche un message indiquant que le tag finetune_compute_allow_list ne fait pas partie des tags du modèle.

    - En résumé, ce script vérifie la présence d’un tag spécifique dans les métadonnées du modèle, convertit sa valeur en liste si elle existe, et informe l’utilisateur.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Vérification de l’instance de compute

1. Ce script Python interagit avec Azure Machine Learning (Azure ML) et effectue plusieurs vérifications sur une instance de compute. Voici ce qu’il fait :

    - Il tente de récupérer l’instance de compute nommée compute_cluster depuis l’espace de travail Azure ML. Si l’état de provisioning est "failed", il lève une ValueError.

    - Il vérifie si computes_allow_list n’est pas None. Si c’est le cas, il convertit toutes les tailles de compute de la liste en minuscules et vérifie si la taille de l’instance actuelle est dans cette liste. Sinon, il lève une ValueError.

    - Si computes_allow_list est None, il vérifie si la taille de l’instance est dans une liste de tailles de VM GPU non supportées. Si oui, il lève une ValueError.

    - Il récupère la liste de toutes les tailles de compute disponibles dans l’espace de travail. Pour chaque taille, il vérifie si son nom correspond à la taille de l’instance actuelle. Si oui, il récupère le nombre de GPU pour cette taille et définit gpu_count_found à True.

    - Si gpu_count_found est True, il affiche le nombre de GPU de l’instance. Sinon, il lève une ValueError.

    - En résumé, ce script effectue plusieurs vérifications sur une instance de compute dans Azure ML, notamment son état, sa taille par rapport à une liste autorisée ou interdite, et le nombre de GPU.

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Choisir le jeu de données pour le fine tuning du modèle

1. Nous utilisons le jeu de données ultrachat_200k. Ce jeu est divisé en quatre parties, adaptées au fine tuning supervisé (sft).
Classement de génération (gen). Le nombre d’exemples par partie est indiqué ci-dessous :

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Les cellules suivantes montrent la préparation basique des données pour le fine tuning :

### Visualiser quelques lignes de données

Nous voulons que cet exemple s’exécute rapidement, donc nous sauvegardons les fichiers train_sft et test_sft contenant 5 % des lignes déjà filtrées. Cela signifie que le modèle affiné aura une précision moindre, il ne doit donc pas être utilisé en production.
Le script download-dataset.py sert à télécharger le jeu ultrachat_200k et à le transformer dans un format consommable par le pipeline de fine tuning. Comme le jeu est volumineux, nous n’en avons ici qu’une partie.

1. Le script ci-dessous télécharge seulement 5 % des données. Ce pourcentage peut être augmenté en modifiant le paramètre dataset_split_pc.

    > [!NOTE]
    > Certains modèles de langue ont des codes linguistiques différents, donc les noms de colonnes dans le jeu de données doivent refléter cela.

1. Voici un exemple de ce à quoi les données doivent ressembler
Le jeu de données chat-completion est stocké au format parquet, chaque entrée suivant le schéma suivant :

    - Il s’agit d’un document JSON (JavaScript Object Notation), un format d’échange de données populaire. Ce n’est pas du code exécutable, mais un moyen de stocker et transporter des données. Voici sa structure :

    - "prompt" : cette clé contient une chaîne représentant une tâche ou une question posée à un assistant IA.

    - "messages" : cette clé contient un tableau d’objets. Chaque objet représente un message dans une conversation entre un utilisateur et un assistant IA. Chaque message a deux clés :

    - "content" : chaîne représentant le contenu du message.
    - "role" : chaîne indiquant le rôle de l’entité ayant envoyé le message, soit "user" ou "assistant".
    - "prompt_id" : chaîne représentant un identifiant unique pour le prompt.

1. Dans ce document JSON spécifique, une conversation est représentée où un utilisateur demande à un assistant IA de créer un protagoniste pour une histoire dystopique. L’assistant répond, puis l’utilisateur demande plus de détails. L’assistant accepte de fournir plus d’informations. Toute la conversation est associée à un identifiant de prompt spécifique.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### Télécharger les données

1. Ce script Python sert à télécharger un jeu de données via un script auxiliaire nommé download-dataset.py. Voici ce qu’il fait :

    - Il importe le module os, qui fournit des fonctions pour interagir avec le système d’exploitation.

    - Il utilise os.system pour exécuter le script download-dataset.py dans le shell avec des arguments spécifiques. Ces arguments précisent le jeu à télécharger (HuggingFaceH4/ultrachat_200k), le répertoire de destination (ultrachat_200k_dataset) et le pourcentage de données à récupérer (5). La fonction os.system retourne le code de sortie de la commande, stocké dans exit_status.

    - Il vérifie si exit_status n’est pas 0. Sur les systèmes Unix, un code 0 signifie succès, tout autre code indique une erreur. En cas d’erreur, il lève une Exception avec un message indiquant un problème lors du téléchargement.

    - En résumé, ce script lance une commande pour télécharger un jeu de données via un script auxiliaire et lève une exception si la commande échoue.

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Charger les données dans un DataFrame

1. Ce script Python charge un fichier JSON Lines dans un DataFrame pandas et affiche les 5 premières lignes. Voici ce qu’il fait :

    - Il importe la bibliothèque pandas, puissante pour la manipulation et l’analyse de données.

    - Il définit la largeur maximale des colonnes dans l’affichage pandas à 0, ce qui signifie que le texte complet de chaque colonne sera affiché sans troncature.

    - Il utilise pd.read_json pour charger le fichier train_sft.jsonl du répertoire ultrachat_200k_dataset dans un DataFrame. L’argument lines=True indique que le fichier est au format JSON Lines, où chaque ligne est un objet JSON séparé.
- Il utilise la méthode head pour afficher les 5 premières lignes du DataFrame. Si le DataFrame contient moins de 5 lignes, il affichera toutes les lignes.

- En résumé, ce script charge un fichier JSON Lines dans un DataFrame et affiche les 5 premières lignes avec le texte complet des colonnes.

```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. Soumettre le travail de fine tuning en utilisant le modèle et les données comme entrées

Créez le travail qui utilise le composant pipeline de chat-completion. Découvrez tous les paramètres pris en charge pour le fine tuning.

### Définir les paramètres de fine tuning

1. Les paramètres de fine tuning peuvent être regroupés en 2 catégories : paramètres d'entraînement, paramètres d'optimisation.

1. Les paramètres d'entraînement définissent les aspects liés à l'entraînement tels que :

    - L'optimiseur, le scheduler à utiliser
    - La métrique à optimiser pour le fine tuning
    - Le nombre d'étapes d'entraînement, la taille des lots, etc.
    - Les paramètres d'optimisation aident à optimiser la mémoire GPU et à utiliser efficacement les ressources de calcul.

1. Voici quelques-uns des paramètres appartenant à cette catégorie. Les paramètres d'optimisation varient selon le modèle et sont intégrés avec le modèle pour gérer ces différences.

    - Activer deepspeed et LoRA
    - Activer l'entraînement en précision mixte
    - Activer l'entraînement multi-nœuds


> [!NOTE]
> Le fine tuning supervisé peut entraîner une perte d'alignement ou un oubli catastrophique. Nous recommandons de vérifier ce problème et d'exécuter une étape d'alignement après le fine tuning.

### Paramètres de Fine Tuning

1. Ce script Python configure les paramètres pour le fine tuning d'un modèle d'apprentissage automatique. Voici ce qu'il fait en détail :

    - Il définit les paramètres d'entraînement par défaut tels que le nombre d'époques, les tailles de lots pour l'entraînement et l'évaluation, le taux d'apprentissage, et le type de scheduler du taux d'apprentissage.

    - Il définit les paramètres d'optimisation par défaut, comme l'application de Layer-wise Relevance Propagation (LoRa) et DeepSpeed, ainsi que le stade DeepSpeed.

    - Il combine les paramètres d'entraînement et d'optimisation dans un dictionnaire unique appelé finetune_parameters.

    - Il vérifie si foundation_model possède des paramètres par défaut spécifiques au modèle. Si c'est le cas, il affiche un message d'avertissement et met à jour le dictionnaire finetune_parameters avec ces paramètres spécifiques. La fonction ast.literal_eval est utilisée pour convertir ces paramètres spécifiques du format chaîne en dictionnaire Python.

    - Il affiche l'ensemble final des paramètres de fine tuning qui seront utilisés pour l'exécution.

    - En résumé, ce script configure et affiche les paramètres pour le fine tuning d'un modèle d'apprentissage automatique, avec la possibilité de remplacer les paramètres par défaut par ceux spécifiques au modèle.

    ```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline d'entraînement

1. Ce script Python définit une fonction pour générer un nom d'affichage pour un pipeline d'entraînement en apprentissage automatique, puis appelle cette fonction pour générer et afficher ce nom. Voici ce qu'il fait en détail :

1. La fonction get_pipeline_display_name est définie. Cette fonction génère un nom d'affichage basé sur divers paramètres liés au pipeline d'entraînement.

1. À l'intérieur de la fonction, elle calcule la taille totale du lot en multipliant la taille du lot par appareil, le nombre d'étapes d'accumulation de gradients, le nombre de GPU par nœud, et le nombre de nœuds utilisés pour le fine tuning.

1. Elle récupère plusieurs autres paramètres tels que le type de scheduler du taux d'apprentissage, si DeepSpeed est appliqué, le stade DeepSpeed, si Layer-wise Relevance Propagation (LoRa) est appliqué, la limite du nombre de checkpoints du modèle à conserver, et la longueur maximale de la séquence.

1. Elle construit une chaîne de caractères incluant tous ces paramètres, séparés par des tirets. Si DeepSpeed ou LoRa est appliqué, la chaîne inclut "ds" suivi du stade DeepSpeed, ou "lora", respectivement. Sinon, elle inclut "nods" ou "nolora", respectivement.

1. La fonction retourne cette chaîne, qui sert de nom d'affichage pour le pipeline d'entraînement.

1. Après la définition de la fonction, elle est appelée pour générer le nom d'affichage, qui est ensuite affiché.

1. En résumé, ce script génère un nom d'affichage pour un pipeline d'entraînement en apprentissage automatique basé sur divers paramètres, puis affiche ce nom.

    ```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Configuration du Pipeline

Ce script Python définit et configure un pipeline d'apprentissage automatique en utilisant le SDK Azure Machine Learning. Voici ce qu'il fait en détail :

1. Il importe les modules nécessaires du SDK Azure AI ML.

1. Il récupère un composant pipeline nommé "chat_completion_pipeline" depuis le registre.

1. Il définit un travail pipeline en utilisant le décorateur `@pipeline` et la fonction `create_pipeline`. Le nom du pipeline est défini par `pipeline_display_name`.

1. À l'intérieur de la fonction `create_pipeline`, il initialise le composant pipeline récupéré avec divers paramètres, incluant le chemin du modèle, les clusters de calcul pour différentes étapes, les partitions de jeu de données pour l'entraînement et le test, le nombre de GPU à utiliser pour le fine tuning, et d'autres paramètres de fine tuning.

1. Il mappe la sortie du travail de fine tuning à la sortie du travail pipeline. Cela permet d'enregistrer facilement le modèle fine tuné, ce qui est nécessaire pour déployer le modèle sur un endpoint en ligne ou batch.

1. Il crée une instance du pipeline en appelant la fonction `create_pipeline`.

1. Il définit le paramètre `force_rerun` du pipeline à `True`, ce qui signifie que les résultats mis en cache des travaux précédents ne seront pas utilisés.

1. Il définit le paramètre `continue_on_step_failure` du pipeline à `False`, ce qui signifie que le pipeline s'arrêtera si une étape échoue.

1. En résumé, ce script définit et configure un pipeline d'apprentissage automatique pour une tâche de chat completion en utilisant le SDK Azure Machine Learning.

    ```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Soumettre le travail

1. Ce script Python soumet un travail pipeline d'apprentissage automatique à un workspace Azure Machine Learning, puis attend la fin du travail. Voici ce qu'il fait en détail :

    - Il appelle la méthode create_or_update de l'objet jobs dans workspace_ml_client pour soumettre le travail pipeline. Le pipeline à exécuter est spécifié par pipeline_object, et l'expérience sous laquelle le travail est lancé est spécifiée par experiment_name.

    - Il appelle ensuite la méthode stream de l'objet jobs dans workspace_ml_client pour attendre la fin du travail pipeline. Le travail à attendre est spécifié par l'attribut name de l'objet pipeline_job.

    - En résumé, ce script soumet un travail pipeline d'apprentissage automatique à un workspace Azure Machine Learning, puis attend la fin du travail.

    ```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Enregistrer le modèle fine tuné dans le workspace

Nous allons enregistrer le modèle issu de la sortie du travail de fine tuning. Cela permettra de suivre la filiation entre le modèle fine tuné et le travail de fine tuning. Ce dernier suit également la filiation avec le modèle de base, les données et le code d'entraînement.

### Enregistrement du modèle ML

1. Ce script Python enregistre un modèle d'apprentissage automatique entraîné dans un pipeline Azure Machine Learning. Voici ce qu'il fait en détail :

    - Il importe les modules nécessaires du SDK Azure AI ML.

    - Il vérifie si la sortie trained_model est disponible depuis le travail pipeline en appelant la méthode get de l'objet jobs dans workspace_ml_client et en accédant à son attribut outputs.

    - Il construit un chemin vers le modèle entraîné en formatant une chaîne avec le nom du travail pipeline et le nom de la sortie ("trained_model").

    - Il définit un nom pour le modèle fine tuné en ajoutant "-ultrachat-200k" au nom original du modèle et en remplaçant les slashs par des tirets.

    - Il prépare l'enregistrement du modèle en créant un objet Model avec divers paramètres, incluant le chemin vers le modèle, le type de modèle (modèle MLflow), le nom et la version du modèle, ainsi qu'une description.

    - Il enregistre le modèle en appelant la méthode create_or_update de l'objet models dans workspace_ml_client avec l'objet Model en argument.

    - Il affiche le modèle enregistré.

1. En résumé, ce script enregistre un modèle d'apprentissage automatique entraîné dans un pipeline Azure Machine Learning.

    ```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. Déployer le modèle fine tuné sur un endpoint en ligne

Les endpoints en ligne fournissent une API REST durable qui peut être utilisée pour intégrer des applications nécessitant d'utiliser le modèle.

### Gérer l'Endpoint

1. Ce script Python crée un endpoint en ligne géré dans Azure Machine Learning pour un modèle enregistré. Voici ce qu'il fait en détail :

    - Il importe les modules nécessaires du SDK Azure AI ML.

    - Il définit un nom unique pour l'endpoint en ligne en ajoutant un horodatage à la chaîne "ultrachat-completion-".

    - Il prépare la création de l'endpoint en ligne en créant un objet ManagedOnlineEndpoint avec divers paramètres, incluant le nom de l'endpoint, une description, et le mode d'authentification ("key").

    - Il crée l'endpoint en ligne en appelant la méthode begin_create_or_update de workspace_ml_client avec l'objet ManagedOnlineEndpoint en argument. Il attend ensuite la fin de l'opération en appelant la méthode wait.

1. En résumé, ce script crée un endpoint en ligne géré dans Azure Machine Learning pour un modèle enregistré.

    ```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Vous pouvez trouver ici la liste des SKU supportés pour le déploiement - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Déployer le modèle ML

1. Ce script Python déploie un modèle d'apprentissage automatique enregistré sur un endpoint en ligne géré dans Azure Machine Learning. Voici ce qu'il fait en détail :

    - Il importe le module ast, qui fournit des fonctions pour traiter les arbres de la grammaire abstraite Python.

    - Il définit le type d'instance pour le déploiement à "Standard_NC6s_v3".

    - Il vérifie si le tag inference_compute_allow_list est présent dans foundation_model. S'il l'est, il convertit la valeur du tag de chaîne en liste Python et l'assigne à inference_computes_allow_list. Sinon, il définit inference_computes_allow_list à None.

    - Il vérifie si le type d'instance spécifié est dans la liste autorisée. Sinon, il affiche un message demandant à l'utilisateur de choisir un type d'instance dans la liste autorisée.

    - Il prépare la création du déploiement en créant un objet ManagedOnlineDeployment avec divers paramètres, incluant le nom du déploiement, le nom de l'endpoint, l'ID du modèle, le type et le nombre d'instances, les paramètres du probe de vivacité, et les paramètres de requête.

    - Il crée le déploiement en appelant la méthode begin_create_or_update de workspace_ml_client avec l'objet ManagedOnlineDeployment en argument. Il attend ensuite la fin de l'opération en appelant la méthode wait.

    - Il configure le trafic de l'endpoint pour diriger 100 % du trafic vers le déploiement "demo".

    - Il met à jour l'endpoint en appelant la méthode begin_create_or_update de workspace_ml_client avec l'objet endpoint en argument. Il attend ensuite la fin de la mise à jour en appelant la méthode result.

1. En résumé, ce script déploie un modèle d'apprentissage automatique enregistré sur un endpoint en ligne géré dans Azure Machine Learning.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Tester l'endpoint avec des données d'exemple

Nous allons récupérer des données d'exemple depuis le jeu de test et les soumettre à l'endpoint en ligne pour inférence. Nous afficherons ensuite les labels prédits aux côtés des labels réels.

### Lecture des résultats

1. Ce script Python lit un fichier JSON Lines dans un DataFrame pandas, prend un échantillon aléatoire, et réinitialise l'index. Voici ce qu'il fait en détail :

    - Il lit le fichier ./ultrachat_200k_dataset/test_gen.jsonl dans un DataFrame pandas. La fonction read_json est utilisée avec l'argument lines=True car le fichier est au format JSON Lines, où chaque ligne est un objet JSON distinct.

    - Il prend un échantillon aléatoire d'une ligne dans le DataFrame. La fonction sample est utilisée avec l'argument n=1 pour spécifier le nombre de lignes aléatoires à sélectionner.

    - Il réinitialise l'index du DataFrame. La fonction reset_index est utilisée avec l'argument drop=True pour supprimer l'index original et le remplacer par un nouvel index d'entiers par défaut.

    - Il affiche les 2 premières lignes du DataFrame avec la fonction head(2). Cependant, comme le DataFrame ne contient qu'une seule ligne après l'échantillonnage, seule cette ligne sera affichée.

1. En résumé, ce script lit un fichier JSON Lines dans un DataFrame pandas, prend un échantillon aléatoire d'une ligne, réinitialise l'index, et affiche la première ligne.

    ```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### Créer un objet JSON

1. Ce script Python crée un objet JSON avec des paramètres spécifiques et l'enregistre dans un fichier. Voici ce qu'il fait en détail :

    - Il importe le module json, qui fournit des fonctions pour travailler avec des données JSON.

    - Il crée un dictionnaire parameters avec des clés et valeurs représentant des paramètres pour un modèle d'apprentissage automatique. Les clés sont "temperature", "top_p", "do_sample" et "max_new_tokens", avec pour valeurs respectives 0.6, 0.9, True, et 200.

    - Il crée un autre dictionnaire test_json avec deux clés : "input_data" et "params". La valeur de "input_data" est un autre dictionnaire avec les clés "input_string" et "parameters". La valeur de "input_string" est une liste contenant le premier message du DataFrame test_df. La valeur de "parameters" est le dictionnaire parameters créé précédemment. La valeur de "params" est un dictionnaire vide.
- Il ouvre un fichier nommé sample_score.json

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### Appel de l'endpoint

1. Ce script Python appelle un endpoint en ligne dans Azure Machine Learning pour évaluer un fichier JSON. Voici ce qu'il fait en détail :

    - Il utilise la méthode invoke de la propriété online_endpoints de l'objet workspace_ml_client. Cette méthode sert à envoyer une requête à un endpoint en ligne et à obtenir une réponse.

    - Il précise le nom de l'endpoint et du déploiement avec les arguments endpoint_name et deployment_name. Dans ce cas, le nom de l'endpoint est stocké dans la variable online_endpoint_name et le nom du déploiement est "demo".

    - Il indique le chemin vers le fichier JSON à évaluer avec l'argument request_file. Ici, le fichier est ./ultrachat_200k_dataset/sample_score.json.

    - Il stocke la réponse de l'endpoint dans la variable response.

    - Il affiche la réponse brute.

1. En résumé, ce script appelle un endpoint en ligne dans Azure Machine Learning pour évaluer un fichier JSON et affiche la réponse.

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. Supprimer l'endpoint en ligne

1. N'oubliez pas de supprimer l'endpoint en ligne, sinon vous continuerez à être facturé pour les ressources de calcul utilisées par l'endpoint. Cette ligne de code Python supprime un endpoint en ligne dans Azure Machine Learning. Voici ce qu'elle fait en détail :

    - Elle utilise la méthode begin_delete de la propriété online_endpoints de l'objet workspace_ml_client. Cette méthode sert à lancer la suppression d'un endpoint en ligne.

    - Elle précise le nom de l'endpoint à supprimer avec l'argument name. Dans ce cas, le nom de l'endpoint est stocké dans la variable online_endpoint_name.

    - Elle appelle la méthode wait pour attendre la fin de l'opération de suppression. C'est une opération bloquante, ce qui signifie que le script ne continuera pas tant que la suppression n'est pas terminée.

    - En résumé, cette ligne de code lance la suppression d'un endpoint en ligne dans Azure Machine Learning et attend la fin de l'opération.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.