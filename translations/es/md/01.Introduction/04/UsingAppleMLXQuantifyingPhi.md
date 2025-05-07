<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-07T10:46:51+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "es"
}
-->
# **Cuantificando Phi-3.5 usando Apple MLX Framework**

MLX es un framework de arrays para investigación en aprendizaje automático en Apple silicon, desarrollado por el equipo de investigación en machine learning de Apple.

MLX está diseñado por investigadores de machine learning para investigadores de machine learning. El framework está pensado para ser fácil de usar, pero a la vez eficiente para entrenar y desplegar modelos. El diseño del framework es conceptualmente simple. Nuestro objetivo es facilitar que los investigadores extiendan y mejoren MLX para poder explorar nuevas ideas rápidamente.

Los LLMs pueden acelerarse en dispositivos Apple Silicon mediante MLX, y los modelos pueden ejecutarse localmente de forma muy conveniente.

Actualmente, Apple MLX Framework soporta la conversión de cuantización de Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**) y Phi-3.5-MoE (**Apple MLX Framework support**). Probémoslo a continuación:

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

### **🤖 Ejemplos para Phi-3.5 con Apple MLX**

| Labs    | Introducción | Ir |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Aprende a usar Phi-3.5 Instruct con el framework Apple MLX   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (imagen) | Aprende a usar Phi-3.5 Vision para analizar imágenes con el framework Apple MLX     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Aprende a usar Phi-3.5 MoE con el framework Apple MLX  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Recursos**

1. Aprende sobre Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositorio Apple MLX en GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositorio MLX-VLM en GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.