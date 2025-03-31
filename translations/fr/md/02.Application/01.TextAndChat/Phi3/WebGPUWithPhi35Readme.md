<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-03-27T11:15:22+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\WebGPUWithPhi35Readme.md",
  "language_code": "fr"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Démonstration de WebGPU et du modèle RAG

Le modèle RAG avec Phi-3.5 Onnx Hosted utilise l'approche de la génération augmentée par récupération (Retrieval-Augmented Generation), combinant la puissance des modèles Phi-3.5 avec l'hébergement ONNX pour des déploiements IA efficaces. Ce modèle est essentiel pour affiner les modèles dans des tâches spécifiques à un domaine, offrant un équilibre entre qualité, rentabilité et compréhension de contextes longs. Il fait partie de la suite Azure AI, proposant une large sélection de modèles faciles à trouver, tester et utiliser, répondant aux besoins de personnalisation de divers secteurs.

## Qu'est-ce que WebGPU 
WebGPU est une API moderne de graphisme web conçue pour offrir un accès efficace au processeur graphique (GPU) d'un appareil directement depuis les navigateurs web. Elle est destinée à succéder à WebGL, avec plusieurs améliorations clés :

1. **Compatibilité avec les GPU modernes** : WebGPU est conçu pour fonctionner parfaitement avec les architectures GPU contemporaines, en exploitant des API système comme Vulkan, Metal et Direct3D 12.
2. **Performances améliorées** : Il prend en charge les calculs généraux sur GPU et des opérations plus rapides, le rendant adapté tant pour le rendu graphique que pour les tâches d'apprentissage automatique.
3. **Fonctionnalités avancées** : WebGPU offre un accès à des capacités GPU plus avancées, permettant des charges de travail graphiques et computationnelles plus complexes et dynamiques.
4. **Réduction de la charge JavaScript** : En déléguant davantage de tâches au GPU, WebGPU réduit significativement la charge sur JavaScript, offrant de meilleures performances et des expériences plus fluides.

WebGPU est actuellement pris en charge par des navigateurs comme Google Chrome, avec des travaux en cours pour étendre cette compatibilité à d'autres plateformes.

### 03.WebGPU
Environnement requis :

**Navigateurs pris en charge :** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Activer WebGPU :

- Dans Chrome/Microsoft Edge 

Activez le drapeau `chrome://flags/#enable-unsafe-webgpu`.

#### Ouvrir votre navigateur :
Lancez Google Chrome ou Microsoft Edge.

#### Accéder à la page des drapeaux :
Dans la barre d'adresse, tapez `chrome://flags` et appuyez sur Entrée.

#### Rechercher le drapeau :
Dans la barre de recherche en haut de la page, tapez 'enable-unsafe-webgpu'.

#### Activer le drapeau :
Trouvez le drapeau #enable-unsafe-webgpu dans la liste des résultats.

Cliquez sur le menu déroulant à côté et sélectionnez Activé.

#### Redémarrer votre navigateur :

Après avoir activé le drapeau, vous devrez redémarrer votre navigateur pour que les modifications prennent effet. Cliquez sur le bouton Relancer qui apparaît en bas de la page.

- Pour Linux, lancez le navigateur avec `--enable-features=Vulkan`.
- Safari 18 (macOS 15) a WebGPU activé par défaut.
- Dans Firefox Nightly, entrez about:config dans la barre d'adresse et `set dom.webgpu.enabled to true`.

### Configuration du GPU pour Microsoft Edge 

Voici les étapes pour configurer un GPU haute performance pour Microsoft Edge sous Windows :

- **Ouvrir les paramètres :** Cliquez sur le menu Démarrer et sélectionnez Paramètres.
- **Paramètres système :** Allez dans Système puis Affichage.
- **Paramètres graphiques :** Faites défiler vers le bas et cliquez sur Paramètres graphiques.
- **Choisir une application :** Sous "Choisir une application pour définir une préférence", sélectionnez Application de bureau puis Parcourir.
- **Sélectionner Edge :** Naviguez jusqu'au dossier d'installation de Edge (généralement `C:\Program Files (x86)\Microsoft\Edge\Application`) et sélectionnez `msedge.exe`.
- **Définir une préférence :** Cliquez sur Options, choisissez Haute performance, puis cliquez sur Enregistrer.
Cela garantira que Microsoft Edge utilise votre GPU haute performance pour de meilleures performances. 
- **Redémarrez** votre machine pour que ces paramètres prennent effet.

### Exemples : Veuillez [cliquer sur ce lien](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.