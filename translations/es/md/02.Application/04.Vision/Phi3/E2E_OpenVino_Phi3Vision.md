<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-07T10:59:41+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "es"
}
-->
Esta demostración muestra cómo usar un modelo pretrained para generar código Python basado en una imagen y un texto de entrada.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Aquí tienes una explicación paso a paso:

1. **Imports and Setup**:
   - Se importan las librerías y módulos necesarios, incluyendo `requests`, `PIL` para el procesamiento de imágenes, y `transformers` para manejar el modelo y el procesamiento.

2. **Loading and Displaying the Image**:
   - Se abre un archivo de imagen (`demo.png`) usando la librería `PIL` y se muestra.

3. **Defining the Prompt**:
   - Se crea un mensaje que incluye la imagen y una solicitud para generar código Python que procese la imagen y la guarde usando `plt` (matplotlib).

4. **Loading the Processor**:
   - Se carga `AutoProcessor` desde un modelo pretrained especificado por el directorio `out_dir`. Este procesador manejará las entradas de texto e imagen.

5. **Creating the Prompt**:
   - Se utiliza el método `apply_chat_template` para formatear el mensaje en un prompt adecuado para el modelo.

6. **Processing the Inputs**:
   - El prompt y la imagen se procesan en tensores que el modelo puede entender.

7. **Setting Generation Arguments**:
   - Se definen los argumentos para el proceso de generación del modelo, incluyendo el número máximo de tokens nuevos a generar y si se debe muestrear la salida.

8. **Generating the Code**:
   - El modelo genera el código Python basado en las entradas y los argumentos de generación. Se utiliza `TextStreamer` para manejar la salida, omitiendo el prompt y los tokens especiales.

9. **Output**:
   - Se imprime el código generado, que debería incluir código Python para procesar la imagen y guardarla según lo especificado en el prompt.

Esta demostración ilustra cómo aprovechar un modelo pretrained usando OpenVino para generar código dinámicamente basado en la entrada del usuario y las imágenes.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.