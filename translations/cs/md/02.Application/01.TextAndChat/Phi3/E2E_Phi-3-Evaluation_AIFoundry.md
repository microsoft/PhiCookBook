<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:52:53+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "cs"
}
-->
# Vyhodnocení doladěného modelu Phi-3 / Phi-3.5 v Azure AI Foundry se zaměřením na principy odpovědné AI od Microsoftu

Tento end-to-end (E2E) příklad vychází z průvodce "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community.

## Přehled

### Jak můžete vyhodnotit bezpečnost a výkon doladěného modelu Phi-3 / Phi-3.5 v Azure AI Foundry?

Doladění modelu může někdy vést k nechtěným nebo nežádoucím odpovědím. Abychom zajistili, že model zůstane bezpečný a efektivní, je důležité vyhodnotit jeho potenciál generovat škodlivý obsah a schopnost produkovat přesné, relevantní a koherentní odpovědi. V tomto tutoriálu se naučíte, jak vyhodnotit bezpečnost a výkon doladěného modelu Phi-3 / Phi-3.5 integrovaného s Prompt flow v Azure AI Foundry.

Zde je proces vyhodnocení v Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/cs/architecture.10bec55250f5d6a4.png)

*Zdroj obrázku: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Pro podrobnější informace a další zdroje o Phi-3 / Phi-3.5 navštivte prosím [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Požadavky

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Doladěný model Phi-3 / Phi-3.5

### Obsah

1. [**Scénář 1: Úvod do vyhodnocení Prompt flow v Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Úvod do vyhodnocení bezpečnosti](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Úvod do vyhodnocení výkonu](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scénář 2: Vyhodnocení modelu Phi-3 / Phi-3.5 v Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Než začnete](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nasazení Azure OpenAI pro vyhodnocení modelu Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Vyhodnocení doladěného modelu Phi-3 / Phi-3.5 pomocí Prompt flow v Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Gratulujeme!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scénář 1: Úvod do vyhodnocení Prompt flow v Azure AI Foundry**

### Úvod do vyhodnocení bezpečnosti

Aby byl váš AI model etický a bezpečný, je zásadní jej vyhodnotit podle principů odpovědné AI od Microsoftu. V Azure AI Foundry umožňují bezpečnostní vyhodnocení posoudit zranitelnost modelu vůči jailbreak útokům a jeho potenciál generovat škodlivý obsah, což přímo odpovídá těmto principům.

![Safaty evaluation.](../../../../../../translated_images/cs/safety-evaluation.083586ec88dfa950.png)

*Zdroj obrázku: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principy odpovědné AI od Microsoftu

Než začnete s technickými kroky, je důležité pochopit principy odpovědné AI od Microsoftu, což je etický rámec navržený k vedení odpovědného vývoje, nasazení a provozu AI systémů. Tyto principy usměrňují odpovědný design, vývoj a nasazení AI systémů tak, aby technologie AI byly spravedlivé, transparentní a inkluzivní. Jsou základem pro vyhodnocení bezpečnosti AI modelů.

Principy odpovědné AI od Microsoftu zahrnují:

- **Spravedlnost a inkluzivita**: AI systémy by měly zacházet se všemi spravedlivě a vyvarovat se rozdílného ovlivňování podobných skupin lidí. Například když AI systémy poskytují doporučení ohledně lékařské péče, žádostí o půjčku nebo zaměstnání, měly by všem s podobnými symptomy, finanční situací nebo kvalifikací doporučit stejné možnosti.

- **Spolehlivost a bezpečnost**: Pro vybudování důvěry je klíčové, aby AI systémy fungovaly spolehlivě, bezpečně a konzistentně. Tyto systémy by měly fungovat tak, jak byly původně navrženy, bezpečně reagovat na nepředvídané situace a odolávat škodlivým manipulacím. Jejich chování a rozsah podmínek, které zvládnou, odráží situace, které vývojáři předpokládali během návrhu a testování.

- **Transparentnost**: Když AI systémy pomáhají rozhodovat o záležitostech s velkým dopadem na životy lidí, je důležité, aby lidé rozuměli, jak byla rozhodnutí učiněna. Například banka může použít AI systém k rozhodnutí, zda je osoba bonitní. Firma může použít AI systém k výběru nejvhodnějších kandidátů na zaměstnání.

- **Soukromí a bezpečnost**: S rostoucím rozšířením AI je ochrana soukromí a zabezpečení osobních a firemních informací stále důležitější a složitější. U AI je třeba věnovat zvláštní pozornost ochraně soukromí a bezpečnosti dat, protože přístup k datům je nezbytný pro přesné a informované předpovědi a rozhodnutí AI systémů o lidech.

- **Zodpovědnost**: Lidé, kteří navrhují a nasazují AI systémy, musí být zodpovědní za jejich fungování. Organizace by měly využívat průmyslové standardy k vytvoření norem zodpovědnosti. Tyto normy zajistí, že AI systémy nebudou konečnou autoritou v žádném rozhodnutí, které ovlivňuje životy lidí. Také zajistí, že lidé budou mít smysluplnou kontrolu nad vysoce autonomními AI systémy.

![Fill hub.](../../../../../../translated_images/cs/responsibleai2.c07ef430113fad8c.png)

*Zdroj obrázku: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Pro více informací o principech odpovědné AI od Microsoftu navštivte [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metriky bezpečnosti

V tomto tutoriálu budete vyhodnocovat bezpečnost doladěného modelu Phi-3 pomocí bezpečnostních metrik Azure AI Foundry. Tyto metriky pomáhají posoudit potenciál modelu generovat škodlivý obsah a jeho zranitelnost vůči jailbreak útokům. Bezpečnostní metriky zahrnují:

- **Obsah související se sebepoškozováním**: Posuzuje, zda model má tendenci generovat obsah týkající se sebepoškozování.
- **Nenávistný a nespravedlivý obsah**: Posuzuje, zda model má tendenci generovat nenávistný nebo nespravedlivý obsah.
- **Násilný obsah**: Posuzuje, zda model má tendenci generovat násilný obsah.
- **Sexuální obsah**: Posuzuje, zda model má tendenci generovat nevhodný sexuální obsah.

Vyhodnocení těchto aspektů zajišťuje, že AI model nevytváří škodlivý nebo urážlivý obsah, což odpovídá společenským hodnotám a regulačním normám.

![Evaluate based on safety.](../../../../../../translated_images/cs/evaluate-based-on-safety.c5df819f5b0bfc07.png)

### Úvod do vyhodnocení výkonu

Aby váš AI model fungoval podle očekávání, je důležité vyhodnotit jeho výkon pomocí metrik výkonu. V Azure AI Foundry umožňují vyhodnocení výkonu posoudit efektivitu modelu při generování přesných, relevantních a koherentních odpovědí.

![Safaty evaluation.](../../../../../../translated_images/cs/performance-evaluation.48b3e7e01a098740.png)

*Zdroj obrázku: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metriky výkonu

V tomto tutoriálu budete vyhodnocovat výkon doladěného modelu Phi-3 / Phi-3.5 pomocí metrik výkonu Azure AI Foundry. Tyto metriky pomáhají posoudit efektivitu modelu při generování přesných, relevantních a koherentních odpovědí. Metriky výkonu zahrnují:

- **Zakotvenost (Groundedness)**: Posuzuje, jak dobře generované odpovědi odpovídají informacím ze vstupního zdroje.
- **Relevance**: Posuzuje, jak relevantní jsou generované odpovědi k položeným otázkám.
- **Koherence**: Posuzuje, jak plynule generovaný text plyne, zda čtení působí přirozeně a zda připomíná lidský jazyk.
- **Plynulost (Fluency)**: Posuzuje jazykovou úroveň generovaného textu.
- **Podobnost s GPT (GPT Similarity)**: Porovnává generovanou odpověď s referenční pravdou z hlediska podobnosti.
- **F1 skóre**: Vypočítává poměr sdílených slov mezi generovanou odpovědí a zdrojovými daty.

Tyto metriky vám pomohou vyhodnotit efektivitu modelu při generování přesných, relevantních a koherentních odpovědí.

![Evaluate based on performance.](../../../../../../translated_images/cs/evaluate-based-on-performance.3e801c647c7554e8.png)

## **Scénář 2: Vyhodnocení modelu Phi-3 / Phi-3.5 v Azure AI Foundry**

### Než začnete

Tento tutoriál navazuje na předchozí blogové příspěvky, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" a "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." V těchto příspěvcích jsme prošli proces doladění modelu Phi-3 / Phi-3.5 v Azure AI Foundry a jeho integraci s Prompt flow.

V tomto tutoriálu nasadíte model Azure OpenAI jako evaluátor v Azure AI Foundry a použijete jej k vyhodnocení vašeho doladěného modelu Phi-3 / Phi-3.5.

Než začnete s tímto tutoriálem, ujistěte se, že máte splněné následující požadavky, jak bylo popsáno v předchozích tutoriálech:

1. Připravenou datovou sadu pro vyhodnocení doladěného modelu Phi-3 / Phi-3.5.
1. Model Phi-3 / Phi-3.5, který byl doladěn a nasazen do Azure Machine Learning.
1. Prompt flow integrovaný s vaším doladěným modelem Phi-3 / Phi-3.5 v Azure AI Foundry.

> [!NOTE]
> Jako datovou sadu pro vyhodnocení doladěného modelu Phi-3 / Phi-3.5 použijete soubor *test_data.jsonl*, který se nachází ve složce data z datasetu **ULTRACHAT_200k** staženého v předchozích blogových příspěvcích.

#### Integrace vlastního modelu Phi-3 / Phi-3.5 s Prompt flow v Azure AI Foundry (přístup založený na kódu)
> [!NOTE]
> Pokud jste postupovali podle přístupu s nízkým kódem popsaného v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", můžete tento úkol přeskočit a pokračovat k dalšímu.
> Pokud jste však použili přístup založený na kódu popsaný v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" pro doladění a nasazení vašeho modelu Phi-3 / Phi-3.5, proces propojení modelu s Prompt flow je mírně odlišný. Tento proces se naučíte v tomto cvičení.
Pro pokračování je potřeba integrovat váš doladěný model Phi-3 / Phi-3.5 do Prompt flow v Azure AI Foundry.

#### Vytvoření Azure AI Foundry Hubu

Než vytvoříte projekt, musíte nejprve vytvořit Hub. Hub funguje jako Resource Group, která vám umožní organizovat a spravovat více projektů v rámci Azure AI Foundry.

1. Přihlaste se do [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. V levém panelu vyberte **All hubs**.

1. V navigačním menu vyberte **+ New hub**.

    ![Create hub.](../../../../../../translated_images/cs/create-hub.5be78fb1e21ffbf1.png)

1. Proveďte následující kroky:

    - Zadejte **Hub name**. Musí být jedinečný.
    - Vyberte vaši Azure **Subscription**.
    - Vyberte **Resource group**, kterou chcete použít (v případě potřeby vytvořte novou).
    - Vyberte **Location**, kterou chcete použít.
    - Vyberte **Connect Azure AI Services**, které chcete použít (v případě potřeby vytvořte nové).
    - U **Connect Azure AI Search** vyberte **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/cs/fill-hub.baaa108495c71e34.png)

1. Klikněte na **Next**.

#### Vytvoření Azure AI Foundry projektu

1. V Hubu, který jste vytvořili, vyberte v levém panelu **All projects**.

1. V navigačním menu vyberte **+ New project**.

    ![Select new project.](../../../../../../translated_images/cs/select-new-project.cd31c0404088d7a3.png)

1. Zadejte **Project name**. Musí být jedinečný.

    ![Create project.](../../../../../../translated_images/cs/create-project.ca3b71298b90e420.png)

1. Klikněte na **Create a project**.

#### Přidání vlastního připojení pro doladěný model Phi-3 / Phi-3.5

Pro integraci vašeho vlastního modelu Phi-3 / Phi-3.5 do Prompt flow je potřeba uložit endpoint a klíč modelu do vlastního připojení. Toto nastavení zajistí přístup k vašemu doladěnému modelu v Prompt flow.

#### Nastavení api klíče a endpoint URI doladěného modelu Phi-3 / Phi-3.5

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Přejděte do Azure Machine learning workspace, který jste vytvořili.

1. V levém panelu vyberte **Endpoints**.

    ![Select endpoints.](../../../../../../translated_images/cs/select-endpoints.ee7387ecd68bd18d.png)

1. Vyberte endpoint, který jste vytvořili.

    ![Select endpoints.](../../../../../../translated_images/cs/select-endpoint-created.9f63af5e4cf98b2e.png)

1. V navigačním menu vyberte **Consume**.

1. Zkopírujte váš **REST endpoint** a **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/cs/copy-endpoint-key.0650c3786bd646ab.png)

#### Přidání vlastního připojení

1. Navštivte [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Přejděte do Azure AI Foundry projektu, který jste vytvořili.

1. V projektu vyberte v levém panelu **Settings**.

1. Klikněte na **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/cs/select-new-connection.fa0f35743758a74b.png)

1. V navigačním menu vyberte **Custom keys**.

    ![Select custom keys.](../../../../../../translated_images/cs/select-custom-keys.5a3c6b25580a9b67.png)

1. Proveďte následující kroky:

    - Klikněte na **+ Add key value pairs**.
    - Do pole pro název klíče zadejte **endpoint** a vložte endpoint z Azure ML Studia do pole hodnoty.
    - Znovu klikněte na **+ Add key value pairs**.
    - Do pole pro název klíče zadejte **key** a vložte klíč z Azure ML Studia do pole hodnoty.
    - Po přidání klíčů zaškrtněte **is secret**, aby klíč nebyl veřejně viditelný.

    ![Add connection.](../../../../../../translated_images/cs/add-connection.ac7f5faf8b10b0df.png)

1. Klikněte na **Add connection**.

#### Vytvoření Prompt flow

Přidali jste vlastní připojení v Azure AI Foundry. Nyní vytvoříme Prompt flow podle následujících kroků. Poté toto Prompt flow připojíte k vlastnímu připojení, abyste mohli používat doladěný model v rámci Prompt flow.

1. Přejděte do Azure AI Foundry projektu, který jste vytvořili.

1. V levém panelu vyberte **Prompt flow**.

1. V navigačním menu klikněte na **+ Create**.

    ![Select Promptflow.](../../../../../../translated_images/cs/select-promptflow.18ff2e61ab9173eb.png)

1. V navigačním menu vyberte **Chat flow**.

    ![Select chat flow.](../../../../../../translated_images/cs/select-flow-type.28375125ec9996d3.png)

1. Zadejte **Folder name**, který chcete použít.

    ![Select chat flow.](../../../../../../translated_images/cs/enter-name.02ddf8fb840ad430.png)

1. Klikněte na **Create**.

#### Nastavení Prompt flow pro chat s vaším vlastním modelem Phi-3 / Phi-3.5

Je potřeba integrovat doladěný model Phi-3 / Phi-3.5 do Prompt flow. Existující Prompt flow však není pro tento účel navržen, proto je nutné Prompt flow přepracovat, aby bylo možné integrovat vlastní model.

1. V Prompt flow proveďte následující kroky pro přestavbu stávajícího flow:

    - Vyberte **Raw file mode**.
    - Odstraňte veškerý existující kód v souboru *flow.dag.yml*.
    - Přidejte následující kód do *flow.dag.yml*.

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

    - Klikněte na **Save**.

    ![Select raw file mode.](../../../../../../translated_images/cs/select-raw-file-mode.06c1eca581ce4f53.png)

1. Přidejte následující kód do *integrate_with_promptflow.py* pro použití vlastního modelu Phi-3 / Phi-3.5 v Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/cs/paste-promptflow-code.cd6d95b101c0ec28.png)

> [!NOTE]
> Pro podrobnější informace o používání Prompt flow v Azure AI Foundry můžete navštívit [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Chat input**, **Chat output** pro povolení chatu s vaším modelem.

    ![Select Input Output.](../../../../../../translated_images/cs/select-input-output.c187fc58f25fbfc3.png)

1. Nyní jste připraveni chatovat s vaším vlastním modelem Phi-3 / Phi-3.5. V dalším cvičení se naučíte, jak spustit Prompt flow a používat ho k chatování s vaším doladěným modelem Phi-3 / Phi-3.5.

> [!NOTE]
>
> Přestavěný flow by měl vypadat jako na obrázku níže:
>
> ![Flow example](../../../../../../translated_images/cs/graph-example.82fd1bcdd3fc545b.png)
>

#### Spuštění Prompt flow

1. Klikněte na **Start compute sessions** pro spuštění Prompt flow.

    ![Start compute session.](../../../../../../translated_images/cs/start-compute-session.9acd8cbbd2c43df1.png)

1. Klikněte na **Validate and parse input** pro obnovení parametrů.

    ![Validate input.](../../../../../../translated_images/cs/validate-input.c1adb9543c6495be.png)

1. Vyberte **Value** u **connection** na vámi vytvořené vlastní připojení, například *connection*.

    ![Connection.](../../../../../../translated_images/cs/select-connection.1f2b59222bcaafef.png)

#### Chatování s vaším vlastním modelem Phi-3 / Phi-3.5

1. Klikněte na **Chat**.

    ![Select chat.](../../../../../../translated_images/cs/select-chat.0406bd9687d0c49d.png)

1. Zde je příklad výsledků: nyní můžete chatovat s vaším vlastním modelem Phi-3 / Phi-3.5. Doporučuje se klást otázky založené na datech použitých pro doladění.

    ![Chat with prompt flow.](../../../../../../translated_images/cs/chat-with-promptflow.1cf8cea112359ada.png)

### Nasazení Azure OpenAI pro vyhodnocení modelu Phi-3 / Phi-3.5

Pro vyhodnocení modelu Phi-3 / Phi-3.5 v Azure AI Foundry je potřeba nasadit model Azure OpenAI. Tento model bude použit k hodnocení výkonu modelu Phi-3 / Phi-3.5.

#### Nasazení Azure OpenAI

1. Přihlaste se do [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Přejděte do Azure AI Foundry projektu, který jste vytvořili.

    ![Select Project.](../../../../../../translated_images/cs/select-project-created.5221e0e403e2c9d6.png)

1. V projektu vyberte v levém panelu **Deployments**.

1. V navigačním menu klikněte na **+ Deploy model**.

1. Vyberte **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/cs/deploy-openai-model.95d812346b25834b.png)

1. Vyberte Azure OpenAI model, který chcete použít, například **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/cs/select-openai-model.959496d7e311546d.png)

1. Klikněte na **Confirm**.

### Vyhodnocení doladěného modelu Phi-3 / Phi-3.5 pomocí Prompt flow evaluace v Azure AI Foundry

### Zahájení nového vyhodnocení

1. Navštivte [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Přejděte do Azure AI Foundry projektu, který jste vytvořili.

    ![Select Project.](../../../../../../translated_images/cs/select-project-created.5221e0e403e2c9d6.png)

1. V projektu vyberte v levém panelu **Evaluation**.

1. V navigačním menu klikněte na **+ New evaluation**.

    ![Select evaluation.](../../../../../../translated_images/cs/select-evaluation.2846ad7aaaca7f4f.png)

1. Vyberte **Prompt flow** evaluaci.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/cs/promptflow-evaluation.cb9758cc19b4760f.png)

1. Proveďte následující kroky:

    - Zadejte název vyhodnocení. Musí být jedinečný.
    - Vyberte typ úlohy **Question and answer without context**, protože dataset **ULTRACHAT_200k** použitý v tomto tutoriálu neobsahuje kontext.
    - Vyberte prompt flow, které chcete vyhodnotit.

    ![Prompt flow evaluation.](../../../../../../translated_images/cs/evaluation-setting1.4aa08259ff7a536e.png)

1. Klikněte na **Next**.

1. Proveďte následující kroky:

    - Klikněte na **Add your dataset** pro nahrání datasetu. Například můžete nahrát testovací datasetový soubor, jako je *test_data.json1*, který je součástí staženého datasetu **ULTRACHAT_200k**.
    - Vyberte odpovídající **Dataset column**, která odpovídá vašemu datasetu. Například pokud používáte dataset **ULTRACHAT_200k**, vyberte **${data.prompt}** jako datasetovou kolonku.

    ![Prompt flow evaluation.](../../../../../../translated_images/cs/evaluation-setting2.07036831ba58d64e.png)

1. Klikněte na **Next**.

1. Proveďte následující kroky pro nastavení metrik výkonu a kvality:

    - Vyberte metriky výkonu a kvality, které chcete použít.
    - Vyberte Azure OpenAI model, který jste vytvořili pro vyhodnocení, například **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/cs/evaluation-setting3-1.d1ae69e3bf80914e.png)

1. Proveďte následující kroky pro nastavení metrik rizika a bezpečnosti:

    - Vyberte metriky rizika a bezpečnosti, které chcete použít.
    - Vyberte práh pro výpočet míry chyb, například **Medium**.
    - Pro **question** vyberte **Data source** na **{$data.prompt}**.
    - Pro **answer** vyberte **Data source** na **{$run.outputs.answer}**.
    - Pro **ground_truth** vyberte **Data source** na **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/cs/evaluation-setting3-2.d53bd075c60a45a2.png)

1. Klikněte na **Next**.

1. Klikněte na **Submit** pro spuštění vyhodnocení.

1. Vyhodnocení bude chvíli trvat. Průběh můžete sledovat na záložce **Evaluation**.

### Prohlédnutí výsledků vyhodnocení
> [!NOTE]
> Níže uvedené výsledky slouží k ilustraci hodnotícího procesu. V tomto tutoriálu jsme použili model doladěný na relativně malém datasetu, což může vést k méně optimálním výsledkům. Skutečné výsledky se mohou výrazně lišit v závislosti na velikosti, kvalitě a rozmanitosti použitého datasetu, stejně jako na konkrétním nastavení modelu.
Po dokončení hodnocení můžete zkontrolovat výsledky jak pro metriky výkonu, tak bezpečnosti.

1. Metriky výkonu a kvality:

    - zhodnoťte efektivitu modelu při generování koherentních, plynulých a relevantních odpovědí.

    ![Evaluation result.](../../../../../../translated_images/cs/evaluation-result-gpu.85f48b42dfb74254.png)

1. Metriky rizika a bezpečnosti:

    - zajistěte, aby výstupy modelu byly bezpečné a odpovídaly zásadám Responsible AI, vyhýbající se škodlivému nebo urážlivému obsahu.

    ![Evaluation result.](../../../../../../translated_images/cs/evaluation-result-gpu-2.1b74e336118f4fd0.png)

1. Můžete posunout stránku dolů a zobrazit **Podrobné výsledky metrik**.

    ![Evaluation result.](../../../../../../translated_images/cs/detailed-metrics-result.afa2f5c39a4f5f17.png)

1. Hodnocením vašeho vlastního modelu Phi-3 / Phi-3.5 podle metrik výkonu i bezpečnosti můžete potvrdit, že model není jen efektivní, ale také dodržuje zásady odpovědné AI, což ho připravuje na nasazení v reálném světě.

## Gratulujeme!

### Dokončili jste tento tutoriál

Úspěšně jste vyhodnotili doladěný model Phi-3 integrovaný s Prompt flow v Azure AI Foundry. Tento krok je důležitý pro zajištění, že vaše AI modely nejen dobře fungují, ale také dodržují zásady Responsible AI od Microsoftu, což vám pomůže vytvářet důvěryhodné a spolehlivé AI aplikace.

![Architecture.](../../../../../../translated_images/cs/architecture.10bec55250f5d6a4.png)

## Úklid Azure zdrojů

Uklidte své Azure zdroje, abyste předešli dalším poplatkům na vašem účtu. Přejděte do Azure portálu a odstraňte následující zdroje:

- Azure Machine learning resource.
- Azure Machine learning model endpoint.
- Azure AI Foundry Project resource.
- Azure AI Foundry Prompt flow resource.

### Další kroky

#### Dokumentace

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Výukový obsah

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.