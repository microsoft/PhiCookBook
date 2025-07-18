<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:35:36+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "de"
}
-->
# Mitwirken

Dieses Projekt freut sich über Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, in der Sie bestätigen, dass Sie das Recht haben und tatsächlich die Rechte einräumen, Ihre Beiträge zu verwenden. Details finden Sie unter [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Wenn Sie eine Pull-Anfrage einreichen, prüft ein CLA-Bot automatisch, ob Sie eine CLA bereitstellen müssen, und versieht die PR entsprechend (z. B. Statusprüfung, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories mit unserer CLA tun.

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen.  
Für weitere Informationen lesen Sie die [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder wenden Sie sich bei weiteren Fragen oder Anmerkungen an [opencode@microsoft.com](mailto:opencode@microsoft.com).

## Hinweise zum Erstellen von Issues

Bitte öffnen Sie keine GitHub-Issues für allgemeine Supportfragen, da die GitHub-Liste für Feature-Anfragen und Fehlerberichte genutzt werden sollte. So können wir tatsächliche Probleme oder Fehler im Code besser verfolgen und die allgemeine Diskussion vom eigentlichen Code trennen.

## Wie man beiträgt

### Richtlinien für Pull Requests

Wenn Sie eine Pull-Anfrage (PR) im Phi-3 CookBook Repository einreichen, beachten Sie bitte folgende Richtlinien:

- **Repository forken**: Forken Sie das Repository immer in Ihr eigenes Konto, bevor Sie Änderungen vornehmen.

- **Getrennte Pull Requests (PR)**:
  - Reichen Sie jede Art von Änderung in einem eigenen Pull Request ein. Zum Beispiel sollten Fehlerbehebungen und Dokumentationsaktualisierungen in separaten PRs eingereicht werden.
  - Tippfehlerkorrekturen und kleinere Dokumentationsänderungen können, wenn sinnvoll, in einem einzigen PR zusammengefasst werden.

- **Merge-Konflikte beheben**: Wenn Ihr Pull Request Merge-Konflikte anzeigt, aktualisieren Sie Ihren lokalen `main`-Branch, um das Haupt-Repository widerzuspiegeln, bevor Sie Ihre Änderungen vornehmen.

- **Übersetzungseinreichungen**: Wenn Sie eine Übersetzungs-PR einreichen, stellen Sie sicher, dass der Übersetzungsordner Übersetzungen für alle Dateien im Originalordner enthält.

### Schreib-Richtlinien

Um Konsistenz in allen Dokumenten zu gewährleisten, verwenden Sie bitte folgende Richtlinien:

- **URL-Formatierung**: Umschließen Sie alle URLs mit eckigen Klammern, gefolgt von runden Klammern, ohne zusätzliche Leerzeichen davor oder dazwischen. Zum Beispiel: `[example](https://www.microsoft.com)`.

- **Relative Links**: Verwenden Sie `./` für relative Links, die auf Dateien oder Ordner im aktuellen Verzeichnis zeigen, und `../` für solche im übergeordneten Verzeichnis. Zum Beispiel: `[example](../../path/to/file)` oder `[example](../../../path/to/file)`.

- **Keine länderspezifischen Lokale**: Achten Sie darauf, dass Ihre Links keine länderspezifischen Lokale enthalten. Vermeiden Sie z. B. `/en-us/` oder `/en/`.

- **Bildspeicherung**: Speichern Sie alle Bilder im Ordner `./imgs`.

- **Beschreibende Bildnamen**: Benennen Sie Bilder aussagekräftig mit englischen Buchstaben, Zahlen und Bindestrichen. Zum Beispiel: `example-image.jpg`.

## GitHub Workflows

Wenn Sie eine Pull-Anfrage einreichen, werden die folgenden Workflows ausgelöst, um die Änderungen zu überprüfen. Befolgen Sie die untenstehenden Anweisungen, damit Ihre Pull-Anfrage die Workflow-Prüfungen besteht:

- [Check Broken Relative Paths](../..)  
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Dieser Workflow stellt sicher, dass alle relativen Pfade in Ihren Dateien korrekt sind.

1. Um sicherzustellen, dass Ihre Links funktionieren, führen Sie folgende Schritte in VS Code aus:  
    - Fahren Sie mit der Maus über einen Link in Ihren Dateien.  
    - Drücken Sie **Strg + Klick**, um zum Link zu navigieren.  
    - Wenn ein Link lokal nicht funktioniert, wird der Workflow ausgelöst und der Link funktioniert auch auf GitHub nicht.

1. Um dieses Problem zu beheben, führen Sie folgende Schritte mit den von VS Code vorgeschlagenen Pfaden aus:  
    - Geben Sie `./` oder `../` ein.  
    - VS Code zeigt Ihnen basierend auf Ihrer Eingabe verfügbare Optionen an.  
    - Folgen Sie dem Pfad, indem Sie auf die gewünschte Datei oder den Ordner klicken, um sicherzustellen, dass Ihr Pfad korrekt ist.

Nachdem Sie den korrekten relativen Pfad hinzugefügt haben, speichern Sie und pushen Ihre Änderungen.

### Check URLs Don't Have Locale

Dieser Workflow stellt sicher, dass keine Web-URL ein länderspezifisches Locale enthält. Da dieses Repository global zugänglich ist, ist es wichtig, dass URLs keine länderspezifischen Lokale enthalten.

1. Um zu überprüfen, dass Ihre URLs keine Länder-Lokale enthalten, führen Sie folgende Schritte aus:

    - Prüfen Sie, ob Texte wie `/en-us/`, `/en/` oder andere Sprach-Lokale in den URLs vorkommen.  
    - Wenn diese nicht vorhanden sind, besteht Ihre Prüfung.

1. Um dieses Problem zu beheben, führen Sie folgende Schritte aus:  
    - Öffnen Sie den vom Workflow hervorgehobenen Dateipfad.  
    - Entfernen Sie das Länder-Locale aus den URLs.

Nachdem Sie das Länder-Locale entfernt haben, speichern Sie und pushen Ihre Änderungen.

### Check Broken Urls

Dieser Workflow stellt sicher, dass jede Web-URL in Ihren Dateien funktioniert und einen Statuscode 200 zurückgibt.

1. Um zu überprüfen, dass Ihre URLs korrekt funktionieren, führen Sie folgende Schritte aus:  
    - Prüfen Sie den Status der URLs in Ihren Dateien.

2. Um defekte URLs zu beheben, führen Sie folgende Schritte aus:  
    - Öffnen Sie die Datei mit der defekten URL.  
    - Aktualisieren Sie die URL auf die korrekte.

Nachdem Sie die URLs korrigiert haben, speichern Sie und pushen Ihre Änderungen.

> [!NOTE]  
>  
> Es kann Fälle geben, in denen die URL-Prüfung fehlschlägt, obwohl der Link erreichbar ist. Dies kann aus verschiedenen Gründen passieren, darunter:  
>  
> - **Netzwerkbeschränkungen:** Die GitHub Actions-Server können Netzwerkbeschränkungen haben, die den Zugriff auf bestimmte URLs verhindern.  
> - **Timeout-Probleme:** URLs, die zu lange zum Antworten brauchen, können im Workflow einen Timeout-Fehler auslösen.  
> - **Temporäre Serverprobleme:** Gelegentliche Serverausfälle oder Wartungen können eine URL während der Prüfung vorübergehend nicht erreichbar machen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.