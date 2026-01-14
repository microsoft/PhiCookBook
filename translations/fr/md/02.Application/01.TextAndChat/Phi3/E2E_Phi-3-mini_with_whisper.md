<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:00:20+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "fr"
}
-->
# Chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

## Vue d'ensemble

Le chatbot interactif Phi 3 Mini 4K Instruct est un outil qui permet aux utilisateurs d’interagir avec la démo Microsoft Phi 3 Mini 4K instruct en utilisant une entrée texte ou audio. Le chatbot peut être utilisé pour diverses tâches, telles que la traduction, les mises à jour météo et la collecte d’informations générales.

### Pour commencer

Pour utiliser ce chatbot, il suffit de suivre ces instructions :

1. Ouvrez un nouveau [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. Dans la fenêtre principale du notebook, vous verrez une interface de chat avec une zone de saisie de texte et un bouton « Envoyer ».
3. Pour utiliser le chatbot basé sur le texte, tapez simplement votre message dans la zone de saisie de texte et cliquez sur le bouton « Envoyer ». Le chatbot répondra avec un fichier audio pouvant être lu directement depuis le notebook.

**Note** : Cet outil nécessite un GPU et l’accès aux modèles Microsoft Phi-3 et OpenAI Whisper, qui sont utilisés pour la reconnaissance vocale et la traduction.

### Exigences GPU

Pour exécuter cette démo, vous avez besoin de 12 Go de mémoire GPU.

Les exigences en mémoire pour exécuter la démo **Microsoft-Phi-3-Mini-4K instruct** sur un GPU dépendront de plusieurs facteurs, tels que la taille des données d’entrée (audio ou texte), la langue utilisée pour la traduction, la vitesse du modèle, et la mémoire disponible sur le GPU.

En général, le modèle Whisper est conçu pour fonctionner sur des GPU. La quantité minimale recommandée de mémoire GPU pour exécuter le modèle Whisper est de 8 Go, mais il peut gérer des quantités plus importantes si nécessaire.

Il est important de noter que le traitement d’un grand volume de données ou d’un fort nombre de requêtes sur le modèle peut nécessiter plus de mémoire GPU et/ou provoquer des problèmes de performance. Il est recommandé de tester votre cas d’utilisation avec différentes configurations et de surveiller l’utilisation de la mémoire afin de déterminer les réglages optimaux pour vos besoins spécifiques.

## Exemple E2E pour le chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

Le notebook Jupyter intitulé [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) montre comment utiliser la démo Microsoft Phi 3 Mini 4K instruct pour générer du texte à partir d’une entrée audio ou textuelle. Le notebook définit plusieurs fonctions :

1. `tts_file_name(text)`: Cette fonction génère un nom de fichier basé sur le texte d’entrée pour sauvegarder le fichier audio généré.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Cette fonction utilise l’API Edge TTS pour générer un fichier audio à partir d’une liste de morceaux de texte d’entrée. Les paramètres d’entrée sont la liste des morceaux, la vitesse de parole, le nom de la voix, et le chemin de sortie pour enregistrer le fichier audio généré.
1. `talk(input_text)`: Cette fonction génère un fichier audio en utilisant l’API Edge TTS et le sauvegarde dans un fichier au nom aléatoire dans le répertoire /content/audio. Le paramètre d’entrée est le texte à convertir en parole.
1. `run_text_prompt(message, chat_history)`: Cette fonction utilise la démo Microsoft Phi 3 Mini 4K instruct pour générer un fichier audio à partir d’un message en entrée et l’ajoute à l’historique du chat.
1. `run_audio_prompt(audio, chat_history)`: Cette fonction convertit un fichier audio en texte en utilisant l’API du modèle Whisper et le transmet à la fonction `run_text_prompt()`.
1. Le code lance une application Gradio qui permet aux utilisateurs d’interagir avec la démo Phi 3 Mini 4K instruct, soit en tapant des messages, soit en téléchargeant des fichiers audio. La sortie est affichée sous forme de message texte dans l’application.

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

1. Vérifiez Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Effectuez les tâches suivantes pour créer un jeton Hugging Face.

    - Rendez-vous sur la [page des paramètres des jetons Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Sélectionnez **Nouveau jeton**.
    - Entrez le **Nom** du projet que vous souhaitez utiliser.
    - Sélectionnez le **Type** sur **Écriture**.

> [!NOTE]
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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->