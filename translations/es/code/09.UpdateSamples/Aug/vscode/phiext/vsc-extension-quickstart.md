<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-03-27T05:06:20+00:00",
  "source_file": "code\\09.UpdateSamples\\Aug\\vscode\\phiext\\vsc-extension-quickstart.md",
  "language_code": "es"
}
-->
# Bienvenido a tu Extensión de VS Code

## Qué hay en la carpeta

* Esta carpeta contiene todos los archivos necesarios para tu extensión.
* `package.json` - este es el archivo de manifiesto donde declaras tu extensión y comando.
  * El plugin de ejemplo registra un comando y define su título y nombre de comando. Con esta información, VS Code puede mostrar el comando en el panel de comandos. Aún no necesita cargar el plugin.
* `src/extension.ts` - este es el archivo principal donde proporcionarás la implementación de tu comando.
  * El archivo exporta una función, `activate`, que se llama la primera vez que se activa tu extensión (en este caso al ejecutar el comando). Dentro de la función `activate` llamamos a `registerCommand`.
  * Pasamos la función que contiene la implementación del comando como segundo parámetro a `registerCommand`.

## Configuración

* Instala las extensiones recomendadas (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner y dbaeumer.vscode-eslint).

## Ponlo en marcha de inmediato

* Presiona `F5` para abrir una nueva ventana con tu extensión cargada.
* Ejecuta tu comando desde el panel de comandos presionando (`Ctrl+Shift+P` o `Cmd+Shift+P` en Mac) y escribiendo `Hello World`.
* Establece puntos de interrupción en tu código dentro de `src/extension.ts` para depurar tu extensión.
* Encuentra la salida de tu extensión en la consola de depuración.

## Realiza cambios

* Puedes reiniciar la extensión desde la barra de herramientas de depuración después de cambiar el código en `src/extension.ts`.
* También puedes recargar (`Ctrl+R` o `Cmd+R` en Mac) la ventana de VS Code con tu extensión para cargar tus cambios.

## Explora la API

* Puedes abrir el conjunto completo de nuestra API cuando abras el archivo `node_modules/@types/vscode/index.d.ts`.

## Ejecuta pruebas

* Instala el [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Ejecuta la tarea "watch" mediante el comando **Tasks: Run Task**. Asegúrate de que esté en ejecución, o las pruebas podrían no ser detectadas.
* Abre la vista de Testing desde la barra de actividades y haz clic en el botón "Run Test", o usa la tecla rápida `Ctrl/Cmd + ; A`.
* Consulta el resultado de las pruebas en la vista de Resultados de Pruebas.
* Realiza cambios en `src/test/extension.test.ts` o crea nuevos archivos de prueba dentro de la carpeta `test`.
  * El ejecutor de pruebas proporcionado solo considerará archivos que coincidan con el patrón de nombre `**.test.ts`.
  * Puedes crear carpetas dentro de la carpeta `test` para estructurar tus pruebas como desees.

## Ve más allá

* Reduce el tamaño de la extensión y mejora el tiempo de inicio [empaquetando tu extensión](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publica tu extensión](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) en el mercado de extensiones de VS Code.
* Automatiza los procesos de construcción configurando [Integración Continua](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.