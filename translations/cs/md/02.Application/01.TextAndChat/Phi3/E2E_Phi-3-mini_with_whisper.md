# Interaktivní Phi 3 Mini 4K Instruct Chatbot s Whisperem

## Přehled

Interaktivní Phi 3 Mini 4K Instruct Chatbot je nástroj, který umožňuje uživatelům interagovat s demonstrací Microsoft Phi 3 Mini 4K instruct pomocí textového nebo audio vstupu. Chatbot lze použít pro různé úkoly, jako je překlad, aktualizace počasí a obecné shromažďování informací.

### Začínáme

Pro použití tohoto chatbota postupujte podle těchto pokynů:

1. Otevřete nový [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. V hlavním okně notebooku uvidíte rozhraní chatboxu s textovým vstupním polem a tlačítkem „Odeslat“.
3. Pro použití textového chatbota jednoduše napište svou zprávu do textového vstupního pole a klikněte na tlačítko „Odeslat“. Chatbot odpoví zvukovým souborem, který lze přehrát přímo v rámci notebooku.

**Poznámka**: Tento nástroj vyžaduje GPU a přístup k modelům Microsoft Phi-3 a OpenAI Whisper, které se používají pro rozpoznávání řeči a překlad.

### Požadavky na GPU

Pro spuštění této ukázky potřebujete 12GB paměti GPU.

Požadavky na paměť pro spuštění **Microsoft-Phi-3-Mini-4K instruct** ukázky na GPU závisí na několika faktorech, jako je velikost vstupních dat (audio nebo text), jazyk používaný pro překlad, rychlost modelu a dostupná paměť na GPU.

Obecně je model Whisper navržen pro běh na GPU. Doporučené minimální množství paměti GPU pro běh modelu Whisper je 8 GB, ale může zvládnout i větší množství, pokud je potřeba.

Je důležité si uvědomit, že zpracování velkého množství dat nebo vysoký počet požadavků na model může vyžadovat více paměti GPU a/nebo může způsobit výkonové problémy. Doporučuje se otestovat svůj případ použití s různými konfiguracemi a sledovat využití paměti, aby bylo možné určit optimální nastavení pro vaše konkrétní potřeby.

## E2E vzorek pro Interaktivní Phi 3 Mini 4K Instruct Chatbot s Whisperem

Jupyter notebook s názvem [Interaktivní Phi 3 Mini 4K Instruct Chatbot s Whisperem](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ukazuje, jak používat Microsoft Phi 3 Mini 4K instruct Demo pro generování textu ze zvukového nebo psaného textového vstupu. Notebook definuje několik funkcí:

1. `tts_file_name(text)`: Tato funkce generuje název souboru na základě vstupního textu pro uložení vygenerovaného zvukového souboru.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Tato funkce používá Edge TTS API k vygenerování zvukového souboru ze seznamu částí vstupního textu. Vstupní parametry jsou seznam částí, rychlost řeči, jméno hlasu a cesta pro uložení vygenerovaného zvukového souboru.
1. `talk(input_text)`: Tato funkce generuje zvukový soubor pomocí Edge TTS API a ukládá jej pod náhodným názvem souboru do adresáře /content/audio. Vstupním parametrem je text, který bude převeden na řeč.
1. `run_text_prompt(message, chat_history)`: Tato funkce používá Microsoft Phi 3 Mini 4K instruct demo pro generování zvukového souboru ze vstupní zprávy a přidává ho do historie chatu.
1. `run_audio_prompt(audio, chat_history)`: Tato funkce převádí zvukový soubor na text pomocí modelu Whisper API a předává jej funkci `run_text_prompt()`.
1. Kód spouští aplikaci Gradio, která umožňuje uživatelům interagovat s Phi 3 Mini 4K instruct demo psaním zpráv nebo nahráváním zvukových souborů. Výstup je zobrazován jako textová zpráva v rámci aplikace.

## Řešení problémů

Instalace ovladačů Cuda pro GPU

1. Ujistěte se, že jsou vaše linuxové aplikace aktualizované

    ```bash
    sudo apt update
    ```

1. Nainstalujte ovladače Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Zaregistrujte umístění cuda ovladače

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kontrola velikosti paměti Nvidia GPU (vyžadováno 12GB paměti GPU)

    ```bash
    nvidia-smi
    ```

1. Vyprázdnění cache: Pokud používáte PyTorch, můžete zavolat torch.cuda.empty_cache() pro uvolnění veškeré nepoužité uložené paměti, aby ji mohly používat jiné GPU aplikace

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kontrola Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Pro vytvoření Hugging Face tokenu proveďte následující kroky.

    - Přejděte na stránku [Nastavení tokenů Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Vyberte **Nový token**.
    - Zadejte název projektu, který chcete použít.
    - Vyberte **Typ** na **Write** (zápis).

> [!NOTE]
>
> Pokud narazíte na následující chybu:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pro vyřešení zadejte v terminálu následující příkaz.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje využít profesionální lidský překlad. Za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu neneseme odpovědnost.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->