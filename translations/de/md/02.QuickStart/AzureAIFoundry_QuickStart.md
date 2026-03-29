# **Verwendung von Phi-3 in Microsoft Foundry**

Mit der Entwicklung von Generativer KI hoffen wir, eine einheitliche Plattform zu verwenden, um verschiedene LLM und SLM, Unternehmensdatenintegration, Feinabstimmung/RAG-Operationen und die Bewertung verschiedener Unternehmensbereiche nach der Integration von LLM und SLM usw. zu verwalten, damit generative KI Smart-Anwendungen besser umgesetzt werden können. [Microsoft Foundry](https://ai.azure.com) ist eine generative KI-Anwendungsplattform auf Unternehmensebene.

![aistudo](../../../../translated_images/de/aifoundry_home.f28a8127c96c7d93.webp)

Mit Microsoft Foundry können Sie die Antworten großer Sprachmodelle (LLM) bewerten und Aufforderungskomponenten mit Prompt Flow orchestrieren, um eine bessere Leistung zu erzielen. Die Plattform erleichtert die Skalierbarkeit, um Konzepte schnell in vollwertige Produktionsumgebungen zu überführen. Kontinuierliche Überwachung und Verfeinerung unterstützen den langfristigen Erfolg.

Wir können das Phi-3-Modell schnell über einfache Schritte in Microsoft Foundry bereitstellen und dann Microsoft Foundry verwenden, um Playground/Chat, Feinabstimmung, Bewertung und andere damit verbundene Arbeiten zu Phi-3 abzuschließen.

## **1. Vorbereitung**

Wenn Sie bereits die [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) auf Ihrem Gerät installiert haben, ist die Verwendung dieser Vorlage so einfach wie das Ausführen dieses Befehls in einem neuen Verzeichnis.

## Manuelle Erstellung

Die Erstellung eines Microsoft Foundry-Projekts und Hubs ist eine großartige Möglichkeit, Ihre KI-Arbeit zu organisieren und zu verwalten. Hier ist eine Schritt-für-Schritt-Anleitung, um loszulegen:

### Ein Projekt in Microsoft Foundry erstellen

1. **Gehen Sie zu Microsoft Foundry**: Melden Sie sich im Microsoft Foundry-Portal an.
2. **Erstellen Sie ein Projekt**:
   - Wenn Sie sich in einem Projekt befinden, wählen Sie oben links auf der Seite „Microsoft Foundry“, um zur Startseite zu gelangen.
   - Wählen Sie „+ Projekt erstellen“.
   - Geben Sie einen Namen für das Projekt ein.
   - Wenn Sie einen Hub haben, wird dieser standardmäßig ausgewählt. Wenn Sie Zugriff auf mehr als einen Hub haben, können Sie einen anderen aus dem Dropdown-Menü auswählen. Wenn Sie einen neuen Hub erstellen möchten, wählen Sie „Neuen Hub erstellen“ und geben Sie einen Namen ein.
   - Wählen Sie „Erstellen“.

### Einen Hub in Microsoft Foundry erstellen

1. **Gehen Sie zu Microsoft Foundry**: Melden Sie sich mit Ihrem Azure-Konto an.
2. **Erstellen Sie einen Hub**:
   - Wählen Sie im linken Menü das Management-Center.
   - Wählen Sie „Alle Ressourcen“, dann den Abwärtspfeil neben „+ Neues Projekt“ und wählen Sie „+ Neuer Hub“.
   - Geben Sie im Dialogfeld „Neuen Hub erstellen“ einen Namen für Ihren Hub ein (z. B. contoso-hub) und ändern Sie die anderen Felder nach Wunsch.
   - Wählen Sie „Weiter“, überprüfen Sie die Angaben und dann „Erstellen“.

Für detailliertere Anweisungen können Sie die offizielle [Microsoft-Dokumentation](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects) konsultieren.

Nach erfolgreicher Erstellung können Sie auf das erstellte Studio über [ai.azure.com](https://ai.azure.com/) zugreifen.

Es können mehrere Projekte in einer AI Foundry vorhanden sein. Erstellen Sie ein Projekt in AI Foundry als Vorbereitung.

Erstellen Sie Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Bereitstellung eines Phi-Modells in Microsoft Foundry**

Klicken Sie auf die Option „Explore“ des Projekts, um den Modellkatalog zu öffnen und wählen Sie Phi-3 aus.

Wählen Sie Phi-3-mini-4k-instruct.

Klicken Sie auf „Deploy“, um das Modell Phi-3-mini-4k-instruct bereitzustellen.

> [!NOTE]
>
> Sie können bei der Bereitstellung die Rechenleistung auswählen.

## **3. Playground Chat Phi in Microsoft Foundry**

Gehen Sie zur Bereitstellungsseite, wählen Sie Playground und chatten Sie mit Phi-3 in Microsoft Foundry.

## **4. Modellbereitstellung aus Microsoft Foundry**

Um ein Modell aus dem Azure Model Catalog bereitzustellen, können Sie folgende Schritte ausführen:

- Melden Sie sich bei Microsoft Foundry an.
- Wählen Sie das Modell aus dem Microsoft Foundry-Modellkatalog aus, das Sie bereitstellen möchten.
- Wählen Sie auf der Detailseite des Modells „Deploy“ und dann „Serverless API mit Azure AI Content Safety“.
- Wählen Sie das Projekt aus, in dem Sie Ihre Modelle bereitstellen möchten. Um das Angebot der Serverless API zu nutzen, muss Ihr Workspace zur Region East US 2 oder Schweden Central gehören. Sie können den Bereitstellungsnamen anpassen.
- Wählen Sie im Bereitstellungsassistenten „Preise und Bedingungen“, um Informationen zu Preisen und Nutzungsbedingungen zu erhalten.
- Wählen Sie „Deploy“. Warten Sie, bis die Bereitstellung abgeschlossen ist und Sie zur Seite „Deployments“ weitergeleitet werden.
- Wählen Sie „Open in playground“, um mit dem Modell zu interagieren.
- Sie können zur Seite „Deployments“ zurückkehren, die Bereitstellung auswählen und die Ziel-URL des Endpunkts sowie den geheimen Schlüssel notieren, mit denen Sie die Bereitstellung aufrufen und Vervollständigungen generieren können.
- Sie finden die Details des Endpunkts, die URL und Zugriffsschlüssel jederzeit, indem Sie zur Registerkarte „Build“ navigieren und unter Komponenten „Deployments“ auswählen.

> [!NOTE]
> Bitte beachten Sie, dass Ihr Konto über die Rollenberechtigung Azure AI Developer auf der Ressourcengruppe verfügen muss, um diese Schritte auszuführen.

## **5. Verwendung der Phi-API in Microsoft Foundry**

Sie können über Postman GET auf https://{Ihr Projektname}.region.inference.ml.azure.com/swagger.json zugreifen und zusammen mit dem Schlüssel die bereitgestellten Schnittstellen kennenlernen.

Sie können die Anfrageparameter sehr bequem abrufen sowie die Antwortparameter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->