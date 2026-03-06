# AGENTS.md

## Aperçu du projet

PhiCookBook est un dépôt complet de livres de cuisine contenant des exemples pratiques, des tutoriels et une documentation pour travailler avec la famille Phi des Small Language Models (SLM) de Microsoft. Le dépôt démontre divers cas d'utilisation, notamment l'inférence, l'affinage, la quantification, les implémentations RAG et les applications multimodales sur différentes plateformes et frameworks.

**Technologies clés :**
- **Langages :** Python, C#/.NET, JavaScript/Node.js
- **Frameworks :** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plateformes :** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Types de modèles :** Phi-3, Phi-3.5, Phi-4 (variantes texte, vision, multimodal, raisonnement)

**Structure du dépôt :**
- `/code/` - Exemples de code fonctionnels et implémentations d'exemples
- `/md/` - Documentation détaillée, tutoriels et guides pratiques  
- `/translations/` - Traductions multilingues (plus de 50 langues via un workflow automatisé)
- `/.devcontainer/` - Configuration du conteneur de développement (Python 3.12 avec Ollama)

## Configuration de l’environnement de développement

### Utilisation de GitHub Codespaces ou Dev Containers (Recommandé)

1. Ouvrir dans GitHub Codespaces (le plus rapide) :
   - Cliquez sur le badge "Open in GitHub Codespaces" dans le README
   - Le conteneur se configure automatiquement avec Python 3.12 et Ollama avec Phi-3

2. Ouvrir dans VS Code Dev Containers :
   - Utilisez le badge "Open in Dev Containers" du README
   - Le conteneur nécessite au minimum 16 Go de mémoire hôte

### Configuration locale

**Prérequis :**
- Python 3.12 ou ultérieur
- SDK .NET 8.0 (pour les exemples en C#)
- Node.js 18+ et npm (pour les exemples JavaScript)
- Au minimum 16 Go de RAM recommandés

**Installation :**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```
  
**Pour les exemples Python :**  
Naviguez vers les répertoires des exemples spécifiques et installez les dépendances :  
```bash
cd code/<example-directory>
pip install -r requirements.txt  # si requirements.txt existe
```
  
**Pour les exemples .NET :**  
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```
  
**Pour les exemples JavaScript/Web :**  
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Démarrer le serveur de développement
npm run build  # Construire pour la production
```
  
## Organisation du dépôt

### Exemples de code (`/code/`)

- **01.Introduce/** - Introductions de base et exemples pour débuter
- **03.Finetuning/** et **04.Finetuning/** - Exemples d’affinage avec différentes méthodes
- **03.Inference/** - Exemples d’inférence sur différents matériels (AIPC, MLX)
- **06.E2E/** - Exemples d’applications de bout en bout
- **07.Lab/** - Implémentations expérimentales/laboratoires
- **08.RAG/** - Exemples de génération augmentée par récupération
- **09.UpdateSamples/** - Exemples récemment mis à jour

### Documentation (`/md/`)

- **01.Introduction/** - Guides d’introduction, configuration de l’environnement, guides plateforme
- **02.Application/** - Exemples d’applications organisés par type (Texte, Code, Vision, Audio, etc.)
- **02.QuickStart/** - Guides de démarrage rapide pour Microsoft Foundry et GitHub Models
- **03.FineTuning/** - Documentation et tutoriels d’affinage
- **04.HOL/** - Laboratoires pratiques (inclut exemples .NET)

### Formats de fichiers

- **Jupyter Notebooks (`.ipynb`)** - Tutoriels interactifs Python marqués avec 📓 dans le README
- **Scripts Python (`.py`)** - Exemples Python autonomes
- **Projets C# (`.csproj`, `.sln`)** - Applications et échantillons .NET
- **JavaScript (`.js`, `package.json`)** - Exemples web et Node.js
- **Markdown (`.md`)** - Documentation et guides

## Utilisation des exemples

### Exécution des Jupyter Notebooks

La plupart des exemples sont fournis sous forme de notebooks Jupyter :  
```bash
pip install jupyter notebook
jupyter notebook  # Ouvre l'interface du navigateur
# Naviguez vers le fichier .ipynb souhaité
```
  
### Exécution des scripts Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```
  
### Exécution des exemples .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```
  
Ou construire la solution entière :  
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```
  
### Exécution des exemples JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Développement avec rechargement à chaud
```
  
## Tests

Ce dépôt contient du code exemple et des tutoriels plutôt qu’un projet logiciel traditionnel avec des tests unitaires. La validation se fait typiquement par :

1. **Exécution des exemples** - Chaque exemple doit s’exécuter sans erreurs
2. **Vérification des résultats** - Vérifier que les réponses des modèles sont appropriées
3. **Suivi des tutoriels** - Les guides pas-à-pas doivent fonctionner comme documenté

**Approche de validation courante :**
- Tester l’exécution des exemples dans l’environnement cible
- Vérifier que les dépendances s’installent correctement
- Vérifier que les modèles se téléchargent se chargent avec succès
- Confirmer que le comportement attendu correspond à la documentation

## Style de code et conventions

### Directives générales

- Les exemples doivent être clairs, bien commentés et pédagogiques
- Respecter les conventions spécifiques aux langages (PEP 8 pour Python, standards C# pour .NET)
- Garder les exemples ciblés sur la démonstration des capacités spécifiques du modèle Phi
- Inclure des commentaires expliquant les concepts clés et paramètres spécifiques aux modèles

### Normes de documentation

**Format des URLs :**
- Utiliser le format `[texte](../../url)` sans espaces supplémentaires
- Liens relatifs : Utiliser `./` pour le répertoire actuel, `../` pour le parent
- Pas de locales spécifiques aux pays dans les URLs (éviter `/en-us/`, `/en/`)

**Images :**
- Stocker toutes les images dans le répertoire `/imgs/`
- Utiliser des noms descriptifs avec caractères anglais, chiffres et tirets
- Exemple : `phi-3-architecture.png`

**Fichiers Markdown :**
- Référencer les exemples réellement fonctionnels dans le répertoire `/code/`
- Garder la documentation synchronisée avec les modifications du code
- Utiliser l’emoji 📓 pour marquer les liens vers Jupyter notebooks dans le README

### Organisation des fichiers

- Exemples de code dans `/code/` organisés par sujet/fonctionnalité
- Documentation dans `/md/` reflète la structure du code quand c’est applicable
- Garder les fichiers liés (notebooks, scripts, configs) ensemble dans les sous-dossiers

## Directives pour les Pull Requests

### Avant de soumettre

1. **Forkez le dépôt** sur votre compte
2. **Séparez les PR par type :**
   - Corrections de bugs dans une PR
   - Mises à jour de documentation dans une autre
   - Nouveaux exemples dans des PR distinctes
   - Corrections de fautes d’orthographe peuvent être combinées

3. **Gérez les conflits de fusion :**
   - Mettez à jour votre branche `main` locale avant de faire des modifications
   - Synchronisez souvent avec la branche principale

4. **PR de traduction :**
   - Doivent inclure les traductions de TOUS les fichiers du dossier
   - Maintenir une structure cohérente avec la langue d’origine

### Vérifications requises

Les PR déclenchent automatiquement des workflows GitHub pour valider :

1. **Validation des chemins relatifs** - Tous les liens internes doivent fonctionner
   - Tester les liens localement : Ctrl+Click dans VS Code
   - Utiliser les suggestions de chemin de VS Code (`./` ou `../`)

2. **Vérification des locales dans les URLs** - Les URLs web ne doivent pas contenir de locales spécifiques aux pays
   - Supprimer `/en-us/`, `/en/` ou autres codes de langue
   - Utiliser des URLs génériques internationales

3. **Vérification des liens cassés** - Toutes les URLs doivent retourner un statut 200
   - Vérifier que les liens sont accessibles avant de soumettre
   - Note : Certains échecs peuvent venir de restrictions réseau

### Format du titre de PR

```
[component] Brief description
```
  
Exemples :  
- `[docs] Ajouter un tutoriel d’inférence Phi-4`  
- `[code] Corriger l’exemple d’intégration ONNX Runtime`  
- `[translation] Ajouter la traduction japonaise pour les guides d’introduction`  

## Modèles courants de développement

### Travail avec les modèles Phi

**Chargement de modèles :**
- Les exemples utilisent divers frameworks : Transformers, ONNX Runtime, MLX, OpenVINO
- Les modèles sont généralement téléchargés depuis Hugging Face, Azure ou GitHub Models
- Vérifier la compatibilité du modèle avec votre matériel (CPU, GPU, NPU)

**Modèles d’inférence :**
- Génération de texte : la plupart des exemples utilisent les variantes chat/instruct
- Vision : Phi-3-vision et Phi-4-multimodal pour compréhension d’images
- Audio : Phi-4-multimodal prend en charge les entrées audio
- Raisonnement : variantes Phi-4-reasoning pour des tâches avancées de raisonnement

### Notes spécifiques à la plateforme

**Microsoft Foundry :**
- Nécessite un abonnement Azure et des clés API
- Voir `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models :**
- Niveau gratuit disponible pour tests
- Voir `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inference locale :**
- ONNX Runtime : multi-plateforme, inférence optimisée
- Ollama : gestion locale facile des modèles (pré-configuré dans le conteneur dev)
- Apple MLX : optimisé pour Apple Silicon

## Dépannage

### Problèmes courants

**Problèmes de mémoire :**
- Les modèles Phi nécessitent beaucoup de RAM (surtout variantes vision/multimodal)
- Utilisez des modèles quantifiés pour environnements à ressources limitées
- Voir `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflits de dépendances :**
- Les exemples Python peuvent avoir des exigences de version spécifiques
- Utilisez des environnements virtuels pour chaque exemple
- Vérifiez les fichiers `requirements.txt` individuels

**Échecs de téléchargement de modèle :**
- Gros modèles peuvent provoquer des délais expirés sur connexions lentes
- Envisagez d’utiliser des environnements cloud (Codespaces, Azure)
- Vérifier le cache Hugging Face : `~/.cache/huggingface/`

**Problèmes de projets .NET :**
- Assurez-vous que le SDK .NET 8.0 est installé
- Utilisez `dotnet restore` avant la compilation
- Certains projets ont des configurations spécifiques CUDA (Debug_Cuda)

**Exemples JavaScript/Web :**
- Utilisez Node.js 18+ pour compatibilité
- Nettoyez `node_modules` et réinstallez si des problèmes persistent
- Vérifiez la console du navigateur pour problèmes de compatibilité WebGPU

### Obtenir de l’aide

- **Discord :** Rejoignez le Discord de la communauté Microsoft Foundry
- **Issues GitHub :** Signalez bugs et problèmes dans le dépôt
- **Discussions GitHub :** Posez des questions et partagez des connaissances

## Contexte supplémentaire

### IA responsable

Toute utilisation des modèles Phi doit suivre les principes d’IA responsable de Microsoft :  
- Équité, fiabilité, sécurité  
- Confidentialité et sécurité  
- Inclusion, transparence, responsabilité  
- Utiliser Azure AI Content Safety pour les applications en production  
- Voir `/md/01.Introduction/01/01.AISafety.md`  

### Traductions

- Plus de 50 langues supportées via une GitHub Action automatisée  
- Traductions dans le répertoire `/translations/`  
- Maintenues par un workflow co-op-translator  
- Ne pas modifier manuellement les fichiers traduits (générés automatiquement)  

### Contribution

- Suivez les directives dans `CONTRIBUTING.md`  
- Acceptez l’accord de licence des contributeurs (CLA)  
- Respectez le Code de conduite Open Source de Microsoft  
- Gardez la sécurité et les identifiants hors des commits  

### Support multilingue

C’est un dépôt polyglotte avec des exemples en :  
- **Python** - Flux ML/IA, notebooks Jupyter, affinage  
- **C#/.NET** - Applications d’entreprise, intégration ONNX Runtime  
- **JavaScript** - IA basée sur le web, inférence navigateur avec WebGPU  

Choisissez le langage qui correspond le mieux à votre cas d’usage et cible de déploiement.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source officielle. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->