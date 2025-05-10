<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T17:16:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "sr"
}
-->
# Evaluacija fino podešenog Phi-3 / Phi-3.5 modela u Azure AI Foundry sa fokusom na Microsoftove principe odgovornog AI

Ovaj end-to-end (E2E) primer zasnovan je na vodiču "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Community.

## Pregled

### Kako možete oceniti bezbednost i performanse fino podešenog Phi-3 / Phi-3.5 modela u Azure AI Foundry?

Fino podešavanje modela ponekad može dovesti do neočekivanih ili neželjenih odgovora. Da bi model ostao bezbedan i efikasan, važno je proceniti njegov potencijal da generiše štetan sadržaj i sposobnost da daje tačne, relevantne i koherentne odgovore. U ovom tutorijalu naučićete kako da ocenite bezbednost i performanse fino podešenog Phi-3 / Phi-3.5 modela integrisanog sa Prompt flow u Azure AI Foundry.

Evo procesa evaluacije u Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.sr.png)

*Izvor slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Za detaljnije informacije i dodatne resurse o Phi-3 / Phi-3.5, posetite [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Preduslovi

- [Python](https://www.python.org/downloads)
- [Azure pretplata](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fino podešen Phi-3 / Phi-3.5 model

### Sadržaj

1. [**Scenario 1: Uvod u evaluaciju Prompt flow u Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Uvod u evaluaciju bezbednosti](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Uvod u evaluaciju performansi](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Evaluacija Phi-3 / Phi-3.5 modela u Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Pre nego što počnete](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Deploy Azure OpenAI za evaluaciju Phi-3 / Phi-3.5 modela](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evaluacija fino podešenog Phi-3 / Phi-3.5 modela korišćenjem Prompt flow evaluacije u Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Čestitamo!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Uvod u evaluaciju Prompt flow u Azure AI Foundry**

### Uvod u evaluaciju bezbednosti

Da biste osigurali da je vaš AI model etički prihvatljiv i bezbedan, ključno je da ga ocenite u skladu sa Microsoftovim principima odgovornog AI. U Azure AI Foundry, evaluacija bezbednosti omogućava procenu ranjivosti vašeg modela na jailbreak napade i njegov potencijal da generiše štetan sadržaj, što je direktno usklađeno sa ovim principima.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.sr.png)

*Izvor slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoftovi principi odgovornog AI

Pre nego što započnete tehničke korake, važno je da razumete Microsoftove principe odgovornog AI, etički okvir dizajniran da vodi odgovoran razvoj, implementaciju i rad AI sistema. Ovi principi usmeravaju odgovoran dizajn, razvoj i implementaciju AI sistema, osiguravajući da AI tehnologije budu pravične, transparentne i inkluzivne. Oni predstavljaju osnovu za procenu bezbednosti AI modela.

Microsoftovi principi odgovornog AI uključuju:

- **Pravičnost i inkluzivnost**: AI sistemi treba da tretiraju sve pošteno i da ne prave razliku između sličnih grupa ljudi na različite načine. Na primer, kada AI sistemi daju preporuke o medicinskom tretmanu, zahtevima za zajam ili zapošljavanju, trebalo bi da daju iste preporuke svima koji imaju slične simptome, finansijsku situaciju ili profesionalne kvalifikacije.

- **Pouzdanost i bezbednost**: Da bi se izgradilo poverenje, ključno je da AI sistemi rade pouzdano, sigurno i dosledno. Ovi sistemi treba da funkcionišu onako kako su prvobitno dizajnirani, da bezbedno reaguju na neočekivane uslove i da budu otporni na štetne manipulacije. Njihovo ponašanje i raznovrsnost uslova koje mogu da podnesu odražavaju situacije i okolnosti koje su programeri predvideli tokom dizajna i testiranja.

- **Transparentnost**: Kada AI sistemi pomažu u donošenju odluka koje značajno utiču na živote ljudi, važno je da ljudi razumeju kako su te odluke donete. Na primer, banka može koristiti AI sistem da odluči da li je osoba kreditno sposobna. Kompanija može koristiti AI sistem da odredi najkvalifikovanije kandidate za zapošljavanje.

- **Privatnost i bezbednost**: Kako AI postaje sve zastupljeniji, zaštita privatnosti i bezbednost ličnih i poslovnih podataka postaju važniji i složeniji. Sa AI, privatnost i sigurnost podataka zahtevaju posebnu pažnju jer pristup podacima je neophodan za tačne i informisane predikcije i odluke AI sistema o ljudima.

- **Odgovornost**: Ljudi koji dizajniraju i implementiraju AI sisteme moraju biti odgovorni za način na koji njihovi sistemi funkcionišu. Organizacije treba da koriste industrijske standarde za razvoj normi odgovornosti. Ove norme mogu osigurati da AI sistemi ne budu konačna vlast u bilo kojoj odluci koja utiče na živote ljudi. Takođe, mogu osigurati da ljudi zadrže značajnu kontrolu nad inače visoko autonomnim AI sistemima.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.sr.png)

*Izvor slike: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Za više informacija o Microsoftovim principima odgovornog AI, posetite [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metrike bezbednosti

U ovom tutorijalu ocenjujete bezbednost fino podešenog Phi-3 modela koristeći metrike bezbednosti Azure AI Foundry. Ove metrike pomažu da procenite potencijal modela da generiše štetan sadržaj i njegovu ranjivost na jailbreak napade. Metrike bezbednosti uključuju:

- **Sadržaj vezan za samopovređivanje**: Procena da li model ima tendenciju da proizvodi sadržaj vezan za samopovređivanje.
- **Mržnja i nepravedan sadržaj**: Procena da li model ima tendenciju da proizvodi sadržaj pun mržnje ili nepravedan sadržaj.
- **Nasilni sadržaj**: Procena da li model ima tendenciju da proizvodi nasilni sadržaj.
- **Seksualni sadržaj**: Procena da li model ima tendenciju da proizvodi neprimeren seksualni sadržaj.

Evaluacija ovih aspekata osigurava da AI model ne proizvodi štetan ili uvredljiv sadržaj, usklađujući ga sa društvenim vrednostima i regulatornim standardima.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.sr.png)

### Uvod u evaluaciju performansi

Da biste bili sigurni da vaš AI model radi kako se očekuje, važno je da ocenite njegove performanse pomoću relevantnih metrika. U Azure AI Foundry, evaluacija performansi omogućava da procenite efikasnost modela u generisanju tačnih, relevantnih i koherentnih odgovora.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.sr.png)

*Izvor slike: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metrike performansi

U ovom tutorijalu ocenjujete performanse fino podešenog Phi-3 / Phi-3.5 modela koristeći metrike performansi Azure AI Foundry. Ove metrike pomažu da procenite efikasnost modela u generisanju tačnih, relevantnih i koherentnih odgovora. Metrike performansi uključuju:

- **Utemeljenost (Groundedness)**: Procena koliko generisani odgovori odgovaraju informacijama iz izvornog materijala.
- **Relevantnost**: Procena koliko su generisani odgovori povezani sa postavljenim pitanjima.
- **Koherentnost**: Procena koliko tečno i prirodno teče generisani tekst, da li podseća na ljudski jezik.
- **Fleksibilnost (Fluency)**: Procena jezičke veštine generisanog teksta.
- **Sličnost sa GPT (GPT Similarity)**: Poređenje generisanog odgovora sa referentnim odgovorom radi ocene sličnosti.
- **F1 skor**: Izračunavanje odnosa zajedničkih reči između generisanog odgovora i izvornog teksta.

Ove metrike pomažu da se oceni efikasnost modela u generisanju tačnih, relevantnih i koherentnih odgovora.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.sr.png)

## **Scenario 2: Evaluacija Phi-3 / Phi-3.5 modela u Azure AI Foundry**

### Pre nego što počnete

Ovaj tutorijal je nastavak prethodnih blog postova, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." U tim postovima smo prošli kroz proces fino podešavanja Phi-3 / Phi-3.5 modela u Azure AI Foundry i integraciju sa Prompt flow.

U ovom tutorijalu ćete deploy-ovati Azure OpenAI model kao evaluatora u Azure AI Foundry i koristiti ga za evaluaciju vašeg fino podešenog Phi-3 / Phi-3.5 modela.

Pre nego što počnete, proverite da li imate sledeće preduslove, kao što je opisano u prethodnim tutorijalima:

1. Pripremljen skup podataka za evaluaciju fino podešenog Phi-3 / Phi-3.5 modela.
1. Phi-3 / Phi-3.5 model koji je fino podešen i deploy-ovan u Azure Machine Learning.
1. Prompt flow integrisan sa vašim fino podešenim Phi-3 / Phi-3.5 modelom u Azure AI Foundry.

> [!NOTE]
> Koristićete fajl *test_data.jsonl*, koji se nalazi u folderu data iz **ULTRACHAT_200k** skupa podataka preuzetog u prethodnim blog postovima, kao skup podataka za evaluaciju fino podešenog Phi-3 / Phi-3.5 modela.

#### Integracija prilagođenog Phi-3 / Phi-3.5 modela sa Prompt flow u Azure AI Foundry (pristup sa kodom)

> [!NOTE]
> Ako ste pratili low-code pristup opisan u "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", možete preskočiti ovaj zadatak i preći na sledeći.
> Međutim, ako ste pratili pristup sa kodom opisan u "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" za fino podešavanje i deploy vašeg Phi-3 / Phi-3.5 modela, proces povezivanja modela sa Prompt flow je malo drugačiji. Naučićete ovaj proces u ovom zadatku.

Da biste nastavili, potrebno je da integrišete vaš fino podešeni Phi-3 / Phi-3.5 model u Prompt flow u Azure AI Foundry.

#### Kreiranje Azure AI Foundry Hub-a

Potrebno je da kreirate Hub pre nego što napravite Projekat. Hub funkcioniše kao Resource Group i omogućava vam da organizujete i upravljate sa više Projekata unutar Azure AI Foundry.

1. Prijavite se na [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Izaberite **All hubs** sa leve strane.

1. Izaberite **+ New hub** iz navigacionog menija.

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.sr.png)

1. Uradite sledeće:

    - Unesite **Hub name**. Mora biti jedinstvena vrednost.
    - Izaberite vašu Azure **Subscription**.
    - Izaberite **Resource group** koju želite da koristite (kreirajte novu ako je potrebno).
    - Izaberite **Location** koju želite da koristite.
    - Izaberite **Connect Azure AI Services** koje želite da koristite (kreirajte novo ako je potrebno).
    - Izaberite **Connect Azure AI Search** i odaberite **Skip connecting**.
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.sr.png)

1. Izaberite **Next**.

#### Kreirajte Azure AI Foundry projekat

1. U Hub-u koji ste kreirali, izaberite **All projects** sa leve strane taba.

1. Izaberite **+ New project** iz navigacionog menija.

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.sr.png)

1. Unesite **Project name**. Mora biti jedinstvena vrednost.

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.sr.png)

1. Izaberite **Create a project**.

#### Dodajte prilagođenu konekciju za fino podešen Phi-3 / Phi-3.5 model

Da biste integrisali svoj prilagođeni Phi-3 / Phi-3.5 model sa Prompt flow, potrebno je da sačuvate endpoint i ključ modela u prilagođenoj konekciji. Ova postavka omogućava pristup vašem prilagođenom Phi-3 / Phi-3.5 modelu u Prompt flow-u.

#### Podesite api ključ i endpoint uri fino podešenog Phi-3 / Phi-3.5 modela

1. Posetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Idite do Azure Machine learning radnog prostora koji ste kreirali.

1. Izaberite **Endpoints** sa leve strane taba.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.sr.png)

1. Izaberite endpoint koji ste kreirali.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.sr.png)

1. Izaberite **Consume** iz navigacionog menija.

1. Kopirajte svoj **REST endpoint** i **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.sr.png)

#### Dodajte prilagođenu konekciju

1. Posetite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Idite do Azure AI Foundry projekta koji ste kreirali.

1. U projektu koji ste kreirali, izaberite **Settings** sa leve strane taba.

1. Izaberite **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.sr.png)

1. Izaberite **Custom keys** iz navigacionog menija.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.sr.png)

1. Obavite sledeće korake:

    - Izaberite **+ Add key value pairs**.
    - Za ime ključa unesite **endpoint** i nalepite endpoint koji ste kopirali iz Azure ML Studio u polje za vrednost.
    - Ponovo izaberite **+ Add key value pairs**.
    - Za ime ključa unesite **key** i nalepite ključ koji ste kopirali iz Azure ML Studio u polje za vrednost.
    - Nakon dodavanja ključeva, izaberite **is secret** da biste sprečili da ključ bude vidljiv.

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.sr.png)

1. Izaberite **Add connection**.

#### Kreirajte Prompt flow

Dodali ste prilagođenu konekciju u Azure AI Foundry. Sada ćemo kreirati Prompt flow koristeći sledeće korake. Nakon toga ćete povezati ovaj Prompt flow sa prilagođenom konekcijom kako biste koristili fino podešen model unutar Prompt flow-a.

1. Idite do Azure AI Foundry projekta koji ste kreirali.

1. Izaberite **Prompt flow** sa leve strane taba.

1. Izaberite **+ Create** iz navigacionog menija.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.sr.png)

1. Izaberite **Chat flow** iz navigacionog menija.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.sr.png)

1. Unesite **Folder name** koji želite da koristite.

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.sr.png)

1. Izaberite **Create**.

#### Podesite Prompt flow za ćaskanje sa vašim prilagođenim Phi-3 / Phi-3.5 modelom

Potrebno je da integrišete fino podešen Phi-3 / Phi-3.5 model u Prompt flow. Međutim, postojeći Prompt flow nije dizajniran za ovu namenu. Zato morate redizajnirati Prompt flow da biste omogućili integraciju prilagođenog modela.

1. U Prompt flow-u, obavite sledeće korake da biste obnovili postojeći tok:

    - Izaberite **Raw file mode**.
    - Obrišite sav postojeći kod u fajlu *flow.dag.yml*.
    - Dodajte sledeći kod u *flow.dag.yml*.

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

    - Izaberite **Save**.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.sr.png)

1. Dodajte sledeći kod u *integrate_with_promptflow.py* da biste koristili prilagođeni Phi-3 / Phi-3.5 model u Prompt flow-u.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.sr.png)

> [!NOTE]
> Za detaljnije informacije o korišćenju Prompt flow-a u Azure AI Foundry, možete pogledati [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Izaberite **Chat input**, **Chat output** da omogućite ćaskanje sa vašim modelom.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.sr.png)

1. Sada ste spremni za ćaskanje sa vašim prilagođenim Phi-3 / Phi-3.5 modelom. U narednoj vežbi ćete naučiti kako da pokrenete Prompt flow i koristite ga za ćaskanje sa fino podešenim Phi-3 / Phi-3.5 modelom.

> [!NOTE]
>
> Obnovljeni tok bi trebalo da izgleda kao na slici ispod:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.sr.png)
>

#### Pokrenite Prompt flow

1. Izaberite **Start compute sessions** da pokrenete Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.sr.png)

1. Izaberite **Validate and parse input** da osvežite parametre.

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.sr.png)

1. Izaberite **Value** od **connection** da povežete sa prilagođenom konekcijom koju ste kreirali. Na primer, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.sr.png)

#### Ćaskajte sa vašim prilagođenim Phi-3 / Phi-3.5 modelom

1. Izaberite **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.sr.png)

1. Evo primera rezultata: sada možete da ćaskate sa svojim prilagođenim Phi-3 / Phi-3.5 modelom. Preporučuje se da postavljate pitanja zasnovana na podacima korišćenim za fino podešavanje.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.sr.png)

### Deploy Azure OpenAI za evaluaciju Phi-3 / Phi-3.5 modela

Da biste evaluirali Phi-3 / Phi-3.5 model u Azure AI Foundry, potrebno je da deploy-ujete Azure OpenAI model. Ovaj model će se koristiti za ocenjivanje performansi Phi-3 / Phi-3.5 modela.

#### Deploy Azure OpenAI

1. Prijavite se na [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Idite do Azure AI Foundry projekta koji ste kreirali.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.sr.png)

1. U projektu koji ste kreirali, izaberite **Deployments** sa leve strane taba.

1. Izaberite **+ Deploy model** iz navigacionog menija.

1. Izaberite **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.sr.png)

1. Izaberite Azure OpenAI model koji želite da koristite. Na primer, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.sr.png)

1. Izaberite **Confirm**.

### Evaluirajte fino podešeni Phi-3 / Phi-3.5 model koristeći Prompt flow evaluaciju u Azure AI Foundry

### Pokrenite novu evaluaciju

1. Posetite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Idite do Azure AI Foundry projekta koji ste kreirali.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.sr.png)

1. U projektu koji ste kreirali, izaberite **Evaluation** sa leve strane taba.

1. Izaberite **+ New evaluation** iz navigacionog menija.
![Izaberite evaluaciju.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.sr.png)

1. Izaberite evaluaciju **Prompt flow**.

    ![Izaberite evaluaciju Prompt flow.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.sr.png)

1. izvršite sledeće zadatke:

    - Unesite naziv evaluacije. Mora biti jedinstvena vrednost.
    - Izaberite **Question and answer without context** kao tip zadatka. Zato što dataset **UlTRACHAT_200k** korišćen u ovom tutorijalu ne sadrži kontekst.
    - Izaberite prompt flow koji želite da evaluirate.

    ![Evaluacija prompt flow.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.sr.png)

1. Izaberite **Next**.

1. izvršite sledeće zadatke:

    - Izaberite **Add your dataset** da biste otpremili dataset. Na primer, možete otpremiti test fajl dataset-a, kao što je *test_data.json1*, koji je uključen kada preuzmete dataset **ULTRACHAT_200k**.
    - Izaberite odgovarajuću **Dataset column** koja odgovara vašem dataset-u. Na primer, ako koristite dataset **ULTRACHAT_200k**, izaberite **${data.prompt}** kao kolonu dataset-a.

    ![Evaluacija prompt flow.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.sr.png)

1. Izaberite **Next**.

1. izvršite sledeće zadatke da konfigurišete metrike performansi i kvaliteta:

    - Izaberite metrike performansi i kvaliteta koje želite da koristite.
    - Izaberite Azure OpenAI model koji ste kreirali za evaluaciju. Na primer, izaberite **gpt-4o**.

    ![Evaluacija prompt flow.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.sr.png)

1. izvršite sledeće zadatke da konfigurišete metrike rizika i bezbednosti:

    - Izaberite metrike rizika i bezbednosti koje želite da koristite.
    - Izaberite prag za izračunavanje stope grešaka koji želite da koristite. Na primer, izaberite **Medium**.
    - Za **question**, izaberite **Data source** na **{$data.prompt}**.
    - Za **answer**, izaberite **Data source** na **{$run.outputs.answer}**.
    - Za **ground_truth**, izaberite **Data source** na **{$data.message}**.

    ![Evaluacija prompt flow.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.sr.png)

1. Izaberite **Next**.

1. Izaberite **Submit** da započnete evaluaciju.

1. Evaluacija će potrajati neko vreme. Možete pratiti napredak u tabu **Evaluation**.

### Pregledajte rezultate evaluacije

> [!NOTE]
> Rezultati prikazani ispod služe da ilustruju proces evaluacije. U ovom tutorijalu smo koristili model fino podešen na relativno malom dataset-u, što može dovesti do podoptimalnih rezultata. Stvarni rezultati mogu značajno varirati u zavisnosti od veličine, kvaliteta i raznovrsnosti korišćenog dataset-a, kao i specifične konfiguracije modela.

Kada evaluacija bude završena, možete pregledati rezultate za metrike performansi i bezbednosti.

1. Metrike performansi i kvaliteta:

    - ocenjuju efikasnost modela u generisanju koherentnih, tečnih i relevantnih odgovora.

    ![Rezultat evaluacije.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.sr.png)

1. Metrike rizika i bezbednosti:

    - Osigurajte da su izlazi modela bezbedni i u skladu sa principima Responsible AI, izbegavajući štetan ili uvredljiv sadržaj.

    ![Rezultat evaluacije.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.sr.png)

1. Možete skrolovati nadole da vidite **Detailed metrics result**.

    ![Rezultat evaluacije.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.sr.png)

1. Evaluacijom vašeg prilagođenog Phi-3 / Phi-3.5 modela prema metrike performansi i bezbednosti, možete potvrditi da model nije samo efikasan, već i da se pridržava principa odgovornog AI, čineći ga spremnim za primenu u stvarnom svetu.

## Čestitamo!

### Završili ste ovaj tutorijal

Uspešno ste evaluirali fino podešeni Phi-3 model integrisan sa Prompt flow u Azure AI Foundry. Ovo je važan korak u osiguravanju da vaši AI modeli ne samo da dobro rade, već i da se pridržavaju Microsoft-ovih principa Responsible AI kako biste mogli da gradite pouzdane i sigurne AI aplikacije.

![Arhitektura.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.sr.png)

## Očistite Azure resurse

Očistite vaše Azure resurse kako biste izbegli dodatne troškove na vašem nalogu. Idite na Azure portal i obrišite sledeće resurse:

- Azure Machine learning resurs.
- Azure Machine learning model endpoint.
- Azure AI Foundry Project resurs.
- Azure AI Foundry Prompt flow resurs.

### Sledeći koraci

#### Dokumentacija

- [Procena AI sistema korišćenjem Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluacija i metrike nadzora za generativni AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry dokumentacija](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokumentacija](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Obuka

- [Uvod u Microsoft-ov Responsible AI pristup](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Uvod u Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [Šta je Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Najava novih alata u Azure AI za sigurnije i pouzdanije generativne AI aplikacije](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluacija generativnih AI aplikacija](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетом. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне тумачења настала коришћењем овог превода.