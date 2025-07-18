<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:12:06+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "es"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo para mostrar WebGPU y el patrón RAG  
El patrón RAG con el modelo Phi-3 Onnx alojado aprovecha el enfoque de Generación Aumentada por Recuperación, combinando la potencia de los modelos Phi-3 con el alojamiento ONNX para implementaciones de IA eficientes. Este patrón es fundamental para ajustar modelos en tareas específicas de dominio, ofreciendo una combinación de calidad, rentabilidad y comprensión de contextos largos. Forma parte de la suite de Azure AI, que proporciona una amplia selección de modelos fáciles de encontrar, probar y usar, adaptándose a las necesidades de personalización de diversas industrias. Los modelos Phi-3, incluyendo Phi-3-mini, Phi-3-small y Phi-3-medium, están disponibles en el Catálogo de Modelos de Azure AI y pueden ser ajustados y desplegados de forma autogestionada o a través de plataformas como HuggingFace y ONNX, demostrando el compromiso de Microsoft con soluciones de IA accesibles y eficientes.

## Qué es WebGPU  
WebGPU es una API moderna de gráficos web diseñada para proporcionar acceso eficiente a la unidad de procesamiento gráfico (GPU) de un dispositivo directamente desde los navegadores web. Está pensada para ser la sucesora de WebGL, ofreciendo varias mejoras clave:

1. **Compatibilidad con GPUs modernas**: WebGPU está diseñada para funcionar sin problemas con arquitecturas GPU contemporáneas, aprovechando APIs del sistema como Vulkan, Metal y Direct3D 12.  
2. **Rendimiento mejorado**: Soporta cálculos generales en GPU y operaciones más rápidas, haciéndola adecuada tanto para renderizado gráfico como para tareas de aprendizaje automático.  
3. **Funciones avanzadas**: WebGPU ofrece acceso a capacidades GPU más avanzadas, permitiendo cargas de trabajo gráficas y computacionales más complejas y dinámicas.  
4. **Reducción de la carga en JavaScript**: Al delegar más tareas a la GPU, WebGPU reduce significativamente la carga de trabajo en JavaScript, lo que se traduce en mejor rendimiento y experiencias más fluidas.

Actualmente, WebGPU es compatible con navegadores como Google Chrome, y se está trabajando para ampliar su soporte a otras plataformas.

### 03.WebGPU  
Entorno requerido:

**Navegadores compatibles:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Cómo habilitar WebGPU:

- En Chrome/Microsoft Edge  

Activa la bandera `chrome://flags/#enable-unsafe-webgpu`.

#### Abre tu navegador:  
Inicia Google Chrome o Microsoft Edge.

#### Accede a la página de Flags:  
En la barra de direcciones, escribe `chrome://flags` y presiona Enter.

#### Busca la bandera:  
En el cuadro de búsqueda en la parte superior, escribe 'enable-unsafe-webgpu'.

#### Habilita la bandera:  
Encuentra la bandera #enable-unsafe-webgpu en la lista de resultados.  

Haz clic en el menú desplegable junto a ella y selecciona Enabled.

#### Reinicia tu navegador:  

Después de habilitar la bandera, deberás reiniciar el navegador para que los cambios tengan efecto. Haz clic en el botón Relaunch que aparece en la parte inferior de la página.

- En Linux, inicia el navegador con `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) tiene WebGPU habilitado por defecto.  
- En Firefox Nightly, ingresa about:config en la barra de direcciones y configura `dom.webgpu.enabled` en true.

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

### Abre tu Codespace:  
Navega a tu repositorio en GitHub.  
Haz clic en el botón Code y selecciona Open with Codespaces.

Si aún no tienes un Codespace, puedes crear uno haciendo clic en New codespace.

**Nota** Instalación del entorno Node en tu codespace  
Ejecutar una demo npm desde un GitHub Codespace es una excelente forma de probar y desarrollar tu proyecto. Aquí tienes una guía paso a paso para comenzar:

### Configura tu entorno:  
Una vez abierto tu Codespace, asegúrate de tener Node.js y npm instalados. Puedes verificarlo ejecutando:  
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

### Navega a tu directorio de proyecto:  
Usa la terminal para ir al directorio donde se encuentra tu proyecto npm:  
```
cd path/to/your/project
```

### Instala las dependencias:  
Ejecuta el siguiente comando para instalar todas las dependencias necesarias listadas en tu archivo package.json:  

```
npm install
```

### Ejecuta la demo:  
Una vez instaladas las dependencias, puedes ejecutar el script de demo. Esto generalmente se especifica en la sección scripts de tu package.json. Por ejemplo, si tu script de demo se llama start, puedes ejecutar:  

```
npm run build
```  
```
npm run dev
```

### Accede a la demo:  
Si tu demo involucra un servidor web, Codespaces proporcionará una URL para acceder a él. Busca una notificación o revisa la pestaña de Puertos para encontrar la URL.

**Nota:** El modelo necesita estar en caché en el navegador, por lo que puede tardar un poco en cargarse.

### Demo RAG  
Sube el archivo markdown `intro_rag.md` para completar la solución RAG. Si usas codespaces, puedes descargar el archivo ubicado en `01.InferencePhi3/docs/`

### Selecciona tu archivo:  
Haz clic en el botón que dice “Choose File” para seleccionar el documento que quieres subir.

### Sube el documento:  
Después de seleccionar tu archivo, haz clic en el botón “Upload” para cargar tu documento para RAG (Generación Aumentada por Recuperación).

### Inicia tu chat:  
Una vez que el documento esté cargado, puedes iniciar una sesión de chat usando RAG basada en el contenido de tu documento.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.