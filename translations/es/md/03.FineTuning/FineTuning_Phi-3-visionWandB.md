<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:04:42+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "es"
}
-->
# Resumen del Proyecto Phi-3-Vision-128K-Instruct

## El Modelo

El Phi-3-Vision-128K-Instruct, un modelo multimodal ligero y de última generación, es el núcleo de este proyecto. Forma parte de la familia de modelos Phi-3 y soporta una longitud de contexto de hasta 128,000 tokens. El modelo fue entrenado con un conjunto de datos diverso que incluye datos sintéticos y sitios web públicos cuidadosamente filtrados, con énfasis en contenido de alta calidad y con razonamiento intensivo. El proceso de entrenamiento incluyó ajuste fino supervisado y optimización directa de preferencias para asegurar una adherencia precisa a las instrucciones, así como medidas robustas de seguridad.

## La creación de datos de ejemplo es crucial por varias razones:

1. **Pruebas**: Los datos de ejemplo permiten probar tu aplicación en diferentes escenarios sin afectar datos reales. Esto es especialmente importante en las fases de desarrollo y preproducción.

2. **Optimización del rendimiento**: Con datos de ejemplo que imitan la escala y complejidad de los datos reales, puedes identificar cuellos de botella en el rendimiento y optimizar tu aplicación en consecuencia.

3. **Prototipado**: Los datos de ejemplo pueden usarse para crear prototipos y maquetas, lo que ayuda a entender los requisitos del usuario y obtener retroalimentación.

4. **Análisis de datos**: En ciencia de datos, los datos de ejemplo se utilizan a menudo para análisis exploratorio, entrenamiento de modelos y pruebas de algoritmos.

5. **Seguridad**: Usar datos de ejemplo en entornos de desarrollo y prueba ayuda a prevenir fugas accidentales de datos sensibles reales.

6. **Aprendizaje**: Si estás aprendiendo una nueva tecnología o herramienta, trabajar con datos de ejemplo ofrece una forma práctica de aplicar lo aprendido.

Recuerda que la calidad de tus datos de ejemplo puede impactar significativamente estas actividades. Deben ser lo más similares posible a los datos reales en términos de estructura y variabilidad.

### Creación de Datos de Ejemplo
[Generate DataSet Script](./CreatingSampleData.md)

## Conjunto de Datos

Un buen ejemplo de conjunto de datos de ejemplo es el [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponible en Huggingface).  
El conjunto de datos de ejemplo de productos Burberry incluye metadatos sobre la categoría, precio y título de los productos, con un total de 3,040 filas, cada una representando un producto único. Este conjunto nos permite probar la capacidad del modelo para entender e interpretar datos visuales, generando texto descriptivo que captura detalles visuales complejos y características específicas de la marca.

**Note:** Puedes usar cualquier conjunto de datos que incluya imágenes.

## Razonamiento Complejo

El modelo necesita razonar sobre precios y nombres solo a partir de la imagen. Esto requiere que el modelo no solo reconozca características visuales, sino que también entienda sus implicaciones en términos de valor del producto y branding. Al sintetizar descripciones textuales precisas a partir de imágenes, el proyecto destaca el potencial de integrar datos visuales para mejorar el rendimiento y la versatilidad de los modelos en aplicaciones del mundo real.

## Arquitectura Phi-3 Vision

La arquitectura del modelo es una versión multimodal de Phi-3. Procesa tanto datos de texto como de imagen, integrando estas entradas en una secuencia unificada para tareas de comprensión y generación completas. El modelo utiliza capas de embedding separadas para texto e imágenes. Los tokens de texto se convierten en vectores densos, mientras que las imágenes se procesan mediante un modelo de visión CLIP para extraer embeddings de características. Estos embeddings de imagen se proyectan para coincidir con las dimensiones de los embeddings de texto, asegurando que puedan integrarse sin problemas.

## Integración de Embeddings de Texto e Imagen

Tokens especiales dentro de la secuencia de texto indican dónde deben insertarse los embeddings de imagen. Durante el procesamiento, estos tokens especiales se reemplazan con los embeddings de imagen correspondientes, permitiendo que el modelo maneje texto e imágenes como una sola secuencia. El prompt para nuestro conjunto de datos está formateado usando el token especial <|image|> de la siguiente manera:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Código de Ejemplo
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Ejemplo de recorrido con Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.