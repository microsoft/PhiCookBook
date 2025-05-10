<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:33:15+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "tl"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

Ang Interactive Phi 3 Mini 4K Instruct Chatbot ay isang tool na nagpapahintulot sa mga user na makipag-ugnayan sa Microsoft Phi 3 Mini 4K instruct demo gamit ang text o audio input. Puwedeng gamitin ang chatbot para sa iba't ibang gawain tulad ng pagsasalin, pagkuha ng update sa panahon, at pangkalahatang pagkuha ng impormasyon.

### Getting Started

Para magamit ang chatbot na ito, sundin lang ang mga hakbang na ito:

1. Buksan ang bagong [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Sa pangunahing window ng notebook, makikita mo ang chatbox interface na may text input box at isang "Send" button.
3. Para gamitin ang text-based chatbot, i-type lang ang iyong mensahe sa text input box at i-click ang "Send" button. Sasagutin ng chatbot ang iyong mensahe gamit ang isang audio file na maaaring i-play direkta mula sa loob ng notebook.

**Note**: Nangangailangan ang tool na ito ng GPU at access sa Microsoft Phi-3 at OpenAI Whisper models, na ginagamit para sa speech recognition at pagsasalin.

### GPU Requirements

Para patakbuhin ang demo na ito, kailangan mo ng 12Gb na GPU memory.

Ang pangangailangan sa memory para sa pagpapatakbo ng **Microsoft-Phi-3-Mini-4K instruct** demo sa GPU ay nakadepende sa ilang mga bagay, tulad ng laki ng input data (audio o text), lengguwaheng gagamitin sa pagsasalin, bilis ng model, at ang available na memorya sa GPU.

Karaniwan, ang Whisper model ay ginawa para tumakbo sa mga GPU. Ang minimum na inirerekomendang GPU memory para patakbuhin ang Whisper model ay 8 GB, pero kaya nitong gumamit ng mas malaking memorya kung kinakailangan.

Mahalagang tandaan na kapag marami ang data o dami ng requests sa model, maaaring kailanganin ng mas malaking GPU memory at/o magdulot ng performance issues. Mainam na subukan ang iyong use case sa iba't ibang settings at bantayan ang paggamit ng memory para malaman ang pinakaangkop na configuration para sa iyong pangangailangan.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

Ang jupyter notebook na pinamagatang [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ay nagpapakita kung paano gamitin ang Microsoft Phi 3 Mini 4K instruct Demo para gumawa ng text mula sa audio o nakasulat na text input. Nagdedeklara ang notebook ng ilang functions:

1. `tts_file_name(text)`: Gumagawa ng file name base sa input text para i-save ang generated audio file.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ginagamit ang Edge TTS API para gumawa ng audio file mula sa listahan ng mga chunks ng input text. Ang mga input parameters ay ang listahan ng chunks, speech rate, pangalan ng boses, at output path para sa pag-save ng generated audio file.
1. `talk(input_text)`: Gumagawa ng audio file gamit ang Edge TTS API at sine-save ito sa random na file name sa /content/audio directory. Ang input parameter ay ang text na iko-convert sa speech.
1. `run_text_prompt(message, chat_history)`: Ginagamit ang Microsoft Phi 3 Mini 4K instruct demo para gumawa ng audio file mula sa mensaheng input at idinadagdag ito sa chat history.
1. `run_audio_prompt(audio, chat_history)`: Kinokonvert ang audio file sa text gamit ang Whisper model API at ipinapasa ito sa `run_text_prompt()` function.
1. Pinapalakad ng code ang isang Gradio app na nagpapahintulot sa mga user na makipag-ugnayan sa Phi 3 Mini 4K instruct demo sa pamamagitan ng pag-type ng mga mensahe o pag-upload ng audio files. Ipinapakita ang output bilang text message sa loob ng app.

## Troubleshooting

Installing Cuda GPU drivers

1. Siguraduhing updated ang iyong Linux application

    ```bash
    sudo apt update
    ```

1. I-install ang Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. I-register ang lokasyon ng cuda driver

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Pag-check ng Nvidia GPU memory size (Kinakailangan 12GB ng GPU Memory)

    ```bash
    nvidia-smi
    ```

1. Empty Cache: Kung gumagamit ka ng PyTorch, pwede mong tawagin ang torch.cuda.empty_cache() para i-release lahat ng unused cached memory para magamit ng ibang GPU applications

    ```python
    torch.cuda.empty_cache() 
    ```

1. Pag-check ng Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Gawin ang mga sumusunod para gumawa ng Hugging Face token.

    - Pumunta sa [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Piliin ang **New token**.
    - Ilagay ang pangalan ng project na gusto mong gamitin.
    - Piliin ang **Type** na **Write**.

> **Note**
>
> Kung makakita ka ng ganitong error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para ayusin ito, i-type ang sumusunod na command sa iyong terminal.
>
> ```bash
> sudo ldconfig
> ```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.