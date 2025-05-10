<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:34:04+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "sk"
}
-->
# Interaktívny Phi 3 Mini 4K Instruct Chatbot s Whisper

## Prehľad

Interaktívny Phi 3 Mini 4K Instruct Chatbot je nástroj, ktorý umožňuje používateľom komunikovať s Microsoft Phi 3 Mini 4K instruct demo pomocou textového alebo audio vstupu. Chatbot možno využiť na rôzne úlohy, ako preklad, aktualizácie počasia a získavanie všeobecných informácií.

### Začíname

Ak chcete používať tento chatbot, jednoducho postupujte podľa týchto inštrukcií:

1. Otvorte nový [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. V hlavnom okne notebooku uvidíte chatbox rozhranie s textovým vstupným poľom a tlačidlom „Send“.
3. Ak chcete používať textového chatbota, jednoducho napíšte svoju správu do textového poľa a kliknite na tlačidlo „Send“. Chatbot odpovie audio súborom, ktorý si môžete prehrať priamo v rámci notebooku.

**Note**: Tento nástroj vyžaduje GPU a prístup k modelom Microsoft Phi-3 a OpenAI Whisper, ktoré sa používajú na rozpoznávanie reči a preklad.

### Požiadavky na GPU

Na spustenie tejto ukážky potrebujete 12 GB GPU pamäte.

Požiadavky na pamäť pre spustenie **Microsoft-Phi-3-Mini-4K instruct** demo na GPU závisia od viacerých faktorov, ako je veľkosť vstupných dát (audio alebo text), jazyk prekladu, rýchlosť modelu a dostupná pamäť na GPU.

Vo všeobecnosti je model Whisper navrhnutý na spustenie na GPU. Odporúčaná minimálna kapacita GPU pamäte pre spustenie modelu Whisper je 8 GB, ale model dokáže pracovať aj s väčším množstvom pamäte podľa potreby.

Je dôležité poznamenať, že spracovanie veľkého množstva dát alebo vysoký počet požiadaviek môže vyžadovať viac GPU pamäte a/alebo môže spôsobiť problémy s výkonom. Odporúča sa otestovať váš prípad použitia s rôznymi nastaveniami a sledovať využitie pamäte, aby ste zistili optimálne parametre pre vaše konkrétne potreby.

## E2E Príklad pre Interaktívny Phi 3 Mini 4K Instruct Chatbot s Whisper

Jupyter notebook s názvom [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ukazuje, ako používať Microsoft Phi 3 Mini 4K instruct Demo na generovanie textu z audio alebo písaného vstupu. Notebook definuje niekoľko funkcií:

1. `tts_file_name(text)`: Táto funkcia vytvára názov súboru na základe vstupného textu pre uloženie generovaného audio súboru.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Táto funkcia používa Edge TTS API na generovanie audio súboru zo zoznamu častí vstupného textu. Vstupné parametre sú zoznam častí, rýchlosť reči, meno hlasu a cesta na uloženie vygenerovaného audio súboru.
1. `talk(input_text)`: Táto funkcia generuje audio súbor pomocou Edge TTS API a ukladá ho pod náhodným názvom v adresári /content/audio. Vstupným parametrom je text, ktorý sa má previesť na reč.
1. `run_text_prompt(message, chat_history)`: Táto funkcia využíva Microsoft Phi 3 Mini 4K instruct demo na generovanie audio súboru zo vstupnej správy a pridáva ho do histórie chatu.
1. `run_audio_prompt(audio, chat_history)`: Táto funkcia konvertuje audio súbor na text pomocou Whisper model API a odovzdáva ho funkcii `run_text_prompt()`.
1. Kód spúšťa Gradio aplikáciu, ktorá umožňuje používateľom komunikovať s Phi 3 Mini 4K instruct demo buď písaním správ, alebo nahrávaním audio súborov. Výstup sa zobrazí ako textová správa v aplikácii.

## Riešenie problémov

Inštalácia Cuda GPU ovládačov

1. Uistite sa, že vaše Linux aplikácie sú aktuálne

    ```bash
    sudo apt update
    ```

1. Nainštalujte Cuda ovládače

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Zaregistrujte umiestnenie cuda ovládača

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Skontrolujte veľkosť Nvidia GPU pamäte (vyžaduje sa 12 GB GPU pamäte)

    ```bash
    nvidia-smi
    ```

1. Vyprázdnite cache: Ak používate PyTorch, môžete zavolať torch.cuda.empty_cache() na uvoľnenie všetkej nepoužívanej cache pamäte, aby ju mohli využiť iné GPU aplikácie

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
> Na vyriešenie zadajte do terminálu tento príkaz.
>
> ```bash
> sudo ldconfig
> ```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím vezmite na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.