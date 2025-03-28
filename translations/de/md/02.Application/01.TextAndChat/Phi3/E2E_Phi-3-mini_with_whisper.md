<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-03-27T10:46:26+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-mini_with_whisper.md",
  "language_code": "de"
}
-->
# Interaktiver Phi 3 Mini 4K Instruct Chatbot mit Whisper

## Überblick

Der Interaktive Phi 3 Mini 4K Instruct Chatbot ist ein Tool, das es Nutzern ermöglicht, mit der Microsoft Phi 3 Mini 4K Instruct Demo über Text- oder Audioeingaben zu interagieren. Der Chatbot kann für verschiedene Aufgaben verwendet werden, wie Übersetzungen, Wetterupdates und allgemeine Informationsbeschaffung.

### Erste Schritte

Um diesen Chatbot zu verwenden, folgen Sie einfach diesen Anweisungen:

1. Öffnen Sie ein neues [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. Im Hauptfenster des Notebooks sehen Sie eine Chatbox-Oberfläche mit einem Texteingabefeld und einem „Senden“-Button.
3. Um den textbasierten Chatbot zu nutzen, geben Sie Ihre Nachricht einfach in das Texteingabefeld ein und klicken Sie auf den „Senden“-Button. Der Chatbot antwortet mit einer Audiodatei, die direkt im Notebook abgespielt werden kann.

**Hinweis**: Dieses Tool erfordert eine GPU und Zugriff auf die Microsoft Phi-3 und OpenAI Whisper Modelle, die für Spracherkennung und Übersetzung verwendet werden.

### GPU-Anforderungen

Um diese Demo auszuführen, benötigen Sie 12 GB GPU-Speicher.

Die Speicheranforderungen für das **Microsoft-Phi-3-Mini-4K Instruct** Demo auf einer GPU hängen von mehreren Faktoren ab, wie der Größe der Eingabedaten (Audio oder Text), der Sprache für die Übersetzung, der Geschwindigkeit des Modells und dem verfügbaren Speicher auf der GPU.

Im Allgemeinen ist das Whisper-Modell für die Ausführung auf GPUs konzipiert. Die empfohlene Mindestmenge an GPU-Speicher für die Ausführung des Whisper-Modells beträgt 8 GB, es kann jedoch größere Speichermengen verarbeiten, wenn erforderlich.

Es ist wichtig zu beachten, dass die Verarbeitung großer Datenmengen oder eines hohen Anfragevolumens beim Modell mehr GPU-Speicher erfordern und/oder Leistungsprobleme verursachen kann. Es wird empfohlen, Ihren Anwendungsfall mit verschiedenen Konfigurationen zu testen und die Speichernutzung zu überwachen, um die optimalen Einstellungen für Ihre spezifischen Anforderungen zu bestimmen.

## E2E-Beispiel für Interaktiven Phi 3 Mini 4K Instruct Chatbot mit Whisper

Das Jupyter Notebook mit dem Titel [Interactive Phi 3 Mini 4K Instruct Chatbot mit Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstriert, wie man die Microsoft Phi 3 Mini 4K Instruct Demo verwendet, um Text aus Audio- oder schriftlichen Eingaben zu generieren. Das Notebook definiert mehrere Funktionen:

1. `tts_file_name(text)`: Diese Funktion generiert einen Dateinamen basierend auf dem Eingabetext, um die erstellte Audiodatei zu speichern.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Diese Funktion nutzt die Edge TTS API, um eine Audiodatei aus einer Liste von Textabschnitten zu generieren. Die Eingabeparameter sind die Liste der Abschnitte, die Sprechgeschwindigkeit, der Stimmenname und der Ausgabepfad zum Speichern der erstellten Audiodatei.
1. `talk(input_text)`: Diese Funktion erstellt eine Audiodatei, indem sie die Edge TTS API verwendet und sie unter einem zufälligen Dateinamen im Verzeichnis /content/audio speichert. Der Eingabeparameter ist der Text, der in Sprache umgewandelt werden soll.
1. `run_text_prompt(message, chat_history)`: Diese Funktion nutzt die Microsoft Phi 3 Mini 4K Instruct Demo, um eine Audiodatei aus einer Nachrichteneingabe zu generieren und fügt sie der Chat-Historie hinzu.
1. `run_audio_prompt(audio, chat_history)`: Diese Funktion konvertiert eine Audiodatei in Text mithilfe der Whisper Model API und übergibt sie an die `run_text_prompt()`-Funktion.
1. Der Code startet eine Gradio-App, die es Nutzern ermöglicht, mit der Phi 3 Mini 4K Instruct Demo zu interagieren, indem sie entweder Nachrichten eingeben oder Audiodateien hochladen. Die Ausgabe wird als Textnachricht innerhalb der App angezeigt.

## Fehlerbehebung

Installation der Cuda GPU-Treiber

1. Stellen Sie sicher, dass Ihre Linux-Anwendungen auf dem neuesten Stand sind.

    ```bash
    sudo apt update
    ```

1. Installieren Sie die Cuda-Treiber.

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrieren Sie den Standort des Cuda-Treibers.

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Überprüfen Sie die Nvidia GPU-Speichergröße (erforderlich: 12 GB GPU-Speicher).

    ```bash
    nvidia-smi
    ```

1. Cache leeren: Wenn Sie PyTorch verwenden, können Sie torch.cuda.empty_cache() aufrufen, um alle nicht genutzten zwischengespeicherten Speicher freizugeben, damit sie von anderen GPU-Anwendungen verwendet werden können.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Überprüfen Sie Nvidia Cuda.

    ```bash
    nvcc --version
    ```

1. Führen Sie die folgenden Aufgaben aus, um ein Hugging Face Token zu erstellen.

    - Navigieren Sie zur [Hugging Face Token Settings-Seite](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Wählen Sie **Neues Token** aus.
    - Geben Sie den Projekt-**Namen** ein, den Sie verwenden möchten.
    - Wählen Sie **Typ** auf **Schreiben**.

> **Hinweis**
>
> Falls Sie auf den folgenden Fehler stoßen:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Um dies zu beheben, geben Sie den folgenden Befehl in Ihr Terminal ein.
>
> ```bash
> sudo ldconfig
> ```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatische Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.