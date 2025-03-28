<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-03-27T12:36:16+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi4\\GenProjectCode\\README.md",
  "language_code": "es"
}
-->
## **Usar Phi-4-mini-mm para generar código**

Phi-4-mini continúa con las potentes capacidades de codificación de la Familia Phi. Puedes usar Prompt para hacer preguntas relacionadas con la programación. Por supuesto, después de añadir la capacidad de razonamiento avanzado, cuenta con habilidades de codificación aún más fuertes, como generar proyectos según los requisitos. Por ejemplo, generar proyectos según las necesidades, como:

### **Requisito**

Crear una aplicación de carrito de compras

- Crear una API Rest con los siguientes métodos:
    - Obtener una lista de cervezas utilizando paginación con offset y límite.
    - Obtener detalles de una cerveza por su id.
    - Buscar cervezas por nombre, descripción, eslogan, maridajes con comida y precio.
- Crear una lista de productos en la página principal.
    - Crear una barra de búsqueda para filtrar productos.
    - Navegar a la página de descripción cuando el usuario haga clic en un producto.
- (Opcional) Filtro para clasificar productos por precio.
- Crear un carrito de compras.
    - Agregar productos al carrito.
    - Eliminar productos del carrito.
    - Calcular el precio total de los productos en el carrito.

### **Código de ejemplo - Python**

```python

import requests
import torch
from PIL import Image
import soundfile
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig,pipeline,AutoTokenizer

model_path = 'Your Phi-4-mini-mm-instruct'

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype='auto',
    _attn_implementation='flash_attention_2',
).cuda()

generation_config = GenerationConfig.from_pretrained(model_path, 'generation_config.json')

user_prompt = '<|user|>'
assistant_prompt = '<|assistant|>'
prompt_suffix = '<|end|>'

requirement = """

Create a Shopping Cart App

- Create an API Rest with the following methods:
    - Get a list of beers using page offset and limit.
    - Get beer details by id.
    - Search for beer by name, description, tagline, food pairings, and price.
- Create a list of products on the main page.
    - Create a search bar to filter products.
    - Navigate to the description page when the user clicks on a product.
- (Optional) Slicer to filter products by price.
- Create a shopping cart.
    - Add products to the cart.
    - Remove products from the cart.
    - Calculate the total price of the products in the cart."""

note = """ 

            Note:

            1. Use Python Flask to create a Repository pattern based on the following structure to generate the files

            ｜- models
            ｜- controllers
            ｜- repositories
            ｜- views

            2. For the view page, please use SPA + VueJS + TypeScript to build

            3. Firstly use markdown to output the generated project structure (including directories and files), and then generate the  file names and corresponding codes step by step, output like this 

               ## Project Structure

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## Backend
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## Frontend
                 
                   #### `templates/index.html`
                   ```html

                   ```
                   ......."""

prompt = f'{user_prompt}Please create a project with Python and Flask according to the following requirements：\n{requirement}{note}{prompt_suffix}{assistant_prompt}'

inputs = processor(prompt, images=None, return_tensors='pt').to('cuda:0')

generate_ids = model.generate(
    **inputs,
    max_new_tokens=2048,
    generation_config=generation_config,
)

generate_ids = generate_ids[:, inputs['input_ids'].shape[1] :]

response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]

print(response)

```

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.