<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-07T10:12:13+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "de"
}
-->
# Willkommen zu Ihrer VS Code Extension

## Was sich im Ordner befindet

* Dieser Ordner enthält alle Dateien, die für Ihre Extension erforderlich sind.
* `package.json` - dies ist die Manifest-Datei, in der Sie Ihre Extension und den Befehl deklarieren.
  * Das Beispiel-Plugin registriert einen Befehl und definiert dessen Titel und Befehlsnamen. Mit diesen Informationen kann VS Code den Befehl in der Befehls-Palette anzeigen. Das Plugin muss dafür noch nicht geladen werden.
* `src/extension.ts` - dies ist die Hauptdatei, in der Sie die Implementierung Ihres Befehls bereitstellen.
  * Die Datei exportiert eine Funktion, `activate`, die beim allerersten Aktivieren Ihrer Extension (in diesem Fall durch Ausführen des Befehls) aufgerufen wird. Innerhalb der `activate`-Funktion rufen wir `registerCommand` auf.
  * Wir übergeben die Funktion mit der Implementierung des Befehls als zweiten Parameter an `registerCommand`.

## Einrichtung

* Installieren Sie die empfohlenen Extensions (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner und dbaeumer.vscode-eslint)


## Sofort loslegen

* Drücken Sie `F5`, um ein neues Fenster mit Ihrer geladenen Extension zu öffnen.
* Führen Sie Ihren Befehl über die Befehls-Palette aus, indem Sie (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf dem Mac) drücken und `Hello World` eingeben.
* Setzen Sie Breakpoints in Ihrem Code innerhalb von `src/extension.ts`, um Ihre Extension zu debuggen.
* Finden Sie die Ausgabe Ihrer Extension in der Debug-Konsole.

## Änderungen vornehmen

* Sie können die Extension über die Debug-Symbolleiste neu starten, nachdem Sie den Code in `src/extension.ts` geändert haben.
* Sie können auch das VS Code-Fenster mit Ihrer Extension neu laden (`Ctrl+R` oder `Cmd+R` auf dem Mac), um Ihre Änderungen zu übernehmen.


## Die API erkunden

* Sie können das vollständige API-Set öffnen, indem Sie die Datei `node_modules/@types/vscode/index.d.ts` öffnen.

## Tests ausführen

* Installieren Sie den [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Führen Sie die "watch"-Aufgabe über den Befehl **Tasks: Run Task** aus. Stellen Sie sicher, dass diese läuft, da sonst Tests nicht erkannt werden.
* Öffnen Sie die Testansicht über die Aktivitätsleiste und klicken Sie auf den Button „Run Test“ oder verwenden Sie die Tastenkombination `Ctrl/Cmd + ; A`
* Sehen Sie die Testergebnisse in der Ansicht „Test Results“.
* Nehmen Sie Änderungen an `src/test/extension.test.ts` vor oder erstellen Sie neue Testdateien im `test`-Ordner.
  * Der bereitgestellte Test Runner berücksichtigt nur Dateien, die dem Namensmuster `**.test.ts` entsprechen.
  * Sie können im `test`-Ordner weitere Unterordner anlegen, um Ihre Tests beliebig zu strukturieren.

## Weiterführende Schritte

* Reduzieren Sie die Größe der Extension und verbessern Sie die Startzeit, indem Sie [Ihre Extension bündeln](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Veröffentlichen Sie Ihre Extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) im VS Code Extension Marketplace.
* Automatisieren Sie Builds durch die Einrichtung von [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.