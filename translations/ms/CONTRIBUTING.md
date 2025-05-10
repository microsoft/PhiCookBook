<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:42:41+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ms"
}
-->
# Contributing

Este proyecto recibe con agrado contribuciones y sugerencias. La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Contribuidor (CLA) que declara que tienes el derecho y realmente otorgas los derechos para usar tu contribución. Para más detalles, visita [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Cuando envíes una solicitud de extracción, un bot de CLA determinará automáticamente si necesitas proporcionar un CLA y marcará la solicitud adecuadamente (por ejemplo, revisión de estado, comentario). Simplemente sigue las instrucciones que te dé el bot. Solo tendrás que hacerlo una vez para todos los repositorios que usan nuestro CLA.

## Code of Conduct

Este proyecto ha adoptado el [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para más información, lee el [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) si tienes preguntas o comentarios adicionales.

## Cautions for creating issues

Por favor, no abras issues en GitHub para preguntas generales de soporte, ya que la lista de GitHub debe usarse para solicitudes de funciones y reportes de errores. De esta manera podemos rastrear más fácilmente problemas o bugs reales en el código y mantener la discusión general separada del código en sí.

## How to Contribute

### Pull Requests Guidelines

Al enviar una solicitud de extracción (PR) al repositorio Phi-3 CookBook, por favor sigue estas pautas:

- **Haz un fork del repositorio**: Siempre haz un fork del repositorio a tu propia cuenta antes de hacer tus modificaciones.

- **Solicitudes de extracción separadas (PR)**:
  - Envía cada tipo de cambio en su propia solicitud. Por ejemplo, las correcciones de errores y las actualizaciones de documentación deben enviarse en PRs separados.
  - Las correcciones de errores tipográficos y actualizaciones menores de documentación pueden combinarse en una sola PR cuando sea apropiado.

- **Manejo de conflictos de fusión**: Si tu solicitud muestra conflictos, actualiza tu rama local `main` para que refleje el repositorio principal antes de hacer tus modificaciones.

- **Envíos de traducción**: Al enviar una PR de traducción, asegúrate de que la carpeta de traducción incluya traducciones para todos los archivos en la carpeta original.

### Translation Guidelines

> [!IMPORTANT]
>
> Al traducir texto en este repositorio, no uses traducción automática. Solo participa en traducciones para idiomas en los que tengas dominio.

Si dominas un idioma distinto al inglés, puedes ayudar a traducir el contenido. Sigue estos pasos para asegurar que tus contribuciones de traducción se integren correctamente, por favor utiliza las siguientes pautas:

- **Crea la carpeta de traducción**: Navega a la carpeta de la sección correspondiente y crea una carpeta de traducción para el idioma al que contribuyes. Por ejemplo:
  - Para la sección de introducción: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Para la sección de inicio rápido: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continúa este patrón para otras secciones (03.Inference, 04.Finetuning, etc.)

- **Actualiza las rutas relativas**: Al traducir, ajusta la estructura de carpetas añadiendo `../../` al inicio de las rutas relativas dentro de los archivos markdown para que los enlaces funcionen correctamente. Por ejemplo, cambia:
  - `(../../imgs/01/phi3aisafety.png)` a `(../../../../imgs/01/phi3aisafety.png)`

- **Organiza tus traducciones**: Cada archivo traducido debe colocarse en la carpeta de traducción correspondiente a la sección. Por ejemplo, si traduces la sección de introducción al español, crearías lo siguiente:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Envía una PR completa**: Asegúrate de que todos los archivos traducidos de una sección estén incluidos en una sola PR. No aceptamos traducciones parciales de una sección. Al enviar una PR de traducción, verifica que la carpeta de traducción contenga traducciones para todos los archivos en la carpeta original.

### Writing Guidelines

Para asegurar consistencia en todos los documentos, por favor usa las siguientes pautas:

- **Formato de URLs**: Envuelve todas las URLs entre corchetes seguidos de paréntesis, sin espacios adicionales dentro o alrededor. Por ejemplo: `[example](https://www.microsoft.com)`.

- **Enlaces relativos**: Usa `./` para enlaces relativos a archivos o carpetas en el directorio actual, y `../` para los que apuntan a directorios superiores. Por ejemplo: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **No usar locales específicos de país**: Asegúrate de que tus enlaces no incluyan locales específicos de país. Por ejemplo, evita `/en-us/` o `/en/`.

- **Almacenamiento de imágenes**: Guarda todas las imágenes en la carpeta `./imgs`.

- **Nombres descriptivos para imágenes**: Nombra las imágenes de forma descriptiva usando caracteres en inglés, números y guiones. Por ejemplo: `example-image.jpg`.

## GitHub Workflows

Cuando envíes una solicitud de extracción, se activarán los siguientes flujos de trabajo para validar los cambios. Sigue las instrucciones a continuación para asegurar que tu PR pase las verificaciones:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Este flujo de trabajo asegura que todas las rutas relativas en tus archivos sean correctas.

1. Para asegurarte de que tus enlaces funcionan correctamente, realiza las siguientes tareas usando VS Code:
    - Pasa el cursor sobre cualquier enlace en tus archivos.
    - Presiona **Ctrl + Click** para navegar al enlace.
    - Si haces clic en un enlace y no funciona localmente, esto activará el flujo de trabajo y tampoco funcionará en GitHub.

1. Para solucionar este problema, realiza las siguientes tareas usando las sugerencias de ruta que ofrece VS Code:
    - Escribe `./` o `../`.
    - VS Code te mostrará opciones basadas en lo que escribiste.
    - Sigue la ruta haciendo clic en el archivo o carpeta deseada para asegurarte de que la ruta sea correcta.

Una vez que hayas añadido la ruta relativa correcta, guarda y sube tus cambios.

### Check URLs Don't Have Locale

Este flujo de trabajo asegura que ninguna URL web incluya un locale específico de país. Como este repositorio es accesible globalmente, es importante verificar que las URLs no contengan el locale de tu país.

1. Para verificar que tus URLs no tengan locales de país, realiza las siguientes tareas:

    - Revisa si hay texto como `/en-us/`, `/en/`, o cualquier otro locale de idioma en las URLs.
    - Si no están presentes, pasarás esta verificación.

1. Para corregir este problema, realiza las siguientes tareas:
    - Abre el archivo señalado por el flujo de trabajo.
    - Elimina el locale de país de las URLs.

Una vez que elimines el locale de país, guarda y sube tus cambios.

### Check Broken Urls

Este flujo de trabajo verifica que cualquier URL web en tus archivos esté funcionando y retorne un código de estado 200.

1. Para verificar que tus URLs funcionan correctamente, realiza las siguientes tareas:
    - Revisa el estado de las URLs en tus archivos.

2. Para corregir URLs rotas, realiza las siguientes tareas:
    - Abre el archivo que contiene la URL rota.
    - Actualiza la URL con la correcta.

Una vez que hayas corregido las URLs, guarda y sube tus cambios.

> [!NOTE]
>
> Puede haber casos donde la verificación de URLs falle aunque el enlace sea accesible. Esto puede ocurrir por varias razones, incluyendo:
>
> - **Restricciones de red:** Los servidores de GitHub Actions pueden tener restricciones que impidan el acceso a ciertas URLs.
> - **Problemas de tiempo de espera:** URLs que tardan demasiado en responder pueden causar un error de timeout en el flujo de trabajo.
> - **Problemas temporales del servidor:** Mantenimientos o caídas ocasionales pueden hacer que una URL no esté disponible temporalmente durante la validación.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.