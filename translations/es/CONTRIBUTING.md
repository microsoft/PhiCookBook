<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:35:22+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "es"
}
-->
# Contribuir

Este proyecto acepta contribuciones y sugerencias. La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Contribuidor (CLA) declarando que tienes el derecho y realmente otorgas los derechos para que usemos tu contribución. Para más detalles, visita [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Cuando envíes una pull request, un bot de CLA determinará automáticamente si necesitas proporcionar un CLA y marcará la PR adecuadamente (por ejemplo, con una verificación de estado o un comentario). Simplemente sigue las instrucciones que te dé el bot. Solo tendrás que hacer esto una vez para todos los repositorios que usan nuestro CLA.

## Código de Conducta

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Para más información, lee las [Preguntas Frecuentes sobre el Código de Conducta](https://opensource.microsoft.com/codeofconduct/faq/) o contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) con cualquier pregunta o comentario adicional.

## Precauciones para crear issues

Por favor, no abras issues en GitHub para preguntas generales de soporte, ya que la lista de GitHub debe usarse para solicitudes de características y reportes de errores. De esta forma podemos rastrear más fácilmente los problemas o bugs reales del código y mantener la discusión general separada del código en sí.

## Cómo Contribuir

### Directrices para Pull Requests

Al enviar una pull request (PR) al repositorio Phi-3 CookBook, por favor sigue estas pautas:

- **Haz un fork del repositorio**: Siempre haz un fork del repositorio a tu propia cuenta antes de hacer tus modificaciones.

- **Pull requests separadas (PR)**:
  - Envía cada tipo de cambio en su propia pull request. Por ejemplo, correcciones de bugs y actualizaciones de documentación deben enviarse en PRs separadas.
  - Correcciones de errores tipográficos y pequeñas actualizaciones de documentación pueden combinarse en una sola PR cuando sea apropiado.

- **Maneja conflictos de merge**: Si tu pull request muestra conflictos de merge, actualiza tu rama local `main` para que refleje el repositorio principal antes de hacer tus modificaciones.

- **Envíos de traducciones**: Al enviar una PR de traducción, asegúrate de que la carpeta de traducción incluya traducciones para todos los archivos de la carpeta original.

### Directrices de Redacción

Para asegurar consistencia en todos los documentos, por favor usa las siguientes pautas:

- **Formato de URLs**: Envuelve todas las URLs entre corchetes seguidos de paréntesis, sin espacios extras alrededor o dentro. Por ejemplo: `[ejemplo](https://www.microsoft.com)`.

- **Enlaces relativos**: Usa `./` para enlaces relativos que apunten a archivos o carpetas en el directorio actual, y `../` para los que estén en un directorio padre. Por ejemplo: `[ejemplo](../../ruta/al/archivo)` o `[ejemplo](../../../ruta/al/archivo)`.

- **Locales no específicos de país**: Asegúrate de que tus enlaces no incluyan locales específicos de país. Por ejemplo, evita `/en-us/` o `/en/`.

- **Almacenamiento de imágenes**: Guarda todas las imágenes en la carpeta `./imgs`.

- **Nombres descriptivos para imágenes**: Nombra las imágenes de forma descriptiva usando caracteres en inglés, números y guiones. Por ejemplo: `ejemplo-imagen.jpg`.

## Flujos de trabajo en GitHub

Cuando envíes una pull request, se activarán los siguientes flujos de trabajo para validar los cambios. Sigue las instrucciones a continuación para asegurarte de que tu pull request pase las verificaciones:

- [Verificar rutas relativas rotas](../..)
- [Verificar que las URLs no tengan locale](../..)

### Verificar rutas relativas rotas

Este flujo de trabajo asegura que todas las rutas relativas en tus archivos sean correctas.

1. Para asegurarte de que tus enlaces funcionan correctamente, realiza las siguientes tareas usando VS Code:
    - Pasa el cursor sobre cualquier enlace en tus archivos.
    - Presiona **Ctrl + Click** para navegar al enlace.
    - Si haces clic en un enlace y no funciona localmente, esto activará el flujo de trabajo y tampoco funcionará en GitHub.

1. Para corregir este problema, realiza las siguientes tareas usando las sugerencias de ruta que ofrece VS Code:
    - Escribe `./` o `../`.
    - VS Code te mostrará opciones disponibles basadas en lo que escribiste.
    - Sigue la ruta haciendo clic en el archivo o carpeta deseada para asegurarte de que la ruta es correcta.

Una vez que hayas agregado la ruta relativa correcta, guarda y sube tus cambios.

### Verificar que las URLs no tengan locale

Este flujo de trabajo asegura que ninguna URL web incluya un locale específico de país. Como este repositorio es accesible globalmente, es importante que las URLs no contengan el locale de tu país.

1. Para verificar que tus URLs no tengan locales de país, realiza las siguientes tareas:

    - Revisa que no haya texto como `/en-us/`, `/en/` u otro locale de idioma en las URLs.
    - Si no están presentes en tus URLs, pasarás esta verificación.

1. Para corregir este problema, realiza las siguientes tareas:
    - Abre el archivo señalado por el flujo de trabajo.
    - Elimina el locale de país de las URLs.

Una vez que elimines el locale de país, guarda y sube tus cambios.

### Verificar URLs rotas

Este flujo de trabajo asegura que cualquier URL web en tus archivos funcione y devuelva un código de estado 200.

1. Para verificar que tus URLs funcionan correctamente, realiza las siguientes tareas:
    - Revisa el estado de las URLs en tus archivos.

2. Para corregir cualquier URL rota, realiza las siguientes tareas:
    - Abre el archivo que contiene la URL rota.
    - Actualiza la URL por la correcta.

Una vez que hayas corregido las URLs, guarda y sube tus cambios.

> [!NOTE]
>
> Puede haber casos en los que la verificación de URLs falle aunque el enlace sea accesible. Esto puede ocurrir por varias razones, incluyendo:
>
> - **Restricciones de red:** Los servidores de acciones de GitHub pueden tener restricciones de red que impiden el acceso a ciertas URLs.
> - **Problemas de tiempo de espera:** URLs que tardan demasiado en responder pueden generar un error de timeout en el flujo de trabajo.
> - **Problemas temporales del servidor:** Caídas ocasionales o mantenimiento del servidor pueden hacer que una URL no esté disponible temporalmente durante la validación.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.