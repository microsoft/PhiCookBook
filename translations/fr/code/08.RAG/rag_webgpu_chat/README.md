Phi-3-mini WebGPU RAG Chatbot

## Démo pour présenter WebGPU et le modèle RAG
Le modèle RAG avec Phi-3 Onnx hébergé utilise l’approche Retrieval-Augmented Generation, combinant la puissance des modèles Phi-3 avec l’hébergement ONNX pour des déploiements IA efficaces. Ce modèle est essentiel pour affiner les modèles sur des tâches spécifiques à un domaine, offrant un équilibre entre qualité, coût et compréhension de longs contextes. Il fait partie de la suite Azure AI, qui propose une large sélection de modèles faciles à trouver, tester et utiliser, répondant aux besoins de personnalisation de divers secteurs. Les modèles Phi-3, incluant Phi-3-mini, Phi-3-small et Phi-3-medium, sont disponibles dans le catalogue Azure AI Model et peuvent être affinés et déployés en autogestion ou via des plateformes comme HuggingFace et ONNX, illustrant l’engagement de Microsoft pour des solutions IA accessibles et performantes.

## Qu’est-ce que WebGPU  
WebGPU est une API graphique web moderne conçue pour offrir un accès efficace au processeur graphique (GPU) d’un appareil directement depuis les navigateurs web. Elle est destinée à succéder à WebGL, avec plusieurs améliorations clés :

1. **Compatibilité avec les GPU modernes** : WebGPU est conçu pour fonctionner parfaitement avec les architectures GPU contemporaines, en s’appuyant sur des API système comme Vulkan, Metal et Direct3D 12.
2. **Performance améliorée** : Il prend en charge les calculs GPU à usage général et des opérations plus rapides, ce qui le rend adapté à la fois au rendu graphique et aux tâches d’apprentissage automatique.
3. **Fonctionnalités avancées** : WebGPU donne accès à des capacités GPU plus avancées, permettant des charges de travail graphiques et computationnelles plus complexes et dynamiques.
4. **Réduction de la charge JavaScript** : En déléguant plus de tâches au GPU, WebGPU réduit considérablement la charge sur JavaScript, ce qui améliore les performances et la fluidité.

WebGPU est actuellement pris en charge dans des navigateurs comme Google Chrome, avec des travaux en cours pour étendre la compatibilité à d’autres plateformes.

### 03.WebGPU
Environnement requis :

**Navigateurs supportés :**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Activer WebGPU :

- Dans Chrome/Microsoft Edge  

Activez le flag `chrome://flags/#enable-unsafe-webgpu`.

#### Ouvrez votre navigateur :  
Lancez Google Chrome ou Microsoft Edge.

#### Accédez à la page des flags :  
Dans la barre d’adresse, tapez `chrome://flags` et appuyez sur Entrée.

#### Recherchez le flag :  
Dans la barre de recherche en haut de la page, tapez 'enable-unsafe-webgpu'

#### Activez le flag :  
Trouvez le flag #enable-unsafe-webgpu dans la liste des résultats.

Cliquez sur le menu déroulant à côté et sélectionnez Activé.

#### Redémarrez votre navigateur :  

Après avoir activé le flag, vous devez redémarrer votre navigateur pour que les modifications prennent effet. Cliquez sur le bouton Relancer qui apparaît en bas de la page.

- Sous Linux, lancez le navigateur avec `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) a WebGPU activé par défaut.  
- Dans Firefox Nightly, entrez about:config dans la barre d’adresse et réglez `dom.webgpu.enabled` sur true.

### Configuration du GPU pour Microsoft Edge  

Voici les étapes pour configurer un GPU haute performance pour Microsoft Edge sous Windows :

- **Ouvrir les Paramètres :** Cliquez sur le menu Démarrer et sélectionnez Paramètres.  
- **Paramètres système :** Allez dans Système puis Affichage.  
- **Paramètres graphiques :** Faites défiler vers le bas et cliquez sur Paramètres graphiques.  
- **Choisir une application :** Sous « Choisir une application pour définir la préférence », sélectionnez Application de bureau puis Parcourir.  
- **Sélectionner Edge :** Naviguez jusqu’au dossier d’installation de Edge (généralement `C:\Program Files (x86)\Microsoft\Edge\Application`) et sélectionnez `msedge.exe`.  
- **Définir la préférence :** Cliquez sur Options, choisissez Haute performance, puis cliquez sur Enregistrer.  
Cela garantira que Microsoft Edge utilise votre GPU haute performance pour de meilleures performances.  
- **Redémarrez** votre machine pour que ces paramètres soient pris en compte.

### Ouvrez votre Codespace :  
Accédez à votre dépôt sur GitHub.  
Cliquez sur le bouton Code et sélectionnez Ouvrir avec Codespaces.

Si vous n’avez pas encore de Codespace, vous pouvez en créer un en cliquant sur Nouveau codespace.

**Note** Installation de l’environnement Node dans votre codespace  
Exécuter une démo npm depuis un GitHub Codespace est un excellent moyen de tester et développer votre projet. Voici un guide étape par étape pour vous aider à démarrer :

### Configurez votre environnement :  
Une fois votre Codespace ouvert, assurez-vous que Node.js et npm sont installés. Vous pouvez vérifier en exécutant :  
```
node -v
```  
```
npm -v
```

S’ils ne sont pas installés, vous pouvez les installer avec :  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Naviguez vers le répertoire de votre projet :  
Utilisez le terminal pour vous rendre dans le dossier où se trouve votre projet npm :  
```
cd path/to/your/project
```

### Installez les dépendances :  
Exécutez la commande suivante pour installer toutes les dépendances nécessaires listées dans votre fichier package.json :  

```
npm install
```

### Lancez la démo :  
Une fois les dépendances installées, vous pouvez lancer votre script de démo. Il est généralement spécifié dans la section scripts de votre package.json. Par exemple, si votre script de démo s’appelle start, vous pouvez exécuter :  

```
npm run build
```  
```
npm run dev
```

### Accédez à la démo :  
Si votre démo implique un serveur web, Codespaces fournira une URL pour y accéder. Cherchez une notification ou consultez l’onglet Ports pour trouver l’URL.

**Note :** Le modèle doit être mis en cache dans le navigateur, il peut donc prendre un certain temps à charger.

### Démo RAG  
Téléversez le fichier markdown `intro_rag.md` pour compléter la solution RAG. Si vous utilisez Codespaces, vous pouvez télécharger le fichier situé dans `01.InferencePhi3/docs/`

### Sélectionnez votre fichier :  
Cliquez sur le bouton « Choisir un fichier » pour sélectionner le document que vous souhaitez téléverser.

### Téléversez le document :  
Après avoir sélectionné votre fichier, cliquez sur le bouton « Upload » pour charger votre document pour RAG (Retrieval-Augmented Generation).

### Démarrez votre chat :  
Une fois le document téléversé, vous pouvez commencer une session de chat utilisant RAG basée sur le contenu de votre document.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.