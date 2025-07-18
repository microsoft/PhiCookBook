<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-07-16T16:39:43+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "de"
}
-->
# Willkommen zu deiner VS Code-Erweiterung

## Was sich im Ordner befindet

* Dieser Ordner enthält alle Dateien, die für deine Erweiterung notwendig sind.
* `package.json` – dies ist die Manifestdatei, in der du deine Erweiterung und den Befehl deklarierst.
  * Das Beispiel-Plugin registriert einen Befehl und definiert dessen Titel und Befehlsnamen. Mit diesen Informationen kann VS Code den Befehl in der Befehlspalette anzeigen. Das Plugin muss dafür noch nicht geladen werden.
* `src/extension.ts` – dies ist die Hauptdatei, in der du die Implementierung deines Befehls bereitstellst.
  * Die Datei exportiert eine Funktion, `activate`, die beim allerersten Aktivieren deiner Erweiterung aufgerufen wird (in diesem Fall durch Ausführen des Befehls). Innerhalb der `activate`-Funktion rufen wir `registerCommand` auf.
  * Wir übergeben die Funktion mit der Implementierung des Befehls als zweiten Parameter an `registerCommand`.

## Einrichtung

* Installiere die empfohlenen Erweiterungen (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner und dbaeumer.vscode-eslint)

## Sofort loslegen

* Drücke `F5`, um ein neues Fenster mit deiner geladenen Erweiterung zu öffnen.
* Führe deinen Befehl über die Befehlspalette aus, indem du (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf dem Mac) drückst und `Hello World` eingibst.
* Setze Breakpoints in deinem Code in `src/extension.ts`, um deine Erweiterung zu debuggen.
* Finde die Ausgabe deiner Erweiterung in der Debug-Konsole.

## Änderungen vornehmen

* Du kannst die Erweiterung über die Debug-Symbolleiste neu starten, nachdem du Code in `src/extension.ts` geändert hast.
* Du kannst auch das VS Code-Fenster mit deiner Erweiterung neu laden (`Ctrl+R` oder `Cmd+R` auf dem Mac), um deine Änderungen zu übernehmen.

## Die API erkunden

* Du kannst den vollständigen Satz unserer API öffnen, indem du die Datei `node_modules/@types/vscode/index.d.ts` öffnest.

## Tests ausführen

* Installiere den [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Starte die "watch"-Aufgabe über den Befehl **Tasks: Run Task**. Stelle sicher, dass diese läuft, sonst werden Tests möglicherweise nicht erkannt.
* Öffne die Testansicht in der Aktivitätsleiste und klicke auf die Schaltfläche „Run Test“ oder nutze die Tastenkombination `Ctrl/Cmd + ; A`
* Sieh dir die Testergebnisse in der Test Results-Ansicht an.
* Nimm Änderungen an `src/test/extension.test.ts` vor oder erstelle neue Testdateien im `test`-Ordner.
  * Der bereitgestellte Test Runner berücksichtigt nur Dateien, die dem Namensmuster `**.test.ts` entsprechen.
  * Du kannst im `test`-Ordner Unterordner anlegen, um deine Tests beliebig zu strukturieren.

## Weiterführende Schritte

* Reduziere die Größe der Erweiterung und verbessere die Startzeit, indem du deine Erweiterung [bündelst](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Veröffentliche deine Erweiterung](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) im VS Code Extension Marketplace.
* Automatisiere Builds, indem du [Continuous Integration einrichtest](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.