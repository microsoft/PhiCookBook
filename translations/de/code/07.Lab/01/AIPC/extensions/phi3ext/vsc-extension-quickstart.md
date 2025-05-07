<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-07T10:15:10+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "de"
}
-->
# Willkommen zu Ihrer VS Code-Erweiterung

## Was sich im Ordner befindet

* Dieser Ordner enthält alle Dateien, die für Ihre Erweiterung notwendig sind.
* `package.json` – dies ist die Manifestdatei, in der Sie Ihre Erweiterung und den Befehl deklarieren.
  * Das Beispiel-Plugin registriert einen Befehl und definiert dessen Titel und Befehlsnamen. Mit diesen Informationen kann VS Code den Befehl in der Befehlspalette anzeigen. Das Plugin muss dafür noch nicht geladen werden.
* `src/extension.ts` – dies ist die Hauptdatei, in der Sie die Implementierung Ihres Befehls bereitstellen.
  * Die Datei exportiert eine Funktion, `activate`, die beim ersten Aktivieren Ihrer Erweiterung (in diesem Fall durch Ausführen des Befehls) aufgerufen wird. Innerhalb der Funktion `activate` rufen wir `registerCommand` auf.
  * Die Funktion mit der Implementierung des Befehls übergeben wir als zweiten Parameter an `registerCommand`.

## Einrichtung

* Installieren Sie die empfohlenen Erweiterungen (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner und dbaeumer.vscode-eslint)


## Sofort loslegen

* Drücken Sie `F5`, um ein neues Fenster mit Ihrer geladenen Erweiterung zu öffnen.
* Führen Sie Ihren Befehl über die Befehlspalette aus, indem Sie (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf dem Mac) drücken und `Hello World` eingeben.
* Setzen Sie Breakpoints in Ihrem Code in `src/extension.ts`, um Ihre Erweiterung zu debuggen.
* Die Ausgabe Ihrer Erweiterung finden Sie in der Debug-Konsole.

## Änderungen vornehmen

* Sie können die Erweiterung nach Änderungen im Code in `src/extension.ts` über die Debug-Symbolleiste neu starten.
* Sie können auch das VS Code-Fenster mit Ihrer Erweiterung neu laden (`Ctrl+R` oder `Cmd+R` auf dem Mac), um Ihre Änderungen zu übernehmen.


## Die API erkunden

* Sie können das komplette API-Set öffnen, indem Sie die Datei `node_modules/@types/vscode/index.d.ts` öffnen.

## Tests ausführen

* Installieren Sie den [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Führen Sie die Aufgabe „watch“ über den Befehl **Tasks: Run Task** aus. Stellen Sie sicher, dass diese läuft, da sonst Tests nicht gefunden werden.
* Öffnen Sie die Testansicht über die Aktivitätsleiste und klicken Sie auf die Schaltfläche „Run Test“ oder verwenden Sie die Tastenkombination `Ctrl/Cmd + ; A`
* Sehen Sie die Testergebnisse in der Ansicht Test Results ein.
* Nehmen Sie Änderungen in `src/test/extension.test.ts` vor oder erstellen Sie neue Testdateien im Ordner `test`.
  * Der bereitgestellte Test Runner berücksichtigt nur Dateien, die dem Namensmuster `**.test.ts` entsprechen.
  * Sie können im Ordner `test` Unterordner anlegen, um Ihre Tests beliebig zu strukturieren.

## Weiterführende Schritte

* Verringern Sie die Größe der Erweiterung und verbessern Sie die Startzeit, indem Sie Ihre Erweiterung [bündeln](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Veröffentlichen Sie Ihre Erweiterung](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) im VS Code-Erweiterungsmarkt.
* Automatisieren Sie Builds durch das Einrichten von [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.