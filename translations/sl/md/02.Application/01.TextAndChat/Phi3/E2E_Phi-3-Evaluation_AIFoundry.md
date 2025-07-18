<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:59:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "sl"
}
-->
# Ocenjevanje fino prilagojenega modela Phi-3 / Phi-3.5 v Azure AI Foundry z osredotočenostjo na Microsoftova načela odgovorne umetne inteligence

Ta celovit (E2E) primer temelji na vodiču "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Community.

## Pregled

### Kako lahko ocenite varnost in zmogljivost fino prilagojenega modela Phi-3 / Phi-3.5 v Azure AI Foundry?

Fino prilagajanje modela lahko včasih privede do neželenih ali nepričakovanih odzivov. Da zagotovimo, da model ostane varen in učinkovit, je pomembno oceniti njegovo sposobnost generiranja škodljive vsebine ter njegovo zmožnost ustvarjanja natančnih, relevantnih in koherentnih odgovorov. V tem vodiču se boste naučili, kako oceniti varnost in zmogljivost fino prilagojenega modela Phi-3 / Phi-3.5, integriranega s Prompt flow v Azure AI Foundry.

Tukaj je postopek ocenjevanja v Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.sl.png)

*Vir slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Za podrobnejše informacije in dodatne vire o Phi-3 / Phi-3.5 obiščite [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Predpogoji

- [Python](https://www.python.org/downloads)
- [Azure naročnina](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fino prilagojen model Phi-3 / Phi-3.5

### Kazalo

1. [**Scenarij 1: Uvod v ocenjevanje Prompt flow v Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Uvod v ocenjevanje varnosti](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Uvod v ocenjevanje zmogljivosti](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenarij 2: Ocenjevanje modela Phi-3 / Phi-3.5 v Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Preden začnete](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implementacija Azure OpenAI za ocenjevanje modela Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ocenjevanje fino prilagojenega modela Phi-3 / Phi-3.5 z uporabo ocenjevanja Prompt flow v Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Čestitke!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenarij 1: Uvod v ocenjevanje Prompt flow v Azure AI Foundry**

### Uvod v ocenjevanje varnosti

Da zagotovite, da je vaš AI model etičen in varen, je ključno, da ga ocenite glede na Microsoftova načela odgovorne umetne inteligence. V Azure AI Foundry ocene varnosti omogočajo preverjanje ranljivosti modela za napade jailbreak in njegovega potenciala za generiranje škodljive vsebine, kar je neposredno povezano s temi načeli.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.sl.png)

*Vir slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoftova načela odgovorne umetne inteligence

Pred začetkom tehničnih korakov je pomembno razumeti Microsoftova načela odgovorne umetne inteligence, etični okvir, ki usmerja odgovoren razvoj, uvajanje in delovanje AI sistemov. Ta načela usmerjajo odgovorno oblikovanje, razvoj in uvajanje AI sistemov ter zagotavljajo, da so AI tehnologije zgrajene na pravičen, pregleden in vključujoč način. Ta načela so temelj za ocenjevanje varnosti AI modelov.

Microsoftova načela odgovorne umetne inteligence vključujejo:

- **Pravičnost in vključevanje**: AI sistemi naj obravnavajo vse pošteno in se izogibajo različnemu obravnavanju skupin ljudi v podobnih okoliščinah. Na primer, ko AI sistemi svetujejo glede medicinskega zdravljenja, vlog za posojila ali zaposlitve, naj vsem z enakimi simptomi, finančnimi pogoji ali strokovnimi kvalifikacijami ponudijo enake priporočila.

- **Zanesljivost in varnost**: Za gradnjo zaupanja je ključno, da AI sistemi delujejo zanesljivo, varno in dosledno. Ti sistemi morajo delovati tako, kot so bili prvotno zasnovani, varno reagirati na nepričakovane pogoje in se upirati škodljivim manipulacijam. Njihovo vedenje in raznolikost pogojev, ki jih lahko obvladajo, odražata nabor situacij in okoliščin, ki so jih razvijalci predvideli med oblikovanjem in testiranjem.

- **Preglednost**: Ko AI sistemi pomagajo pri odločanju, ki močno vpliva na življenja ljudi, je ključno, da ljudje razumejo, kako so bile te odločitve sprejete. Na primer, banka lahko uporabi AI sistem za odločanje o kreditni sposobnosti osebe. Podjetje lahko uporabi AI sistem za izbiro najbolj usposobljenih kandidatov za zaposlitev.

- **Zasebnost in varnost**: Z naraščajočo uporabo AI postaja zaščita zasebnosti in varovanje osebnih ter poslovnih podatkov vse pomembnejša in zahtevnejša. Pri AI je zasebnost in varnost podatkov ključna, saj je dostop do podatkov nujen za natančne in informirane napovedi ter odločitve o ljudeh.

- **Odgovornost**: Ljudje, ki oblikujejo in uvajajo AI sisteme, morajo biti odgovorni za delovanje svojih sistemov. Organizacije naj se opirajo na industrijske standarde za razvoj norm odgovornosti. Te norme lahko zagotovijo, da AI sistemi niso zadnja avtoriteta pri odločitvah, ki vplivajo na življenja ljudi, in da ljudje ohranijo pomemben nadzor nad sicer zelo avtonomnimi AI sistemi.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.sl.png)

*Vir slike: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Za več informacij o Microsoftovih načelih odgovorne umetne inteligence obiščite [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Merila varnosti

V tem vodiču boste ocenili varnost fino prilagojenega modela Phi-3 z uporabo varnostnih meril Azure AI Foundry. Ta merila vam pomagajo oceniti potencial modela za generiranje škodljive vsebine in njegovo ranljivost za napade jailbreak. Varnostna merila vključujejo:

- **Vsebina, povezana s samopoškodovanjem**: Ocenjuje, ali model kaže nagnjenost k ustvarjanju vsebine, povezane s samopoškodovanjem.
- **Sovražna in nepravična vsebina**: Ocenjuje, ali model kaže nagnjenost k ustvarjanju sovražne ali nepravične vsebine.
- **Nasilna vsebina**: Ocenjuje, ali model kaže nagnjenost k ustvarjanju nasilne vsebine.
- **Seksualna vsebina**: Ocenjuje, ali model kaže nagnjenost k ustvarjanju neprimerne seksualne vsebine.

Ocenjevanje teh vidikov zagotavlja, da AI model ne proizvaja škodljive ali žaljive vsebine, s čimer se usklajuje z družbenimi vrednotami in regulativnimi standardi.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.sl.png)

### Uvod v ocenjevanje zmogljivosti

Da zagotovite, da vaš AI model deluje kot pričakovano, je pomembno oceniti njegovo zmogljivost glede na merila zmogljivosti. V Azure AI Foundry ocene zmogljivosti omogočajo oceno učinkovitosti modela pri ustvarjanju natančnih, relevantnih in koherentnih odgovorov.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.sl.png)

*Vir slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Merila zmogljivosti

V tem vodiču boste ocenili zmogljivost fino prilagojenega modela Phi-3 / Phi-3.5 z uporabo meril zmogljivosti Azure AI Foundry. Ta merila vam pomagajo oceniti učinkovitost modela pri ustvarjanju natančnih, relevantnih in koherentnih odgovorov. Merila zmogljivosti vključujejo:

- **Utemeljenost (Groundedness)**: Ocenjuje, kako dobro se ustvarjeni odgovori ujemajo z informacijami iz vhodnega vira.
- **Relevanca**: Ocenjuje ustreznost ustvarjenih odgovorov glede na zastavljena vprašanja.
- **Koherentnost**: Ocenjuje, kako gladko teče ustvarjeno besedilo, ali se bere naravno in spominja na človeški jezik.
- **Fluidnost**: Ocenjuje jezikovno spretnost ustvarjenega besedila.
- **Podobnost z GPT (GPT Similarity)**: Primerja ustvarjeni odgovor z dejanskim odgovorom glede podobnosti.
- **F1 rezultat**: Izračuna razmerje skupnih besed med ustvarjenim odgovorom in izvorno vsebino.

Ta merila vam pomagajo oceniti učinkovitost modela pri ustvarjanju natančnih, relevantnih in koherentnih odgovorov.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.sl.png)

## **Scenarij 2: Ocenjevanje modela Phi-3 / Phi-3.5 v Azure AI Foundry**

### Preden začnete

Ta vodič je nadaljevanje prejšnjih blog objav, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." V teh objavah smo predstavili postopek fino prilagajanja modela Phi-3 / Phi-3.5 v Azure AI Foundry in njegovo integracijo s Prompt flow.

V tem vodiču boste implementirali Azure OpenAI model kot ocenjevalca v Azure AI Foundry in ga uporabili za ocenjevanje vašega fino prilagojenega modela Phi-3 / Phi-3.5.

Preden začnete ta vodič, poskrbite, da imate naslednje predpogoje, kot je opisano v prejšnjih vodičih:

1. Pripravljen nabor podatkov za ocenjevanje fino prilagojenega modela Phi-3 / Phi-3.5.
1. Model Phi-3 / Phi-3.5, ki je bil fino prilagojen in implementiran v Azure Machine Learning.
1. Prompt flow, integriran z vašim fino prilagojenim modelom Phi-3 / Phi-3.5 v Azure AI Foundry.

> [!NOTE]
> Za ocenjevanje fino prilagojenega modela Phi-3 / Phi-3.5 boste uporabili datoteko *test_data.jsonl*, ki se nahaja v mapi data iz nabora podatkov **ULTRACHAT_200k**, prenesenega v prejšnjih blog objavah.

#### Integracija prilagojenega modela Phi-3 / Phi-3.5 s Prompt flow v Azure AI Foundry (pristop najprej koda)
> [!NOTE]
> Če ste sledili pristopu z nizko kodo, opisanem v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", lahko to vajo preskočite in nadaljujete z naslednjo.
> Če pa ste sledili pristopu, ki temelji na kodi, opisanem v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)", da bi prilagodili in namestili svoj model Phi-3 / Phi-3.5, je postopek povezovanja vašega modela s Prompt flow nekoliko drugačen. Ta postopek boste spoznali v tej vaji.
Za nadaljevanje morate integrirati svoj fino nastavljeni model Phi-3 / Phi-3.5 v Prompt flow v Azure AI Foundry.

#### Ustvarite Azure AI Foundry Hub

Pred ustvarjanjem projekta morate ustvariti Hub. Hub deluje kot Resource Group, ki vam omogoča organizacijo in upravljanje več projektov znotraj Azure AI Foundry.

1. Prijavite se v [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Izberite **All hubs** na levi stranski vrstici.

1. Izberite **+ New hub** v navigacijskem meniju.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.sl.png)

1. Izvedite naslednje korake:

    - Vnesite **Hub name**. Mora biti edinstvena vrednost.
    - Izberite svojo Azure **Subscription**.
    - Izberite **Resource group**, ki jo želite uporabiti (po potrebi ustvarite novo).
    - Izberite **Location**, ki jo želite uporabiti.
    - Izberite **Connect Azure AI Services**, ki jih želite uporabiti (po potrebi ustvarite nove).
    - Izberite **Connect Azure AI Search** in izberite **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.sl.png)

1. Izberite **Next**.

#### Ustvarite Azure AI Foundry projekt

1. V Hubu, ki ste ga ustvarili, izberite **All projects** na levi stranski vrstici.

1. Izberite **+ New project** v navigacijskem meniju.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.sl.png)

1. Vnesite **Project name**. Mora biti edinstvena vrednost.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.sl.png)

1. Izberite **Create a project**.

#### Dodajte lastno povezavo za fino nastavljeni model Phi-3 / Phi-3.5

Za integracijo svojega modela Phi-3 / Phi-3.5 s Prompt flow morate shraniti endpoint in ključ modela v lastno povezavo. Ta nastavitev zagotavlja dostop do vašega modela Phi-3 / Phi-3.5 v Prompt flow.

#### Nastavite api ključ in endpoint uri fino nastavljenega modela Phi-3 / Phi-3.5

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pomaknite se do Azure Machine learning delovnega prostora, ki ste ga ustvarili.

1. Izberite **Endpoints** na levi stranski vrstici.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.sl.png)

1. Izberite endpoint, ki ste ga ustvarili.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.sl.png)

1. Izberite **Consume** v navigacijskem meniju.

1. Kopirajte svoj **REST endpoint** in **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.sl.png)

#### Dodajte lastno povezavo

1. Obiščite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pomaknite se do Azure AI Foundry projekta, ki ste ga ustvarili.

1. V projektu, ki ste ga ustvarili, izberite **Settings** na levi stranski vrstici.

1. Izberite **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.sl.png)

1. Izberite **Custom keys** v navigacijskem meniju.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.sl.png)

1. Izvedite naslednje korake:

    - Izberite **+ Add key value pairs**.
    - Za ime ključa vnesite **endpoint** in prilepite endpoint, ki ste ga kopirali iz Azure ML Studio, v polje za vrednost.
    - Ponovno izberite **+ Add key value pairs**.
    - Za ime ključa vnesite **key** in prilepite ključ, ki ste ga kopirali iz Azure ML Studio, v polje za vrednost.
    - Po dodajanju ključev izberite **is secret**, da preprečite razkritje ključa.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.sl.png)

1. Izberite **Add connection**.

#### Ustvarite Prompt flow

Dodali ste lastno povezavo v Azure AI Foundry. Zdaj ustvarimo Prompt flow z naslednjimi koraki. Nato boste to Prompt flow povezali z lastno povezavo, da boste lahko uporabljali fino nastavljeni model znotraj Prompt flow.

1. Pomaknite se do Azure AI Foundry projekta, ki ste ga ustvarili.

1. Izberite **Prompt flow** na levi stranski vrstici.

1. Izberite **+ Create** v navigacijskem meniju.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.sl.png)

1. Izberite **Chat flow** v navigacijskem meniju.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.sl.png)

1. Vnesite **Folder name**, ki ga želite uporabiti.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.sl.png)

1. Izberite **Create**.

#### Nastavite Prompt flow za klepet z vašim fino nastavljenim modelom Phi-3 / Phi-3.5

Model Phi-3 / Phi-3.5 morate integrirati v Prompt flow. Vendar obstoječi Prompt flow ni zasnovan za ta namen, zato ga morate predelati, da omogočite integracijo lastnega modela.

1. V Prompt flow izvedite naslednje korake za prenovo obstoječega toka:

    - Izberite **Raw file mode**.
    - Izbrišite vso obstoječo kodo v datoteki *flow.dag.yml*.
    - Dodajte naslednjo kodo v *flow.dag.yml*.

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

    - Izberite **Save**.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.sl.png)

1. Dodajte naslednjo kodo v *integrate_with_promptflow.py*, da uporabite lastni model Phi-3 / Phi-3.5 v Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.sl.png)

> [!NOTE]
> Za podrobnejše informacije o uporabi Prompt flow v Azure AI Foundry si lahko ogledate [Prompt flow v Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Izberite **Chat input**, **Chat output**, da omogočite klepet z vašim modelom.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.sl.png)

1. Zdaj ste pripravljeni za klepet z vašim fino nastavljenim modelom Phi-3 / Phi-3.5. V naslednji vaji se boste naučili, kako zagnati Prompt flow in ga uporabiti za klepet z vašim modelom.

> [!NOTE]
>
> Prenovljen tok bi moral izgledati kot na spodnji sliki:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.sl.png)
>

#### Zaženite Prompt flow

1. Izberite **Start compute sessions**, da zaženete Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.sl.png)

1. Izberite **Validate and parse input**, da osvežite parametre.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.sl.png)

1. Izberite **Value** za **connection** in izberite lastno povezavo, ki ste jo ustvarili. Na primer, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.sl.png)

#### Klepetajte z vašim fino nastavljenim modelom Phi-3 / Phi-3.5

1. Izberite **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.sl.png)

1. Tukaj je primer rezultatov: Zdaj lahko klepetate z vašim fino nastavljenim modelom Phi-3 / Phi-3.5. Priporočljivo je, da zastavljate vprašanja, ki temeljijo na podatkih, uporabljenih za fino nastavitev.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.sl.png)

### Namestite Azure OpenAI za ocenjevanje modela Phi-3 / Phi-3.5

Za ocenjevanje modela Phi-3 / Phi-3.5 v Azure AI Foundry morate namestiti Azure OpenAI model. Ta model bo uporabljen za oceno zmogljivosti modela Phi-3 / Phi-3.5.

#### Namestite Azure OpenAI

1. Prijavite se v [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pomaknite se do Azure AI Foundry projekta, ki ste ga ustvarili.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.sl.png)

1. V projektu, ki ste ga ustvarili, izberite **Deployments** na levi stranski vrstici.

1. Izberite **+ Deploy model** v navigacijskem meniju.

1. Izberite **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.sl.png)

1. Izberite Azure OpenAI model, ki ga želite uporabiti. Na primer, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.sl.png)

1. Izberite **Confirm**.

### Ocenite fino nastavljeni model Phi-3 / Phi-3.5 z uporabo Prompt flow ocenjevanja v Azure AI Foundry

### Začnite novo ocenjevanje

1. Obiščite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pomaknite se do Azure AI Foundry projekta, ki ste ga ustvarili.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.sl.png)

1. V projektu, ki ste ga ustvarili, izberite **Evaluation** na levi stranski vrstici.

1. Izberite **+ New evaluation** v navigacijskem meniju.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.sl.png)

1. Izberite **Prompt flow** ocenjevanje.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.sl.png)

1. Izvedite naslednje korake:

    - Vnesite ime ocenjevanja. Mora biti edinstvena vrednost.
    - Izberite **Question and answer without context** kot vrsto naloge, saj podatkovni niz **ULTRACHAT_200k**, uporabljen v tem vodiču, ne vsebuje konteksta.
    - Izberite prompt flow, ki ga želite oceniti.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.sl.png)

1. Izberite **Next**.

1. Izvedite naslednje korake:

    - Izberite **Add your dataset** za nalaganje podatkovnega niza. Na primer, lahko naložite testno datoteko, kot je *test_data.json1*, ki je vključena pri prenosu podatkovnega niza **ULTRACHAT_200k**.
    - Izberite ustrezno **Dataset column**, ki ustreza vašemu podatkovnemu nizu. Na primer, če uporabljate **ULTRACHAT_200k**, izberite **${data.prompt}** kot stolpec podatkovnega niza.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.sl.png)

1. Izberite **Next**.

1. Izvedite naslednje korake za nastavitev metrik zmogljivosti in kakovosti:

    - Izberite metrike zmogljivosti in kakovosti, ki jih želite uporabiti.
    - Izberite Azure OpenAI model, ki ste ga ustvarili za ocenjevanje. Na primer, izberite **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.sl.png)

1. Izvedite naslednje korake za nastavitev metrik tveganja in varnosti:

    - Izberite metrike tveganja in varnosti, ki jih želite uporabiti.
    - Izberite prag za izračun stopnje napak, ki ga želite uporabiti. Na primer, izberite **Medium**.
    - Za **question** izberite **Data source** na **{$data.prompt}**.
    - Za **answer** izberite **Data source** na **{$run.outputs.answer}**.
    - Za **ground_truth** izberite **Data source** na **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.sl.png)

1. Izberite **Next**.

1. Izberite **Submit**, da začnete ocenjevanje.

1. Ocenjevanje bo trajalo nekaj časa. Napredek lahko spremljate v zavihku **Evaluation**.

### Preglejte rezultate ocenjevanja
> [!NOTE]
> Rezultati, prikazani spodaj, so namenjeni ponazoritvi postopka ocenjevanja. V tem vodiču smo uporabili model, ki je bil dodatno usposobljen na razmeroma majhnem naboru podatkov, kar lahko vodi do manj optimalnih rezultatov. Dejanski rezultati se lahko močno razlikujejo glede na velikost, kakovost in raznolikost uporabljenega nabora podatkov ter specifično konfiguracijo modela.
Ko je ocenjevanje končano, lahko pregledate rezultate tako za metrike zmogljivosti kot varnosti.

1. Metrike zmogljivosti in kakovosti:

    - ocenite učinkovitost modela pri ustvarjanju koherentnih, tekočih in relevantnih odgovorov.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.sl.png)

1. Metrike tveganja in varnosti:

    - Poskrbite, da so izhodi modela varni in skladni s Principi odgovorne umetne inteligence, brez škodljive ali žaljive vsebine.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.sl.png)

1. Pomaknite se navzdol, da si ogledate **Podrobne rezultate metrik**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.sl.png)

1. Z ocenjevanjem vašega prilagojenega modela Phi-3 / Phi-3.5 glede na metrike zmogljivosti in varnosti lahko potrdite, da model ni le učinkovit, ampak tudi sledi praksam odgovorne umetne inteligence, zaradi česar je pripravljen za uporabo v resničnem svetu.

## Čestitke!

### Uspešno ste zaključili ta vodič

Uspešno ste ocenili fino nastavljeni model Phi-3, integriran s Prompt flow v Azure AI Foundry. To je pomemben korak pri zagotavljanju, da vaši AI modeli ne le dobro delujejo, ampak tudi sledijo Microsoftovim principom odgovorne umetne inteligence, kar vam pomaga graditi zaupanja vredne in zanesljive AI aplikacije.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.sl.png)

## Počistite Azure vire

Počistite svoje Azure vire, da se izognete dodatnim stroškom na vašem računu. Pojdite v Azure portal in izbrišite naslednje vire:

- Azure Machine learning vir.
- Azure Machine learning model endpoint.
- Azure AI Foundry Project vir.
- Azure AI Foundry Prompt flow vir.

### Naslednji koraki

#### Dokumentacija

- [Ocenjevanje AI sistemov z uporabo Responsible AI nadzorne plošče](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metrike ocenjevanja in spremljanja za generativno AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Dokumentacija Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Dokumentacija Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Izobraževalna vsebina

- [Uvod v Microsoftov pristop k odgovorni umetni inteligenci](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Uvod v Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [Kaj je odgovorna umetna inteligenca?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Napoved novih orodij v Azure AI za pomoč pri gradnji varnejših in zaupanja vrednih generativnih AI aplikacij](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Ocenjevanje generativnih AI aplikacij](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.