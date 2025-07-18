<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:21:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "sw"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Muhtasari

Interactive Phi 3 Mini 4K Instruct Chatbot ni chombo kinachowezesha watumiaji kuwasiliana na maonyesho ya Microsoft Phi 3 Mini 4K instruct kwa kutumia maandishi au sauti. Chatbot hii inaweza kutumika kwa kazi mbalimbali, kama vile tafsiri, taarifa za hali ya hewa, na ukusanyaji wa taarifa kwa ujumla.

### Kuanzia

Ili kutumia chatbot hii, fuata maelekezo haya:

1. Fungua [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Kwenye dirisha kuu la daftari, utaona kiolesura cha mazungumzo chenye kisanduku cha kuingiza maandishi na kitufe cha "Send".
3. Ili kutumia chatbot inayotumia maandishi, andika ujumbe wako kwenye kisanduku cha maandishi kisha bonyeza kitufe cha "Send". Chatbot itajibu kwa faili la sauti ambalo linaweza kusikilizwa moja kwa moja ndani ya daftari.

**Note**: Chombo hiki kinahitaji GPU na upatikanaji wa mifano ya Microsoft Phi-3 na OpenAI Whisper, inayotumika kwa utambuzi wa hotuba na tafsiri.

### Mahitaji ya GPU

Ili kuendesha maonyesho haya unahitaji kumbukumbu ya GPU ya 12GB.

Mahitaji ya kumbukumbu kwa kuendesha maonyesho ya **Microsoft-Phi-3-Mini-4K instruct** kwenye GPU yatategemea mambo kadhaa, kama ukubwa wa data ya kuingiza (sauti au maandishi), lugha inayotumika kwa tafsiri, kasi ya mfano, na kumbukumbu inayopatikana kwenye GPU.

Kwa ujumla, mfano wa Whisper umeundwa kuendeshwa kwenye GPUs. Kiasi kinachopendekezwa cha chini cha kumbukumbu ya GPU kwa kuendesha mfano wa Whisper ni 8 GB, lakini unaweza kushughulikia kiasi kikubwa zaidi cha kumbukumbu ikiwa inahitajika.

Ni muhimu kuelewa kuwa kuendesha data nyingi au maombi mengi kwa mfano kunaweza kuhitaji kumbukumbu zaidi ya GPU na/au kusababisha matatizo ya utendaji. Inapendekezwa kujaribu matumizi yako kwa usanidi tofauti na kufuatilia matumizi ya kumbukumbu ili kubaini mipangilio bora kwa mahitaji yako maalum.

## Mfano wa E2E kwa Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

Daftari la jupyter lenye kichwa [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) linaonyesha jinsi ya kutumia Microsoft Phi 3 Mini 4K instruct Demo kuzalisha maandishi kutoka kwa sauti au maandishi yaliyoandikwa. Daftari linafafanua kazi kadhaa:

1. `tts_file_name(text)`: Kazi hii huunda jina la faili kulingana na maandishi ya kuingiza kwa ajili ya kuhifadhi faili la sauti lililotengenezwa.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Kazi hii hutumia Edge TTS API kuzalisha faili la sauti kutoka kwa orodha ya vipande vya maandishi ya kuingiza. Vigezo vya kuingiza ni orodha ya vipande, kasi ya hotuba, jina la sauti, na njia ya kuhifadhi faili la sauti lililotengenezwa.
1. `talk(input_text)`: Kazi hii huzalisha faili la sauti kwa kutumia Edge TTS API na kuihifadhi kwa jina la faili la nasibu katika saraka ya /content/audio. Kigezo cha kuingiza ni maandishi yanayobadilishwa kuwa hotuba.
1. `run_text_prompt(message, chat_history)`: Kazi hii hutumia maonyesho ya Microsoft Phi 3 Mini 4K instruct kuzalisha faili la sauti kutoka kwa ujumbe wa kuingiza na kuiongeza kwenye historia ya mazungumzo.
1. `run_audio_prompt(audio, chat_history)`: Kazi hii hubadilisha faili la sauti kuwa maandishi kwa kutumia API ya mfano wa Whisper na kuipitia kwa kazi ya `run_text_prompt()`.
1. Msimbo unaanzisha app ya Gradio inayowezesha watumiaji kuwasiliana na maonyesho ya Phi 3 Mini 4K instruct kwa kuandika ujumbe au kupakia faili za sauti. Matokeo yanaonyeshwa kama ujumbe wa maandishi ndani ya app.

## Utatuzi wa Matatizo

Kusakinisha madereva ya Cuda GPU

1. Hakikisha programu zako za Linux zimesasishwa

    ```bash
    sudo apt update
    ```

1. Sakinisha Madereva ya Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Sajili eneo la dereva wa cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kagua ukubwa wa kumbukumbu ya Nvidia GPU (Inahitajika kumbukumbu ya GPU ya 12GB)

    ```bash
    nvidia-smi
    ```

1. Futa Cache: Ikiwa unatumia PyTorch, unaweza kuita torch.cuda.empty_cache() ili kuachilia kumbukumbu zote zisizotumika zilizohifadhiwa ili zitumike na programu nyingine za GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kagua Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Fanya yafuatayo kuunda tokeni ya Hugging Face.

    - Nenda kwenye [ukurasa wa mipangilio ya Tokeni ya Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Chagua **New token**.
    - Weka jina la mradi (**Name**) unayotaka kutumia.
    - Chagua aina (**Type**) kuwa **Write**.

> **Note**
>
> Ikiwa utakutana na kosa lifuatalo:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Ili kulitatua, andika amri ifuatayo ndani ya terminal yako.
>
> ```bash
> sudo ldconfig
> ```

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.