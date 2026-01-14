<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:54:02+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "tl"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

Ang Interactive Phi 3 Mini 4K Instruct Chatbot ay isang kasangkapan na nagpapahintulot sa mga gumagamit na makipag-ugnayan sa Microsoft Phi 3 Mini 4K instruct demo gamit ang teksto o input ng audio. Ang chatbot ay maaaring gamitin para sa iba't ibang gawain, tulad ng pagsasalin, mga update sa panahon, at pangkalahatang pagkolekta ng impormasyon.

### Getting Started

Upang magamit ang chatbot na ito, sundin lamang ang mga tagubiling ito:

1. Buksan ang isang bagong [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Sa pangunahing window ng notebook, makikita mo ang isang chatbox interface na may kahon para sa input ng teksto at isang "Send" na pindutan.
3. Upang gamitin ang text-based chatbot, i-type lamang ang iyong mensahe sa input box para sa teksto at i-click ang "Send" na pindutan. Tutugon ang chatbot ng isang audio file na maaaring patugtugin nang direkta mula sa loob ng notebook.

**Note**: Nangangailangan ang kasangkapang ito ng GPU at access sa Microsoft Phi-3 at OpenAI Whisper models, na ginagamit para sa speech recognition at pagsasalin.

### GPU Requirements

Upang patakbuhin ang demo na ito kailangan mo ng 12Gb ng memorya sa GPU.

Ang pangangailangan sa memorya para sa pagpapatakbo ng **Microsoft-Phi-3-Mini-4K instruct** demo sa isang GPU ay depende sa ilang mga salik, tulad ng laki ng input data (audio o teksto), ang wikang gagamitin para sa pagsasalin, ang bilis ng modelo, at ang available na memorya sa GPU.

Sa pangkalahatan, ang Whisper model ay dinisenyo upang patakbuhin sa mga GPU. Ang inirerekomendang minimum na halaga ng memorya sa GPU para sa pagpapatakbo ng Whisper model ay 8 GB, ngunit kaya nitong hawakan ang mas malaking halaga ng memorya kung kinakailangan.

Mahalagang tandaan na ang pagpapatakbo ng malaking dami ng data o mataas na bilang ng mga request sa modelo ay maaaring mangailangan ng mas maraming memorya sa GPU at/o maaaring magdulot ng mga isyu sa performance. Inirerekomenda na subukan ang iyong kaso ng paggamit sa iba’t ibang mga configuration at subaybayan ang paggamit ng memorya upang matukoy ang pinakamainam na mga setting para sa iyong partikular na pangangailangan.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

Ang jupyter notebook na pinamagatang [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ay nagpapakita kung paano gamitin ang Microsoft Phi 3 Mini 4K instruct Demo para bumuo ng teksto mula sa audio o nakasulat na input na teksto Ang notebook ay nagdedeklara ng ilang mga function:

1. `tts_file_name(text)`: Ang function na ito ay bumubuo ng pangalan ng file base sa input na teksto para sa pag-iimbak ng nagawang audio file.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ang function na ito ay gumagamit ng Edge TTS API upang bumuo ng audio file mula sa listahan ng mga bahagi ng input na teksto. Ang mga input na parameter ay ang listahan ng mga bahagi, ang bilis ng pagsasalita, ang pangalan ng boses, at ang landas ng output para i-save ang nagawang audio file.
1. `talk(input_text)`: Ang function na ito ay lumilikha ng audio file gamit ang Edge TTS API at sine-save ito sa isang random na pangalan ng file sa direktoryong /content/audio. Ang input parameter ay ang teksto na iko-convert sa pagsasalita.
1. `run_text_prompt(message, chat_history)`: Ang function na ito ay gumagamit ng Microsoft Phi 3 Mini 4K instruct demo upang gumawa ng audio file mula sa input na mensahe at idinadagdag ito sa kasaysayan ng chat.
1. `run_audio_prompt(audio, chat_history)`: Ang function na ito ay nagko-convert ng audio file sa teksto gamit ang Whisper model API at ipapasa ito sa `run_text_prompt()` na function.
1. Ang code ay naglunsad ng isang Gradio app na nagpapahintulot sa mga gumagamit na makipag-ugnayan sa Phi 3 Mini 4K instruct demo sa pamamagitan ng pag-type ng mga mensahe o pag-upload ng audio files. Ang output ay ipinapakita bilang isang text message sa loob ng app.

## Troubleshooting

Installing Cuda GPU drivers

1. Siguraduhing ang iyong Linux application ay na-update

    ```bash
    sudo apt update
    ```

1. I-install ang Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Irehistro ang lokasyon ng cuda driver

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Suriin ang laki ng Nvidia GPU memory (Kinakailangan 12GB ng GPU Memory)

    ```bash
    nvidia-smi
    ```

1. Walang laman na Cache: Kung gumagamit ka ng PyTorch, maaari mong tawagin ang torch.cuda.empty_cache() upang pakawalan ang lahat ng hindi nagagamit na naka-cache na memorya para magamit ng ibang mga aplikasyon ng GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Suriin ang Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Gawin ang sumusunod na mga hakbang upang gumawa ng Hugging Face token.

    - Pumunta sa [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Piliin ang **New token**.
    - Ipasok ang pangalan ng proyekto (**Name**) na nais mong gamitin.
    - Piliin ang **Type** bilang **Write**.

> [!NOTE]
>
> Kung makatagpo ka ng sumusunod na error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Upang malutas ito, i-type ang sumusunod na utos sa loob ng iyong terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami na maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na pangunahing sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->