<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T16:25:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "pl"
}
-->
# Oceń dostosowany model Phi-3 / Phi-3.5 w Azure AI Foundry z uwzględnieniem zasad odpowiedzialnej sztucznej inteligencji Microsoftu

Ten kompleksowy (E2E) przykład opiera się na przewodniku "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community.

## Przegląd

### Jak ocenić bezpieczeństwo i wydajność dostosowanego modelu Phi-3 / Phi-3.5 w Azure AI Foundry?

Dostosowanie modelu może czasem prowadzić do niezamierzonych lub niepożądanych odpowiedzi. Aby upewnić się, że model pozostaje bezpieczny i skuteczny, ważne jest ocenienie jego potencjału do generowania szkodliwych treści oraz zdolności do tworzenia precyzyjnych, istotnych i spójnych odpowiedzi. W tym samouczku nauczysz się, jak ocenić bezpieczeństwo i wydajność dostosowanego modelu Phi-3 / Phi-3.5 zintegrowanego z Prompt flow w Azure AI Foundry.

Poniżej znajduje się proces oceny w Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.pl.png)

*Źródło obrazu: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Aby uzyskać bardziej szczegółowe informacje i poznać dodatkowe zasoby dotyczące Phi-3 / Phi-3.5, odwiedź [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Wymagania wstępne

- [Python](https://www.python.org/downloads)
- [Subskrypcja Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Dostosowany model Phi-3 / Phi-3.5

### Spis treści

1. [**Scenariusz 1: Wprowadzenie do oceny Prompt flow w Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Wprowadzenie do oceny bezpieczeństwa](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Wprowadzenie do oceny wydajności](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenariusz 2: Ocena modelu Phi-3 / Phi-3.5 w Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Przed rozpoczęciem](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Wdrażanie Azure OpenAI do oceny modelu Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ocena dostosowanego modelu Phi-3 / Phi-3.5 przy użyciu oceny Prompt flow w Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Gratulacje!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenariusz 1: Wprowadzenie do oceny Prompt flow w Azure AI Foundry**

### Wprowadzenie do oceny bezpieczeństwa

Aby zapewnić, że Twój model AI jest etyczny i bezpieczny, kluczowe jest ocenienie go pod kątem zasad odpowiedzialnej sztucznej inteligencji Microsoftu. W Azure AI Foundry oceny bezpieczeństwa pozwalają sprawdzić podatność modelu na ataki jailbreak oraz jego potencjał do generowania szkodliwych treści, co jest bezpośrednio zgodne z tymi zasadami.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.pl.png)

*Źródło obrazu: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Zasady odpowiedzialnej sztucznej inteligencji Microsoftu

Przed rozpoczęciem kroków technicznych ważne jest zrozumienie zasad odpowiedzialnej sztucznej inteligencji Microsoftu — ram etycznych mających na celu kierowanie odpowiedzialnym rozwojem, wdrażaniem i działaniem systemów AI. Zasady te kierują odpowiedzialnym projektowaniem, tworzeniem i wdrażaniem systemów AI, zapewniając, że technologie AI są budowane w sposób sprawiedliwy, przejrzysty i inkluzywny. Stanowią one podstawę oceny bezpieczeństwa modeli AI.

Zasady odpowiedzialnej AI Microsoftu obejmują:

- **Sprawiedliwość i inkluzywność**: Systemy AI powinny traktować wszystkich sprawiedliwie i unikać różnicowania podobnych grup ludzi. Na przykład, gdy systemy AI udzielają wskazówek dotyczących leczenia, wniosków kredytowych czy zatrudnienia, powinny one oferować takie same rekomendacje wszystkim osobom o podobnych objawach, sytuacji finansowej czy kwalifikacjach zawodowych.

- **Niezawodność i bezpieczeństwo**: Aby budować zaufanie, systemy AI muszą działać niezawodnie, bezpiecznie i konsekwentnie. Powinny funkcjonować zgodnie z pierwotnym zamierzeniem, reagować bezpiecznie na nieprzewidziane sytuacje oraz być odporne na szkodliwe manipulacje. Ich zachowanie i zakres obsługiwanych warunków odzwierciedla przewidywane przez twórców sytuacje i okoliczności podczas projektowania i testów.

- **Przejrzystość**: Gdy systemy AI wspierają decyzje mające ogromny wpływ na życie ludzi, ważne jest, aby ludzie rozumieli, jak te decyzje zostały podjęte. Na przykład bank może korzystać z systemu AI do oceny zdolności kredytowej osoby. Firma może używać AI do wyboru najbardziej kwalifikowanych kandydatów do pracy.

- **Prywatność i bezpieczeństwo**: Wraz z rosnącą popularnością AI ochrona prywatności oraz bezpieczeństwo danych osobowych i firmowych stają się coraz ważniejsze i bardziej złożone. W AI prywatność i bezpieczeństwo danych wymagają szczególnej uwagi, ponieważ dostęp do danych jest niezbędny do tworzenia dokładnych i świadomych prognoz oraz decyzji dotyczących ludzi.

- **Odpowiedzialność**: Osoby projektujące i wdrażające systemy AI muszą ponosić odpowiedzialność za sposób działania swoich systemów. Organizacje powinny korzystać z branżowych standardów, aby opracować normy odpowiedzialności. Normy te zapewniają, że systemy AI nie są ostateczną instancją w żadnej decyzji wpływającej na życie ludzi i że ludzie zachowują znaczącą kontrolę nad wysoce autonomicznymi systemami AI.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.pl.png)

*Źródło obrazu: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Aby dowiedzieć się więcej o zasadach odpowiedzialnej AI Microsoftu, odwiedź [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metryki bezpieczeństwa

W tym samouczku ocenisz bezpieczeństwo dostosowanego modelu Phi-3, korzystając z metryk bezpieczeństwa Azure AI Foundry. Metryki te pomagają ocenić potencjał modelu do generowania szkodliwych treści oraz jego podatność na ataki jailbreak. Metryki bezpieczeństwa obejmują:

- **Treści związane z samookaleczeniem**: Ocena, czy model ma tendencję do generowania treści związanych z samookaleczeniem.
- **Treści nienawistne i niesprawiedliwe**: Ocena, czy model ma tendencję do tworzenia treści nienawistnych lub niesprawiedliwych.
- **Treści przemocowe**: Ocena, czy model ma tendencję do generowania treści przemocowych.
- **Treści seksualne**: Ocena, czy model ma tendencję do tworzenia nieodpowiednich treści seksualnych.

Ocena tych aspektów zapewnia, że model AI nie generuje treści szkodliwych lub obraźliwych, zgodnie z wartościami społecznymi i wymogami regulacyjnymi.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.pl.png)

### Wprowadzenie do oceny wydajności

Aby upewnić się, że Twój model AI działa zgodnie z oczekiwaniami, ważne jest ocenienie jego wydajności względem metryk wydajności. W Azure AI Foundry oceny wydajności pozwalają sprawdzić skuteczność modelu w generowaniu dokładnych, istotnych i spójnych odpowiedzi.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.pl.png)

*Źródło obrazu: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metryki wydajności

W tym samouczku ocenisz wydajność dostosowanego modelu Phi-3 / Phi-3.5, korzystając z metryk wydajności Azure AI Foundry. Metryki te pomagają ocenić skuteczność modelu w generowaniu dokładnych, istotnych i spójnych odpowiedzi. Metryki wydajności obejmują:

- **Oparcie na źródle**: Ocena, jak dobrze wygenerowane odpowiedzi są zgodne z informacjami pochodzącymi ze źródła wejściowego.
- **Istotność**: Ocena trafności wygenerowanych odpowiedzi względem zadanych pytań.
- **Spójność**: Ocena płynności tekstu, naturalności oraz podobieństwa do języka ludzkiego.
- **Płynność**: Ocena biegłości językowej wygenerowanego tekstu.
- **Podobieństwo do GPT**: Porównanie wygenerowanej odpowiedzi z prawdziwą odpowiedzią pod względem podobieństwa.
- **Wynik F1**: Oblicza stosunek wspólnych słów między wygenerowaną odpowiedzią a danymi źródłowymi.

Te metryki pomagają ocenić skuteczność modelu w generowaniu dokładnych, istotnych i spójnych odpowiedzi.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.pl.png)

## **Scenariusz 2: Ocena modelu Phi-3 / Phi-3.5 w Azure AI Foundry**

### Przed rozpoczęciem

Ten samouczek jest kontynuacją poprzednich wpisów na blogu, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" oraz "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." W tych wpisach przeprowadziliśmy proces dostosowywania modelu Phi-3 / Phi-3.5 w Azure AI Foundry oraz jego integracji z Prompt flow.

W tym samouczku wdrożysz model Azure OpenAI jako ocenianie w Azure AI Foundry i użyjesz go do oceny swojego dostosowanego modelu Phi-3 / Phi-3.5.

Przed rozpoczęciem tego samouczka upewnij się, że masz następujące wymagania wstępne, opisane w poprzednich tutorialach:

1. Przygotowany zestaw danych do oceny dostosowanego modelu Phi-3 / Phi-3.5.
1. Model Phi-3 / Phi-3.5, który został dostosowany i wdrożony w Azure Machine Learning.
1. Prompt flow zintegrowany z Twoim dostosowanym modelem Phi-3 / Phi-3.5 w Azure AI Foundry.

> [!NOTE]
> Do oceny dostosowanego modelu Phi-3 / Phi-3.5 użyjesz pliku *test_data.jsonl*, znajdującego się w folderze data w zestawie danych **ULTRACHAT_200k** pobranym w poprzednich wpisach na blogu.

#### Integracja niestandardowego modelu Phi-3 / Phi-3.5 z Prompt flow w Azure AI Foundry (podejście kodowe)

> [!NOTE]
> Jeśli korzystałeś z podejścia low-code opisanego w "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", możesz pominąć to ćwiczenie i przejść do kolejnego.
> Jeśli jednak korzystałeś z podejścia kodowego opisanego w "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" do dostosowania i wdrożenia swojego modelu Phi-3 / Phi-3.5, proces połączenia modelu z Prompt flow jest nieco inny. Nauczysz się tego w tym ćwiczeniu.

Aby kontynuować, musisz zintegrować swój dostosowany model Phi-3 / Phi-3.5 z Prompt flow w Azure AI Foundry.

#### Utwórz Azure AI Foundry Hub

Musisz utworzyć Hub przed utworzeniem Projektu. Hub działa jak grupa zasobów, umożliwiając organizację i zarządzanie wieloma projektami w Azure AI Foundry.

1. Zaloguj się do [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Wybierz **All hubs** z lewego panelu.

1. Wybierz **+ New hub** z menu nawigacyjnego.

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.pl.png)

1. Wykonaj następujące czynności:

    - Wprowadź **Hub name**. Musi to być unikalna nazwa.
    - Wybierz swoją subskrypcję Azure (**Subscription**).
    - Wybierz **Resource group**, której chcesz użyć (w razie potrzeby utwórz nową).
    - Wybierz **Location**, której chcesz użyć.
    - Wybierz **Connect Azure AI Services**, którego chcesz użyć (w razie potrzeby utwórz nowe).
    - W sekcji **Connect Azure AI Search** wybierz **Skip connecting**.
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.pl.png)

1. Wybierz **Next**.

#### Utwórz projekt Azure AI Foundry

1. W utworzonym Hubie wybierz **All projects** z zakładki po lewej stronie.

1. W menu nawigacyjnym wybierz **+ New project**.

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.pl.png)

1. Wprowadź **Project name**. Musi to być unikalna wartość.

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.pl.png)

1. Wybierz **Create a project**.

#### Dodaj niestandardowe połączenie dla dostosowanego modelu Phi-3 / Phi-3.5

Aby zintegrować swój niestandardowy model Phi-3 / Phi-3.5 z Prompt flow, musisz zapisać punkt końcowy modelu oraz klucz w niestandardowym połączeniu. To ustawienie zapewnia dostęp do Twojego niestandardowego modelu Phi-3 / Phi-3.5 w Prompt flow.

#### Ustaw klucz api i uri punktu końcowego dostosowanego modelu Phi-3 / Phi-3.5

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Przejdź do utworzonego przez siebie obszaru roboczego Azure Machine Learning.

1. Wybierz **Endpoints** z zakładki po lewej stronie.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.pl.png)

1. Wybierz utworzony punkt końcowy.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.pl.png)

1. W menu nawigacyjnym wybierz **Consume**.

1. Skopiuj swój **REST endpoint** oraz **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.pl.png)

#### Dodaj niestandardowe połączenie

1. Odwiedź [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Przejdź do utworzonego przez siebie projektu Azure AI Foundry.

1. W utworzonym projekcie wybierz **Settings** z zakładki po lewej stronie.

1. Wybierz **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.pl.png)

1. W menu nawigacyjnym wybierz **Custom keys**.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.pl.png)

1. Wykonaj następujące kroki:

    - Wybierz **+ Add key value pairs**.
    - W polu nazwy klucza wpisz **endpoint** i wklej skopiowany z Azure ML Studio punkt końcowy w pole wartości.
    - Ponownie wybierz **+ Add key value pairs**.
    - W polu nazwy klucza wpisz **key** i wklej skopiowany z Azure ML Studio klucz w pole wartości.
    - Po dodaniu kluczy zaznacz opcję **is secret**, aby zapobiec ujawnieniu klucza.

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.pl.png)

1. Wybierz **Add connection**.

#### Utwórz Prompt flow

Dodałeś niestandardowe połączenie w Azure AI Foundry. Teraz utwórz Prompt flow, wykonując poniższe kroki. Następnie połącz ten Prompt flow z niestandardowym połączeniem, aby korzystać z dostosowanego modelu w Prompt flow.

1. Przejdź do utworzonego przez siebie projektu Azure AI Foundry.

1. Wybierz **Prompt flow** z zakładki po lewej stronie.

1. W menu nawigacyjnym wybierz **+ Create**.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.pl.png)

1. W menu nawigacyjnym wybierz **Chat flow**.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.pl.png)

1. Wprowadź **Folder name**, którego chcesz użyć.

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.pl.png)

1. Wybierz **Create**.

#### Skonfiguruj Prompt flow do rozmowy z niestandardowym modelem Phi-3 / Phi-3.5

Musisz zintegrować dostosowany model Phi-3 / Phi-3.5 z Prompt flow. Jednak dostarczony domyślnie Prompt flow nie jest do tego przystosowany. Dlatego musisz przeprojektować Prompt flow, aby umożliwić integrację niestandardowego modelu.

1. W Prompt flow wykonaj następujące czynności, aby przebudować istniejący przepływ:

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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.pl.png)

1. Dodaj poniższy kod do *integrate_with_promptflow.py*, aby korzystać z niestandardowego modelu Phi-3 / Phi-3.5 w Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
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

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.pl.png)

> [!NOTE]
> Aby uzyskać bardziej szczegółowe informacje na temat korzystania z Prompt flow w Azure AI Foundry, możesz odwiedzić [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Włącz **Chat input** oraz **Chat output**, aby umożliwić rozmowę z modelem.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.pl.png)

1. Teraz możesz rozpocząć rozmowę z niestandardowym modelem Phi-3 / Phi-3.5. W kolejnym ćwiczeniu dowiesz się, jak uruchomić Prompt flow i używać go do rozmowy z dostosowanym modelem Phi-3 / Phi-3.5.

> [!NOTE]
>
> Przebudowany przepływ powinien wyglądać jak na poniższym obrazku:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.pl.png)
>

#### Uruchom Prompt flow

1. Wybierz **Start compute sessions**, aby uruchomić Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.pl.png)

1. Wybierz **Validate and parse input**, aby odświeżyć parametry.

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.pl.png)

1. Wybierz **Value** pola **connection**, aby wskazać niestandardowe połączenie, które utworzyłeś. Na przykład *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.pl.png)

#### Rozmawiaj z niestandardowym modelem Phi-3 / Phi-3.5

1. Wybierz **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.pl.png)

1. Oto przykład wyników: teraz możesz rozmawiać z niestandardowym modelem Phi-3 / Phi-3.5. Zaleca się zadawanie pytań opartych na danych użytych do dostrojenia.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.pl.png)

### Wdróż Azure OpenAI, aby ocenić model Phi-3 / Phi-3.5

Aby ocenić model Phi-3 / Phi-3.5 w Azure AI Foundry, musisz wdrożyć model Azure OpenAI. Ten model posłuży do oceny wydajności modelu Phi-3 / Phi-3.5.

#### Wdróż Azure OpenAI

1. Zaloguj się do [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Przejdź do utworzonego przez siebie projektu Azure AI Foundry.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.pl.png)

1. W utworzonym projekcie wybierz **Deployments** z zakładki po lewej stronie.

1. W menu nawigacyjnym wybierz **+ Deploy model**.

1. Wybierz **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.pl.png)

1. Wybierz model Azure OpenAI, którego chcesz użyć, np. **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.pl.png)

1. Wybierz **Confirm**.

### Oceń dostosowany model Phi-3 / Phi-3.5 za pomocą oceny Prompt flow w Azure AI Foundry

### Rozpocznij nową ocenę

1. Odwiedź [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Przejdź do utworzonego przez siebie projektu Azure AI Foundry.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.pl.png)

1. W utworzonym projekcie wybierz **Evaluation** z zakładki po lewej stronie.

1. W menu nawigacyjnym wybierz **+ New evaluation**.
![Select evaluation.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.pl.png)

1. Wybierz ocenę **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.pl.png)

1. Wykonaj następujące zadania:

    - Wprowadź nazwę oceny. Musi to być unikalna wartość.
    - Wybierz typ zadania **Question and answer without context**. Ponieważ zestaw danych **UlTRACHAT_200k** użyty w tym samouczku nie zawiera kontekstu.
    - Wybierz prompt flow, który chcesz ocenić.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.pl.png)

1. Wybierz **Next**.

1. Wykonaj następujące zadania:

    - Wybierz **Add your dataset**, aby przesłać zestaw danych. Na przykład możesz przesłać plik testowego zestawu danych, taki jak *test_data.json1*, który jest dołączony podczas pobierania zestawu danych **ULTRACHAT_200k**.
    - Wybierz odpowiednią **Dataset column**, która odpowiada Twojemu zestawowi danych. Na przykład, jeśli używasz zestawu danych **ULTRACHAT_200k**, wybierz **${data.prompt}** jako kolumnę zestawu danych.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.pl.png)

1. Wybierz **Next**.

1. Wykonaj następujące zadania, aby skonfigurować metryki wydajności i jakości:

    - Wybierz metryki wydajności i jakości, które chcesz użyć.
    - Wybierz model Azure OpenAI, który utworzyłeś do oceny. Na przykład wybierz **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.pl.png)

1. Wykonaj następujące zadania, aby skonfigurować metryki ryzyka i bezpieczeństwa:

    - Wybierz metryki ryzyka i bezpieczeństwa, które chcesz użyć.
    - Wybierz próg do obliczania wskaźnika defektów, który chcesz zastosować. Na przykład wybierz **Medium**.
    - Dla **question** wybierz **Data source** na **{$data.prompt}**.
    - Dla **answer** wybierz **Data source** na **{$run.outputs.answer}**.
    - Dla **ground_truth** wybierz **Data source** na **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.pl.png)

1. Wybierz **Next**.

1. Wybierz **Submit**, aby rozpocząć ocenę.

1. Ocena potrwa chwilę. Możesz śledzić postęp na karcie **Evaluation**.

### Przegląd wyników oceny

> [!NOTE]
> Wyniki przedstawione poniżej mają na celu zilustrowanie procesu oceny. W tym samouczku użyliśmy modelu dostrojonego na stosunkowo małym zestawie danych, co może prowadzić do nieoptymalnych rezultatów. Rzeczywiste wyniki mogą się znacznie różnić w zależności od wielkości, jakości i różnorodności użytego zestawu danych oraz konkretnej konfiguracji modelu.

Po zakończeniu oceny możesz przejrzeć wyniki zarówno dla metryk wydajności, jak i bezpieczeństwa.

1. Metryki wydajności i jakości:

    - oceniają skuteczność modelu w generowaniu spójnych, płynnych i trafnych odpowiedzi.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.pl.png)

1. Metryki ryzyka i bezpieczeństwa:

    - Zapewnij, że wyniki modelu są bezpieczne i zgodne z zasadami Responsible AI, unikając treści szkodliwych lub obraźliwych.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.pl.png)

1. Możesz przewinąć w dół, aby zobaczyć **Detailed metrics result**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.pl.png)

1. Ocena własnego modelu Phi-3 / Phi-3.5 pod kątem metryk wydajności i bezpieczeństwa pozwala potwierdzić, że model jest nie tylko skuteczny, ale także przestrzega zasad odpowiedzialnej sztucznej inteligencji, dzięki czemu jest gotowy do wdrożenia w rzeczywistych zastosowaniach.

## Gratulacje!

### Ukończyłeś ten samouczek

Pomyślnie oceniłeś dostrojony model Phi-3 zintegrowany z Prompt flow w Azure AI Foundry. To ważny krok, aby upewnić się, że Twoje modele AI nie tylko działają efektywnie, ale także przestrzegają zasad Responsible AI Microsoftu, pomagając Ci budować wiarygodne i niezawodne aplikacje AI.

![Architecture.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.pl.png)

## Sprzątanie zasobów Azure

Posprzątaj zasoby Azure, aby uniknąć dodatkowych opłat na Twoim koncie. Przejdź do portalu Azure i usuń następujące zasoby:

- Zasób Azure Machine learning.
- Punkt końcowy modelu Azure Machine learning.
- Zasób projektu Azure AI Foundry.
- Zasób Prompt flow w Azure AI Foundry.

### Kolejne kroki

#### Dokumentacja

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Materiały szkoleniowe

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Źródła

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najdokładniejsze, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.