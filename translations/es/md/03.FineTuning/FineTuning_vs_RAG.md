<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-03-27T15:38:18+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_vs_RAG.md",
  "language_code": "es"
}
-->
## Ajuste fino vs RAG

## Generación Aumentada con Recuperación

RAG combina recuperación de datos y generación de texto. Los datos estructurados y no estructurados de la empresa se almacenan en la base de datos vectorial. Al buscar contenido relevante, se encuentran el resumen y contenido pertinentes para formar un contexto, y se combina con la capacidad de finalización de texto de LLM/SLM para generar contenido.

## Proceso de RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.es.png)

## Ajuste fino
El ajuste fino se basa en la mejora de un modelo determinado. No es necesario comenzar desde el algoritmo del modelo, pero se requiere acumular datos de manera continua. Si deseas una terminología más precisa y una expresión lingüística adecuada en aplicaciones industriales, el ajuste fino es tu mejor opción. Sin embargo, si tus datos cambian con frecuencia, el ajuste fino puede volverse complicado.

## Cómo elegir
Si nuestra respuesta requiere la introducción de datos externos, RAG es la mejor elección.

Si necesitas generar conocimiento estable y preciso en un ámbito industrial, el ajuste fino será una buena opción. RAG prioriza extraer contenido relevante, pero puede no captar siempre los matices especializados.

El ajuste fino requiere un conjunto de datos de alta calidad, y si solo se trata de un rango pequeño de datos, no habrá mucha diferencia. RAG es más flexible.  
El ajuste fino es una "caja negra", algo metafísico, y es difícil comprender su mecanismo interno. Por otro lado, RAG facilita encontrar la fuente de los datos, lo que permite ajustar eficazmente alucinaciones o errores en el contenido y proporciona mayor transparencia.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.