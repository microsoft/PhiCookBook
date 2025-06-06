<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-05-27T02:39:19+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "es"
}
-->
# Contribuyendo

Este proyecto acepta contribuciones y sugerencias. La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Contribuidor (CLA) declarando que tienes el derecho y realmente nos otorgas los derechos para usar tu contribución. Para más detalles, visita [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Cuando envíes un pull request, un bot de CLA determinará automáticamente si necesitas proporcionar un CLA y decorará el PR adecuadamente (por ejemplo, con una verificación de estado o comentario). Simplemente sigue las instrucciones proporcionadas por el bot. Solo necesitarás hacer esto una vez para todos los repositorios que usan nuestro CLA.

## Código de Conducta

Este proyecto ha adoptado el [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Para más información, lee las [Preguntas Frecuentes sobre el Código de Conducta](https://opensource.microsoft.com/codeofconduct/faq/) o contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) para cualquier pregunta o comentario adicional.

## Precauciones para crear issues

Por favor, no abras issues en GitHub para preguntas generales de soporte, ya que la lista de GitHub debe usarse para solicitudes de funciones y reportes de errores. De esta manera podemos rastrear más fácilmente los problemas o bugs reales del código y mantener la discusión general separada del código en sí.

## Cómo Contribuir

### Directrices para Pull Requests

Al enviar un pull request (PR) al repositorio Phi-3 CookBook, por favor usa las siguientes directrices:

- **Haz un fork del repositorio**: Siempre haz un fork del repositorio a tu propia cuenta antes de hacer tus modificaciones.

- **Pull requests separadas (PR)**:
  - Envía cada tipo de cambio en su propio pull request. Por ejemplo, las correcciones de errores y las actualizaciones de documentación deben enviarse en PRs separados.
  - Las correcciones de errores tipográficos y las pequeñas actualizaciones de documentación pueden combinarse en un solo PR cuando sea apropiado.

- **Maneja los conflictos de merge**: Si tu pull request muestra conflictos de merge, actualiza tu rama local `main` para reflejar el repositorio principal antes de hacer tus modificaciones.

- **Envíos de traducciones**: Cuando envíes un PR de traducción, asegúrate de que la carpeta de traducción incluya traducciones para todos los archivos de la carpeta original.

### Directrices de Escritura

Para asegurar consistencia en todos los documentos, por favor usa las siguientes pautas:

- **Formato de URLs**: Envuelve todas las URLs entre corchetes seguidos de paréntesis, sin espacios extras alrededor o dentro de ellos. Por ejemplo: `[example](https://www.microsoft.com)`.

- **Enlaces relativos**: Usa `./` para enlaces relativos que apuntan a archivos o carpetas en el directorio actual, y `../` para los que están en un directorio padre. Por ejemplo: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Locales no específicos de país**: Asegúrate de que tus enlaces no incluyan locales específicos de país. Por ejemplo, evita `/en-us/` o `/en/`.

- **Almacenamiento de imágenes**: Guarda todas las imágenes en la carpeta `./imgs`.

- **Nombres descriptivos para imágenes**: Nombra las imágenes de forma descriptiva usando caracteres en inglés, números y guiones. Por ejemplo: `example-image.jpg`.

## Flujos de trabajo en GitHub

Cuando envíes un pull request, se activarán los siguientes flujos de trabajo para validar los cambios. Sigue las instrucciones a continuación para asegurarte de que tu pull request pase las verificaciones del flujo de trabajo:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Este flujo de trabajo asegura que todas las rutas relativas en tus archivos sean correctas.

1. Para asegurarte de que tus enlaces funcionan correctamente, realiza las siguientes tareas usando VS Code:
    - Pasa el cursor sobre cualquier enlace en tus archivos.
    - Presiona **Ctrl + Click** para navegar al enlace.
    - Si haces clic en un enlace y no funciona localmente, se activará el flujo de trabajo y no funcionará en GitHub.

1. Para corregir este problema, realiza las siguientes tareas usando las sugerencias de ruta que ofrece VS Code:
    - Escribe `./` o `../`.
    - VS Code te pedirá que elijas entre las opciones disponibles según lo que escribiste.
    - Sigue la ruta haciendo clic en el archivo o carpeta deseada para asegurarte de que la ruta es correcta.

Una vez que hayas agregado la ruta relativa correcta, guarda y sube tus cambios.

### Check URLs Don't Have Locale

Este flujo de trabajo asegura que cualquier URL web no incluya un locale específico de país. Como este repositorio es accesible globalmente, es importante asegurarse de que las URLs no contengan el locale de tu país.

1. Para verificar que tus URLs no tengan locales de país, realiza las siguientes tareas:

    - Revisa si hay texto como `/en-us/`, `/en/`, o cualquier otro locale de idioma en las URLs.
    - Si estos no están presentes en tus URLs, entonces pasarás esta verificación.

1. Para corregir este problema, realiza las siguientes tareas:
    - Abre la ruta del archivo que el flujo de trabajo haya resaltado.
    - Elimina el locale de país de las URLs.

Una vez que elimines el locale de país, guarda y sube tus cambios.

### Check Broken Urls

Este flujo de trabajo asegura que cualquier URL web en tus archivos esté funcionando y devuelva un código de estado 200.

1. Para verificar que tus URLs funcionan correctamente, realiza las siguientes tareas:
    - Revisa el estado de las URLs en tus archivos.

2. Para corregir cualquier URL rota, realiza las siguientes tareas:
    - Abre el archivo que contiene la URL rota.
    - Actualiza la URL a la correcta.

Una vez que hayas corregido las URLs, guarda y sube tus cambios.

> [!NOTE]
>
> Puede haber casos en los que la verificación de URLs falle aunque el enlace sea accesible. Esto puede suceder por varias razones, incluyendo:
>
> - **Restricciones de red:** Los servidores de GitHub Actions pueden tener restricciones de red que impidan el acceso a ciertas URLs.
> - **Problemas de tiempo de espera:** Las URLs que tardan demasiado en responder pueden generar un error de timeout en el flujo de trabajo.
> - **Problemas temporales del servidor:** Caídas ocasionales o mantenimiento del servidor pueden hacer que una URL no esté disponible temporalmente durante la validación.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.