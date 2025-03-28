<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-03-27T04:18:16+00:00",
  "source_file": "code\\07.Lab\\01\\AIPC\\extensions\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "de"
}
-->
# Willkommen zu Ihrer VS Code-Erweiterung

## Was ist in diesem Ordner

* Dieser Ordner enthält alle Dateien, die für Ihre Erweiterung notwendig sind.
* `package.json` - dies ist die Manifestdatei, in der Sie Ihre Erweiterung und den Befehl deklarieren.
  * Das Beispiel-Plugin registriert einen Befehl und definiert dessen Titel und Befehlsnamen. Mit diesen Informationen kann VS Code den Befehl in der Befehlspalette anzeigen. Es muss das Plugin noch nicht laden.
* `src/extension.ts` - dies ist die Hauptdatei, in der Sie die Implementierung Ihres Befehls bereitstellen.
  * Die Datei exportiert eine Funktion, `activate`, die das allererste Mal aufgerufen wird, wenn Ihre Erweiterung aktiviert wird (in diesem Fall durch die Ausführung des Befehls). Innerhalb der `activate`-Funktion rufen wir `registerCommand` auf.
  * Wir übergeben die Funktion, die die Implementierung des Befehls enthält, als zweiten Parameter an `registerCommand`.

## Einrichtung

* Installieren Sie die empfohlenen Erweiterungen (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner und dbaeumer.vscode-eslint).

## Schnell starten

* Drücken Sie `F5`, um ein neues Fenster mit Ihrer geladenen Erweiterung zu öffnen.
* Führen Sie Ihren Befehl aus der Befehlspalette aus, indem Sie (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf einem Mac) drücken und `Hello World` eingeben.
* Setzen Sie Haltepunkte in Ihrem Code innerhalb von `src/extension.ts`, um Ihre Erweiterung zu debuggen.
* Finden Sie die Ausgabe Ihrer Erweiterung in der Debug-Konsole.

## Änderungen vornehmen

* Sie können die Erweiterung über die Debug-Toolbar neu starten, nachdem Sie den Code in `src/extension.ts` geändert haben.
* Sie können auch das VS Code-Fenster mit Ihrer Erweiterung neu laden (`Ctrl+R` oder `Cmd+R` auf einem Mac), um Ihre Änderungen zu laden.

## API erkunden

* Sie können das vollständige Set unserer API öffnen, wenn Sie die Datei `node_modules/@types/vscode/index.d.ts` öffnen.

## Tests ausführen

* Installieren Sie den [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Führen Sie die Aufgabe "watch" über den Befehl **Tasks: Run Task** aus. Stellen Sie sicher, dass diese Aufgabe läuft, da Tests sonst möglicherweise nicht erkannt werden.
* Öffnen Sie die Testansicht in der Aktivitätsleiste und klicken Sie auf die Schaltfläche "Run Test", oder verwenden Sie die Tastenkombination `Ctrl/Cmd + ; A`.
* Sehen Sie sich die Ausgabe des Testergebnisses in der Test-Ergebnisansicht an.
* Nehmen Sie Änderungen an `src/test/extension.test.ts` vor oder erstellen Sie neue Testdateien im Ordner `test`.
  * Der bereitgestellte Test-Runner berücksichtigt nur Dateien, die dem Namensmuster `**.test.ts` entsprechen.
  * Sie können Ordner innerhalb des `test`-Ordners erstellen, um Ihre Tests beliebig zu strukturieren.

## Weiterführende Schritte

* Reduzieren Sie die Größe der Erweiterung und verbessern Sie die Startzeit, indem Sie [Ihre Erweiterung bündeln](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Veröffentlichen Sie Ihre Erweiterung](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) auf dem VS Code-Erweiterungs-Marktplatz.
* Automatisieren Sie Builds, indem Sie [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) einrichten.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.