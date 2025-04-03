<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "212531c5722978740dcfb73e3995cbba",
  "translation_date": "2025-04-03T05:47:59+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "de"
}
-->
# Beitragen

Dieses Projekt begrüßt Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, die erklärt, dass Sie das Recht haben und tatsächlich die Rechte gewähren, Ihren Beitrag zu nutzen. Weitere Details finden Sie unter [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Wenn Sie eine Pull-Anfrage einreichen, wird ein CLA-Bot automatisch bestimmen, ob Sie eine CLA bereitstellen müssen, und die PR entsprechend markieren (z. B. Statusprüfung, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories tun, die unsere CLA verwenden.

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen. Weitere Informationen finden Sie in den [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei zusätzlichen Fragen oder Kommentaren.

## Hinweise zum Erstellen von Issues

Bitte öffnen Sie keine GitHub-Issues für allgemeine Supportfragen, da die GitHub-Liste für Funktionsanfragen und Fehlerberichte verwendet werden sollte. Auf diese Weise können wir tatsächliche Probleme oder Fehler im Code leichter verfolgen und die allgemeine Diskussion vom eigentlichen Code trennen.

## Wie Sie beitragen können

### Richtlinien für Pull-Anfragen

Wenn Sie eine Pull-Anfrage (PR) an das Phi-3 CookBook-Repository einreichen, verwenden Sie bitte die folgenden Richtlinien:

- **Repository forken**: Forken Sie das Repository immer auf Ihr eigenes Konto, bevor Sie Änderungen vornehmen.

- **Separate Pull-Anfragen (PR)**:
  - Reichen Sie jede Art von Änderung in einer eigenen Pull-Anfrage ein. Zum Beispiel sollten Fehlerbehebungen und Dokumentationsaktualisierungen in separaten PRs eingereicht werden.
  - Tippfehlerkorrekturen und kleinere Dokumentationsaktualisierungen können bei Bedarf in einer einzigen PR kombiniert werden.

- **Umgang mit Merge-Konflikten**: Wenn Ihre Pull-Anfrage Merge-Konflikte aufweist, aktualisieren Sie Ihren lokalen `main`-Branch, um das Haupt-Repository zu spiegeln, bevor Sie Änderungen vornehmen.

- **Einreichung von Übersetzungen**: Wenn Sie eine Übersetzungs-PR einreichen, stellen Sie sicher, dass der Übersetzungsordner Übersetzungen für alle Dateien im Originalordner enthält.

### Richtlinien für Übersetzungen

> [!IMPORTANT]
>
> Verwenden Sie bei der Übersetzung von Texten in diesem Repository keine maschinelle Übersetzung. Melden Sie sich nur für Übersetzungen in Sprachen, in denen Sie kompetent sind.

Wenn Sie eine andere Sprache als Englisch beherrschen, können Sie helfen, den Inhalt zu übersetzen. Befolgen Sie diese Schritte, um sicherzustellen, dass Ihre Übersetzungsbeiträge korrekt integriert werden. Verwenden Sie die folgenden Richtlinien:

- **Übersetzungsordner erstellen**: Navigieren Sie zum entsprechenden Abschnittsordner und erstellen Sie einen Übersetzungsordner für die Sprache, zu der Sie beitragen möchten. Zum Beispiel:
  - Für den Einführungsabschnitt: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Für den Schnellstartabschnitt: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Setzen Sie dieses Muster für andere Abschnitte (03.Inference, 04.Finetuning usw.) fort.

- **Relative Pfade aktualisieren**: Passen Sie beim Übersetzen die Ordnerstruktur an, indem Sie `../../` am Anfang von relativen Pfaden in den Markdown-Dateien hinzufügen, um sicherzustellen, dass Links korrekt funktionieren. Zum Beispiel ändern Sie Folgendes:
  - Ändern Sie `(../../imgs/01/phi3aisafety.png)` zu `(../../../../imgs/01/phi3aisafety.png)`.

- **Organisieren Sie Ihre Übersetzungen**: Jede übersetzte Datei sollte im entsprechenden Übersetzungsordner des Abschnitts abgelegt werden. Wenn Sie beispielsweise den Einführungsabschnitt ins Spanische übersetzen, würden Sie Folgendes erstellen:
  - `PhiCookBook/md/01.Introduce/translations/es/`.

- **Vollständige PR einreichen**: Stellen Sie sicher, dass alle übersetzten Dateien für einen Abschnitt in einer PR enthalten sind. Wir akzeptieren keine Teilübersetzungen für einen Abschnitt. Stellen Sie sicher, dass der Übersetzungsordner Übersetzungen für alle Dateien im Originalordner enthält, wenn Sie eine Übersetzungs-PR einreichen.

### Schreibrichtlinien

Um Konsistenz über alle Dokumente hinweg zu gewährleisten, verwenden Sie bitte die folgenden Richtlinien:

- **URL-Formatierung**: Umschließen Sie alle URLs in eckigen Klammern, gefolgt von runden Klammern, ohne zusätzliche Leerzeichen darum oder darin. Zum Beispiel: `[example](https://www.microsoft.com)`.

- **Relative Links**: Verwenden Sie `./` für relative Links, die auf Dateien oder Ordner im aktuellen Verzeichnis verweisen, und `../` für solche in einem übergeordneten Verzeichnis. Zum Beispiel: `[example](../../path/to/file)` oder `[example](../../../path/to/file)`.

- **Nicht länderspezifische Lokalisierungen**: Stellen Sie sicher, dass Ihre Links keine länderspezifischen Lokalisierungen enthalten. Zum Beispiel vermeiden Sie `/en-us/` oder `/en/`.

- **Speicherung von Bildern**: Speichern Sie alle Bilder im `./imgs`-Ordner.

- **Beschreibende Bildnamen**: Benennen Sie Bilder beschreibend mit englischen Zeichen, Zahlen und Bindestrichen. Zum Beispiel: `example-image.jpg`.

## GitHub Workflows

Wenn Sie eine Pull-Anfrage einreichen, werden die folgenden Workflows ausgelöst, um die Änderungen zu validieren. Befolgen Sie die untenstehenden Anweisungen, um sicherzustellen, dass Ihre Pull-Anfrage die Workflow-Prüfungen besteht:

- [Überprüfen von fehlerhaften relativen Pfaden](../..)
- [Überprüfen, dass URLs keine Lokalisierungen enthalten](../..)

### Überprüfen von fehlerhaften relativen Pfaden

Dieser Workflow stellt sicher, dass alle relativen Pfade in Ihren Dateien korrekt sind.

1. Um sicherzustellen, dass Ihre Links korrekt funktionieren, führen Sie die folgenden Aufgaben mit VS Code aus:
    - Fahren Sie mit der Maus über einen beliebigen Link in Ihren Dateien.
    - Drücken Sie **Strg + Klick**, um zum Link zu navigieren.
    - Wenn Sie auf einen Link klicken und dieser lokal nicht funktioniert, wird der Workflow ausgelöst und funktioniert auch nicht auf GitHub.

1. Um dieses Problem zu beheben, führen Sie die folgenden Aufgaben mit den Pfadvorschlägen von VS Code aus:
    - Geben Sie `./` oder `../` ein.
    - VS Code wird Sie auffordern, aus den verfügbaren Optionen basierend auf dem einzugebenden Text auszuwählen.
    - Folgen Sie dem Pfad, indem Sie auf die gewünschte Datei oder den gewünschten Ordner klicken, um sicherzustellen, dass Ihr Pfad korrekt ist.

Sobald Sie den richtigen relativen Pfad hinzugefügt haben, speichern und pushen Sie Ihre Änderungen.

### Überprüfen, dass URLs keine Lokalisierungen enthalten

Dieser Workflow stellt sicher, dass keine Web-URLs eine länderspezifische Lokalisierung enthalten. Da dieses Repository weltweit zugänglich ist, ist es wichtig sicherzustellen, dass URLs keine Lokalisierungen Ihres Landes enthalten.

1. Um sicherzustellen, dass Ihre URLs keine Länder-Lokalisierungen enthalten, führen Sie die folgenden Aufgaben aus:

    - Überprüfen Sie auf Texte wie `/en-us/`, `/en/` oder andere Sprachlokalisierungen in den URLs.
    - Wenn diese nicht in Ihren URLs vorhanden sind, bestehen Sie diese Prüfung.

1. Um dieses Problem zu beheben, führen Sie die folgenden Aufgaben aus:
    - Öffnen Sie den Dateipfad, der vom Workflow hervorgehoben wurde.
    - Entfernen Sie die Länder-Lokalisierung aus den URLs.

Sobald Sie die Länder-Lokalisierung entfernt haben, speichern und pushen Sie Ihre Änderungen.

### Überprüfen von fehlerhaften URLs

Dieser Workflow stellt sicher, dass jede Web-URL in Ihren Dateien funktioniert und einen 200-Statuscode zurückgibt.

1. Um sicherzustellen, dass Ihre URLs korrekt funktionieren, führen Sie die folgenden Aufgaben aus:
    - Überprüfen Sie den Status der URLs in Ihren Dateien.

2. Um fehlerhafte URLs zu beheben, führen Sie die folgenden Aufgaben aus:
    - Öffnen Sie die Datei, die die fehlerhafte URL enthält.
    - Aktualisieren Sie die URL auf die korrekte.

Sobald Sie die URLs korrigiert haben, speichern und pushen Sie Ihre Änderungen.

> [!NOTE]
>
> Es kann Fälle geben, in denen die URL-Prüfung fehlschlägt, obwohl der Link zugänglich ist. Dies kann aus verschiedenen Gründen passieren, einschließlich:
>
> - **Netzwerkbeschränkungen:** GitHub-Aktionsserver können Netzwerkbeschränkungen haben, die den Zugriff auf bestimmte URLs verhindern.
> - **Timeout-Probleme:** URLs, die zu lange zum Antworten benötigen, können einen Timeout-Fehler im Workflow auslösen.
> - **Temporäre Serverprobleme:** Gelegentliche Serverausfälle oder Wartungen können eine URL während der Validierung vorübergehend unzugänglich machen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.