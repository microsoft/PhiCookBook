<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-03-27T04:36:40+00:00",
  "source_file": "code\\07.Lab\\01\\Apple\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "de"
}
-->
# Willkommen bei deiner VS Code-Erweiterung

## Was ist in diesem Ordner

* Dieser Ordner enthält alle notwendigen Dateien für deine Erweiterung.
* `package.json` - dies ist die Manifest-Datei, in der du deine Erweiterung und Befehle deklarierst.
  * Das Beispiel-Plugin registriert einen Befehl und definiert dessen Titel und Befehlsnamen. Mit diesen Informationen kann VS Code den Befehl in der Befehlspalette anzeigen. Es muss das Plugin noch nicht laden.
* `src/extension.ts` - dies ist die Hauptdatei, in der du die Implementierung deines Befehls bereitstellst.
  * Die Datei exportiert eine Funktion, `activate`, die beim allerersten Aktivieren deiner Erweiterung aufgerufen wird (in diesem Fall durch Ausführen des Befehls). Innerhalb der `activate`-Funktion rufen wir `registerCommand` auf.
  * Wir übergeben die Funktion, die die Implementierung des Befehls enthält, als zweiten Parameter an `registerCommand`.

## Einrichtung

* Installiere die empfohlenen Erweiterungen (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner und dbaeumer.vscode-eslint).


## Sofort loslegen

* Drücke `F5`, um ein neues Fenster mit deiner geladenen Erweiterung zu öffnen.
* Führe deinen Befehl über die Befehlspalette aus, indem du (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf Mac) drückst und `Hello World` eingibst.
* Setze Haltepunkte in deinem Code innerhalb von `src/extension.ts`, um deine Erweiterung zu debuggen.
* Finde Ausgaben deiner Erweiterung in der Debug-Konsole.

## Änderungen vornehmen

* Du kannst die Erweiterung aus der Debug-Toolbar neu starten, nachdem du Änderungen am Code in `src/extension.ts` vorgenommen hast.
* Du kannst auch das VS Code-Fenster mit deiner Erweiterung neu laden (`Ctrl+R` oder `Cmd+R` auf Mac), um deine Änderungen zu laden.


## Die API erkunden

* Du kannst das vollständige Set unserer API öffnen, wenn du die Datei `node_modules/@types/vscode/index.d.ts` öffnest.

## Tests ausführen

* Installiere den [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Führe die "watch"-Aufgabe über den Befehl **Tasks: Run Task** aus. Stelle sicher, dass diese läuft, da Tests sonst möglicherweise nicht erkannt werden.
* Öffne die Testansicht in der Aktivitätsleiste und klicke auf die Schaltfläche "Run Test" oder nutze das Hotkey `Ctrl/Cmd + ; A`.
* Sieh dir die Ergebnisse der Tests in der Test Results-Ansicht an.
* Nimm Änderungen an `src/test/extension.test.ts` vor oder erstelle neue Testdateien im Ordner `test`.
  * Der bereitgestellte Test Runner berücksichtigt nur Dateien, die dem Namensmuster `**.test.ts` entsprechen.
  * Du kannst Ordner innerhalb des `test`-Ordners erstellen, um deine Tests beliebig zu strukturieren.

## Weiterführende Schritte

* Verringere die Größe der Erweiterung und verbessere die Startzeit, indem du [deine Erweiterung bündelst](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Veröffentliche deine Erweiterung](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) im VS Code-Erweiterungs-Marktplatz.
* Automatisiere Builds, indem du [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) einrichtest.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.