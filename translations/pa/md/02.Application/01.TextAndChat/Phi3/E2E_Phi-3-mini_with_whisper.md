<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:29:53+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "pa"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## ਝਲਕ

Interactive Phi 3 Mini 4K Instruct Chatbot ਇੱਕ ਟੂਲ ਹੈ ਜੋ ਯੂਜ਼ਰਾਂ ਨੂੰ Microsoft Phi 3 Mini 4K instruct ਡੈਮੋ ਨਾਲ ਟੈਕਸਟ ਜਾਂ ਆਡੀਓ ਇਨਪੁੱਟ ਰਾਹੀਂ ਇੰਟਰੈਕਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਚੈਟਬੋਟ ਅਨੁਵਾਦ, ਮੌਸਮ ਦੀ ਜਾਣਕਾਰੀ, ਅਤੇ ਆਮ ਜਾਣਕਾਰੀ ਇਕੱਠੀ ਕਰਨ ਵਰਗੀਆਂ ਕਈ ਕੰਮਾਂ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

### ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ

ਇਸ ਚੈਟਬੋਟ ਨੂੰ ਵਰਤਣ ਲਈ ਸਿਰਫ ਇਹਨਾਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ:

1. ਇੱਕ ਨਵਾਂ [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ਖੋਲ੍ਹੋ
2. ਨੋਟਬੁੱਕ ਦੀ ਮੁੱਖ ਵਿੰਡੋ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਇੱਕ ਚੈਟਬਾਕਸ ਇੰਟਰਫੇਸ ਦਿੱਸੇਗਾ ਜਿਸ ਵਿੱਚ ਟੈਕਸਟ ਇਨਪੁੱਟ ਬਾਕਸ ਅਤੇ "Send" ਬਟਨ ਹੋਵੇਗਾ।
3. ਟੈਕਸਟ-ਆਧਾਰਿਤ ਚੈਟਬੋਟ ਵਰਤਣ ਲਈ, ਸਿਰਫ ਆਪਣੇ ਸੁਨੇਹੇ ਨੂੰ ਟੈਕਸਟ ਇਨਪੁੱਟ ਬਾਕਸ ਵਿੱਚ ਟਾਈਪ ਕਰੋ ਅਤੇ "Send" ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਚੈਟਬੋਟ ਇੱਕ ਆਡੀਓ ਫਾਈਲ ਨਾਲ ਜਵਾਬ ਦੇਵੇਗਾ ਜੋ ਨੋਟਬੁੱਕ ਦੇ ਅੰਦਰੋਂ ਸਿੱਧਾ ਚਲਾਈ ਜਾ ਸਕਦੀ ਹੈ।

**Note**: ਇਸ ਟੂਲ ਲਈ GPU ਅਤੇ Microsoft Phi-3 ਅਤੇ OpenAI Whisper ਮਾਡਲਾਂ ਤੱਕ ਪਹੁੰਚ ਲੋੜੀਂਦੀ ਹੈ, ਜੋ ਕਿ ਸਪੀਚ ਰਿਕਗਨਿਸ਼ਨ ਅਤੇ ਅਨੁਵਾਦ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

### GPU ਦੀਆਂ ਲੋੜਾਂ

ਇਸ ਡੈਮੋ ਨੂੰ ਚਲਾਉਣ ਲਈ ਤੁਹਾਨੂੰ 12GB GPU ਮੈਮੋਰੀ ਦੀ ਲੋੜ ਹੈ।

Microsoft-Phi-3-Mini-4K instruct ਡੈਮੋ ਨੂੰ GPU 'ਤੇ ਚਲਾਉਣ ਲਈ ਮੈਮੋਰੀ ਦੀ ਲੋੜ ਕਈ ਕਾਰਕਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਇਨਪੁੱਟ ਡੇਟਾ (ਆਡੀਓ ਜਾਂ ਟੈਕਸਟ) ਦਾ ਆਕਾਰ, ਅਨੁਵਾਦ ਲਈ ਵਰਤੀ ਭਾਸ਼ਾ, ਮਾਡਲ ਦੀ ਗਤੀ, ਅਤੇ GPU 'ਤੇ ਉਪਲਬਧ ਮੈਮੋਰੀ।

ਆਮ ਤੌਰ 'ਤੇ, Whisper ਮਾਡਲ GPU 'ਤੇ ਚਲਾਉਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। Whisper ਮਾਡਲ ਚਲਾਉਣ ਲਈ ਘੱਟੋ-ਘੱਟ 8GB GPU ਮੈਮੋਰੀ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਪਰ ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਵੱਧ ਮੈਮੋਰੀ ਵੀ ਵਰਤੀ ਜਾ ਸਕਦੀ ਹੈ।

ਇਹ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਵੱਡੀ ਮਾਤਰਾ ਵਿੱਚ ਡੇਟਾ ਜਾਂ ਬਹੁਤ ਸਾਰੇ ਰਿਕਵੈਸਟ ਮਾਡਲ ਨੂੰ ਭੇਜੇ ਜਾਣ ਤੇ ਹੋਰ GPU ਮੈਮੋਰੀ ਦੀ ਲੋੜ ਪੈ ਸਕਦੀ ਹੈ ਜਾਂ ਪ੍ਰਦਰਸ਼ਨ 'ਤੇ ਅਸਰ ਪੈ ਸਕਦਾ ਹੈ। ਆਪਣੀ ਵਰਤੋਂ ਦੇ ਕੇਸ ਨੂੰ ਵੱਖ-ਵੱਖ ਸੰਰਚਨਾਵਾਂ ਨਾਲ ਟੈਸਟ ਕਰੋ ਅਤੇ ਮੈਮੋਰੀ ਦੀ ਵਰਤੋਂ 'ਤੇ ਨਜ਼ਰ ਰੱਖੋ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਖਾਸ ਜ਼ਰੂਰਤਾਂ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਸੈਟਿੰਗ ਮਿਲ ਸਕੇ।

## E2E ਸੈਂਪਲ Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper ਲਈ

ਜੁਪਾਈਟਰ ਨੋਟਬੁੱਕ ਜਿਸਦਾ ਸਿਰਲੇਖ [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ਹੈ, ਇਹ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ Microsoft Phi 3 Mini 4K instruct ਡੈਮੋ ਨੂੰ ਆਡੀਓ ਜਾਂ ਲਿਖਤੀ ਟੈਕਸਟ ਇਨਪੁੱਟ ਤੋਂ ਟੈਕਸਟ ਜਨਰੇਟ ਕਰਨ ਲਈ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ। ਨੋਟਬੁੱਕ ਵਿੱਚ ਕਈ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਗਏ ਹਨ:

1. `tts_file_name(text)`: ਇਹ ਫੰਕਸ਼ਨ ਇਨਪੁੱਟ ਟੈਕਸਟ ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ ਫਾਈਲ ਨਾਂ ਬਣਾਉਂਦਾ ਹੈ ਤਾਂ ਜੋ ਜਨਰੇਟ ਕੀਤੀ ਆਡੀਓ ਫਾਈਲ ਨੂੰ ਸੇਵ ਕੀਤਾ ਜਾ ਸਕੇ।
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: ਇਹ ਫੰਕਸ਼ਨ Edge TTS API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਟੈਕਸਟ ਦੇ ਟੁਕੜਿਆਂ ਦੀ ਸੂਚੀ ਤੋਂ ਆਡੀਓ ਫਾਈਲ ਬਣਾਉਂਦਾ ਹੈ। ਇਨਪੁੱਟ ਪੈਰਾਮੀਟਰ ਟੁਕੜਿਆਂ ਦੀ ਸੂਚੀ, ਬੋਲਣ ਦੀ ਰਫ਼ਤਾਰ, ਵੌਇਸ ਦਾ ਨਾਂ, ਅਤੇ ਆਡੀਓ ਫਾਈਲ ਸੇਵ ਕਰਨ ਲਈ ਆਉਟਪੁੱਟ ਪਾਥ ਹਨ।
1. `talk(input_text)`: ਇਹ ਫੰਕਸ਼ਨ Edge TTS API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਫਾਈਲ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਉਸਨੂੰ /content/audio ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ ਰੈਂਡਮ ਫਾਈਲ ਨਾਂ ਨਾਲ ਸੇਵ ਕਰਦਾ ਹੈ। ਇਨਪੁੱਟ ਪੈਰਾਮੀਟਰ ਬੋਲਣ ਲਈ ਟੈਕਸਟ ਹੈ।
1. `run_text_prompt(message, chat_history)`: ਇਹ ਫੰਕਸ਼ਨ Microsoft Phi 3 Mini 4K instruct ਡੈਮੋ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੁਨੇਹੇ ਤੋਂ ਆਡੀਓ ਫਾਈਲ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਚੈਟ ਇਤਿਹਾਸ ਵਿੱਚ ਜੋੜਦਾ ਹੈ।
1. `run_audio_prompt(audio, chat_history)`: ਇਹ ਫੰਕਸ਼ਨ Whisper ਮਾਡਲ API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਫਾਈਲ ਨੂੰ ਟੈਕਸਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਅਤੇ ਉਸਨੂੰ `run_text_prompt()` ਫੰਕਸ਼ਨ ਨੂੰ ਭੇਜਦਾ ਹੈ।
1. ਕੋਡ ਇੱਕ Gradio ਐਪ ਚਲਾਉਂਦਾ ਹੈ ਜੋ ਯੂਜ਼ਰਾਂ ਨੂੰ Phi 3 Mini 4K instruct ਡੈਮੋ ਨਾਲ ਸੁਨੇਹੇ ਟਾਈਪ ਕਰਨ ਜਾਂ ਆਡੀਓ ਫਾਈਲਾਂ ਅਪਲੋਡ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਨਤੀਜਾ ਐਪ ਵਿੱਚ ਟੈਕਸਟ ਸੁਨੇਹੇ ਵਜੋਂ ਦਿਖਾਇਆ ਜਾਂਦਾ ਹੈ।

## ਸਮੱਸਿਆ ਨਿਵਾਰਣ

Cuda GPU ਡਰਾਈਵਰ ਇੰਸਟਾਲ ਕਰਨਾ

1. ਆਪਣੇ Linux ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰੋ

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

1. ਕੈਸ਼ ਖਾਲੀ ਕਰੋ: ਜੇ ਤੁਸੀਂ PyTorch ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ torch.cuda.empty_cache() ਕਾਲ ਕਰਕੇ ਸਾਰੀ ਬੇਕਾਰ ਕੈਸ਼ ਕੀਤੀ ਮੈਮੋਰੀ ਖਾਲੀ ਕਰ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਹੋਰ GPU ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਵਰਤੀ ਜਾ ਸਕੇ

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda ਚੈੱਕ ਕਰੋ

    ```bash
    nvcc --version
    ```

1. Hugging Face ਟੋਕਨ ਬਣਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮ ਕਰੋ।

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) 'ਤੇ ਜਾਓ।
    - **New token** ਚੁਣੋ।
    - ਉਹ ਪ੍ਰੋਜੈਕਟ **Name** ਦਿਓ ਜੋ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ।
    - **Type** ਨੂੰ **Write** 'ਤੇ ਸੈੱਟ ਕਰੋ।

> **Note**
>
> ਜੇ ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੀ ਗਲਤੀ ਆਵੇ:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> ਇਸਨੂੰ ਠੀਕ ਕਰਨ ਲਈ, ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਟਾਈਪ ਕਰੋ।
>
> ```bash
> sudo ldconfig
> ```

**ਡਿਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।