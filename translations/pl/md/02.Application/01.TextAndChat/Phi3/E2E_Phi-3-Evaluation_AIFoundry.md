# Oceń dostosowany model Phi-3 / Phi-3.5 w Microsoft Foundry ze szczególnym uwzględnieniem zasad odpowiedzialnej sztucznej inteligencji Microsoftu

Ten przykład end-to-end (E2E) opiera się na przewodniku "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community.

## Przegląd

### Jak można ocenić bezpieczeństwo i wydajność dostosowanego modelu Phi-3 / Phi-3.5 w Microsoft Foundry?

Dostrajanie modelu może czasami prowadzić do niezamierzonych lub niepożądanych odpowiedzi. Aby zapewnić, że model pozostaje bezpieczny i skuteczny, ważne jest, aby ocenić potencjał modelu do generowania szkodliwych treści oraz jego zdolność do generowania dokładnych, istotnych i spójnych odpowiedzi. W tym samouczku nauczysz się, jak ocenić bezpieczeństwo i wydajność dostosowanego modelu Phi-3 / Phi-3.5 zintegrowanego z Prompt flow w Microsoft Foundry.

Oto proces oceny Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/pl/architecture.10bec55250f5d6a4.webp)

*Źródło obrazu: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Aby uzyskać bardziej szczegółowe informacje i odkryć dodatkowe zasoby dotyczące Phi-3 / Phi-3.5, odwiedź [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Wymagania wstępne

- [Python](https://www.python.org/downloads)
- [Subskrypcja Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Dostosowany model Phi-3 / Phi-3.5

### Spis treści

1. [**Scenariusz 1: Wprowadzenie do oceny Prompt flow w Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Wprowadzenie do oceny bezpieczeństwa](#wprowadzenie-do-oceny-bezpieczeństwa)
    - [Wprowadzenie do oceny wydajności](#wprowadzenie-do-oceny-wydajności)

1. [**Scenariusz 2: Ocena modelu Phi-3 / Phi-3.5 w Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Zanim zaczniesz](#zanim-zaczniesz)
    - [Wdrażanie Azure OpenAI do oceny modelu Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Ocena dostosowanego modelu Phi-3 / Phi-3.5 za pomocą oceny Prompt flow Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Gratulacje!](#gratulacje)

## **Scenariusz 1: Wprowadzenie do oceny Prompt flow w Microsoft Foundry**

### Wprowadzenie do oceny bezpieczeństwa

Aby zapewnić, że Twój model AI jest etyczny i bezpieczny, kluczowe jest ocenianie go zgodnie z zasadami odpowiedzialnej sztucznej inteligencji Microsoft. W Microsoft Foundry oceny bezpieczeństwa pozwalają na ocenę podatności modelu na ataki jailbreak oraz jego zdolności do generowania szkodliwych treści, co jest bezpośrednio zgodne z tymi zasadami.

![Safaty evaluation.](../../../../../../translated_images/pl/safety-evaluation.083586ec88dfa950.webp)

*Źródło obrazu: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Zasady odpowiedzialnej AI Microsoft

Przed rozpoczęciem kroków technicznych ważne jest zrozumienie zasad odpowiedzialnej sztucznej inteligencji Microsoft, etycznych ram zaprojektowanych, aby kierować odpowiedzialnym rozwojem, wdrażaniem i działaniem systemów AI. Zasady te kierują odpowiedzialnym projektowaniem, rozwijaniem i wdrażaniem systemów AI, zapewniając, że technologie AI są tworzone w sposób sprawiedliwy, przejrzysty i włączający. Te zasady stanowią podstawę oceny bezpieczeństwa modeli AI.

Zasady odpowiedzialnej AI Microsoft obejmują:

- **Sprawiedliwość i inkluzywność**: Systemy AI powinny traktować wszystkich sprawiedliwie i unikać różnicowania podobnie sytuowanych grup osób. Na przykład, kiedy systemy AI udzielają wskazówek dotyczących leczenia medycznego, wniosków kredytowych lub zatrudnienia, powinny one udzielać tych samych rekomendacji wszystkim osobom o podobnych objawach, sytuacji finansowej lub kwalifikacjach zawodowych.

- **Niezawodność i bezpieczeństwo**: Aby budować zaufanie, systemy AI muszą działać niezawodnie, bezpiecznie i konsekwentnie. Systemy te powinny być w stanie działać zgodnie z pierwotnym zaprojektowaniem, bezpiecznie reagować na nieprzewidziane warunki oraz być odporne na szkodliwe manipulacje. Ich zachowanie i zakres warunków, które mogą obsłużyć, odzwierciedlają zakres sytuacji, które twórcy przewidzieli podczas projektowania i testowania.

- **Przejrzystość**: Gdy systemy AI pomagają podejmować decyzje mające ogromny wpływ na życie ludzi, ważne jest, aby ludzie rozumieli, w jaki sposób te decyzje zostały podjęte. Na przykład bank może używać systemu AI do oceny zdolności kredytowej osoby. Firma może używać systemu AI do określenia najbardziej kwalifikowanych kandydatów do pracy.

- **Prywatność i bezpieczeństwo**: Wraz z rosnącą popularnością AI, ochrona prywatności oraz bezpieczeństwo informacji osobistych i biznesowych stają się coraz ważniejsze i bardziej złożone. W przypadku AI prywatność i bezpieczeństwo danych wymagają szczególnej uwagi, ponieważ dostęp do danych jest niezbędny, aby systemy AI mogły dokonywać dokładnych i świadomych przewidywań oraz decyzji dotyczących ludzi.

- **Odpowiedzialność**: Osoby, które projektują i wdrażają systemy AI, muszą być odpowiedzialne za sposób działania swoich systemów. Organizacje powinny opracowywać normy odpowiedzialności, korzystając ze standardów branżowych. Normy te mogą zapewnić, że systemy AI nie będą ostatecznym autorytetem w żadnej decyzji wpływającej na życie ludzi. Mogą także zapewnić, że ludzie zachowają znaczącą kontrolę nad w przeciwnym razie wysoce autonomicznymi systemami AI.

![Fill hub.](../../../../../../translated_images/pl/responsibleai2.c07ef430113fad8c.webp)

*Źródło obrazu: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Aby dowiedzieć się więcej o zasadach odpowiedzialnej AI Microsoft, odwiedź [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metryki bezpieczeństwa

W tym samouczku ocenisz bezpieczeństwo dostosowanego modelu Phi-3 za pomocą metryk bezpieczeństwa Microsoft Foundry. Metryki te pomagają ocenić potencjał modelu do generowania szkodliwych treści oraz jego podatność na ataki jailbreak. Metryki bezpieczeństwa obejmują:

- **Treści związane z samookaleczeniem**: Ocena, czy model ma tendencję do generowania treści dotyczących samookaleczeń.
- **Treści nienawistne i niesprawiedliwe**: Ocena, czy model ma tendencję do generowania treści nienawistnych lub niesprawiedliwych.
- **Treści przemocowe**: Ocena, czy model ma tendencję do generowania treści przemocowych.
- **Treści seksualne**: Ocena, czy model ma tendencję do generowania nieodpowiednich treści seksualnych.

Ocena tych aspektów zapewnia, że model AI nie generuje szkodliwych ani obraźliwych treści, co jest zgodne z wartościami społecznymi i standardami regulacyjnymi.

![Evaluate based on safety.](../../../../../../translated_images/pl/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Wprowadzenie do oceny wydajności

Aby upewnić się, że Twój model AI działa zgodnie z oczekiwaniami, ważne jest ocenianie jego wydajności przy użyciu metryk wydajności. W Microsoft Foundry oceny wydajności pozwalają ocenić skuteczność modelu w generowaniu dokładnych, istotnych i spójnych odpowiedzi.

![Safaty evaluation.](../../../../../../translated_images/pl/performance-evaluation.48b3e7e01a098740.webp)

*Źródło obrazu: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metryki wydajności

W tym samouczku ocenisz wydajność dostosowanego modelu Phi-3 / Phi-3.5 za pomocą metryk wydajności Microsoft Foundry. Metryki te pomagają ocenić skuteczność modelu w generowaniu dokładnych, istotnych i spójnych odpowiedzi. Metryki wydajności obejmują:

- **Ugruntowanie**: Ocena, jak dobrze wygenerowane odpowiedzi pokrywają się z informacjami z danych wejściowych.
- **Istotność**: Ocena trafności wygenerowanych odpowiedzi względem zadanych pytań.
- **Spójność**: Ocena, jak płynnie generowany tekst płynie, czy czyta się naturalnie i przypomina język ludzki.
- **Płynność**: Ocena biegłości językowej wygenerowanego tekstu.
- **Podobieństwo GPT**: Porównanie wygenerowanej odpowiedzi z prawdziwą odpowiedzią pod kątem podobieństwa.
- **Wynik F1**: Oblicza stosunek wspólnych słów między wygenerowaną odpowiedzią a danymi źródłowymi.

Metryki te pomagają ocenić skuteczność modelu w generowaniu dokładnych, istotnych i spójnych odpowiedzi.

![Evaluate based on performance.](../../../../../../translated_images/pl/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenariusz 2: Ocena modelu Phi-3 / Phi-3.5 w Microsoft Foundry**

### Zanim zaczniesz

Ten samouczek jest kontynuacją poprzednich wpisów na blogu, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" oraz "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." W tych wpisach przeprowadziliśmy proces dostrajania modelu Phi-3 / Phi-3.5 w Microsoft Foundry oraz jego integrację z Prompt flow.

W tym samouczku wdrożysz model Azure OpenAI jako oceniający w Microsoft Foundry i użyjesz go do oceny dostosowanego modelu Phi-3 / Phi-3.5.

Przed rozpoczęciem tego samouczka upewnij się, że masz następujące wymagania wstępne, opisane w poprzednich samouczkach:

1. Przygotowany zestaw danych do oceny dostosowanego modelu Phi-3 / Phi-3.5.
1. Model Phi-3 / Phi-3.5, który został dostrojony i wdrożony na Azure Machine Learning.
1. Prompt flow zintegrowany z Twoim dostosowanym modelem Phi-3 / Phi-3.5 w Microsoft Foundry.

> [!NOTE]
> Do oceny dostosowanego modelu Phi-3 / Phi-3.5 użyjesz pliku *test_data.jsonl*, który znajduje się w folderze danych z zestawu danych **ULTRACHAT_200k** pobranego w poprzednich wpisach na blogu.

#### Integracja dostosowanego modelu Phi-3 / Phi-3.5 z Prompt flow w Microsoft Foundry (podejście kodowe)

> [!NOTE]
> Jeśli korzystałeś z podejścia low-code opisanego w "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", możesz pominąć to ćwiczenie i przejść do następnego.
> Jeśli jednak korzystałeś z podejścia kodowego opisanego w "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" do dostrajania i wdrażania modelu Phi-3 / Phi-3.5, proces łączenia modelu z Prompt flow jest nieco inny. Nauczysz się tego procesu w tym ćwiczeniu.

Aby kontynuować, musisz zintegrować swój dostosowany model Phi-3 / Phi-3.5 z Prompt flow w Microsoft Foundry.

#### Utwórz Microsoft Foundry Hub

Musisz utworzyć Hub zanim utworzysz Projekt. Hub działa jak Grupa Zasobów, pozwalając Ci organizować i zarządzać wieloma Projektami w Microsoft Foundry.
1. Zaloguj się do [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Wybierz **All hubs** z lewej zakładki.

1. Wybierz **+ New hub** z menu nawigacyjnego.

    ![Create hub.](../../../../../../translated_images/pl/create-hub.5be78fb1e21ffbf1.webp)

1. Wykonaj następujące zadania:

    - Wprowadź **Hub name**. Musi to być unikalna wartość.
    - Wybierz swoją subskrypcję Azure **Subscription**.
    - Wybierz **Resource group**, której chcesz użyć (utwórz nową, jeśli to konieczne).
    - Wybierz **Location**, którego chcesz użyć.
    - Wybierz **Connect Azure AI Services**, którego chcesz użyć (utwórz nowy, jeśli to konieczne).
    - Wybierz **Connect Azure AI Search** i zaznacz **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/pl/fill-hub.baaa108495c71e34.webp)

1. Wybierz **Next**.

#### Utwórz projekt Microsoft Foundry

1. W hubie, który utworzyłeś, wybierz **All projects** z lewej zakładki.

1. Wybierz **+ New project** z menu nawigacyjnego.

    ![Select new project.](../../../../../../translated_images/pl/select-new-project.cd31c0404088d7a3.webp)

1. Wprowadź **Project name**. Musi to być unikalna wartość.

    ![Create project.](../../../../../../translated_images/pl/create-project.ca3b71298b90e420.webp)

1. Wybierz **Create a project**.

#### Dodaj niestandardowe połączenie dla wytrenowanego modelu Phi-3 / Phi-3.5

Aby zintegrować swój niestandardowy model Phi-3 / Phi-3.5 z Prompt flow, musisz zapisać punkt końcowy modelu oraz klucz w niestandardowym połączeniu. To ustawienie zapewnia dostęp do Twojego niestandardowego modelu Phi-3 / Phi-3.5 w Prompt flow.

#### Ustaw klucz api i URI punktu końcowego wytrenowanego modelu Phi-3 / Phi-3.5

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Przejdź do workspace Azure Machine Learning, które utworzyłeś.

1. Wybierz **Endpoints** z lewej zakładki.

    ![Select endpoints.](../../../../../../translated_images/pl/select-endpoints.ee7387ecd68bd18d.webp)

1. Wybierz punkt końcowy, który utworzyłeś.

    ![Select endpoints.](../../../../../../translated_images/pl/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Wybierz **Consume** z menu nawigacyjnego.

1. Skopiuj swój **REST endpoint** oraz **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pl/copy-endpoint-key.0650c3786bd646ab.webp)

#### Dodaj niestandardowe połączenie

1. Odwiedź [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Przejdź do projektu Microsoft Foundry, który utworzyłeś.

1. W projekcie, który utworzyłeś, wybierz **Settings** z lewej zakładki.

1. Wybierz **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/pl/select-new-connection.fa0f35743758a74b.webp)

1. Wybierz **Custom keys** z menu nawigacyjnego.

    ![Select custom keys.](../../../../../../translated_images/pl/select-custom-keys.5a3c6b25580a9b67.webp)

1. Wykonaj następujące zadania:

    - Wybierz **+ Add key value pairs**.
    - Dla nazwy klucza wpisz **endpoint** i wklej skopiowany z Azure ML Studio punkt końcowy w pole wartości.
    - Ponownie wybierz **+ Add key value pairs**.
    - Dla nazwy klucza wpisz **key** i wklej skopiowany z Azure ML Studio klucz w pole wartości.
    - Po dodaniu kluczy zaznacz **is secret**, aby zapobiec ujawnieniu klucza.

    ![Add connection.](../../../../../../translated_images/pl/add-connection.ac7f5faf8b10b0df.webp)

1. Wybierz **Add connection**.

#### Utwórz Prompt flow

Dodałeś niestandardowe połączenie w Microsoft Foundry. Teraz utwórz Prompt flow, korzystając z następujących kroków. Następnie połącz ten Prompt flow z niestandardowym połączeniem, aby użyć wytrenowanego modelu w Prompt flow.

1. Przejdź do projektu Microsoft Foundry, który utworzyłeś.

1. Wybierz **Prompt flow** z lewej zakładki.

1. Wybierz **+ Create** z menu nawigacyjnego.

    ![Select Promptflow.](../../../../../../translated_images/pl/select-promptflow.18ff2e61ab9173eb.webp)

1. Wybierz **Chat flow** z menu nawigacyjnego.

    ![Select chat flow.](../../../../../../translated_images/pl/select-flow-type.28375125ec9996d3.webp)

1. Wprowadź **Folder name**, którego chcesz użyć.

    ![Select chat flow.](../../../../../../translated_images/pl/enter-name.02ddf8fb840ad430.webp)

1. Wybierz **Create**.

#### Skonfiguruj Prompt flow do rozmowy z niestandardowym modelem Phi-3 / Phi-3.5

Musisz zintegrować wytrenowany model Phi-3 / Phi-3.5 z Prompt flow. Jednak istniejący Prompt flow nie jest zaprojektowany do tego celu. Dlatego musisz przeprojektować Prompt flow, aby umożliwić integrację niestandardowego modelu.

1. W Prompt flow wykonaj następujące zadania, aby przebudować istniejący przepływ:

    - Wybierz **Raw file mode**.
    - Usuń cały istniejący kod w pliku *flow.dag.yml*.
    - Dodaj następujący kod do *flow.dag.yml*.

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

    - Wybierz **Save**.

    ![Select raw file mode.](../../../../../../translated_images/pl/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Dodaj następujący kod do *integrate_with_promptflow.py*, aby użyć niestandardowego modelu Phi-3 / Phi-3.5 w Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Konfiguracja logowania
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

        # "connection" to nazwa Własnego Połączenia, "endpoint", "key" to klucze w Własnym Połączeniu
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
            
            # Zaloguj pełną odpowiedź JSON
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

    ![Paste prompt flow code.](../../../../../../translated_images/pl/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Aby uzyskać bardziej szczegółowe informacje na temat korzystania z Prompt flow w Microsoft Foundry, możesz zapoznać się z [Prompt flow w Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Wybierz **Chat input**, **Chat output**, aby umożliwić rozmowę z modelem.

    ![Select Input Output.](../../../../../../translated_images/pl/select-input-output.c187fc58f25fbfc3.webp)

1. Teraz możesz rozmawiać z niestandardowym modelem Phi-3 / Phi-3.5. W następnym ćwiczeniu nauczysz się, jak uruchomić Prompt flow i używać go do rozmowy z wytrenowanym modelem Phi-3 / Phi-3.5.

> [!NOTE]
>
> Przebudowany przepływ powinien wyglądać jak na poniższym obrazku:
>
> ![Flow example](../../../../../../translated_images/pl/graph-example.82fd1bcdd3fc545b.webp)
>

#### Uruchom Prompt flow

1. Wybierz **Start compute sessions**, aby uruchomić Prompt flow.

    ![Start compute session.](../../../../../../translated_images/pl/start-compute-session.9acd8cbbd2c43df1.webp)

1. Wybierz **Validate and parse input**, aby odświeżyć parametry.

    ![Validate input.](../../../../../../translated_images/pl/validate-input.c1adb9543c6495be.webp)

1. Wybierz wartość **Value** połączenia **connection** utworzonego niestandardowego połączenia. Na przykład, *connection*.

    ![Connection.](../../../../../../translated_images/pl/select-connection.1f2b59222bcaafef.webp)

#### Rozmawiaj ze swoim niestandardowym modelem Phi-3 / Phi-3.5

1. Wybierz **Chat**.

    ![Select chat.](../../../../../../translated_images/pl/select-chat.0406bd9687d0c49d.webp)

1. Oto przykład wyników: teraz możesz rozmawiać z niestandardowym modelem Phi-3 / Phi-3.5. Zaleca się zadawanie pytań opartych na danych użytych do fine-tuningu.

    ![Chat with prompt flow.](../../../../../../translated_images/pl/chat-with-promptflow.1cf8cea112359ada.webp)

### Wdróż Azure OpenAI, aby ocenić model Phi-3 / Phi-3.5

Aby ocenić model Phi-3 / Phi-3.5 w Microsoft Foundry, musisz wdrożyć model Azure OpenAI. Model ten zostanie użyty do oceny wydajności modelu Phi-3 / Phi-3.5.

#### Wdróż Azure OpenAI

1. Zaloguj się do [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Przejdź do projektu Microsoft Foundry, który utworzyłeś.

    ![Select Project.](../../../../../../translated_images/pl/select-project-created.5221e0e403e2c9d6.webp)

1. W projekcie, który utworzyłeś, wybierz **Deployments** z lewej zakładki.

1. Wybierz **+ Deploy model** z menu nawigacyjnego.

1. Wybierz **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/pl/deploy-openai-model.95d812346b25834b.webp)

1. Wybierz model Azure OpenAI, którego chcesz użyć. Na przykład, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/pl/select-openai-model.959496d7e311546d.webp)

1. Wybierz **Confirm**.

### Oceń wytrenowany model Phi-3 / Phi-3.5 przy użyciu oceny Prompt flow w Microsoft Foundry

### Rozpocznij nową ocenę

1. Odwiedź [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Przejdź do projektu Microsoft Foundry, który utworzyłeś.

    ![Select Project.](../../../../../../translated_images/pl/select-project-created.5221e0e403e2c9d6.webp)

1. W projekcie, który utworzyłeś, wybierz **Evaluation** z lewej zakładki.

1. Wybierz **+ New evaluation** z menu nawigacyjnego.

    ![Select evaluation.](../../../../../../translated_images/pl/select-evaluation.2846ad7aaaca7f4f.webp)

1. Wybierz ocenę **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/pl/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Wykonaj następujące zadania:

    - Wpisz nazwę oceny. Musi to być unikalna wartość.
    - Wybierz typ zadania **Question and answer without context**. Ponieważ zestaw danych **ULTRACHAT_200k** używany w tym poradniku nie zawiera kontekstu.
    - Wybierz prompt flow, które chcesz ocenić.

    ![Prompt flow evaluation.](../../../../../../translated_images/pl/evaluation-setting1.4aa08259ff7a536e.webp)

1. Wybierz **Next**.

1. Wykonaj następujące zadania:

    - Wybierz **Add your dataset**, aby przesłać zestaw danych. Na przykład możesz przesłać plik testowy zestawu danych, taki jak *test_data.json1*, który jest dołączony podczas pobierania zestawu danych **ULTRACHAT_200k**.
    - Wybierz odpowiednią kolumnę **Dataset column** odpowiadającą Twojemu zestawowi danych. Na przykład, jeśli używasz zestawu danych **ULTRACHAT_200k**, wybierz **${data.prompt}** jako kolumnę zestawu danych.

    ![Prompt flow evaluation.](../../../../../../translated_images/pl/evaluation-setting2.07036831ba58d64e.webp)

1. Wybierz **Next**.

1. Wykonaj następujące zadania, aby skonfigurować metryki wydajności i jakości:

    - Wybierz metryki wydajności i jakości, których chcesz użyć.
    - Wybierz model Azure OpenAI, który utworzyłeś do oceny. Na przykład wybierz **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pl/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Wykonaj następujące zadania, aby skonfigurować metryki ryzyka i bezpieczeństwa:

    - Wybierz metryki ryzyka i bezpieczeństwa, których chcesz użyć.
    - Wybierz próg do obliczenia wskaźnika defektów, którego chcesz użyć. Na przykład wybierz **Medium**.
    - Dla **question** wybierz **Data source** jako **{$data.prompt}**.
    - Dla **answer** wybierz **Data source** jako **{$run.outputs.answer}**.
    - Dla **ground_truth** wybierz **Data source** jako **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pl/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Wybierz **Next**.

1. Wybierz **Submit**, aby rozpocząć ocenę.

1. Ocena zajmie trochę czasu. Możesz monitorować postęp na zakładce **Evaluation**.

### Przejrzyj wyniki oceny

> [!NOTE]
> Wyniki przedstawione poniżej mają na celu zilustrowanie procesu oceny. W tym poradniku użyliśmy modelu wytrenowanego na stosunkowo małym zbiorze danych, co może prowadzić do nieoptymalnych wyników. Rzeczywiste wyniki mogą się znacznie różnić w zależności od wielkości, jakości i różnorodności użytego zbioru danych oraz konkretnej konfiguracji modelu.

Po zakończeniu oceny możesz przejrzeć wyniki dla metryk wydajności i bezpieczeństwa.
1. Metryki wydajności i jakości:

    - ocena skuteczności modelu w generowaniu spójnych, płynnych i istotnych odpowiedzi.

    ![Wynik oceny.](../../../../../../translated_images/pl/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Metryki ryzyka i bezpieczeństwa:

    - Zapewnienie, że wyniki modelu są bezpieczne i zgodne z Zasadami Odpowiedzialnej Sztucznej Inteligencji, unikając wszelkich szkodliwych lub obraźliwych treści.

    ![Wynik oceny.](../../../../../../translated_images/pl/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Możesz przewinąć w dół, aby zobaczyć **Szczegółowy wynik metryk**.

    ![Wynik oceny.](../../../../../../translated_images/pl/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Oceniając swój niestandardowy model Phi-3 / Phi-3.5 pod kątem zarówno metryk wydajności, jak i bezpieczeństwa, możesz potwierdzić, że model jest nie tylko skuteczny, ale także przestrzega praktyk odpowiedzialnej sztucznej inteligencji, co czyni go gotowym do wdrożenia w rzeczywistych warunkach.

## Gratulacje!

### Ukończyłeś ten samouczek

Pomyślnie oceniłeś dostrojoną wersję modelu Phi-3 zintegrowaną z Prompt flow w Microsoft Foundry. Jest to ważny krok w zapewnieniu, że Twoje modele AI nie tylko działają efektywnie, ale również przestrzegają zasad Odpowiedzialnej Sztucznej Inteligencji Microsoft, pomagając budować wiarygodne i niezawodne aplikacje AI.

![Architektura.](../../../../../../translated_images/pl/architecture.10bec55250f5d6a4.webp)

## Sprzątanie zasobów Azure

Posprzątaj swoje zasoby Azure, aby uniknąć dodatkowych opłat na swoim koncie. Przejdź do portalu Azure i usuń następujące zasoby:

- Zasób Azure Machine Learning.
- Punkt końcowy modelu Azure Machine Learning.
- Zasób projektu Microsoft Foundry.
- Zasób Prompt flow Microsoft Foundry.

### Kolejne kroki

#### Dokumentacja

- [Oceń systemy AI za pomocą pulpitu nawigacyjnego Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metryki oceny i monitorowania dla generatywnej AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Dokumentacja Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Dokumentacja Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Materiały szkoleniowe

- [Wprowadzenie do podejścia Microsoft do Odpowiedzialnej Sztucznej Inteligencji](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Wprowadzenie do Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referencje

- [Czym jest Odpowiedzialna AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Ogłoszenie nowych narzędzi w Azure AI, które pomogą Ci tworzyć bezpieczniejsze i bardziej wiarygodne aplikacje generatywnej AI](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Ocena aplikacji generatywnej AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->