<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:22:32+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "sk"
}
-->
# Interaktívny Phi 3 Mini 4K Instruct Chatbot s Whisper

## Prehľad

Interaktívny Phi 3 Mini 4K Instruct Chatbot je nástroj, ktorý umožňuje používateľom komunikovať s Microsoft Phi 3 Mini 4K instruct demo pomocou textového alebo zvukového vstupu. Chatbot je možné využiť na rôzne úlohy, ako preklad, aktualizácie počasia alebo získavanie všeobecných informácií.

### Začíname

Na používanie tohto chatbota postupujte podľa týchto pokynov:

1. Otvorte nový [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. V hlavnom okne notebooku uvidíte rozhranie chatboxu s textovým vstupným poľom a tlačidlom „Send“.
3. Ak chcete použiť textového chatbota, jednoducho napíšte správu do textového poľa a kliknite na tlačidlo „Send“. Chatbot odpovie zvukovým súborom, ktorý je možné prehrať priamo v notebooku.

**Note**: Tento nástroj vyžaduje GPU a prístup k modelom Microsoft Phi-3 a OpenAI Whisper, ktoré sa používajú na rozpoznávanie reči a preklad.

### Požiadavky na GPU

Na spustenie tejto ukážky potrebujete 12 GB pamäte na GPU.

Požiadavky na pamäť pre spustenie **Microsoft-Phi-3-Mini-4K instruct** demo na GPU závisia od viacerých faktorov, ako je veľkosť vstupných dát (audio alebo text), jazyk prekladu, rýchlosť modelu a dostupná pamäť na GPU.

Vo všeobecnosti je model Whisper navrhnutý na beh na GPU. Odporúčaná minimálna veľkosť pamäte GPU pre spustenie modelu Whisper je 8 GB, ale model zvládne aj väčšie množstvo pamäte, ak je to potrebné.

Je dôležité si uvedomiť, že spracovanie veľkého množstva dát alebo vysoký počet požiadaviek môže vyžadovať viac pamäte na GPU a/alebo môže spôsobiť problémy s výkonom. Odporúča sa testovať váš prípad použitia s rôznymi konfiguráciami a sledovať využitie pamäte, aby ste určili optimálne nastavenia pre vaše konkrétne potreby.

## E2E príklad pre Interaktívny Phi 3 Mini 4K Instruct Chatbot s Whisper

Jupyter notebook s názvom [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ukazuje, ako používať Microsoft Phi 3 Mini 4K instruct Demo na generovanie textu zo zvukového alebo písaného vstupu. Notebook definuje niekoľko funkcií:

1. `tts_file_name(text)`: Táto funkcia generuje názov súboru na základe vstupného textu pre uloženie vygenerovaného zvukového súboru.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Táto funkcia využíva Edge TTS API na generovanie zvukového súboru zo zoznamu častí vstupného textu. Vstupné parametre sú zoznam častí, rýchlosť reči, názov hlasu a cesta na uloženie vygenerovaného zvukového súboru.
1. `talk(input_text)`: Táto funkcia generuje zvukový súbor pomocou Edge TTS API a uloží ho pod náhodným názvom v adresári /content/audio. Vstupným parametrom je text, ktorý sa má previesť na reč.
1. `run_text_prompt(message, chat_history)`: Táto funkcia používa Microsoft Phi 3 Mini 4K instruct demo na generovanie zvukového súboru zo vstupnej správy a pridáva ho do histórie chatu.
1. `run_audio_prompt(audio, chat_history)`: Táto funkcia prevádza zvukový súbor na text pomocou Whisper model API a odovzdáva ho funkcii `run_text_prompt()`.
1. Kód spúšťa Gradio aplikáciu, ktorá umožňuje používateľom komunikovať s Phi 3 Mini 4K instruct demo buď písaním správ, alebo nahrávaním zvukových súborov. Výstup sa zobrazuje ako textová správa v aplikácii.

## Riešenie problémov

Inštalácia ovládačov Cuda GPU

1. Uistite sa, že vaše Linux aplikácie sú aktuálne

    ```bash
    sudo apt update
    ```

1. Nainštalujte ovládače Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Zaregistrujte umiestnenie ovládača cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Skontrolujte veľkosť pamäte Nvidia GPU (vyžaduje sa 12 GB pamäte GPU)

    ```bash
    nvidia-smi
    ```

1. Vyprázdnite cache: Ak používate PyTorch, môžete zavolať torch.cuda.empty_cache(), aby ste uvoľnili všetku nepoužívanú cache pamäť, ktorá môže byť použitá inými GPU aplikáciami

    ```python
    torch.cuda.empty_cache() 
    ```

1. Skontrolujte Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Vykonajte nasledujúce kroky na vytvorenie Hugging Face tokenu.

    - Prejdite na [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Vyberte **New token**.
    - Zadajte názov projektu, ktorý chcete použiť.
    - Vyberte **Type** na **Write**.

> **Note**
>
> Ak sa vám zobrazí nasledujúca chyba:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Na vyriešenie zadajte nasledujúci príkaz do terminálu.
>
> ```bash
> sudo ldconfig
> ```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.