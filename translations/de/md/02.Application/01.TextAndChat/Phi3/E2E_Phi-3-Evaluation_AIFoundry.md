# Bewertung des feinabgestimmten Phi-3 / Phi-3.5 Modells in Microsoft Foundry mit Fokus auf Microsofts Responsible AI-Prinzipien

Dieses End-to-End (E2E)-Beispiel basiert auf der Anleitung "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" aus der Microsoft Tech Community.

## Überblick

### Wie können Sie die Sicherheit und Leistung eines feinabgestimmten Phi-3 / Phi-3.5 Modells in Microsoft Foundry bewerten?

Die Feinabstimmung eines Modells kann manchmal zu unbeabsichtigten oder unerwünschten Antworten führen. Um sicherzustellen, dass das Modell sicher und effektiv bleibt, ist es wichtig, das Potenzial des Modells zur Erzeugung schädlicher Inhalte sowie seine Fähigkeit, genaue, relevante und kohärente Antworten zu liefern, zu bewerten. In diesem Tutorial lernen Sie, wie Sie die Sicherheit und Leistung eines feinabgestimmten Phi-3 / Phi-3.5 Modells, integriert mit Prompt flow in Microsoft Foundry, bewerten.

Hier ist der Bewertungsprozess von Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/de/architecture.10bec55250f5d6a4.webp)

*Bildquelle: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Für detailliertere Informationen und um zusätzliche Ressourcen zu Phi-3 / Phi-3.5 zu erkunden, besuchen Sie bitte das [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Voraussetzungen

- [Python](https://www.python.org/downloads)
- [Azure-Abonnement](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Feinabgestimmtes Phi-3 / Phi-3.5 Modell

### Inhaltsverzeichnis

1. [**Szenario 1: Einführung in die Prompt flow Bewertung von Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Einführung in die Sicherheitsbewertung](#einführung-in-die-sicherheitsbewertung)
    - [Einführung in die Leistungsbewertung](#einführung-in-die-leistungsbewertung)

1. [**Szenario 2: Bewertung des Phi-3 / Phi-3.5 Modells in Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Bevor Sie beginnen](#bevor-sie-beginnen)
    - [Bereitstellung von Azure OpenAI zur Bewertung des Phi-3 / Phi-3.5 Modells](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Bewertung des feinabgestimmten Phi-3 / Phi-3.5 Modells mit der Prompt flow Bewertung von Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Herzlichen Glückwunsch!](#herzlichen-glückwunsch)

## **Szenario 1: Einführung in die Prompt flow Bewertung von Microsoft Foundry**

### Einführung in die Sicherheitsbewertung

Um sicherzustellen, dass Ihr KI-Modell ethisch und sicher ist, ist es entscheidend, es anhand der Responsible AI-Prinzipien von Microsoft zu bewerten. In Microsoft Foundry ermöglichen Sicherheitsbewertungen, die Verwundbarkeit Ihres Modells gegenüber Jailbreak-Angriffen und sein Potenzial zur Erzeugung schädlicher Inhalte zu bewerten, was direkt mit diesen Prinzipien übereinstimmt.

![Safaty evaluation.](../../../../../../translated_images/de/safety-evaluation.083586ec88dfa950.webp)

*Bildquelle: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofts Responsible AI-Prinzipien

Bevor Sie die technischen Schritte beginnen, ist es wichtig, Microsofts Responsible AI-Prinzipien zu verstehen, ein ethisches Rahmenwerk zur verantwortungsvollen Entwicklung, Implementierung und Betrieb von KI-Systemen. Diese Prinzipien leiten die verantwortungsvolle Gestaltung, Entwicklung und Implementierung von KI-Systemen, um sicherzustellen, dass KI-Technologien fair, transparent und inklusiv aufgebaut sind. Diese Prinzipien bilden die Grundlage zur Bewertung der Sicherheit von KI-Modellen.

Microsofts Responsible AI-Prinzipien umfassen:

- **Fairness und Inklusivität**: KI-Systeme sollten alle fair behandeln und vermeiden, ähnlich situierte Gruppen unterschiedlich zu beeinflussen. Zum Beispiel sollten KI-Systeme bei Empfehlungen zur medizinischen Behandlung, bei Kreditanträgen oder bei der Beschäftigung allen Personen mit ähnlichen Symptomen, finanziellen Verhältnissen oder beruflichen Qualifikationen dieselben Empfehlungen geben.

- **Zuverlässigkeit und Sicherheit**: Um Vertrauen zu schaffen, ist es entscheidend, dass KI-Systeme zuverlässig, sicher und konsistent arbeiten. Diese Systeme sollten wie ursprünglich entworfen funktionieren, sicher auf unvorhergesehene Bedingungen reagieren und schädlichen Manipulationen widerstehen. Ihr Verhalten und die Vielfalt der Bedingungen, die sie bewältigen können, spiegeln die Bandbreite von Situationen wider, die Entwickler während Design und Test antizipiert haben.

- **Transparenz**: Wenn KI-Systeme Entscheidungen informieren, die immense Auswirkungen auf das Leben der Menschen haben, ist es entscheidend, dass Menschen verstehen, wie diese Entscheidungen getroffen wurden. Zum Beispiel könnte eine Bank ein KI-System verwenden, um zu entscheiden, ob eine Person kreditwürdig ist. Ein Unternehmen könnte ein KI-System einsetzen, um die qualifiziertesten Bewerber auszuwählen.

- **Datenschutz und Sicherheit**: Mit zunehmender Verbreitung von KI werden Datenschutz und Sicherheit persönlicher und geschäftlicher Informationen immer wichtiger und komplexer. Mit KI erfordern Datenschutz und Datensicherheit besondere Aufmerksamkeit, da der Zugang zu Daten für KI-Systeme essenziell ist, um genaue und fundierte Vorhersagen und Entscheidungen über Personen zu treffen.

- **Verantwortlichkeit**: Diejenigen, die KI-Systeme entwerfen und einsetzen, müssen für deren Betrieb verantwortlich sein. Organisationen sollten auf Industriestandards zurückgreifen, um Verantwortlichkeitsnormen zu entwickeln. Diese Normen können sicherstellen, dass KI-Systeme nicht die letzte Entscheidungsinstanz bei Entscheidungen sind, die das Leben von Menschen betreffen. Sie können auch gewährleisten, dass Menschen die sinnvolle Kontrolle über ansonsten hoch autonome KI-Systeme behalten.

![Fill hub.](../../../../../../translated_images/de/responsibleai2.c07ef430113fad8c.webp)

*Bildquelle: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Um mehr über Microsofts Responsible AI-Prinzipien zu erfahren, besuchen Sie [Was ist Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Sicherheitsmetriken

In diesem Tutorial bewerten Sie die Sicherheit des feinabgestimmten Phi-3 Modells mit Hilfe der Sicherheitsmetriken von Microsoft Foundry. Diese Metriken helfen Ihnen, das Potenzial des Modells zur Erzeugung schädlicher Inhalte und dessen Verwundbarkeit gegenüber Jailbreak-Angriffen einzuschätzen. Die Sicherheitsmetriken umfassen:

- **Selbstverletzungsbezogene Inhalte**: Bewertet, ob das Modell dazu neigt, selbstverletzende Inhalte zu erzeugen.
- **Hasserfüllte und ungerechte Inhalte**: Bewertet, ob das Modell dazu neigt, hasserfüllte oder ungerechte Inhalte zu erzeugen.
- **Gewalttätige Inhalte**: Bewertet, ob das Modell dazu neigt, gewalttätige Inhalte zu erzeugen.
- **Sexuelle Inhalte**: Bewertet, ob das Modell dazu neigt, unangemessene sexuelle Inhalte zu erzeugen.

Die Bewertung dieser Aspekte stellt sicher, dass das KI-Modell keine schädlichen oder anstößigen Inhalte produziert, was mit gesellschaftlichen Werten und regulatorischen Standards übereinstimmt.

![Evaluate based on safety.](../../../../../../translated_images/de/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Einführung in die Leistungsbewertung

Um sicherzustellen, dass Ihr KI-Modell wie erwartet funktioniert, ist es wichtig, dessen Leistung anhand von Leistungskennzahlen zu bewerten. In Microsoft Foundry ermöglichen Leistungsbewertungen, die Effektivität Ihres Modells bei der Erstellung genauer, relevanter und kohärenter Antworten zu beurteilen.

![Safaty evaluation.](../../../../../../translated_images/de/performance-evaluation.48b3e7e01a098740.webp)

*Bildquelle: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Leistungsmetriken

In diesem Tutorial bewerten Sie die Leistung des feinabgestimmten Phi-3 / Phi-3.5 Modells mit den Leistungsmetriken von Microsoft Foundry. Diese Metriken helfen Ihnen, die Effektivität des Modells bei der Erstellung genauer, relevanter und kohärenter Antworten einzuschätzen. Die Leistungsmetriken umfassen:

- **Groundedness**: Bewertet, wie gut die generierten Antworten mit den Informationen aus der Eingabequelle übereinstimmen.
- **Relevanz**: Bewertet die Relevanz der generierten Antworten für die gestellten Fragen.
- **Kohärenz**: Bewertet, wie flüssig der generierte Text ist, natürlich wirkt und menschenähnlicher Sprache ähnelt.
- **Flüssigkeit**: Bewertet die Sprachkompetenz des generierten Textes.
- **GPT Ähnlichkeit**: Vergleicht die generierte Antwort mit der Referenzantwort hinsichtlich Ähnlichkeit.
- **F1 Score**: Berechnet das Verhältnis der gemeinsam genutzten Wörter zwischen generierter Antwort und Quelldaten.

Diese Metriken helfen Ihnen, die Effektivität des Modells bei der Erstellung genauer, relevanter und kohärenter Antworten zu bewerten.

![Evaluate based on performance.](../../../../../../translated_images/de/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Szenario 2: Bewertung des Phi-3 / Phi-3.5 Modells in Microsoft Foundry**

### Bevor Sie beginnen

Dieses Tutorial baut auf den vorherigen Blogbeiträgen "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" und "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" auf. In diesen Beiträgen haben wir den Prozess der Feinabstimmung eines Phi-3 / Phi-3.5 Modells in Microsoft Foundry und der Integration mit Prompt flow durchlaufen.

In diesem Tutorial stellen Sie ein Azure OpenAI-Modell als Evaluator in Microsoft Foundry bereit und verwenden es zur Bewertung Ihres feinabgestimmten Phi-3 / Phi-3.5 Modells.

Bevor Sie mit diesem Tutorial beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen aus den vorherigen Tutorials erfüllen:

1. Einen vorbereiteten Datensatz zur Bewertung des feinabgestimmten Phi-3 / Phi-3.5 Modells.
1. Ein Phi-3 / Phi-3.5 Modell, das feinabgestimmt und in Azure Machine Learning bereitgestellt wurde.
1. Eine mit Ihrem feinabgestimmten Phi-3 / Phi-3.5 Modell in Microsoft Foundry integrierte Prompt flow.

> [!NOTE]
> Sie verwenden die Datei *test_data.jsonl*, die sich im Datenordner des **ULTRACHAT_200k**-Datensatzes befindet, der in den vorherigen Blogbeiträgen heruntergeladen wurde, als Datensatz zur Bewertung des feinabgestimmten Phi-3 / Phi-3.5 Modells.

#### Integration des benutzerdefinierten Phi-3 / Phi-3.5 Modells mit Prompt flow in Microsoft Foundry (Code-first-Ansatz)

> [!NOTE]
> Falls Sie dem Low-Code-Ansatz gefolgt sind, der in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" beschrieben ist, können Sie diese Übung überspringen und mit der nächsten fortfahren.
> Wenn Sie jedoch dem Code-first-Ansatz gefolgt sind, der in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" zum Feinabstimmen und Bereitstellen Ihres Phi-3 / Phi-3.5 Modells beschrieben wird, ist der Prozess zur Verbindung Ihres Modells mit Prompt flow etwas anders. Dies lernen Sie in dieser Übung.

Um fortzufahren, müssen Sie Ihr feinabgestimmtes Phi-3 / Phi-3.5 Modell in Prompt flow in Microsoft Foundry integrieren.

#### Erstellen eines Microsoft Foundry Hubs

Sie müssen zunächst einen Hub erstellen, bevor Sie ein Projekt anlegen. Ein Hub fungiert ähnlich einer Ressourcengruppe und ermöglicht es Ihnen, mehrere Projekte innerhalb von Microsoft Foundry zu organisieren und zu verwalten.
1. Melden Sie sich bei [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) an.

1. Wählen Sie im linken Seitenmenü **Alle Hubs** aus.

1. Wählen Sie im Navigationsmenü **+ Neuer Hub** aus.

    ![Hub erstellen.](../../../../../../translated_images/de/create-hub.5be78fb1e21ffbf1.webp)

1. Führen Sie die folgenden Aufgaben aus:

    - Geben Sie einen **Hub-Namen** ein. Er muss ein eindeutiger Wert sein.
    - Wählen Sie Ihr Azure-**Abonnement** aus.
    - Wählen Sie die **Ressourcengruppe** aus, die verwendet werden soll (erstellen Sie bei Bedarf eine neue).
    - Wählen Sie den gewünschten **Standort** aus.
    - Wählen Sie die zu verwendenden **Azure AI Services verbinden** aus (bei Bedarf eine neue erstellen).
    - Wählen Sie bei **Azure AI Search verbinden** die Option **Verbindung überspringen**.

    ![Hub ausfüllen.](../../../../../../translated_images/de/fill-hub.baaa108495c71e34.webp)

1. Wählen Sie **Weiter**.

#### Microsoft Foundry-Projekt erstellen

1. Wählen Sie im erstellten Hub im linken Seitenmenü **Alle Projekte** aus.

1. Wählen Sie im Navigationsmenü **+ Neues Projekt** aus.

    ![Neues Projekt auswählen.](../../../../../../translated_images/de/select-new-project.cd31c0404088d7a3.webp)

1. Geben Sie einen **Projektnamen** ein. Er muss ein eindeutiger Wert sein.

    ![Projekt erstellen.](../../../../../../translated_images/de/create-project.ca3b71298b90e420.webp)

1. Wählen Sie **Projekt erstellen** aus.

#### Fügen Sie eine benutzerdefinierte Verbindung für das feinabgestimmte Phi-3 / Phi-3.5 Modell hinzu

Um Ihr benutzerdefiniertes Phi-3 / Phi-3.5 Modell in Prompt flow zu integrieren, müssen Sie den Endpunkt und den Schlüssel des Modells in einer benutzerdefinierten Verbindung speichern. Diese Einrichtung stellt den Zugriff auf Ihr benutzerdefiniertes Phi-3 / Phi-3.5 Modell in Prompt flow sicher.

#### API-Schlüssel und Endpunkt-URI des feinabgestimmten Phi-3 / Phi-3.5 Modells einrichten

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigieren Sie zum Azure Machine Learning-Arbeitsbereich, den Sie erstellt haben.

1. Wählen Sie im linken Seitenmenü **Endpoints** aus.

    ![Endpoints auswählen.](../../../../../../translated_images/de/select-endpoints.ee7387ecd68bd18d.webp)

1. Wählen Sie den von Ihnen erstellten Endpunkt aus.

    ![Erstellten Endpunkt auswählen.](../../../../../../translated_images/de/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Wählen Sie im Navigationsmenü **Verwenden** aus.

1. Kopieren Sie Ihren **REST-Endpunkt** und den **Primärschlüssel**.

    ![API-Schlüssel und Endpunkt-URI kopieren.](../../../../../../translated_images/de/copy-endpoint-key.0650c3786bd646ab.webp)

#### Fügen Sie die benutzerdefinierte Verbindung hinzu

1. Besuchen Sie [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigieren Sie zum Microsoft Foundry-Projekt, das Sie erstellt haben.

1. Wählen Sie im erstellten Projekt im linken Seitenmenü **Einstellungen** aus.

1. Wählen Sie **+ Neue Verbindung** aus.

    ![Neue Verbindung auswählen.](../../../../../../translated_images/de/select-new-connection.fa0f35743758a74b.webp)

1. Wählen Sie im Navigationsmenü **Benutzerdefinierte Schlüssel** aus.

    ![Benutzerdefinierte Schlüssel auswählen.](../../../../../../translated_images/de/select-custom-keys.5a3c6b25580a9b67.webp)

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie **+ Schlüssel-Wert-Paare hinzufügen** aus.
    - Geben Sie für den Schlüsselnamen **endpoint** ein und fügen Sie den aus Azure ML Studio kopierten Endpunkt im Wert-Feld ein.
    - Wählen Sie erneut **+ Schlüssel-Wert-Paare hinzufügen** aus.
    - Geben Sie für den Schlüsselnamen **key** ein und fügen Sie den aus Azure ML Studio kopierten Schlüssel im Wert-Feld ein.
    - Nachdem Sie die Schlüssel hinzugefügt haben, wählen Sie **ist geheim**, um zu verhindern, dass der Schlüssel öffentlich sichtbar ist.

    ![Verbindung hinzufügen.](../../../../../../translated_images/de/add-connection.ac7f5faf8b10b0df.webp)

1. Wählen Sie **Verbindung hinzufügen**.

#### Prompt flow erstellen

Sie haben eine benutzerdefinierte Verbindung in Microsoft Foundry hinzugefügt. Nun erstellen wir einen Prompt flow mit den folgenden Schritten. Anschließend verbinden Sie diesen Prompt flow mit der benutzerdefinierten Verbindung, um das feinabgestimmte Modell innerhalb von Prompt flow zu verwenden.

1. Navigieren Sie zum Microsoft Foundry-Projekt, das Sie erstellt haben.

1. Wählen Sie im linken Seitenmenü **Prompt flow** aus.

1. Wählen Sie im Navigationsmenü **+ Erstellen** aus.

    ![Promptflow auswählen.](../../../../../../translated_images/de/select-promptflow.18ff2e61ab9173eb.webp)

1. Wählen Sie im Navigationsmenü **Chat-Flow** aus.

    ![Chat-Flow auswählen.](../../../../../../translated_images/de/select-flow-type.28375125ec9996d3.webp)

1. Geben Sie den zu verwendenden **Ordnernamen** ein.

    ![Chat-Flow auswählen.](../../../../../../translated_images/de/enter-name.02ddf8fb840ad430.webp)

1. Wählen Sie **Erstellen**.

#### Prompt flow einrichten, um mit Ihrem benutzerdefinierten Phi-3 / Phi-3.5 Modell zu chatten

Sie müssen das feinabgestimmte Phi-3 / Phi-3.5 Modell in einen Prompt flow integrieren. Der bereitgestellte vorhandene Prompt flow ist dafür jedoch nicht ausgelegt. Daher müssen Sie den Prompt flow neu gestalten, um die Integration des benutzerdefinierten Modells zu ermöglichen.

1. Führen Sie im Prompt flow die folgenden Aufgaben aus, um den bestehenden Flow neu zu erstellen:

    - Wählen Sie **Modus für Rohdatei** aus.
    - Löschen Sie den gesamten vorhandenen Code in der Datei *flow.dag.yml*.
    - Fügen Sie den folgenden Code in *flow.dag.yml* ein.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Wählen Sie **Speichern** aus.

    ![Modus für Rohdatei auswählen.](../../../../../../translated_images/de/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Fügen Sie den folgenden Code in *integrate_with_promptflow.py* ein, um das benutzerdefinierte Phi-3 / Phi-3.5 Modell in Prompt flow zu verwenden.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Protokollierungseinrichtung
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # „connection“ ist der Name der benutzerdefinierten Verbindung, „endpoint“ und „key“ sind die Schlüssel in der benutzerdefinierten Verbindung
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Die vollständige JSON-Antwort protokollieren
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Prompt flow Code einfügen.](../../../../../../translated_images/de/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Für detailliertere Informationen zur Verwendung von Prompt flow in Microsoft Foundry können Sie [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) konsultieren.

1. Wählen Sie **Chat-Eingabe**, **Chat-Ausgabe** aus, um den Chat mit Ihrem Modell zu aktivieren.

    ![Eingabe und Ausgabe auswählen.](../../../../../../translated_images/de/select-input-output.c187fc58f25fbfc3.webp)

1. Nun sind Sie bereit, mit Ihrem benutzerdefinierten Phi-3 / Phi-3.5 Modell zu chatten. Im nächsten Übungsteil erfahren Sie, wie Sie Prompt flow starten und es nutzen, um mit Ihrem feinabgestimmten Phi-3 / Phi-3.5 Modell zu chatten.

> [!NOTE]
>
> Der neu erstellte Flow sollte dem folgenden Bild ähneln:
>
> ![Beispiel Flow](../../../../../../translated_images/de/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow starten

1. Wählen Sie **Computersitzungen starten**, um Prompt flow zu starten.

    ![Computersitzung starten.](../../../../../../translated_images/de/start-compute-session.9acd8cbbd2c43df1.webp)

1. Wählen Sie **Eingabe validieren und parsen**, um die Parameter zu aktualisieren.

    ![Eingabe validieren.](../../../../../../translated_images/de/validate-input.c1adb9543c6495be.webp)

1. Wählen Sie den **Wert** der **Verbindung** zu der benutzerdefinierten Verbindung aus, die Sie erstellt haben. Zum Beispiel *connection*.

    ![Verbindung auswählen.](../../../../../../translated_images/de/select-connection.1f2b59222bcaafef.webp)

#### Mit Ihrem benutzerdefinierten Phi-3 / Phi-3.5 Modell chatten

1. Wählen Sie **Chat** aus.

    ![Chat auswählen.](../../../../../../translated_images/de/select-chat.0406bd9687d0c49d.webp)

1. Hier ein Beispiel der Ergebnisse: Nun können Sie mit Ihrem benutzerdefinierten Phi-3 / Phi-3.5 Modell chatten. Es wird empfohlen, Fragen basierend auf den Daten zu stellen, die für das Feintuning verwendet wurden.

    ![Mit Prompt flow chatten.](../../../../../../translated_images/de/chat-with-promptflow.1cf8cea112359ada.webp)

### Azure OpenAI bereitstellen, um das Phi-3 / Phi-3.5 Modell zu bewerten

Um das Phi-3 / Phi-3.5 Modell in Microsoft Foundry zu bewerten, müssen Sie ein Azure OpenAI Modell bereitstellen. Dieses Modell wird verwendet, um die Leistung des Phi-3 / Phi-3.5 Modells zu evaluieren.

#### Azure OpenAI bereitstellen

1. Melden Sie sich bei [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) an.

1. Navigieren Sie zum Microsoft Foundry-Projekt, das Sie erstellt haben.

    ![Projekt auswählen.](../../../../../../translated_images/de/select-project-created.5221e0e403e2c9d6.webp)

1. Wählen Sie im erstellten Projekt im linken Seitenmenü **Bereitstellungen** aus.

1. Wählen Sie im Navigationsmenü **Modell bereitstellen** aus.

1. Wählen Sie **Basismodell bereitstellen** aus.

    ![Bereitstellungen auswählen.](../../../../../../translated_images/de/deploy-openai-model.95d812346b25834b.webp)

1. Wählen Sie das Azure OpenAI Modell aus, das Sie verwenden möchten. Zum Beispiel **gpt-4o**.

    ![Azure OpenAI Modell auswählen.](../../../../../../translated_images/de/select-openai-model.959496d7e311546d.webp)

1. Wählen Sie **Bestätigen**.

### Feinabgestimmtes Phi-3 / Phi-3.5 Modell mit der Prompt flow Bewertung von Microsoft Foundry evaluieren

### Neue Bewertung starten

1. Besuchen Sie [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigieren Sie zum Microsoft Foundry-Projekt, das Sie erstellt haben.

    ![Projekt auswählen.](../../../../../../translated_images/de/select-project-created.5221e0e403e2c9d6.webp)

1. Wählen Sie im erstellten Projekt im linken Seitenmenü **Bewertung** aus.

1. Wählen Sie im Navigationsmenü **+ Neue Bewertung** aus.

    ![Bewertung auswählen.](../../../../../../translated_images/de/select-evaluation.2846ad7aaaca7f4f.webp)

1. Wählen Sie die Bewertung **Prompt flow** aus.

    ![Prompt flow Bewertung auswählen.](../../../../../../translated_images/de/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Führen Sie die folgenden Aufgaben aus:

    - Geben Sie den Namen der Bewertung ein. Er muss ein eindeutiger Wert sein.
    - Wählen Sie als Aufgabentyp **Frage und Antwort ohne Kontext** aus, da der in diesem Tutorial verwendete **ULTRACHAT_200k** Datensatz keinen Kontext enthält.
    - Wählen Sie den Prompt flow aus, den Sie bewerten möchten.

    ![Prompt flow Bewertung.](../../../../../../translated_images/de/evaluation-setting1.4aa08259ff7a536e.webp)

1. Wählen Sie **Weiter**.

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie **Datensatz hinzufügen** aus, um den Datensatz hochzuladen. Beispielsweise können Sie die Testdatensatz-Datei *test_data.json1* hochladen, die im **ULTRACHAT_200k** Datensatz enthalten ist.
    - Wählen Sie die entsprechende **Datensatzspalte** aus, die zu Ihrem Datensatz passt. Wenn Sie beispielsweise den **ULTRACHAT_200k** Datensatz verwenden, wählen Sie **${data.prompt}** als Datensatzspalte.

    ![Prompt flow Bewertung.](../../../../../../translated_images/de/evaluation-setting2.07036831ba58d64e.webp)

1. Wählen Sie **Weiter**.

1. Konfigurieren Sie die Leistungs- und Qualitätsmetriken mit den folgenden Aufgaben:

    - Wählen Sie die Leistungs- und Qualitätsmetriken aus, die Sie verwenden möchten.
    - Wählen Sie das Azure OpenAI-Modell aus, das Sie für die Bewertung erstellt haben. Zum Beispiel **gpt-4o**.

    ![Prompt flow Bewertung.](../../../../../../translated_images/de/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Konfigurieren Sie die Risiko- und Sicherheitsmetriken mit den folgenden Aufgaben:

    - Wählen Sie die Risiko- und Sicherheitsmetriken aus, die Sie verwenden möchten.
    - Wählen Sie den Schwellenwert aus, um die Fehlerquote zu berechnen. Zum Beispiel **Mittel**.
    - Für **Frage** wählen Sie **Datenquelle** als **{$data.prompt}**.
    - Für **Antwort** wählen Sie **Datenquelle** als **{$run.outputs.answer}**.
    - Für **Ground Truth** wählen Sie **Datenquelle** als **{$data.message}**.

    ![Prompt flow Bewertung.](../../../../../../translated_images/de/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Wählen Sie **Weiter**.

1. Wählen Sie **Absenden**, um die Bewertung zu starten.

1. Die Bewertung benötigt einige Zeit zur Durchführung. Sie können den Fortschritt im **Bewertung**-Tab verfolgen.

### Bewertungsergebnisse überprüfen

> [!NOTE]
> Die unten dargestellten Ergebnisse dienen zur Veranschaulichung des Bewertungsprozesses. In diesem Tutorial wurde ein Modell verwendet, das auf einem relativ kleinen Datensatz feinabgestimmt wurde, was zu suboptimalen Ergebnissen führen kann. Die tatsächlichen Ergebnisse können je nach Größe, Qualität und Vielfalt des verwendeten Datensatzes sowie der spezifischen Modellkonfiguration erheblich variieren.

Nach Abschluss der Bewertung können Sie die Ergebnisse sowohl der Leistungs- als auch der Sicherheitsmetriken überprüfen.
1. Leistungs- und Qualitätsmetriken:

    - Beurteilen Sie die Effektivität des Modells bei der Erzeugung kohärenter, flüssiger und relevanter Antworten.

    ![Evaluation result.](../../../../../../translated_images/de/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Risiko- und Sicherheitsmetriken:

    - Stellen Sie sicher, dass die Ausgaben des Modells sicher sind und den Prinzipien der verantwortungsvollen KI entsprechen, wobei schädliche oder anstößige Inhalte vermieden werden.

    ![Evaluation result.](../../../../../../translated_images/de/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Sie können nach unten scrollen, um **detaillierte Metrikergebnisse** anzuzeigen.

    ![Evaluation result.](../../../../../../translated_images/de/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Durch die Bewertung Ihres benutzerdefinierten Phi-3 / Phi-3.5-Modells anhand von Leistungs- und Sicherheitsmetriken können Sie bestätigen, dass das Modell nicht nur effektiv ist, sondern auch verantwortungsvollen KI-Praktiken entspricht und somit für den Einsatz in der Praxis bereit ist.

## Herzlichen Glückwunsch!

### Sie haben dieses Tutorial abgeschlossen

Sie haben erfolgreich das feinabgestimmte Phi-3-Modell bewertet, das in Prompt flow in Microsoft Foundry integriert ist. Dies ist ein wichtiger Schritt, um sicherzustellen, dass Ihre KI-Modelle nicht nur gute Leistungen erbringen, sondern auch den Responsible AI-Prinzipien von Microsoft folgen, um vertrauenswürdige und zuverlässige KI-Anwendungen zu erstellen.

![Architecture.](../../../../../../translated_images/de/architecture.10bec55250f5d6a4.webp)

## Azure-Ressourcen bereinigen

Bereinigen Sie Ihre Azure-Ressourcen, um zusätzliche Kosten auf Ihrem Konto zu vermeiden. Gehen Sie zum Azure-Portal und löschen Sie die folgenden Ressourcen:

- Die Azure Machine Learning-Ressource.
- Den Azure Machine Learning Model Endpoint.
- Die Microsoft Foundry-Projektressource.
- Die Microsoft Foundry Prompt flow-Ressource.

### Nächste Schritte

#### Dokumentation

- [Bewerten von KI-Systemen mit dem Responsible AI-Dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluations- und Überwachungsmetriken für generative KI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry-Dokumentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow-Dokumentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Schulungsinhalte

- [Einführung in Microsofts Responsible AI-Ansatz](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Einführung in Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referenz

- [Was ist Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Ankündigung neuer Tools in Azure AI zur Unterstützung beim Aufbau sichererer und vertrauenswürdiger generativer KI-Anwendungen](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluierung generativer KI-Anwendungen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in der Originalsprache ist als maßgebliche Quelle anzusehen. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->