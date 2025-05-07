<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-07T10:08:51+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "de"
}
-->
# Contributing

Dieses Projekt freut sich über Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, in der Sie erklären, dass Sie das Recht haben und tatsächlich die Rechte einräumen, Ihre Beiträge zu verwenden. Details finden Sie unter [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Wenn Sie eine Pull-Anfrage einreichen, ermittelt ein CLA-Bot automatisch, ob Sie eine CLA vorlegen müssen und kennzeichnet die PR entsprechend (z. B. Statusprüfung, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories tun, die unsere CLA verwenden.

## Code of Conduct

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen. Für weitere Informationen lesen Sie die [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder wenden Sie sich bei Fragen oder Anmerkungen an [opencode@microsoft.com](mailto:opencode@microsoft.com).

## Vorsicht beim Erstellen von Issues

Bitte öffnen Sie keine GitHub-Issues für allgemeine Supportfragen, da die GitHub-Liste für Feature-Anfragen und Fehlerberichte gedacht ist. So können wir tatsächliche Probleme oder Bugs im Code besser verfolgen und die allgemeine Diskussion von der eigentlichen Codebasis getrennt halten.

## Wie man beiträgt

### Richtlinien für Pull Requests

Wenn Sie eine Pull-Anfrage (PR) im Phi-3 CookBook-Repository einreichen, beachten Sie bitte folgende Richtlinien:

- **Repository forken**: Forken Sie das Repository immer in Ihr eigenes Konto, bevor Sie Änderungen vornehmen.

- **Getrennte Pull Requests (PR)**:
  - Reichen Sie jede Art von Änderung in einem eigenen Pull Request ein. Beispielsweise sollten Fehlerbehebungen und Dokumentationsaktualisierungen in separaten PRs eingereicht werden.
  - Tippfehlerkorrekturen und kleinere Dokumentationsänderungen können, wo sinnvoll, in einem einzigen PR zusammengefasst werden.

- **Merge-Konflikte behandeln**: Wenn Ihr Pull Request Merge-Konflikte aufweist, aktualisieren Sie Ihren lokalen `main`-Branch, um das Hauptrepository zu spiegeln, bevor Sie Änderungen vornehmen.

- **Übersetzungseinreichungen**: Wenn Sie eine Übersetzungs-PR einreichen, stellen Sie sicher, dass der Übersetzungsordner Übersetzungen für alle Dateien im Originalordner enthält.

### Richtlinien für Übersetzungen

> [!IMPORTANT]
>
> Verwenden Sie beim Übersetzen von Texten in diesem Repository keine maschinelle Übersetzung. Übersetzen Sie nur in Sprachen, in denen Sie sicher sind.

Wenn Sie eine nicht-englische Sprache beherrschen, können Sie bei der Übersetzung helfen. Befolgen Sie diese Schritte, damit Ihre Übersetzungen korrekt integriert werden:

- **Übersetzungsordner erstellen**: Navigieren Sie zum entsprechenden Abschnittsordner und erstellen Sie einen Übersetzungsordner für die Sprache, zu der Sie beitragen. Zum Beispiel:
  - Für den Einführungsabschnitt: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Für den Schnellstartabschnitt: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Folgen Sie diesem Muster für weitere Abschnitte (03.Inference, 04.Finetuning usw.)

- **Relative Pfade aktualisieren**: Passen Sie beim Übersetzen die Ordnerstruktur an, indem Sie `../../` an den Anfang der relativen Pfade in den Markdown-Dateien setzen, damit die Links korrekt funktionieren. Zum Beispiel ändern Sie:
  - `(../../imgs/01/phi3aisafety.png)` zu `(../../../../imgs/01/phi3aisafety.png)`

- **Übersetzungen organisieren**: Jede übersetzte Datei sollte im entsprechenden Übersetzungsordner des Abschnitts abgelegt werden. Wenn Sie beispielsweise den Einführungsabschnitt ins Spanische übersetzen, erstellen Sie:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Vollständige PR einreichen**: Stellen Sie sicher, dass alle übersetzten Dateien eines Abschnitts in einem PR enthalten sind. Teilübersetzungen für einen Abschnitt werden nicht akzeptiert.

### Schreib-Richtlinien

Um die Konsistenz aller Dokumente zu gewährleisten, beachten Sie bitte folgende Richtlinien:

- **URL-Formatierung**: Umschließen Sie alle URLs mit eckigen Klammern, gefolgt von runden Klammern, ohne zusätzliche Leerzeichen dazwischen. Zum Beispiel: `[example](https://www.microsoft.com)`.

- **Relative Links**: Verwenden Sie `./` für relative Links zu Dateien oder Ordnern im aktuellen Verzeichnis und `../` für solche im übergeordneten Verzeichnis. Zum Beispiel: `[example](../../path/to/file)` oder `[example](../../../path/to/file)`.

- **Keine länderspezifischen Locale**: Achten Sie darauf, dass Ihre Links keine länderspezifischen Locale enthalten. Vermeiden Sie zum Beispiel `/en-us/` oder `/en/`.

- **Bildspeicherung**: Speichern Sie alle Bilder im `./imgs`-Ordner.

- **Beschreibende Bildnamen**: Benennen Sie Bilder aussagekräftig mit englischen Buchstaben, Zahlen und Bindestrichen. Zum Beispiel: `example-image.jpg`.

## GitHub Workflows

Wenn Sie eine Pull-Anfrage einreichen, werden folgende Workflows ausgelöst, um die Änderungen zu überprüfen. Befolgen Sie die Anweisungen, damit Ihre Pull-Anfrage die Workflow-Prüfungen besteht:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Dieser Workflow stellt sicher, dass alle relativen Pfade in Ihren Dateien korrekt sind.

1. Um sicherzustellen, dass Ihre Links funktionieren, führen Sie die folgenden Schritte in VS Code aus:
    - Bewegen Sie den Mauszeiger über einen Link in Ihren Dateien.
    - Drücken Sie **Strg + Klick**, um zum Link zu navigieren.
    - Wenn ein Link lokal nicht funktioniert, löst dies den Workflow aus und der Link funktioniert auch auf GitHub nicht.

1. Um dieses Problem zu beheben, führen Sie die folgenden Schritte mit den von VS Code vorgeschlagenen Pfaden aus:
    - Geben Sie `./` oder `../` ein.
    - VS Code zeigt Ihnen daraufhin verfügbare Optionen basierend auf Ihrer Eingabe an.
    - Folgen Sie dem Pfad, indem Sie auf die gewünschte Datei oder den Ordner klicken, um sicherzustellen, dass der Pfad korrekt ist.

Sobald Sie den korrekten relativen Pfad hinzugefügt haben, speichern und pushen Sie Ihre Änderungen.

### Check URLs Don't Have Locale

Dieser Workflow stellt sicher, dass keine Web-URL eine länderspezifische Locale enthält. Da dieses Repository global zugänglich ist, ist es wichtig, dass URLs keine länderspezifischen Locale enthalten.

1. Um zu überprüfen, dass Ihre URLs keine länderspezifischen Locale enthalten, führen Sie folgende Schritte aus:

    - Prüfen Sie, ob Texte wie `/en-us/`, `/en/` oder andere Sprach-Locale in den URLs vorkommen.
    - Wenn diese nicht in Ihren URLs vorhanden sind, besteht der Check.

1. Um das Problem zu beheben, gehen Sie wie folgt vor:
    - Öffnen Sie die vom Workflow hervorgehobene Datei.
    - Entfernen Sie die länderspezifische Locale aus den URLs.

Sobald Sie die länderspezifische Locale entfernt haben, speichern und pushen Sie Ihre Änderungen.

### Check Broken Urls

Dieser Workflow stellt sicher, dass jede Web-URL in Ihren Dateien funktioniert und einen Statuscode 200 zurückgibt.

1. Um zu überprüfen, dass Ihre URLs funktionieren, führen Sie folgende Schritte aus:
    - Prüfen Sie den Status der URLs in Ihren Dateien.

2. Um defekte URLs zu beheben, führen Sie folgende Schritte aus:
    - Öffnen Sie die Datei mit der defekten URL.
    - Aktualisieren Sie die URL auf die korrekte.

Sobald Sie die URLs korrigiert haben, speichern und pushen Sie Ihre Änderungen.

> [!NOTE]
>
> Es kann vorkommen, dass die URL-Prüfung fehlschlägt, obwohl der Link erreichbar ist. Dies kann verschiedene Gründe haben, darunter:
>
> - **Netzwerkbeschränkungen:** Die GitHub Actions-Server können Netzwerkbeschränkungen haben, die den Zugriff auf bestimmte URLs verhindern.
> - **Timeout-Probleme:** URLs, die zu lange zum Antworten brauchen, können im Workflow einen Timeout-Fehler auslösen.
> - **Temporäre Serverprobleme:** Gelegentliche Serverausfälle oder Wartungsarbeiten können eine URL während der Validierung vorübergehend unerreichbar machen.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.