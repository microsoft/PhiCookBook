# AGENTS.md

## Resumen del Proyecto

PhiCookBook es un repositorio completo de recetas que contiene ejemplos prácticos, tutoriales y documentación para trabajar con la familia Phi de Modelos de Lenguaje Pequeños (SLMs) de Microsoft. El repositorio demuestra diversos casos de uso, incluyendo inferencia, ajuste fino, cuantización, implementaciones RAG y aplicaciones multimodales en diferentes plataformas y marcos.

**Tecnologías Clave:**
- **Lenguajes:** Python, C#/.NET, JavaScript/Node.js
- **Marcos:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plataformas:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Tipos de Modelos:** Phi-3, Phi-3.5, Phi-4 (texto, visión, multimodal, variantes de razonamiento)

**Estructura del Repositorio:**
- `/code/` - Ejemplos de código funcional y implementaciones de muestra
- `/md/` - Documentación detallada, tutoriales y guías prácticas  
- `/translations/` - Traducciones en múltiples idiomas (más de 50 idiomas mediante flujo de trabajo automatizado)
- `/.devcontainer/` - Configuración del contenedor de desarrollo (Python 3.12 con Ollama)

## Configuración del Entorno de Desarrollo

### Usando GitHub Codespaces o Contenedores de Desarrollo (Recomendado)

1. Abrir en GitHub Codespaces (más rápido):
   - Haz clic en la insignia "Open in GitHub Codespaces" en README
   - El contenedor se configura automáticamente con Python 3.12 y Ollama con Phi-3

2. Abrir en Contenedores de Desarrollo de VS Code:
   - Usa la insignia "Open in Dev Containers" desde README
   - El contenedor requiere un mínimo de 16GB de memoria en el host

### Configuración Local

**Requisitos Previos:**
- Python 3.12 o posterior
- .NET 8.0 SDK (para ejemplos en C#)
- Node.js 18+ y npm (para ejemplos en JavaScript)
- Se recomienda un mínimo de 16GB de RAM

**Instalación:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Para ejemplos en Python:**
Navega a los directorios de ejemplos específicos e instala las dependencias:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Para ejemplos en .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Para ejemplos en JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organización del Repositorio

### Ejemplos de Código (`/code/`)

- **01.Introduce/** - Introducciones básicas y ejemplos para comenzar
- **03.Finetuning/** y **04.Finetuning/** - Ejemplos de ajuste fino con varios métodos
- **03.Inference/** - Ejemplos de inferencia en diferentes hardware (AIPC, MLX)
- **06.E2E/** - Ejemplos de aplicaciones de extremo a extremo
- **07.Lab/** - Implementaciones de laboratorio/experimentales
- **08.RAG/** - Ejemplos de Generación Aumentada por Recuperación
- **09.UpdateSamples/** - Ejemplos actualizados más recientes

### Documentación (`/md/`)

- **01.Introduction/** - Guías introductorias, configuración del entorno, guías de plataforma
- **02.Application/** - Ejemplos de aplicaciones organizados por tipo (Texto, Código, Visión, Audio, etc.)
- **02.QuickStart/** - Guías rápidas para Microsoft Foundry y GitHub Models
- **03.FineTuning/** - Documentación y tutoriales de ajuste fino
- **04.HOL/** - Laboratorios prácticos (incluye ejemplos en .NET)

### Formatos de Archivo

- **Jupyter Notebooks (`.ipynb`)** - Tutoriales interactivos en Python marcados con 📓 en README
- **Scripts de Python (`.py`)** - Ejemplos independientes en Python
- **Proyectos en C# (`.csproj`, `.sln`)** - Aplicaciones y ejemplos en .NET
- **JavaScript (`.js`, `package.json`)** - Ejemplos basados en web y Node.js
- **Markdown (`.md`)** - Documentación y guías

## Trabajando con Ejemplos

### Ejecutando Jupyter Notebooks

La mayoría de los ejemplos se proporcionan como notebooks de Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Ejecutando Scripts de Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Ejecutando Ejemplos en .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

O construye toda la solución:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Ejecutando Ejemplos en JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Pruebas

Este repositorio contiene ejemplos de código y tutoriales en lugar de un proyecto de software tradicional con pruebas unitarias. La validación generalmente se realiza mediante:

1. **Ejecutar los ejemplos** - Cada ejemplo debe ejecutarse sin errores
2. **Verificar los resultados** - Comprobar que las respuestas del modelo sean adecuadas
3. **Seguir los tutoriales** - Las guías paso a paso deben funcionar como se documenta

**Enfoque común de validación:**
- Probar la ejecución de ejemplos en el entorno objetivo
- Verificar que las dependencias se instalen correctamente
- Comprobar que los modelos se descarguen/carguen exitosamente
- Confirmar que el comportamiento esperado coincida con la documentación

## Estilo de Código y Convenciones

### Directrices Generales

- Los ejemplos deben ser claros, estar bien comentados y ser educativos
- Seguir las convenciones específicas del lenguaje (PEP 8 para Python, estándares de C# para .NET)
- Mantener los ejemplos enfocados en demostrar capacidades específicas del modelo Phi
- Incluir comentarios que expliquen conceptos clave y parámetros específicos del modelo

### Estándares de Documentación

**Formato de URLs:**
- Usar el formato `[texto](../../url)` sin espacios adicionales
- Enlaces relativos: Usar `./` para el directorio actual, `../` para el superior
- No incluir locales específicos de país en las URLs (evitar `/en-us/`, `/en/`)

**Imágenes:**
- Almacenar todas las imágenes en el directorio `/imgs/`
- Usar nombres descriptivos con caracteres en inglés, números y guiones
- Ejemplo: `phi-3-architecture.png`

**Archivos Markdown:**
- Referenciar ejemplos funcionales reales en el directorio `/code/`
- Mantener la documentación sincronizada con los cambios en el código
- Usar el emoji 📓 para marcar enlaces a notebooks de Jupyter en README

### Organización de Archivos

- Ejemplos de código en `/code/` organizados por tema/función
- Documentación en `/md/` refleja la estructura del código cuando sea aplicable
- Mantener archivos relacionados (notebooks, scripts, configuraciones) juntos en subdirectorios

## Directrices para Pull Requests

### Antes de Enviar

1. **Haz un fork del repositorio** en tu cuenta
2. **Separa los PRs por tipo:**
   - Corrección de errores en un PR
   - Actualizaciones de documentación en otro
   - Nuevos ejemplos en PRs separados
   - Correcciones de errores tipográficos pueden combinarse

3. **Resolver conflictos de fusión:**
   - Actualiza tu rama local `main` antes de realizar cambios
   - Sincroniza con el upstream frecuentemente

4. **PRs de traducción:**
   - Deben incluir traducciones para TODOS los archivos en la carpeta
   - Mantener una estructura consistente con el idioma original

### Verificaciones Requeridas

Los PRs ejecutan automáticamente flujos de trabajo de GitHub para validar:

1. **Validación de rutas relativas** - Todos los enlaces internos deben funcionar
   - Prueba los enlaces localmente: Ctrl+Click en VS Code
   - Usa sugerencias de ruta de VS Code (`./` o `../`)

2. **Verificación de locales en URLs** - Las URLs web no deben contener códigos de idioma
   - Eliminar `/en-us/`, `/en/` u otros códigos de idioma
   - Usar URLs internacionales genéricas

3. **Verificación de URLs rotas** - Todas las URLs deben devolver estado 200
   - Verifica que los enlaces sean accesibles antes de enviar
   - Nota: Algunos fallos pueden deberse a restricciones de red

### Formato del Título del PR

```
[component] Brief description
```

Ejemplos:
- `[docs] Añadir tutorial de inferencia Phi-4`
- `[code] Corregir ejemplo de integración ONNX Runtime`
- `[translation] Añadir traducción al japonés para guías introductorias`

## Patrones Comunes de Desarrollo

### Trabajando con Modelos Phi

**Carga de Modelos:**
- Los ejemplos usan varios marcos: Transformers, ONNX Runtime, MLX, OpenVINO
- Los modelos generalmente se descargan desde Hugging Face, Azure o GitHub Models
- Verifica la compatibilidad del modelo con tu hardware (CPU, GPU, NPU)

**Patrones de Inferencia:**
- Generación de texto: La mayoría de los ejemplos usan variantes de chat/instrucción
- Visión: Phi-3-vision y Phi-4-multimodal para comprensión de imágenes
- Audio: Phi-4-multimodal admite entradas de audio
- Razonamiento: Variantes de razonamiento Phi-4 para tareas avanzadas de razonamiento

### Notas Específicas de Plataforma

**Microsoft Foundry:**
- Requiere suscripción a Azure y claves API
- Ver `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Nivel gratuito disponible para pruebas
- Ver `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferencia Local:**
- ONNX Runtime: Inferencia optimizada y multiplataforma
- Ollama: Gestión fácil de modelos locales (preconfigurado en contenedor de desarrollo)
- Apple MLX: Optimizado para Apple Silicon

## Solución de Problemas

### Problemas Comunes

**Problemas de Memoria:**
- Los modelos Phi requieren una cantidad significativa de RAM (especialmente variantes de visión/multimodal)
- Usa modelos cuantificados para entornos con recursos limitados
- Ver `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflictos de Dependencias:**
- Los ejemplos en Python pueden tener requisitos específicos de versión
- Usa entornos virtuales para cada ejemplo
- Revisa los archivos `requirements.txt` individuales

**Fallos en Descarga de Modelos:**
- Los modelos grandes pueden agotarse en conexiones lentas
- Considera usar entornos en la nube (Codespaces, Azure)
- Revisa la caché de Hugging Face: `~/.cache/huggingface/`

**Problemas en Proyectos .NET:**
- Asegúrate de tener instalado .NET 8.0 SDK
- Usa `dotnet restore` antes de construir
- Algunos proyectos tienen configuraciones específicas de CUDA (Debug_Cuda)

**Ejemplos en JavaScript/Web:**
- Usa Node.js 18+ para compatibilidad
- Limpia `node_modules` y reinstala si persisten los problemas
- Revisa la consola del navegador para problemas de compatibilidad con WebGPU

### Obtener Ayuda

- **Discord:** Únete a la comunidad de Microsoft Foundry en Discord
- **GitHub Issues:** Reporta errores y problemas en el repositorio
- **GitHub Discussions:** Haz preguntas y comparte conocimientos

## Contexto Adicional

### IA Responsable

Todo uso de modelos Phi debe seguir los principios de IA Responsable de Microsoft:
- Justicia, confiabilidad, seguridad
- Privacidad y seguridad  
- Inclusión, transparencia, responsabilidad
- Usa Azure AI Content Safety para aplicaciones en producción
- Ver `/md/01.Introduction/01/01.AISafety.md`

### Traducciones

- Más de 50 idiomas soportados mediante acción automatizada de GitHub
- Traducciones en el directorio `/translations/`
- Mantenido por el flujo de trabajo co-op-translator
- No edites manualmente los archivos traducidos (generados automáticamente)

### Contribuciones

- Sigue las directrices en `CONTRIBUTING.md`
- Acepta el Acuerdo de Licencia de Contribuidor (CLA)
- Adhiérete al Código de Conducta de Código Abierto de Microsoft
- Mantén la seguridad y las credenciales fuera de los commits

### Soporte Multilingüe

Este es un repositorio políglota con ejemplos en:
- **Python** - Flujos de trabajo de ML/IA, notebooks de Jupyter, ajuste fino
- **C#/.NET** - Aplicaciones empresariales, integración con ONNX Runtime
- **JavaScript** - IA basada en web, inferencia en navegador con WebGPU

Elige el lenguaje que mejor se adapte a tu caso de uso y objetivo de implementación.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.