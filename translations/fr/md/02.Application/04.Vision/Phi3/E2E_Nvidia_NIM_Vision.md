<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-07T13:43:12+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "fr"
}
-->
### Scénario Exemple

Imaginez que vous avez une image (`demo.png`) et que vous souhaitez générer un code Python qui traite cette image et enregistre une nouvelle version (`phi-3-vision.jpg`).

Le code ci-dessus automatise ce processus en :

1. Configurant l’environnement et les paramètres nécessaires.  
2. Créant une invite qui demande au modèle de générer le code Python requis.  
3. Envoyant l’invite au modèle et récupérant le code généré.  
4. Extrait et exécute le code généré.  
5. Affichant les images originale et traitée.

Cette approche exploite la puissance de l’IA pour automatiser les tâches de traitement d’image, rendant leur réalisation plus simple et plus rapide.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Décomposons ce que fait le code étape par étape :

1. **Installer le package requis** :  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Cette commande installe le package `langchain_nvidia_ai_endpoints`, en s’assurant d’avoir la dernière version.

2. **Importer les modules nécessaires** :  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Ces importations incluent les modules nécessaires pour interagir avec les endpoints NVIDIA AI, gérer les mots de passe de manière sécurisée, interagir avec le système d’exploitation, et encoder/décoder des données en base64.

3. **Configurer la clé API** :  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Ce code vérifie si la variable d’environnement `NVIDIA_API_KEY` est définie. Sinon, il invite l’utilisateur à saisir sa clé API en toute sécurité.

4. **Définir le modèle et le chemin de l’image** :  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Cela définit le modèle à utiliser, crée une instance de `ChatNVIDIA` avec ce modèle, et définit le chemin vers le fichier image.

5. **Créer l’invite textuelle** :  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Ceci définit une invite textuelle demandant au modèle de générer un code Python pour traiter une image.

6. **Encoder l’image en base64** :  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Ce code lit le fichier image, l’encode en base64, et crée une balise HTML image avec les données encodées.

7. **Combiner texte et image dans l’invite** :  
    ```python
    prompt = f"{text} {image}"
    ```  
    Cela combine l’invite textuelle et la balise image HTML en une seule chaîne.

8. **Générer le code avec ChatNVIDIA** :  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Ce code envoie l’invite à `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Extraire le code Python du contenu généré** :  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Cela extrait le code Python réel du contenu généré en supprimant la mise en forme markdown.

10. **Exécuter le code généré** :  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Ce code exécute le code Python extrait en tant que sous-processus et capture sa sortie.

11. **Afficher les images** :  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Ces lignes affichent les images en utilisant le module `IPython.display`.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.