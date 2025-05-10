<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:23:46+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "pt"
}
-->
# Gerar Conjunto de Dados de Imagens baixando DataSet do Hugging Face e imagens associadas


### Visão Geral

Este script prepara um conjunto de dados para machine learning baixando as imagens necessárias, filtrando as linhas onde o download das imagens falha, e salvando o conjunto de dados como um arquivo CSV.

### Pré-requisitos

Antes de executar este script, certifique-se de ter as seguintes bibliotecas instaladas: `Pandas`, `Datasets`, `requests`, `PIL` e `io`. Você também precisará substituir `'Insert_Your_Dataset'` na linha 2 pelo nome do seu dataset do Hugging Face.

Bibliotecas necessárias:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funcionalidade

O script realiza os seguintes passos:

1. Baixa o dataset do Hugging Face usando a função `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` faz o download de uma imagem a partir de uma URL e a salva localmente utilizando a biblioteca Pillow Image Library (PIL) e o módulo `io`. Retorna True se a imagem for baixada com sucesso, e False caso contrário. A função também lança uma exceção com a mensagem de erro quando a requisição falha.

### Como isso funciona

A função download_image recebe dois parâmetros: image_url, que é a URL da imagem a ser baixada, e save_path, que é o caminho onde a imagem baixada será salva.

Veja como a função funciona:

Ela começa fazendo uma requisição GET para image_url usando o método requests.get. Isso recupera os dados da imagem a partir da URL.

A linha response.raise_for_status() verifica se a requisição foi bem-sucedida. Se o código de status da resposta indicar um erro (por exemplo, 404 - Não Encontrado), ela lança uma exceção. Isso garante que só prosseguimos com o download da imagem se a requisição tiver sido bem-sucedida.

Os dados da imagem são então passados para o método Image.open do módulo PIL (Python Imaging Library). Esse método cria um objeto Image a partir dos dados da imagem.

A linha image.save(save_path) salva a imagem no caminho especificado por save_path. O save_path deve incluir o nome do arquivo desejado e a extensão.

Por fim, a função retorna True para indicar que a imagem foi baixada e salva com sucesso. Se ocorrer qualquer exceção durante o processo, ela captura a exceção, imprime uma mensagem de erro indicando a falha, e retorna False.

Esta função é útil para baixar imagens a partir de URLs e salvá-las localmente. Ela trata possíveis erros durante o processo de download e fornece um feedback sobre o sucesso ou falha do download.

Vale destacar que a biblioteca requests é usada para fazer requisições HTTP, a biblioteca PIL é usada para trabalhar com imagens, e a classe BytesIO é usada para manipular os dados da imagem como um fluxo de bytes.



### Conclusão

Este script oferece uma forma prática de preparar um conjunto de dados para machine learning baixando as imagens necessárias, filtrando as linhas onde o download das imagens falha, e salvando o conjunto de dados como um arquivo CSV.

### Script de Exemplo

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

### Código de Exemplo para Download  
[Gerar um novo script de Data Set](../../../../code/04.Finetuning/generate_dataset.py)

### Conjunto de Dados de Exemplo
[Exemplo de Data Set do fine-tuning com LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.