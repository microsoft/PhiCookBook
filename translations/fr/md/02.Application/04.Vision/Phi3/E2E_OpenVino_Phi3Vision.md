Cette démo montre comment utiliser un modèle pré-entraîné pour générer du code Python à partir d’une image et d’une invite textuelle.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Voici une explication étape par étape :

1. **Imports et configuration** :  
   - Les bibliothèques et modules nécessaires sont importés, notamment `requests`, `PIL` pour le traitement d’image, et `transformers` pour gérer le modèle et le traitement.

2. **Chargement et affichage de l’image** :  
   - Un fichier image (`demo.png`) est ouvert avec la bibliothèque `PIL` et affiché.

3. **Définition de l’invite** :  
   - Un message est créé, incluant l’image et une demande de génération de code Python pour traiter l’image et la sauvegarder avec `plt` (matplotlib).

4. **Chargement du processeur** :  
   - L’`AutoProcessor` est chargé à partir d’un modèle pré-entraîné situé dans le répertoire `out_dir`. Ce processeur gérera les entrées texte et image.

5. **Création de l’invite** :  
   - La méthode `apply_chat_template` est utilisée pour formater le message en une invite adaptée au modèle.

6. **Traitement des entrées** :  
   - L’invite et l’image sont transformées en tenseurs compréhensibles par le modèle.

7. **Définition des arguments de génération** :  
   - Les paramètres pour le processus de génération du modèle sont définis, incluant le nombre maximal de nouveaux tokens à générer et l’activation ou non de l’échantillonnage.

8. **Génération du code** :  
   - Le modèle génère le code Python à partir des entrées et des arguments de génération. Le `TextStreamer` est utilisé pour gérer la sortie, en sautant l’invite et les tokens spéciaux.

9. **Sortie** :  
   - Le code généré est affiché, il devrait contenir du code Python pour traiter l’image et la sauvegarder comme spécifié dans l’invite.

Cette démo illustre comment exploiter un modèle pré-entraîné avec OpenVino pour générer dynamiquement du code à partir d’entrées utilisateur et d’images.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.