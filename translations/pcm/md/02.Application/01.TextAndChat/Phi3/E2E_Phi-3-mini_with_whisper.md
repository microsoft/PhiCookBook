<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-16T20:05:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "pcm"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot wit Whisper

## Overview

Di Interactive Phi 3 Mini 4K Instruct Chatbot na tool wey dey allow users to dey interact wit Microsoft Phi 3 Mini 4K instruct demo using text or audio input. Di chatbot fit use for plenty tins, like translation, weather updates, and general information gathering.

### Getting Started

To use dis chatbot, just follow dis instructions:

1. Open new [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. For di main window of di notebook, you go see chatbox interface with text input box and "Send" button.
3. To use di text-based chatbot, just type your message for inside di text input box and click di "Send" button. Di chatbot go respond wit audio file wey you fit play directly from inside di notebook.

**Note**: Dis tool need GPU and access to Microsoft Phi-3 and OpenAI Whisper models, wey dem dey use for speech recognition and translation.

### GPU Requirements

To run dis demo, you need 12Gb of GPU memory.

Di memory wey you go need to run **Microsoft-Phi-3-Mini-4K instruct** demo for GPU go depend on plenty tins, like how big di input data be (audio or text), di language wey you dey use for translation, di speed of di model, and how much memory dey available for di GPU.

Normally, di Whisper model design to run on GPUs. Di minimum GPU memory wey dem recommend for running Whisper model na 8 GB, but e fit handle bigger memory if e need am.

E important to know say if you dey run plenty data or too much requests on di model, e fit require more GPU memory and/or e fit cause performance wahala. E good make you test your use case wit different settings and dey watch di memory use to find di best settings for your own needs.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot wit Whisper

Di jupyter notebook wey dem call [Interactive Phi 3 Mini 4K Instruct Chatbot wit Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) show how to use Microsoft Phi 3 Mini 4K instruct Demo to generate text from audio or written text input. Di notebook define plenty functions:

1. `tts_file_name(text)`: Dis function go create file name based on di input text to save di generated audio file.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Dis function dey use Edge TTS API to create audio file from list of text chunks. Di input parameters na di list of chunks, speech rate, voice name, and di output path to save di generated audio file.
1. `talk(input_text)`: Dis function go generate audio file using Edge TTS API and save am to random file name inside /content/audio directory. Di input parameter na di text wey you want make dem convert to speech.
1. `run_text_prompt(message, chat_history)`: Dis function dey use Microsoft Phi 3 Mini 4K instruct demo to generate audio file from message input and e dey add am to chat history.
1. `run_audio_prompt(audio, chat_history)`: Dis function dey convert audio file to text using Whisper model API then e pass am go `run_text_prompt()` function.
1. Di code go run Gradio app wey allow users to interact wit di Phi 3 Mini 4K instruct demo by typing message or uploading audio files. Di output go show as text message inside di app.

## Troubleshooting

Installing Cuda GPU drivers

1. Make sure say your Linux application dey up to date

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

1. Check Nvidia GPU memory size (You need 12GB of GPU Memory)

    ```bash
    nvidia-smi
    ```

1. Empty Cache: If you dey use PyTorch, you fit call torch.cuda.empty_cache() to free all di unused cached memory make other GPU apps fit use am

    ```python
    torch.cuda.empty_cache() 
    ```

1. Check Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Do dis tins to create Hugging Face token.

    - Go [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Choose **New token**.
    - Enter di project **Name** wey you want use.
    - Choose **Type** to **Write**.

> [!NOTE]
>
> If you see dis error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> To fix dis, type dis command for inside your terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg sabi say automated translation fit get mistake or no too correct. Di original dokument for im own language na di correct one wey you suppose trust pass. If na important information, better make human professional translate am. We no go responsible if anybody missunderstand or misinterpret tins wey dem see from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->