# Procjena fino podešenog modela Phi-3 / Phi-3.5 u Microsoft Foundry usredotočena na Microsoftove principe odgovornog AI

Ovaj end-to-end (E2E) uzorak temelji se na vodiču "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Community.

## Pregled

### Kako možete procijeniti sigurnost i performanse fino podešenog modela Phi-3 / Phi-3.5 u Microsoft Foundry?

Fino podešavanje modela ponekad može dovesti do nepredviđenih ili neželjenih odgovora. Kako biste osigurali da model ostane siguran i učinkovit, važno je procijeniti potencijal modela za generiranje štetnog sadržaja te njegovu sposobnost da daje točne, relevantne i koherentne odgovore. U ovom vodiču naučit ćete kako procijeniti sigurnost i performanse fino podešenog modela Phi-3 / Phi-3.5 integriranog s Prompt flowom u Microsoft Foundryju.

Ovdje je Microsoft Foundry-jev proces procjene.

![Architecture of tutorial.](../../../../../../translated_images/hr/architecture.10bec55250f5d6a4.webp)

*Izvor slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Za detaljnije informacije i dodatne resurse o Phi-3 / Phi-3.5, posjetite [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Preduvjeti

- [Python](https://www.python.org/downloads)
- [Azure pretplata](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fino podešeni model Phi-3 / Phi-3.5

### Sadržaj

1. [**Scenarij 1: Uvod u evaluaciju Prompt flowa u Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Uvod u procjenu sigurnosti](#uvod-u-procjenu-sigurnosti)
    - [Uvod u procjenu performansi](#uvod-u-procjenu-performansi)

1. [**Scenarij 2: Procjena modela Phi-3 / Phi-3.5 u Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Prije nego što počnete](#prije-nego-što-počnete)
    - [Postavljanje Azure OpenAI za procjenu modela Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Procjena fino podešenog modela Phi-3 / Phi-3.5 koristeći Prompt flow evaluaciju Microsoft Foundryja](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Čestitamo!](#čestitamo)

## **Scenarij 1: Uvod u evaluaciju Prompt flowa u Microsoft Foundry**

### Uvod u procjenu sigurnosti

Kako biste osigurali da je vaš AI model etičan i siguran, ključno je procijeniti ga u skladu s Microsoftovim principima odgovornog AI. U Microsoft Foundryju, procjene sigurnosti omogućuju procjenu ranjivosti vašeg modela na jailbreak napade i njegov potencijal za generiranje štetnog sadržaja, što je u potpunosti usklađeno s ovim principima.

![Safaty evaluation.](../../../../../../translated_images/hr/safety-evaluation.083586ec88dfa950.webp)

*Izvor slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoftovi principi odgovornog AI

Prije početka tehničkih koraka, važno je razumjeti Microsoftove principe odgovornog AI, etički okvir dizajniran da vodi odgovoran razvoj, implementaciju i rad AI sustava. Ovi principi usmjeravaju odgovoran dizajn, razvoj i implementaciju AI sustava, osiguravajući da AI tehnologije budu razvijene na način koji je pravedan, transparentan i inkluzivan. Ovi principi čine temelj za procjenu sigurnosti AI modela.

Microsoftovi principi odgovornog AI uključuju:

- **Pravednost i inkluzivnost**: AI sustavi trebaju tretirati sve pravedno i izbjegavati različito tretiranje sličnih grupa ljudi. Na primjer, kada AI sustavi daju smjernice o medicinskom liječenju, zahtjevima za zajam ili zaposlenju, trebaju davati iste preporuke svima koji imaju slične simptome, financijske prilike ili profesionalne kvalifikacije.

- **Pouzdanost i sigurnost**: Za izgradnju povjerenja ključno je da AI sustavi djeluju pouzdano, sigurno i dosljedno. Ti sustavi trebaju moći raditi onako kako su izvorno dizajnirani, sigurno reagirati na neočekivane uvjete i odupirati se štetnim manipulacijama. Njihovo ponašanje i raspon uvjeta koje mogu podnijeti odražavaju skup situacija koje su programeri predvidjeli tijekom dizajna i testiranja.

- **Transparentnost**: Kad AI sustavi pomažu u donošenju odluka s velikim utjecajem na živote ljudi, ključno je da ljudi razumiju kako su te odluke donesene. Na primjer, banka može koristiti AI sustav da odluči je li netko kreditno sposoban. Tvrtka može koristiti AI sustav za određivanje najkvalificiranijih kandidata za zaposlenje.

- **Privatnost i sigurnost podataka**: Kako AI postaje sve rašireniji, zaštita privatnosti i sigurnost osobnih i poslovnih podataka postaju sve važniji i kompleksniji. Uz AI, privatnost i sigurnost podataka zahtijevaju posebnu pažnju jer je pristup podacima ključan za točnost i informiranost AI sustava pri predviđanjima i odlukama o ljudima.

- **Odgovornost**: Osobe koje dizajniraju i implementiraju AI sustave moraju biti odgovorne za način na koji njihovi sustavi djeluju. Organizacije bi trebale primjenjivati industrijske standarde kako bi razvile norme za odgovornost. Te norme mogu osigurati da AI sustavi ne budu konačna vlast na bilo kojoj odluci koja utječe na živote ljudi, te da ljudi zadrže značajnu kontrolu nad visokopouzdanim autonomnim AI sustavima.

![Fill hub.](../../../../../../translated_images/hr/responsibleai2.c07ef430113fad8c.webp)

*Izvor slike: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Za više informacija o Microsoftovim principima odgovornog AI, posjetite [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metrike sigurnosti

U ovom vodiču procijenit ćete sigurnost fino podešenog Phi-3 modela koristeći sigurnosne metrike Microsoft Foundryja. Ove metrike pomažu u procjeni potencijala modela za generiranje štetnog sadržaja i njegove ranjivosti na jailbreak napade. Metrike sigurnosti uključuju:

- **Sadržaj vezan uz samoštetu**: Procjenjuje ima li model sklonost proizvodnji sadržaja vezanog uz samoštetu.
- **Mrzilački i nepravedan sadržaj**: Procjenjuje ima li model sklonost proizvodnji mrzilačkog ili nepravednog sadržaja.
- **Nasilni sadržaj**: Procjenjuje ima li model sklonost proizvodnji nasilnog sadržaja.
- **Seksualni sadržaj**: Procjenjuje ima li model sklonost proizvodnji neprimjerenog seksualnog sadržaja.

Procjena ovih aspekata osigurava da AI model ne proizvodi štetan ili uvredljiv sadržaj, usklađen sa društvenim vrijednostima i regulatornim standardima.

![Evaluate based on safety.](../../../../../../translated_images/hr/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Uvod u procjenu performansi

Kako biste osigurali da vaš AI model radi kako se očekuje, važno je procijeniti njegove performanse prema mjerilima performansi. U Microsoft Foundryju, procjene performansi omogućuju procjenu učinkovitosti vašeg modela u generiranju točnih, relevantnih i koherentnih odgovora.

![Safaty evaluation.](../../../../../../translated_images/hr/performance-evaluation.48b3e7e01a098740.webp)

*Izvor slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metrike performansi

U ovom vodiču procijenit ćete performanse fino podešenog modela Phi-3 / Phi-3.5 koristeći metrike performansi Microsoft Foundryja. Ove metrike pomažu u procjeni učinkovitosti modela u generiranju točnih, relevantnih i koherentnih odgovora. Metrike performansi uključuju:

- **Utemeljenost (Groundedness)**: Procjenjuje koliko se generirani odgovori slažu s informacijama iz izvornog izvora.
- **Relevantnost**: Procjenjuje relevantnost generiranih odgovora na postavljena pitanja.
- **Koherentnost**: Procjenjuje koliko tečno i prirodno teče generirani tekst te koliko nalikuje ljudskom jeziku.
- **Tečnost (Fluency)**: Procjenjuje jezičnu stručnost generiranog teksta.
- **Sličnost s GPT-om**: Uspoređuje generirani odgovor sa stvarnim podacima u pogledu sličnosti.
- **F1 rezultat**: Izračunava omjer zajedničkih riječi između generiranog odgovora i izvora podataka.

Ove metrike pomažu u procjeni učinkovitosti modela u generiranju točnih, relevantnih i koherentnih odgovora.

![Evaluate based on performance.](../../../../../../translated_images/hr/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenarij 2: Procjena modela Phi-3 / Phi-3.5 u Microsoft Foundry**

### Prije nego što počnete

Ovaj vodič je nastavak prethodnih blog zapisa, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." U tim postovima proveli smo kroz proces fino podešavanja modela Phi-3 / Phi-3.5 u Microsoft Foundryju i njegovu integraciju s Prompt flowom.

U ovom vodiču postavit ćete Azure OpenAI model kao evaluatora u Microsoft Foundryju i upotrijebiti ga za evaluaciju vašeg fino podešenog modela Phi-3 / Phi-3.5.

Prije početka ovog vodiča, osigurajte da imate sljedeće preduvjete, kao što je opisano u prethodnim vodičima:

1. Pripremljeni skup podataka za evaluaciju fino podešenog modela Phi-3 / Phi-3.5.
1. Fino podešen i implementiran Phi-3 / Phi-3.5 model u Azure Machine Learningu.
1. Prompt flow integriran s vašim fino podešenim modelom Phi-3 / Phi-3.5 u Microsoft Foundryju.

> [!NOTE]
> Kao skup podataka za procjenu fino podešenog modela Phi-3 / Phi-3.5 koristit ćete datoteku *test_data.jsonl*, smještenu u mapi s podacima iz skupa podataka **ULTRACHAT_200k** preuzetog u prethodnim blog zapisima.

#### Integracija prilagođenog Phi-3 / Phi-3.5 modela s Prompt flow u Microsoft Foundryju (pristup temeljen na kodu)

> [!NOTE]
> Ako ste pratili pristup s malo koda opisan u "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", možete preskočiti ovaj zadatak i nastaviti na sljedeći.
> Međutim, ako ste pratili pristup temeljen na kodu opisan u "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" za fino podešavanje i implementaciju vašeg modela Phi-3 / Phi-3.5, proces povezivanja vašeg modela s Prompt flowom je malo drugačiji. Naučit ćete taj proces u ovom zadatku.

Za nastavak trebate integrirati vaš fino podešeni model Phi-3 / Phi-3.5 u Prompt flow u Microsoft Foundryju.

#### Kreiranje Microsoft Foundry Hub-a

Prije nego što stvorite Projekt, morate kreirati Hub. Hub djeluje kao Resource Group, omogućujući vam organizaciju i upravljanje višestrukim Projektima unutar Microsoft Foundryja.
1. Prijavite se na [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Odaberite **All hubs** iz lijevog izbornika.

1. Odaberite **+ New hub** iz navigacijskog izbornika.

    ![Create hub.](../../../../../../translated_images/hr/create-hub.5be78fb1e21ffbf1.webp)

1. Obavite sljedeće zadatke:

    - Unesite **Hub name**. Mora biti jedinstvena vrijednost.
    - Odaberite svoj Azure **Subscription**.
    - Odaberite **Resource group** koju želite koristiti (kreirajte novu ako je potrebno).
    - Odaberite **Location** koju želite koristiti.
    - Odaberite **Connect Azure AI Services** za korištenje (kreirajte novu ako je potrebno).
    - Odaberite **Connect Azure AI Search** na **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/hr/fill-hub.baaa108495c71e34.webp)

1. Odaberite **Next**.

#### Kreirajte Microsoft Foundry projekt

1. U Hubu koji ste kreirali, odaberite **All projects** iz lijevog izbornika.

1. Odaberite **+ New project** iz navigacijskog izbornika.

    ![Select new project.](../../../../../../translated_images/hr/select-new-project.cd31c0404088d7a3.webp)

1. Unesite **Project name**. Mora biti jedinstvena vrijednost.

    ![Create project.](../../../../../../translated_images/hr/create-project.ca3b71298b90e420.webp)

1. Odaberite **Create a project**.

#### Dodajte prilagođenu vezu za fino podešeni Phi-3 / Phi-3.5 model

Da biste integrirali svoj prilagođeni Phi-3 / Phi-3.5 model s Prompt flow, morate spremiti endpoint modela i ključ u prilagođenu vezu. Ova postavka osigurava pristup vašem prilagođenom Phi-3 / Phi-3.5 modelu u Prompt flow.

#### Postavite api ključ i endpoint uri fino podešenog Phi-3 / Phi-3.5 modela

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigirajte do Azure Machine learning radnog prostora koji ste kreirali.

1. Odaberite **Endpoints** iz lijevog izbornika.

    ![Select endpoints.](../../../../../../translated_images/hr/select-endpoints.ee7387ecd68bd18d.webp)

1. Odaberite endpoint koji ste kreirali.

    ![Select endpoints.](../../../../../../translated_images/hr/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Odaberite **Consume** iz navigacijskog izbornika.

1. Kopirajte svoj **REST endpoint** i **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/hr/copy-endpoint-key.0650c3786bd646ab.webp)

#### Dodajte prilagođenu vezu

1. Posjetite [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigirajte do Microsoft Foundry projekta koji ste kreirali.

1. U Projektu koji ste kreirali, odaberite **Settings** iz lijevog izbornika.

1. Odaberite **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/hr/select-new-connection.fa0f35743758a74b.webp)

1. Odaberite **Custom keys** iz navigacijskog izbornika.

    ![Select custom keys.](../../../../../../translated_images/hr/select-custom-keys.5a3c6b25580a9b67.webp)

1. Obavite sljedeće zadatke:

    - Odaberite **+ Add key value pairs**.
    - Za naziv ključa unesite **endpoint** i zalijepite endpoint koji ste kopirali iz Azure ML Studia u polje vrijednosti.
    - Ponovno odaberite **+ Add key value pairs**.
    - Za naziv ključa unesite **key** i zalijepite ključ koji ste kopirali iz Azure ML Studia u polje vrijednosti.
    - Nakon dodavanja ključeva, odaberite **is secret** kako biste spriječili otkrivanje ključa.

    ![Add connection.](../../../../../../translated_images/hr/add-connection.ac7f5faf8b10b0df.webp)

1. Odaberite **Add connection**.

#### Kreirajte Prompt flow

Dodali ste prilagođenu vezu u Microsoft Foundry. Sada, kreirat ćemo Prompt flow koristeći sljedeće korake. Nakon toga, spojit ćete ovaj Prompt flow na prilagođenu vezu kako biste koristili fino podešeni model u okviru Prompt flow-a.

1. Navigirajte do Microsoft Foundry projekta koji ste kreirali.

1. Odaberite **Prompt flow** iz lijevog izbornika.

1. Odaberite **+ Create** iz navigacijskog izbornika.

    ![Select Promptflow.](../../../../../../translated_images/hr/select-promptflow.18ff2e61ab9173eb.webp)

1. Odaberite **Chat flow** iz navigacijskog izbornika.

    ![Select chat flow.](../../../../../../translated_images/hr/select-flow-type.28375125ec9996d3.webp)

1. Unesite **Folder name** koji ćete koristiti.

    ![Select chat flow.](../../../../../../translated_images/hr/enter-name.02ddf8fb840ad430.webp)

1. Odaberite **Create**.

#### Postavite Prompt flow za chat s vašim prilagođenim Phi-3 / Phi-3.5 modelom

Potrebno je integrirati fino podešeni Phi-3 / Phi-3.5 model u Prompt flow. Međutim, postojeći Prompt flow nije dizajniran za tu svrhu. Stoga, morate redizajnirati Prompt flow kako biste omogućili integraciju prilagođenog modela.

1. U Prompt flow-u obavite sljedeće zadatke za rekonstrukciju postojećeg toka:

    - Odaberite **Raw file mode**.
    - Izbrišite sav postojeći kod u datoteci *flow.dag.yml*.
    - Dodajte sljedeći kod u *flow.dag.yml*.

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

    - Odaberite **Save**.

    ![Select raw file mode.](../../../../../../translated_images/hr/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Dodajte sljedeći kod u *integrate_with_promptflow.py* da biste koristili prilagođeni Phi-3 / Phi-3.5 model u Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Postavljanje zapisivanja
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

        # "connection" je naziv Prilagođene veze, "endpoint", "key" su ključevi u Prilagođenoj vezi
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
            
            # Zabilježi puni JSON odgovor
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

    ![Paste prompt flow code.](../../../../../../translated_images/hr/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Za detaljnije informacije o korištenju Prompt flow u Microsoft Foundry, možete se obratiti [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Odaberite **Chat input**, **Chat output** da omogućite chat s vašim modelom.

    ![Select Input Output.](../../../../../../translated_images/hr/select-input-output.c187fc58f25fbfc3.webp)

1. Sada ste spremni za chat s vašim prilagođenim Phi-3 / Phi-3.5 modelom. U sljedećem zadatku naučit ćete kako pokrenuti Prompt flow i koristiti ga za chat s vašim fino podešenim Phi-3 / Phi-3.5 modelom.

> [!NOTE]
>
> Rekonstruirani tok trebao bi izgledati kao na slici ispod:
>
> ![Flow example](../../../../../../translated_images/hr/graph-example.82fd1bcdd3fc545b.webp)
>

#### Pokrenite Prompt flow

1. Odaberite **Start compute sessions** za pokretanje Prompt flow-a.

    ![Start compute session.](../../../../../../translated_images/hr/start-compute-session.9acd8cbbd2c43df1.webp)

1. Odaberite **Validate and parse input** za obnovu parametara.

    ![Validate input.](../../../../../../translated_images/hr/validate-input.c1adb9543c6495be.webp)

1. Odaberite **Value** veze prema prilagođenoj vezi koju ste kreirali. Na primjer, *connection*.

    ![Connection.](../../../../../../translated_images/hr/select-connection.1f2b59222bcaafef.webp)

#### Chat s vašim prilagođenim Phi-3 / Phi-3.5 modelom

1. Odaberite **Chat**.

    ![Select chat.](../../../../../../translated_images/hr/select-chat.0406bd9687d0c49d.webp)

1. Primjer rezultata: Sada možete razgovarati s vašim prilagođenim Phi-3 / Phi-3.5 modelom. Preporučuje se postavljati pitanja temeljena na podacima korištenim za fino podešavanje.

    ![Chat with prompt flow.](../../../../../../translated_images/hr/chat-with-promptflow.1cf8cea112359ada.webp)

### Postavite Azure OpenAI za evaluaciju Phi-3 / Phi-3.5 modela

Za evaluaciju Phi-3 / Phi-3.5 modela u Microsoft Foundry potrebno je postaviti Azure OpenAI model. Taj model će se koristiti za evaluaciju performansi Phi-3 / Phi-3.5 modela.

#### Postavite Azure OpenAI

1. Prijavite se na [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigirajte do Microsoft Foundry projekta koji ste kreirali.

    ![Select Project.](../../../../../../translated_images/hr/select-project-created.5221e0e403e2c9d6.webp)

1. U projektu koji ste kreirali, odaberite **Deployments** iz lijevog izbornika.

1. Odaberite **+ Deploy model** iz navigacijskog izbornika.

1. Odaberite **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/hr/deploy-openai-model.95d812346b25834b.webp)

1. Odaberite Azure OpenAI model koji želite koristiti. Na primjer, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/hr/select-openai-model.959496d7e311546d.webp)

1. Odaberite **Confirm**.

### Evaluirajte fino podešeni Phi-3 / Phi-3.5 model koristeći Microsoft Foundry's Prompt flow evaluaciju

### Pokrenite novu evaluaciju

1. Posjetite [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigirajte do Microsoft Foundry projekta koji ste kreirali.

    ![Select Project.](../../../../../../translated_images/hr/select-project-created.5221e0e403e2c9d6.webp)

1. U projektu koji ste kreirali, odaberite **Evaluation** iz lijevog izbornika.

1. Odaberite **+ New evaluation** iz navigacijskog izbornika.

    ![Select evaluation.](../../../../../../translated_images/hr/select-evaluation.2846ad7aaaca7f4f.webp)

1. Odaberite evaluaciju **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/hr/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Obavite sljedeće zadatke:

    - Unesite naziv evaluacije. Mora biti jedinstvena vrijednost.
    - Odaberite **Question and answer without context** kao tip zadatka. Jer, **UlTRACHAT_200k** skup podataka korišten u ovom tutorijalu ne sadrži kontekst.
    - Odaberite prompt flow koji želite evaluirati.

    ![Prompt flow evaluation.](../../../../../../translated_images/hr/evaluation-setting1.4aa08259ff7a536e.webp)

1. Odaberite **Next**.

1. Obavite sljedeće zadatke:

    - Odaberite **Add your dataset** za upload skupa podataka. Na primjer, možete uploadati testni skup podataka, kao što je *test_data.json1*, koji je uključen prilikom preuzimanja **ULTRACHAT_200k** skupa podataka.
    - Odaberite odgovarajuću **Dataset column** koja odgovara vašem skupu podataka. Na primjer, ako koristite **ULTRACHAT_200k** skup podataka, odaberite **${data.prompt}** kao Dataset column.

    ![Prompt flow evaluation.](../../../../../../translated_images/hr/evaluation-setting2.07036831ba58d64e.webp)

1. Odaberite **Next**.

1. Obavite sljedeće zadatke za konfiguraciju metrika performansi i kvalitete:

    - Odaberite metrike performansi i kvalitete koje želite koristiti.
    - Odaberite Azure OpenAI model koji ste kreirali za evaluaciju. Na primjer, odaberite **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/hr/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Obavite sljedeće zadatke za konfiguraciju metrika rizika i sigurnosti:

    - Odaberite metrike rizika i sigurnosti koje želite koristiti.
    - Odaberite prag za izračun stope pogrešaka kojeg želite koristiti. Na primjer, odaberite **Medium**.
    - Za **question**, odaberite **Data source** na **{$data.prompt}**.
    - Za **answer**, odaberite **Data source** na **{$run.outputs.answer}**.
    - Za **ground_truth**, odaberite **Data source** na **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/hr/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Odaberite **Next**.

1. Odaberite **Submit** za pokretanje evaluacije.

1. Evaluacija će potrajati neko vrijeme. Napredak možete pratiti na kartici **Evaluation**.

### Pregledajte rezultate evaluacije

> [!NOTE]
> Rezultati prikazani u nastavku namijenjeni su ilustraciji procesa evaluacije. U ovom tutorijalu koristili smo model fino podešen na relativno malom skupu podataka, što može dovesti do suboptimalnih rezultata. Stvarni rezultati mogu znatno varirati ovisno o veličini, kvaliteti i raznolikosti korištenog skupa podataka, kao i specifičnoj konfiguraciji modela.

Nakon završetka evaluacije, možete pregledati rezultate za metrike performansi i sigurnosti.
1. Metrike izvedbe i kvalitete:

    - procijenite učinkovitost modela u generiranju koherentnih, tečnih i relevantnih odgovora.

    ![Evaluation result.](../../../../../../translated_images/hr/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Metrike rizika i sigurnosti:

    - Osigurajte da su izlazi modela sigurni i usklađeni s Principima odgovornog umjetne inteligencije, izbjegavajući bilo kakav štetan ili uvredljiv sadržaj.

    ![Evaluation result.](../../../../../../translated_images/hr/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Možete se pomicati prema dolje da biste vidjeli **Detaljan rezultat metrika**.

    ![Evaluation result.](../../../../../../translated_images/hr/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Procjenom vašeg prilagođenog Phi-3 / Phi-3.5 modela u skladu s metrikama izvedbe i sigurnosti, možete potvrditi da model nije samo učinkovit, nego i da se pridržava praksi odgovorne umjetne inteligencije, čineći ga spremnim za primjenu u stvarnom svijetu.

## Čestitamo!

### Završili ste ovaj vodič

Uspješno ste procijenili fino podešeni Phi-3 model integriran s Prompt flow u Microsoft Foundry. Ovo je važan korak u osiguravanju da vaši AI modeli ne samo da dobro funkcioniraju, već i da se pridržavaju Microsoftovih principa odgovorne umjetne inteligencije kako biste mogli izgraditi pouzdane i odgovorne AI aplikacije.

![Architecture.](../../../../../../translated_images/hr/architecture.10bec55250f5d6a4.webp)

## Očistite Azure resurse

Očistite svoje Azure resurse kako biste izbjegli dodatne troškove na svom računu. Idite na Azure portal i izbrišite sljedeće resurse:

- Azure Machine learning resurs.
- Azure Machine learning model endpoint.
- Microsoft Foundry Project resurs.
- Microsoft Foundry Prompt flow resurs.

### Sljedeći koraci

#### Dokumentacija

- [Procijenite AI sustave pomoću nadzorne ploče Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metrike evaluacije i praćenja za generativnu umjetnu inteligenciju](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry dokumentacija](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokumentacija](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Trenažni sadržaj

- [Uvod u Microsoftov pristup odgovornoj umjetnoj inteligenciji](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Uvod u Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [Što je odgovorna umjetna inteligencija?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Najava novih alata u Azure AI za pomoć u izgradnji sigurnijih i pouzdanijih generativnih AI aplikacija](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluacija generativnih AI aplikacija](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI prijevodnog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, molimo imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->