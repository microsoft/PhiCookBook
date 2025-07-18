<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:22:52+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ro"
}
-->
# Chatbot Interactiv Phi 3 Mini 4K Instruct cu Whisper

## Prezentare generală

Chatbotul Interactiv Phi 3 Mini 4K Instruct este un instrument care permite utilizatorilor să interacționeze cu demo-ul Microsoft Phi 3 Mini 4K instruct folosind input text sau audio. Chatbotul poate fi folosit pentru diverse sarcini, cum ar fi traduceri, actualizări meteo și colectare generală de informații.

### Început rapid

Pentru a folosi acest chatbot, urmează pur și simplu aceste instrucțiuni:

1. Deschide un nou [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. În fereastra principală a notebook-ului, vei vedea o interfață de chat cu o casetă de introducere text și un buton „Send”.
3. Pentru a folosi chatbotul bazat pe text, pur și simplu tastează mesajul în caseta de text și apasă butonul „Send”. Chatbotul va răspunde cu un fișier audio care poate fi redat direct din notebook.

**Note**: Acest instrument necesită un GPU și acces la modelele Microsoft Phi-3 și OpenAI Whisper, folosite pentru recunoașterea vocală și traducere.

### Cerințe GPU

Pentru a rula acest demo ai nevoie de 12GB memorie GPU.

Cererea de memorie pentru rularea demo-ului **Microsoft-Phi-3-Mini-4K instruct** pe GPU depinde de mai mulți factori, cum ar fi dimensiunea datelor de intrare (audio sau text), limba folosită pentru traducere, viteza modelului și memoria disponibilă pe GPU.

În general, modelul Whisper este conceput să ruleze pe GPU-uri. Cantitatea minimă recomandată de memorie GPU pentru rularea modelului Whisper este de 8 GB, dar poate gestiona și cantități mai mari de memorie dacă este necesar.

Este important de menționat că rularea unui volum mare de date sau a unui număr mare de cereri către model poate necesita mai multă memorie GPU și/sau poate cauza probleme de performanță. Se recomandă testarea cazului tău de utilizare cu diferite configurații și monitorizarea utilizării memoriei pentru a determina setările optime pentru nevoile tale specifice.

## Exemplu E2E pentru Chatbot Interactiv Phi 3 Mini 4K Instruct cu Whisper

Notebook-ul jupyter intitulat [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrează cum să folosești demo-ul Microsoft Phi 3 Mini 4K instruct pentru a genera text din input audio sau text scris. Notebook-ul definește mai multe funcții:

1. `tts_file_name(text)`: Această funcție generează un nume de fișier bazat pe textul de intrare pentru salvarea fișierului audio generat.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Această funcție folosește API-ul Edge TTS pentru a genera un fișier audio dintr-o listă de segmente de text de intrare. Parametrii de intrare sunt lista de segmente, viteza vorbirii, numele vocii și calea de salvare a fișierului audio generat.
1. `talk(input_text)`: Această funcție generează un fișier audio folosind API-ul Edge TTS și îl salvează cu un nume aleator în directorul /content/audio. Parametrul de intrare este textul care trebuie convertit în vorbire.
1. `run_text_prompt(message, chat_history)`: Această funcție folosește demo-ul Microsoft Phi 3 Mini 4K instruct pentru a genera un fișier audio dintr-un mesaj de intrare și îl adaugă la istoricul conversației.
1. `run_audio_prompt(audio, chat_history)`: Această funcție convertește un fișier audio în text folosind API-ul modelului Whisper și îl transmite funcției `run_text_prompt()`.
1. Codul lansează o aplicație Gradio care permite utilizatorilor să interacționeze cu demo-ul Phi 3 Mini 4K instruct fie tastând mesaje, fie încărcând fișiere audio. Rezultatul este afișat ca mesaj text în aplicație.

## Depanare

Instalarea driverelor Cuda GPU

1. Asigură-te că aplicațiile tale Linux sunt actualizate

    ```bash
    sudo apt update
    ```

1. Instalează driverele Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Înregistrează locația driverului cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Verificarea dimensiunii memoriei GPU Nvidia (Necesar 12GB memorie GPU)

    ```bash
    nvidia-smi
    ```

1. Golirea cache-ului: Dacă folosești PyTorch, poți apela torch.cuda.empty_cache() pentru a elibera toată memoria cache neutilizată astfel încât să poată fi folosită de alte aplicații GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verificarea Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Efectuează următoarele pentru a crea un token Hugging Face.

    - Accesează pagina [Hugging Face Token Settings](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selectează **New token**.
    - Introdu numele proiectului pe care vrei să-l folosești.
    - Selectează **Type** ca **Write**.

> **Note**
>
> Dacă întâmpini următoarea eroare:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pentru a rezolva, tastează următoarea comandă în terminal.
>
> ```bash
> sudo ldconfig
> ```

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.