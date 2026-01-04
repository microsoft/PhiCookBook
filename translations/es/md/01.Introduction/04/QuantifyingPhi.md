<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-04T06:40:56+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "es"
}
-->
# **Cuantificación de la familia Phi**

La cuantización de modelos se refiere al proceso de mapear los parámetros (como pesos y valores de activación) en un modelo de red neuronal desde un amplio rango de valores (generalmente un rango continuo) a un rango finito más pequeño. Esta tecnología puede reducir el tamaño y la complejidad computacional del modelo y mejorar la eficiencia de funcionamiento del modelo en entornos con recursos limitados, como dispositivos móviles o sistemas embebidos. La cuantización del modelo logra compresión al reducir la precisión de los parámetros, pero también introduce cierta pérdida de precisión. Por lo tanto, en el proceso de cuantización es necesario equilibrar el tamaño del modelo, la complejidad computacional y la precisión. Los métodos comunes de cuantización incluyen la cuantización en punto fijo, la cuantización en coma flotante, etc. Puedes elegir la estrategia de cuantización adecuada según el escenario y las necesidades específicas.

Esperamos desplegar modelos GenAI en dispositivos edge y permitir que más dispositivos entren en escenarios GenAI, como dispositivos móviles, AI PC/Copilot+PC y dispositivos IoT tradicionales. A través del modelo cuantizado, podemos desplegarlo en diferentes dispositivos edge según el equipo. Combinado con el framework de aceleración de modelos y el modelo de cuantización proporcionados por los fabricantes de hardware, podemos construir mejores escenarios de aplicación SLM.

En el escenario de cuantización, tenemos diferentes precisiones (INT4, INT8, FP16, FP32). A continuación se presenta una explicación de las precisiones de cuantización comúnmente utilizadas

### **INT4**

La cuantización INT4 es un método de cuantización radical que cuantiza los pesos y los valores de activación del modelo en enteros de 4 bits. La cuantización INT4 suele producir una mayor pérdida de precisión debido al rango de representación más pequeño y la menor precisión. Sin embargo, en comparación con la cuantización INT8, la cuantización INT4 puede reducir aún más los requisitos de almacenamiento y la complejidad computacional del modelo. Cabe señalar que la cuantización INT4 es relativamente rara en aplicaciones prácticas, ya que una precisión demasiado baja puede provocar una degradación significativa en el rendimiento del modelo. Además, no todo el hardware admite operaciones INT4, por lo que es necesario considerar la compatibilidad del hardware al elegir un método de cuantización.

### **INT8**

La cuantización INT8 es el proceso de convertir los pesos y las activaciones de un modelo de números de punto flotante a enteros de 8 bits. Aunque el rango numérico representado por los enteros INT8 es más pequeño y menos preciso, puede reducir significativamente los requisitos de almacenamiento y cálculo. En la cuantización INT8, los pesos y los valores de activación del modelo pasan por un proceso de cuantización, que incluye escalado y desplazamiento, para preservar la mayor información posible del punto flotante original. Durante la inferencia, estos valores cuantizados se descuantizan nuevamente a números de punto flotante para el cálculo y luego se cuantizan de nuevo a INT8 para el siguiente paso. Este método puede proporcionar una precisión suficiente en la mayoría de las aplicaciones manteniendo una alta eficiencia computacional.

### **FP16**

El formato FP16, es decir, números en coma flotante de 16 bits (float16), reduce la huella de memoria a la mitad en comparación con los números en coma flotante de 32 bits (float32), lo que presenta ventajas significativas en aplicaciones de aprendizaje profundo a gran escala. El formato FP16 permite cargar modelos más grandes o procesar más datos dentro de las mismas limitaciones de memoria de la GPU. A medida que el hardware de GPU moderno continúa soportando operaciones FP16, el uso del formato FP16 también puede traer mejoras en la velocidad de cálculo. Sin embargo, el formato FP16 también tiene desventajas inherentes, a saber, una menor precisión, lo que puede conducir a inestabilidad numérica o pérdida de precisión en algunos casos.

### **FP32**

El formato FP32 ofrece mayor precisión y puede representar con exactitud una amplia gama de valores. En escenarios donde se realizan operaciones matemáticas complejas o se requieren resultados de alta precisión, se prefiere el formato FP32. Sin embargo, la alta precisión también significa un mayor uso de memoria y tiempos de cálculo más largos. Para modelos de aprendizaje profundo a gran escala, especialmente cuando hay muchos parámetros del modelo y una enorme cantidad de datos, el formato FP32 puede provocar insuficiencia de memoria en la GPU o una disminución en la velocidad de inferencia.

En dispositivos móviles o dispositivos IoT, podemos convertir modelos Phi-3.x a INT4, mientras que AI PC / Copilot PC puede usar precisiones más altas como INT8, FP16, FP 32.

En la actualidad, diferentes fabricantes de hardware tienen distintos frameworks para soportar modelos generativos, como OpenVINO de Intel, QNN de Qualcomm, MLX de Apple y CUDA de Nvidia, etc., combinados con la cuantización del modelo para completar el despliegue local.

En términos de tecnología, tenemos diferentes soportes de formato tras la cuantización, como el formato PyTorch / TensorFlow, GGUF y ONNX. He realizado una comparación de formatos y escenarios de aplicación entre GGUF y ONNX. Aquí recomiendo el formato de cuantización ONNX, que cuenta con un buen soporte desde el framework del modelo hasta el hardware. En este capítulo, nos centraremos en ONNX Runtime para GenAI, OpenVINO y Apple MLX para realizar la cuantización de modelos (si tienes una mejor forma, también puedes aportarla enviando un PR)

**Este capítulo incluye**

1. [Cuantizando Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Cuantizando Phi-3.5 / 4 usando las extensiones Generative AI para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Cuantizando Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Cuantizando Phi-3.5 / 4 usando el framework Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Descargo de responsabilidad:
Este documento ha sido traducido utilizando el servicio de traducción por IA Co-op Translator (https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda recurrir a una traducción profesional realizada por un traductor humano. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->