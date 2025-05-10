<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:23:54+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "br"
}
-->
# Generate Image Data Set by downloading DataSet from Hugging Face and associated images


### Overview

Este script prepara un conjunto de datos para aprendizaje automático descargando las imágenes necesarias, filtrando las filas donde la descarga de imágenes falla, y guardando el conjunto de datos como un archivo CSV.

### Prerequisites

Antes de ejecutar este script, asegúrate de tener instaladas las siguientes librerías: `Pandas`, `Datasets`, `requests`, `PIL`, y `io`. También necesitarás reemplazar `'Insert_Your_Dataset'` en la línea 2 con el nombre de tu conjunto de datos de Hugging Face.

Required Libraries:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Functionality

El script realiza los siguientes pasos:

1. Descarga el conjunto de datos desde Hugging Face usando la función `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` descarga una imagen desde una URL y la guarda localmente usando la biblioteca Pillow Image Library (PIL) y el módulo `io`. Devuelve True si la imagen se descarga correctamente, y False en caso contrario. La función también lanza una excepción con el mensaje de error cuando la solicitud falla.

### How does this work

La función download_image recibe dos parámetros: image_url, que es la URL de la imagen a descargar, y save_path, que es la ruta donde se guardará la imagen descargada.

Así es como funciona la función:

Comienza haciendo una petición GET a image_url usando el método requests.get. Esto recupera los datos de la imagen desde la URL.

La línea response.raise_for_status() verifica si la solicitud fue exitosa. Si el código de estado de la respuesta indica un error (por ejemplo, 404 - No Encontrado), lanzará una excepción. Esto asegura que solo procedamos a descargar la imagen si la solicitud fue exitosa.

Los datos de la imagen se pasan luego al método Image.open del módulo PIL (Python Imaging Library). Este método crea un objeto Image a partir de los datos de la imagen.

La línea image.save(save_path) guarda la imagen en la ruta especificada por save_path. El save_path debe incluir el nombre de archivo y la extensión deseados.

Finalmente, la función devuelve True para indicar que la imagen se descargó y guardó correctamente. Si ocurre alguna excepción durante el proceso, la captura, imprime un mensaje de error indicando la falla y devuelve False.

Esta función es útil para descargar imágenes desde URLs y guardarlas localmente. Maneja posibles errores durante el proceso de descarga y proporciona retroalimentación sobre si la descarga fue exitosa o no.

Vale la pena mencionar que la librería requests se usa para hacer peticiones HTTP, la librería PIL para trabajar con imágenes, y la clase BytesIO para manejar los datos de la imagen como un flujo de bytes.



### Conclusion

Este script ofrece una forma práctica de preparar un conjunto de datos para aprendizaje automático descargando las imágenes necesarias, filtrando las filas donde la descarga de imágenes falla, y guardando el conjunto de datos como un archivo CSV.

### Sample Script

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

### Sample Code Download 
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Sample Data Set
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.