<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-03-27T13:30:34+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "fr"
}
-->
# Générer un ensemble de données d'images en téléchargeant un DataSet depuis Hugging Face et les images associées

### Vue d'ensemble

Ce script prépare un ensemble de données pour l'apprentissage automatique en téléchargeant les images nécessaires, en filtrant les lignes où le téléchargement des images échoue, et en sauvegardant l'ensemble de données sous forme de fichier CSV.

### Prérequis

Avant d'exécuter ce script, assurez-vous d'avoir installé les bibliothèques suivantes : `Pandas`, `Datasets`, `requests`, `PIL`, et `io`. Vous devrez également remplacer `'Insert_Your_Dataset'` à la ligne 2 par le nom de votre ensemble de données provenant de Hugging Face.

Bibliothèques requises :

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Fonctionnalités

Le script effectue les étapes suivantes :

1. Télécharge l'ensemble de données depuis Hugging Face en utilisant les fonctions `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.  
2. Filtre les lignes où le téléchargement des images échoue.  
3. Sauvegarde l'ensemble de données final sous forme de fichier CSV.  

La fonction `download_image()` télécharge une image à partir d'une URL et la sauvegarde localement en utilisant la bibliothèque Pillow (PIL) et le module `io`. Elle renvoie True si l'image est téléchargée avec succès, et False sinon. La fonction lève également une exception avec un message d'erreur lorsque la requête échoue.

### Comment cela fonctionne

La fonction `download_image` prend deux paramètres : `image_url`, qui est l'URL de l'image à télécharger, et `save_path`, qui est le chemin où l'image téléchargée sera sauvegardée.

Voici comment fonctionne la fonction :

1. Elle commence par effectuer une requête GET vers `image_url` en utilisant la méthode `requests.get`. Cela récupère les données de l'image à partir de l'URL.  
2. La ligne `response.raise_for_status()` vérifie si la requête a réussi. Si le code de statut de la réponse indique une erreur (par exemple, 404 - Non trouvé), une exception est levée. Cela garantit que le téléchargement de l'image ne se poursuit que si la requête est réussie.  
3. Les données de l'image sont ensuite passées à la méthode `Image.open` du module PIL (Python Imaging Library). Cette méthode crée un objet Image à partir des données de l'image.  
4. La ligne `image.save(save_path)` sauvegarde l'image dans le chemin spécifié `save_path`. Le chemin doit inclure le nom de fichier souhaité et son extension.  
5. Enfin, la fonction renvoie True pour indiquer que l'image a été téléchargée et sauvegardée avec succès. Si une exception se produit durant le processus, elle est capturée, un message d'erreur est affiché pour indiquer l'échec, et la fonction renvoie False.  

Cette fonction est utile pour télécharger des images à partir d'URLs et les sauvegarder localement. Elle gère les erreurs potentielles durant le processus de téléchargement et fournit un retour d'information sur la réussite ou l'échec du téléchargement.

À noter que la bibliothèque `requests` est utilisée pour effectuer des requêtes HTTP, la bibliothèque PIL est utilisée pour manipuler les images, et la classe `BytesIO` est utilisée pour traiter les données de l'image comme un flux d'octets.

### Conclusion

Ce script offre une méthode pratique pour préparer un ensemble de données destiné à l'apprentissage automatique en téléchargeant les images nécessaires, en filtrant les lignes où les téléchargements échouent, et en sauvegardant l'ensemble de données sous forme de fichier CSV.

### Exemple de script

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download the dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert the Hugging Face dataset to a Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save the dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows where image download fails
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Create a new DataFrame with the filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save the updated dataset to disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### Téléchargement du code exemple  
[Script pour générer un nouvel ensemble de données](../../../../code/04.Finetuning/generate_dataset.py)

### Exemple d'ensemble de données  
[Exemple d'ensemble de données issu du finetuning avec LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.