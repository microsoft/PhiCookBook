<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-03-27T12:53:41+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_OpenVino_Phi3Vision.md",
  "language_code": "fr"
}
-->
Cette démonstration montre comment utiliser un modèle préentraîné pour générer du code Python à partir d'une image et d'une instruction textuelle.

[Code Exemple](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Voici une explication étape par étape :

1. **Importations et Configuration** :
   - Les bibliothèques et modules nécessaires sont importés, notamment `requests`, `PIL` pour le traitement d'image, et `transformers` pour gérer le modèle et le traitement.

2. **Chargement et Affichage de l'Image** :
   - Un fichier image (`demo.png`) est ouvert en utilisant la bibliothèque `PIL` et affiché.

3. **Définition de l'Instruction** :
   - Un message est créé qui inclut l'image et une demande pour générer du code Python afin de traiter l'image et de l'enregistrer en utilisant `plt` (matplotlib).

4. **Chargement du Processeur** :
   - Le `AutoProcessor` est chargé à partir d'un modèle préentraîné spécifié dans le répertoire `out_dir`. Ce processeur gérera les entrées textuelles et visuelles.

5. **Création de l'Instruction** :
   - La méthode `apply_chat_template` est utilisée pour formater le message en une instruction adaptée au modèle.

6. **Traitement des Entrées** :
   - L'instruction et l'image sont transformées en tenseurs compréhensibles par le modèle.

7. **Définition des Arguments de Génération** :
   - Les arguments pour le processus de génération du modèle sont définis, incluant le nombre maximum de nouveaux tokens à générer et si l'on doit échantillonner la sortie.

8. **Génération du Code** :
   - Le modèle génère le code Python basé sur les entrées et les arguments de génération. Le `TextStreamer` est utilisé pour gérer la sortie, en sautant l'instruction et les tokens spéciaux.

9. **Résultat** :
   - Le code généré est affiché, et il devrait inclure du code Python pour traiter l'image et l'enregistrer comme spécifié dans l'instruction.

Cette démonstration illustre comment exploiter un modèle préentraîné avec OpenVino pour générer du code de manière dynamique en fonction des entrées utilisateur et des images.

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.