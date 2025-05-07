<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-07T11:04:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "es"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot con Whisper

## Resumen

El Interactive Phi 3 Mini 4K Instruct Chatbot es una herramienta que permite a los usuarios interactuar con la demo Microsoft Phi 3 Mini 4K instruct utilizando entrada de texto o audio. El chatbot puede usarse para diversas tareas, como traducción, actualizaciones del clima y recopilación general de información.

### Primeros pasos

Para usar este chatbot, simplemente sigue estas instrucciones:

1. Abre un nuevo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. En la ventana principal del notebook, verás una interfaz de chat con un cuadro de texto para ingresar mensajes y un botón "Send".
3. Para usar el chatbot basado en texto, simplemente escribe tu mensaje en el cuadro de texto y haz clic en el botón "Send". El chatbot responderá con un archivo de audio que puede reproducirse directamente dentro del notebook.

**Nota**: Esta herramienta requiere una GPU y acceso a los modelos Microsoft Phi-3 y OpenAI Whisper, que se utilizan para el reconocimiento y traducción de voz.

### Requisitos de GPU

Para ejecutar esta demo necesitas 12 Gb de memoria GPU.

Los requisitos de memoria para ejecutar la demo **Microsoft-Phi-3-Mini-4K instruct** en una GPU dependen de varios factores, como el tamaño de los datos de entrada (audio o texto), el idioma utilizado para la traducción, la velocidad del modelo y la memoria disponible en la GPU.

En general, el modelo Whisper está diseñado para ejecutarse en GPUs. La cantidad mínima recomendada de memoria GPU para ejecutar Whisper es de 8 GB, aunque puede manejar cantidades mayores si es necesario.

Es importante destacar que procesar grandes volúmenes de datos o muchas solicitudes al modelo puede requerir más memoria GPU y/o causar problemas de rendimiento. Se recomienda probar tu caso de uso con diferentes configuraciones y monitorear el uso de memoria para determinar los ajustes óptimos según tus necesidades específicas.

## Ejemplo E2E para Interactive Phi 3 Mini 4K Instruct Chatbot con Whisper

El notebook de Jupyter titulado [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) muestra cómo usar la demo Microsoft Phi 3 Mini 4K instruct para generar texto a partir de entrada de audio o texto escrito. El notebook define varias funciones:

1. `tts_file_name(text)`: Esta función genera un nombre de archivo basado en el texto de entrada para guardar el archivo de audio generado.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta función usa la API Edge TTS para generar un archivo de audio a partir de una lista de fragmentos de texto de entrada. Los parámetros de entrada son la lista de fragmentos, la velocidad del habla, el nombre de la voz y la ruta de salida para guardar el archivo de audio generado.
1. `talk(input_text)`: Esta función genera un archivo de audio usando la API Edge TTS y lo guarda con un nombre aleatorio en el directorio /content/audio. El parámetro de entrada es el texto que se convertirá en voz.
1. `run_text_prompt(message, chat_history)`: Esta función usa la demo Microsoft Phi 3 Mini 4K instruct para generar un archivo de audio a partir de un mensaje de entrada y lo añade al historial del chat.
1. `run_audio_prompt(audio, chat_history)`: Esta función convierte un archivo de audio en texto usando la API del modelo Whisper y lo pasa a la función `run_text_prompt()`.
1. El código lanza una aplicación Gradio que permite a los usuarios interactuar con la demo Phi 3 Mini 4K instruct escribiendo mensajes o subiendo archivos de audio. La salida se muestra como un mensaje de texto dentro de la app.

## Solución de problemas

Instalación de drivers Cuda para GPU

1. Asegúrate de que tu aplicación Linux esté actualizada

    ```bash
    sudo apt update
    ```

1. Instala los drivers de Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registra la ubicación del driver cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Verifica el tamaño de la memoria de la GPU Nvidia (Se requieren 12GB de memoria GPU)

    ```bash
    nvidia-smi
    ```

1. Vaciar caché: Si usas PyTorch, puedes llamar a torch.cuda.empty_cache() para liberar toda la memoria caché no usada y que pueda ser utilizada por otras aplicaciones GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verificar Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Realiza las siguientes tareas para crear un token de Hugging Face.

    - Navega a la [página de configuración de tokens de Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selecciona **New token**.
    - Ingresa el **Nombre** del proyecto que deseas usar.
    - Selecciona el **Tipo** como **Write**.

> **Nota**
>
> Si encuentras el siguiente error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para resolverlo, escribe el siguiente comando en tu terminal.
>
> ```bash
> sudo ldconfig
> ```

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.