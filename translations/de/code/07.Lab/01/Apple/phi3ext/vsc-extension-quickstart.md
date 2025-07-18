<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T16:57:59+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "de"
}
-->
# Willkommen zu deiner VS Code Extension

## Was sich im Ordner befindet

* Dieser Ordner enthält alle Dateien, die für deine Extension notwendig sind.
* `package.json` – dies ist die Manifestdatei, in der du deine Extension und den Befehl deklarierst.
  * Das Beispiel-Plugin registriert einen Befehl und definiert dessen Titel und Befehlsnamen. Mit diesen Informationen kann VS Code den Befehl in der Befehlspalette anzeigen. Das Plugin muss dafür noch nicht geladen werden.
* `src/extension.ts` – dies ist die Hauptdatei, in der du die Implementierung deines Befehls bereitstellst.
  * Die Datei exportiert eine Funktion, `activate`, die beim allerersten Aktivieren deiner Extension aufgerufen wird (in diesem Fall durch Ausführen des Befehls). Innerhalb der `activate`-Funktion rufen wir `registerCommand` auf.
  * Wir übergeben die Funktion mit der Implementierung des Befehls als zweiten Parameter an `registerCommand`.

## Einrichtung

* Installiere die empfohlenen Extensions (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner und dbaeumer.vscode-eslint)

## Sofort loslegen

* Drücke `F5`, um ein neues Fenster mit deiner geladenen Extension zu öffnen.
* Führe deinen Befehl über die Befehlspalette aus, indem du (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf dem Mac) drückst und `Hello World` eingibst.
* Setze Breakpoints in deinem Code in `src/extension.ts`, um deine Extension zu debuggen.
* Finde die Ausgabe deiner Extension in der Debug-Konsole.

## Änderungen vornehmen

* Du kannst die Extension über die Debug-Symbolleiste neu starten, nachdem du Code in `src/extension.ts` geändert hast.
* Du kannst auch das VS Code-Fenster mit deiner Extension neu laden (`Ctrl+R` oder `Cmd+R` auf dem Mac), um deine Änderungen zu übernehmen.

## Die API erkunden

* Du kannst das vollständige API-Set öffnen, indem du die Datei `node_modules/@types/vscode/index.d.ts` öffnest.

## Tests ausführen

* Installiere den [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Starte die "watch"-Aufgabe über den Befehl **Tasks: Run Task**. Stelle sicher, dass diese läuft, sonst werden Tests möglicherweise nicht erkannt.
* Öffne die Testansicht über die Aktivitätsleiste und klicke auf den Button „Run Test“ oder nutze die Tastenkombination `Ctrl/Cmd + ; A`
* Sieh dir die Testergebnisse in der Test Results-Ansicht an.
* Nimm Änderungen an `src/test/extension.test.ts` vor oder erstelle neue Testdateien im `test`-Ordner.
  * Der bereitgestellte Test Runner berücksichtigt nur Dateien, die dem Namensmuster `**.test.ts` entsprechen.
  * Du kannst im `test`-Ordner Unterordner anlegen, um deine Tests beliebig zu strukturieren.

## Weiterführende Schritte

* Reduziere die Größe der Extension und verbessere die Startzeit, indem du deine Extension [bündelst](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Veröffentliche deine Extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) im VS Code Extension Marketplace.
* Automatisiere Builds, indem du [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) einrichtest.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.