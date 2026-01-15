<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:01:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "de"
}
-->
# Interaktiver Phi 3 Mini 4K Instruct Chatbot mit Whisper

## Überblick

Der interaktive Phi 3 Mini 4K Instruct Chatbot ist ein Tool, das es Benutzern ermöglicht, mit der Microsoft Phi 3 Mini 4K instruct Demo über Texteingabe oder Audioeingabe zu interagieren. Der Chatbot kann für verschiedene Aufgaben verwendet werden, wie z. B. Übersetzungen, Wetterupdates und allgemeine Informationsbeschaffung.

### Erste Schritte

Um diesen Chatbot zu verwenden, befolgen Sie einfach diese Anweisungen:

1. Öffnen Sie ein neues [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Im Hauptfenster des Notebooks sehen Sie eine Chatbox-Oberfläche mit einem Texteingabefeld und einer "Send"-Schaltfläche.
3. Um den textbasierten Chatbot zu verwenden, geben Sie einfach Ihre Nachricht in das Texteingabefeld ein und klicken Sie auf die Schaltfläche "Send". Der Chatbot antwortet mit einer Audiodatei, die direkt im Notebook abgespielt werden kann.

**Hinweis**: Dieses Tool erfordert eine GPU und Zugriff auf die Microsoft Phi-3- und OpenAI Whisper-Modelle, die für Spracherkennung und Übersetzung verwendet werden.

### GPU-Anforderungen

Um diese Demo auszuführen, benötigen Sie 12 GB GPU-Speicher.

Die Speicheranforderungen für die Ausführung der **Microsoft-Phi-3-Mini-4K instruct** Demo auf einer GPU hängen von mehreren Faktoren ab, z. B. der Größe der Eingabedaten (Audio oder Text), der verwendeten Sprache für die Übersetzung, der Geschwindigkeit des Modells und dem verfügbaren Speicher auf der GPU.

Im Allgemeinen ist das Whisper-Modell darauf ausgelegt, auf GPUs zu laufen. Die empfohlene Mindestmenge an GPU-Speicher für die Ausführung des Whisper-Modells beträgt 8 GB, es kann jedoch größere Speichergrößen verarbeiten, wenn erforderlich.

Es ist wichtig zu beachten, dass das Ausführen großer Datenmengen oder eines hohen Aufkommens von Anfragen an das Modell mehr GPU-Speicher erfordern und/oder Leistungsprobleme verursachen kann. Es wird empfohlen, Ihren Anwendungsfall mit verschiedenen Konfigurationen zu testen und die Speichernutzung zu überwachen, um die optimalen Einstellungen für Ihre spezifischen Bedürfnisse zu ermitteln.

## E2E-Beispiel für den interaktiven Phi 3 Mini 4K Instruct Chatbot mit Whisper

Das Jupyter-Notebook mit dem Titel [Interaktiver Phi 3 Mini 4K Instruct Chatbot mit Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) zeigt, wie man die Microsoft Phi 3 Mini 4K instruct Demo verwendet, um Text aus Audio- oder geschriebenem Texteingang zu erzeugen. Das Notebook definiert mehrere Funktionen:

1. `tts_file_name(text)`: Diese Funktion erzeugt einen Dateinamen basierend auf dem eingegebenen Text zum Speichern der erzeugten Audiodatei.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Diese Funktion verwendet die Edge TTS API, um aus einer Liste von Textabschnitten eine Audiodatei zu generieren. Die Eingabeparameter sind die Liste der Abschnitte, die Sprechgeschwindigkeit, der Stimmname und der Ausgabepfad zum Speichern der erzeugten Audiodatei.
1. `talk(input_text)`: Diese Funktion erzeugt eine Audiodatei über die Edge TTS API und speichert sie unter einem zufälligen Dateinamen im Verzeichnis /content/audio. Der Eingabeparameter ist der zu sprechende Text.
1. `run_text_prompt(message, chat_history)`: Diese Funktion verwendet die Microsoft Phi 3 Mini 4K instruct Demo, um aus einer Nachricht eine Audiodatei zu generieren und hängt diese an den Chatverlauf an.
1. `run_audio_prompt(audio, chat_history)`: Diese Funktion wandelt eine Audiodatei mit der Whisper Modell-API in Text um und übergibt diesen an die Funktion `run_text_prompt()`.
1. Der Code startet eine Gradio-App, die es Benutzern ermöglicht, mit der Phi 3 Mini 4K instruct Demo zu interagieren, indem sie Nachrichten eintippen oder Audiodateien hochladen. Die Ausgabe wird als Textnachricht innerhalb der App angezeigt.

## Fehlerbehebung

Installation von Cuda GPU-Treibern

1. Stellen Sie sicher, dass Ihre Linux-Anwendungen aktuell sind

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

1. Überprüfen Sie die Nvidia GPU-Speichergröße (benötigt 12 GB GPU-Speicher)

    ```bash
    nvidia-smi
    ```

1. Cache leeren: Wenn Sie PyTorch verwenden, können Sie torch.cuda.empty_cache() aufrufen, um nicht verwendeten zwischengespeicherten Speicher freizugeben, damit andere GPU-Anwendungen ihn nutzen können.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda überprüfen

    ```bash
    nvcc --version
    ```

1. Führen Sie die folgenden Schritte aus, um ein Hugging Face Token zu erstellen.

    - Navigieren Sie zur [Hugging Face Token-Einstellungsseite](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Wählen Sie **Neues Token**.
    - Geben Sie den Projektnamen ein, den Sie verwenden möchten.
    - Wählen Sie als **Typ** die Option **Write** aus.

> [!NOTE]
>
> Wenn Sie folgenden Fehler erhalten:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Um dies zu beheben, geben Sie folgenden Befehl in Ihrem Terminal ein.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, bitten wir zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->