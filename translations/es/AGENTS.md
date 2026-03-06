# AGENTS.md

## Descripción del Proyecto

PhiCookBook es un repositorio completo de libros de cocina que contiene ejemplos prácticos, tutoriales y documentación para trabajar con la familia Phi de Modelos de Lenguaje Pequeños (SLMs) de Microsoft. El repositorio demuestra varios casos de uso incluyendo inferencia, ajuste fino, cuantización, implementaciones RAG y aplicaciones multimodales en diferentes plataformas y marcos.

**Tecnologías Clave:**
- **Lenguajes:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plataformas:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Tipos de Modelos:** Phi-3, Phi-3.5, Phi-4 (variantes de texto, visión, multimodal, razonamiento)

**Estructura del Repositorio:**
- `/code/` - Ejemplos de código funcional y implementaciones de muestra
- `/md/` - Documentación detallada, tutoriales y guías prácticas  
- `/translations/` - Traducciones multilingües (más de 50 idiomas mediante flujo de trabajo automatizado)
- `/.devcontainer/` - Configuración del contenedor de desarrollo (Python 3.12 con Ollama)

## Configuración del Entorno de Desarrollo

### Uso de GitHub Codespaces o Contenedores de Desarrollo (Recomendado)

1. Abrir en GitHub Codespaces (más rápido):
   - Haz clic en la insignia "Open in GitHub Codespaces" en el README
   - El contenedor se configura automáticamente con Python 3.12 y Ollama con Phi-3

2. Abrir en Contenedores de Desarrollo de VS Code:
   - Usa la insignia "Open in Dev Containers" del README
   - El contenedor requiere mínimo 16GB de memoria en el host

### Configuración Local

**Requisitos Previos:**
- Python 3.12 o posterior
- SDK .NET 8.0 (para ejemplos en C#)
- Node.js 18+ y npm (para ejemplos en JavaScript)
- Se recomiendan al menos 16GB de RAM

**Instalación:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Para Ejemplos en Python:**
Navega a los directorios de ejemplos específicos e instala las dependencias:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # si requirements.txt existe
```

**Para Ejemplos en .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Para Ejemplos en JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Iniciar el servidor de desarrollo
npm run build  # Construir para producción
```

## Organización del Repositorio

### Ejemplos de Código (`/code/`)

- **01.Introduce/** - Introducciones básicas y muestras para comenzar
- **03.Finetuning/** y **04.Finetuning/** - Ejemplos de ajuste fino con varios métodos
- **03.Inference/** - Ejemplos de inferencia en diferentes hardware (AIPC, MLX)
- **06.E2E/** - Muestras de aplicaciones de extremo a extremo
- **07.Lab/** - Implementaciones de laboratorio/experimentales
- **08.RAG/** - Muestras de Generación Aumentada por Recuperación
- **09.UpdateSamples/** - Muestras actualizadas más recientes

### Documentación (`/md/`)

- **01.Introduction/** - Guías introductorias, configuración del entorno, guías de plataforma
- **02.Application/** - Ejemplos de aplicaciones organizados por tipo (Texto, Código, Visión, Audio, etc.)
- **02.QuickStart/** - Guías rápidas para Microsoft Foundry y GitHub Models
- **03.FineTuning/** - Documentación y tutoriales de ajuste fino
- **04.HOL/** - Laboratorios prácticos (incluye ejemplos en .NET)

### Formatos de Archivo

- **Jupyter Notebooks (`.ipynb`)** - Tutoriales interactivos en Python marcados con 📓 en el README
- **Scripts de Python (`.py`)** - Ejemplos de Python independientes
- **Proyectos en C# (`.csproj`, `.sln`)** - Aplicaciones y muestras en .NET
- **JavaScript (`.js`, `package.json`)** - Ejemplos para web y Node.js
- **Markdown (`.md`)** - Documentación y guías

## Trabajo con Ejemplos

### Ejecución de Jupyter Notebooks

La mayoría de los ejemplos se proporcionan como notebooks Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Abre la interfaz del navegador
# Navega al archivo .ipynb deseado
```

### Ejecución de Scripts en Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Ejecución de Ejemplos en .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

O construye la solución completa:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Ejecución de Ejemplos en JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Desarrollo con recarga en caliente
```

## Pruebas

Este repositorio contiene código de ejemplo y tutoriales en lugar de un proyecto de software tradicional con pruebas unitarias. La validación se realiza típicamente mediante:

1. **Ejecución de los ejemplos** - Cada ejemplo debe ejecutarse sin errores
2. **Verificación de salidas** - Comprobar que las respuestas del modelo sean apropiadas
3. **Seguimiento de tutoriales** - Las guías paso a paso deben funcionar según lo documentado

**Enfoque común de validación:**
- Probar la ejecución del ejemplo en el entorno objetivo
- Verificar que las dependencias se instalen correctamente
- Comprobar que los modelos se descarguen/carguen exitosamente
- Confirmar que el comportamiento esperado coincida con la documentación

## Estilo y Convenciones de Código

### Guías Generales

- Los ejemplos deben ser claros, bien comentados y educativos
- Seguir convenciones específicas del lenguaje (PEP 8 para Python, estándares C# para .NET)
- Mantener los ejemplos enfocados en demostrar capacidades específicas de los modelos Phi
- Incluir comentarios que expliquen conceptos clave y parámetros específicos del modelo

### Estándares de Documentación

**Formato de URL:**
- Usar formato `[text](../../url)` sin espacios adicionales
- Enlaces relativos: usar `./` para directorio actual, `../` para el padre
- No usar locales específicos de país en URLs (evitar `/en-us/`, `/en/`)

**Imágenes:**
- Almacenar todas las imágenes en el directorio `/imgs/`
- Usar nombres descriptivos con caracteres en inglés, números y guiones
- Ejemplo: `phi-3-architecture.png`

**Archivos Markdown:**
- Referenciar ejemplos funcionales reales en el directorio `/code/`
- Mantener la documentación sincronizada con los cambios en el código
- Usar el emoji 📓 para marcar enlaces a notebooks Jupyter en el README

### Organización de Archivos

- Los ejemplos de código en `/code/` están organizados por tema/característica
- La documentación en `/md/` refleja la estructura de código cuando aplica
- Mantener archivos relacionados (notebooks, scripts, configuraciones) juntos en subdirectorios

## Directrices para Pull Requests

### Antes de Enviar

1. **Haz fork del repositorio** a tu cuenta
2. **Separar PRs por tipo:**
   - Correcciones de errores en un PR
   - Actualizaciones de documentación en otro
   - Nuevos ejemplos en PRs separados
   - Correcciones tipográficas pueden combinarse

3. **Resolver conflictos de fusión:**
   - Actualiza tu rama `main` local antes de hacer cambios
   - Sincroniza frecuentemente con upstream

4. **PRs de traducción:**
   - Deben incluir traducciones para TODOS los archivos en la carpeta
   - Mantener estructura consistente con el idioma original

### Verificaciones Requeridas

Los PRs ejecutan automáticamente flujos de trabajo de GitHub para validar:

1. **Validación de rutas relativas** - Todos los enlaces internos deben funcionar
   - Prueba los enlaces localmente: Ctrl+Click en VS Code
   - Usa sugerencias de ruta de VS Code (`./` o `../`)

2. **Chequeo de localización en URLs** - Las URLs web no deben contener locales de país
   - Elimina `/en-us/`, `/en/` u otros códigos de idioma
   - Usa URLs internacionales genéricas

3. **Chequeo de URLs rotas** - Todas las URLs deben devolver estado 200
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

### Trabajo con Modelos Phi

**Carga del Modelo:**
- Los ejemplos usan varios frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Los modelos suelen descargarse desde Hugging Face, Azure o GitHub Models
- Verifica compatibilidad del modelo con tu hardware (CPU, GPU, NPU)

**Patrones de Inferencia:**
- Generación de texto: la mayoría usa variantes chat/instruction
- Visión: Phi-3-vision y Phi-4-multimodal para comprensión de imágenes
- Audio: Phi-4-multimodal soporta entradas de audio
- Razonamiento: variantes Phi-4-reasoning para tareas avanzadas de razonamiento

### Notas Específicas de Plataforma

**Microsoft Foundry:**
- Requiere suscripción Azure y claves API
- Ver `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Nivel gratuito disponible para pruebas
- Ver `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferencia Local:**
- ONNX Runtime: Inferencia multiplataforma optimizada
- Ollama: Gestión local sencilla de modelos (pre-configurado en contenedor de desarrollo)
- Apple MLX: Optimizado para Apple Silicon

## Solución de Problemas

### Problemas Comunes

**Problemas de Memoria:**
- Los modelos Phi requieren RAM significativa (especialmente variantes visión/multimodal)
- Usa modelos cuantificados para entornos con recursos limitados
- Ver `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflictos de Dependencias:**
- Los ejemplos de Python pueden necesitar versiones específicas
- Usa entornos virtuales para cada ejemplo
- Revisa archivos `requirements.txt` individuales

**Fallas en Descarga de Modelos:**
- Modelos grandes pueden agotar tiempo en conexiones lentas
- Considera usar entornos en la nube (Codespaces, Azure)
- Revisa caché Hugging Face: `~/.cache/huggingface/`

**Problemas con Proyectos .NET:**
- Asegúrate de tener instalado SDK .NET 8.0
- Usa `dotnet restore` antes de compilar
- Algunos proyectos incluyen configuraciones específicas CUDA (Debug_Cuda)

**Ejemplos de JavaScript/Web:**
- Usa Node.js 18+ para compatibilidad
- Limpia `node_modules` y reinstala si hay problemas
- Revisa consola del navegador para problemas de compatibilidad con WebGPU

### Obtener Ayuda

- **Discord:** Únete al Discord de la comunidad Microsoft Foundry
- **GitHub Issues:** Reporta errores e incidencias en el repositorio
- **GitHub Discussions:** Haz preguntas y comparte conocimientos

## Contexto Adicional

### IA Responsable

Todo uso de modelos Phi debe seguir los principios de IA Responsable de Microsoft:
- Justicia, fiabilidad, seguridad
- Privacidad y seguridad  
- Inclusividad, transparencia, responsabilidad
- Usa Azure AI Content Safety en aplicaciones de producción
- Ver `/md/01.Introduction/01/01.AISafety.md`

### Traducciones

- Más de 50 idiomas soportados mediante acción automatizada de GitHub
- Traducciones en el directorio `/translations/`
- Mantenidas por flujo de trabajo co-op-translator
- No editar archivos traducidos manualmente (generados automáticamente)

### Contribuciones

- Sigue las directrices en `CONTRIBUTING.md`
- Acepta el Acuerdo de Licencia para Contribuyentes (CLA)
- Cumple con el Código de Conducta de código abierto de Microsoft
- Mantén seguridad y credenciales fuera de los commits

### Soporte Multilenguaje

Este es un repositorio políglota con ejemplos en:
- **Python** - Flujos de trabajo ML/AI, notebooks Jupyter, ajuste fino
- **C#/.NET** - Aplicaciones empresariales, integración ONNX Runtime
- **JavaScript** - IA para web, inferencia en navegador con WebGPU

Elige el lenguaje que mejor se adapte a tu caso de uso y objetivo de despliegue.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->