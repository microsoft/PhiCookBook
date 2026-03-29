# Vyhodnoťte doladený model Phi-3 / Phi-3.5 v Microsoft Foundry so zameraním na zásady zodpovedného AI od Microsoftu

Tento end-to-end (E2E) príklad je založený na návode "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community.

## Prehľad

### Ako môžete vyhodnotiť bezpečnosť a výkon doladeného modelu Phi-3 / Phi-3.5 v Microsoft Foundry?

Doladenie modelu môže niekedy viesť k neúmyselným alebo nežiaducim odpovediam. Aby ste zaistili, že model zostane bezpečný a efektívny, je dôležité vyhodnotiť potenciál modelu generovať škodlivý obsah a jeho schopnosť produkovať presné, relevantné a zrozumiteľné odpovede. V tomto návode sa naučíte, ako vyhodnotiť bezpečnosť a výkon doladeného modelu Phi-3 / Phi-3.5 integrovaného s Prompt flow v Microsoft Foundry.

Tu je proces vyhodnotenia v Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/sk/architecture.10bec55250f5d6a4.webp)

*Zdroj obrázka: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Pre podrobnejšie informácie a preskúmanie ďalších zdrojov o Phi-3 / Phi-3.5 navštívte prosím [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Predpoklady

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Doladený model Phi-3 / Phi-3.5

### Obsah

1. [**Scenár 1: Úvod do vyhodnotenia Prompt flow v Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Úvod do vyhodnotenia bezpečnosti](#úvod-do-vyhodnotenia-bezpečnosti)
    - [Úvod do vyhodnotenia výkonu](#úvod-do-vyhodnotenia-výkonu)

1. [**Scenár 2: Vyhodnotenie modelu Phi-3 / Phi-3.5 v Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Pred začiatkom](#pred-začiatkom)
    - [Nasadenie Azure OpenAI na vyhodnotenie modelu Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Vyhodnotenie doladeného modelu Phi-3 / Phi-3.5 pomocou Prompt flow v Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Gratulujeme!](#gratulujeme)

## **Scenár 1: Úvod do vyhodnotenia Prompt flow v Microsoft Foundry**

### Úvod do vyhodnotenia bezpečnosti

Aby ste zaistili, že váš AI model je etický a bezpečný, je zásadné ho vyhodnotiť podľa zásad zodpovedného AI od Microsoftu. V Microsoft Foundry bezpečnostné vyhodnotenia umožňujú posúdiť zraniteľnosť vášho modelu voči jailbreak útokom a jeho potenciál generovať škodlivý obsah, čo priamo korešponduje s týmito princípmi.

![Safaty evaluation.](../../../../../../translated_images/sk/safety-evaluation.083586ec88dfa950.webp)

*Zdroj obrázka: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Zásady zodpovedného AI od Microsoftu

Pred začatím technických krokov je nevyhnutné pochopiť zásady zodpovedného AI od Microsoftu, etický rámec navrhnutý na riadenie zodpovedného vývoja, nasadenia a prevádzky AI systémov. Tieto princípy vedú zodpovedný dizajn, vývoj a nasadenie AI systémov, zabezpečujúc, že AI technológie sú vytvárané spravodlivo, transparentne a inkluzívne. Princípy sú základom pre vyhodnotenie bezpečnosti AI modelov.

Zásady zodpovedného AI od Microsoftu zahŕňajú:

- **Spravodlivosť a inkluzívnosť**: AI systémy by mali zaobchádzať so všetkými spravodlivo a vyhnúť sa rozdielnemu zaobchádzaniu s podobne situovanými skupinami ľudí. Napríklad keď AI systémy poskytujú odporúčania ohľadom lekárskej liečby, žiadostí o úver alebo zamestnania, mali by poskytovať rovnaké odporúčania každému, kto má podobné príznaky, finančnú situáciu alebo odbornú kvalifikáciu.

- **Spoľahlivosť a bezpečnosť**: Na vybudovanie dôvery je nevyhnutné, aby AI systémy fungovali spoľahlivo, bezpečne a konzistentne. Tieto systémy by mali byť schopné fungovať tak, ako boli pôvodne navrhnuté, bezpečne reagovať na nepredvídané podmienky a odolávať škodlivým manipuláciám. Ich správanie a rozmanitosť podmienok, ktoré dokážu zvládnuť, odrážajú množstvo situácií a okolností, ktoré vývojári očakávali počas návrhu a testovania.

- **Transparentnosť**: Keď AI systémy pomáhajú pri rozhodnutiach, ktoré majú zásadný dopad na životy ľudí, je kľúčové, aby ľudia chápali, ako boli tieto rozhodnutia prijaté. Napríklad banka môže použiť AI systém na rozhodnutie, či je osoba bonitná. Firma môže použiť AI systém na výber najkvalifikovanejších kandidátov na zamestnanie.

- **Súkromie a bezpečnosť**: S rastúcim rozšírením AI sú ochrana súkromia a zabezpečenie osobných a obchodných informácií čoraz dôležitejšie a komplexnejšie. Pri AI vyžadujú ochrana súkromia a bezpečnosť dát osobitnú pozornosť, pretože prístup k dátam je nevyhnutný pre AI systémy na presné a informované predpovede a rozhodnutia o ľuďoch.

- **Zodpovednosť**: Ľudia, ktorí navrhujú a nasadzujú AI systémy, musia byť zodpovední za to, ako ich systémy fungujú. Organizácie by mali používať priemyselné štandardy na rozvoj noriem zodpovednosti. Tieto normy môžu zabezpečiť, že AI systémy nebudú konečným autoritatívnym rozhodovateľom v akomkoľvek rozhodnutí ovplyvňujúcom životy ľudí. Takisto môžu zabezpečiť, že ľudia udržia zmysluplnú kontrolu nad inak vysoko autonómnymi AI systémami.

![Fill hub.](../../../../../../translated_images/sk/responsibleai2.c07ef430113fad8c.webp)

*Zdroj obrázka: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Pre viac informácií o zásadách zodpovedného AI od Microsoftu navštívte [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metriky bezpečnosti

V tomto návode vyhodnotíte bezpečnosť doladeného modelu Phi-3 pomocou metrik bezpečnosti v Microsoft Foundry. Tieto metriky vám pomáhajú posúdiť potenciál modelu generovať škodlivý obsah a jeho zraniteľnosť voči jailbreak útokom. Medzi metriky bezpečnosti patrí:

- **Obsah súvisiaci s sebapoškodzovaním**: Hodnotí, či model má tendenciu produkovať obsah súvisiaci so sebapoškodzovaním.
- **Nenávistný a nespravodlivý obsah**: Hodnotí, či model produkuje nenávistný alebo nespravodlivý obsah.
- **Násilný obsah**: Hodnotí, či model generuje násilný obsah.
- **Sexuálny obsah**: Hodnotí, či model produkovať nevhodný sexuálny obsah.

Vyhodnotenie týchto aspektov zabezpečuje, že AI model neprodukuje škodlivý alebo urážlivý obsah, čím je v súlade so spoločenskými hodnotami a regulačnými normami.

![Evaluate based on safety.](../../../../../../translated_images/sk/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Úvod do vyhodnotenia výkonu

Aby ste zaistili, že váš AI model funguje podľa očakávaní, je dôležité vyhodnotiť jeho výkon na základe výkonnostných metrík. V Microsoft Foundry výkonnostné vyhodnotenia umožňujú posúdiť efektívnosť modelu v generovaní presných, relevantných a zrozumiteľných odpovedí.

![Safaty evaluation.](../../../../../../translated_images/sk/performance-evaluation.48b3e7e01a098740.webp)

*Zdroj obrázka: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metriky výkonu

V tomto návode vyhodnotíte výkon doladeného modelu Phi-3 / Phi-3.5 pomocou výkonnostných metrík Microsoft Foundry. Tieto metriky vám pomáhajú posúdiť efektívnosť modelu pri generovaní presných, relevantných a zrozumiteľných odpovedí. Medzi metriky výkonu patria:

- **Zakotvenosť (Groundedness)**: Hodnotí, ako dobre generované odpovede korešpondujú s informáciami zo vstupného zdroja.
- **Relevantnosť**: Hodnotí významnosť generovaných odpovedí vzhľadom na zadané otázky.
- **Koherencia**: Hodnotí, ako plynulo text plynie, či je prirodzený a pripomína ľudský jazyk.
- **Plynulosť (Fluency)**: Hodnotí jazykovú zdatnosť generovaného textu.
- **Podobnosť s GPT (GPT Similarity)**: Porovnáva generovanú odpoveď so skutočnou odpoveďou, aby určil mieru podobnosti.
- **F1 skóre**: Vypočítava pomer zdieľaných slov medzi generovanou odpoveďou a zdrojovými dátami.

Tieto metriky vám pomáhajú vyhodnotiť efektívnosť modelu pri generovaní presných, relevantných a zrozumiteľných odpovedí.

![Evaluate based on performance.](../../../../../../translated_images/sk/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenár 2: Vyhodnotenie modelu Phi-3 / Phi-3.5 v Microsoft Foundry**

### Pred začiatkom

Tento návod nadväzuje na predchádzajúce blogové príspevky, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" a "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." V týchto článkoch sme prešli procesom doladenia modelu Phi-3 / Phi-3.5 v Microsoft Foundry a jeho integráciou s Prompt flow.

V tomto návode nasadíte model Azure OpenAI ako evaluátor v Microsoft Foundry a použijete ho na vyhodnotenie vášho doladeného modelu Phi-3 / Phi-3.5.

Pred začatím tohto návodu si overte, že máte nasledovné predpoklady, ako je popísané v predchádzajúcich návodoch:

1. Pripravený dataset na vyhodnotenie doladeného modelu Phi-3 / Phi-3.5.
1. Model Phi-3 / Phi-3.5, ktorý bol doladený a nasadený v Azure Machine Learning.
1. Prompt flow integrovaný s vaším doladeným modelom Phi-3 / Phi-3.5 v Microsoft Foundry.

> [!NOTE]
> Ako dataset pre vyhodnotenie doladeného modelu Phi-3 / Phi-3.5 použijete súbor *test_data.jsonl*, ktorý sa nachádza v priečinku data v datasete **ULTRACHAT_200k**, stiahnutom v predchádzajúcich blogových príspevkoch.

#### Integrácia vlastného modelu Phi-3 / Phi-3.5 s Prompt flow v Microsoft Foundry (prístup s dôrazom na kód)

> [!NOTE]
> Ak ste postupovali podľa low-code prístupu popísaného v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", môžete tento cvičenie preskočiť a pokračovať na ďalšie.
> Ak ste však postupovali podľa kód-first prístupu popísaného v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" na doladenie a nasadenie vášho modelu Phi-3 / Phi-3.5, proces prepojenia modelu s Prompt flow je mierne odlišný. Tento proces sa naučíte v tomto cvičení.

Na pokračovanie potrebujete integrovať váš doladený model Phi-3 / Phi-3.5 do Prompt flow v Microsoft Foundry.

#### Vytvorenie Microsoft Foundry Hub

Pred vytvorením projektu musíte vytvoriť Hub. Hub funguje ako Resource Group, ktorý vám umožňuje organizovať a spravovať viacero projektov v rámci Microsoft Foundry.
1. Prihláste sa do [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Vyberte **All hubs** z ľavého bočného panela.

1. Vyberte **+ New hub** z navigačného menu.

    ![Create hub.](../../../../../../translated_images/sk/create-hub.5be78fb1e21ffbf1.webp)

1. Vykonajte nasledujúce úlohy:

    - Zadajte **Hub name**. Musí to byť unikátna hodnota.
    - Vyberte svoje Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť (v prípade potreby vytvorte novú).
    - Vyberte **Location**, ktorú chcete použiť.
    - Vyberte **Connect Azure AI Services**, ktoré chcete použiť (v prípade potreby vytvorte nové).
    - Vyberte **Connect Azure AI Search** na **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/sk/fill-hub.baaa108495c71e34.webp)

1. Vyberte **Next**.

#### Vytvorenie projektu v Microsoft Foundry

1. V Hube, ktorý ste vytvorili, vyberte **All projects** z ľavého bočného panela.

1. Vyberte **+ New project** z navigačného menu.

    ![Select new project.](../../../../../../translated_images/sk/select-new-project.cd31c0404088d7a3.webp)

1. Zadajte **Project name**. Musí to byť unikátna hodnota.

    ![Create project.](../../../../../../translated_images/sk/create-project.ca3b71298b90e420.webp)

1. Vyberte **Create a project**.

#### Pridanie vlastného pripojenia pre doladený model Phi-3 / Phi-3.5

Ak chcete integrovať svoj vlastný model Phi-3 / Phi-3.5 s Prompt flow, musíte uložiť endpoint a kľúč modelu do vlastného pripojenia. Tento setup zabezpečí prístup k vášmu vlastnému modelu Phi-3 / Phi-3.5 v Prompt flow.

#### Nastavenie api kľúča a endpoint uri doladeného modelu Phi-3 / Phi-3.5

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Prejdite do Azure Machine learning workspace, ktorý ste vytvorili.

1. Vyberte **Endpoints** z ľavého bočného panela.

    ![Select endpoints.](../../../../../../translated_images/sk/select-endpoints.ee7387ecd68bd18d.webp)

1. Vyberte endpoint, ktorý ste vytvorili.

    ![Select endpoints.](../../../../../../translated_images/sk/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Vyberte **Consume** z navigačného menu.

1. Skopírujte svoj **REST endpoint** a **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/sk/copy-endpoint-key.0650c3786bd646ab.webp)

#### Pridanie vlastného pripojenia

1. Navštívte [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Prejdite do projektu Microsoft Foundry, ktorý ste vytvorili.

1. V projekte, ktorý ste vytvorili, vyberte **Settings** z ľavého bočného panela.

1. Vyberte **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/sk/select-new-connection.fa0f35743758a74b.webp)

1. Vyberte **Custom keys** z navigačného menu.

    ![Select custom keys.](../../../../../../translated_images/sk/select-custom-keys.5a3c6b25580a9b67.webp)

1. Vykonajte nasledujúce úlohy:

    - Vyberte **+ Add key value pairs**.
    - Pre názov kľúča zadajte **endpoint** a vložte endpoint skopírovaný z Azure ML Studio do poľa hodnoty.
    - Opäť vyberte **+ Add key value pairs**.
    - Pre názov kľúča zadajte **key** a vložte kľúč skopírovaný z Azure ML Studio do poľa hodnoty.
    - Po pridaní kľúčov vyberte **is secret**, aby sa kľúč neodhalil.

    ![Add connection.](../../../../../../translated_images/sk/add-connection.ac7f5faf8b10b0df.webp)

1. Vyberte **Add connection**.

#### Vytvorenie Prompt flow

Pridali ste vlastné pripojenie v Microsoft Foundry. Teraz si vytvoríme Prompt flow pomocou nasledujúcich krokov. Potom prepojíte tento Prompt flow s vlastným pripojením, aby ste mohli použiť doladený model v rámci Prompt flow.

1. Prejdite do projektu Microsoft Foundry, ktorý ste vytvorili.

1. Vyberte **Prompt flow** z ľavého bočného panela.

1. Vyberte **+ Create** z navigačného menu.

    ![Select Promptflow.](../../../../../../translated_images/sk/select-promptflow.18ff2e61ab9173eb.webp)

1. Vyberte **Chat flow** z navigačného menu.

    ![Select chat flow.](../../../../../../translated_images/sk/select-flow-type.28375125ec9996d3.webp)

1. Zadajte **Folder name**, ktorú chcete použiť.

    ![Select chat flow.](../../../../../../translated_images/sk/enter-name.02ddf8fb840ad430.webp)

1. Vyberte **Create**.

#### Nastavenie Prompt flow na chatovanie s vlastným modelom Phi-3 / Phi-3.5

Musíte integrovať doladený model Phi-3 / Phi-3.5 do Prompt flow. Avšak existujúci Prompt flow nie je na tento účel navrhnutý. Preto musíte Prompt flow prerobiť, aby umožňoval integráciu vlastného modelu.

1. V Prompt flow vykonajte nasledujúce úlohy na prestavbu existujúceho flow:

    - Vyberte **Raw file mode**.
    - Odstráňte všetok existujúci kód v súbore *flow.dag.yml*.
    - Pridajte nasledujúci kód do *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/sk/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Pridajte nasledujúci kód do *integrate_with_promptflow.py* na použitie vlastného modelu Phi-3 / Phi-3.5 v Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Nastavenie protokolovania
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

        # "connection" je názov vlastného pripojenia, "endpoint", "key" sú kľúče v rámci vlastného pripojenia
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
            
            # Protokolovať celú JSON odpoveď
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

    ![Paste prompt flow code.](../../../../../../translated_images/sk/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Pre podrobnejšie informácie o používaní Prompt flow v Microsoft Foundry môžete nahliadnuť do [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Chat input**, **Chat output**, aby ste povolili chatovanie s vašim modelom.

    ![Select Input Output.](../../../../../../translated_images/sk/select-input-output.c187fc58f25fbfc3.webp)

1. Teraz ste pripravení chatovať s vašim vlastným modelom Phi-3 / Phi-3.5. V nasledujúcej úlohe sa naučíte, ako spustiť Prompt flow a použiť ho na chatovanie s doladeným modelom Phi-3 / Phi-3.5.

> [!NOTE]
>
> Prestavaný flow by mal vyzerať ako na obrázku nižšie:
>
> ![Flow example](../../../../../../translated_images/sk/graph-example.82fd1bcdd3fc545b.webp)
>

#### Spustenie Prompt flow

1. Vyberte **Start compute sessions** na spustenie Prompt flow.

    ![Start compute session.](../../../../../../translated_images/sk/start-compute-session.9acd8cbbd2c43df1.webp)

1. Vyberte **Validate and parse input** na obnovenie parametrov.

    ![Validate input.](../../../../../../translated_images/sk/validate-input.c1adb9543c6495be.webp)

1. Vyberte **Value** položky **connection** na vlastné pripojenie, ktoré ste vytvorili. Napríklad *connection*.

    ![Connection.](../../../../../../translated_images/sk/select-connection.1f2b59222bcaafef.webp)

#### Chatovanie s vlastným modelom Phi-3 / Phi-3.5

1. Vyberte **Chat**.

    ![Select chat.](../../../../../../translated_images/sk/select-chat.0406bd9687d0c49d.webp)

1. Tu je príklad výsledkov: Teraz môžete chatovať s vašim vlastným modelom Phi-3 / Phi-3.5. Odporúča sa klásť otázky založené na dátach použitých na doladenie.

    ![Chat with prompt flow.](../../../../../../translated_images/sk/chat-with-promptflow.1cf8cea112359ada.webp)

### Nasadenie Azure OpenAI na vyhodnotenie modelu Phi-3 / Phi-3.5

Na vyhodnotenie modelu Phi-3 / Phi-3.5 v Microsoft Foundry je potrebné nasadiť model Azure OpenAI. Tento model sa bude používať na vyhodnotenie výkonu modelu Phi-3 / Phi-3.5.

#### Nasadenie Azure OpenAI

1. Prihláste sa do [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Prejdite do projektu Microsoft Foundry, ktorý ste vytvorili.

    ![Select Project.](../../../../../../translated_images/sk/select-project-created.5221e0e403e2c9d6.webp)

1. V projekte, ktorý ste vytvorili, vyberte **Deployments** z ľavého bočného panela.

1. Vyberte **+ Deploy model** z navigačného menu.

1. Vyberte **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/sk/deploy-openai-model.95d812346b25834b.webp)

1. Vyberte Azure OpenAI model, ktorý chcete použiť. Napríklad **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/sk/select-openai-model.959496d7e311546d.webp)

1. Vyberte **Confirm**.

### Vyhodnotenie doladeného modelu Phi-3 / Phi-3.5 pomocou Prompt flow evaluácie v Microsoft Foundry

### Spustenie nového vyhodnotenia

1. Navštívte [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Prejdite do projektu Microsoft Foundry, ktorý ste vytvorili.

    ![Select Project.](../../../../../../translated_images/sk/select-project-created.5221e0e403e2c9d6.webp)

1. V projekte, ktorý ste vytvorili, vyberte **Evaluation** z ľavého bočného panela.

1. Vyberte **+ New evaluation** z navigačného menu.

    ![Select evaluation.](../../../../../../translated_images/sk/select-evaluation.2846ad7aaaca7f4f.webp)

1. Vyberte vyhodnotenie typu **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/sk/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Vykonajte nasledujúce úlohy:

    - Zadajte názov vyhodnotenia. Musí to byť unikátna hodnota.
    - Vyberte **Question and answer without context** ako typ úlohy. Pretože dataset **ULTRACHAT_200k** použitý v tomto návode neobsahuje kontext.
    - Vyberte prompt flow, ktorý chcete vyhodnotiť.

    ![Prompt flow evaluation.](../../../../../../translated_images/sk/evaluation-setting1.4aa08259ff7a536e.webp)

1. Vyberte **Next**.

1. Vykonajte nasledujúce úlohy:

    - Vyberte **Add your dataset** na nahranie datasetu. Napríklad môžete nahrať testovací dataset ako *test_data.json1*, ktorý je zahrnutý pri stiahnutí datasetu **ULTRACHAT_200k**.
    - Vyberte vhodný **Dataset column**, ktorý zodpovedá vášmu datasetu. Napríklad, ak používate dataset **ULTRACHAT_200k**, vyberte **${data.prompt}** ako datasetový stĺpec.

    ![Prompt flow evaluation.](../../../../../../translated_images/sk/evaluation-setting2.07036831ba58d64e.webp)

1. Vyberte **Next**.

1. Vykonajte nasledujúce úlohy na konfiguráciu metrík výkonu a kvality:

    - Vyberte metriky výkonu a kvality, ktoré chcete použiť.
    - Vyberte Azure OpenAI model, ktorý ste vytvorili na vyhodnotenie. Napríklad vyberte **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/sk/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Vykonajte nasledujúce úlohy na konfiguráciu metrík rizika a bezpečnosti:

    - Vyberte metriky rizika a bezpečnosti, ktoré chcete použiť.
    - Vyberte prahovú hodnotu pre výpočet miery chýb, ktorú chcete použiť. Napríklad vyberte **Medium**.
    - Pre **question** vyberte **Data source** na **{$data.prompt}**.
    - Pre **answer** vyberte **Data source** na **{$run.outputs.answer}**.
    - Pre **ground_truth** vyberte **Data source** na **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/sk/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Vyberte **Next**.

1. Vyberte **Submit** na spustenie vyhodnotenia.

1. Vyhodnotenie potrvá nejaký čas. Môžete sledovať priebeh v záložke **Evaluation**.

### Prehľad výsledkov vyhodnotenia

> [!NOTE]
> Nasledovné výsledky sú určené na ilustráciu vyhodnocovacieho procesu. V tomto návode sme použili model doladený na relatívne malom datasete, čo môže viesť k podpriemerným výsledkom. Skutočné výsledky sa môžu výrazne líšiť v závislosti od veľkosti, kvality a rôznorodosti datasetu, ako aj špecifickej konfigurácie modelu.

Po dokončení vyhodnotenia môžete prehliadať výsledky pre metriky výkonu aj bezpečnosti.
1. Výkonnostné a kvalitatívne metriky:

    - vyhodnoťte účinnosť modelu pri generovaní koherentných, plynulých a relevantných odpovedí.

    ![Výsledok hodnotenia.](../../../../../../translated_images/sk/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Metódy hodnotenia rizík a bezpečnosti:

    - Zaistite, aby výstupy modelu boli bezpečné a zodpovedali princípom zodpovednej umelej inteligencie, vyhýbajúc sa škodlivému alebo urážlivému obsahu.

    ![Výsledok hodnotenia.](../../../../../../translated_images/sk/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Môžete rolovať nadol a zobraziť **Podrobné výsledky metriky**.

    ![Výsledok hodnotenia.](../../../../../../translated_images/sk/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Vyhodnotením vášho vlastného modelu Phi-3 / Phi-3.5 na základe výkonnostných aj bezpečnostných metrík môžete potvrdiť, že model nie je len efektívny, ale aj zodpovedá zásadám zodpovednej umelej inteligencie, čím je pripravený na nasadenie v reálnom svete.

## Gratulujeme!

### Úspešne ste dokončili tento tutoriál

Úspešne ste vyhodnotili jemne doladený model Phi-3 integrovaný s Prompt flow v Microsoft Foundry. Toto je dôležitý krok na zabezpečenie, že vaše AI modely nielen dobre fungujú, ale aj rešpektujú Microsoft princípy zodpovednej umelej inteligencie, čo vám pomôže vytvárať dôveryhodné a spoľahlivé AI aplikácie.

![Architektúra.](../../../../../../translated_images/sk/architecture.10bec55250f5d6a4.webp)

## Vyčistenie Azure zdrojov

Vyčistite svoje Azure zdroje, aby ste predišli ďalším poplatkom na vašom účte. Prejdite na Azure portál a vymažte nasledujúce zdroje:

- Azure Machine learning zdroj.
- Azure Machine learning model endpoint.
- Microsoft Foundry projektový zdroj.
- Microsoft Foundry Prompt flow zdroj.

### Ďalšie kroky

#### Dokumentácia

- [Hodnotenie AI systémov pomocou dashboardu Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metriky hodnotenia a monitorovania pre generatívnu AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Dokumentácia Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Dokumentácia Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Výukový obsah

- [Úvod do Microsoft prístupu k zodpovednej umelej inteligencii](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Úvod do Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referencie

- [Čo je to zodpovedná AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Oznamujeme nové nástroje v Azure AI na pomoc pri vývoji bezpečnejších a dôveryhodnejších generatívnych AI aplikácií](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Hodnotenie generatívnych AI aplikácií](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->