# Chatbot Interactiv Phi 3 Mini 4K Instruct cu Whisper

## Prezentare generală

Chatbot-ul Interactiv Phi 3 Mini 4K Instruct este un instrument care permite utilizatorilor să interacționeze cu demo-ul Microsoft Phi 3 Mini 4K instruct folosind input text sau audio. Chatbot-ul poate fi folosit pentru o varietate de sarcini, cum ar fi traducerea, actualizările meteo și colectarea generală de informații.

### Începutul utilizării

Pentru a folosi acest chatbot, urmați pur și simplu aceste instrucțiuni:

1. Deschideți un nou [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. În fereastra principală a notebook-ului, veți vedea o interfață de chatbox cu o casetă de introducere text și un buton „Send”.
3. Pentru a utiliza chatbot-ul bazat pe text, tastați pur și simplu mesajul în caseta de introducere text și faceți clic pe butonul „Send”. Chatbot-ul va răspunde cu un fișier audio care poate fi redat direct din interiorul notebook-ului.

**Notă**: Acest instrument necesită un GPU și acces la modelele Microsoft Phi-3 și OpenAI Whisper, care sunt folosite pentru recunoașterea vocală și traducere.

### Cerințe pentru GPU

Pentru a rula acest demo aveți nevoie de 12Gb memorie GPU.

Cerințele de memorie pentru rularea demo-ului **Microsoft-Phi-3-Mini-4K instruct** pe un GPU vor depinde de mai mulți factori, cum ar fi dimensiunea datelor de intrare (audio sau text), limba folosită pentru traducere, viteza modelului și memoria disponibilă pe GPU.

În general, modelul Whisper este conceput să ruleze pe GPU-uri. Cantitatea minimă recomandată de memorie GPU pentru rularea modelului Whisper este 8 GB, dar acesta poate gestiona cantități mai mari de memorie dacă este necesar.

Este important de menționat că rularea unui volum mare de date sau a unui număr mare de cereri către model poate necesita mai multă memorie GPU și/sau poate cauza probleme de performanță. Se recomandă testarea cazului dvs. de utilizare cu diferite configurații și monitorizarea utilizării memoriei pentru a determina setările optime pentru nevoile dvs. specifice.

## Exemplu E2E pentru Chatbot Interactiv Phi 3 Mini 4K Instruct cu Whisper

Notebook-ul jupyter intitulat [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrează cum să folosiți demo-ul Microsoft Phi 3 Mini 4K instruct pentru a genera text din input audio sau text scris. Notebook-ul definește mai multe funcții:

1. `tts_file_name(text)`: Această funcție generează un nume de fișier bazat pe textul de intrare pentru salvarea fișierului audio generat.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Această funcție folosește API-ul Edge TTS pentru a genera un fișier audio dintr-o listă de segmente de text de intrare. Parametrii de intrare sunt lista de segmente, viteza vorbirii, numele vocii și calea de ieșire pentru salvarea fișierului audio generat.
1. `talk(input_text)`: Această funcție generează un fișier audio folosind API-ul Edge TTS și îl salvează cu un nume aleator în directorul /content/audio. Parametrul de intrare este textul ce urmează a fi convertit în vorbire.
1. `run_text_prompt(message, chat_history)`: Această funcție folosește demo-ul Microsoft Phi 3 Mini 4K instruct pentru a genera un fișier audio dintr-un mesaj introdus și îl adaugă la istoricul conversației.
1. `run_audio_prompt(audio, chat_history)`: Această funcție convertește un fișier audio în text folosind API-ul modelului Whisper și îl pasează funcției `run_text_prompt()`.
1. Codul lansează o aplicație Gradio care permite utilizatorilor să interacționeze cu demo-ul Phi 3 Mini 4K instruct fie tastând mesaje, fie încărcând fișiere audio. Rezultatul este afișat ca mesaj text în cadrul aplicației.

## Depanare

Instalarea driverelor Cuda GPU

1. Asigurați-vă că aplicațiile Linux sunt actualizate

    ```bash
    sudo apt update
    ```

1. Instalați driverele Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Înregistrați locația driverului cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Verificarea mărimii memoriei Nvidia GPU (Necesari 12GB memorie GPU)

    ```bash
    nvidia-smi
    ```

1. Golirea cache-ului: Dacă folosiți PyTorch, puteți apela torch.cuda.empty_cache() pentru a elibera toată memoria cache neutilizată astfel încât să poată fi folosită de alte aplicații GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verificarea Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Realizați următoarele sarcini pentru a crea un token Hugging Face.

    - Navigați la [pagina de setări Hugging Face Token](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selectați **New token**.
    - Introduceți **Numele** proiectului pe care doriți să îl folosiți.
    - Selectați **Tipul** pe **Write**.

> [!NOTE]
>
> Dacă întâmpinați următoarea eroare:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pentru a rezolva aceasta, tastați următoarea comandă în terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->