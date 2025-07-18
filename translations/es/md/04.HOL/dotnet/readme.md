<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:30:31+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "es"
}
-->
## Bienvenido a los laboratorios Phi usando C#

Aquí encontrarás una selección de laboratorios que muestran cómo integrar las diferentes versiones potentes de los modelos Phi en un entorno .NET.

## Requisitos previos

Antes de ejecutar el ejemplo, asegúrate de tener instalado lo siguiente:

**.NET 9:** Verifica que tengas instalada la [última versión de .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) en tu equipo.

**(Opcional) Visual Studio o Visual Studio Code:** Necesitarás un IDE o editor de código capaz de ejecutar proyectos .NET. Se recomienda [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) o [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Usando git** clona localmente una de las versiones disponibles Phi-3, Phi3.5 o Phi-4 desde [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Descarga los modelos Phi-4 ONNX** a tu máquina local:

### navega a la carpeta donde almacenar los modelos

```bash
cd c:\phi\models
```

### agrega soporte para lfs

```bash
git lfs install 
```

### clona y descarga el modelo Phi-4 mini instruct y el modelo multimodal Phi-4

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Descarga los modelos Phi-3 ONNX** a tu máquina local:

### clona y descarga el modelo Phi-3 mini 4K instruct y el modelo Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Importante:** Las demos actuales están diseñadas para usar las versiones ONNX del modelo. Los pasos anteriores clonan los siguientes modelos.

## Sobre los laboratorios

La solución principal contiene varios laboratorios de ejemplo que demuestran las capacidades de los modelos Phi usando C#.

| Proyecto | Modelo | Descripción |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 o Phi-3.5 | Chat de consola de ejemplo que permite al usuario hacer preguntas. El proyecto carga un modelo ONNX Phi-3 local usando las librerías `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 o Phi-3.5 | Chat de consola de ejemplo que permite al usuario hacer preguntas. El proyecto carga un modelo ONNX Phi-3 local usando las librerías `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 o Phi-3.5 | Proyecto de ejemplo que usa un modelo local phi3 vision para analizar imágenes. El proyecto carga un modelo ONNX Phi-3 Vision local usando las librerías `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 o Phi-3.5 | Proyecto de ejemplo que usa un modelo local phi3 vision para analizar imágenes. El proyecto carga un modelo ONNX Phi-3 Vision local usando las librerías `Microsoft.ML.OnnxRuntime`. Además, presenta un menú con diferentes opciones para interactuar con el usuario. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Chat de consola de ejemplo que permite al usuario hacer preguntas. El proyecto carga un modelo ONNX Phi-4 local usando las librerías `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Chat de consola de ejemplo que permite al usuario hacer preguntas. El proyecto carga un modelo ONNX Phi-4 local usando las librerías `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Chat de consola de ejemplo que permite al usuario hacer preguntas. El proyecto carga un modelo ONNX Phi-4 local usando las librerías `Microsoft.ML.OnnxRuntimeGenAI` e implementa la interfaz `IChatClient` de `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Chat de consola de ejemplo que permite al usuario hacer preguntas. El chat implementa memoria. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Proyecto de ejemplo que usa un modelo local Phi-4 para analizar imágenes mostrando el resultado en la consola. El proyecto carga un modelo local Phi-4-`multimodal-instruct-onnx` usando las librerías `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Proyecto de ejemplo que usa un modelo local Phi-4 para analizar un archivo de audio, generar la transcripción del archivo y mostrar el resultado en la consola. El proyecto carga un modelo local Phi-4-`multimodal-instruct-onnx` usando las librerías `Microsoft.ML.OnnxRuntime`. |

## Cómo ejecutar los proyectos

Para ejecutar los proyectos, sigue estos pasos:

1. Clona el repositorio en tu máquina local.

1. Abre una terminal y navega al proyecto deseado. Por ejemplo, vamos a ejecutar `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Ejecuta el proyecto con el comando

    ```bash
    dotnet run
    ```

1. El proyecto de ejemplo solicita una entrada del usuario y responde usando el modelo local.

   La demo en ejecución es similar a esta:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.