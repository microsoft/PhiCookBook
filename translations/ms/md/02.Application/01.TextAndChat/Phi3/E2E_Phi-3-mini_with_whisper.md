<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:33:05+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ms"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

The Interactive Phi 3 Mini 4K Instruct Chatbot is a tool that lets users engage with the Microsoft Phi 3 Mini 4K instruct demo using either text or audio input. This chatbot can be used for various tasks, including translation, weather updates, and general information retrieval.

### Getting Started

To start using this chatbot, just follow these steps:

1. Open the [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) notebook.
2. In the notebook’s main window, you’ll find a chatbox interface with a text input field and a "Send" button.
3. To interact with the chatbot via text, type your message into the input box and click "Send." The chatbot will reply with an audio file that can be played directly inside the notebook.

**Note**: This tool requires a GPU and access to the Microsoft Phi-3 and OpenAI Whisper models, which handle speech recognition and translation.

### GPU Requirements

To run this demo, you need at least 12GB of GPU memory.

The memory needed to run the **Microsoft-Phi-3-Mini-4K instruct** demo on a GPU depends on factors like input data size (audio or text), the translation language, model speed, and available GPU memory.

Generally, the Whisper model is designed for GPU use. The recommended minimum GPU memory for Whisper is 8 GB, but it can work with larger memory if available.

Keep in mind that processing large amounts of data or many requests may require more GPU memory and might affect performance. It’s best to test your scenario with different settings and monitor memory usage to find the optimal configuration for your needs.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

The Jupyter notebook titled [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) shows how to use the Microsoft Phi 3 Mini 4K instruct Demo to generate text from audio or written input. The notebook includes several functions:

1. `tts_file_name(text)`: Generates a filename based on the input text for saving the generated audio file.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Uses the Edge TTS API to create an audio file from a list of text chunks. Inputs include the chunk list, speech rate, voice name, and output path to save the audio.
1. `talk(input_text)`: Creates an audio file via the Edge TTS API and saves it with a random filename in the /content/audio directory. The input is the text to convert to speech.
1. `run_text_prompt(message, chat_history)`: Uses the Microsoft Phi 3 Mini 4K instruct demo to generate an audio file from a message and appends it to the chat history.
1. `run_audio_prompt(audio, chat_history)`: Converts an audio file to text using the Whisper model API and passes the result to `run_text_prompt()`.
1. The code launches a Gradio app allowing users to interact with the Phi 3 Mini 4K instruct demo by typing messages or uploading audio files. The response is shown as text within the app.

## Troubleshooting

Installing Cuda GPU drivers

1. Make sure your Linux system is up to date

    ```bash
    sudo apt update
    ```

1. Install Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Register the cuda driver location

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Check Nvidia GPU memory size (12GB GPU memory required)

    ```bash
    nvidia-smi
    ```

1. Clear Cache: If using PyTorch, call torch.cuda.empty_cache() to free unused cached memory so other GPU applications can use it

    ```python
    torch.cuda.empty_cache() 
    ```

1. Check Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Follow these steps to create a Hugging Face token:

    - Go to the [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Click **New token**.
    - Enter the project **Name** you want.
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

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau tafsiran yang timbul daripada penggunaan terjemahan ini.