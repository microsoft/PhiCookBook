<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:22:17+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "cs"
}
-->
# Interaktivní Phi 3 Mini 4K Instruct Chatbot s Whisper

## Přehled

Interaktivní Phi 3 Mini 4K Instruct Chatbot je nástroj, který umožňuje uživatelům komunikovat s Microsoft Phi 3 Mini 4K instruct demo pomocí textového nebo hlasového vstupu. Chatbot lze využít pro různé úkoly, jako je překlad, aktuální informace o počasí nebo obecné získávání informací.

### Začínáme

Pro použití tohoto chatbota jednoduše postupujte podle těchto pokynů:

1. Otevřete nový [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. V hlavním okně notebooku uvidíte rozhraní chatboxu s textovým vstupním polem a tlačítkem „Send“.
3. Pro použití textového chatbota jednoduše napište svou zprávu do textového pole a klikněte na tlačítko „Send“. Chatbot odpoví audio souborem, který lze přehrát přímo v notebooku.

**Note**: Tento nástroj vyžaduje GPU a přístup k modelům Microsoft Phi-3 a OpenAI Whisper, které se používají pro rozpoznávání řeči a překlad.

### Požadavky na GPU

Pro spuštění této ukázky potřebujete 12 GB paměti na GPU.

Požadavky na paměť pro spuštění **Microsoft-Phi-3-Mini-4K instruct** demo na GPU závisí na několika faktorech, jako je velikost vstupních dat (audio nebo text), jazyk použitý pro překlad, rychlost modelu a dostupná paměť na GPU.

Obecně je model Whisper navržen pro běh na GPU. Doporučené minimální množství paměti GPU pro běh modelu Whisper je 8 GB, ale model zvládne i větší množství paměti, pokud je potřeba.

Je důležité poznamenat, že zpracování velkého množství dat nebo vysoký počet požadavků na model může vyžadovat více paměti GPU a/nebo může způsobit problémy s výkonem. Doporučuje se otestovat váš případ použití s různými konfiguracemi a sledovat využití paměti, abyste určili optimální nastavení pro vaše konkrétní potřeby.

## E2E ukázka pro Interaktivní Phi 3 Mini 4K Instruct Chatbot s Whisper

Jupyter notebook s názvem [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ukazuje, jak používat Microsoft Phi 3 Mini 4K instruct Demo k generování textu z audio nebo psaného vstupu. Notebook definuje několik funkcí:

1. `tts_file_name(text)`: Tato funkce generuje název souboru na základě vstupního textu pro uložení vygenerovaného audio souboru.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Tato funkce využívá Edge TTS API k vytvoření audio souboru ze seznamu částí vstupního textu. Vstupní parametry jsou seznam částí, rychlost řeči, jméno hlasu a cesta pro uložení vygenerovaného audio souboru.
1. `talk(input_text)`: Tato funkce generuje audio soubor pomocí Edge TTS API a uloží ho pod náhodným názvem do adresáře /content/audio. Vstupním parametrem je text, který se má převést na řeč.
1. `run_text_prompt(message, chat_history)`: Tato funkce využívá Microsoft Phi 3 Mini 4K instruct demo k vytvoření audio souboru ze zadané zprávy a přidá ho do historie chatu.
1. `run_audio_prompt(audio, chat_history)`: Tato funkce převádí audio soubor na text pomocí Whisper model API a předává ho funkci `run_text_prompt()`.
1. Kód spouští aplikaci Gradio, která umožňuje uživatelům komunikovat s Phi 3 Mini 4K instruct demo buď psaním zpráv, nebo nahráváním audio souborů. Výstup je zobrazen jako textová zpráva v aplikaci.

## Řešení problémů

Instalace ovladačů Cuda GPU

1. Ujistěte se, že vaše Linux aplikace jsou aktuální

    ```bash
    sudo apt update
    ```

1. Nainstalujte ovladače Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Zaregistrujte umístění ovladače cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kontrola velikosti paměti Nvidia GPU (Požadováno 12GB paměti GPU)

    ```bash
    nvidia-smi
    ```

1. Vyprázdnění cache: Pokud používáte PyTorch, můžete zavolat torch.cuda.empty_cache() pro uvolnění veškeré nepoužívané cache paměti, aby ji mohly využít jiné GPU aplikace

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kontrola Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Pro vytvoření Hugging Face tokenu proveďte následující kroky.

    - Přejděte na [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Vyberte **New token**.
    - Zadejte název projektu, který chcete použít.
    - Vyberte **Type** na **Write**.

> **Note**
>
> Pokud narazíte na následující chybu:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pro vyřešení zadejte do terminálu následující příkaz.
>
> ```bash
> sudo ldconfig
> ```

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.