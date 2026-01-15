<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T16:03:26+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "sk"
}
-->
# Interaktívny Phi 3 Mini 4K Instruct Chatbot s Whisper

## Prehľad

Interaktívny Phi 3 Mini 4K Instruct Chatbot je nástroj, ktorý umožňuje používateľom komunikovať s demom Microsoft Phi 3 Mini 4K instruct pomocou textového alebo zvukového vstupu. Chatbot možno využiť na rôzne úlohy, ako sú preklady, aktualizácie počasia a zber všeobecných informácií.

### Začíname

Na použitie tohto chatbota jednoducho postupujte podľa týchto pokynov:

1. Otvorte nový [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. V hlavnom okne notebooku uvidíte rozhranie chatboxu s textovým vstupným políčkom a tlačidlom "Send".
3. Na použitie textového chatbota jednoducho napíšte svoju správu do textového vstupného poľa a kliknite na tlačidlo "Send". Chatbot odpovie zvukovým súborom, ktorý je možné prehrať priamo v notebooku.

**Poznámka**: Tento nástroj vyžaduje GPU a prístup k modelom Microsoft Phi-3 a OpenAI Whisper, ktorý sa používa na rozpoznávanie reči a preklad.

### Požiadavky na GPU

Na spustenie tohto dema potrebujete 12 GB GPU pamäte.

Požiadavky na pamäť pre spustenie **Microsoft-Phi-3-Mini-4K instruct** dema na GPU závisia od viacerých faktorov, napríklad od veľkosti vstupných dát (audio alebo text), jazyka použitého na preklad, rýchlosti modelu a dostupnej pamäte na GPU.

Vo všeobecnosti je model Whisper navrhnutý na beh na GPU. Odporúčaná minimálna kapacita GPU pamäte na spustenie modelu Whisper je 8 GB, ale dokáže pracovať aj s väčším množstvom pamäte podľa potreby.

Je dôležité poznamenať, že spracovanie veľkého množstva dát alebo vysokého počtu požiadaviek na model môže vyžadovať viac GPU pamäte a/alebo môže spôsobovať problémy s výkonom. Odporúča sa otestovať váš prípad použitia s rôznymi konfiguráciami a sledovať využitie pamäte, aby ste určili optimálne nastavenia pre vaše konkrétne potreby.

## Príklad E2E pre interaktívny Phi 3 Mini 4K Instruct Chatbot s Whisper

Jupyter notebook s názvom [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonštruje, ako používať Microsoft Phi 3 Mini 4K instruct Demo na generovanie textu z audio alebo písaného textového vstupu. Notebook definuje niekoľko funkcií:

1. `tts_file_name(text)`: Táto funkcia generuje názov súboru na základe vstupného textu pre uloženie generovaného zvukového súboru.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Táto funkcia používa Edge TTS API na generovanie zvukového súboru zo zoznamu častí vstupného textu. Vstupné parametre sú zoznam častí, rýchlosť reči, meno hlasu a výstupná cesta na uloženie generovaného zvukového súboru.
1. `talk(input_text)`: Táto funkcia generuje zvukový súbor pomocou Edge TTS API a ukladá ho do náhodne pomenovaného súboru v priečinku /content/audio. Vstupným parametrom je text na prevod na reč.
1. `run_text_prompt(message, chat_history)`: Táto funkcia používa demo Microsoft Phi 3 Mini 4K instruct na generovanie zvukového súboru zo vstupu správy a pridáva ho do histórie chatu.
1. `run_audio_prompt(audio, chat_history)`: Táto funkcia konvertuje zvukový súbor na text pomocou Whisper model API a odovzdá ho funkcii `run_text_prompt()`.
1. Kód spúšťa Gradio aplikáciu, ktorá umožňuje používateľom komunikovať s Phi 3 Mini 4K instruct demom buď písaním správ alebo nahrávaním audio súborov. Výstup sa zobrazí ako textová správa v aplikácii.

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

1. Skontrolujte veľkosť pamäte Nvidia GPU (vyžaduje sa 12GB GPU pamäte)

    ```bash
    nvidia-smi
    ```

1. Vyprázdnite cache: Ak používate PyTorch, môžete zavolať torch.cuda.empty_cache(), aby ste uvoľnili všetku nepoužitú uloženú pamäť, ktorú môžu použiť iné GPU aplikácie

    ```python
    torch.cuda.empty_cache() 
    ```

1. Skontrolujte Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Vykonajte nasledujúce kroky na vytvorenie Hugging Face tokenu.

    - Prejdite na stránku [Hugging Face Token Settings](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Vyberte **New token**.
    - Zadajte názov projektu, ktorý chcete použiť.
    - Vyberte **Type** ako **Write**.

> [!NOTE]
>
> Ak sa zobrazí nasledujúca chyba:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Na vyriešenie tohto problému zadajte do terminálu nasledujúci príkaz.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:
Tento dokument bol preložený pomocou AI prekladača [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->