Esta demostración muestra cómo usar un modelo pretrained para generar código Python basado en una imagen y un texto de entrada.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Aquí tienes una explicación paso a paso:

1. **Imports y configuración**:
   - Se importan las librerías y módulos necesarios, incluyendo `requests`, `PIL` para el procesamiento de imágenes, y `transformers` para manejar el modelo y el procesamiento.

2. **Cargar y mostrar la imagen**:
   - Se abre un archivo de imagen (`demo.png`) usando la librería `PIL` y se muestra.

3. **Definir el prompt**:
   - Se crea un mensaje que incluye la imagen y una solicitud para generar código Python que procese la imagen y la guarde usando `plt` (matplotlib).

4. **Cargar el Processor**:
   - Se carga el `AutoProcessor` desde un modelo pretrained especificado por el directorio `out_dir`. Este processor manejará las entradas de texto e imagen.

5. **Crear el prompt**:
   - Se usa el método `apply_chat_template` para formatear el mensaje en un prompt adecuado para el modelo.

6. **Procesar las entradas**:
   - El prompt y la imagen se procesan en tensores que el modelo puede entender.

7. **Configurar los argumentos de generación**:
   - Se definen los argumentos para el proceso de generación del modelo, incluyendo el número máximo de tokens nuevos a generar y si se debe muestrear la salida.

8. **Generar el código**:
   - El modelo genera el código Python basado en las entradas y los argumentos de generación. Se usa `TextStreamer` para manejar la salida, omitiendo el prompt y los tokens especiales.

9. **Salida**:
   - Se imprime el código generado, que debería incluir código Python para procesar la imagen y guardarla según lo especificado en el prompt.

Esta demostración ilustra cómo aprovechar un modelo pretrained usando OpenVino para generar código dinámicamente basado en la entrada del usuario y las imágenes.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.