# Chatbot la Kuelekezwa la Interactive Phi 3 Mini 4K na Whisper

## Muhtasari

Chatbot la Kuelekezwa la Interactive Phi 3 Mini 4K ni chombo kinachowezesha watumiaji kuingiliana na onyesho la Microsoft Phi 3 Mini 4K la kuelekeza kwa kutumia maandishi au sauti. Chatbot inaweza kutumika kwa kazi mbalimbali, kama vile tafsiri, masasisho ya hali ya hewa, na ukusanyaji wa taarifa za jumla.

### Kuanzisha

Ili kutumia chatbot hii, fuata maelekezo haya:

1. Fungua [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) mpya
2. Kwenye dirisha kuu la daftari, utaona kiolesura cha chatbox chenye kisanduku cha kuingiza maandishi na kitufe cha "Send".
3. Ili kutumia chatbot inayotumia maandishi, andika tu ujumbe wako kwenye kisanduku cha kuingiza maandishi na bonyeza kitufe cha "Send". Chatbot itajibu na faili la sauti ambalo linaweza kusikilizwa moja kwa moja ndani ya daftari.

**Kumbuka**: Chombo hiki kinahitaji GPU na upatikanaji wa mifano ya Microsoft Phi-3 na OpenAI Whisper, ambayo hutumika kwa utambuzi wa hotuba na tafsiri.

### Mahitaji ya GPU

Ili kuendesha onyesho hili unahitaji GB 12 za kumbukumbu ya GPU.

Mahitaji ya kumbukumbu kwa kuendesha onyesho la **Microsoft-Phi-3-Mini-4K instruct** kwenye GPU yataegemea mambo kadhaa, kama ukubwa wa data ya ingizo (sauti au maandishi), lugha inayotumika kwa tafsiri, kasi ya mfano, na kumbukumbu inayopatikana kwenye GPU.

Kwa ujumla, mfano wa Whisper umebuniwa kuendeshwa kwenye GPUs. Kiasi kinachopendekezwa cha chini cha kumbukumbu ya GPU kwa kuendesha mfano wa Whisper ni GB 8, lakini unaweza kushughulikia kiasi kikubwa cha kumbukumbu ikiwa inahitajika.

Ni muhimu kutambua kuwa kuendesha data kubwa au idadi kubwa ya maombi kwenye mfano kunaweza kuhitaji kumbukumbu zaidi ya GPU na/au kusababisha matatizo ya utendaji. Inashauriwa kujaribu matumizi yako kwa mipangilio tofauti na kufuatilia matumizi ya kumbukumbu ili kubaini mipangilio bora kwa mahitaji yako maalum.

## Sampuli ya E2E kwa Chatbot la Interactive Phi 3 Mini 4K Instruct na Whisper

Daftari la jupyter lililojaa kichwa [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) linaonyesha jinsi ya kutumia Onyesho la Microsoft Phi 3 Mini 4K la kuelekeza kuzalisha maandishi kutoka kwa sauti au maandishi yaliyoandikwa. Daftari linafafanua kazi kadhaa:

1. `tts_file_name(text)`: Kazi hii huzalisha jina la faili kulingana na maandishi yaliyopo kwa ajili ya kuhifadhi faili la sauti lililotengenezwa.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Kazi hii hutumia API ya Edge TTS kuzalisha faili la sauti kutoka kwenye orodha ya vipande vya maandishi. Vigezo vya ingizo ni orodha ya vipande, kasi ya hotuba, jina la sauti, na njia ya kuhifadhi faili la sauti lililotengenezwa.
1. `talk(input_text)`: Kazi hii huzalisha faili la sauti kwa kutumia API ya Edge TTS na kuihifadhi kwa jina la faili la nasibu kwenye saraka ya /content/audio. Kigezo cha ingizo ni maandishi ya kubadilishwa kuwa hotuba.
1. `run_text_prompt(message, chat_history)`: Kazi hii hutumia onyesho la Microsoft Phi 3 Mini 4K la kuelekeza kuzalisha faili la sauti kutoka kwa ujumbe wa ingizo na kuongeza kwenye historia ya mazungumzo.
1. `run_audio_prompt(audio, chat_history)`: Kazi hii hubadilisha faili la sauti kuwa maandishi kwa kutumia API ya mfano wa Whisper na kulituma kwa kazi ya `run_text_prompt()`.
1. Msimbo unaanzisha programu ya Gradio inayowezesha watumiaji kuingiliana na onyesho la Phi 3 Mini 4K la kuelekeza kwa kuandika ujumbe au kupakia faili za sauti. Matokeo yanaonyeshwa kama ujumbe wa maandishi ndani ya programu.

## Utatuzi wa Matatizo

KufungaDereva za Cuda GPU

1. Hakikisha programu yako ya Linux ni za kisasa

    ```bash
    sudo apt update
    ```

1. Sakinisha Dereva za Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Sajili eneo la dereva wa cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kukagua ukubwa wa kumbukumbu ya GPU ya Nvidia (Inahitajika GB 12 za Kumbukumbu ya GPU)

    ```bash
    nvidia-smi
    ```

1. Ondoa Kache: Ikiwa unatumia PyTorch, unaweza kutumia torch.cuda.empty_cache() kuachilia kumbukumbu isiyotumika ya kache ili itumike na programu nyingine za GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kukagua Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Fanya kazi zifuatazo kutengeneza tokeni ya Hugging Face.

    - Nenda kwenye [ukurasa wa Mipangilio ya Tokeni ya Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Chagua **New token**.
    - Weka jina la mradi (**Name**) unalotaka kutumia.
    - Chagua aina (**Type**) kuwa **Write**.

> [!NOTE]
>
> Ikiwa unakutana na hitilafu ifuatayo:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Ili kutatua hili, andika amri ifuatayo ndani ya terminal yako.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tamko la Haki**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokukamilika. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya mtaalamu wa binadamu inapendekezwa. Hatubebi dhima kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->