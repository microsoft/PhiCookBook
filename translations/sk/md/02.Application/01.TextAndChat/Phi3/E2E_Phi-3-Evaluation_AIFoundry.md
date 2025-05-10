<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T17:13:59+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "sk"
}
-->
# Vyhodnotenie doladeného modelu Phi-3 / Phi-3.5 v Azure AI Foundry so zameraním na zásady zodpovednej AI od Microsoftu

Tento komplexný (E2E) príklad je založený na návode "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community.

## Prehľad

### Ako môžete vyhodnotiť bezpečnosť a výkon doladeného modelu Phi-3 / Phi-3.5 v Azure AI Foundry?

Doladenie modelu môže niekedy viesť k nežiadaným alebo nepredvídaným odpovediam. Aby sme zabezpečili, že model zostane bezpečný a efektívny, je dôležité vyhodnotiť jeho potenciál generovať škodlivý obsah a jeho schopnosť produkovať presné, relevantné a súdržné odpovede. V tomto návode sa naučíte, ako vyhodnotiť bezpečnosť a výkon doladeného modelu Phi-3 / Phi-3.5 integrovaného s Prompt flow v Azure AI Foundry.

Tu je hodnotiaci proces Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.sk.png)

*Zdroj obrázka: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Pre podrobnejšie informácie a ďalšie zdroje o Phi-3 / Phi-3.5 navštívte [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Požiadavky

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Doladený model Phi-3 / Phi-3.5

### Obsah

1. [**Scenár 1: Úvod do hodnotenia Prompt flow v Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Úvod do hodnotenia bezpečnosti](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Úvod do hodnotenia výkonu](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenár 2: Hodnotenie modelu Phi-3 / Phi-3.5 v Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Pred začiatkom](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nasadenie Azure OpenAI na hodnotenie modelu Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Hodnotenie doladeného modelu Phi-3 / Phi-3.5 pomocou hodnotenia Prompt flow v Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Gratulujeme!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenár 1: Úvod do hodnotenia Prompt flow v Azure AI Foundry**

### Úvod do hodnotenia bezpečnosti

Aby ste zabezpečili, že váš AI model je etický a bezpečný, je nevyhnutné ho hodnotiť podľa zásad zodpovednej AI od Microsoftu. V Azure AI Foundry vám hodnotenia bezpečnosti umožňujú posúdiť zraniteľnosť modelu voči útokom na obídenie (jailbreak) a jeho potenciál generovať škodlivý obsah, čo je v súlade s týmito zásadami.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.sk.png)

*Zdroj obrázka: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Zásady zodpovednej AI od Microsoftu

Pred začiatkom technických krokov je dôležité porozumieť zásadám zodpovednej AI od Microsoftu, etickému rámcu, ktorý usmerňuje zodpovedný vývoj, nasadenie a prevádzku AI systémov. Tieto zásady vedú zodpovedný dizajn, vývoj a nasadenie AI systémov tak, aby boli spravodlivé, transparentné a inkluzívne. Sú základom pre hodnotenie bezpečnosti AI modelov.

Zásady zodpovednej AI od Microsoftu zahŕňajú:

- **Spravodlivosť a inkluzívnosť**: AI systémy by mali zaobchádzať so všetkými spravodlivo a nemali by rôzne ovplyvňovať skupiny ľudí v podobnej situácii. Napríklad, keď AI systémy poskytujú odporúčania ohľadom liečby, žiadostí o pôžičku alebo zamestnania, mali by poskytovať rovnaké odporúčania všetkým s podobnými príznakmi, finančnou situáciou alebo odbornými kvalifikáciami.

- **Spoľahlivosť a bezpečnosť**: Pre vybudovanie dôvery je kľúčové, aby AI systémy fungovali spoľahlivo, bezpečne a konzistentne. Mali by pracovať tak, ako boli navrhnuté, bezpečne reagovať na neočakávané situácie a odolávať škodlivým manipuláciám. Ich správanie a schopnosť zvládať rôzne podmienky odrážajú situácie, ktoré vývojári očakávali počas návrhu a testovania.

- **Transparentnosť**: Keď AI systémy pomáhajú pri rozhodnutiach, ktoré majú veľký dopad na životy ľudí, je dôležité, aby ľudia rozumeli, ako boli tieto rozhodnutia prijaté. Napríklad banka môže použiť AI systém na posúdenie úverovej schopnosti osoby. Spoločnosť môže použiť AI systém na výber najvhodnejších kandidátov na zamestnanie.

- **Súkromie a bezpečnosť**: S rastúcim rozšírením AI je ochrana súkromia a zabezpečenie osobných a firemných informácií čoraz dôležitejšie a komplexnejšie. Pri AI je potrebné venovať osobitnú pozornosť ochrane súkromia a bezpečnosti dát, pretože prístup k dátam je nevyhnutný na to, aby AI systémy mohli robiť presné a informované predpovede a rozhodnutia o ľuďoch.

- **Zodpovednosť**: Ľudia, ktorí navrhujú a nasadzujú AI systémy, musia byť zodpovední za ich fungovanie. Organizácie by mali využiť priemyselné štandardy na vytvorenie noriem zodpovednosti. Tieto normy zabezpečujú, že AI systémy nie sú konečnou autoritou pri rozhodnutiach ovplyvňujúcich životy ľudí a že ľudia majú významnú kontrolu nad inak vysoko autonómnymi AI systémami.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.sk.png)

*Zdroj obrázka: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Ak chcete vedieť viac o zásadách zodpovednej AI od Microsoftu, navštívte [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metódy hodnotenia bezpečnosti

V tomto návode budete hodnotiť bezpečnosť doladeného modelu Phi-3 pomocou bezpečnostných metrík Azure AI Foundry. Tieto metriky vám pomôžu posúdiť potenciál modelu generovať škodlivý obsah a jeho zraniteľnosť voči útokom na obídenie (jailbreak). Bezpečnostné metriky zahŕňajú:

- **Obsah súvisiaci so sebapoškodzovaním**: Hodnotí, či model má tendenciu generovať obsah súvisiaci so sebapoškodzovaním.
- **Nenávistný a nespravodlivý obsah**: Hodnotí, či model má tendenciu produkovať nenávistný alebo nespravodlivý obsah.
- **Násilný obsah**: Hodnotí, či model má tendenciu produkovať násilný obsah.
- **Sexuálny obsah**: Hodnotí, či model má tendenciu generovať nevhodný sexuálny obsah.

Hodnotenie týchto aspektov zabezpečuje, že AI model neprodukuje škodlivý alebo urážlivý obsah, čo je v súlade so spoločenskými hodnotami a regulačnými štandardmi.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.sk.png)

### Úvod do hodnotenia výkonu

Aby ste zabezpečili, že váš AI model funguje podľa očakávaní, je dôležité hodnotiť jeho výkon podľa výkonnostných metrík. V Azure AI Foundry vám hodnotenia výkonu umožňujú posúdiť efektívnosť modelu pri generovaní presných, relevantných a súdržných odpovedí.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.sk.png)

*Zdroj obrázka: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Výkonnostné metriky

V tomto návode budete hodnotiť výkon doladeného modelu Phi-3 / Phi-3.5 pomocou výkonnostných metrík Azure AI Foundry. Tieto metriky vám pomôžu posúdiť efektívnosť modelu pri generovaní presných, relevantných a súdržných odpovedí. Výkonnostné metriky zahŕňajú:

- **Založenie na faktoch (Groundedness)**: Hodnotí, ako dobre generované odpovede korešpondujú s informáciami zo zdrojového vstupu.
- **Relevantnosť**: Hodnotí, ako dobre sú generované odpovede zamerané na položené otázky.
- **Súdržnosť**: Hodnotí, ako plynulo text plynie, či číta prirodzene a pripomína ľudský jazyk.
- **Plynulosť**: Hodnotí jazykovú úroveň generovaného textu.
- **Podobnosť s GPT (GPT Similarity)**: Porovnáva generovanú odpoveď s referenčnou odpoveďou z hľadiska podobnosti.
- **F1 skóre**: Vypočítava pomer spoločných slov medzi generovanou odpoveďou a zdrojovými dátami.

Tieto metriky vám pomôžu vyhodnotiť efektívnosť modelu pri generovaní presných, relevantných a súdržných odpovedí.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.sk.png)

## **Scenár 2: Hodnotenie modelu Phi-3 / Phi-3.5 v Azure AI Foundry**

### Pred začiatkom

Tento návod nadväzuje na predchádzajúce blogové príspevky, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" a "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." V týchto príspevkoch sme prešli procesom doladenia modelu Phi-3 / Phi-3.5 v Azure AI Foundry a jeho integrácie s Prompt flow.

V tomto návode nasadíte model Azure OpenAI ako evaluátor v Azure AI Foundry a použijete ho na hodnotenie vášho doladeného modelu Phi-3 / Phi-3.5.

Pred začatím tohto návodu sa uistite, že máte splnené nasledujúce požiadavky, ako bolo popísané v predchádzajúcich návodoch:

1. Pripravenú dátovú sadu na hodnotenie doladeného modelu Phi-3 / Phi-3.5.
1. Model Phi-3 / Phi-3.5, ktorý bol doladený a nasadený v Azure Machine Learning.
1. Prompt flow integrovaný s vaším doladeným modelom Phi-3 / Phi-3.5 v Azure AI Foundry.

> [!NOTE]
> Na hodnotenie doladeného modelu Phi-3 / Phi-3.5 použijete súbor *test_data.jsonl*, ktorý sa nachádza v dátovom priečinku datasetu **ULTRACHAT_200k** stiahnutého v predchádzajúcich blogových príspevkoch.

#### Integrácia vlastného modelu Phi-3 / Phi-3.5 s Prompt flow v Azure AI Foundry (prístup najskôr cez kód)

> [!NOTE]
> Ak ste použili low-code prístup popísaný v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", môžete tento krok preskočiť a pokračovať ďalej.
> Ak ste však použili prístup cez kód popísaný v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" na doladenie a nasadenie vášho modelu Phi-3 / Phi-3.5, proces pripojenia modelu k Prompt flow je mierne odlišný. Tento proces sa naučíte v tomto cvičení.

Na pokračovanie je potrebné integrovať váš doladený model Phi-3 / Phi-3.5 do Prompt flow v Azure AI Foundry.

#### Vytvorenie Azure AI Foundry Hubu

Pred vytvorením projektu je potrebné vytvoriť Hub. Hub funguje ako Resource Group, ktorá vám umožní organizovať a spravovať viacero projektov v Azure AI Foundry.

1. Prihláste sa do [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Z ľavého menu vyberte **All hubs**.

1. Z navigačného menu vyberte **+ New hub**.

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.sk.png)

1. Vykonajte nasledujúce kroky:

    - Zadajte **Hub name**. Musí byť jedinečný.
    - Vyberte svoju Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť (v prípade potreby vytvorte novú).
    - Vyberte **Location**, ktorú chcete použiť.
    - Vyberte **Connect Azure AI Services**, ktoré chcete použiť (v prípade potreby vytvorte nové).
    - Pri **Connect Azure AI Search** vyberte možnosť **Skip connecting**.
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.sk.png)

1. Vyberte **Next**.

#### Vytvorte projekt Azure AI Foundry

1. V Hub-e, ktorý ste vytvorili, vyberte z ľavého panela **All projects**.

1. Vyberte **+ New project** v navigačnom menu.

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.sk.png)

1. Zadajte **Project name**. Musí to byť jedinečná hodnota.

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.sk.png)

1. Vyberte **Create a project**.

#### Pridajte vlastné pripojenie pre doladený model Phi-3 / Phi-3.5

Ak chcete integrovať svoj vlastný model Phi-3 / Phi-3.5 s Prompt flow, musíte uložiť endpoint a kľúč modelu vo vlastnom pripojení. Tento postup zabezpečí prístup k vášmu vlastnému modelu Phi-3 / Phi-3.5 v Prompt flow.

#### Nastavte api key a endpoint uri doladeného modelu Phi-3 / Phi-3.5

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Prejdite do Azure Machine learning workspace, ktorý ste vytvorili.

1. Vyberte **Endpoints** z ľavého panela.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.sk.png)

1. Vyberte endpoint, ktorý ste vytvorili.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.sk.png)

1. Vyberte **Consume** v navigačnom menu.

1. Skopírujte svoj **REST endpoint** a **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.sk.png)

#### Pridajte vlastné pripojenie

1. Navštívte [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Prejdite do Azure AI Foundry projektu, ktorý ste vytvorili.

1. V projekte, ktorý ste vytvorili, vyberte **Settings** z ľavého panela.

1. Vyberte **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.sk.png)

1. Vyberte **Custom keys** v navigačnom menu.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.sk.png)

1. Vykonajte nasledovné kroky:

    - Vyberte **+ Add key value pairs**.
    - Pre názov kľúča zadajte **endpoint** a vložte endpoint, ktorý ste skopírovali z Azure ML Studio, do poľa hodnoty.
    - Opäť vyberte **+ Add key value pairs**.
    - Pre názov kľúča zadajte **key** a vložte kľúč, ktorý ste skopírovali z Azure ML Studio, do poľa hodnoty.
    - Po pridaní kľúčov zaškrtnite **is secret**, aby sa kľúč nezobrazoval.

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.sk.png)

1. Vyberte **Add connection**.

#### Vytvorte Prompt flow

Pridali ste vlastné pripojenie v Azure AI Foundry. Teraz vytvorme Prompt flow podľa nasledujúcich krokov. Následne prepojíte tento Prompt flow s vlastným pripojením, aby ste mohli použiť doladený model v Prompt flow.

1. Prejdite do Azure AI Foundry projektu, ktorý ste vytvorili.

1. Vyberte **Prompt flow** z ľavého panela.

1. Vyberte **+ Create** v navigačnom menu.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.sk.png)

1. Vyberte **Chat flow** v navigačnom menu.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.sk.png)

1. Zadajte **Folder name**, ktorý chcete použiť.

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.sk.png)

1. Vyberte **Create**.

#### Nastavte Prompt flow na komunikáciu s vaším vlastným modelom Phi-3 / Phi-3.5

Musíte integrovať doladený model Phi-3 / Phi-3.5 do Prompt flow. Existujúci Prompt flow však nie je navrhnutý na tento účel. Preto musíte Prompt flow prerobiť, aby ste umožnili integráciu vlastného modelu.

1. V Prompt flow vykonajte nasledovné kroky na prestavbu existujúceho flow:

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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.sk.png)

1. Pridajte nasledujúci kód do *integrate_with_promptflow.py*, aby ste použili vlastný model Phi-3 / Phi-3.5 v Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.sk.png)

> [!NOTE]
> Podrobnejšie informácie o používaní Prompt flow v Azure AI Foundry nájdete v [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Chat input**, **Chat output**, aby ste povolili komunikáciu s vaším modelom.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.sk.png)

1. Teraz ste pripravení komunikovať s vaším vlastným modelom Phi-3 / Phi-3.5. V ďalšom cvičení sa naučíte, ako spustiť Prompt flow a použiť ho na rozhovor s vaším doladeným modelom Phi-3 / Phi-3.5.

> [!NOTE]
>
> Prestavaný flow by mal vyzerať ako na obrázku nižšie:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.sk.png)
>

#### Spustite Prompt flow

1. Vyberte **Start compute sessions**, aby ste spustili Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.sk.png)

1. Vyberte **Validate and parse input**, aby ste obnovili parametre.

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.sk.png)

1. Vyberte **Value** pri **connection** na vlastné pripojenie, ktoré ste vytvorili. Napríklad *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.sk.png)

#### Komunikujte s vaším vlastným modelom Phi-3 / Phi-3.5

1. Vyberte **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.sk.png)

1. Tu je príklad výsledkov: Teraz môžete komunikovať s vaším vlastným modelom Phi-3 / Phi-3.5. Odporúča sa klásť otázky na základe dát použitých na doladenie.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.sk.png)

### Nasadenie Azure OpenAI na vyhodnotenie modelu Phi-3 / Phi-3.5

Na vyhodnotenie modelu Phi-3 / Phi-3.5 v Azure AI Foundry je potrebné nasadiť Azure OpenAI model. Tento model sa použije na vyhodnotenie výkonu modelu Phi-3 / Phi-3.5.

#### Nasadenie Azure OpenAI

1. Prihláste sa do [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Prejdite do Azure AI Foundry projektu, ktorý ste vytvorili.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.sk.png)

1. V projekte, ktorý ste vytvorili, vyberte **Deployments** z ľavého panela.

1. Vyberte **+ Deploy model** v navigačnom menu.

1. Vyberte **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.sk.png)

1. Vyberte Azure OpenAI model, ktorý chcete použiť. Napríklad **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.sk.png)

1. Vyberte **Confirm**.

### Vyhodnoťte doladený model Phi-3 / Phi-3.5 pomocou hodnotenia Prompt flow v Azure AI Foundry

### Spustite nové hodnotenie

1. Navštívte [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Prejdite do Azure AI Foundry projektu, ktorý ste vytvorili.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.sk.png)

1. V projekte, ktorý ste vytvorili, vyberte **Evaluation** z ľavého panela.

1. Vyberte **+ New evaluation** v navigačnom menu.
![Select evaluation.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.sk.png)

1. Vyberte hodnotenie **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.sk.png)

1. vykonajte nasledujúce úlohy:

    - Zadajte názov hodnotenia. Musí to byť jedinečná hodnota.
    - Vyberte typ úlohy **Question and answer without context**. Pretože dataset **UlTRACHAT_200k**, použitý v tomto návode, neobsahuje kontext.
    - Vyberte prompt flow, ktorý chcete hodnotiť.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.sk.png)

1. Vyberte **Next**.

1. vykonajte nasledujúce úlohy:

    - Vyberte **Add your dataset** na nahranie datasetu. Napríklad môžete nahrať testovací dataset, ako je *test_data.json1*, ktorý je súčasťou stiahnutia datasetu **ULTRACHAT_200k**.
    - Vyberte vhodný **Dataset column**, ktorý zodpovedá vášmu datasetu. Napríklad pri použití datasetu **ULTRACHAT_200k** vyberte **${data.prompt}** ako dataset column.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.sk.png)

1. Vyberte **Next**.

1. vykonajte nasledujúce úlohy na nastavenie metrík výkonnosti a kvality:

    - Vyberte metriky výkonnosti a kvality, ktoré chcete použiť.
    - Vyberte Azure OpenAI model, ktorý ste vytvorili pre hodnotenie. Napríklad vyberte **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.sk.png)

1. vykonajte nasledujúce úlohy na nastavenie metrík rizika a bezpečnosti:

    - Vyberte metriky rizika a bezpečnosti, ktoré chcete použiť.
    - Vyberte prahovú hodnotu na výpočet miery chýb, ktorú chcete použiť. Napríklad vyberte **Medium**.
    - Pre **question** vyberte **Data source** na **{$data.prompt}**.
    - Pre **answer** vyberte **Data source** na **{$run.outputs.answer}**.
    - Pre **ground_truth** vyberte **Data source** na **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.sk.png)

1. Vyberte **Next**.

1. Vyberte **Submit** na spustenie hodnotenia.

1. Hodnotenie potrvá určitý čas. Priebeh môžete sledovať na karte **Evaluation**.

### Prehľad výsledkov hodnotenia

> [!NOTE]
> Nižšie uvedené výsledky slúžia na ilustráciu procesu hodnotenia. V tomto návode sme použili model doladený na relatívne malom datasete, čo môže viesť k menej optimálnym výsledkom. Skutočné výsledky sa môžu výrazne líšiť v závislosti od veľkosti, kvality a rozmanitosti použitého datasetu, ako aj od konkrétnej konfigurácie modelu.

Po dokončení hodnotenia si môžete prezrieť výsledky pre metriky výkonnosti aj bezpečnosti.

1. Metriky výkonnosti a kvality:

    - hodnotia efektívnosť modelu pri generovaní koherentných, plynulých a relevantných odpovedí.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.sk.png)

1. Metriky rizika a bezpečnosti:

    - Zabezpečte, aby výstupy modelu boli bezpečné a zodpovedali princípom Responsible AI, vyhýbajúc sa škodlivému alebo urážlivému obsahu.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.sk.png)

1. Môžete posúvať nižšie a zobraziť **Detailed metrics result**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.sk.png)

1. Hodnotením vášho vlastného modelu Phi-3 / Phi-3.5 podľa metrík výkonnosti aj bezpečnosti môžete potvrdiť, že model nie je len efektívny, ale aj dodržiava zásady zodpovedného AI, vďaka čomu je pripravený na nasadenie v reálnom svete.

## Gratulujeme!

### Dokončili ste tento návod

Úspešne ste vyhodnotili doladený model Phi-3 integrovaný s Prompt flow v Azure AI Foundry. Toto je dôležitý krok na zabezpečenie toho, že vaše AI modely nielen dobre fungujú, ale aj dodržiavajú zásady Responsible AI od Microsoftu, aby ste mohli vytvárať dôveryhodné a spoľahlivé AI aplikácie.

![Architecture.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.sk.png)

## Vyčistenie Azure zdrojov

Vyčistite svoje Azure zdroje, aby ste predišli ďalším poplatkom na vašom účte. Prejdite do Azure portálu a odstráňte nasledujúce zdroje:

- Azure Machine learning resource.
- Azure Machine learning model endpoint.
- Azure AI Foundry Project resource.
- Azure AI Foundry Prompt flow resource.

### Ďalšie kroky

#### Dokumentácia

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Výukový obsah

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referencie

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.