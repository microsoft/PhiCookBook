<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-03-27T12:54:42+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_OpenVino_Phi3Vision.md",
  "language_code": "es"
}
-->
Esta demostración muestra cómo usar un modelo preentrenado para generar código Python basado en una imagen y un mensaje de texto.

[Código de ejemplo](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Aquí tienes una explicación paso a paso:

1. **Importaciones y Configuración**:
   - Se importan las bibliotecas y módulos necesarios, incluyendo `requests`, `PIL` para el procesamiento de imágenes, y `transformers` para manejar el modelo y el procesamiento.

2. **Cargando y Mostrando la Imagen**:
   - Un archivo de imagen (`demo.png`) se abre utilizando la biblioteca `PIL` y se muestra.

3. **Definiendo el Mensaje**:
   - Se crea un mensaje que incluye la imagen y una solicitud para generar código Python que procese la imagen y la guarde utilizando `plt` (matplotlib).

4. **Cargando el Procesador**:
   - Se carga el `AutoProcessor` desde un modelo preentrenado especificado por el directorio `out_dir`. Este procesador manejará las entradas de texto e imagen.

5. **Creando el Mensaje**:
   - El método `apply_chat_template` se utiliza para formatear el mensaje en un formato adecuado para el modelo.

6. **Procesando las Entradas**:
   - El mensaje y la imagen se procesan en tensores que el modelo puede interpretar.

7. **Configurando los Argumentos de Generación**:
   - Se definen los argumentos para el proceso de generación del modelo, incluyendo el número máximo de nuevos tokens a generar y si se debe usar muestreo en la salida.

8. **Generando el Código**:
   - El modelo genera el código Python basado en las entradas y los argumentos de generación. `TextStreamer` se utiliza para manejar la salida, omitiendo el mensaje inicial y los tokens especiales.

9. **Salida**:
   - Se imprime el código generado, el cual debería incluir código Python para procesar la imagen y guardarla según lo especificado en el mensaje.

Esta demostración ilustra cómo aprovechar un modelo preentrenado utilizando OpenVino para generar código de manera dinámica basado en entradas del usuario e imágenes.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.