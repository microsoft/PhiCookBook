<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-09-12T14:29:01+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "lt"
}
-->
# Interaktyvus Phi 3 Mini 4K Instruct pokalbių robotas su Whisper

## Apžvalga

Interaktyvus Phi 3 Mini 4K Instruct pokalbių robotas yra įrankis, leidžiantis vartotojams bendrauti su Microsoft Phi 3 Mini 4K instruct demonstracine versija naudojant tekstinį arba garso įvestį. Pokalbių robotas gali būti naudojamas įvairioms užduotims, tokioms kaip vertimas, orų prognozės ir bendros informacijos rinkimas.

### Pradžia

Norėdami naudotis šiuo pokalbių robotu, atlikite šiuos veiksmus:

1. Atidarykite naują [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Pagrindiniame užrašinės lange pamatysite pokalbių lango sąsają su tekstinės įvesties laukeliu ir mygtuku „Siųsti“.
3. Norėdami naudotis tekstiniu pokalbių robotu, tiesiog įveskite savo žinutę į tekstinės įvesties laukelį ir spustelėkite mygtuką „Siųsti“. Pokalbių robotas atsakys garso failu, kurį galima paleisti tiesiogiai užrašinėje.

**Pastaba**: Šiam įrankiui reikalinga GPU ir prieiga prie Microsoft Phi-3 bei OpenAI Whisper modelių, kurie naudojami kalbos atpažinimui ir vertimui.

### GPU reikalavimai

Norint paleisti šią demonstracinę versiją, reikia 12 GB GPU atminties.

Atminties reikalavimai, skirti **Microsoft-Phi-3-Mini-4K instruct** demonstracinei versijai GPU, priklausys nuo kelių veiksnių, tokių kaip įvesties duomenų dydis (garso ar teksto), naudojama vertimo kalba, modelio greitis ir GPU turima atmintis.

Apskritai, Whisper modelis yra sukurtas veikti su GPU. Rekomenduojamas minimalus GPU atminties kiekis Whisper modeliui yra 8 GB, tačiau jis gali apdoroti ir didesnį atminties kiekį, jei reikia.

Svarbu pažymėti, kad didelio duomenų kiekio ar didelio užklausų srauto apdorojimas modelyje gali reikalauti daugiau GPU atminties ir/arba sukelti našumo problemų. Rekomenduojama išbandyti savo naudojimo atvejį su skirtingomis konfigūracijomis ir stebėti atminties naudojimą, kad nustatytumėte optimalias nuostatas savo specifiniams poreikiams.

## E2E pavyzdys interaktyviam Phi 3 Mini 4K Instruct pokalbių robotui su Whisper

Užrašinė pavadinimu [Interaktyvus Phi 3 Mini 4K Instruct pokalbių robotas su Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstruoja, kaip naudoti Microsoft Phi 3 Mini 4K instruct demonstracinę versiją tekstui generuoti iš garso ar rašytinės teksto įvesties. Užrašinėje apibrėžiamos kelios funkcijos:

1. `tts_file_name(text)`: Ši funkcija generuoja failo pavadinimą pagal įvesties tekstą, skirtą sugeneruotam garso failui išsaugoti.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ši funkcija naudoja Edge TTS API, kad sugeneruotų garso failą iš teksto dalių sąrašo. Įvesties parametrai yra dalių sąrašas, kalbėjimo greitis, balso pavadinimas ir išsaugojimo kelias sugeneruotam garso failui.
1. `talk(input_text)`: Ši funkcija generuoja garso failą naudodama Edge TTS API ir išsaugo jį atsitiktiniu failo pavadinimu kataloge /content/audio. Įvesties parametras yra tekstas, kurį reikia konvertuoti į kalbą.
1. `run_text_prompt(message, chat_history)`: Ši funkcija naudoja Microsoft Phi 3 Mini 4K instruct demonstracinę versiją, kad sugeneruotų garso failą iš žinutės įvesties ir prideda jį prie pokalbių istorijos.
1. `run_audio_prompt(audio, chat_history)`: Ši funkcija konvertuoja garso failą į tekstą naudodama Whisper modelio API ir perduoda jį funkcijai `run_text_prompt()`.
1. Kodas paleidžia Gradio programą, leidžiančią vartotojams bendrauti su Phi 3 Mini 4K instruct demonstracine versija, įvedant žinutes arba įkeliant garso failus. Rezultatas rodomas kaip tekstinė žinutė programos viduje.

## Trikčių šalinimas

Cuda GPU tvarkyklių diegimas

1. Įsitikinkite, kad jūsų Linux programos yra atnaujintos

    ```bash
    sudo apt update
    ```

1. Įdiekite Cuda tvarkykles

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Užregistruokite Cuda tvarkyklių vietą

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Patikrinkite Nvidia GPU atminties dydį (Reikalinga 12 GB GPU atminties)

    ```bash
    nvidia-smi
    ```

1. Išvalykite talpyklą: Jei naudojate PyTorch, galite iškviesti torch.cuda.empty_cache(), kad atlaisvintumėte visą nenaudojamą talpyklos atmintį, kad ją galėtų naudoti kitos GPU programos.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Patikrinkite Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Atlikite šiuos veiksmus, kad sukurtumėte Hugging Face tokeną.

    - Eikite į [Hugging Face Token Settings puslapį](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Pasirinkite **New token**.
    - Įveskite projekto **Name**, kurį norite naudoti.
    - Pasirinkite **Type** kaip **Write**.

> **Pastaba**
>
> Jei susiduriate su šia klaida:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Norėdami ją išspręsti, įveskite šią komandą savo terminale.
>
> ```bash
> sudo ldconfig
> ```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.