<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:13:15+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "de"
}
-->
# Interaktiver Phi 3 Mini 4K Instruct Chatbot mit Whisper

## Überblick

Der interaktive Phi 3 Mini 4K Instruct Chatbot ist ein Tool, mit dem Nutzer über Texteingabe oder Audioeingabe mit der Microsoft Phi 3 Mini 4K Instruct-Demo interagieren können. Der Chatbot kann für verschiedene Aufgaben verwendet werden, wie z. B. Übersetzungen, Wetterupdates und allgemeine Informationsbeschaffung.

### Erste Schritte

Um diesen Chatbot zu verwenden, folgen Sie einfach diesen Anweisungen:

1. Öffnen Sie ein neues [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Im Hauptfenster des Notebooks sehen Sie eine Chatbox-Oberfläche mit einem Texteingabefeld und einem „Send“-Button.
3. Um den textbasierten Chatbot zu nutzen, geben Sie einfach Ihre Nachricht in das Texteingabefeld ein und klicken Sie auf „Send“. Der Chatbot antwortet mit einer Audiodatei, die direkt im Notebook abgespielt werden kann.

**Hinweis**: Dieses Tool benötigt eine GPU sowie Zugriff auf die Microsoft Phi-3 und OpenAI Whisper Modelle, die für Spracherkennung und Übersetzung verwendet werden.

### GPU-Anforderungen

Um diese Demo auszuführen, benötigen Sie 12 GB GPU-Speicher.

Der Speicherbedarf für die Ausführung der **Microsoft-Phi-3-Mini-4K instruct** Demo auf einer GPU hängt von verschiedenen Faktoren ab, wie der Größe der Eingabedaten (Audio oder Text), der verwendeten Sprache für die Übersetzung, der Geschwindigkeit des Modells und dem verfügbaren GPU-Speicher.

Im Allgemeinen ist das Whisper-Modell für den Betrieb auf GPUs ausgelegt. Die empfohlene Mindestmenge an GPU-Speicher für das Whisper-Modell beträgt 8 GB, es kann jedoch bei Bedarf auch größere Speichermengen nutzen.

Es ist wichtig zu beachten, dass die Verarbeitung großer Datenmengen oder eines hohen Anfragevolumens mehr GPU-Speicher erfordern und/oder zu Leistungsproblemen führen kann. Es wird empfohlen, Ihren Anwendungsfall mit verschiedenen Konfigurationen zu testen und die Speichernutzung zu überwachen, um die optimalen Einstellungen für Ihre spezifischen Anforderungen zu ermitteln.

## E2E-Beispiel für den interaktiven Phi 3 Mini 4K Instruct Chatbot mit Whisper

Das Jupyter-Notebook mit dem Titel [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) zeigt, wie man die Microsoft Phi 3 Mini 4K Instruct Demo verwendet, um Text aus Audio- oder geschriebenen Texteingaben zu generieren. Das Notebook definiert mehrere Funktionen:

1. `tts_file_name(text)`: Diese Funktion erzeugt einen Dateinamen basierend auf dem Eingabetext, um die generierte Audiodatei zu speichern.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Diese Funktion nutzt die Edge TTS API, um aus einer Liste von Textabschnitten eine Audiodatei zu erzeugen. Die Eingabeparameter sind die Liste der Textabschnitte, die Sprechgeschwindigkeit, der Name der Stimme und der Speicherpfad für die generierte Audiodatei.
1. `talk(input_text)`: Diese Funktion erzeugt eine Audiodatei mit der Edge TTS API und speichert sie unter einem zufälligen Dateinamen im Verzeichnis /content/audio. Der Eingabeparameter ist der Text, der in Sprache umgewandelt werden soll.
1. `run_text_prompt(message, chat_history)`: Diese Funktion verwendet die Microsoft Phi 3 Mini 4K Instruct Demo, um aus einer Nachricht eine Audiodatei zu generieren und fügt diese dem Chatverlauf hinzu.
1. `run_audio_prompt(audio, chat_history)`: Diese Funktion wandelt eine Audiodatei mit dem Whisper Modell in Text um und übergibt diesen an die Funktion `run_text_prompt()`.
1. Der Code startet eine Gradio-App, die es Nutzern ermöglicht, mit der Phi 3 Mini 4K Instruct Demo zu interagieren, indem sie Nachrichten eingeben oder Audiodateien hochladen. Die Ausgabe wird als Textnachricht innerhalb der App angezeigt.

## Fehlerbehebung

Installation der Cuda GPU-Treiber

1. Stellen Sie sicher, dass Ihre Linux-Anwendungen auf dem neuesten Stand sind

    ```bash
    sudo apt update
    ```

1. Installieren Sie die Cuda-Treiber

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrieren Sie den Speicherort des Cuda-Treibers

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Überprüfen der Nvidia GPU-Speichergröße (Benötigt 12 GB GPU-Speicher)

    ```bash
    nvidia-smi
    ```

1. Cache leeren: Wenn Sie PyTorch verwenden, können Sie torch.cuda.empty_cache() aufrufen, um nicht genutzten Cache-Speicher freizugeben, damit er von anderen GPU-Anwendungen verwendet werden kann

    ```python
    torch.cuda.empty_cache() 
    ```

1. Überprüfen von Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Führen Sie die folgenden Schritte aus, um ein Hugging Face Token zu erstellen.

    - Navigieren Sie zur [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Wählen Sie **New token**.
    - Geben Sie den Projektnamen ein, den Sie verwenden möchten.
    - Wählen Sie als **Type** die Option **Write**.

> **Hinweis**
>
> Wenn Sie auf den folgenden Fehler stoßen:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Um das Problem zu beheben, geben Sie den folgenden Befehl in Ihrem Terminal ein.
>
> ```bash
> sudo ldconfig
> ```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.