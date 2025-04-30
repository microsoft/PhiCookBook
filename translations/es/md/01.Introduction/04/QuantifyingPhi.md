<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-03-27T08:17:46+00:00",
  "source_file": "md\\01.Introduction\\04\\QuantifyingPhi.md",
  "language_code": "es"
}
-->
# **Cuantificación de la Familia Phi**

La cuantificación de modelos se refiere al proceso de mapear los parámetros (como pesos y valores de activación) en un modelo de red neuronal desde un rango de valores amplio (generalmente continuo) a un rango de valores finito más pequeño. Esta tecnología puede reducir el tamaño y la complejidad computacional del modelo, además de mejorar la eficiencia operativa del modelo en entornos con recursos limitados, como dispositivos móviles o sistemas embebidos. La cuantificación de modelos logra compresión al reducir la precisión de los parámetros, pero también introduce cierta pérdida de precisión. Por lo tanto, durante el proceso de cuantificación, es necesario equilibrar el tamaño del modelo, la complejidad computacional y la precisión. Los métodos de cuantificación más comunes incluyen cuantificación de punto fijo, cuantificación de punto flotante, entre otros. Puedes elegir la estrategia de cuantificación adecuada según el escenario y las necesidades específicas.

Esperamos desplegar modelos GenAI en dispositivos de borde y permitir que más dispositivos entren en escenarios GenAI, como dispositivos móviles, PC con IA/PC Copilot+ y dispositivos IoT tradicionales. A través del modelo cuantificado, podemos desplegarlo en diferentes dispositivos de borde según las características de cada dispositivo. Combinado con el marco de aceleración de modelos y los modelos cuantificados proporcionados por los fabricantes de hardware, podemos construir mejores escenarios de aplicación SLM.

En el escenario de cuantificación, tenemos diferentes niveles de precisión (INT4, INT8, FP16, FP32). A continuación, se explica cada uno de los niveles de precisión comúnmente utilizados:

### **INT4**

La cuantificación INT4 es un método radical que cuantifica los pesos y valores de activación del modelo en enteros de 4 bits. Debido al rango de representación más pequeño y la menor precisión, la cuantificación INT4 generalmente resulta en una mayor pérdida de precisión. Sin embargo, en comparación con la cuantificación INT8, INT4 puede reducir aún más los requisitos de almacenamiento y la complejidad computacional del modelo. Es importante señalar que la cuantificación INT4 es relativamente rara en aplicaciones prácticas, ya que la precisión tan baja puede causar una degradación significativa en el rendimiento del modelo. Además, no todo el hardware es compatible con operaciones INT4, por lo que se debe considerar la compatibilidad del hardware al elegir un método de cuantificación.

### **INT8**

La cuantificación INT8 es el proceso de convertir los pesos y activaciones de un modelo de números de punto flotante a enteros de 8 bits. Aunque el rango numérico representado por los enteros INT8 es más pequeño y menos preciso, puede reducir significativamente los requisitos de almacenamiento y cálculo. En la cuantificación INT8, los pesos y valores de activación del modelo pasan por un proceso de cuantificación, que incluye escalado y desplazamiento, para preservar la mayor cantidad posible de información original en punto flotante. Durante la inferencia, estos valores cuantificados se des-cuantifican de nuevo a números de punto flotante para los cálculos, y luego se vuelven a cuantificar a INT8 para el siguiente paso. Este método puede proporcionar una precisión suficiente en la mayoría de las aplicaciones mientras mantiene una alta eficiencia computacional.

### **FP16**

El formato FP16, es decir, números de punto flotante de 16 bits (float16), reduce el uso de memoria a la mitad en comparación con los números de punto flotante de 32 bits (float32), lo que ofrece ventajas significativas en aplicaciones de aprendizaje profundo a gran escala. El formato FP16 permite cargar modelos más grandes o procesar más datos dentro de las limitaciones de memoria de una GPU. A medida que el hardware moderno de GPU continúa soportando operaciones FP16, el uso del formato FP16 también puede traer mejoras en la velocidad de cálculo. Sin embargo, el formato FP16 tiene desventajas inherentes, como una menor precisión, lo que puede llevar a inestabilidad numérica o pérdida de precisión en algunos casos.

### **FP32**

El formato FP32 ofrece mayor precisión y puede representar con exactitud un rango amplio de valores. En escenarios donde se realizan operaciones matemáticas complejas o se requieren resultados de alta precisión, se prefiere el formato FP32. Sin embargo, una mayor precisión también implica un mayor uso de memoria y tiempos de cálculo más largos. Para modelos de aprendizaje profundo a gran escala, especialmente cuando hay muchos parámetros en el modelo y una gran cantidad de datos, el formato FP32 puede causar insuficiencia de memoria en la GPU o una disminución en la velocidad de inferencia.

En dispositivos móviles o dispositivos IoT, podemos convertir los modelos Phi-3.x a INT4, mientras que en PC con IA / PC Copilot se pueden usar niveles de precisión más altos, como INT8, FP16, FP32.

En la actualidad, diferentes fabricantes de hardware tienen diferentes marcos para soportar modelos generativos, como OpenVINO de Intel, QNN de Qualcomm, MLX de Apple y CUDA de Nvidia, entre otros, que se combinan con la cuantificación de modelos para completar el despliegue local.

En términos técnicos, tenemos diferentes formatos compatibles después de la cuantificación, como los formatos PyTorch / Tensorflow, GGUF y ONNX. He realizado una comparación de formatos y escenarios de aplicación entre GGUF y ONNX. Aquí recomiendo el formato de cuantificación ONNX, que tiene un buen soporte desde el marco del modelo hasta el hardware. En este capítulo, nos centraremos en ONNX Runtime para GenAI, OpenVINO y Apple MLX para realizar la cuantificación de modelos (si tienes una mejor manera, también puedes enviárnosla mediante un PR).

**Este capítulo incluye**

1. [Cuantificar Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Cuantificar Phi-3.5 / 4 usando extensiones de IA generativa para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Cuantificar Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Cuantificar Phi-3.5 / 4 usando el marco Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.