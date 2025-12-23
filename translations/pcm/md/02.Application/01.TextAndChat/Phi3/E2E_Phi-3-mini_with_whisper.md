<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-12-21T21:12:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "pcm"
}
-->
# Interaktiv Phi 3 Mini 4K Instruct Chatbot wit Whisper

## Wetin E Be

Di Interactive Phi 3 Mini 4K Instruct Chatbot na tool wey allow users to interact wit di Microsoft Phi 3 Mini 4K instruct demo by text or audio input. Di chatbot fit use for different mata dem, like translation, weather updates, and general info gathering.

### Getting Started

To use dis chatbot, jus follow these instructions:

1. Open a new [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. For di main window of di notebook, you go see one chatbox interface wey get a text input box and a "Send" button.
3. To use di text-based chatbot, jus type your message into di text input box and click di "Send" button. Di chatbot go respond wit an audio file wey fit play directly from inside di notebook.

**Note**: Dis tool need GPU and access to di Microsoft Phi-3 and OpenAI Whisper models, wey dem dey use for speech recognition and translation.

### GPU Requirements

To run dis demo you need 12Gb of GPU memory.

Di memory requirements for running di **Microsoft-Phi-3-Mini-4K instruct** demo on a GPU go depend on several factors, like di size of di input data (audio or text), di language wey you dey translate, di speed of di model, and di memory wey dey available on di GPU.

In general, di Whisper model design to run on GPUs. Di recommended minimum amount of GPU memory for running di Whisper model na 8 GB, but e fit handle bigger amounts of memory if e necessary.

Make you sabi say if you dey run plenty data or many requests on di model, e fit require more GPU memory and/or e fit cause performance wahala. E better make you test your use case with different configurations and dey monitor di memory usage to know di best settings for your specific needs.

## E2E Sample for Interaktiv Phi 3 Mini 4K Instruct Chatbot wit Whisper

Di jupyter notebook wey title get [Interaktiv Phi 3 Mini 4K Instruct Chatbot wit Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) dey show how to use di Microsoft Phi 3 Mini 4K instruct Demo to generate text from audio or written text input. Di notebook define several functions:

1. `tts_file_name(text)`: Dis function dey generate a file name based on di input text for saving di generated audio file.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Dis function dey use di Edge TTS API to generate an audio file from a list of chunks of input text. Di input parameters na di list of chunks, di speech rate, di voice name, and di output path for saving di generated audio file.
1. `talk(input_text)`: Dis function dey generate an audio file by using di Edge TTS API and save am to a random file name in di /content/audio directory. Di input parameter na di input text wey go convert to speech.
1. `run_text_prompt(message, chat_history)`: Dis function dey use di Microsoft Phi 3 Mini 4K instruct demo to generate an audio file from a message input and e go append am to di chat history.
1. `run_audio_prompt(audio, chat_history)`: Dis function dey convert an audio file into text using di Whisper model API and then pass am to di `run_text_prompt()` function.
1. Di code go launch a Gradio app wey allow users to interact wit di Phi 3 Mini 4K instruct demo by either typing messages or uploading audio files. Di output go show as a text message inside di app.

## Troubleshooting

Installing Cuda GPU drivers

1. Make sure your Linux applications dey up to date

    ```bash
    sudo apt update
    ```

1. Install Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Register di cuda driver location

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Checking Nvidia GPU memory size (Required 12GB of GPU Memory)

    ```bash
    nvidia-smi
    ```

1. Empty Cache: If you dey use PyTorch, you fit call torch.cuda.empty_cache() to release all unused cached memory so dat other GPU applications fit use am

    ```python
    torch.cuda.empty_cache() 
    ```

1. Checking Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Perform di following tasks to create a Hugging Face token.

    - Go to di [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Choose **New token**.
    - Enter di project **Name** wey you wan use.
    - Select **Type** make e be **Write**.

> **Note**
>
> If you see dis error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> To fix am, type di following command inside your terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate with AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get mistakes or no too correct. Di original document wey dey im native language na di authoritative source. If na important/critical information, make you use professional human translator. We no go responsible for any misunderstanding or wrong interpretation wey fit result from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->