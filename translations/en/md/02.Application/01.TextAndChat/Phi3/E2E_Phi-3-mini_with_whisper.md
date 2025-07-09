<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-09T19:12:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "en"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

The Interactive Phi 3 Mini 4K Instruct Chatbot is a tool that lets users interact with the Microsoft Phi 3 Mini 4K instruct demo using either text or audio input. This chatbot can be used for various tasks, including translation, weather updates, and general information retrieval.

### Getting Started

To use this chatbot, just follow these steps:

1. Open the [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) notebook.
2. In the main notebook window, you’ll see a chatbox interface with a text input field and a "Send" button.
3. To use the text-based chatbot, type your message into the input box and click "Send." The chatbot will reply with an audio file that you can play directly within the notebook.

**Note**: This tool requires a GPU and access to the Microsoft Phi-3 and OpenAI Whisper models, which handle speech recognition and translation.

### GPU Requirements

Running this demo requires 12GB of GPU memory.

The GPU memory needed to run the **Microsoft-Phi-3-Mini-4K instruct** demo depends on several factors, such as the size of the input data (audio or text), the language used for translation, the model’s speed, and the available GPU memory.

Generally, the Whisper model is designed to run on GPUs. The recommended minimum GPU memory for running Whisper is 8 GB, but it can utilize more memory if available.

Keep in mind that processing large amounts of data or handling many requests simultaneously may require more GPU memory and could affect performance. It’s best to test your specific use case with different settings and monitor memory usage to find the optimal configuration.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

The Jupyter notebook titled [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) shows how to use the Microsoft Phi 3 Mini 4K instruct demo to generate text from audio or written input. The notebook defines several functions:

1. `tts_file_name(text)`: Generates a file name based on the input text for saving the generated audio file.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Uses the Edge TTS API to create an audio file from a list of text chunks. The inputs are the list of chunks, speech rate, voice name, and the output path for saving the audio.
3. `talk(input_text)`: Generates an audio file using the Edge TTS API and saves it with a random file name in the /content/audio directory. The input is the text to convert to speech.
4. `run_text_prompt(message, chat_history)`: Uses the Microsoft Phi 3 Mini 4K instruct demo to generate an audio file from a text message and adds it to the chat history.
5. `run_audio_prompt(audio, chat_history)`: Converts an audio file to text using the Whisper model API, then passes it to `run_text_prompt()`.
6. The code launches a Gradio app that lets users interact with the Phi 3 Mini 4K instruct demo by typing messages or uploading audio files. The output is shown as a text message within the app.

## Troubleshooting

Installing Cuda GPU drivers

1. Make sure your Linux system is up to date

    ```bash
    sudo apt update
    ```

2. Install Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Register the CUDA driver location

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Check Nvidia GPU memory size (12GB of GPU memory required)

    ```bash
    nvidia-smi
    ```

5. Clear Cache: If you’re using PyTorch, call torch.cuda.empty_cache() to free all unused cached memory so other GPU applications can use it

    ```python
    torch.cuda.empty_cache() 
    ```

6. Check Nvidia CUDA installation

    ```bash
    nvcc --version
    ```

7. Follow these steps to create a Hugging Face token:

    - Go to the [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Click **New token**.
    - Enter the project **Name** you want to use.
    - Set **Type** to **Write**.

> **Note**
>
> If you see the following error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> To fix this, run the following command in your terminal:
>
> ```bash
> sudo ldconfig
> ```

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.