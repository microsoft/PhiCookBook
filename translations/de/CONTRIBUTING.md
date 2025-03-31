<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-03-27T02:31:18+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "de"
}
-->
# Beitrag leisten

Dieses Projekt freut sich über Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, die erklärt, dass Sie das Recht haben und uns tatsächlich die Rechte gewähren, Ihren Beitrag zu nutzen. Weitere Details finden Sie unter [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Wenn Sie eine Pull-Anfrage einreichen, wird ein CLA-Bot automatisch feststellen, ob Sie eine CLA bereitstellen müssen, und die PR entsprechend kennzeichnen (z. B. Statusprüfung, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories tun, die unsere CLA verwenden.

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen. Weitere Informationen finden Sie in den [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder wenden Sie sich mit zusätzlichen Fragen oder Kommentaren an [opencode@microsoft.com](mailto:opencode@microsoft.com).

## Hinweise zum Erstellen von Issues

Bitte erstellen Sie keine GitHub-Issues für allgemeine Support-Fragen, da die GitHub-Liste für Funktionsanfragen und Fehlerberichte verwendet werden sollte. Auf diese Weise können wir tatsächliche Probleme oder Fehler im Code leichter nachverfolgen und die allgemeine Diskussion vom eigentlichen Code trennen.

## Wie man beiträgt

### Richtlinien für Pull-Anfragen

Wenn Sie eine Pull-Anfrage (PR) für das Phi-3 CookBook-Repository einreichen, beachten Sie bitte die folgenden Richtlinien:

- **Fork des Repositories**: Forken Sie immer das Repository auf Ihr eigenes Konto, bevor Sie Änderungen vornehmen.

- **Separate Pull-Anfragen (PR)**:
  - Reichen Sie jede Art von Änderung in einer eigenen Pull-Anfrage ein. Zum Beispiel sollten Fehlerbehebungen und Dokumentationsaktualisierungen in separaten PRs eingereicht werden.
  - Rechtschreibfehler und kleinere Dokumentationsaktualisierungen können bei Bedarf in einer einzigen PR kombiniert werden.

- **Umgang mit Merge-Konflikten**: Wenn Ihre Pull-Anfrage Merge-Konflikte aufweist, aktualisieren Sie Ihren lokalen `main`-Branch, um das Hauptrepository zu spiegeln, bevor Sie Änderungen vornehmen.

- **Übersetzungseinreichungen**: Stellen Sie bei der Einreichung einer Übersetzungs-PR sicher, dass der Übersetzungsordner Übersetzungen für alle Dateien im Originalordner enthält.

### Richtlinien für Übersetzungen

> [!IMPORTANT]
>
> Verwenden Sie keine maschinelle Übersetzung, wenn Sie Texte in diesem Repository übersetzen. Melden Sie sich nur für Übersetzungen in Sprachen, in denen Sie kompetent sind.

Wenn Sie eine nicht-englische Sprache beherrschen, können Sie bei der Übersetzung der Inhalte helfen. Befolgen Sie diese Schritte, um sicherzustellen, dass Ihre Übersetzungsbeiträge ordnungsgemäß integriert werden. Bitte verwenden Sie die folgenden Richtlinien:

- **Erstellen Sie einen Übersetzungsordner**: Navigieren Sie zum entsprechenden Abschnittsordner und erstellen Sie einen Übersetzungsordner für die Sprache, zu der Sie beitragen möchten. Zum Beispiel:
  - Für den Abschnitt "Einführung": `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Für den Abschnitt "Schnellstart": `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Fahren Sie mit diesem Muster für andere Abschnitte fort (03.Inference, 04.Finetuning usw.).

- **Relative Pfade aktualisieren**: Passen Sie bei der Übersetzung die Ordnerstruktur an, indem Sie `../../` am Anfang von relativen Pfaden innerhalb der Markdown-Dateien hinzufügen, um sicherzustellen, dass Links korrekt funktionieren. Beispielsweise ändern Sie wie folgt:
  - Ändern Sie `(../../imgs/01/phi3aisafety.png)` in `(../../../../imgs/01/phi3aisafety.png)`.

- **Organisieren Sie Ihre Übersetzungen**: Jede übersetzte Datei sollte im entsprechenden Übersetzungsordner des Abschnitts abgelegt werden. Zum Beispiel, wenn Sie den Abschnitt "Einführung" ins Spanische übersetzen, würden Sie wie folgt erstellen:
  - `PhiCookBook/md/01.Introduce/translations/es/`.

- **Reichen Sie eine vollständige PR ein**: Stellen Sie sicher, dass alle übersetzten Dateien für einen Abschnitt in einer PR enthalten sind. Wir akzeptieren keine Teilübersetzungen für einen Abschnitt. Wenn Sie eine Übersetzungs-PR einreichen, stellen Sie sicher, dass der Übersetzungsordner Übersetzungen für alle Dateien im Originalordner enthält.

### Richtlinien zum Schreiben

Um Konsistenz in allen Dokumenten zu gewährleisten, verwenden Sie bitte die folgenden Richtlinien:

- **URL-Formatierung**: Umschließen Sie alle URLs in eckigen Klammern, gefolgt von Klammern, ohne zusätzliche Leerzeichen davor oder dazwischen. Zum Beispiel: `[example](https://www.microsoft.com)`.

- **Relative Links**: Verwenden Sie `./` für relative Links, die auf Dateien oder Ordner im aktuellen Verzeichnis zeigen, und `../` für solche in einem übergeordneten Verzeichnis. Zum Beispiel: `[example](../../path/to/file)` oder `[example](../../../path/to/file)`.

- **Nicht länderspezifische Lokalisierungen**: Stellen Sie sicher, dass Ihre Links keine länderspezifischen Lokalisierungen enthalten. Zum Beispiel vermeiden Sie `/en-us/` oder `/en/`.

- **Speicherung von Bildern**: Speichern Sie alle Bilder im `./imgs`-Ordner.

- **Beschreibende Bildnamen**: Benennen Sie Bilder beschreibend mit englischen Zeichen, Zahlen und Bindestrichen. Zum Beispiel: `example-image.jpg`.

## GitHub-Workflows

Wenn Sie eine Pull-Anfrage einreichen, werden die folgenden Workflows ausgelöst, um die Änderungen zu validieren. Befolgen Sie die unten stehenden Anweisungen, um sicherzustellen, dass Ihre Pull-Anfrage die Workflow-Checks besteht:

- [Broken Relative Paths prüfen](../..)
- [URLs auf Lokalisierungen prüfen](../..)

### Broken Relative Paths prüfen

Dieser Workflow stellt sicher, dass alle relativen Pfade in Ihren Dateien korrekt sind.

1. Um sicherzustellen, dass Ihre Links ordnungsgemäß funktionieren, führen Sie die folgenden Aufgaben mit VS Code aus:
    - Fahren Sie mit der Maus über jeden Link in Ihren Dateien.
    - Drücken Sie **Strg + Klick**, um zum Link zu navigieren.
    - Wenn Sie auf einen Link klicken und dieser lokal nicht funktioniert, wird der Workflow ausgelöst und funktioniert nicht auf GitHub.

1. Um dieses Problem zu beheben, führen Sie die folgenden Aufgaben mit den Pfadvorschlägen aus, die von VS Code bereitgestellt werden:
    - Geben Sie `./` oder `../` ein.
    - VS Code wird Sie auffordern, aus den verfügbaren Optionen basierend auf dem, was Sie eingegeben haben, auszuwählen.
    - Folgen Sie dem Pfad, indem Sie auf die gewünschte Datei oder den gewünschten Ordner klicken, um sicherzustellen, dass Ihr Pfad korrekt ist.

Sobald Sie den korrekten relativen Pfad hinzugefügt haben, speichern und pushen Sie Ihre Änderungen.

### URLs auf Lokalisierungen prüfen

Dieser Workflow stellt sicher, dass keine Web-URL eine länderspezifische Lokalisierung enthält. Da dieses Repository global zugänglich ist, ist es wichtig, dass URLs keine länderspezifischen Lokalisierungen enthalten.

1. Um zu überprüfen, ob Ihre URLs keine Länder-Lokalisierungen enthalten, führen Sie die folgenden Aufgaben aus:

    - Überprüfen Sie, ob Text wie `/en-us/`, `/en/` oder andere Sprach-Lokalisierungen in den URLs enthalten ist.
    - Wenn diese in Ihren URLs nicht vorhanden sind, bestehen Sie diesen Check.

1. Um dieses Problem zu beheben, führen Sie die folgenden Aufgaben aus:
    - Öffnen Sie den Dateipfad, der vom Workflow hervorgehoben wurde.
    - Entfernen Sie die Länder-Lokalisierung aus den URLs.

Sobald Sie die Länder-Lokalisierung entfernt haben, speichern und pushen Sie Ihre Änderungen.

### Broken URLs prüfen

Dieser Workflow stellt sicher, dass alle Web-URLs in Ihren Dateien funktionieren und einen 200-Statuscode zurückgeben.

1. Um sicherzustellen, dass Ihre URLs korrekt funktionieren, führen Sie die folgenden Aufgaben aus:
    - Überprüfen Sie den Status der URLs in Ihren Dateien.

2. Um fehlerhafte URLs zu beheben, führen Sie die folgenden Aufgaben aus:
    - Öffnen Sie die Datei, die die fehlerhafte URL enthält.
    - Aktualisieren Sie die URL auf die richtige.

Sobald Sie die URLs korrigiert haben, speichern und pushen Sie Ihre Änderungen.

> [!NOTE]
>
> Es kann vorkommen, dass der URL-Check fehlschlägt, obwohl der Link zugänglich ist. Dies kann aus mehreren Gründen passieren, einschließlich:
>
> - **Netzwerkbeschränkungen**: GitHub Actions-Server können Netzwerkbeschränkungen haben, die den Zugriff auf bestimmte URLs verhindern.
> - **Timeout-Probleme**: URLs, die zu lange zum Antworten benötigen, können einen Timeout-Fehler im Workflow auslösen.
> - **Vorübergehende Serverprobleme**: Gelegentliche Serverausfälle oder Wartungsarbeiten können dazu führen, dass eine URL während der Validierung vorübergehend nicht verfügbar ist.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.