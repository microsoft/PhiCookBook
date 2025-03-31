<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-03-27T11:16:22+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\WebGPUWithPhi35Readme.md",
  "language_code": "es"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demostración para mostrar WebGPU y el patrón RAG

El patrón RAG con el modelo Phi-3.5 Onnx Hosted utiliza el enfoque de Generación Aumentada por Recuperación, combinando el poder de los modelos Phi-3.5 con el hosting ONNX para despliegues eficientes de IA. Este patrón es fundamental para ajustar modelos a tareas específicas de dominio, ofreciendo una combinación de calidad, rentabilidad y comprensión de contexto largo. Forma parte de la suite de Azure AI, que proporciona una amplia selección de modelos fáciles de encontrar, probar y usar, adaptándose a las necesidades de personalización de diversas industrias.

## ¿Qué es WebGPU? 
WebGPU es una API moderna de gráficos web diseñada para proporcionar acceso eficiente a la unidad de procesamiento gráfico (GPU) de un dispositivo directamente desde los navegadores web. Está destinada a ser el sucesor de WebGL, ofreciendo varias mejoras clave:

1. **Compatibilidad con GPUs modernas**: WebGPU está diseñado para funcionar sin problemas con arquitecturas de GPU contemporáneas, aprovechando APIs del sistema como Vulkan, Metal y Direct3D 12.
2. **Rendimiento mejorado**: Soporta cálculos generales en GPU y operaciones más rápidas, lo que lo hace adecuado tanto para renderizado gráfico como para tareas de aprendizaje automático.
3. **Características avanzadas**: WebGPU proporciona acceso a capacidades más avanzadas de GPU, permitiendo cargas de trabajo gráficas y computacionales más complejas y dinámicas.
4. **Reducción de la carga de JavaScript**: Al delegar más tareas a la GPU, WebGPU reduce significativamente la carga en JavaScript, mejorando el rendimiento y proporcionando experiencias más fluidas.

Actualmente, WebGPU es compatible con navegadores como Google Chrome, y se está trabajando para expandir el soporte a otras plataformas.

### 03.WebGPU
Entorno requerido:

**Navegadores compatibles:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Habilitar WebGPU:

- En Chrome/Microsoft Edge 

Habilitar la opción `chrome://flags/#enable-unsafe-webgpu`.

#### Abre tu navegador:
Lanza Google Chrome o Microsoft Edge.

#### Accede a la página de Flags:
En la barra de direcciones, escribe `chrome://flags` y presiona Enter.

#### Busca el Flag:
En el cuadro de búsqueda en la parte superior de la página, escribe 'enable-unsafe-webgpu'.

#### Habilita el Flag:
Encuentra el flag #enable-unsafe-webgpu en la lista de resultados.

Haz clic en el menú desplegable junto a él y selecciona Enabled.

#### Reinicia tu navegador:

Después de habilitar el flag, necesitarás reiniciar tu navegador para que los cambios surtan efecto. Haz clic en el botón Relaunch que aparece en la parte inferior de la página.

- Para Linux, lanza el navegador con `--enable-features=Vulkan`.
- Safari 18 (macOS 15) tiene WebGPU habilitado por defecto.
- En Firefox Nightly, ingresa about:config en la barra de direcciones y `set dom.webgpu.enabled to true`.

### Configuración de GPU para Microsoft Edge 

Aquí están los pasos para configurar una GPU de alto rendimiento para Microsoft Edge en Windows:

- **Abrir Configuración:** Haz clic en el menú Inicio y selecciona Configuración.
- **Configuración del sistema:** Ve a Sistema y luego a Pantalla.
- **Configuración de gráficos:** Desplázate hacia abajo y haz clic en Configuración de gráficos.
- **Elegir aplicación:** En “Elige una aplicación para establecer preferencias,” selecciona Aplicación de escritorio y luego Examinar.
- **Seleccionar Edge:** Navega a la carpeta de instalación de Edge (generalmente `C:\Program Files (x86)\Microsoft\Edge\Application`) y selecciona `msedge.exe`.
- **Establecer preferencia:** Haz clic en Opciones, elige Alto rendimiento y luego haz clic en Guardar.
Esto asegurará que Microsoft Edge utilice tu GPU de alto rendimiento para un mejor rendimiento. 
- **Reinicia** tu máquina para que estos ajustes surtan efecto.

### Ejemplos: Por favor [haz clic en este enlace](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por un humano. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.