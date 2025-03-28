<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-03-27T02:29:09+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "es"
}
-->
# Contribuir

Este proyecto da la bienvenida a contribuciones y sugerencias. La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Contribuyente (CLA), declarando que tienes el derecho de otorgarnos los permisos necesarios para usar tu contribución. Para más detalles, visita [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Cuando envíes una solicitud de extracción (pull request), un bot de CLA determinará automáticamente si necesitas proporcionar un CLA y decorará la PR apropiadamente (por ejemplo, con un estado de verificación o comentario). Simplemente sigue las instrucciones proporcionadas por el bot. Solo necesitarás hacer esto una vez en todos los repositorios que usen nuestro CLA.

## Código de Conducta

Este proyecto ha adoptado el [Código de Conducta de Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). Para más información, lee las [Preguntas Frecuentes sobre el Código de Conducta](https://opensource.microsoft.com/codeofconduct/faq/) o contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) si tienes preguntas o comentarios adicionales.

## Precauciones para crear problemas

Por favor, no abras problemas en GitHub para preguntas generales de soporte, ya que la lista de GitHub debe ser utilizada para solicitudes de características y reportes de errores. De esta manera, podemos rastrear más fácilmente problemas reales o errores en el código y mantener la discusión general separada del código.

## Cómo Contribuir

### Directrices para Solicitudes de Extracción (PR)

Al enviar una solicitud de extracción (PR) al repositorio Phi-3 CookBook, utiliza las siguientes pautas:

- **Haz un fork del repositorio**: Siempre haz un fork del repositorio en tu propia cuenta antes de realizar modificaciones.

- **Solicitudes de extracción separadas (PR)**:
  - Envía cada tipo de cambio en su propia solicitud de extracción. Por ejemplo, las correcciones de errores y las actualizaciones de documentación deben enviarse en PRs separados.
  - Las correcciones de errores tipográficos y las actualizaciones menores de documentación pueden combinarse en una sola PR si es apropiado.

- **Manejo de conflictos de fusión**: Si tu solicitud de extracción muestra conflictos de fusión, actualiza tu rama local `main` para reflejar el repositorio principal antes de realizar tus modificaciones.

- **Envíos de traducción**: Al enviar una PR de traducción, asegúrate de que la carpeta de traducciones incluya traducciones de todos los archivos de la carpeta original.

### Directrices para Traducción

> [!IMPORTANT]
>
> Al traducir texto en este repositorio, no utilices traducción automática. Solo ofrece traducciones en idiomas en los que seas competente.

Si dominas un idioma distinto al inglés, puedes ayudar a traducir el contenido. Sigue estos pasos para garantizar que tus contribuciones de traducción se integren correctamente y utiliza las siguientes pautas:

- **Crear carpeta de traducción**: Navega a la carpeta de la sección correspondiente y crea una carpeta de traducción para el idioma al que estás contribuyendo. Por ejemplo:
  - Para la sección de introducción: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Para la sección de inicio rápido: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continúa este patrón para otras secciones (03.Inference, 04.Finetuning, etc.).

- **Actualizar rutas relativas**: Al traducir, ajusta la estructura de carpetas añadiendo `../../` al inicio de las rutas relativas dentro de los archivos markdown para garantizar que los enlaces funcionen correctamente. Por ejemplo, cambia lo siguiente:
  - Cambia `(../../imgs/01/phi3aisafety.png)` a `(../../../../imgs/01/phi3aisafety.png)`.

- **Organiza tus traducciones**: Cada archivo traducido debe colocarse en la carpeta de traducción correspondiente a la sección. Por ejemplo, si estás traduciendo la sección de introducción al español, deberías crear lo siguiente:
  - `PhiCookBook/md/01.Introduce/translations/es/`.

- **Enviar una PR completa**: Asegúrate de incluir todos los archivos traducidos para una sección en una sola PR. No aceptamos traducciones parciales para una sección. Al enviar una PR de traducción, asegúrate de que la carpeta de traducción incluya traducciones de todos los archivos de la carpeta original.

### Directrices de Redacción

Para garantizar la coherencia en todos los documentos, utiliza las siguientes pautas:

- **Formato de URLs**: Envuelve todas las URLs entre corchetes seguidos de paréntesis, sin espacios adicionales alrededor o dentro de ellos. Por ejemplo: `[example](https://www.microsoft.com)`.

- **Enlaces relativos**: Usa `./` para enlaces relativos que apunten a archivos o carpetas en el directorio actual, y `../` para aquellos en un directorio superior. Por ejemplo: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Locales no específicos de país**: Asegúrate de que tus enlaces no incluyan locales específicos de país. Por ejemplo, evita `/en-us/` o `/en/`.

- **Almacenamiento de imágenes**: Almacena todas las imágenes en la carpeta `./imgs`.

- **Nombres descriptivos para imágenes**: Nombra las imágenes de manera descriptiva usando caracteres en inglés, números y guiones. Por ejemplo: `example-image.jpg`.

## Flujos de Trabajo de GitHub

Cuando envíes una solicitud de extracción, se activarán los siguientes flujos de trabajo para validar los cambios. Sigue las instrucciones a continuación para garantizar que tu solicitud de extracción pase las verificaciones de flujo de trabajo:

- [Verificar Rutas Relativas Rotas](../..)
- [Verificar que las URLs No Tengan Locale](../..)

### Verificar Rutas Relativas Rotas

Este flujo de trabajo asegura que todas las rutas relativas en tus archivos sean correctas.

1. Para asegurarte de que tus enlaces funcionen correctamente, realiza las siguientes tareas usando VS Code:
    - Pasa el cursor sobre cualquier enlace en tus archivos.
    - Presiona **Ctrl + Click** para navegar al enlace.
    - Si haces clic en un enlace y no funciona localmente, activará el flujo de trabajo y no funcionará en GitHub.

1. Para solucionar este problema, realiza las siguientes tareas usando las sugerencias de rutas proporcionadas por VS Code:
    - Escribe `./` o `../`.
    - VS Code te indicará las opciones disponibles según lo que escribiste.
    - Sigue la ruta haciendo clic en el archivo o carpeta deseado para garantizar que tu ruta sea correcta.

Una vez que hayas añadido la ruta relativa correcta, guarda y sube tus cambios.

### Verificar que las URLs No Tengan Locale

Este flujo de trabajo asegura que ninguna URL web incluya un locale específico de país. Dado que este repositorio es accesible globalmente, es importante garantizar que las URLs no contengan el locale de tu país.

1. Para verificar que tus URLs no tengan locales específicos de país, realiza las siguientes tareas:

    - Busca texto como `/en-us/`, `/en/` o cualquier otro locale de idioma en las URLs.
    - Si estos no están presentes en tus URLs, entonces pasarás esta verificación.

1. Para solucionar este problema, realiza las siguientes tareas:
    - Abre la ruta del archivo resaltada por el flujo de trabajo.
    - Elimina el locale de país de las URLs.

Una vez que elimines el locale de país, guarda y sube tus cambios.

### Verificar URLs Rotas

Este flujo de trabajo asegura que cualquier URL web en tus archivos funcione y devuelva un código de estado 200.

1. Para verificar que tus URLs funcionen correctamente, realiza las siguientes tareas:
    - Verifica el estado de las URLs en tus archivos.

2. Para solucionar cualquier URL rota, realiza las siguientes tareas:
    - Abre el archivo que contiene la URL rota.
    - Actualiza la URL a la correcta.

Una vez que hayas solucionado las URLs, guarda y sube tus cambios.

> [!NOTE]
>
> Puede haber casos en los que la verificación de URLs falle aunque el enlace sea accesible. Esto puede suceder por varias razones, incluyendo:
>
> - **Restricciones de red:** Los servidores de acciones de GitHub pueden tener restricciones de red que impidan el acceso a ciertas URLs.
> - **Problemas de tiempo de espera:** Las URLs que tardan demasiado en responder pueden desencadenar un error de tiempo de espera en el flujo de trabajo.
> - **Problemas temporales del servidor:** El tiempo de inactividad ocasional o el mantenimiento del servidor pueden hacer que una URL esté temporalmente no disponible durante la validación.

