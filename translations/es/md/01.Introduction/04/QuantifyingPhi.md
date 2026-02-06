# **Cuantificación de la Familia Phi**

La cuantificación de modelos se refiere al proceso de mapear los parámetros (como pesos y valores de activación) en un modelo de red neuronal desde un rango de valores grande (generalmente un rango continuo) a un rango finito más pequeño. Esta tecnología puede reducir el tamaño y la complejidad computacional del modelo y mejorar la eficiencia operativa del modelo en entornos con recursos limitados como dispositivos móviles o sistemas embebidos. La cuantificación de modelos logra compresión al reducir la precisión de los parámetros, pero también introduce una cierta pérdida de precisión. Por lo tanto, en el proceso de cuantificación es necesario equilibrar el tamaño del modelo, la complejidad computacional y la precisión. Los métodos comunes de cuantificación incluyen cuantificación de punto fijo, cuantificación de punto flotante, etc. Puedes elegir la estrategia de cuantificación adecuada según el escenario específico y las necesidades.

Esperamos desplegar modelos GenAI en dispositivos edge y permitir que más dispositivos entren en escenarios GenAI, como dispositivos móviles, PC AI/Copilot+PC y dispositivos IoT tradicionales. A través del modelo cuantificado, podemos desplegarlo en diferentes dispositivos edge según el dispositivo. Combinado con el marco de aceleración del modelo y el modelo de cuantificación proporcionado por los fabricantes de hardware, podemos construir mejores escenarios de aplicación SLM.

En el escenario de cuantificación, tenemos diferentes precisiones (INT4, INT8, FP16, FP32). A continuación se muestra una explicación de las precisiones de cuantificación comúnmente usadas.

### **INT4**

La cuantificación INT4 es un método de cuantificación radical que cuantifica los pesos y valores de activación del modelo a enteros de 4 bits. La cuantificación INT4 usualmente genera una mayor pérdida de precisión debido al rango de representación más pequeño y menor precisión. Sin embargo, en comparación con la cuantificación INT8, la cuantificación INT4 puede reducir aún más los requisitos de almacenamiento y la complejidad computacional del modelo. Cabe destacar que la cuantificación INT4 es relativamente rara en aplicaciones prácticas, porque una precisión demasiado baja puede causar una degradación significativa en el rendimiento del modelo. Además, no todo el hardware soporta operaciones INT4, por lo que la compatibilidad hardware debe considerarse al elegir un método de cuantificación.

### **INT8**

La cuantificación INT8 es el proceso de convertir los pesos y activaciones de un modelo desde números de punto flotante a enteros de 8 bits. Aunque el rango numérico representado por enteros INT8 es menor y menos preciso, puede reducir significativamente los requerimientos de almacenamiento y cálculo. En la cuantificación INT8, los pesos y valores de activación del modelo pasan por un proceso de cuantificación que incluye escalado y desplazamiento para preservar la información original en punto flotante tanto como sea posible. Durante la inferencia, estos valores cuantificados se descuantifican de nuevo a números en punto flotante para el cálculo, y luego se vuelven a cuantificar a INT8 para el siguiente paso. Este método puede proporcionar suficiente precisión en la mayoría de las aplicaciones mientras mantiene alta eficiencia computacional.

### **FP16**

El formato FP16, es decir, números de punto flotante de 16 bits (float16), reduce a la mitad el uso de memoria en comparación con números de punto flotante de 32 bits (float32), lo que tiene ventajas significativas en aplicaciones de aprendizaje profundo a gran escala. El formato FP16 permite cargar modelos más grandes o procesar más datos dentro de las mismas limitaciones de memoria GPU. A medida que el hardware GPU moderno sigue soportando operaciones FP16, usar el formato FP16 también puede traer mejoras en la velocidad de cálculo. Sin embargo, el formato FP16 también tiene desventajas inherentes, como menor precisión, lo que puede llevar a inestabilidad numérica o pérdida de precisión en algunos casos.

### **FP32**

El formato FP32 ofrece mayor precisión y puede representar con exactitud un amplio rango de valores. En escenarios donde se realizan operaciones matemáticas complejas o se requieren resultados de alta precisión, se prefiere el formato FP32. Sin embargo, mayor precisión también significa mayor uso de memoria y mayor tiempo de cálculo. Para modelos de aprendizaje profundo a gran escala, especialmente cuando hay muchos parámetros de modelo y una enorme cantidad de datos, el formato FP32 puede provocar falta de memoria en la GPU o una disminución en la velocidad de inferencia.

En dispositivos móviles o dispositivos IoT, podemos convertir modelos Phi-3.x a INT4, mientras que PC AI / Copilot PC pueden usar precisiones mayores como INT8, FP16, FP32.

Actualmente, diferentes fabricantes de hardware tienen diferentes marcos para soportar modelos generativos, tales como OpenVINO de Intel, QNN de Qualcomm, MLX de Apple y CUDA de Nvidia, etc., combinados con cuantificación de modelos para completar el despliegue local.

En cuanto a tecnología, tenemos diferentes soportes de formato después de la cuantificación, tales como formato PyTorch / TensorFlow, GGUF y ONNX. He realizado una comparación de formatos y escenarios de aplicación entre GGUF y ONNX. Aquí recomiendo el formato de cuantificación ONNX, que tiene buen soporte desde el marco del modelo hasta el hardware. En este capítulo, nos centraremos en ONNX Runtime para GenAI, OpenVINO y Apple MLX para realizar la cuantificación de modelos (si tienes una mejor manera, también puedes aportarla mediante un PR).

**Este capítulo incluye**

1. [Cuantificación de Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Cuantificación de Phi-3.5 / 4 usando extensiones de IA Generativa para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Cuantificación de Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Cuantificación de Phi-3.5 / 4 usando el marco Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos responsabilizamos por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->