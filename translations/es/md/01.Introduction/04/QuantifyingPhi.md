<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:41:21+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "es"
}
-->
# **Cuantificación de la Familia Phi**

La cuantificación de modelos se refiere al proceso de mapear los parámetros (como pesos y valores de activación) en un modelo de red neuronal desde un rango amplio de valores (generalmente un rango continuo) a un rango finito más pequeño. Esta tecnología puede reducir el tamaño y la complejidad computacional del modelo, además de mejorar la eficiencia operativa en entornos con recursos limitados, como dispositivos móviles o sistemas embebidos. La cuantificación logra la compresión al reducir la precisión de los parámetros, pero también introduce cierta pérdida de precisión. Por ello, en el proceso de cuantificación es necesario equilibrar el tamaño del modelo, la complejidad computacional y la precisión. Los métodos comunes de cuantificación incluyen cuantificación en punto fijo, en punto flotante, entre otros. Puedes elegir la estrategia de cuantificación adecuada según el escenario y las necesidades específicas.

Nuestro objetivo es desplegar modelos GenAI en dispositivos edge y permitir que más dispositivos accedan a escenarios GenAI, como dispositivos móviles, AI PC/Copilot+PC y dispositivos IoT tradicionales. A través del modelo cuantificado, podemos desplegarlo en diferentes dispositivos edge según el tipo de dispositivo. Combinado con el framework de aceleración de modelos y el modelo cuantificado proporcionados por los fabricantes de hardware, podemos construir mejores escenarios de aplicación SLM.

En el escenario de cuantificación, contamos con diferentes precisiones (INT4, INT8, FP16, FP32). A continuación, se explica cada una de las precisiones de cuantificación más comunes.

### **INT4**

La cuantificación INT4 es un método radical que cuantifica los pesos y valores de activación del modelo en enteros de 4 bits. La cuantificación INT4 suele implicar una mayor pérdida de precisión debido al rango de representación más pequeño y la menor precisión. Sin embargo, en comparación con la cuantificación INT8, INT4 puede reducir aún más los requisitos de almacenamiento y la complejidad computacional del modelo. Cabe destacar que la cuantificación INT4 es relativamente rara en aplicaciones prácticas, ya que una precisión demasiado baja puede causar una degradación significativa en el rendimiento del modelo. Además, no todo el hardware soporta operaciones INT4, por lo que se debe considerar la compatibilidad del hardware al elegir un método de cuantificación.

### **INT8**

La cuantificación INT8 es el proceso de convertir los pesos y activaciones de un modelo de números en punto flotante a enteros de 8 bits. Aunque el rango numérico representado por enteros INT8 es menor y menos preciso, puede reducir significativamente los requisitos de almacenamiento y cálculo. En la cuantificación INT8, los pesos y valores de activación del modelo pasan por un proceso de cuantificación que incluye escalado y desplazamiento, para preservar la información original en punto flotante tanto como sea posible. Durante la inferencia, estos valores cuantificados se des-cuantifican de nuevo a números en punto flotante para el cálculo, y luego se vuelven a cuantificar a INT8 para el siguiente paso. Este método puede ofrecer una precisión suficiente en la mayoría de las aplicaciones, manteniendo una alta eficiencia computacional.

### **FP16**

El formato FP16, es decir, números en punto flotante de 16 bits (float16), reduce a la mitad el uso de memoria en comparación con los números en punto flotante de 32 bits (float32), lo que representa una ventaja significativa en aplicaciones de aprendizaje profundo a gran escala. El formato FP16 permite cargar modelos más grandes o procesar más datos dentro de las mismas limitaciones de memoria de la GPU. A medida que el hardware moderno de GPU continúa soportando operaciones FP16, el uso de este formato también puede mejorar la velocidad de cálculo. Sin embargo, el formato FP16 tiene desventajas inherentes, como una menor precisión, que puede provocar inestabilidad numérica o pérdida de precisión en algunos casos.

### **FP32**

El formato FP32 ofrece mayor precisión y puede representar con exactitud un amplio rango de valores. En escenarios donde se realizan operaciones matemáticas complejas o se requieren resultados de alta precisión, se prefiere el formato FP32. Sin embargo, una alta precisión también implica un mayor uso de memoria y tiempos de cálculo más largos. Para modelos de aprendizaje profundo a gran escala, especialmente cuando hay muchos parámetros y una gran cantidad de datos, el formato FP32 puede causar insuficiencia de memoria en la GPU o una disminución en la velocidad de inferencia.

En dispositivos móviles o IoT, podemos convertir modelos Phi-3.x a INT4, mientras que AI PC / Copilot PC pueden usar precisiones más altas como INT8, FP16 o FP32.

Actualmente, diferentes fabricantes de hardware cuentan con distintos frameworks para soportar modelos generativos, como OpenVINO de Intel, QNN de Qualcomm, MLX de Apple y CUDA de Nvidia, entre otros, combinados con la cuantificación de modelos para completar el despliegue local.

En cuanto a tecnología, contamos con diferentes formatos soportados tras la cuantificación, como PyTorch / Tensorflow, GGUF y ONNX. He realizado una comparación de formatos y escenarios de aplicación entre GGUF y ONNX. Aquí recomiendo el formato de cuantificación ONNX, que cuenta con buen soporte desde el framework del modelo hasta el hardware. En este capítulo, nos centraremos en ONNX Runtime para GenAI, OpenVINO y Apple MLX para realizar la cuantificación de modelos (si tienes un método mejor, también puedes compartirlo enviando un PR).

**Este capítulo incluye**

1. [Cuantificación de Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Cuantificación de Phi-3.5 / 4 usando extensiones de Generative AI para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Cuantificación de Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Cuantificación de Phi-3.5 / 4 usando Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.