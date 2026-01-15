<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T16:17:08+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "lt"
}
-->
# Interaktyvus Phi 3 Mini 4K Instruct pokalbių robotas su Whisper

## Apžvalga

Interaktyvus Phi 3 Mini 4K Instruct pokalbių robotas yra įrankis, leidžiantis vartotojams bendrauti su Microsoft Phi 3 Mini 4K instruct demonstracija naudojant teksto arba garso įvestį. Šis pokalbių robotas gali būti naudojamas įvairioms užduotims, tokioms kaip vertimas, orų atnaujinimai ir bendros informacijos rinkimas.

### Pradžia

Norėdami naudoti šį pokalbių robotą, tiesiog vadovaukitės šiomis instrukcijomis:

1. Atidarykite naują [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Užrašo pagrindiniame lange pamatysite pokalbių lango sąsają su teksto įvesties laukeliu ir mygtuku „Send“.
3. Norėdami naudoti teksto pagrindu veikiantį pokalbių robotą, tiesiog įveskite savo žinutę į teksto įvesties laukelį ir spustelėkite mygtuką „Send“. Pokalbių robotas atsakys garso failu, kurį galima tiesiogiai leisti užraše.

**Pastaba**: Šiam įrankiui reikalinga GPU ir prieiga prie Microsoft Phi-3 bei OpenAI Whisper modelių, kurie naudojami kalbos atpažinimui ir vertimui.

### GPU reikalavimai

Norint paleisti šią demonstraciją, reikia 12 GB GPU atminties.

Atminties poreikiai paleidžiant **Microsoft-Phi-3-Mini-4K instruct** demonstraciją GPU priklausys nuo kelių veiksnių, tokių kaip įvesties duomenų dydis (garso ar teksto), vertimui naudojama kalba, modelio greitis ir prieinama atmintis GPU.

Paprastai Whisper modelis sukurtas veikti GPU. Rekomenduojamas minimalus GPU atminties kiekis Whisper modeliui paleisti yra 8 GB, tačiau jis gali naudoti ir didesnę atmintį, jei to reikia.

Svarbu pažymėti, kad didelio duomenų kiekio ar didelio užklausų srauto paleidimas modeliui gali prireikti daugiau GPU atminties ir/ar gali sukelti našumo problemų. Rekomenduojama išbandyti savo naudojimo scenarijų su skirtingomis konfigūracijomis ir stebėti atminties naudojimą, kad nustatytumėte optimalias nustatymų reikšmes jūsų konkretiems poreikiams.

## E2E pavyzdys interaktyviam Phi 3 Mini 4K Instruct pokalbių robotui su Whisper

Jupyter užrašas pavadinimu [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstruoja, kaip naudoti Microsoft Phi 3 Mini 4K instruct demonstraciją tekstui sugeneruoti iš garso arba rašytinio teksto įvesties. Užraše apibrėžtos kelios funkcijos:

1. `tts_file_name(text)`: ši funkcija sukuria failo pavadinimą pagal įvestą tekstą, skirtą sugeneruotam garso failui išsaugoti.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: ši funkcija naudoja Edge TTS API, kad sugeneruotų garso failą iš tekstinių dalių sąrašo. Įvesties parametrai – dalių sąrašas, kalbėjimo greitis, balso pavadinimas ir išvesties kelias sugeneruotam garso failui išsaugoti.
1. `talk(input_text)`: ši funkcija sugeneruoja garso failą naudodama Edge TTS API ir išsaugo jį atsitiktiniu pavadinimu kataloge /content/audio. Įvesties parametras yra tekstas, kuris bus paverstas kalba.
1. `run_text_prompt(message, chat_history)`: ši funkcija naudoja Microsoft Phi 3 Mini 4K instruct demonstraciją, kad sugeneruotų garso failą iš žinutės įvesties ir prideda jį prie pokalbio istorijos.
1. `run_audio_prompt(audio, chat_history)`: ši funkcija paverčia garso failą tekstu naudodama Whisper modelio API ir perduoda rezultatą funkcijai `run_text_prompt()`.
1. Kodas paleidžia Gradio programėlę, leidžiančią vartotojams bendrauti su Phi 3 Mini 4K instruct demonstracija tiek rašant žinutes, tiek įkelti garso failus. Išvestis rodoma kaip teksto žinutė programėlėje.

## Trikčių šalinimas

Cuda GPU vairuotojų įdiegimas

1. Įsitikinkite, kad jūsų Linux sistema yra atnaujinta

    ```bash
    sudo apt update
    ```

1. Įdiekite Cuda vairuotojus

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Užregistruokite cuda vairuotojo vietą

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Patikrinkite Nvidia GPU atminties dydį (reikalaujama 12GB GPU atminties)

    ```bash
    nvidia-smi
    ```

1. Ištuštinkite talpyklą: jei naudojate PyTorch, galite iškviesti torch.cuda.empty_cache(), kad atlaisvintumėte nenaudojamą talpyklos atmintį, kad ją galėtų naudoti kitos GPU programos

    ```python
    torch.cuda.empty_cache() 
    ```

1. Patikrinkite Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Atlikite šiuos veiksmus, kad sukurtumėte Hugging Face tokeną.

    - Eikite į [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Pasirinkite **New token**.
    - Įveskite norimo naudoti projekto **Name**.
    - Pasirinkite **Type** – **Write**.

> [!NOTE]
>
> Jei susiduriate su šia klaida:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Norėdami ją išspręsti, terminale įveskite šią komandą.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Autentiškas šio dokumento šaltinis yra originali kalba. Svarbiai informacijai rekomenduojamas profesionalus vertimas žmogaus. Mes neatsakome už bet kokius nesusipratimus ar klaidingus aiškinimus, kilusius iš šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->