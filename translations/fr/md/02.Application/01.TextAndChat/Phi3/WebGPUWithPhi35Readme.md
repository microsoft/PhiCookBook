<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-07T14:09:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "fr"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Démo pour présenter WebGPU et le modèle RAG

Le modèle RAG avec Phi-3.5 Onnx hébergé utilise l’approche Retrieval-Augmented Generation, combinant la puissance des modèles Phi-3.5 avec l’hébergement ONNX pour des déploiements IA efficaces. Ce modèle est essentiel pour affiner les modèles sur des tâches spécifiques à un domaine, offrant un équilibre entre qualité, coût et compréhension de contextes longs. Il fait partie de la suite Azure AI, proposant un large choix de modèles faciles à trouver, tester et utiliser, répondant aux besoins de personnalisation de divers secteurs.

## Qu’est-ce que WebGPU  
WebGPU est une API graphique web moderne conçue pour offrir un accès efficace au processeur graphique (GPU) d’un appareil directement depuis les navigateurs web. Elle est destinée à remplacer WebGL, avec plusieurs améliorations majeures :

1. **Compatibilité avec les GPU modernes** : WebGPU est conçu pour fonctionner parfaitement avec les architectures GPU actuelles, en tirant parti des API système comme Vulkan, Metal et Direct3D 12.
2. **Performance améliorée** : Il prend en charge les calculs généraux sur GPU et des opérations plus rapides, adapté aussi bien au rendu graphique qu’aux tâches d’apprentissage automatique.
3. **Fonctionnalités avancées** : WebGPU donne accès à des capacités GPU plus sophistiquées, permettant des charges graphiques et computationnelles plus complexes et dynamiques.
4. **Réduction de la charge JavaScript** : En déléguant plus de tâches au GPU, WebGPU réduit considérablement la charge sur JavaScript, améliorant les performances et la fluidité.

WebGPU est actuellement supporté dans des navigateurs comme Google Chrome, avec des travaux en cours pour étendre la prise en charge à d’autres plateformes.

### 03.WebGPU  
Environnement requis :

**Navigateurs supportés :**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Activer WebGPU :

- Sur Chrome/Microsoft Edge

Activez le drapeau `chrome://flags/#enable-unsafe-webgpu`.

#### Ouvrez votre navigateur :  
Lancez Google Chrome ou Microsoft Edge.

#### Accédez à la page des flags :  
Dans la barre d’adresse, tapez `chrome://flags` et appuyez sur Entrée.

#### Recherchez le drapeau :  
Dans la barre de recherche en haut de la page, tapez 'enable-unsafe-webgpu'.

#### Activez le drapeau :  
Trouvez le drapeau #enable-unsafe-webgpu dans la liste des résultats.  
Cliquez sur le menu déroulant à côté et sélectionnez Enabled.

#### Redémarrez votre navigateur :  
Après avoir activé le drapeau, vous devez redémarrer votre navigateur pour que les modifications prennent effet. Cliquez sur le bouton Relaunch qui apparaît en bas de la page.

- Sous Linux, lancez le navigateur avec `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) a WebGPU activé par défaut.  
- Dans Firefox Nightly, entrez about:config dans la barre d’adresse et `set dom.webgpu.enabled to true`.

### Configuration du GPU pour Microsoft Edge  

Voici les étapes pour configurer un GPU haute performance pour Microsoft Edge sous Windows :

- **Ouvrez les Paramètres :** Cliquez sur le menu Démarrer et sélectionnez Paramètres.  
- **Paramètres système :** Allez dans Système puis Affichage.  
- **Paramètres graphiques :** Descendez et cliquez sur Paramètres graphiques.  
- **Choisissez une application :** Sous « Choisissez une application pour définir la préférence », sélectionnez Application de bureau puis Parcourir.  
- **Sélectionnez Edge :** Naviguez jusqu’au dossier d’installation de Edge (généralement `C:\Program Files (x86)\Microsoft\Edge\Application`) et sélectionnez `msedge.exe`.  
- **Définissez la préférence :** Cliquez sur Options, choisissez Haute performance, puis cliquez sur Enregistrer.  
Cela garantira que Microsoft Edge utilise votre GPU haute performance pour de meilleures performances.  
- **Redémarrez** votre machine pour que ces paramètres soient pris en compte.

### Exemples : Veuillez [cliquer sur ce lien](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.