# Zhodnocení doladěného modelu Phi-3 / Phi-3.5 v Microsoft Foundry se zaměřením na zodpovědné principy AI společnosti Microsoft

Tento ukázkový příklad (E2E) je založen na průvodci "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community.

## Přehled

### Jak můžete zhodnotit bezpečnost a výkon doladěného modelu Phi-3 / Phi-3.5 v Microsoft Foundry?

Doladění modelu může někdy vést k neúmyslným nebo nežádoucím odpovědím. Aby bylo zajištěno, že model zůstává bezpečný a efektivní, je důležité zhodnotit potenciál modelu generovat škodlivý obsah a jeho schopnost produkovat přesné, relevantní a koherentní odpovědi. V tomto tutoriálu se naučíte, jak zhodnotit bezpečnost a výkon doladěného modelu Phi-3 / Phi-3.5 integrovaného s Prompt flow v Microsoft Foundry.

Zde je proces hodnocení Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/cs/architecture.10bec55250f5d6a4.webp)

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

1. [**Scénář 1: Úvod do hodnocení Prompt flow v Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Úvod do hodnocení bezpečnosti](#úvod-do-hodnocení-bezpečnosti)
    - [Úvod do hodnocení výkonu](#úvod-do-hodnocení-výkonu)

1. [**Scénář 2: Hodnocení modelu Phi-3 / Phi-3.5 v Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Než začnete](#než-začnete)
    - [Nasazení Azure OpenAI pro hodnocení modelu Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Hodnocení doladěného modelu Phi-3 / Phi-3.5 pomocí hodnocení Prompt flow v Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Gratulujeme!](#gratulujeme)

## **Scénář 1: Úvod do hodnocení Prompt flow v Microsoft Foundry**

### Úvod do hodnocení bezpečnosti

Aby byl váš AI model etický a bezpečný, je nezbytné ho hodnotit podle zodpovědných principů AI společnosti Microsoft. V Microsoft Foundry umožňují hodnocení bezpečnosti posoudit zranitelnost vašeho modelu vůči jailbreak útokům a jeho potenciál generovat škodlivý obsah, což přímo odpovídá těmto principům.

![Safaty evaluation.](../../../../../../translated_images/cs/safety-evaluation.083586ec88dfa950.webp)

*Zdroj obrázku: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Zodpovědné principy AI společnosti Microsoft

Než začnete technické kroky, je důležité pochopit zodpovědné principy AI společnosti Microsoft, což je etický rámec navržený k vedení zodpovědného vývoje, nasazení a provozu AI systémů. Tyto principy vedou odpovědný návrh, vývoj a nasazení AI systémů, zajišťují, že technologie AI jsou vytvořeny tak, aby byly spravedlivé, transparentní a inkluzivní. Tyto principy jsou základem pro hodnocení bezpečnosti AI modelů.

Principy zodpovědné AI společnosti Microsoft zahrnují:

- **Spravedlnost a inkluzivita**: AI systémy by měly zacházet se všemi spravedlivě a vyvarovat se různých dopadů na podobně situované skupiny lidí. Například když AI systémy poskytují rady ohledně lékařského ošetření, žádostí o půjčku nebo zaměstnání, měly by všem s podobnými symptomy, finančními podmínkami nebo kvalifikacemi doporučovat totéž.

- **Spolehlivost a bezpečnost**: K vybudování důvěry je zásadní, aby AI systémy fungovaly spolehlivě, bezpečně a konzistentně. Tyto systémy by měly fungovat tak, jak byly původně navrženy, bezpečně reagovat na nečekané podmínky a odolávat škodlivým manipulacím. Jejich chování a spektrum situací, které dokážou zvládnout, odráží rozsah situací a okolností, které vývojáři předpokládali během návrhu a testování.

- **Transparentnost**: Když AI systémy pomáhají informovat rozhodnutí, která mají obrovský dopad na životy lidí, je klíčové, aby lidé pochopili, jak byla tato rozhodnutí učiněna. Například banka může používat AI systém k rozhodování, zda je osoba bonitní. Společnost může použít AI systém k určení nejvhodnějších kandidátů pro zaměstnání.

- **Soukromí a bezpečnost**: S postupným rozšířením AI nabývá ochrana soukromí a zabezpečení osobních a firemních informací na důležitosti a komplexnosti. S AI vyžadují soukromí a zabezpečení dat zvláštní pozornost, protože přístup k datům je nezbytný, aby AI systémy mohly vytvářet přesné a informované predikce a rozhodnutí o lidech.

- **Zodpovědnost**: Lidé, kteří navrhují a nasazují AI systémy, musí nést zodpovědnost za to, jak jejich systémy fungují. Organizace by měly vycházet z průmyslových standardů pro rozvoj zodpovědných norem. Tyto normy mohou zajistit, že AI systémy nejsou konečnou autoritou při jakémkoli rozhodnutí, které ovlivňuje životy lidí. Zároveň mohou zajistit, že lidé si udrží smysluplnou kontrolu nad jinak vysoce autonomními AI systémy.

![Fill hub.](../../../../../../translated_images/cs/responsibleai2.c07ef430113fad8c.webp)

*Zdroj obrázku: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Pro více informací o zodpovědných principech AI společnosti Microsoft navštivte [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metriky bezpečnosti

V tomto tutoriálu budete hodnotit bezpečnost doladěného modelu Phi-3 pomocí metrik bezpečnosti Microsoft Foundry. Tyto metriky vám pomohou posoudit potenciál modelu generovat škodlivý obsah a jeho zranitelnost vůči jailbreak útokům. Metriky bezpečnosti zahrnují:

- **Obsah související s sebepoškozováním**: Posuzuje, zda má model tendenci produkovat obsah související se sebepoškozováním.
- **Nenávistný a nespravedlivý obsah**: Posuzuje, zda má model tendenci produkovat nenávistný nebo nespravedlivý obsah.
- **Násilný obsah**: Posuzuje, zda má model tendenci produkovat násilný obsah.
- **Sexuální obsah**: Posuzuje, zda má model tendenci produkovat nevhodný sexuální obsah.

Hodnocením těchto aspektů zajistíte, že AI model nebude produkovat škodlivý nebo urážlivý obsah, což odpovídá společenským hodnotám a regulačním normám.

![Evaluate based on safety.](../../../../../../translated_images/cs/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Úvod do hodnocení výkonu

Aby váš AI model fungoval podle očekávání, je důležité hodnotit jeho výkon pomocí metrik výkonu. V Microsoft Foundry umožňuje hodnocení výkonu posoudit efektivitu vašeho modelu při generování přesných, relevantních a koherentních odpovědí.

![Safaty evaluation.](../../../../../../translated_images/cs/performance-evaluation.48b3e7e01a098740.webp)

*Zdroj obrázku: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metriky výkonu

V tomto tutoriálu budete hodnotit výkon doladěného modelu Phi-3 / Phi-3.5 pomocí metrik výkonu Microsoft Foundry. Tyto metriky vám pomohou posoudit efektivitu modelu při generování přesných, relevantních a koherentních odpovědí. Metriky výkonu zahrnují:

- **Založenost na zdroji**: Hodnotí, jak dobře generované odpovědi odpovídají informacím ze vstupního zdroje.
- **Relevance**: Posuzuje přiměřenost generovaných odpovědí vzhledem ke kladeným otázkám.
- **Koherence**: Hodnotí, jak plynule generovaný text plyne, čte se přirozeně a připomíná lidský jazyk.
- **Plynulost**: Hodnotí jazykovou zdatnost generovaného textu.
- **Podobnost s GPT**: Porovnání generované odpovědi s reálnou pravdou z hlediska podobnosti.
- **F1 skóre**: Vypočítává poměr sdílených slov mezi generovanou odpovědí a zdrojovými daty.

Tyto metriky vám pomohou hodnotit efektivitu modelu při generování přesných, relevantních a koherentních odpovědí.

![Evaluate based on performance.](../../../../../../translated_images/cs/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scénář 2: Hodnocení modelu Phi-3 / Phi-3.5 v Microsoft Foundry**

### Než začnete

Tento tutoriál je pokračováním předchozích blogových příspěvků, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" a "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." V těchto příspěvcích jsme prošli proces doladění modelu Phi-3 / Phi-3.5 v Microsoft Foundry a jeho integraci s Prompt flow.

V tomto tutoriálu nasadíte Azure OpenAI model jako evaluátora v Microsoft Foundry a použijete jej k hodnocení vašeho doladěného modelu Phi-3 / Phi-3.5.

Než začnete, ujistěte se, že máte následující předpoklady, jak bylo popsáno v předchozích tutoriálech:

1. Připravený dataset pro hodnocení doladěného modelu Phi-3 / Phi-3.5.
1. Model Phi-3 / Phi-3.5, který byl doladěn a nasazen do Azure Machine Learning.
1. Prompt flow integrovaný s vaším doladěným modelem Phi-3 / Phi-3.5 v Microsoft Foundry.

> [!NOTE]
> Jako dataset pro hodnocení doladěného modelu Phi-3 / Phi-3.5 použijete soubor *test_data.jsonl* umístěný ve složce data z datasetu **ULTRACHAT_200k** staženého v předchozích blogových příspěvcích.

#### Integrace vlastního modelu Phi-3 / Phi-3.5 s Prompt flow v Microsoft Foundry (přístup orientovaný na kód)

> [!NOTE]
> Pokud jste použili přístup nízkokódu, jak je popsáno v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", můžete tuto část přeskočit a pokračovat dále.
> Nicméně pokud jste použili přístup orientovaný na kód, jak je popsáno v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" k doladění a nasazení svého modelu Phi-3 / Phi-3.5, proces připojení vašeho modelu k Prompt flow je mírně odlišný. Tento proces se naučíte v tomto cvičení.

Pro pokračování je třeba integrovat svůj doladěný model Phi-3 / Phi-3.5 do Prompt flow v Microsoft Foundry.

#### Vytvoření Microsoft Foundry Hubu

Než vytvoříte Projekt, je třeba vytvořit Hub. Hub funguje jako skupina zdrojů (Resource Group), která vám umožní organizovat a spravovat více Projektů v rámci Microsoft Foundry.
1. Přihlaste se do [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Vyberte **All hubs** z levé záložky.

1. Vyberte **+ New hub** z navigačního menu.

    ![Create hub.](../../../../../../translated_images/cs/create-hub.5be78fb1e21ffbf1.webp)

1. Proveďte následující úkony:

    - Zadejte **Hub name**. Musí být jedinečná hodnota.
    - Vyberte svůj Azure **Subscription**.
    - Vyberte **Resource group**, kterou chcete použít (v případě potřeby vytvořte novou).
    - Vyberte **Location**, kterou chcete použít.
    - Vyberte **Connect Azure AI Services**, které chcete použít (v případě potřeby vytvořte novou).
    - Vyberte **Connect Azure AI Search** na **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/cs/fill-hub.baaa108495c71e34.webp)

1. Vyberte **Next**.

#### Vytvoření projektu Microsoft Foundry

1. V hubu, který jste vytvořili, vyberte **All projects** z levé záložky.

1. Vyberte **+ New project** z navigačního menu.

    ![Select new project.](../../../../../../translated_images/cs/select-new-project.cd31c0404088d7a3.webp)

1. Zadejte **Project name**. Musí být jedinečná hodnota.

    ![Create project.](../../../../../../translated_images/cs/create-project.ca3b71298b90e420.webp)

1. Vyberte **Create a project**.

#### Přidání vlastního připojení pro jemně vyladěný model Phi-3 / Phi-3.5

Pro integraci vlastního modelu Phi-3 / Phi-3.5 s Prompt flow musíte uložit koncový bod modelu a klíč ve vlastním připojení. Toto nastavení zajistí přístup k vašemu vlastnímu modelu Phi-3 / Phi-3.5 v Prompt flow.

#### Nastavení api klíče a endpoint URI jemně vyladěného modelu Phi-3 / Phi-3.5

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Přejděte do pracovního prostoru Azure Machine learning, který jste vytvořili.

1. Vyberte **Endpoints** z levé záložky.

    ![Select endpoints.](../../../../../../translated_images/cs/select-endpoints.ee7387ecd68bd18d.webp)

1. Vyberte koncový bod, který jste vytvořili.

    ![Select endpoints.](../../../../../../translated_images/cs/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Zvolte **Consume** z navigačního menu.

1. Zkopírujte svůj **REST endpoint** a **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/cs/copy-endpoint-key.0650c3786bd646ab.webp)

#### Přidání vlastního připojení

1. Navštivte [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Přejděte do projektu Microsoft Foundry, který jste vytvořili.

1. Ve vytvořeném projektu vyberte **Settings** z levé záložky.

1. Vyberte **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/cs/select-new-connection.fa0f35743758a74b.webp)

1. Vyberte **Custom keys** z navigačního menu.

    ![Select custom keys.](../../../../../../translated_images/cs/select-custom-keys.5a3c6b25580a9b67.webp)

1. Proveďte následující kroky:

    - Vyberte **+ Add key value pairs**.
    - Pro název klíče zadejte **endpoint** a vložte zkopírovaný endpoint z Azure ML Studio do pole hodnoty.
    - Znovu vyberte **+ Add key value pairs**.
    - Pro název klíče zadejte **key** a vložte klíč zkopírovaný z Azure ML Studio do pole hodnoty.
    - Po přidání klíčů zaškrtněte **is secret**, aby klíč nebyl zpřístupněn.

    ![Add connection.](../../../../../../translated_images/cs/add-connection.ac7f5faf8b10b0df.webp)

1. Vyberte **Add connection**.

#### Vytvoření Prompt flow

Přidali jste vlastní připojení v Microsoft Foundry. Nyní vytvoříme Prompt flow podle následujících kroků. Poté toto Prompt flow spojíte s vlastním připojením, abyste mohli použít jemně vyladěný model v rámci Prompt flow.

1. Přejděte do projektu Microsoft Foundry, který jste vytvořili.

1. Vyberte **Prompt flow** z levé záložky.

1. Vyberte **+ Create** z navigačního menu.

    ![Select Promptflow.](../../../../../../translated_images/cs/select-promptflow.18ff2e61ab9173eb.webp)

1. Vyberte **Chat flow** z navigačního menu.

    ![Select chat flow.](../../../../../../translated_images/cs/select-flow-type.28375125ec9996d3.webp)

1. Zadejte **Folder name** k použití.

    ![Select chat flow.](../../../../../../translated_images/cs/enter-name.02ddf8fb840ad430.webp)

1. Vyberte **Create**.

#### Nastavení Prompt flow pro chat s vlastním modelem Phi-3 / Phi-3.5

Musíte integrovat jemně vyladěný model Phi-3 / Phi-3.5 do Prompt flow. Existující Prompt flow však není navržen pro tento účel. Proto musíte Prompt flow přepracovat tak, aby bylo možné integrovat vlastní model.

1. V Prompt flow proveďte následující kroky k přestavbě existujícího toku:

    - Vyberte **Raw file mode**.
    - Odstraňte všechen existující kód v souboru *flow.dag.yml*.
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

    - Vyberte **Save**.

    ![Select raw file mode.](../../../../../../translated_images/cs/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Přidejte následující kód do *integrate_with_promptflow.py* pro použití vlastního modelu Phi-3 / Phi-3.5 v Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Nastavení protokolování
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

        # "connection" je název Vlastního připojení, "endpoint", "key" jsou klíče ve Vlastním připojení
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
            
            # Protokolovat celou JSON odpověď
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

    ![Paste prompt flow code.](../../../../../../translated_images/cs/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Pro podrobnější informace o použití Prompt flow v Microsoft Foundry můžete navštívit [Prompt flow v Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Chat input**, **Chat output** pro povolení chatu s vaším modelem.

    ![Select Input Output.](../../../../../../translated_images/cs/select-input-output.c187fc58f25fbfc3.webp)

1. Nyní jste připraveni chatovat s vlastním modelem Phi-3 / Phi-3.5. V následujícím cvičení se naučíte, jak spustit Prompt flow a komunikovat s vaším jemně vyladěným modelem Phi-3 / Phi-3.5.

> [!NOTE]
>
> Přepracovaný tok by měl vypadat jako na obrázku níže:
>
> ![Flow example](../../../../../../translated_images/cs/graph-example.82fd1bcdd3fc545b.webp)
>

#### Spuštění Prompt flow

1. Vyberte **Start compute sessions** pro spuštění Prompt flow.

    ![Start compute session.](../../../../../../translated_images/cs/start-compute-session.9acd8cbbd2c43df1.webp)

1. Vyberte **Validate and parse input** pro obnovení parametrů.

    ![Validate input.](../../../../../../translated_images/cs/validate-input.c1adb9543c6495be.webp)

1. Vyberte **Value** u **connection** pro vlastní připojení, které jste vytvořili. Například *connection*.

    ![Connection.](../../../../../../translated_images/cs/select-connection.1f2b59222bcaafef.webp)

#### Chat s vlastním modelem Phi-3 / Phi-3.5

1. Vyberte **Chat**.

    ![Select chat.](../../../../../../translated_images/cs/select-chat.0406bd9687d0c49d.webp)

1. Zde je příklad výsledků: nyní můžete chatovat se svým vlastním modelem Phi-3 / Phi-3.5. Doporučuje se klást otázky založené na datech použitých k jemnému doladění.

    ![Chat with prompt flow.](../../../../../../translated_images/cs/chat-with-promptflow.1cf8cea112359ada.webp)

### Nasazení Azure OpenAI pro hodnocení modelu Phi-3 / Phi-3.5

Pro hodnocení modelu Phi-3 / Phi-3.5 v Microsoft Foundry musíte nasadit model Azure OpenAI. Tento model bude použit pro hodnocení výkonu modelu Phi-3 / Phi-3.5.

#### Nasazení Azure OpenAI

1. Přihlaste se do [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Přejděte do projektu Microsoft Foundry, který jste vytvořili.

    ![Select Project.](../../../../../../translated_images/cs/select-project-created.5221e0e403e2c9d6.webp)

1. Ve vytvořeném projektu vyberte **Deployments** z levé záložky.

1. Vyberte **+ Deploy model** z navigačního menu.

1. Vyberte **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/cs/deploy-openai-model.95d812346b25834b.webp)

1. Vyberte model Azure OpenAI, který chcete použít. Například **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/cs/select-openai-model.959496d7e311546d.webp)

1. Vyberte **Confirm**.

### Hodnocení jemně vyladěného modelu Phi-3 / Phi-3.5 pomocí hodnocení Prompt flow v Microsoft Foundry

### Spuštění nové evaluace

1. Navštivte [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Přejděte do projektu Microsoft Foundry, který jste vytvořili.

    ![Select Project.](../../../../../../translated_images/cs/select-project-created.5221e0e403e2c9d6.webp)

1. Ve vytvořeném projektu vyberte **Evaluation** z levé záložky.

1. Vyberte **+ New evaluation** z navigačního menu.

    ![Select evaluation.](../../../../../../translated_images/cs/select-evaluation.2846ad7aaaca7f4f.webp)

1. Vyberte hodnocení **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/cs/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Proveďte následující kroky:

    - Zadejte název hodnocení. Musí být jedinečná hodnota.
    - Vyberte **Question and answer without context** jako typ úlohy, protože dataset **UlTRACHAT_200k** použitý v tomto tutoriálu neobsahuje kontext.
    - Vyberte Prompt flow, které chcete hodnotit.

    ![Prompt flow evaluation.](../../../../../../translated_images/cs/evaluation-setting1.4aa08259ff7a536e.webp)

1. Vyberte **Next**.

1. Proveďte následující kroky:

    - Vyberte **Add your dataset** pro nahrání datasetu. Například můžete nahrát testovací datasetový soubor, jako *test_data.json1*, který je součástí staženého datasetu **ULTRACHAT_200k**.
    - Vyberte odpovídající **Dataset column**, která odpovídá vašemu datasetu. Například pokud používáte dataset **ULTRACHAT_200k**, vyberte **${data.prompt}** jako sloupec datasetu.

    ![Prompt flow evaluation.](../../../../../../translated_images/cs/evaluation-setting2.07036831ba58d64e.webp)

1. Vyberte **Next**.

1. Nastavte metriky výkonu a kvality:

    - Vyberte metriky výkonu a kvality, které chcete použít.
    - Vyberte model Azure OpenAI, který jste vytvořili pro hodnocení. Například vyberte **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/cs/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Nastavte metriky rizika a bezpečnosti:

    - Vyberte metriky rizika a bezpečnosti, které chcete použít.
    - Vyberte hranici pro výpočet míry chyb, kterou chcete použít. Například vyberte **Medium**.
    - Pro **question** vyberte **Data source** na **{$data.prompt}**.
    - Pro **answer** vyberte **Data source** na **{$run.outputs.answer}**.
    - Pro **ground_truth** vyberte **Data source** na **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/cs/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Vyberte **Next**.

1. Vyberte **Submit** pro zahájení hodnocení.

1. Hodnocení potrvá nějaký čas. Pokrok můžete sledovat na záložce **Evaluation**.

### Prohlédnutí výsledků hodnocení

> [!NOTE]
> Výsledky uvedené níže ilustrují průběh hodnocení. V tomto tutoriálu jsme použili model jemně vyladěný na relativně malém datasetu, což může vést k suboptimálním výsledkům. Skutečné výsledky se mohou výrazně lišit v závislosti na velikosti, kvalitě a různorodosti použitého datasetu, stejně jako na konkrétní konfiguraci modelu.

Po dokončení hodnocení si můžete prohlédnout výsledky jak metrik výkonu, tak bezpečnosti.
1. Výkonové a kvalitativní metriky:

    - zhodnoťte efektivitu modelu při generování koherentních, plynulých a relevantních odpovědí.

    ![Evaluation result.](../../../../../../translated_images/cs/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Rizikové a bezpečnostní metriky:

    - Ujistěte se, že výstupy modelu jsou bezpečné a v souladu s principy odpovědné AI, vyhýbají se jakémukoli škodlivému nebo urážlivému obsahu.

    ![Evaluation result.](../../../../../../translated_images/cs/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Můžete poscrollovat dolů a zobrazit **Podrobný výsledek metrik**.

    ![Evaluation result.](../../../../../../translated_images/cs/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Hodnocením vašeho vlastního modelu Phi-3 / Phi-3.5 jak podle výkonových, tak bezpečnostních metrik můžete potvrdit, že model není jen efektivní, ale také dodržuje zásady odpovědné AI a je připraven k nasazení v reálném světě.

## Gratulujeme!

### Dokončili jste tento návod

Úspěšně jste vyhodnotili doladěný model Phi-3 integrovaný s Prompt flow v Microsoft Foundry. Tento krok je důležitý k zajištění, že vaše AI modely nejenže dosahují dobrého výkonu, ale také dodržují principy odpovědné AI společnosti Microsoft, což vám pomůže vybudovat důvěryhodné a spolehlivé AI aplikace.

![Architecture.](../../../../../../translated_images/cs/architecture.10bec55250f5d6a4.webp)

## Úklid Azure zdrojů

Vyčistěte své Azure zdroje, abyste se vyhnuli dalším poplatkům na vašem účtu. Přejděte do Azure portálu a smažte následující zdroje:

- Azure Machine learning zdroj.
- Azure Machine learning model endpoint.
- Microsoft Foundry projektový zdroj.
- Microsoft Foundry Prompt flow zdroj.

### Další kroky

#### Dokumentace

- [Hodnocení AI systémů pomocí dashboardu Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metriky pro vyhodnocení a monitorování generativní AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry dokumentace](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokumentace](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Výukový obsah

- [Úvod do přístupu odpovědné AI od Microsoftu](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Úvod do Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [Co je odpovědná AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Oznámení nových nástrojů v Azure AI, které vám pomohou vytvářet bezpečnější a důvěryhodnější generativní AI aplikace](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Hodnocení generativních AI aplikací](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí služby AI překladatele [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->