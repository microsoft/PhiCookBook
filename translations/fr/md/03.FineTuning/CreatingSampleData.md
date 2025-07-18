<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:44:04+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "fr"
}
-->
# Générer un jeu de données d’images en téléchargeant un DataSet depuis Hugging Face et les images associées


### Vue d’ensemble

Ce script prépare un jeu de données pour l’apprentissage automatique en téléchargeant les images nécessaires, en filtrant les lignes où le téléchargement des images échoue, et en sauvegardant le jeu de données au format CSV.

### Prérequis

Avant d’exécuter ce script, assurez-vous d’avoir installé les bibliothèques suivantes : `Pandas`, `Datasets`, `requests`, `PIL` et `io`. Vous devrez également remplacer `'Insert_Your_Dataset'` à la ligne 2 par le nom de votre jeu de données provenant de Hugging Face.

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

1. Télécharge le jeu de données depuis Hugging Face en utilisant la fonction `load_dataset()`.
2. Convertit le jeu de données Hugging Face en DataFrame Pandas pour une manipulation plus aisée grâce à la méthode `to_pandas()`.
3. Crée les répertoires pour sauvegarder le jeu de données et les images.
4. Filtre les lignes où le téléchargement des images échoue en parcourant chaque ligne du DataFrame, téléchargeant l’image avec la fonction personnalisée `download_image()`, et en ajoutant les lignes valides à un nouveau DataFrame nommé `filtered_rows`.
5. Crée un nouveau DataFrame avec les lignes filtrées et le sauvegarde sur disque au format CSV.
6. Affiche un message indiquant où le jeu de données et les images ont été enregistrés.

### Fonction personnalisée

La fonction `download_image()` télécharge une image depuis une URL et la sauvegarde localement en utilisant la bibliothèque Pillow (PIL) et le module `io`. Elle retourne True si l’image est téléchargée avec succès, et False sinon. La fonction lève également une exception avec le message d’erreur lorsque la requête échoue.

### Comment ça fonctionne

La fonction download_image prend deux paramètres : image_url, qui est l’URL de l’image à télécharger, et save_path, qui est le chemin où l’image téléchargée sera enregistrée.

Voici comment fonctionne la fonction :

Elle commence par effectuer une requête GET vers image_url en utilisant la méthode requests.get. Cela récupère les données de l’image depuis l’URL.

La ligne response.raise_for_status() vérifie si la requête a réussi. Si le code de statut de la réponse indique une erreur (par exemple, 404 - Non trouvé), une exception sera levée. Cela garantit que le téléchargement de l’image ne se poursuit que si la requête a réussi.

Les données de l’image sont ensuite passées à la méthode Image.open du module PIL (Python Imaging Library). Cette méthode crée un objet Image à partir des données.

La ligne image.save(save_path) enregistre l’image à l’emplacement spécifié par save_path. Le save_path doit inclure le nom de fichier et l’extension souhaités.

Enfin, la fonction retourne True pour indiquer que l’image a été téléchargée et sauvegardée avec succès. Si une exception survient durant le processus, elle est interceptée, un message d’erreur indiquant l’échec est affiché, et la fonction retourne False.

Cette fonction est utile pour télécharger des images depuis des URL et les enregistrer localement. Elle gère les erreurs potentielles lors du téléchargement et fournit un retour sur la réussite ou non du téléchargement.

Il est important de noter que la bibliothèque requests est utilisée pour effectuer les requêtes HTTP, la bibliothèque PIL pour manipuler les images, et la classe BytesIO pour gérer les données de l’image sous forme de flux d’octets.



### Conclusion

Ce script offre un moyen simple de préparer un jeu de données pour l’apprentissage automatique en téléchargeant les images nécessaires, en filtrant les lignes où le téléchargement échoue, et en sauvegardant le jeu de données au format CSV.

### Script d’exemple

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

### Exemple de téléchargement de code  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Exemple de jeu de données  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.