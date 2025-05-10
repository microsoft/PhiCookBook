<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:43:51+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "cs"
}
-->
# Contributing

Este proyecto recibe con gusto contribuciones y sugerencias. La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Contribuyente (CLA) declarando que tienes el derecho y realmente nos otorgas los derechos para usar tu contribución. Para más detalles, visita [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Cuando envíes un pull request, un bot de CLA determinará automáticamente si necesitas proporcionar un CLA y decorará el PR apropiadamente (por ejemplo, verificación de estado, comentario). Simplemente sigue las instrucciones proporcionadas por el bot. Solo tendrás que hacer esto una vez para todos los repositorios que usan nuestro CLA.

## Code of Conduct

Este proyecto ha adoptado el [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Para más información, lee las [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) con cualquier pregunta o comentario adicional.

## Cautions for creating issues

Por favor, no abras issues en GitHub para preguntas generales de soporte, ya que la lista de GitHub debe usarse para solicitudes de características y reportes de errores. De esta manera podemos rastrear más fácilmente problemas o bugs reales del código y mantener la discusión general separada del código en sí.

## How to Contribute

### Pull Requests Guidelines

Al enviar un pull request (PR) al repositorio Phi-3 CookBook, por favor usa las siguientes pautas:

- **Haz fork del repositorio**: Siempre haz un fork del repositorio a tu propia cuenta antes de hacer tus modificaciones.

- **Pull requests (PR) separados**:
  - Envía cada tipo de cambio en su propio pull request. Por ejemplo, correcciones de bugs y actualizaciones de documentación deben enviarse en PRs separados.
  - Las correcciones de errores tipográficos y actualizaciones menores de documentación pueden combinarse en un solo PR cuando sea apropiado.

- **Manejo de conflictos de merge**: Si tu pull request muestra conflictos de merge, actualiza tu rama local `main` para reflejar el repositorio principal antes de hacer tus modificaciones.

- **Envíos de traducción**: Al enviar un PR de traducción, asegúrate de que la carpeta de traducción incluya las traducciones para todos los archivos de la carpeta original.

### Translation Guidelines

> [!IMPORTANT]
>
> Al traducir texto en este repositorio, no uses traducción automática. Solo ofrece traducciones para idiomas en los que seas competente.

Si dominas un idioma que no sea inglés, puedes ayudar a traducir el contenido. Sigue estos pasos para asegurar que tus contribuciones de traducción se integren correctamente, por favor utiliza las siguientes pautas:

- **Crea una carpeta de traducción**: Navega a la carpeta de la sección correspondiente y crea una carpeta de traducción para el idioma al que contribuyes. Por ejemplo:
  - Para la sección de introducción: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Para la sección de inicio rápido: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continúa este patrón para otras secciones (03.Inference, 04.Finetuning, etc.)

- **Actualiza rutas relativas**: Al traducir, ajusta la estructura de carpetas añadiendo `../../` al inicio de las rutas relativas dentro de los archivos markdown para asegurar que los enlaces funcionen correctamente. Por ejemplo, cambia:
  - `(../../imgs/01/phi3aisafety.png)` a `(../../../../imgs/01/phi3aisafety.png)`

- **Organiza tus traducciones**: Cada archivo traducido debe colocarse en la carpeta de traducción correspondiente a la sección. Por ejemplo, si traduces la sección de introducción al español, crearías:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Envía un PR completo**: Asegúrate de incluir todos los archivos traducidos de una sección en un solo PR. No aceptamos traducciones parciales para una sección. Al enviar un PR de traducción, asegúrate de que la carpeta de traducción incluya las traducciones para todos los archivos de la carpeta original.

### Writing Guidelines

Para asegurar consistencia en todos los documentos, por favor usa las siguientes pautas:

- **Formato de URLs**: Envuelve todas las URLs entre corchetes seguidos de paréntesis, sin espacios extras dentro o alrededor. Por ejemplo: `[example](https://www.microsoft.com)`.

- **Enlaces relativos**: Usa `./` para enlaces relativos a archivos o carpetas en el directorio actual, y `../` para aquellos en un directorio padre. Por ejemplo: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Locales no específicos de país**: Asegúrate de que tus enlaces no incluyan locales específicos de país. Por ejemplo, evita `/en-us/` o `/en/`.

- **Almacenamiento de imágenes**: Guarda todas las imágenes en la carpeta `./imgs`.

- **Nombres descriptivos para imágenes**: Nombra las imágenes descriptivamente usando caracteres en inglés, números y guiones. Por ejemplo: `example-image.jpg`.

## GitHub Workflows

Cuando envíes un pull request, se activarán los siguientes workflows para validar los cambios. Sigue las instrucciones a continuación para asegurar que tu pull request pase las verificaciones del workflow:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Este workflow asegura que todas las rutas relativas en tus archivos sean correctas.

1. Para asegurarte de que tus enlaces funcionan correctamente, realiza las siguientes tareas usando VS Code:
    - Pasa el cursor sobre cualquier enlace en tus archivos.
    - Presiona **Ctrl + Click** para navegar al enlace.
    - Si haces clic en un enlace y no funciona localmente, se activará el workflow y no funcionará en GitHub.

1. Para solucionar este problema, realiza las siguientes tareas usando las sugerencias de ruta que ofrece VS Code:
    - Escribe `./` o `../`.
    - VS Code te pedirá que elijas entre las opciones disponibles según lo que escribiste.
    - Sigue la ruta haciendo clic en el archivo o carpeta deseada para asegurarte de que la ruta es correcta.

Una vez que hayas agregado la ruta relativa correcta, guarda y sube tus cambios.

### Check URLs Don't Have Locale

Este workflow asegura que ninguna URL web incluya un locale específico de país. Como este repositorio es accesible globalmente, es importante que las URLs no contengan el locale de tu país.

1. Para verificar que tus URLs no tengan locales de país, realiza las siguientes tareas:

    - Revisa que no haya texto como `/en-us/`, `/en/`, o cualquier otro locale de idioma en las URLs.
    - Si no están presentes en tus URLs, pasarás esta verificación.

1. Para solucionar este problema, realiza las siguientes tareas:
    - Abre el archivo cuyo path fue destacado por el workflow.
    - Elimina el locale de país de las URLs.

Una vez que elimines el locale de país, guarda y sube tus cambios.

### Check Broken Urls

Este workflow asegura que cualquier URL web en tus archivos funcione y retorne código de estado 200.

1. Para verificar que tus URLs funcionen correctamente, realiza las siguientes tareas:
    - Revisa el estado de las URLs en tus archivos.

2. Para arreglar cualquier URL rota, realiza las siguientes tareas:
    - Abre el archivo que contiene la URL rota.
    - Actualiza la URL a la correcta.

Una vez que hayas corregido las URLs, guarda y sube tus cambios.

> [!NOTE]
>
> Puede haber casos donde la verificación de URLs falle aunque el enlace sea accesible. Esto puede suceder por varias razones, incluyendo:
>
> - **Restricciones de red:** Los servidores de GitHub Actions pueden tener restricciones de red que impiden el acceso a ciertas URLs.
> - **Problemas de tiempo de espera:** URLs que tardan demasiado en responder pueden generar un error de timeout en el workflow.
> - **Problemas temporales del servidor:** Caídas ocasionales o mantenimiento del servidor pueden hacer que una URL no esté disponible temporalmente durante la validación.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje využít profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.