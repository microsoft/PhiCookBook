<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-03-27T10:44:24+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-mini_with_whisper.md",
  "language_code": "fr"
}
-->
# Chatbot interactif Phi 3 Mini 4K avec Whisper

## Vue d'ensemble

Le chatbot interactif Phi 3 Mini 4K Instruct est un outil permettant aux utilisateurs d'interagir avec la démonstration Microsoft Phi 3 Mini 4K Instruct via une entrée textuelle ou audio. Ce chatbot peut être utilisé pour diverses tâches, comme la traduction, les mises à jour météo et la recherche d'informations générales.

### Prise en main

Pour utiliser ce chatbot, suivez simplement ces étapes :

1. Ouvrez un nouveau fichier [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. Dans la fenêtre principale du notebook, vous verrez une interface de chat avec une boîte de saisie textuelle et un bouton "Envoyer".
3. Pour utiliser le chatbot basé sur le texte, tapez simplement votre message dans la boîte de saisie textuelle et cliquez sur le bouton "Envoyer". Le chatbot répondra avec un fichier audio qui peut être lu directement depuis le notebook.

**Note** : Cet outil nécessite une GPU ainsi que l'accès aux modèles Microsoft Phi-3 et OpenAI Whisper, utilisés pour la reconnaissance vocale et la traduction.

### Exigences GPU

Pour exécuter cette démonstration, vous avez besoin de 12 Go de mémoire GPU.

Les exigences en mémoire pour exécuter la démonstration **Microsoft-Phi-3-Mini-4K Instruct** sur un GPU dépendront de plusieurs facteurs, tels que la taille des données d'entrée (audio ou texte), la langue utilisée pour la traduction, la vitesse du modèle et la mémoire disponible sur le GPU.

En général, le modèle Whisper est conçu pour fonctionner sur des GPUs. La quantité minimale recommandée de mémoire GPU pour exécuter le modèle Whisper est de 8 Go, mais il peut gérer des quantités de mémoire plus importantes si nécessaire.

Il est important de noter que le traitement d'un volume important de données ou de nombreuses requêtes sur le modèle peut nécessiter davantage de mémoire GPU et/ou entraîner des problèmes de performance. Il est recommandé de tester votre cas d'utilisation avec différentes configurations et de surveiller l'utilisation de la mémoire afin de déterminer les paramètres optimaux pour vos besoins spécifiques.

## Exemple E2E pour le chatbot interactif Phi 3 Mini 4K avec Whisper

Le notebook Jupyter intitulé [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) montre comment utiliser la démonstration Microsoft Phi 3 Mini 4K Instruct pour générer du texte à partir d'une entrée audio ou textuelle. Le notebook définit plusieurs fonctions :

1. `tts_file_name(text)` : Cette fonction génère un nom de fichier basé sur le texte d'entrée pour enregistrer le fichier audio généré.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)` : Cette fonction utilise l'API Edge TTS pour générer un fichier audio à partir d'une liste de segments de texte d'entrée. Les paramètres d'entrée sont la liste des segments, la vitesse de parole, le nom de la voix et le chemin de sortie pour enregistrer le fichier audio généré.
3. `talk(input_text)` : Cette fonction génère un fichier audio en utilisant l'API Edge TTS et en l'enregistrant sous un nom de fichier aléatoire dans le répertoire /content/audio. Le paramètre d'entrée est le texte à convertir en audio.
4. `run_text_prompt(message, chat_history)` : Cette fonction utilise la démonstration Microsoft Phi 3 Mini 4K Instruct pour générer un fichier audio à partir d'un message d'entrée et l'ajoute à l'historique de discussion.
5. `run_audio_prompt(audio, chat_history)` : Cette fonction convertit un fichier audio en texte en utilisant l'API du modèle Whisper et le transmet à la fonction `run_text_prompt()`.
6. Le code lance une application Gradio permettant aux utilisateurs d'interagir avec la démonstration Phi 3 Mini 4K Instruct en saisissant des messages ou en téléchargeant des fichiers audio. La sortie est affichée sous forme de message texte dans l'application.

## Résolution de problèmes

Installation des pilotes GPU Cuda

1. Assurez-vous que vos applications Linux sont à jour.

    ```bash
    sudo apt update
    ```

2. Installez les pilotes Cuda.

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Enregistrez l'emplacement du pilote Cuda.

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Vérifiez la taille de la mémoire GPU Nvidia (12 Go de mémoire GPU nécessaires).

    ```bash
    nvidia-smi
    ```

5. Videz le cache : Si vous utilisez PyTorch, vous pouvez appeler torch.cuda.empty_cache() pour libérer toute mémoire mise en cache inutilisée afin qu'elle puisse être utilisée par d'autres applications GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Vérifiez Cuda Nvidia.

    ```bash
    nvcc --version
    ```

7. Effectuez les tâches suivantes pour créer un jeton Hugging Face.

    - Accédez à la [page des paramètres de jeton Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Sélectionnez **Nouveau jeton**.
    - Entrez le **Nom** du projet que vous souhaitez utiliser.
    - Sélectionnez **Type** sur **Écriture**.

> **Note**
>
> Si vous rencontrez l'erreur suivante :
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pour la résoudre, tapez la commande suivante dans votre terminal.
>
> ```bash
> sudo ldconfig
> ```

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatisée [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.