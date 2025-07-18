<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:21:24+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "tl"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Pangkalahatang-ideya

Ang Interactive Phi 3 Mini 4K Instruct Chatbot ay isang kasangkapan na nagpapahintulot sa mga gumagamit na makipag-ugnayan sa Microsoft Phi 3 Mini 4K instruct demo gamit ang text o audio input. Maaaring gamitin ang chatbot para sa iba't ibang gawain, tulad ng pagsasalin, pag-update ng panahon, at pangkalahatang pangangalap ng impormasyon.

### Pagsisimula

Para magamit ang chatbot na ito, sundin lamang ang mga tagubiling ito:

1. Buksan ang bagong [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Sa pangunahing bintana ng notebook, makikita mo ang chatbox interface na may kahon para sa text input at isang "Send" na button.
3. Para gamitin ang text-based chatbot, i-type lang ang iyong mensahe sa text input box at i-click ang "Send" na button. Tutugon ang chatbot gamit ang isang audio file na maaaring patugtugin direkta mula sa loob ng notebook.

**Note**: Nangangailangan ang kasangkapang ito ng GPU at access sa Microsoft Phi-3 at OpenAI Whisper models, na ginagamit para sa speech recognition at pagsasalin.

### Mga Kinakailangan sa GPU

Para patakbuhin ang demo na ito, kailangan mo ng 12Gb na memorya ng GPU.

Ang pangangailangan sa memorya para sa pagpapatakbo ng **Microsoft-Phi-3-Mini-4K instruct** demo sa GPU ay nakadepende sa ilang mga salik, tulad ng laki ng input data (audio o text), ang wikang gagamitin para sa pagsasalin, bilis ng modelo, at ang available na memorya sa GPU.

Sa pangkalahatan, ang Whisper model ay dinisenyo para tumakbo sa mga GPU. Ang inirerekomendang minimum na memorya ng GPU para sa pagpapatakbo ng Whisper model ay 8 GB, ngunit kaya nitong hawakan ang mas malaking memorya kung kinakailangan.

Mahalagang tandaan na ang pagpapatakbo ng malaking dami ng data o mataas na bilang ng mga request sa modelo ay maaaring mangailangan ng mas maraming memorya ng GPU at/o magdulot ng mga isyu sa performance. Inirerekomenda na subukan ang iyong kaso gamit ang iba't ibang mga configuration at bantayan ang paggamit ng memorya upang matukoy ang pinakamainam na settings para sa iyong partikular na pangangailangan.

## E2E Sample para sa Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

Ipinapakita ng jupyter notebook na pinamagatang [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) kung paano gamitin ang Microsoft Phi 3 Mini 4K instruct Demo para gumawa ng text mula sa audio o nakasulat na input na teksto. Nagde-define ang notebook ng ilang mga function:

1. `tts_file_name(text)`: Gumagawa ang function na ito ng pangalan ng file base sa input na teksto para sa pag-save ng nagawang audio file.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ginagamit ng function na ito ang Edge TTS API para gumawa ng audio file mula sa listahan ng mga bahagi ng input na teksto. Ang mga input parameter ay ang listahan ng mga bahagi, bilis ng pagsasalita, pangalan ng boses, at ang output path para sa pag-save ng nagawang audio file.
1. `talk(input_text)`: Gumagawa ang function na ito ng audio file gamit ang Edge TTS API at sine-save ito sa isang random na pangalan ng file sa /content/audio directory. Ang input parameter ay ang teksto na iko-convert sa pagsasalita.
1. `run_text_prompt(message, chat_history)`: Ginagamit ng function na ito ang Microsoft Phi 3 Mini 4K instruct demo para gumawa ng audio file mula sa input na mensahe at idinadagdag ito sa chat history.
1. `run_audio_prompt(audio, chat_history)`: Kinokonvert ng function na ito ang audio file sa teksto gamit ang Whisper model API at ipinapasa ito sa `run_text_prompt()` function.
1. Pinapalabas ng code ang isang Gradio app na nagpapahintulot sa mga gumagamit na makipag-ugnayan sa Phi 3 Mini 4K instruct demo sa pamamagitan ng pagta-type ng mga mensahe o pag-upload ng mga audio file. Ipinapakita ang output bilang text message sa loob ng app.

## Pag-aayos ng Problema

Pag-install ng Cuda GPU drivers

1. Siguraduhing updated ang iyong Linux application

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

1. Pagsusuri ng laki ng Nvidia GPU memory (Kinakailangan 12GB na GPU Memory)

    ```bash
    nvidia-smi
    ```

1. Pag-empty ng Cache: Kung gumagamit ka ng PyTorch, maaari mong tawagin ang torch.cuda.empty_cache() para palayain ang lahat ng hindi nagagamit na cached memory upang magamit ito ng ibang GPU applications

    ```python
    torch.cuda.empty_cache() 
    ```

1. Pagsusuri ng Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Gawin ang mga sumusunod na hakbang para gumawa ng Hugging Face token.

    - Pumunta sa [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Piliin ang **New token**.
    - Ilagay ang pangalan ng proyekto na nais mong gamitin.
    - Piliin ang **Type** bilang **Write**.

> **Note**
>
> Kung makatagpo ka ng sumusunod na error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para malutas ito, i-type ang sumusunod na command sa loob ng iyong terminal.
>
> ```bash
> sudo ldconfig
> ```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.