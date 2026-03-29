# Ocenite fino nastavljeni model Phi-3 / Phi-3.5 v Microsoft Foundry s poudarkom na Microsoftovih načelih odgovorne umetne inteligence

Ta vzorec od začetka do konca (E2E) temelji na vodiču "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Community.

## Pregled

### Kako lahko ocenite varnost in zmogljivost fino nastavljenega modela Phi-3 / Phi-3.5 v Microsoft Foundry?

Fino nastavljanje modela včasih lahko privede do nenamernih ali nezaželenih odzivov. Da zagotovite, da model ostane varen in učinkovit, je pomembno oceniti potencial modela za ustvarjanje škodljive vsebine in njegovo sposobnost da proizvede natančne, relevantne in skladne odzive. V tem tutorialu se boste naučili, kako oceniti varnost in zmogljivost fino nastavljenega modela Phi-3 / Phi-3.5, integriranega s Prompt flow v Microsoft Foundry.

Tukaj je postopek ocenjevanja v Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/sl/architecture.10bec55250f5d6a4.webp)

*Vir slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Za več podrobnosti in raziskovanje dodatnih virov o Phi-3 / Phi-3.5, obiščite [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Predpogoji

- [Python](https://www.python.org/downloads)
- [Azure naročnina](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fino nastavljeni model Phi-3 / Phi-3.5

### Kazalo vsebine

1. [**Scenarij 1: Uvod v ocenjevanje Prompt flow v Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Uvod v ocenjevanje varnosti](#uvod-v-ocenjevanje-varnosti)
    - [Uvod v ocenjevanje zmogljivosti](#uvod-v-ocenjevanje-zmogljivosti)

1. [**Scenarij 2: Ocenjevanje modela Phi-3 / Phi-3.5 v Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Preden začnete](#preden-začnete)
    - [Namestitev Azure OpenAI za oceno modela Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Ocenite fino nastavljeni model Phi-3 / Phi-3.5 z uporabo ocenjevanja Prompt flow v Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Čestitke!](#čestitamo)

## **Scenarij 1: Uvod v ocenjevanje Prompt flow v Microsoft Foundry**

### Uvod v ocenjevanje varnosti

Da zagotovite, da je vaš model umetne inteligence etičen in varen, je ključnega pomena, da ga ocenite glede na Microsoftova načela odgovorne umetne inteligence. V Microsoft Foundry ocene varnosti omogočajo, da ocenite ranljivost vašega modela za napade s "jailbreak" in njegov potencial za ustvarjanje škodljive vsebine, kar je v neposredni povezanosti s temi načeli.

![Safaty evaluation.](../../../../../../translated_images/sl/safety-evaluation.083586ec88dfa950.webp)

*Vir slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoftova načela odgovorne umetne inteligence

Pred začetkom tehničnih korakov je bistveno razumeti Microsoftova načela odgovorne umetne inteligence, etični okvir, ki je zasnovan za usmerjanje odgovornega razvoja, uvedbe in delovanja sistemov umetne inteligence. Ta načela usmerjajo odgovorno oblikovanje, razvoj in uvedbo sistemov umetne inteligence ter zagotavljajo, da so AI tehnologije zgrajene na način, ki je pošten, pregleden in vključujoč. Ta načela so temelj za ocenjevanje varnosti AI modelov.

Microsoftova načela odgovorne umetne inteligence vključujejo:

- **Pravičnost in vključevanje**: Sistemi umetne inteligence bi morali vse obravnavati pošteno in se izogibati, da bi na različne načine vplivali na podobne skupine ljudi. Na primer, kadar sistemi AI zagotavljajo usmeritve o medicinskem zdravljenju, vlogah za kredite ali zaposlovanju, bi morali podati enake priporočila vsem, ki imajo podobne simptome, finančne okoliščine ali poklicne kvalifikacije.

- **Zanesljivost in varnost**: Za vzpostavitev zaupanja je ključno, da sistemi umetne inteligence delujejo zanesljivo, varno in dosledno. Ti sistemi bi morali biti sposobni delovati tako, kot so bili prvotno zasnovani, varno odzvati na nepredvidene pogoje in se upreti škodljivim manipulacijam. Njihovo vedenje in paleta pogojev, s katerimi se lahko spopadejo, odražata obseg situacij in okoliščin, ki jih je razvijalec predvidel med oblikovanjem in testiranjem.

- **Čeprvna jasnost**: Ko sistemi umetne inteligence pomagajo pri odločanju, ki ima velik vpliv na življenja ljudi, je ključnega pomena, da ljudje razumejo, kako so bile te odločitve sprejete. Na primer, banka bi lahko uporabila sistem umetne inteligence za odločitev, ali je oseba kreditno sposobna. Podjetje bi lahko uporabilo sistem AI, da določi najbolj kvalificirane kandidate za zaposlitev.

- **Zasebnost in varnost**: Ko umetna inteligenca postaja bolj razširjena, je zaščita zasebnosti in varovanje osebnih ter poslovnih informacij vse bolj pomembna in zapletena. Pri AI sta zasebnost in varnost podatkov zelo ključna, ker je dostop do podatkov nujen za natančne in informirane napovedi ter odločitve o ljudeh.

- **Odgovornost**: Ljudje, ki oblikujejo in uvajajo sisteme umetne inteligence, morajo biti odgovorni za delovanje svojih sistemov. Organizacije naj uporabljajo industrijske standarde za razvoj norm odgovornosti. Te norme lahko zagotovijo, da sistemi AI niso končni avtoriteta za katerokoli odločitev, ki vpliva na življenja ljudi. Prav tako lahko zagotovijo, da ljudje ohranijo pomemben nadzor nad sicer zelo avtonomnimi sistemi umetne inteligence.

![Fill hub.](../../../../../../translated_images/sl/responsibleai2.c07ef430113fad8c.webp)

*Vir slike: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Za več informacij o Microsoftovih načelih odgovorne umetne inteligence obiščite [Kaj je odgovorna umetna inteligenca?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Merila varnosti

V tem vodiču boste ocenili varnost fino nastavljenega modela Phi-3 z uporabo varnostnih meril Microsoft Foundry. Ta merila vam pomagajo oceniti potencial modela za ustvarjanje škodljive vsebine in njegovo ranljivost za napade "jailbreak". Merila varnosti vključujejo:

- **Vsebine povezane z samopoškodovanjem**: Ocenjuje, ali ima model tendenco proizvajati vsebine povezane s samopoškodovanjem.
- **Sovražne in nepravične vsebine**: Ocenjuje, ali ima model tendenco proizvajati sovražne ali nepravične vsebine.
- **Nasilne vsebine**: Ocenjuje, ali ima model tendenco proizvajati nasilne vsebine.
- **Seksualne vsebine**: Ocenjuje, ali ima model tendenco proizvajati neprimerne seksualne vsebine.

Ocenjevanje teh vidikov zagotavlja, da AI model ne proizvaja škodljive ali žaljive vsebine, kar je v skladu z družbenimi vrednotami in regulativnimi standardi.

![Evaluate based on safety.](../../../../../../translated_images/sl/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Uvod v ocenjevanje zmogljivosti

Da zagotovite, da vaš model umetne inteligence deluje tako, kot je pričakovano, je pomembno oceniti njegovo zmogljivost glede na merila zmogljivosti. V Microsoft Foundry ocenjevanje zmogljivosti omogoča, da ocenite učinkovitost vašega modela pri ustvarjanju natančnih, relevantnih in skladnih odgovorov.

![Safaty evaluation.](../../../../../../translated_images/sl/performance-evaluation.48b3e7e01a098740.webp)

*Vir slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Merila zmogljivosti

V tem vodiču boste ocenili zmogljivost fino nastavljenega modela Phi-3 / Phi-3.5 z uporabo meril zmogljivosti Microsoft Foundry. Ta merila vam pomagajo oceniti učinkovitost modela pri ustvarjanju natančnih, relevantnih in skladnih odgovorov. Merila zmogljivosti vključujejo:

- **Utemeljenost**: Ocenite, kako dobro se ustvarjeni odgovori ujemajo z informacijami iz vhodnega vira.
- **Relevantnost**: Ocenjuje ustreznost ustvarjenih odgovorov glede na postavljena vprašanja.
- **Skladnost**: Ocenite, kako gladko teče ustvarjeno besedilo, kako naravno bere in kako spominja na jezik, ki ga uporablja človek.
- **Tekočnost**: Ocenite jezikovno spretnost ustvarjenega besedila.
- **Podobnost z GPT**: Primerja ustvarjeni odgovor z resničnimi podatki glede na podobnost.
- **F1 Ocena**: Izračuna razmerje skupnih besed med ustvarjenim odgovorom in izvirnimi podatki.

Ta merila vam pomagajo oceniti učinkovitost modela pri ustvarjanju natančnih, relevantnih in skladnih odgovorov.

![Evaluate based on performance.](../../../../../../translated_images/sl/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenarij 2: Ocenjevanje modela Phi-3 / Phi-3.5 v Microsoft Foundry**

### Preden začnete

Ta tutorial je nadaljevanje prejšnjih blog zapisov, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." V teh zapisih smo šli skozi postopek fino nastavljanja modela Phi-3 / Phi-3.5 v Microsoft Foundry in njegove integracije s Prompt flow.

V tem tutorialu boste namestili model Azure OpenAI kot ocenjevalca v Microsoft Foundry in ga uporabili za oceno vašega fino nastavljenega modela Phi-3 / Phi-3.5.

Pred začetkom tega tutoriala poskrbite, da imate naslednje predpogoje, kot so opisani v prejšnjih tutorialih:

1. Pripravljena podatkovna zbirka za oceno fino nastavljenega modela Phi-3 / Phi-3.5.
1. Model Phi-3 / Phi-3.5, ki je bil fino nastavljen in nameščen v Azure Machine Learning.
1. Prompt flow integriran z vašim fino nastavljenim modelom Phi-3 / Phi-3.5 v Microsoft Foundry.

> [!NOTE]
> Za ocenjevanje fino nastavljenega modela Phi-3 / Phi-3.5 boste uporabili datoteko *test_data.jsonl*, ki se nahaja v mapi podatkov iz naložene zbirke **ULTRACHAT_200k** iz prejšnjih blog zapisov.

#### Integracija po meri prilagojenega modela Phi-3 / Phi-3.5 s Prompt flow v Microsoft Foundry (pristop z uporabo kode)

> [!NOTE]
> Če ste sledili low-code pristopu, opisanem v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", lahko ta vaja preskočite in nadaljujete na naslednjo.
> Če pa ste sledili pristopu, ki se najprej ukvarja s kodo, opisanem v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" za fino nastavljanje in nameščanje vašega modela Phi-3 / Phi-3.5, je postopek povezovanja modela s Prompt flow nekoliko drugačen. Ta postopek boste spoznali v tej vaji.

Za nadaljevanje morate integrirati vaš fino nastavljeni model Phi-3 / Phi-3.5 v Prompt flow v Microsoft Foundry.

#### Ustvarjanje Microsoft Foundry Hub

Pred ustvarjanjem projekta morate ustvariti Hub. Hub deluje kot skupina virov, kar omogoča organizacijo in upravljanje več projektov znotraj Microsoft Foundry.
1. Prijavite se v [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Izberite **Vsi središč** na levi strani zavihka.

1. Izberite **+ Novo središče** v navigacijskem meniju.

    ![Ustvarite središče.](../../../../../../translated_images/sl/create-hub.5be78fb1e21ffbf1.webp)

1. Izvedite naslednja opravila:

    - Vnesite **Ime središča**. Mora biti edinstvena vrednost.
    - Izberite vaš Azure **Naročnina**.
    - Izberite **Skupino virov**, ki jo želite uporabiti (po potrebi ustvarite novo).
    - Izberite **Lokacijo**, ki bi jo radi uporabili.
    - Izberite **Povežite Azure AI storitve** za uporabo (po potrebi ustvarite nove).
    - Izberite **Poveži Azure AI iskanje** in **Preskoči povezovanje**.

    ![Izpolnite središče.](../../../../../../translated_images/sl/fill-hub.baaa108495c71e34.webp)

1. Izberite **Naprej**.

#### Ustvarite Microsoft Foundry projekt

1. V središču, ki ste ga ustvarili, izberite **Vsi projekti** na levi strani zavihka.

1. Izberite **+ Nov projekt** v navigacijskem meniju.

    ![Izberite nov projekt.](../../../../../../translated_images/sl/select-new-project.cd31c0404088d7a3.webp)

1. Vnesite **Ime projekta**. Mora biti edinstvena vrednost.

    ![Ustvarite projekt.](../../../../../../translated_images/sl/create-project.ca3b71298b90e420.webp)

1. Izberite **Ustvari projekt**.

#### Dodajte lastno povezavo za fino nastavljeni model Phi-3 / Phi-3.5

Za integracijo vašega lastnega modela Phi-3 / Phi-3.5 s Prompt flow morate shraniti končno točko in ključ modela v lastno povezavo. Ta nastavitev zagotavlja dostop do vašega lastnega modela Phi-3 / Phi-3.5 v Prompt flow.

#### Nastavite API ključ in URI končne točke za fino nastavljeni model Phi-3 / Phi-3.5

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pojdite v delovno okolje Azure Machine learning, ki ste ga ustvarili.

1. Izberite **Končne točke** na levi strani zavihka.

    ![Izberite končne točke.](../../../../../../translated_images/sl/select-endpoints.ee7387ecd68bd18d.webp)

1. Izberite končno točko, ki ste jo ustvarili.

    ![Izberite končno točko.](../../../../../../translated_images/sl/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Izberite **Poraba** v navigacijskem meniju.

1. Kopirajte vaš **REST endpoint** in **Primarni ključ**.

    ![Kopirajte API ključ in URI končne točke.](../../../../../../translated_images/sl/copy-endpoint-key.0650c3786bd646ab.webp)

#### Dodajte lastno povezavo

1. Obiščite [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pojdite v Microsoft Foundry projekt, ki ste ga ustvarili.

1. V projektu, ki ste ga ustvarili, izberite **Nastavitve** na levi strani zavihka.

1. Izberite **+ Nova povezava**.

    ![Izberite novo povezavo.](../../../../../../translated_images/sl/select-new-connection.fa0f35743758a74b.webp)

1. Izberite **Lastni ključi** v navigacijskem meniju.

    ![Izberite lastne ključe.](../../../../../../translated_images/sl/select-custom-keys.5a3c6b25580a9b67.webp)

1. Izvedite naslednja opravila:

    - Izberite **+ Dodaj par ključ-vrednost**.
    - Za ime ključa vnesite **endpoint** in prilepite končno točko, ki ste jo kopirali iz Azure ML Studia, v polje vrednosti.
    - Ponovno izberite **+ Dodaj par ključ-vrednost**.
    - Za ime ključa vnesite **key** in prilepite ključ, ki ste ga kopirali iz Azure ML Studia, v polje vrednosti.
    - Po dodajanju ključev izberite **je skrivnost**, da preprečite razkritje ključa.

    ![Dodajte povezavo.](../../../../../../translated_images/sl/add-connection.ac7f5faf8b10b0df.webp)

1. Izberite **Dodaj povezavo**.

#### Ustvarite Prompt flow

Dodali ste lastno povezavo v Microsoft Foundry. Zdaj ustvarimo Prompt flow z naslednjimi koraki. Nato boste to Prompt flow povezali z lastno povezavo za uporabo fino nastavljenega modela znotraj Prompt flow.

1. Pojdite v Microsoft Foundry projekt, ki ste ga ustvarili.

1. Izberite **Prompt flow** na levi strani zavihka.

1. Izberite **+ Ustvari** v navigacijskem meniju.

    ![Izberite Promptflow.](../../../../../../translated_images/sl/select-promptflow.18ff2e61ab9173eb.webp)

1. Izberite **Chat flow** v navigacijskem meniju.

    ![Izberite chat flow.](../../../../../../translated_images/sl/select-flow-type.28375125ec9996d3.webp)

1. Vnesite **Ime mape**, ki jo želite uporabiti.

    ![Izberite chat flow.](../../../../../../translated_images/sl/enter-name.02ddf8fb840ad430.webp)

1. Izberite **Ustvari**.

#### Nastavite Prompt flow za pogovor z vašim lastnim modelom Phi-3 / Phi-3.5

Za integracijo fino nastavljenega modela Phi-3 / Phi-3.5 v Prompt flow, morate preoblikovati obstoječi Prompt flow, ker obstoječi ni zasnovan za to. Zato morate predelati Prompt flow, da omogoči integracijo lastnega modela.

1. V Prompt flow izvedite naslednja opravila za predelavo obstoječega toka:

    - Izberite **Način surove datoteke**.
    - Izbrišite vse obstoječe kode v datoteki *flow.dag.yml*.
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

    - Izberite **Shrani**.

    ![Izberite način surove datoteke.](../../../../../../translated_images/sl/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Dodajte naslednjo kodo v *integrate_with_promptflow.py* za uporabo lastnega modela Phi-3 / Phi-3.5 v Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Nastavitev zapisovanja
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

        # "connection" je ime Po meri povezave, "endpoint", "key" so ključi v Po meri povezavi
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
            
            # Zabeleži celoten JSON odgovor
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

    ![Prilepite kodo prompt flow.](../../../../../../translated_images/sl/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Za bolj podrobne informacije o uporabi Prompt flow v Microsoft Foundry si lahko ogledate [Prompt flow v Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Izberite **Vhod za klepet**, **Izhod za klepet** za omogočanje klepeta z vašim modelom.

    ![Izberite vhod-izhod.](../../../../../../translated_images/sl/select-input-output.c187fc58f25fbfc3.webp)

1. Zdaj ste pripravljeni za klepet z vašim lastnim modelom Phi-3 / Phi-3.5. V naslednji vaji se boste naučili, kako zagnati Prompt flow in ga uporabiti za klepet z vašim fino nastavljenim modelom Phi-3 / Phi-3.5.

> [!NOTE]
>
> Predelani tok bi moral izgledati kot na spodnji sliki:
>
> ![Primer toka](../../../../../../translated_images/sl/graph-example.82fd1bcdd3fc545b.webp)
>

#### Zaženite Prompt flow

1. Izberite **Začni seje računanja** za začetek Prompt flow.

    ![Začnite sejo računanja.](../../../../../../translated_images/sl/start-compute-session.9acd8cbbd2c43df1.webp)

1. Izberite **Potrdi in obdela vhod** za osvežitev parametrov.

    ![Potrdi vhod.](../../../../../../translated_images/sl/validate-input.c1adb9543c6495be.webp)

1. Izberite **Vrednost** povezave do lastne povezave, ki ste jo ustvarili. Na primer, *connection*.

    ![Povezava.](../../../../../../translated_images/sl/select-connection.1f2b59222bcaafef.webp)

#### Klepetajte z vašim lastnim modelom Phi-3 / Phi-3.5

1. Izberite **Klepet**.

    ![Izberite klepet.](../../../../../../translated_images/sl/select-chat.0406bd9687d0c49d.webp)

1. Tukaj je primer rezultatov: zdaj lahko klepetate z vašim lastnim modelom Phi-3 / Phi-3.5. Priporočamo, da postavljate vprašanja, ki temeljijo na podatkih, uporabljenih za fino nastavitev.

    ![Klepet z prompt flow.](../../../../../../translated_images/sl/chat-with-promptflow.1cf8cea112359ada.webp)

### Namestite Azure OpenAI za ocenjevanje modela Phi-3 / Phi-3.5

Za ocenjevanje modela Phi-3 / Phi-3.5 v Microsoft Foundry morate namestiti Azure OpenAI model. Ta model bo uporabljen za ocenjevanje zmogljivosti modela Phi-3 / Phi-3.5.

#### Namestite Azure OpenAI

1. Prijavite se v [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pojdite v Microsoft Foundry projekt, ki ste ga ustvarili.

    ![Izberite projekt.](../../../../../../translated_images/sl/select-project-created.5221e0e403e2c9d6.webp)

1. V projektu, ki ste ga ustvarili, izberite **Namestitve** na levi strani zavihka.

1. Izberite **+ Namesti model** v navigacijskem meniju.

1. Izberite **Namesti osnovni model**.

    ![Izberite Namestitve.](../../../../../../translated_images/sl/deploy-openai-model.95d812346b25834b.webp)

1. Izberite Azure OpenAI model, ki ga želite uporabiti. Na primer, **gpt-4o**.

    ![Izberite Azure OpenAI model, ki ga želite uporabiti.](../../../../../../translated_images/sl/select-openai-model.959496d7e311546d.webp)

1. Izberite **Potrdi**.

### Ocenite fino nastavljeni model Phi-3 / Phi-3.5 z uporabo ocenjevanja Prompt flow v Microsoft Foundry

### Začni novo ocenjevanje

1. Obiščite [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pojdite v Microsoft Foundry projekt, ki ste ga ustvarili.

    ![Izberite projekt.](../../../../../../translated_images/sl/select-project-created.5221e0e403e2c9d6.webp)

1. V projektu, ki ste ga ustvarili, izberite **Ocenjevanje** na levi strani zavihka.

1. Izberite **+ Novo ocenjevanje** v navigacijskem meniju.

    ![Izberite ocenjevanje.](../../../../../../translated_images/sl/select-evaluation.2846ad7aaaca7f4f.webp)

1. Izberite ocenjevanje **Prompt flow**.

    ![Izberite ocenjevanje Prompt flow.](../../../../../../translated_images/sl/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Izvedite naslednja opravila:

    - Vnesite ime ocenjevanja. Mora biti edinstvena vrednost.
    - Izberite **Vprašanje in odgovor brez konteksta** kot vrsto naloge. Ker **ULTRACHAT_200k** podatkovni niz uporabljen v tej vadnici ne vsebuje konteksta.
    - Izberite prompt flow, ki ga želite oceniti.

    ![Ocenjevanje Prompt flow.](../../../../../../translated_images/sl/evaluation-setting1.4aa08259ff7a536e.webp)

1. Izberite **Naprej**.

1. Izvedite naslednja opravila:

    - Izberite **Dodajte svoj podatkovni niz** za nalaganje podatkovnega niza. Na primer, lahko naložite testno datoteko podatkov, kot je *test_data.json1*, ki je vključena ob prenosu **ULTRACHAT_200k** podatkovnega niza.
    - Izberite ustrezen **Stolpec podatkovnega niza**, ki ustreza vašemu podatkovnemu nizu. Na primer, če uporabljate **ULTRACHAT_200k** podatkovni niz, izberite **${data.prompt}** kot stolpec podatkovnega niza.

    ![Ocenjevanje Prompt flow.](../../../../../../translated_images/sl/evaluation-setting2.07036831ba58d64e.webp)

1. Izberite **Naprej**.

1. Izvedite naslednja opravila za konfiguracijo metrik zmogljivosti in kakovosti:

    - Izberite merila zmogljivosti in kakovosti, ki jih želite uporabiti.
    - Izberite Azure OpenAI model, ki ste ga ustvarili za ocenjevanje. Na primer, izberite **gpt-4o**.

    ![Ocenjevanje Prompt flow.](../../../../../../translated_images/sl/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Izvedite naslednja opravila za konfiguracijo metrik tveganja in varnosti:

    - Izberite merila tveganja in varnosti, ki jih želite uporabiti.
    - Izberite prag za izračun stopnje napak, ki jo želite uporabiti. Na primer, izberite **Srednje**.
    - Za **vprašanje** izberite **Vir podatkov** na **{$data.prompt}**.
    - Za **odgovor** izberite **Vir podatkov** na **{$run.outputs.answer}**.
    - Za **resničnost** izberite **Vir podatkov** na **{$data.message}**.

    ![Ocenjevanje Prompt flow.](../../../../../../translated_images/sl/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Izberite **Naprej**.

1. Izberite **Pošlji** za začetek ocenjevanja.

1. Ocenjevanje bo trajalo nekaj časa. Napredek lahko spremljate v zavihku **Ocenjevanje**.

### Pregled rezultatov ocenjevanja

> [!NOTE]
> Rezultati, predstavljeni spodaj, so namenjeni ilustraciji procesa ocenjevanja. V tej vadnici smo uporabili model, fino nastavljen na razmeroma majhnem podatkovnem nizu, kar lahko vodi do podoptimalnih rezultatov. Dejanski rezultati se lahko bistveno razlikujejo glede na velikost, kakovost in raznolikost uporabljenega podatkovnega niza, kot tudi na specifično konfiguracijo modela.

Ko je ocenjevanje zaključeno, lahko pregledate rezultate tako za metrike zmogljivosti kot tudi za varnost.
1. Meritve učinkovitosti in kakovosti:

    - ocenite učinkovitost modela pri ustvarjanju koherentnih, tekočih in relevantnih odgovorov.

    ![Evaluation result.](../../../../../../translated_images/sl/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Meritve tveganja in varnosti:

    - Zagotovite, da so izhodi modela varni in skladni z načeli Odgovorne umetne inteligence, z izogibanjem kakršni koli škodljivi ali žaljivi vsebini.

    ![Evaluation result.](../../../../../../translated_images/sl/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Pomikate se lahko navzdol, da si ogledate **podrobne rezultate meritev**.

    ![Evaluation result.](../../../../../../translated_images/sl/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Z oceno vašega prilagojenega modela Phi-3 / Phi-3.5 glede na meritve zmogljivosti in varnosti lahko potrdite, da model ni le učinkovit, ampak tudi sledi praksam odgovorne umetne inteligence, kar ga naredi pripravljenega za uporabo v resničnem svetu.

## Čestitamo!

### Uspešno ste zaključili ta vodič

Uspešno ste ocenili fino nastavljeni model Phi-3, integriran s Prompt flow v Microsoft Foundry. To je pomemben korak pri zagotavljanju, da vaši AI modeli ne le dobro delujejo, temveč tudi sledijo Microsoftovim načelom Odgovorne umetne inteligence, kar vam pomaga graditi zaupanja vredne in zanesljive AI aplikacije.

![Architecture.](../../../../../../translated_images/sl/architecture.10bec55250f5d6a4.webp)

## Očistite Azure vire

Počistite vaše Azure vire, da se izognete dodatnim stroškom na vašem računu. Pojdite v Azure portal in izbrišite naslednje vire:

- Vir Azure Machine Learning.
- Končna točka modela Azure Machine Learning.
- Vir projekta Microsoft Foundry.
- Vir Microsoft Foundry Prompt flow.

### Naslednji koraki

#### Dokumentacija

- [Ocenjevanje AI sistemov z uporabo nadzorne plošče Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Meritve ocenjevanja in spremljanja za generativno AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Dokumentacija Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Dokumentacija za Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Izobraževalna vsebina

- [Uvod v Microsoftov pristop k Odgovorni umetni inteligenci](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Uvod v Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referenca

- [Kaj je Odgovorna AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Objava novih orodij v Azure AI, ki vam pomagajo graditi bolj varne in zaupanja vredne generativne AI aplikacije](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Ocenjevanje generativnih AI aplikacij](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za kakršna koli nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->