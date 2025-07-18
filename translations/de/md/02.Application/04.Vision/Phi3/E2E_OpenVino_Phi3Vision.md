<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:00:34+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "de"
}
-->
Diese Demo zeigt, wie man ein vortrainiertes Modell verwendet, um basierend auf einem Bild und einer Texteingabe Python-Code zu generieren.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Hier eine Schritt-für-Schritt-Erklärung:

1. **Imports und Einrichtung**:
   - Die benötigten Bibliotheken und Module werden importiert, darunter `requests`, `PIL` für die Bildverarbeitung und `transformers` für die Modellverwaltung und -verarbeitung.

2. **Bild laden und anzeigen**:
   - Eine Bilddatei (`demo.png`) wird mit der `PIL`-Bibliothek geöffnet und angezeigt.

3. **Definieren der Eingabeaufforderung**:
   - Eine Nachricht wird erstellt, die das Bild enthält und die Aufforderung, Python-Code zu generieren, der das Bild verarbeitet und mit `plt` (matplotlib) speichert.

4. **Laden des Processors**:
   - Der `AutoProcessor` wird aus einem vortrainierten Modell geladen, das im Verzeichnis `out_dir` gespeichert ist. Dieser Processor verarbeitet die Text- und Bildeingaben.

5. **Erstellen der Eingabeaufforderung**:
   - Die Methode `apply_chat_template` wird verwendet, um die Nachricht in eine für das Modell geeignete Eingabeaufforderung zu formatieren.

6. **Verarbeiten der Eingaben**:
   - Die Eingabeaufforderung und das Bild werden in Tensoren umgewandelt, die das Modell verarbeiten kann.

7. **Festlegen der Generierungsparameter**:
   - Parameter für den Generierungsprozess des Modells werden definiert, darunter die maximale Anzahl neuer Tokens und ob die Ausgabe gesampelt werden soll.

8. **Generieren des Codes**:
   - Das Modell erzeugt basierend auf den Eingaben und den Generierungsparametern den Python-Code. Der `TextStreamer` wird verwendet, um die Ausgabe zu handhaben, wobei die Eingabeaufforderung und spezielle Tokens übersprungen werden.

9. **Ausgabe**:
   - Der generierte Code wird ausgegeben, der Python-Code enthalten sollte, um das Bild zu verarbeiten und wie in der Eingabeaufforderung angegeben zu speichern.

Diese Demo zeigt, wie man ein vortrainiertes Modell mit OpenVino nutzt, um dynamisch Code basierend auf Benutzereingaben und Bildern zu generieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.