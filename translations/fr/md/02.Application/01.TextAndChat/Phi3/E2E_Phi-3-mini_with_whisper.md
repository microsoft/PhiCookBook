<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:12:46+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "fr"
}
-->
# Chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

## Présentation

Le chatbot interactif Phi 3 Mini 4K Instruct est un outil qui permet aux utilisateurs d’interagir avec la démo Microsoft Phi 3 Mini 4K instruct via une saisie texte ou audio. Ce chatbot peut être utilisé pour diverses tâches, telles que la traduction, les prévisions météo, ou la collecte d’informations générales.

### Premiers pas

Pour utiliser ce chatbot, suivez simplement ces instructions :

1. Ouvrez un nouveau [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Dans la fenêtre principale du notebook, vous verrez une interface de chat avec une zone de saisie de texte et un bouton « Envoyer ».
3. Pour utiliser le chatbot basé sur le texte, tapez simplement votre message dans la zone de saisie et cliquez sur le bouton « Envoyer ». Le chatbot répondra avec un fichier audio pouvant être lu directement dans le notebook.

**Note** : Cet outil nécessite un GPU ainsi qu’un accès aux modèles Microsoft Phi-3 et OpenAI Whisper, utilisés pour la reconnaissance vocale et la traduction.

### Exigences GPU

Pour exécuter cette démo, vous avez besoin de 12 Go de mémoire GPU.

Les besoins en mémoire pour faire tourner la démo **Microsoft-Phi-3-Mini-4K instruct** sur un GPU dépendent de plusieurs facteurs, comme la taille des données d’entrée (audio ou texte), la langue utilisée pour la traduction, la vitesse du modèle, et la mémoire disponible sur le GPU.

En général, le modèle Whisper est conçu pour fonctionner sur GPU. La quantité minimale recommandée de mémoire GPU pour exécuter Whisper est de 8 Go, mais il peut gérer des quantités plus importantes si nécessaire.

Il est important de noter que traiter un grand volume de données ou un nombre élevé de requêtes peut nécessiter plus de mémoire GPU et/ou entraîner des problèmes de performance. Il est conseillé de tester votre cas d’usage avec différentes configurations et de surveiller l’utilisation mémoire pour déterminer les réglages optimaux selon vos besoins spécifiques.

## Exemple E2E pour le chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

Le notebook Jupyter intitulé [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) montre comment utiliser la démo Microsoft Phi 3 Mini 4K instruct pour générer du texte à partir d’une entrée audio ou écrite. Le notebook définit plusieurs fonctions :

1. `tts_file_name(text)` : Cette fonction génère un nom de fichier basé sur le texte d’entrée pour sauvegarder le fichier audio généré.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)` : Cette fonction utilise l’API Edge TTS pour générer un fichier audio à partir d’une liste de segments de texte. Les paramètres d’entrée sont la liste des segments, la vitesse de parole, le nom de la voix, et le chemin de sortie pour sauvegarder le fichier audio généré.
1. `talk(input_text)` : Cette fonction génère un fichier audio en utilisant l’API Edge TTS et le sauvegarde sous un nom de fichier aléatoire dans le répertoire /content/audio. Le paramètre d’entrée est le texte à convertir en parole.
1. `run_text_prompt(message, chat_history)` : Cette fonction utilise la démo Microsoft Phi 3 Mini 4K instruct pour générer un fichier audio à partir d’un message et l’ajoute à l’historique du chat.
1. `run_audio_prompt(audio, chat_history)` : Cette fonction convertit un fichier audio en texte via l’API du modèle Whisper, puis transmet ce texte à la fonction `run_text_prompt()`.
1. Le code lance une application Gradio qui permet aux utilisateurs d’interagir avec la démo Phi 3 Mini 4K instruct en tapant des messages ou en téléchargeant des fichiers audio. La sortie est affichée sous forme de message texte dans l’application.

## Dépannage

Installation des pilotes GPU Cuda

1. Assurez-vous que votre application Linux est à jour

    ```bash
    sudo apt update
    ```

1. Installez les pilotes Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Enregistrez l’emplacement du pilote cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Vérifiez la taille de la mémoire GPU Nvidia (12 Go de mémoire GPU requis)

    ```bash
    nvidia-smi
    ```

1. Vider le cache : Si vous utilisez PyTorch, vous pouvez appeler torch.cuda.empty_cache() pour libérer toute la mémoire cache inutilisée afin qu’elle puisse être utilisée par d’autres applications GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Vérification de Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Effectuez les opérations suivantes pour créer un token Hugging Face.

    - Rendez-vous sur la [page des paramètres de token Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Sélectionnez **New token**.
    - Entrez le **Nom** du projet que vous souhaitez utiliser.
    - Sélectionnez le **Type** sur **Write**.

> **Note**
>
> Si vous rencontrez l’erreur suivante :
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pour résoudre ce problème, tapez la commande suivante dans votre terminal.
>
> ```bash
> sudo ldconfig
> ```

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.