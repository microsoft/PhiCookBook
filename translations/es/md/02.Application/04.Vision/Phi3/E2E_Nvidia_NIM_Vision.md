<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-07T10:59:11+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "es"
}
-->
### Escenario de Ejemplo

Imagina que tienes una imagen (`demo.png`) y quieres generar código Python que procese esta imagen y guarde una nueva versión de la misma (`phi-3-vision.jpg`).

El código anterior automatiza este proceso mediante:

1. Configurar el entorno y las configuraciones necesarias.  
2. Crear un prompt que indique al modelo generar el código Python requerido.  
3. Enviar el prompt al modelo y recopilar el código generado.  
4. Extraer y ejecutar el código generado.  
5. Mostrar las imágenes original y procesada.

Este enfoque aprovecha el poder de la IA para automatizar tareas de procesamiento de imágenes, facilitando y acelerando la consecución de tus objetivos.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Desglosemos paso a paso qué hace todo el código:

1. **Instalar el Paquete Requerido**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Este comando instala el paquete `langchain_nvidia_ai_endpoints`, asegurándose de que sea la versión más reciente.

2. **Importar Módulos Necesarios**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Estas importaciones incluyen los módulos necesarios para interactuar con los endpoints de NVIDIA AI, manejar contraseñas de forma segura, trabajar con el sistema operativo y codificar/decodificar datos en formato base64.

3. **Configurar la Clave API**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Este código verifica si la variable de entorno `NVIDIA_API_KEY` está configurada. Si no es así, solicita al usuario que ingrese su clave API de manera segura.

4. **Definir Modelo y Ruta de la Imagen**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Aquí se establece el modelo a usar, se crea una instancia de `ChatNVIDIA` con el modelo especificado y se define la ruta al archivo de imagen.

5. **Crear el Texto del Prompt**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Se define un texto que indica al modelo que genere código Python para procesar una imagen.

6. **Codificar la Imagen en Base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Este código lee el archivo de imagen, lo codifica en base64 y crea una etiqueta HTML de imagen con los datos codificados.

7. **Combinar Texto e Imagen en el Prompt**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    Aquí se combinan el texto del prompt y la etiqueta HTML de la imagen en una sola cadena.

8. **Generar Código Usando ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Este código envía el prompt al `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Extraer el Código Python del Contenido Generado**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Esto extrae el código Python real del contenido generado eliminando el formato markdown.

10. **Ejecutar el Código Generado**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Este paso ejecuta el código Python extraído como un subproceso y captura su salida.

11. **Mostrar las Imágenes**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Estas líneas muestran las imágenes usando el módulo `IPython.display`.

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.