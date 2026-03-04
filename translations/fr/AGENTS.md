# AGENTS.md

## Aperçu du projet

PhiCookBook est un dépôt complet de recettes contenant des exemples pratiques, des tutoriels et de la documentation pour travailler avec la famille Phi de modèles de langage réduits (SLMs) de Microsoft. Le dépôt illustre divers cas d'utilisation, notamment l'inférence, le fine-tuning, la quantification, les implémentations RAG et les applications multimodales sur différentes plateformes et frameworks.

**Technologies clés :**
- **Langages :** Python, C#/.NET, JavaScript/Node.js
- **Frameworks :** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plateformes :** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Types de modèles :** Phi-3, Phi-3.5, Phi-4 (texte, vision, multimodal, variantes de raisonnement)

**Structure du dépôt :**
- `/code/` - Exemples de code fonctionnel et implémentations d'échantillons
- `/md/` - Documentation détaillée, tutoriels et guides pratiques  
- `/translations/` - Traductions multilingues (50+ langues via un workflow automatisé)
- `/.devcontainer/` - Configuration du conteneur de développement (Python 3.12 avec Ollama)

## Configuration de l'environnement de développement

### Utilisation de GitHub Codespaces ou des conteneurs de développement (recommandé)

1. Ouvrir dans GitHub Codespaces (le plus rapide) :
   - Cliquez sur le badge "Open in GitHub Codespaces" dans le README
   - Le conteneur se configure automatiquement avec Python 3.12 et Ollama avec Phi-3

2. Ouvrir dans les conteneurs de développement VS Code :
   - Utilisez le badge "Open in Dev Containers" depuis le README
   - Le conteneur nécessite au minimum 16 Go de mémoire sur l'hôte

### Configuration locale

**Prérequis :**
- Python 3.12 ou version ultérieure
- SDK .NET 8.0 (pour les exemples en C#)
- Node.js 18+ et npm (pour les exemples en JavaScript)
- 16 Go de RAM minimum recommandés

**Installation :**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Pour les exemples en Python :**
Accédez aux répertoires d'exemples spécifiques et installez les dépendances :
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Pour les exemples en .NET :**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Pour les exemples en JavaScript/Web :**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organisation du dépôt

### Exemples de code (`/code/`)

- **01.Introduce/** - Introductions de base et exemples pour bien démarrer
- **03.Finetuning/** et **04.Finetuning/** - Exemples de fine-tuning avec différentes méthodes
- **03.Inference/** - Exemples d'inférence sur différents matériels (AIPC, MLX)
- **06.E2E/** - Exemples d'applications de bout en bout
- **07.Lab/** - Implémentations expérimentales/laboratoires
- **08.RAG/** - Exemples de génération augmentée par récupération
- **09.UpdateSamples/** - Derniers exemples mis à jour

### Documentation (`/md/`)

- **01.Introduction/** - Guides d'introduction, configuration de l'environnement, guides des plateformes
- **02.Application/** - Exemples d'applications organisés par type (Texte, Code, Vision, Audio, etc.)
- **02.QuickStart/** - Guides de démarrage rapide pour Microsoft Foundry et GitHub Models
- **03.FineTuning/** - Documentation et tutoriels sur le fine-tuning
- **04.HOL/** - Laboratoires pratiques (inclut des exemples en .NET)

### Formats de fichiers

- **Notebooks Jupyter (`.ipynb`)** - Tutoriels interactifs en Python marqués avec 📓 dans le README
- **Scripts Python (`.py`)** - Exemples Python autonomes
- **Projets C# (`.csproj`, `.sln`)** - Applications et exemples en .NET
- **JavaScript (`.js`, `package.json`)** - Exemples basés sur le web et Node.js
- **Markdown (`.md`)** - Documentation et guides

## Travailler avec les exemples

### Exécution des notebooks Jupyter

La plupart des exemples sont fournis sous forme de notebooks Jupyter :
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Exécution des scripts Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Exécution des exemples en .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Ou construisez toute la solution :
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Exécution des exemples JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Tests

Ce dépôt contient du code d'exemple et des tutoriels plutôt qu'un projet logiciel traditionnel avec des tests unitaires. La validation est généralement effectuée en :

1. **Exécutant les exemples** - Chaque exemple doit s'exécuter sans erreurs
2. **Vérifiant les résultats** - Assurez-vous que les réponses des modèles sont appropriées
3. **Suivant les tutoriels** - Les guides pas à pas doivent fonctionner comme documenté

**Approche de validation courante :**
- Testez l'exécution des exemples dans l'environnement cible
- Vérifiez que les dépendances s'installent correctement
- Assurez-vous que les modèles se téléchargent/se chargent avec succès
- Confirmez que le comportement attendu correspond à la documentation

## Style de code et conventions

### Directives générales

- Les exemples doivent être clairs, bien commentés et éducatifs
- Suivez les conventions spécifiques au langage (PEP 8 pour Python, normes C# pour .NET)
- Gardez les exemples centrés sur la démonstration des capacités spécifiques des modèles Phi
- Incluez des commentaires expliquant les concepts clés et les paramètres spécifiques aux modèles

### Normes de documentation

**Formatage des URL :**
- Utilisez le format `[texte](../../url)` sans espaces supplémentaires
- Liens relatifs : Utilisez `./` pour le répertoire actuel, `../` pour le parent
- Pas de locales spécifiques aux pays dans les URL (évitez `/en-us/`, `/en/`)

**Images :**
- Stockez toutes les images dans le répertoire `/imgs/`
- Utilisez des noms descriptifs avec des caractères anglais, des chiffres et des tirets
- Exemple : `phi-3-architecture.png`

**Fichiers Markdown :**
- Référencez des exemples fonctionnels réels dans le répertoire `/code/`
- Gardez la documentation synchronisée avec les modifications du code
- Utilisez l'emoji 📓 pour marquer les liens vers les notebooks Jupyter dans le README

### Organisation des fichiers

- Exemples de code dans `/code/` organisés par sujet/fonctionnalité
- Documentation dans `/md/` reflétant la structure du code lorsque cela est applicable
- Gardez les fichiers associés (notebooks, scripts, configurations) ensemble dans des sous-répertoires

## Directives pour les pull requests

### Avant de soumettre

1. **Forkez le dépôt** sur votre compte
2. **Séparez les PRs par type :**
   - Corrections de bugs dans une PR
   - Mises à jour de la documentation dans une autre
   - Nouveaux exemples dans des PRs séparées
   - Les corrections de fautes peuvent être combinées

3. **Gérez les conflits de fusion :**
   - Mettez à jour votre branche `main` locale avant de faire des modifications
   - Synchronisez fréquemment avec l'amont

4. **PRs de traduction :**
   - Doivent inclure les traductions pour TOUS les fichiers du dossier
   - Maintenez une structure cohérente avec la langue originale

### Vérifications requises

Les PRs exécutent automatiquement des workflows GitHub pour valider :

1. **Validation des chemins relatifs** - Tous les liens internes doivent fonctionner
   - Testez les liens localement : Ctrl+Click dans VS Code
   - Utilisez les suggestions de chemin de VS Code (`./` ou `../`)

2. **Vérification des locales des URL** - Les URL web ne doivent pas contenir de locales de pays
   - Supprimez `/en-us/`, `/en/` ou autres codes de langue
   - Utilisez des URL internationales génériques

3. **Vérification des URL cassées** - Toutes les URL doivent retourner un statut 200
   - Vérifiez que les liens sont accessibles avant de soumettre
   - Remarque : Certains échecs peuvent être dus à des restrictions réseau

### Format du titre de la PR

```
[component] Brief description
```

Exemples :
- `[docs] Ajouter un tutoriel d'inférence Phi-4`
- `[code] Corriger l'exemple d'intégration ONNX Runtime`
- `[translation] Ajouter la traduction japonaise des guides d'introduction`

## Modèles de développement courants

### Travailler avec les modèles Phi

**Chargement des modèles :**
- Les exemples utilisent divers frameworks : Transformers, ONNX Runtime, MLX, OpenVINO
- Les modèles sont généralement téléchargés depuis Hugging Face, Azure ou GitHub Models
- Vérifiez la compatibilité des modèles avec votre matériel (CPU, GPU, NPU)

**Modèles d'inférence :**
- Génération de texte : La plupart des exemples utilisent des variantes chat/instruct
- Vision : Phi-3-vision et Phi-4-multimodal pour la compréhension d'images
- Audio : Phi-4-multimodal prend en charge les entrées audio
- Raisonnement : Variantes Phi-4-reasoning pour les tâches de raisonnement avancées

### Notes spécifiques aux plateformes

**Microsoft Foundry :**
- Nécessite un abonnement Azure et des clés API
- Voir `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models :**
- Niveau gratuit disponible pour les tests
- Voir `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inférence locale :**
- ONNX Runtime : Inférence optimisée multiplateforme
- Ollama : Gestion facile des modèles locaux (préconfiguré dans le conteneur de développement)
- Apple MLX : Optimisé pour Apple Silicon

## Résolution des problèmes

### Problèmes courants

**Problèmes de mémoire :**
- Les modèles Phi nécessitent une RAM importante (surtout les variantes vision/multimodal)
- Utilisez des modèles quantifiés pour les environnements avec ressources limitées
- Voir `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflits de dépendances :**
- Les exemples Python peuvent avoir des exigences spécifiques de version
- Utilisez des environnements virtuels pour chaque exemple
- Consultez les fichiers `requirements.txt` individuels

**Échecs de téléchargement de modèles :**
- Les modèles volumineux peuvent expirer sur des connexions lentes
- Envisagez d'utiliser des environnements cloud (Codespaces, Azure)
- Vérifiez le cache Hugging Face : `~/.cache/huggingface/`

**Problèmes de projet .NET :**
- Assurez-vous que le SDK .NET 8.0 est installé
- Utilisez `dotnet restore` avant de construire
- Certains projets ont des configurations spécifiques CUDA (Debug_Cuda)

**Exemples JavaScript/Web :**
- Utilisez Node.js 18+ pour la compatibilité
- Effacez `node_modules` et réinstallez en cas de problèmes
- Vérifiez la console du navigateur pour les problèmes de compatibilité WebGPU

### Obtenir de l'aide

- **Discord :** Rejoignez la communauté Discord Microsoft Foundry
- **GitHub Issues :** Signalez les bugs et problèmes dans le dépôt
- **GitHub Discussions :** Posez des questions et partagez vos connaissances

## Contexte supplémentaire

### IA responsable

Toute utilisation des modèles Phi doit respecter les principes d'IA responsable de Microsoft :
- Équité, fiabilité, sécurité
- Confidentialité et sécurité  
- Inclusion, transparence, responsabilité
- Utilisez Azure AI Content Safety pour les applications en production
- Voir `/md/01.Introduction/01/01.AISafety.md`

### Traductions

- Plus de 50 langues prises en charge via une action GitHub automatisée
- Traductions dans le répertoire `/translations/`
- Maintenues par le workflow co-op-translator
- Ne modifiez pas manuellement les fichiers traduits (générés automatiquement)

### Contribution

- Suivez les directives dans `CONTRIBUTING.md`
- Acceptez l'accord de licence de contributeur (CLA)
- Respectez le code de conduite de Microsoft Open Source
- Ne laissez pas d'informations de sécurité ou d'identifiants dans les commits

### Support multilingue

Il s'agit d'un dépôt polyglotte avec des exemples en :
- **Python** - Workflows ML/IA, notebooks Jupyter, fine-tuning
- **C#/.NET** - Applications d'entreprise, intégration ONNX Runtime
- **JavaScript** - IA basée sur le web, inférence dans le navigateur avec WebGPU

Choisissez le langage qui correspond le mieux à votre cas d'utilisation et à votre cible de déploiement.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.