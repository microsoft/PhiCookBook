<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-03-27T04:47:55+00:00",
  "source_file": "code\\08.RAG\\rag_webgpu_chat\\README.md",
  "language_code": "es"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demostración para mostrar WebGPU y el Patrón RAG
El Patrón RAG con el modelo Phi-3 Onnx Hosted aprovecha el enfoque de Generación Aumentada por Recuperación, combinando el poder de los modelos Phi-3 con el hosting de ONNX para implementaciones de IA eficientes. Este patrón es fundamental para ajustar modelos a tareas específicas de dominio, ofreciendo una mezcla de calidad, rentabilidad y comprensión de contextos largos. Es parte del conjunto de Azure AI, que proporciona una amplia selección de modelos fáciles de encontrar, probar y usar, adaptándose a las necesidades de personalización de diversas industrias. Los modelos Phi-3, incluyendo Phi-3-mini, Phi-3-small y Phi-3-medium, están disponibles en el Catálogo de Modelos de Azure AI y pueden ajustarse y desplegarse de forma autogestionada o a través de plataformas como HuggingFace y ONNX, mostrando el compromiso de Microsoft con soluciones de IA accesibles y eficientes.

## ¿Qué es WebGPU?
WebGPU es una API moderna de gráficos web diseñada para proporcionar acceso eficiente a la unidad de procesamiento gráfico (GPU) de un dispositivo directamente desde los navegadores web. Está destinada a ser la sucesora de WebGL, ofreciendo varias mejoras clave:

1. **Compatibilidad con GPUs Modernas**: WebGPU está diseñada para funcionar sin problemas con arquitecturas de GPU contemporáneas, aprovechando APIs del sistema como Vulkan, Metal y Direct3D 12.
2. **Rendimiento Mejorado**: Soporta cálculos generales en GPU y operaciones más rápidas, lo que la hace adecuada tanto para renderización gráfica como para tareas de aprendizaje automático.
3. **Características Avanzadas**: WebGPU proporciona acceso a capacidades más avanzadas de GPU, permitiendo cargas de trabajo gráficas y computacionales más complejas y dinámicas.
4. **Reducción de la Carga de JavaScript**: Al delegar más tareas a la GPU, WebGPU reduce significativamente la carga en JavaScript, mejorando el rendimiento y ofreciendo experiencias más fluidas.

Actualmente, WebGPU es compatible con navegadores como Google Chrome, y se está trabajando para expandir su soporte a otras plataformas.

### 03.WebGPU
Entorno Requerido:

**Navegadores compatibles:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Habilitar WebGPU:

- En Chrome/Microsoft Edge 

Habilita el flag `chrome://flags/#enable-unsafe-webgpu`.

#### Abre tu Navegador:
Inicia Google Chrome o Microsoft Edge.

#### Accede a la Página de Flags:
En la barra de direcciones, escribe `chrome://flags` y presiona Enter.

#### Busca el Flag:
En el cuadro de búsqueda en la parte superior de la página, escribe 'enable-unsafe-webgpu'.

#### Habilita el Flag:
Encuentra el flag #enable-unsafe-webgpu en la lista de resultados.

Haz clic en el menú desplegable junto a él y selecciona Enabled.

#### Reinicia tu Navegador:

Después de habilitar el flag, necesitarás reiniciar tu navegador para que los cambios surtan efecto. Haz clic en el botón Relaunch que aparece en la parte inferior de la página.

- Para Linux, inicia el navegador con `--enable-features=Vulkan`.
- Safari 18 (macOS 15) tiene WebGPU habilitado de forma predeterminada.
- En Firefox Nightly, ingresa about:config en la barra de direcciones y `set dom.webgpu.enabled to true`.

### Configuración de GPU para Microsoft Edge 

Aquí están los pasos para configurar una GPU de alto rendimiento para Microsoft Edge en Windows:

- **Abrir Configuración:** Haz clic en el menú de Inicio y selecciona Configuración.
- **Configuración del Sistema:** Ve a Sistema y luego a Pantalla.
- **Configuración de Gráficos:** Desplázate hacia abajo y haz clic en Configuración de gráficos.
- **Elegir Aplicación:** En “Elegir una aplicación para establecer preferencia”, selecciona Aplicación de escritorio y luego Examinar.
- **Seleccionar Edge:** Navega a la carpeta de instalación de Edge (generalmente `C:\Program Files (x86)\Microsoft\Edge\Application`) y selecciona `msedge.exe`.
- **Establecer Preferencia:** Haz clic en Opciones, elige Alto rendimiento y luego haz clic en Guardar.
Esto garantizará que Microsoft Edge use tu GPU de alto rendimiento para un mejor rendimiento. 
- **Reinicia** tu máquina para que estos ajustes surtan efecto.

### Abre tu Codespace:
Navega a tu repositorio en GitHub.
Haz clic en el botón Code y selecciona Open with Codespaces.

Si aún no tienes un Codespace, puedes crear uno haciendo clic en New codespace.

**Nota:** Instalación del entorno Node en tu Codespace
Ejecutar un demo npm desde un Codespace de GitHub es una excelente manera de probar y desarrollar tu proyecto. Aquí tienes una guía paso a paso para comenzar:

### Configura tu Entorno:
Una vez que tu Codespace esté abierto, asegúrate de que tienes Node.js y npm instalados. Puedes verificarlo ejecutando:
```
node -v
```
```
npm -v
```

Si no están instalados, puedes instalarlos usando:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navega a tu Directorio de Proyecto:
Usa la terminal para navegar al directorio donde se encuentra tu proyecto npm:
```
cd path/to/your/project
```

### Instala las Dependencias:
Ejecuta el siguiente comando para instalar todas las dependencias necesarias listadas en tu archivo package.json:

```
npm install
```

### Ejecuta el Demo:
Una vez instaladas las dependencias, puedes ejecutar tu script demo. Esto generalmente se especifica en la sección de scripts de tu package.json. Por ejemplo, si tu script demo se llama start, puedes ejecutar:

```
npm run build
```
```
npm run dev
```

### Accede al Demo:
Si tu demo involucra un servidor web, Codespaces proporcionará una URL para acceder a él. Busca una notificación o revisa la pestaña Ports para encontrar la URL.

**Nota:** El modelo necesita ser almacenado en caché en el navegador, por lo que puede tardar un tiempo en cargarse.

### Demo RAG
Sube el archivo markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Selecciona tu Archivo:
Haz clic en el botón que dice “Choose File” para elegir el documento que deseas subir.

### Sube el Documento:
Después de seleccionar tu archivo, haz clic en el botón “Upload” para cargar tu documento para RAG (Generación Aumentada por Recuperación).

### Inicia tu Chat:
Una vez que el documento esté cargado, puedes iniciar una sesión de chat utilizando RAG basado en el contenido de tu documento.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.