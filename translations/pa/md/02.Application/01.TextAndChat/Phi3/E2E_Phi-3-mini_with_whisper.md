<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:17:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "pa"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## ਝਲਕ

Interactive Phi 3 Mini 4K Instruct Chatbot ਇੱਕ ਐਸਾ ਸੰਦ ਹੈ ਜੋ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ Microsoft Phi 3 Mini 4K instruct ਡੈਮੋ ਨਾਲ ਟੈਕਸਟ ਜਾਂ ਆਡੀਓ ਇਨਪੁੱਟ ਰਾਹੀਂ ਇੰਟਰਐਕਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਚੈਟਬੋਟ ਅਨੁਵਾਦ, ਮੌਸਮ ਦੀ ਜਾਣਕਾਰੀ ਅਤੇ ਆਮ ਜਾਣਕਾਰੀ ਇਕੱਠੀ ਕਰਨ ਵਰਗੇ ਕਈ ਕੰਮਾਂ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

### ਸ਼ੁਰੂਆਤ

ਇਸ ਚੈਟਬੋਟ ਨੂੰ ਵਰਤਣ ਲਈ, ਸਿਰਫ਼ ਹੇਠਾਂ ਦਿੱਤੇ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ:

1. ਇੱਕ ਨਵਾਂ [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ਖੋਲ੍ਹੋ
2. ਨੋਟਬੁੱਕ ਦੀ ਮੁੱਖ ਵਿੰਡੋ ਵਿੱਚ, ਤੁਸੀਂ ਇੱਕ ਚੈਟਬਾਕਸ ਇੰਟਰਫੇਸ ਦੇਖੋਗੇ ਜਿਸ ਵਿੱਚ ਟੈਕਸਟ ਇਨਪੁੱਟ ਬਾਕਸ ਅਤੇ "Send" ਬਟਨ ਹੈ।
3. ਟੈਕਸਟ-ਆਧਾਰਿਤ ਚੈਟਬੋਟ ਵਰਤਣ ਲਈ, ਸਿਰਫ਼ ਆਪਣਾ ਸੁਨੇਹਾ ਟੈਕਸਟ ਇਨਪੁੱਟ ਬਾਕਸ ਵਿੱਚ ਲਿਖੋ ਅਤੇ "Send" ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਚੈਟਬੋਟ ਇੱਕ ਆਡੀਓ ਫਾਈਲ ਨਾਲ ਜਵਾਬ ਦੇਵੇਗਾ ਜੋ ਸਿੱਧਾ ਨੋਟਬੁੱਕ ਵਿੱਚੋਂ ਚਲਾਈ ਜਾ ਸਕਦੀ ਹੈ।

**Note**: ਇਸ ਸੰਦ ਲਈ GPU ਅਤੇ Microsoft Phi-3 ਅਤੇ OpenAI Whisper ਮਾਡਲਾਂ ਦੀ ਪਹੁੰਚ ਲੋੜੀਂਦੀ ਹੈ, ਜੋ ਬੋਲਚਾਲ ਦੀ ਪਛਾਣ ਅਤੇ ਅਨੁਵਾਦ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

### GPU ਦੀਆਂ ਲੋੜਾਂ

ਇਸ ਡੈਮੋ ਨੂੰ ਚਲਾਉਣ ਲਈ ਤੁਹਾਨੂੰ 12GB GPU ਮੈਮੋਰੀ ਦੀ ਲੋੜ ਹੈ।

**Microsoft-Phi-3-Mini-4K instruct** ਡੈਮੋ ਨੂੰ GPU 'ਤੇ ਚਲਾਉਣ ਲਈ ਮੈਮੋਰੀ ਦੀ ਲੋੜ ਕਈ ਗੱਲਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਇਨਪੁੱਟ ਡੇਟਾ (ਆਡੀਓ ਜਾਂ ਟੈਕਸਟ) ਦਾ ਆਕਾਰ, ਅਨੁਵਾਦ ਲਈ ਵਰਤੀ ਭਾਸ਼ਾ, ਮਾਡਲ ਦੀ ਗਤੀ ਅਤੇ GPU ਉੱਤੇ ਉਪਲਬਧ ਮੈਮੋਰੀ।

ਆਮ ਤੌਰ 'ਤੇ, Whisper ਮਾਡਲ GPU 'ਤੇ ਚਲਾਉਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। Whisper ਮਾਡਲ ਚਲਾਉਣ ਲਈ ਘੱਟੋ-ਘੱਟ 8GB GPU ਮੈਮੋਰੀ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਪਰ ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਵੱਡੀ ਮੈਮੋਰੀ ਵੀ ਸੰਭਾਲ ਸਕਦਾ ਹੈ।

ਇਹ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਵੱਡੀ ਮਾਤਰਾ ਵਿੱਚ ਡੇਟਾ ਜਾਂ ਬਹੁਤ ਸਾਰੇ ਰਿਕਵੇਸਟ ਮਾਡਲ 'ਤੇ ਚਲਾਉਣ ਨਾਲ ਵੱਧ GPU ਮੈਮੋਰੀ ਦੀ ਲੋੜ ਪੈ ਸਕਦੀ ਹੈ ਜਾਂ ਪ੍ਰਦਰਸ਼ਨ ਵਿੱਚ ਸਮੱਸਿਆਵਾਂ ਆ ਸਕਦੀਆਂ ਹਨ। ਆਪਣੀ ਵਰਤੋਂ ਦੇ ਕੇਸ ਨੂੰ ਵੱਖ-ਵੱਖ ਸੰਰਚਨਾਵਾਂ ਨਾਲ ਟੈਸਟ ਕਰਨਾ ਅਤੇ ਮੈਮੋਰੀ ਦੀ ਵਰਤੋਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਖਾਸ ਜ਼ਰੂਰਤਾਂ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਸੈਟਿੰਗਜ਼ ਮਿਲ ਸਕਣ।

## E2E ਨਮੂਨਾ Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper ਲਈ

ਜੁਪਾਈਟਰ ਨੋਟਬੁੱਕ ਜਿਸਦਾ ਸਿਰਲੇਖ [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ਹੈ, ਇਹ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ Microsoft Phi 3 Mini 4K instruct ਡੈਮੋ ਨੂੰ ਆਡੀਓ ਜਾਂ ਲਿਖਤ ਟੈਕਸਟ ਇਨਪੁੱਟ ਤੋਂ ਟੈਕਸਟ ਬਣਾਉਣ ਲਈ ਕਿਵੇਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਨੋਟਬੁੱਕ ਵਿੱਚ ਕਈ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਗਏ ਹਨ:

1. `tts_file_name(text)`: ਇਹ ਫੰਕਸ਼ਨ ਇਨਪੁੱਟ ਟੈਕਸਟ ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ ਫਾਈਲ ਨਾਮ ਬਣਾਉਂਦਾ ਹੈ ਤਾਂ ਜੋ ਬਣਾਈ ਗਈ ਆਡੀਓ ਫਾਈਲ ਸੇਵ ਕੀਤੀ ਜਾ ਸਕੇ।
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: ਇਹ ਫੰਕਸ਼ਨ Edge TTS API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਟੈਕਸਟ ਦੇ ਟੁਕੜਿਆਂ ਦੀ ਸੂਚੀ ਤੋਂ ਆਡੀਓ ਫਾਈਲ ਬਣਾਉਂਦਾ ਹੈ। ਇਨਪੁੱਟ ਪੈਰਾਮੀਟਰ ਹਨ ਟੁਕੜਿਆਂ ਦੀ ਸੂਚੀ, ਬੋਲਣ ਦੀ ਗਤੀ, ਆਵਾਜ਼ ਦਾ ਨਾਮ ਅਤੇ ਬਣਾਈ ਗਈ ਆਡੀਓ ਫਾਈਲ ਸੇਵ ਕਰਨ ਲਈ ਰਾਹ।
1. `talk(input_text)`: ਇਹ ਫੰਕਸ਼ਨ Edge TTS API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਫਾਈਲ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ /content/audio ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ ਰੈਂਡਮ ਫਾਈਲ ਨਾਮ ਨਾਲ ਸੇਵ ਕਰਦਾ ਹੈ। ਇਨਪੁੱਟ ਪੈਰਾਮੀਟਰ ਬੋਲਣ ਲਈ ਟੈਕਸਟ ਹੈ।
1. `run_text_prompt(message, chat_history)`: ਇਹ ਫੰਕਸ਼ਨ Microsoft Phi 3 Mini 4K instruct ਡੈਮੋ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੁਨੇਹੇ ਤੋਂ ਆਡੀਓ ਫਾਈਲ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਇਸਨੂੰ ਚੈਟ ਇਤਿਹਾਸ ਵਿੱਚ ਜੋੜਦਾ ਹੈ।
1. `run_audio_prompt(audio, chat_history)`: ਇਹ ਫੰਕਸ਼ਨ Whisper ਮਾਡਲ API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਫਾਈਲ ਨੂੰ ਟੈਕਸਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਅਤੇ ਇਸਨੂੰ `run_text_prompt()` ਫੰਕਸ਼ਨ ਨੂੰ ਭੇਜਦਾ ਹੈ।
1. ਕੋਡ ਇੱਕ Gradio ਐਪ ਲਾਂਚ ਕਰਦਾ ਹੈ ਜੋ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ Phi 3 Mini 4K instruct ਡੈਮੋ ਨਾਲ ਸੁਨੇਹੇ ਲਿਖ ਕੇ ਜਾਂ ਆਡੀਓ ਫਾਈਲਾਂ ਅਪਲੋਡ ਕਰਕੇ ਇੰਟਰਐਕਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਨਤੀਜਾ ਐਪ ਵਿੱਚ ਟੈਕਸਟ ਸੁਨੇਹੇ ਵਜੋਂ ਦਿਖਾਇਆ ਜਾਂਦਾ ਹੈ।

## ਸਮੱਸਿਆ ਨਿਵਾਰਣ

Cuda GPU ਡਰਾਈਵਰਾਂ ਦੀ ਇੰਸਟਾਲੇਸ਼ਨ

1. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡਾ Linux ਐਪਲੀਕੇਸ਼ਨ ਅਪ-ਟੂ-ਡੇਟ ਹੈ

    ```bash
    sudo apt update
    ```

1. Cuda ਡਰਾਈਵਰ ਇੰਸਟਾਲ ਕਰੋ

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. cuda ਡਰਾਈਵਰ ਦੀ ਸਥਿਤੀ ਰਜਿਸਟਰ ਕਰੋ

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU ਮੈਮੋਰੀ ਦਾ ਆਕਾਰ ਚੈੱਕ ਕਰੋ (ਲੋੜੀਂਦਾ 12GB GPU ਮੈਮੋਰੀ)

    ```bash
    nvidia-smi
    ```

1. ਖਾਲੀ ਕੈਸ਼: ਜੇ ਤੁਸੀਂ PyTorch ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ torch.cuda.empty_cache() ਕਾਲ ਕਰਕੇ ਸਾਰੀ ਬੇਕਾਰ ਕੈਸ਼ ਕੀਤੀ ਮੈਮੋਰੀ ਛੱਡ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਹੋਰ GPU ਐਪਲੀਕੇਸ਼ਨਾਂ ਵੱਲੋਂ ਵਰਤੀ ਜਾ ਸਕੇ

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda ਦੀ ਜਾਂਚ ਕਰੋ

    ```bash
    nvcc --version
    ```

1. Hugging Face ਟੋਕਨ ਬਣਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) 'ਤੇ ਜਾਓ।
    - **New token** ਚੁਣੋ।
    - ਪ੍ਰੋਜੈਕਟ ਦਾ **Name** ਦਰਜ ਕਰੋ ਜੋ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ।
    - **Type** ਨੂੰ **Write** ਚੁਣੋ।

> **Note**
>
> ਜੇ ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੀ ਗਲਤੀ ਆਵੇ:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> ਇਸ ਨੂੰ ਠੀਕ ਕਰਨ ਲਈ, ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਟਾਈਪ ਕਰੋ।
>
> ```bash
> sudo ldconfig
> ```

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।