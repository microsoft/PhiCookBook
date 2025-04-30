<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-03-27T08:23:59+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "es"
}
-->
# **Cuantización de Phi-3.5 usando el Framework Apple MLX**

MLX es un framework de arrays para investigación en aprendizaje automático en dispositivos Apple silicon, desarrollado por el equipo de investigación de aprendizaje automático de Apple.

MLX está diseñado por investigadores de aprendizaje automático para investigadores de aprendizaje automático. El framework tiene como objetivo ser fácil de usar, pero eficiente para entrenar y desplegar modelos. Además, el diseño del framework es conceptualmente simple, lo que facilita que los investigadores lo amplíen y mejoren con el objetivo de explorar nuevas ideas rápidamente.

Los LLMs pueden acelerarse en dispositivos Apple Silicon mediante MLX, y los modelos pueden ejecutarse localmente de manera muy conveniente.

Actualmente, el Framework Apple MLX admite la conversión de cuantización de Phi-3.5-Instruct (**compatibilidad con el Framework Apple MLX**), Phi-3.5-Vision (**compatibilidad con el Framework MLX-VLM**) y Phi-3.5-MoE (**compatibilidad con el Framework Apple MLX**). Vamos a probarlo a continuación:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Ejemplos de Phi-3.5 con Apple MLX**

| Laboratorios    | Descripción | Ir |
| -------- | ------- |  ------- |
| 🚀 Laboratorio - Introducción a Phi-3.5 Instruct  | Aprende cómo usar Phi-3.5 Instruct con el framework Apple MLX   |  [Ir](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Laboratorio - Introducción a Phi-3.5 Vision (imagen) | Aprende cómo usar Phi-3.5 Vision para analizar imágenes con el framework Apple MLX     |  [Ir](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Laboratorio - Introducción a Phi-3.5 Vision (moE)   | Aprende cómo usar Phi-3.5 MoE con el framework Apple MLX  |  [Ir](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Recursos**

1. Aprende más sobre el Framework Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositorio GitHub de Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositorio GitHub de MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.