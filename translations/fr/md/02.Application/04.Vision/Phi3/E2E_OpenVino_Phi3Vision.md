<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-07T13:44:18+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "fr"
}
-->
Cette démo montre comment utiliser un modèle préentraîné pour générer du code Python à partir d'une image et d'une invite textuelle.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Voici une explication étape par étape :

1. **Imports et configuration** :  
   - Les bibliothèques et modules nécessaires sont importés, y compris `requests`, `PIL` pour le traitement d’image, et `transformers` pour gérer le modèle et le traitement.

2. **Chargement et affichage de l’image** :  
   - Un fichier image (`demo.png`) est ouvert avec la bibliothèque `PIL` et affiché.

3. **Définition de l’invite** :  
   - Un message est créé, incluant l’image et une demande de génération de code Python pour traiter l’image et l’enregistrer en utilisant `plt` (matplotlib).

4. **Chargement du processeur** :  
   - Le `AutoProcessor` est chargé à partir d’un modèle préentraîné situé dans le répertoire `out_dir`. Ce processeur gérera les entrées texte et image.

5. **Création de l’invite** :  
   - La méthode `apply_chat_template` est utilisée pour formater le message en une invite adaptée au modèle.

6. **Traitement des entrées** :  
   - L’invite et l’image sont transformées en tenseurs compréhensibles par le modèle.

7. **Définition des arguments de génération** :  
   - Les paramètres pour la génération du modèle sont définis, incluant le nombre maximal de nouveaux tokens à générer et l’activation ou non de l’échantillonnage.

8. **Génération du code** :  
   - Le modèle génère le code Python à partir des entrées et des arguments de génération. Le `TextStreamer` est utilisé pour gérer la sortie, en sautant l’invite et les tokens spéciaux.

9. **Sortie** :  
   - Le code généré est affiché, il doit inclure le code Python pour traiter l’image et l’enregistrer comme spécifié dans l’invite.

Cette démo illustre comment exploiter un modèle préentraîné avec OpenVino pour générer dynamiquement du code en fonction des entrées utilisateur et des images.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables de tout malentendu ou mauvaise interprétation résultant de l’utilisation de cette traduction.