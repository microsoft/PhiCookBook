<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:47:47+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "pt"
}
-->
# Gerar Conjunto de Dados de Imagens ao descarregar DataSet do Hugging Face e imagens associadas


### Visão Geral

Este script prepara um conjunto de dados para machine learning ao descarregar as imagens necessárias, filtrar as linhas onde o download das imagens falha, e guardar o conjunto de dados como um ficheiro CSV.

### Pré-requisitos

Antes de executar este script, certifique-se de que tem as seguintes bibliotecas instaladas: `Pandas`, `Datasets`, `requests`, `PIL` e `io`. Também será necessário substituir `'Insert_Your_Dataset'` na linha 2 pelo nome do seu dataset do Hugging Face.

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

O script executa os seguintes passos:

1. Descarrega o dataset do Hugging Face usando a função `load_dataset()`.
2. Converte o dataset do Hugging Face para um DataFrame do Pandas para facilitar a manipulação, usando o método `to_pandas()`.
3. Cria diretórios para guardar o dataset e as imagens.
4. Filtra as linhas onde o download da imagem falha, iterando por cada linha do DataFrame, descarregando a imagem com a função personalizada `download_image()` e adicionando a linha filtrada a um novo DataFrame chamado `filtered_rows`.
5. Cria um novo DataFrame com as linhas filtradas e guarda-o no disco como um ficheiro CSV.
6. Imprime uma mensagem indicando onde o dataset e as imagens foram guardados.

### Função Personalizada

A função `download_image()` descarrega uma imagem a partir de uma URL e guarda-a localmente usando a biblioteca Pillow (PIL) e o módulo `io`. Retorna True se a imagem for descarregada com sucesso, e False caso contrário. A função também lança uma exceção com a mensagem de erro quando o pedido falha.

### Como funciona

A função download_image recebe dois parâmetros: image_url, que é a URL da imagem a descarregar, e save_path, que é o caminho onde a imagem descarregada será guardada.

Aqui está como a função funciona:

Começa por fazer um pedido GET à image_url usando o método requests.get. Isto obtém os dados da imagem a partir da URL.

A linha response.raise_for_status() verifica se o pedido foi bem-sucedido. Se o código de estado da resposta indicar um erro (por exemplo, 404 - Não Encontrado), será lançada uma exceção. Isto garante que só avançamos para descarregar a imagem se o pedido tiver sucesso.

Os dados da imagem são então passados para o método Image.open do módulo PIL (Python Imaging Library). Este método cria um objeto Image a partir dos dados da imagem.

A linha image.save(save_path) guarda a imagem no caminho save_path especificado. O save_path deve incluir o nome do ficheiro e a extensão desejada.

Finalmente, a função retorna True para indicar que a imagem foi descarregada e guardada com sucesso. Se ocorrer alguma exceção durante o processo, esta é capturada, é impressa uma mensagem de erro indicando a falha, e retorna False.

Esta função é útil para descarregar imagens a partir de URLs e guardá-las localmente. Trata possíveis erros durante o processo de download e fornece feedback sobre se o download foi bem-sucedido ou não.

É importante notar que a biblioteca requests é usada para fazer pedidos HTTP, a biblioteca PIL é usada para trabalhar com imagens, e a classe BytesIO é usada para tratar os dados da imagem como um fluxo de bytes.



### Conclusão

Este script oferece uma forma prática de preparar um conjunto de dados para machine learning ao descarregar as imagens necessárias, filtrar as linhas onde o download das imagens falha, e guardar o conjunto de dados como um ficheiro CSV.

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

### Exemplo de Data Set  
[Exemplo de Data Set do finetuning com LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.