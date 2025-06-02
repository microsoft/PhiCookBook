<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-05-27T02:39:04+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "de"
}
-->
# Mitwirken

Dieses Projekt freut sich über Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, in der Sie erklären, dass Sie das Recht haben und tatsächlich die Rechte einräumen, Ihre Beiträge zu verwenden. Details finden Sie unter [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Wenn Sie eine Pull Request einreichen, bestimmt ein CLA-Bot automatisch, ob Sie eine CLA vorlegen müssen, und versieht die PR entsprechend (z. B. Statusprüfung, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories erledigen, die unsere CLA verwenden.

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen. Für weitere Informationen lesen Sie die [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Hinweise zum Erstellen von Issues

Bitte öffnen Sie keine GitHub-Issues für allgemeine Supportfragen, da die GitHub-Liste für Feature-Anfragen und Bug-Reports genutzt werden sollte. So können wir tatsächliche Probleme oder Fehler im Code leichter nachverfolgen und die allgemeine Diskussion von der eigentlichen Codebasis trennen.

## Wie man beiträgt

### Richtlinien für Pull Requests

Beim Einreichen einer Pull Request (PR) im Phi-3 CookBook Repository beachten Sie bitte folgende Richtlinien:

- **Repository forken**: Forken Sie das Repository immer in Ihr eigenes Konto, bevor Sie Änderungen vornehmen.

- **Getrennte Pull Requests (PR)**:
  - Reichen Sie jede Art von Änderung in einer eigenen Pull Request ein. Zum Beispiel sollten Fehlerbehebungen und Dokumentationsupdates in separaten PRs eingereicht werden.
  - Tippfehlerkorrekturen und kleinere Dokumentationsänderungen können, wenn sinnvoll, in einer einzigen PR zusammengefasst werden.

- **Umgang mit Merge-Konflikten**: Wenn Ihre Pull Request Merge-Konflikte anzeigt, aktualisieren Sie Ihren lokalen `main` Branch, um dem Hauptrepository zu entsprechen, bevor Sie Ihre Änderungen vornehmen.

- **Übersetzungseinreichungen**: Bei der Einreichung einer Übersetzungs-PR stellen Sie sicher, dass der Übersetzungsordner Übersetzungen für alle Dateien des Originalordners enthält.

### Schreibregeln

Um Konsistenz in allen Dokumenten sicherzustellen, verwenden Sie bitte die folgenden Richtlinien:

- **URL-Formatierung**: Umschließen Sie alle URLs mit eckigen Klammern, gefolgt von runden Klammern, ohne zusätzliche Leerzeichen dazwischen oder innen. Zum Beispiel: `[example](https://www.microsoft.com)`.

- **Relative Links**: Verwenden Sie `./` für relative Links, die auf Dateien oder Ordner im aktuellen Verzeichnis verweisen, und `../` für solche im übergeordneten Verzeichnis. Zum Beispiel: `[example](../../path/to/file)` oder `[example](../../../path/to/file)`.

- **Keine länderspezifischen Sprachcodes**: Stellen Sie sicher, dass Ihre Links keine länderspezifischen Sprachcodes enthalten. Vermeiden Sie zum Beispiel `/en-us/` oder `/en/`.

- **Bildspeicherung**: Speichern Sie alle Bilder im `./imgs` Ordner.

- **Beschreibende Bildnamen**: Benennen Sie Bilder beschreibend mit englischen Buchstaben, Zahlen und Bindestrichen. Zum Beispiel: `example-image.jpg`.

## GitHub Workflows

Beim Einreichen einer Pull Request werden folgende Workflows ausgelöst, um die Änderungen zu überprüfen. Befolgen Sie die untenstehenden Anweisungen, damit Ihre Pull Request die Workflow-Prüfungen besteht:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Dieser Workflow stellt sicher, dass alle relativen Pfade in Ihren Dateien korrekt sind.

1. Um sicherzustellen, dass Ihre Links funktionieren, führen Sie folgende Schritte in VS Code aus:
    - Fahren Sie mit der Maus über einen Link in Ihren Dateien.
    - Drücken Sie **Strg + Klick**, um zum Link zu navigieren.
    - Wenn ein Link lokal nicht funktioniert, löst dies den Workflow aus und funktioniert auch auf GitHub nicht.

1. Um das Problem zu beheben, führen Sie die folgenden Schritte mit den von VS Code vorgeschlagenen Pfaden aus:
    - Geben Sie `./` oder `../` ein.
    - VS Code zeigt Ihnen basierend auf Ihrer Eingabe verfügbare Optionen an.
    - Folgen Sie dem Pfad, indem Sie auf die gewünschte Datei oder den Ordner klicken, um sicherzustellen, dass Ihr Pfad korrekt ist.

Nachdem Sie den richtigen relativen Pfad hinzugefügt haben, speichern und pushen Sie Ihre Änderungen.

### Check URLs Don't Have Locale

Dieser Workflow stellt sicher, dass keine Web-URL einen länderspezifischen Sprachcode enthält. Da dieses Repository weltweit zugänglich ist, ist es wichtig, dass URLs keine lokalen Sprachcodes enthalten.

1. Um zu überprüfen, dass Ihre URLs keine länderspezifischen Sprachcodes enthalten, führen Sie folgende Schritte aus:

    - Prüfen Sie, ob Texte wie `/en-us/`, `/en/` oder andere Sprachcodes in den URLs vorhanden sind.
    - Wenn diese nicht in Ihren URLs vorkommen, besteht die Prüfung.

1. Um das Problem zu beheben, führen Sie folgende Schritte aus:
    - Öffnen Sie die vom Workflow markierte Datei.
    - Entfernen Sie den länderspezifischen Sprachcode aus den URLs.

Nachdem Sie den Sprachcode entfernt haben, speichern und pushen Sie Ihre Änderungen.

### Check Broken Urls

Dieser Workflow stellt sicher, dass jede Web-URL in Ihren Dateien funktioniert und einen Statuscode 200 zurückgibt.

1. Um zu überprüfen, dass Ihre URLs korrekt funktionieren, führen Sie folgende Schritte aus:
    - Prüfen Sie den Status der URLs in Ihren Dateien.

2. Um defekte URLs zu beheben, führen Sie folgende Schritte aus:
    - Öffnen Sie die Datei, die die defekte URL enthält.
    - Aktualisieren Sie die URL auf die korrekte.

Nachdem Sie die URLs korrigiert haben, speichern und pushen Sie Ihre Änderungen.

> [!NOTE]
>
> Es kann vorkommen, dass die URL-Prüfung fehlschlägt, obwohl der Link erreichbar ist. Dies kann verschiedene Gründe haben, unter anderem:
>
> - **Netzwerkbeschränkungen:** Die GitHub Actions-Server können Netzwerkbeschränkungen haben, die den Zugriff auf bestimmte URLs verhindern.
> - **Timeout-Probleme:** URLs, die zu lange zum Antworten brauchen, können im Workflow einen Timeout-Fehler auslösen.
> - **Vorübergehende Serverprobleme:** Gelegentliche Serverausfälle oder Wartungen können eine URL während der Prüfung temporär unerreichbar machen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.