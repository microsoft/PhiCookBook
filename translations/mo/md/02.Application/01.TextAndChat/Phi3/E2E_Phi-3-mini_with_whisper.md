<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f737bf207e1691cdc654535c48dd2df4",
  "translation_date": "2025-04-04T12:40:54+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-mini_with_whisper.md",
  "language_code": "mo"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

The Interactive Phi 3 Mini 4K Instruct Chatbot is a tool that enables users to interact with the Microsoft Phi 3 Mini 4K instruct demo using text or audio inputs. This chatbot can assist with various tasks, including translation, weather updates, and general information retrieval.

### Getting Started

Follow these steps to use the chatbot:

1. Open the [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) notebook.
2. In the notebook's main window, you'll find a chatbox interface with a text input field and a "Send" button.
3. To interact with the text-based chatbot, type your message in the input field and click "Send." The chatbot will reply with an audio file that you can play directly within the notebook.

**Note**: This tool requires a GPU and access to the Microsoft Phi-3 and OpenAI Whisper models, which are utilized for speech recognition and translation.

### GPU Requirements

You need a GPU with 12GB of memory to run this demo.

The memory needed for running the **Microsoft-Phi-3-Mini-4K instruct** demo depends on factors such as input size (audio or text), translation language, model speed, and available GPU memory.

The Whisper model is generally designed for GPU use. While 8GB of GPU memory is the recommended minimum, it can utilize more memory as needed.

Keep in mind that processing large datasets or handling high request volumes may require additional GPU memory and could impact performance. It's advisable to test your specific use case with different configurations and monitor memory usage to find the optimal setup.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

The Jupyter notebook titled [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrates how to use the Microsoft Phi 3 Mini 4K instruct demo to generate text from audio or written inputs. It includes several functions:

1. `tts_file_name(text)`: Generates a file name based on the input text for saving the generated audio file.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Uses the Edge TTS API to create an audio file from input text chunks. Parameters include the text chunks, speech rate, voice name, and output path for saving the audio file.
3. `talk(input_text)`: Generates an audio file using the Edge TTS API, saving it with a random file name in the /content/audio directory. The input parameter is the text to be converted into speech.
4. `run_text_prompt(message, chat_history)`: Uses the Microsoft Phi 3 Mini 4K instruct demo to create an audio file from a message input and adds it to the chat history.
5. `run_audio_prompt(audio, chat_history)`: Converts an audio file into text using the Whisper model API and sends it to the `run_text_prompt()` function.
6. The code launches a Gradio app that allows users to interact with the Phi 3 Mini 4K instruct demo by typing messages or uploading audio files. The app displays the output as text.

## Troubleshooting

Installing Cuda GPU drivers:

1. Ensure your Linux applications are up to date:

    ```bash
    sudo apt update
    ```

2. Install Cuda drivers:

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Register the Cuda driver location:

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Check Nvidia GPU memory size (12GB required):

    ```bash
    nvidia-smi
    ```

5. Empty Cache: If you're using PyTorch, call torch.cuda.empty_cache() to free unused cached memory for other GPU applications.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Check Nvidia Cuda:

    ```bash
    nvcc --version
    ```

7. Follow these steps to create a Hugging Face token:

    - Visit the [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Click **New token**.
    - Enter the project **Name**.
    - Select **Type** as **Write**.

> **Note**
>
> If you encounter the following error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Resolve it by typing this command in your terminal:
>
> ```bash
> sudo ldconfig
> ```

It seems like you are asking to translate the provided text into "mo," but it's unclear what "mo" refers to. Could you clarify whether "mo" is a specific language (e.g., Maori, Montenegrin, or something else) or if you mean something else entirely?