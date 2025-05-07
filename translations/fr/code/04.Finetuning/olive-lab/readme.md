<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-07T15:12:57+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "fr"
}
-->
# Lab. Optimiser les modèles IA pour l'inférence sur appareil

## Introduction

> [!IMPORTANT]  
> Ce laboratoire nécessite une **GPU Nvidia A10 ou A100** avec les pilotes associés et le toolkit CUDA (version 12+) installés.

> [!NOTE]  
> Il s'agit d'un laboratoire de **35 minutes** qui vous donnera une introduction pratique aux concepts clés de l’optimisation des modèles pour l'inférence sur appareil avec OLIVE.

## Objectifs d’apprentissage

À la fin de ce laboratoire, vous serez capable d’utiliser OLIVE pour :

- Quantifier un modèle IA en utilisant la méthode de quantification AWQ.  
- Affiner un modèle IA pour une tâche spécifique.  
- Générer des adaptateurs LoRA (modèle affiné) pour une inférence efficace sur appareil avec ONNX Runtime.

### Qu’est-ce qu’Olive

Olive (*O*NNX *live*) est une boîte à outils d’optimisation de modèles avec une interface CLI associée qui vous permet de déployer des modèles pour ONNX runtime +++https://onnxruntime.ai+++ avec qualité et performance.

![Olive Flow](../../../../../translated_images/olive-flow.c4f76d9142c579b2462b631b8aa862093b595bb89064fa33e6d4fa90f937f52d.fr.png)

L’entrée d’Olive est généralement un modèle PyTorch ou Hugging Face, et la sortie est un modèle ONNX optimisé, exécuté sur un appareil (cible de déploiement) utilisant ONNX runtime. Olive optimise le modèle pour l’accélérateur IA de la cible de déploiement (NPU, GPU, CPU) fourni par un fabricant de matériel comme Qualcomm, AMD, Nvidia ou Intel.

Olive exécute un *workflow*, une séquence ordonnée de tâches d’optimisation de modèle individuelles appelées *passes* – par exemple : compression de modèle, capture de graphe, quantification, optimisation de graphe. Chaque passe a un ensemble de paramètres que l’on peut ajuster pour obtenir les meilleures métriques, par exemple la précision et la latence, évaluées par l’évaluateur respectif. Olive utilise une stratégie de recherche qui emploie un algorithme pour ajuster automatiquement chaque passe une par une ou un ensemble de passes ensemble.

#### Avantages d’Olive

- **Réduit la frustration et le temps** des expérimentations manuelles par essais-erreurs avec différentes techniques d’optimisation de graphe, compression et quantification. Définissez vos contraintes de qualité et de performance et laissez Olive trouver automatiquement le meilleur modèle pour vous.  
- **Plus de 40 composants intégrés d’optimisation de modèle** couvrant les techniques de pointe en quantification, compression, optimisation de graphe et affinement.  
- **CLI facile à utiliser** pour les tâches courantes d’optimisation de modèle. Par exemple, olive quantize, olive auto-opt, olive finetune.  
- Emballage et déploiement de modèles intégrés.  
- Supporte la génération de modèles pour le **Multi LoRA serving**.  
- Construction de workflows avec YAML/JSON pour orchestrer les tâches d’optimisation et de déploiement de modèles.  
- Intégration **Hugging Face** et **Azure AI**.  
- Mécanisme de **caching** intégré pour **réduire les coûts**.

## Instructions du laboratoire

> [!NOTE]  
> Veuillez vous assurer d’avoir provisionné votre Azure AI Hub et Projet et configuré votre calcul A100 conformément au Lab 1.

### Étape 0 : Connexion à votre calcul Azure AI

Vous allez vous connecter au calcul Azure AI en utilisant la fonctionnalité distante dans **VS Code**.

1. Ouvrez votre application de bureau **VS Code** :  
1. Ouvrez la **palette de commandes** avec **Shift+Ctrl+P**  
1. Dans la palette de commandes, cherchez **AzureML - remote: Connect to compute instance in New Window**.  
1. Suivez les instructions à l’écran pour vous connecter au calcul. Cela implique de sélectionner votre abonnement Azure, groupe de ressources, projet et nom du calcul configuré dans le Lab 1.  
1. Une fois connecté à votre nœud Azure ML Compute, cela s’affichera en **bas à gauche de Visual Code** `><Azure ML: Compute Name`

### Étape 1 : Cloner ce dépôt

Dans VS Code, vous pouvez ouvrir un nouveau terminal avec **Ctrl+J** et cloner ce dépôt :

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

Ouvrez une fenêtre terminal dans VS Code sur votre instance Azure AI Compute (astuce : **Ctrl+J**) et exécutez les commandes suivantes pour installer les dépendances :

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> L’installation de toutes les dépendances prendra environ 5 minutes.

Dans ce laboratoire, vous téléchargerez et téléverserez des modèles vers le catalogue de modèles Azure AI. Pour accéder au catalogue, vous devez vous connecter à Azure avec :

```bash
az login
```

> [!NOTE]  
> Lors de la connexion, on vous demandera de sélectionner votre abonnement. Assurez-vous de choisir l’abonnement fourni pour ce laboratoire.

### Étape 4 : Exécuter les commandes Olive

Ouvrez une fenêtre terminal dans VS Code sur votre instance Azure AI Compute (astuce : **Ctrl+J**) et assurez-vous que l’environnement conda `olive-ai` est activé :

```bash
conda activate olive-ai
```

Ensuite, exécutez les commandes Olive suivantes dans la ligne de commande.

1. **Inspecter les données :** Dans cet exemple, vous allez affiner le modèle Phi-3.5-Mini pour qu’il soit spécialisé dans la réponse aux questions liées aux voyages. Le code ci-dessous affiche les premières entrées du jeu de données, au format JSON lines :

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **Quantifier le modèle :** Avant d’entraîner le modèle, vous le quantifiez avec la commande suivante qui utilise une technique appelée Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ quantifie les poids d’un modèle en prenant en compte les activations produites lors de l’inférence. Cela signifie que le processus de quantification considère la distribution réelle des données dans les activations, ce qui permet une meilleure préservation de la précision du modèle comparé aux méthodes traditionnelles de quantification des poids.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    La quantification AWQ prend environ **8 minutes** et permet de **réduire la taille du modèle d’environ 7,5 Go à 2,5 Go**.

    Dans ce laboratoire, nous vous montrons comment importer des modèles depuis Hugging Face (par exemple : `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` commande affine le modèle quantifié. Quantifier le modèle *avant* l’affinage plutôt qu’après permet d’obtenir une meilleure précision car l’affinage compense une partie de la perte due à la quantification.

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

    L’affinage prend environ **6 minutes** (avec 100 itérations).

1. **Optimiser :** Une fois le modèle entraîné, vous l’optimisez avec la commande `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` d’Olive – mais pour ce laboratoire, nous utiliserons le CPU.

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

Téléverser le modèle dans un dépôt de modèles Azure AI le rend partageable avec les autres membres de votre équipe de développement et gère également le contrôle des versions. Pour téléverser le modèle, exécutez la commande suivante :

> [!NOTE]  
> Mettez à jour les `{}` ` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group ` avec le nom de votre groupe de ressources et le nom de votre projet Azure AI, puis exécutez la commande

```
az ml workspace show
```

Ou bien, allez sur +++ai.azure.com+++ et sélectionnez **centre de gestion** > **projet** > **aperçu**

Remplacez les `{}` par le nom de votre groupe de ressources et le nom de votre projet Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Vous pourrez alors voir votre modèle téléversé et le déployer sur https://ml.azure.com/model/list

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous ne saurions être tenus responsables des malentendus ou des interprétations erronées résultant de l’utilisation de cette traduction.