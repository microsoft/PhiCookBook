<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-07T11:00:20+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "es"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo para mostrar WebGPU y el patrón RAG

El patrón RAG con el modelo Phi-3.5 Onnx Hosted aprovecha el enfoque de Generación Aumentada por Recuperación, combinando la potencia de los modelos Phi-3.5 con el hosting ONNX para implementaciones de IA eficientes. Este patrón es fundamental para ajustar modelos en tareas específicas de dominio, ofreciendo una mezcla de calidad, rentabilidad y comprensión de contextos extensos. Forma parte de la suite de Azure AI, que proporciona una amplia selección de modelos fáciles de encontrar, probar y usar, adaptándose a las necesidades de personalización de diversas industrias.

## ¿Qué es WebGPU?  
WebGPU es una API moderna de gráficos web diseñada para proporcionar acceso eficiente a la unidad de procesamiento gráfico (GPU) de un dispositivo directamente desde los navegadores web. Está destinada a ser la sucesora de WebGL, ofreciendo varias mejoras clave:

1. **Compatibilidad con GPUs modernas**: WebGPU está diseñado para funcionar sin problemas con arquitecturas de GPU contemporáneas, aprovechando APIs del sistema como Vulkan, Metal y Direct3D 12.
2. **Rendimiento mejorado**: Soporta cálculos generales en GPU y operaciones más rápidas, siendo adecuado tanto para renderizado gráfico como para tareas de aprendizaje automático.
3. **Funciones avanzadas**: WebGPU ofrece acceso a capacidades GPU más avanzadas, permitiendo cargas de trabajo gráficas y computacionales más complejas y dinámicas.
4. **Reducción de la carga en JavaScript**: Al descargar más tareas a la GPU, WebGPU reduce significativamente la carga en JavaScript, lo que se traduce en un mejor rendimiento y experiencias más fluidas.

Actualmente, WebGPU es compatible con navegadores como Google Chrome, y se está trabajando para ampliar el soporte a otras plataformas.

### 03.WebGPU  
Entorno requerido:

**Navegadores compatibles:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Habilitar WebGPU:

- En Chrome/Microsoft Edge  

Habilita la bandera `chrome://flags/#enable-unsafe-webgpu`.

#### Abre tu navegador:  
Inicia Google Chrome o Microsoft Edge.

#### Accede a la página de banderas:  
En la barra de direcciones, escribe `chrome://flags` y presiona Enter.

#### Busca la bandera:  
En el cuadro de búsqueda en la parte superior de la página, escribe 'enable-unsafe-webgpu'.

#### Habilita la bandera:  
Encuentra la bandera #enable-unsafe-webgpu en la lista de resultados.

Haz clic en el menú desplegable junto a ella y selecciona Enabled.

#### Reinicia tu navegador:  

Después de habilitar la bandera, deberás reiniciar tu navegador para que los cambios surtan efecto. Haz clic en el botón Relaunch que aparece en la parte inferior de la página.

- En Linux, inicia el navegador con `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) tiene WebGPU habilitado por defecto.  
- En Firefox Nightly, ingresa about:config en la barra de direcciones y `set dom.webgpu.enabled to true`.

### Configurar GPU para Microsoft Edge  

Aquí están los pasos para configurar una GPU de alto rendimiento para Microsoft Edge en Windows:

- **Abrir Configuración:** Haz clic en el menú Inicio y selecciona Configuración.  
- **Configuración del sistema:** Ve a Sistema y luego a Pantalla.  
- **Configuración de gráficos:** Desplázate hacia abajo y haz clic en Configuración de gráficos.  
- **Elegir aplicación:** Bajo “Elegir una aplicación para establecer preferencia,” selecciona Aplicación de escritorio y luego Examinar.  
- **Seleccionar Edge:** Navega a la carpeta de instalación de Edge (usualmente `C:\Program Files (x86)\Microsoft\Edge\Application`) y selecciona `msedge.exe`.  
- **Establecer preferencia:** Haz clic en Opciones, elige Alto rendimiento y luego haz clic en Guardar.  
Esto asegurará que Microsoft Edge use tu GPU de alto rendimiento para un mejor desempeño.  
- **Reinicia** tu equipo para que estos ajustes tengan efecto.

### Ejemplos : Por favor [haz clic en este enlace](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.