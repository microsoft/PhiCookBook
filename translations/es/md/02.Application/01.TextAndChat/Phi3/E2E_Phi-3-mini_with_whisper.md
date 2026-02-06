# Chatbot Interactivo Phi 3 Mini 4K Instruct con Whisper

## Descripción general

El Chatbot Interactivo Phi 3 Mini 4K Instruct es una herramienta que permite a los usuarios interactuar con la demo Microsoft Phi 3 Mini 4K instruct usando entrada de texto o audio. El chatbot puede ser utilizado para una variedad de tareas, como traducción, actualizaciones meteorológicas y recopilación de información general.

### Cómo empezar

Para usar este chatbot, simplemente siga estas instrucciones:

1. Abra un nuevo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. En la ventana principal del cuaderno, verá una interfaz de chat con un cuadro de entrada de texto y un botón "Enviar".
3. Para usar el chatbot basado en texto, simplemente escriba su mensaje en el cuadro de entrada de texto y haga clic en el botón "Enviar". El chatbot responderá con un archivo de audio que se puede reproducir directamente desde el cuaderno.

**Nota**: Esta herramienta requiere una GPU y acceso a los modelos Microsoft Phi-3 y OpenAI Whisper, que se usan para reconocimiento y traducción de voz.

### Requisitos de GPU

Para ejecutar esta demo necesita 12 Gb de memoria de GPU.

Los requisitos de memoria para ejecutar la demo **Microsoft-Phi-3-Mini-4K instruct** en una GPU dependerán de varios factores, como el tamaño de los datos de entrada (audio o texto), el idioma usado para la traducción, la velocidad del modelo y la memoria disponible en la GPU.

En general, el modelo Whisper está diseñado para ejecutarse en GPUs. La cantidad mínima recomendada de memoria GPU para ejecutar el modelo Whisper es de 8 GB, pero puede manejar mayores cantidades de memoria si es necesario.

Es importante notar que ejecutar una gran cantidad de datos o un alto volumen de solicitudes en el modelo puede requerir más memoria GPU y/o puede causar problemas de rendimiento. Se recomienda probar su caso de uso con diferentes configuraciones y monitorear el uso de memoria para determinar la configuración óptima para sus necesidades específicas.

## Ejemplo E2E para el Chatbot Interactivo Phi 3 Mini 4K Instruct con Whisper

El cuaderno jupyter titulado [Chatbot Interactivo Phi 3 Mini 4K Instruct con Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demuestra cómo usar la demo Microsoft Phi 3 Mini 4K instruct para generar texto a partir de audio o texto escrito. El cuaderno define varias funciones:

1. `tts_file_name(text)`: Esta función genera un nombre de archivo basado en el texto de entrada para guardar el archivo de audio generado.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta función usa la API Edge TTS para generar un archivo de audio a partir de una lista de fragmentos de texto de entrada. Los parámetros de entrada son la lista de fragmentos, la velocidad de habla, el nombre de la voz y la ruta de salida para guardar el archivo de audio generado.
1. `talk(input_text)`: Esta función genera un archivo de audio usando la API Edge TTS y lo guarda con un nombre aleatorio en el directorio /content/audio. El parámetro de entrada es el texto que se convertirá en habla.
1. `run_text_prompt(message, chat_history)`: Esta función usa la demo Microsoft Phi 3 Mini 4K instruct para generar un archivo de audio a partir de un mensaje de entrada y lo añade al historial de chat.
1. `run_audio_prompt(audio, chat_history)`: Esta función convierte un archivo de audio en texto usando la API del modelo Whisper y lo pasa a la función `run_text_prompt()`.
1. El código lanza una aplicación Gradio que permite a los usuarios interactuar con la demo Phi 3 Mini 4K instruct ya sea escribiendo mensajes o subiendo archivos de audio. La salida se muestra como un mensaje de texto dentro de la aplicación.

## Solución de problemas

Instalación de drivers Cuda GPU

1. Asegúrese de que sus aplicaciones Linux estén actualizadas

    ```bash
    sudo apt update
    ```

1. Instale los drivers Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registre la ubicación del driver cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Comprobar el tamaño de memoria de la GPU Nvidia (Se requiere 12GB de memoria GPU)

    ```bash
    nvidia-smi
    ```

1. Vaciar caché: si está usando PyTorch, puede llamar a torch.cuda.empty_cache() para liberar toda la memoria caché no utilizada para que pueda ser usada por otras aplicaciones GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Comprobando Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Realice las siguientes tareas para crear un token de Hugging Face.

    - Navegue a la [página de configuración de tokens de Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Seleccione **Nuevo token**.
    - Ingrese el **Nombre** del proyecto que desea usar.
    - Seleccione el **Tipo** a **Write**.

> [!NOTE]
>
> Si encuentra el siguiente error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para resolverlo, escriba el siguiente comando dentro de su terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan derivarse del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->