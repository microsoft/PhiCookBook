<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-03-27T13:31:34+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "es"
}
-->
# Generar un conjunto de datos de imágenes descargando el DataSet desde Hugging Face y las imágenes asociadas

### Descripción general

Este script prepara un conjunto de datos para aprendizaje automático descargando las imágenes necesarias, filtrando las filas donde las descargas de imágenes fallan, y guardando el conjunto de datos como un archivo CSV.

### Requisitos previos

Antes de ejecutar este script, asegúrate de tener instaladas las siguientes bibliotecas: `Pandas`, `Datasets`, `requests`, `PIL` y `io`. También necesitarás reemplazar `'Insert_Your_Dataset'` en la línea 2 con el nombre de tu conjunto de datos de Hugging Face.

Bibliotecas requeridas:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funcionalidad

El script realiza los siguientes pasos:

1. Descarga el conjunto de datos desde Hugging Face utilizando `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. La función `download_image()` descarga una imagen desde una URL y la guarda localmente utilizando la biblioteca Pillow Image Library (PIL) y el módulo `io`. Devuelve True si la imagen se descarga correctamente, y False en caso contrario. Además, la función lanza una excepción con el mensaje de error cuando la solicitud falla.

### ¿Cómo funciona?

La función `download_image` toma dos parámetros: `image_url`, que es la URL de la imagen a descargar, y `save_path`, que es la ruta donde se guardará la imagen descargada.

Así es como funciona la función:

- Comienza haciendo una solicitud GET a `image_url` utilizando el método `requests.get`. Esto recupera los datos de la imagen desde la URL.

- La línea `response.raise_for_status()` verifica si la solicitud fue exitosa. Si el código de estado de la respuesta indica un error (por ejemplo, 404 - No encontrado), se lanzará una excepción. Esto asegura que solo procedamos con la descarga de la imagen si la solicitud fue exitosa.

- Los datos de la imagen se pasan al método `Image.open` del módulo PIL (Python Imaging Library). Este método crea un objeto Image a partir de los datos de la imagen.

- La línea `image.save(save_path)` guarda la imagen en la ruta especificada `save_path`. La ruta debe incluir el nombre del archivo y la extensión deseados.

- Finalmente, la función devuelve True para indicar que la imagen se descargó y guardó exitosamente. Si ocurre alguna excepción durante el proceso, esta se captura, se imprime un mensaje de error indicando el fallo, y se devuelve False.

Esta función es útil para descargar imágenes desde URLs y guardarlas localmente. Maneja posibles errores durante el proceso de descarga y proporciona información sobre si la descarga fue exitosa o no.

Es importante destacar que la biblioteca `requests` se utiliza para realizar solicitudes HTTP, la biblioteca `PIL` se utiliza para trabajar con imágenes, y la clase `BytesIO` se utiliza para manejar los datos de la imagen como un flujo de bytes.

### Conclusión

Este script ofrece una forma conveniente de preparar un conjunto de datos para aprendizaje automático descargando las imágenes necesarias, filtrando las filas donde las descargas fallan, y guardando el conjunto de datos como un archivo CSV.

### Script de ejemplo

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

### Descarga de código de ejemplo
[Generar script para un nuevo conjunto de datos](../../../../code/04.Finetuning/generate_dataset.py)

### Ejemplo de conjunto de datos
[Ejemplo de conjunto de datos del ajuste fino con LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.