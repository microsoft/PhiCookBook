# Laboratoire. Optimiser les modèles d’IA pour l’inférence sur appareil

## Introduction

> [!IMPORTANT]  
> Ce laboratoire nécessite un **GPU Nvidia A10 ou A100** avec les pilotes associés et le toolkit CUDA (version 12+) installés.

> [!NOTE]  
> Il s’agit d’un laboratoire de **35 minutes** qui vous offrira une introduction pratique aux concepts clés de l’optimisation des modèles pour l’inférence sur appareil à l’aide d’OLIVE.

## Objectifs d’apprentissage

À la fin de ce laboratoire, vous serez capable d’utiliser OLIVE pour :

- Quantifier un modèle d’IA en utilisant la méthode de quantification AWQ.  
- Affiner un modèle d’IA pour une tâche spécifique.  
- Générer des adaptateurs LoRA (modèle affiné) pour une inférence efficace sur appareil avec ONNX Runtime.

### Qu’est-ce qu’Olive

Olive (*O*NNX *live*) est une boîte à outils d’optimisation de modèles avec une interface CLI associée qui vous permet de déployer des modèles pour ONNX runtime +++https://onnxruntime.ai+++ avec qualité et performance.

![Olive Flow](../../../../../translated_images/fr/olive-flow.5daf97340275f8b6.webp)

L’entrée d’Olive est généralement un modèle PyTorch ou Hugging Face et la sortie est un modèle ONNX optimisé qui s’exécute sur un appareil (cible de déploiement) utilisant ONNX runtime. Olive optimise le modèle pour l’accélérateur IA de la cible de déploiement (NPU, GPU, CPU) fourni par un fabricant de matériel tel que Qualcomm, AMD, Nvidia ou Intel.

Olive exécute un *workflow*, qui est une séquence ordonnée de tâches individuelles d’optimisation de modèle appelées *passes* – parmi les passes on trouve par exemple : compression de modèle, capture de graphe, quantification, optimisation de graphe. Chaque passe dispose d’un ensemble de paramètres pouvant être ajustés pour atteindre les meilleurs indicateurs, comme la précision et la latence, évalués par l’évaluateur correspondant. Olive utilise une stratégie de recherche qui emploie un algorithme pour auto-ajuster chaque passe une par une ou un ensemble de passes simultanément.

#### Avantages d’Olive

- **Réduire la frustration et le temps** des expérimentations manuelles par essais-erreurs avec différentes techniques d’optimisation de graphe, compression et quantification. Définissez vos contraintes de qualité et de performance et laissez Olive trouver automatiquement le meilleur modèle pour vous.  
- **Plus de 40 composants d’optimisation intégrés** couvrant les techniques de pointe en quantification, compression, optimisation de graphe et affinage.  
- **CLI facile à utiliser** pour les tâches courantes d’optimisation de modèle. Par exemple, olive quantize, olive auto-opt, olive finetune.  
- Emballage et déploiement de modèles intégrés.  
- Supporte la génération de modèles pour le **Multi LoRA serving**.  
- Construction de workflows via YAML/JSON pour orchestrer les tâches d’optimisation et de déploiement de modèles.  
- Intégration avec **Hugging Face** et **Azure AI**.  
- Mécanisme de **caching** intégré pour **réduire les coûts**.

## Instructions du laboratoire

> [!NOTE]  
> Veuillez vous assurer d’avoir provisionné votre Azure AI Hub et Projet et configuré votre calcul A100 comme indiqué dans le Laboratoire 1.

### Étape 0 : Connexion à votre calcul Azure AI

Vous allez vous connecter au calcul Azure AI en utilisant la fonctionnalité distante dans **VS Code**.

1. Ouvrez votre application de bureau **VS Code** :  
1. Ouvrez la **palette de commandes** avec **Shift+Ctrl+P**  
1. Dans la palette, recherchez **AzureML - remote: Connect to compute instance in New Window**.  
1. Suivez les instructions à l’écran pour vous connecter au calcul. Cela impliquera de sélectionner votre abonnement Azure, groupe de ressources, projet et nom du calcul configuré dans le Laboratoire 1.  
1. Une fois connecté à votre nœud Azure ML Compute, cela s’affichera en bas à gauche de Visual Code `><Azure ML: Compute Name`

### Étape 1 : Cloner ce dépôt

Dans VS Code, ouvrez un nouveau terminal avec **Ctrl+J** et clonez ce dépôt :

Dans le terminal, vous devriez voir l’invite

```
azureuser@computername:~/cloudfiles/code$ 
```  
Cloner la solution

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Étape 2 : Ouvrir le dossier dans VS Code

Pour ouvrir VS Code dans le dossier concerné, exécutez la commande suivante dans le terminal, ce qui ouvrira une nouvelle fenêtre :

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Sinon, vous pouvez ouvrir le dossier en sélectionnant **Fichier** > **Ouvrir un dossier**.

### Étape 3 : Dépendances

Ouvrez un terminal dans VS Code sur votre instance Azure AI Compute (astuce : **Ctrl+J**) et exécutez les commandes suivantes pour installer les dépendances :

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> L’installation de toutes les dépendances prendra environ 5 minutes.

Dans ce laboratoire, vous téléchargerez et téléverserez des modèles dans le catalogue de modèles Azure AI. Pour accéder au catalogue, vous devez vous connecter à Azure avec :

```bash
az login
```

> [!NOTE]  
> Lors de la connexion, il vous sera demandé de sélectionner votre abonnement. Assurez-vous de choisir celui fourni pour ce laboratoire.

### Étape 4 : Exécuter les commandes Olive

Ouvrez un terminal dans VS Code sur votre instance Azure AI Compute (astuce : **Ctrl+J**) et assurez-vous que l’environnement conda `olive-ai` est activé :

```bash
conda activate olive-ai
```

Ensuite, exécutez les commandes Olive suivantes dans la ligne de commande.

1. **Inspecter les données :** Dans cet exemple, vous allez affiner le modèle Phi-3.5-Mini pour qu’il soit spécialisé dans les questions liées aux voyages. Le code ci-dessous affiche les premiers enregistrements du jeu de données, au format JSON lines :

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **Quantifier le modèle :** Avant d’entraîner le modèle, vous le quantifiez d’abord avec la commande suivante qui utilise une technique appelée Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ quantifie les poids d’un modèle en tenant compte des activations produites lors de l’inférence. Cela signifie que le processus de quantification prend en compte la distribution réelle des données dans les activations, ce qui permet de mieux préserver la précision du modèle comparé aux méthodes traditionnelles de quantification des poids.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    La quantification AWQ prend environ **8 minutes** et permet de **réduire la taille du modèle d’environ 7,5 Go à environ 2,5 Go**.

    Dans ce laboratoire, nous vous montrons comment importer des modèles depuis Hugging Face (par exemple : `microsoft/Phi-3.5-mini-instruct`). Cependant, Olive permet aussi d’importer des modèles depuis le catalogue Azure AI en mettant à jour l’argument `model_name_or_path` avec un ID d’actif Azure AI (par exemple : `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

1. **Entraîner le modèle :** Ensuite, la commande `olive finetune` affine le modèle quantifié. Quantifier le modèle *avant* l’affinage plutôt qu’après permet d’obtenir une meilleure précision car le processus d’affinage compense une partie de la perte due à la quantification.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    L’affinage prend environ **6 minutes** (avec 100 étapes).

1. **Optimiser :** Une fois le modèle entraîné, vous l’optimisez avec la commande `auto-opt` d’Olive, qui capture le graphe ONNX et effectue automatiquement plusieurs optimisations pour améliorer les performances du modèle sur CPU en compressant le modèle et en réalisant des fusions. Notez que vous pouvez aussi optimiser pour d’autres appareils comme NPU ou GPU en modifiant simplement les arguments `--device` et `--provider` – mais pour ce laboratoire, nous utiliserons le CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    L’optimisation prend environ **5 minutes**.

### Étape 5 : Test rapide d’inférence du modèle

Pour tester l’inférence du modèle, créez un fichier Python dans votre dossier nommé **app.py** et copiez-collez le code suivant :

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Exécutez le code avec :

```bash
python app.py
```

### Étape 6 : Téléverser le modèle sur Azure AI

Téléverser le modèle dans un dépôt de modèles Azure AI permet de le partager avec d’autres membres de votre équipe de développement et gère également le contrôle de version du modèle. Pour téléverser le modèle, exécutez la commande suivante :

> [!NOTE]  
> Remplacez les espaces réservés `{}` par le nom de votre groupe de ressources et le nom de votre projet Azure AI.

Pour trouver votre groupe de ressources `"resourceGroup"` et le nom de votre projet Azure AI, exécutez la commande suivante :

```
az ml workspace show
```

Ou rendez-vous sur +++ai.azure.com+++ et sélectionnez **centre de gestion** > **projet** > **aperçu**

Remplacez les espaces réservés `{}` par le nom de votre groupe de ressources et le nom de votre projet Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Vous pourrez ensuite voir votre modèle téléversé et le déployer sur https://ml.azure.com/model/list

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.