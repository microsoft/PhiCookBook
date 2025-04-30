<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-03-27T15:00:46+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Phi-3-visionWandB.md",
  "language_code": "es"
}
-->
# Resumen del Proyecto Phi-3-Vision-128K-Instruct

## El Modelo

El Phi-3-Vision-128K-Instruct, un modelo multimodal avanzado y liviano, es el núcleo de este proyecto. Forma parte de la familia de modelos Phi-3 y admite una longitud de contexto de hasta 128,000 tokens. El modelo fue entrenado con un conjunto de datos diverso que incluye datos sintéticos y sitios web públicos cuidadosamente filtrados, con énfasis en contenido de alta calidad y que requiere razonamiento intensivo. El proceso de entrenamiento incluyó ajuste fino supervisado y optimización directa de preferencias para garantizar una adhesión precisa a las instrucciones, así como medidas de seguridad robustas.

## Crear datos de muestra es crucial por varias razones:

1. **Pruebas**: Los datos de muestra te permiten probar tu aplicación en diversos escenarios sin afectar datos reales. Esto es especialmente importante en las fases de desarrollo y pruebas.

2. **Optimización del Rendimiento**: Con datos de muestra que imiten la escala y complejidad de los datos reales, puedes identificar cuellos de botella en el rendimiento y optimizar tu aplicación en consecuencia.

3. **Prototipos**: Los datos de muestra pueden usarse para crear prototipos y maquetas, lo que ayuda a comprender los requisitos del usuario y obtener retroalimentación.

4. **Análisis de Datos**: En ciencia de datos, los datos de muestra a menudo se usan para análisis exploratorio, entrenamiento de modelos y pruebas de algoritmos.

5. **Seguridad**: Usar datos de muestra en entornos de desarrollo y prueba puede ayudar a prevenir filtraciones accidentales de datos sensibles reales.

6. **Aprendizaje**: Si estás aprendiendo una nueva tecnología o herramienta, trabajar con datos de muestra puede ser una forma práctica de aplicar lo aprendido.

Recuerda, la calidad de tus datos de muestra puede impactar significativamente estas actividades. Deberían ser lo más similares posible a los datos reales en términos de estructura y variabilidad.

### Creación de Datos de Muestra
[Script para Generar Conjunto de Datos](./CreatingSampleData.md)

## Conjunto de Datos

Un buen ejemplo de conjunto de datos de muestra es [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponible en Huggingface).  
El conjunto de datos de muestra incluye productos de Burberry junto con metadatos sobre la categoría del producto, precio y título, con un total de 3,040 filas, cada una representando un producto único. Este conjunto de datos nos permite probar la capacidad del modelo para comprender e interpretar datos visuales, generando texto descriptivo que capture detalles visuales intrincados y características específicas de la marca.

**Nota:** Puedes usar cualquier conjunto de datos que incluya imágenes.

## Razonamiento Complejo

El modelo necesita razonar sobre precios y nombres basándose únicamente en la imagen. Esto requiere que el modelo no solo reconozca características visuales, sino que también entienda sus implicaciones en términos de valor del producto y marca. Al sintetizar descripciones textuales precisas a partir de imágenes, el proyecto resalta el potencial de integrar datos visuales para mejorar el rendimiento y la versatilidad de los modelos en aplicaciones del mundo real.

## Arquitectura de Phi-3 Vision

La arquitectura del modelo es una versión multimodal de un Phi-3. Procesa tanto datos de texto como de imágenes, integrando estas entradas en una secuencia unificada para tareas de comprensión y generación. El modelo utiliza capas de embeddings separadas para texto e imágenes. Los tokens de texto se convierten en vectores densos, mientras que las imágenes se procesan a través de un modelo CLIP de visión para extraer embeddings de características. Estos embeddings de imágenes luego se proyectan para coincidir con las dimensiones de los embeddings de texto, asegurando que puedan integrarse sin problemas.

## Integración de Embeddings de Texto e Imagen

Tokens especiales dentro de la secuencia de texto indican dónde deben insertarse los embeddings de imagen. Durante el procesamiento, estos tokens especiales se reemplazan con los embeddings de imagen correspondientes, permitiendo al modelo manejar texto e imágenes como una sola secuencia. El formato del prompt para nuestro conjunto de datos utiliza el token especial <|image|> de la siguiente manera:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Código de Ejemplo
- [Script de Entrenamiento de Phi-3-Vision](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Ejemplo de Walkthrough con Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.