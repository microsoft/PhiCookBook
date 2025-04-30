<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-03-27T12:55:44+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_OpenVino_Phi3Vision.md",
  "language_code": "de"
}
-->
Diese Demo zeigt, wie ein vortrainiertes Modell verwendet werden kann, um Python-Code basierend auf einem Bild und einer Textaufforderung zu generieren.

[Beispielcode](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Hier ist eine schrittweise Erklärung:

1. **Importe und Einrichtung**:
   - Die notwendigen Bibliotheken und Module werden importiert, einschließlich `requests`, `PIL` für die Bildverarbeitung und `transformers` für die Modellverarbeitung.

2. **Bild laden und anzeigen**:
   - Eine Bilddatei (`demo.png`) wird mit der `PIL`-Bibliothek geöffnet und angezeigt.

3. **Definition der Aufforderung**:
   - Eine Nachricht wird erstellt, die das Bild und eine Anfrage enthält, Python-Code zu generieren, um das Bild zu verarbeiten und es mit `plt` (matplotlib) zu speichern.

4. **Prozessor laden**:
   - Der `AutoProcessor` wird aus einem vortrainierten Modell geladen, das im Verzeichnis `out_dir` angegeben ist. Dieser Prozessor verarbeitet die Text- und Bildeingaben.

5. **Erstellung der Aufforderung**:
   - Die Methode `apply_chat_template` wird verwendet, um die Nachricht in eine für das Modell geeignete Aufforderung zu formatieren.

6. **Verarbeitung der Eingaben**:
   - Die Aufforderung und das Bild werden in Tensoren umgewandelt, die vom Modell verstanden werden können.

7. **Festlegen der Generierungsparameter**:
   - Parameter für den Generierungsprozess des Modells werden definiert, einschließlich der maximalen Anzahl neuer Tokens, die generiert werden sollen, und ob die Ausgabe stochastisch sein soll.

8. **Code generieren**:
   - Das Modell generiert den Python-Code basierend auf den Eingaben und den Generierungsparametern. Die `TextStreamer` wird verwendet, um die Ausgabe zu verarbeiten, wobei die Aufforderung und spezielle Tokens übersprungen werden.

9. **Ausgabe**:
   - Der generierte Code wird ausgegeben und sollte Python-Code enthalten, um das Bild wie in der Aufforderung beschrieben zu verarbeiten und zu speichern.

Diese Demo zeigt, wie ein vortrainiertes Modell mit OpenVino genutzt werden kann, um Code dynamisch basierend auf Benutzereingaben und Bildern zu generieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.