<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-05-07T13:27:15+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "fr"
}
-->
## Bienvenue dans AI Toolkit pour VS Code

[AI Toolkit pour VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) regroupe plusieurs modèles issus du catalogue Azure AI Studio ainsi que d’autres catalogues comme Hugging Face. Cette boîte à outils simplifie les tâches courantes de développement pour créer des applications IA avec des outils et modèles d’IA générative grâce à :
- Découverte de modèles et espace de test pour débuter.
- Affinage et inférence de modèles en utilisant les ressources locales.
- Affinage et inférence à distance via les ressources Azure.

[Installer AI Toolkit pour VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.7157953df04812dced01c8815a5a4d4b139e6640cc19b1c7adb4eea15b5403e6.fr.png)


**[Private Preview]** Provisionnement en un clic pour Azure Container Apps afin d’exécuter l’affinage et l’inférence des modèles dans le cloud.

Passons maintenant au développement de votre application IA :

- [Bienvenue dans AI Toolkit pour VS Code](../../../../md/03.FineTuning)
- [Développement local](../../../../md/03.FineTuning)
  - [Préparatifs](../../../../md/03.FineTuning)
  - [Activation de Conda](../../../../md/03.FineTuning)
  - [Affinage du modèle de base uniquement](../../../../md/03.FineTuning)
  - [Affinage et inférence du modèle](../../../../md/03.FineTuning)
  - [Affinage du modèle](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Exemples et ressources d’affinage](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Développement à distance](../../../../md/03.FineTuning)
  - [Prérequis](../../../../md/03.FineTuning)
  - [Configuration d’un projet de développement à distance](../../../../md/03.FineTuning)
  - [Provisionnement des ressources Azure](../../../../md/03.FineTuning)
  - [\[Optionnel\] Ajout du token Huggingface au secret de l’Azure Container App](../../../../md/03.FineTuning)
  - [Lancer l’affinage](../../../../md/03.FineTuning)
  - [Provisionnement du point d’inférence](../../../../md/03.FineTuning)
  - [Déploiement du point d’inférence](../../../../md/03.FineTuning)
  - [Utilisation avancée](../../../../md/03.FineTuning)

## Développement local
### Préparatifs

1. Assurez-vous que le pilote NVIDIA est installé sur l’hôte.  
2. Exécutez `huggingface-cli login` si vous utilisez HF pour l’utilisation de datasets.  
3. `Olive` explications des paramètres clés pour tout ce qui modifie l’utilisation de la mémoire.

### Activation de Conda
Puisque nous utilisons un environnement WSL partagé, vous devez activer manuellement l’environnement conda. Après cette étape, vous pouvez lancer l’affinage ou l’inférence.

```bash
conda activate [conda-env-name] 
```

### Affinage du modèle de base uniquement
Pour simplement tester le modèle de base sans affinage, vous pouvez exécuter cette commande après avoir activé conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Affinage et inférence du modèle

Une fois l’espace de travail ouvert dans un conteneur de développement, ouvrez un terminal (le chemin par défaut est la racine du projet), puis lancez la commande ci-dessous pour affiner un LLM sur le dataset sélectionné.

```bash
python finetuning/invoke_olive.py 
```

Les checkpoints et le modèle final seront sauvegardés dans `models` folder.

Next run inferencing with the fune-tuned model through chats in a `console`, `web browser` or `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Pour utiliser `prompt flow` in VS Code, please refer to this [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Model Fine-tuning

Next, download the following model depending on the availability of a GPU on your device.

To initiate the local fine-tuning session using QLoRA, select a model you want to fine-tune from our catalog.
| Platform(s) | GPU available | Model name | Size (GB) |
|---------|---------|--------|--------|
| Windows | Yes | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Yes | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | No | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Note_** You do not need an Azure Account to download the models

The Phi3-mini (int4) model is approximately 2GB-3GB in size. Depending on your network speed, it could take a few minutes to download.

Start by selecting a project name and location.
Next, select a model from the model catalog. You will be prompted to download the project template. You can then click "Configure Project" to adjust various settings.

### Microsoft Olive 

We use [Olive](https://microsoft.github.io/Olive/why-olive.html) to run QLoRA fine-tuning on a PyTorch model from our catalog. All of the settings are preset with the default values to optimize to run the fine-tuning process locally with optimized use of memory, but it can be adjusted for your scenario.

### Fine Tuning Samples and Resoures

- [Fine tuning Getting Started Guide](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Fine tuning with a HuggingFace Dataset](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Fine tuning with Simple DataSet](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Remote Development

### Prerequisites

1. To run the model fine-tuning in your remote Azure Container App Environment, make sure your subscription has enough GPU capacity. Submit a [support ticket](https://azure.microsoft.com/support/create-ticket/) to request the required capacity for your application. [Get More Info about GPU capacity](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. If you are using private dataset on HuggingFace, make sure you have a [HuggingFace account](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) and [generate an access token](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. Enable Remote Fine-tuning and Inference feature flag in the AI Toolkit for VS Code
   1. Open the VS Code Settings by selecting *File -> Preferences -> Settings*.
   2. Navigate to *Extensions* and select *AI Toolkit*.
   3. Select the *"Enable Remote Fine-tuning And Inference"* option.
   4. Reload VS Code to take effect.

- [Remote Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Setting Up a Remote Development Project
1. Execute the command palette `AI Toolkit : Concentration sur la vue Ressources`.
2. Navigate to *Model Fine-tuning* to access the model catalog. Assign a name to your project and select its location on your machine. Then, hit the *"Configure Project"* button.
3. Project Configuration
    1. Avoid enabling the *"Fine-tune locally"* option.
    2. The Olive configuration settings will appear with pre-set default values. Please adjust and fill in these configurations as required.
    3. Move on to *Generate Project*. This stage leverages WSL and involves setting up a new Conda environment, preparing for future updates that include Dev Containers.
4. Click on *"Relaunch Window In Workspace"* to open your remote development project.

> **Note:** The project currently works either locally or remotely within the AI Toolkit for VS Code. If you choose *"Fine-tune locally"* during project creation, it will operate exclusively in WSL without remote development capabilities. On the other hand, if you forego enabling *"Fine-tune locally"*, the project will be restricted to the remote Azure Container App environment.

### Provision Azure Resources
To get started, you need to provision the Azure Resource for remote fine-tuning. Do this by running the `AI Toolkit : Provisionnement Azure Container Apps pour l’affinage` from the command palette.

Monitor the progress of the provision through the link displayed in the output channel.

### [Optional] Add Huggingface Token to the Azure Container App Secret
If you're using private HuggingFace dataset, set your HuggingFace token as an environment variable to avoid the need for manual login on the Hugging Face Hub.
You can do this using the `AI Toolkit : Ajout du secret Azure Container Apps pour l’affinage`. With this command, you can set the secret name as [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) and use your Hugging Face token as the secret value.

### Run Fine-tuning
To start the remote fine-tuning job, execute the `AI Toolkit : Lancer l’affinage` command.

To view the system and console logs, you can visit the Azure portal using the link in the output panel (more steps at [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Or, you can view the console logs directly in the VSCode output panel by running the command `AI Toolkit : Afficher les logs en streaming de la tâche d’affinage en cours`. 
> **Note:** The job might be queued due to insufficient resources. If the log is not displayed, execute the `AI Toolkit : Afficher les logs en streaming de la tâche d’affinage en cours` command, wait for a while and then execute the command again to re-connect to the streaming log.

During this process, QLoRA will be used for fine-tuning, and will create LoRA adapters for the model to use during inference.
The results of the fine-tuning will be stored in the Azure Files.

### Provision Inference Endpoint
After the adapters are trained in the remote environment, use a simple Gradio application to interact with the model.
Similar to the fine-tuning process, you need to set up the Azure Resources for remote inference by executing the `AI Toolkit : Provisionnement Azure Container Apps pour l’inférence` from the command palette.

By default, the subscription and the resource group for inference should match those used for fine-tuning. The inference will use the same Azure Container App Environment and access the model and model adapter stored in Azure Files, which were generated during the fine-tuning step. 


### Deploy the Inference Endpoint
If you wish to revise the inference code or reload the inference model, please execute the `AI Toolkit : Déploiement pour l’inférence` command. This will synchronize your latest code with Azure Container App and restart the replica.  

Once deployment is successfully completed, you can access the inference API by clicking on the "*Go to Inference Endpoint*" button displayed in the VSCode notification. Or, the web API endpoint can be found under `ACA_APP_ENDPOINT` in `./infra/inference.config.json` et dans le panneau de sortie. Vous êtes maintenant prêt à évaluer le modèle via ce point d’accès.

### Utilisation avancée
Pour plus d’informations sur le développement à distance avec AI Toolkit, consultez la documentation [Affinage des modèles à distance](https://aka.ms/ai-toolkit/remote-provision) et [Inférence avec le modèle affiné](https://aka.ms/ai-toolkit/remote-inference).

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.