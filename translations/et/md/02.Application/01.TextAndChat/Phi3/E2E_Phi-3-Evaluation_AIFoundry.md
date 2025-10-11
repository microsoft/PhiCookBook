<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-10-11T12:08:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "et"
}
-->
# Hinnake Azure AI Foundry's peenhäälestatud Phi-3 / Phi-3.5 mudelit, keskendudes Microsofti vastutustundliku AI põhimõtetele

See otsast lõpuni (E2E) näidis põhineb juhendil "[Hinnake peenhäälestatud Phi-3 / 3.5 mudeleid Azure AI Foundry's, keskendudes Microsofti vastutustundlikule AI-le](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" Microsoft Tech Community'st.

## Ülevaade

### Kuidas hinnata peenhäälestatud Phi-3 / Phi-3.5 mudeli ohutust ja jõudlust Azure AI Foundry's?

Mudeli peenhäälestamine võib mõnikord viia soovimatute või ootamatute vastusteni. Selleks, et mudel jääks ohutuks ja tõhusaks, on oluline hinnata mudeli potentsiaali luua kahjulikku sisu ning tema võimet toota täpseid, asjakohaseid ja sidusaid vastuseid. Selles juhendis õpid, kuidas hinnata peenhäälestatud Phi-3 / Phi-3.5 mudeli ohutust ja jõudlust, mis on integreeritud Azure AI Foundry'sse koos Prompt flow'ga.

Siin on Azure AI Foundry hindamisprotsess.

![Juhendi arhitektuur.](../../../../../../imgs/02/Evaluation-AIFoundry/architecture.png)

*Pildi allikas: [Generatiivse AI rakenduste hindamine](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Täpsema teabe ja lisamaterjalide uurimiseks Phi-3 / Phi-3.5 kohta külastage [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Eeltingimused

- [Python](https://www.python.org/downloads)
- [Azure'i tellimus](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Peenhäälestatud Phi-3 / Phi-3.5 mudel

### Sisukord

1. [**Stsenaarium 1: Azure AI Foundry Prompt flow hindamise tutvustus**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Ohutuse hindamise tutvustus](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Jõudluse hindamise tutvustus](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Stsenaarium 2: Phi-3 / Phi-3.5 mudeli hindamine Azure AI Foundry's**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Enne alustamist](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure OpenAI juurutamine Phi-3 / Phi-3.5 mudeli hindamiseks](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamine Azure AI Foundry Prompt flow hindamise abil](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Palju õnne!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Stsenaarium 1: Azure AI Foundry Prompt flow hindamise tutvustus**

### Ohutuse hindamise tutvustus

Selleks, et teie AI mudel oleks eetiline ja ohutu, on oluline hinnata seda Microsofti vastutustundliku AI põhimõtete alusel. Azure AI Foundry's võimaldavad ohutuse hindamised hinnata mudeli haavatavust jailbreak-rünnakute suhtes ja tema potentsiaali luua kahjulikku sisu, mis on otseselt kooskõlas nende põhimõtetega.

![Ohutuse hindamine.](../../../../../../imgs/02/Evaluation-AIFoundry/safety-evaluation.png)

*Pildi allikas: [Generatiivse AI rakenduste hindamine](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofti vastutustundliku AI põhimõtted

Enne tehniliste sammude alustamist on oluline mõista Microsofti vastutustundliku AI põhimõtteid, mis on eetiline raamistik, mis juhendab AI süsteemide vastutustundlikku arendamist, juurutamist ja kasutamist. Need põhimõtted juhendavad AI süsteemide vastutustundlikku disaini, arendamist ja juurutamist, tagades, et AI tehnoloogiad on loodud viisil, mis on õiglane, läbipaistev ja kaasav. Need põhimõtted on AI mudelite ohutuse hindamise aluseks.

Microsofti vastutustundliku AI põhimõtted hõlmavad:

- **Õiglus ja kaasavus**: AI süsteemid peaksid kohtlema kõiki õiglaselt ja vältima sarnaste gruppide erinevat kohtlemist. Näiteks, kui AI süsteemid annavad juhiseid meditsiinilise ravi, laenutaotluste või töölevõtmise kohta, peaksid nad tegema samad soovitused kõigile, kellel on sarnased sümptomid, finantsolukord või professionaalsed kvalifikatsioonid.

- **Usaldusväärsus ja ohutus**: Usalduse loomiseks on kriitiline, et AI süsteemid töötaksid usaldusväärselt, ohutult ja järjepidevalt. Need süsteemid peaksid olema võimelised toimima nii, nagu nad algselt kavandati, reageerima ohutult ootamatutele tingimustele ja vastu seisma kahjulikule manipuleerimisele. Nende käitumine ja tingimuste mitmekesisus, millega nad toime tulevad, peegeldavad olukordi ja asjaolusid, mida arendajad disaini ja testimise ajal ette nägid.

- **Läbipaistvus**: Kui AI süsteemid aitavad teha otsuseid, millel on suur mõju inimeste eludele, on kriitiline, et inimesed mõistaksid, kuidas need otsused tehti. Näiteks võib pank kasutada AI süsteemi, et otsustada, kas inimene on krediidivõimeline. Ettevõte võib kasutada AI süsteemi, et määrata kõige kvalifitseeritumad kandidaadid tööle.

- **Privaatsus ja turvalisus**: Kuna AI muutub üha levinumaks, muutub privaatsuse kaitsmine ja isikliku ning ärilise teabe turvalisus üha olulisemaks ja keerukamaks. AI-ga nõuab privaatsus ja andmete turvalisus erilist tähelepanu, kuna juurdepääs andmetele on hädavajalik, et AI süsteemid saaksid teha täpseid ja informeeritud ennustusi ning otsuseid inimeste kohta.

- **Vastutus**: Inimesed, kes disainivad ja juurutavad AI süsteeme, peavad olema vastutavad selle eest, kuidas nende süsteemid töötavad. Organisatsioonid peaksid tuginema tööstusstandarditele, et arendada vastutuse norme. Need normid võivad tagada, et AI süsteemid ei ole lõplik autoriteet ühegi otsuse tegemisel, mis mõjutab inimeste elusid. Samuti võivad need tagada, et inimesed säilitavad tähendusliku kontrolli muidu väga autonoomsete AI süsteemide üle.

![Täida hub.](../../../../../../imgs/02/Evaluation-AIFoundry/responsibleai2.png)

*Pildi allikas: [Mis on vastutustundlik AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Lisateabe saamiseks Microsofti vastutustundliku AI põhimõtete kohta külastage [Mis on vastutustundlik AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Ohutuse mõõdikud

Selles juhendis hindate peenhäälestatud Phi-3 mudeli ohutust, kasutades Azure AI Foundry ohutuse mõõdikuid. Need mõõdikud aitavad teil hinnata mudeli potentsiaali luua kahjulikku sisu ja tema haavatavust jailbreak-rünnakute suhtes. Ohutuse mõõdikud hõlmavad:

- **Enesevigastamisega seotud sisu**: Hinnatakse, kas mudelil on kalduvus toota enesevigastamisega seotud sisu.
- **Vihkav ja ebaõiglane sisu**: Hinnatakse, kas mudelil on kalduvus toota vihkavat või ebaõiglast sisu.
- **Vägivaldne sisu**: Hinnatakse, kas mudelil on kalduvus toota vägivaldset sisu.
- **Seksuaalne sisu**: Hinnatakse, kas mudelil on kalduvus toota sobimatut seksuaalset sisu.

Nende aspektide hindamine tagab, et AI mudel ei tooda kahjulikku või solvavat sisu, mis on kooskõlas ühiskondlike väärtuste ja regulatiivsete standarditega.

![Hinda ohutuse alusel.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluate-based-on-safety.png)

### Jõudluse hindamise tutvustus

Selleks, et teie AI mudel töötaks ootuspäraselt, on oluline hinnata selle jõudlust jõudluse mõõdikute alusel. Azure AI Foundry's võimaldavad jõudluse hindamised hinnata mudeli tõhusust täpsete, asjakohaste ja sidusate vastuste genereerimisel.

![Ohutuse hindamine.](../../../../../../imgs/02/Evaluation-AIFoundry/performance-evaluation.png)

*Pildi allikas: [Generatiivse AI rakenduste hindamine](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Jõudluse mõõdikud

Selles juhendis hindate peenhäälestatud Phi-3 / Phi-3.5 mudeli jõudlust, kasutades Azure AI Foundry jõudluse mõõdikuid. Need mõõdikud aitavad teil hinnata mudeli tõhusust täpsete, asjakohaste ja sidusate vastuste genereerimisel. Jõudluse mõõdikud hõlmavad:

- **Põhjendatus**: Hinnatakse, kui hästi genereeritud vastused vastavad sisendi allikast saadud teabele.
- **Asjakohasus**: Hinnatakse genereeritud vastuste olulisust antud küsimuste suhtes.
- **Sidusus**: Hinnatakse, kui sujuvalt genereeritud tekst voolab, loeb loomulikult ja sarnaneb inimkeelele.
- **Soravus**: Hinnatakse genereeritud teksti keelelist oskust.
- **GPT sarnasus**: Võrdleb genereeritud vastust tõese vastusega sarnasuse osas.
- **F1 skoor**: Arvutab jagatud sõnade suhte genereeritud vastuse ja allikandmete vahel.

Need mõõdikud aitavad teil hinnata mudeli tõhusust täpsete, asjakohaste ja sidusate vastuste genereerimisel.

![Hinda jõudluse alusel.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluate-based-on-performance.png)

## **Stsenaarium 2: Phi-3 / Phi-3.5 mudeli hindamine Azure AI Foundry's**

### Enne alustamist

See juhend on jätk varasematele blogipostitustele, "[Peenhäälesta ja integreeri kohandatud Phi-3 mudelid Prompt flow'ga: samm-sammuline juhend](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ja "[Peenhäälesta ja integreeri kohandatud Phi-3 mudelid Prompt flow'ga Azure AI Foundry's](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Nendes postitustes käisime läbi Phi-3 / Phi-3.5 mudeli peenhäälestamise protsessi Azure AI Foundry's ja selle integreerimise Prompt flow'ga.

Selles juhendis juurutate Azure OpenAI mudeli hindajana Azure AI Foundry's ja kasutate seda oma peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamiseks.

Enne selle juhendi alustamist veenduge, et teil on järgmised eeltingimused, nagu kirjeldatud varasemates juhendites:

1. Valmistatud andmestik peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamiseks.
1. Phi-3 / Phi-3.5 mudel, mis on peenhäälestatud ja juurutatud Azure Machine Learning'usse.
1. Prompt flow, mis on integreeritud teie peenhäälestatud Phi-3 / Phi-3.5 mudeliga Azure AI Foundry's.

> [!NOTE]
> Kasutate *test_data.jsonl* faili, mis asub andmekaustas **ULTRACHAT_200k** andmestikust, mis laaditi alla varasemates blogipostitustes, peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamiseks.

#### Kohandatud Phi-3 / Phi-3.5 mudeli integreerimine Prompt flow'ga Azure AI Foundry's (koodipõhine lähenemine)

> [!NOTE]
> Kui järgite madala koodi lähenemist, nagu kirjeldatud "[Peenhäälesta ja integreeri kohandatud Phi-3 mudelid Prompt flow'ga Azure AI Foundry's](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", võite selle harjutuse vahele jätta ja liikuda järgmise juurde.
> Kui aga järgite koodipõhist lähenemist, nagu kirjeldatud "[Peenhäälesta ja integreeri kohandatud Phi-3 mudelid Prompt flow'ga: samm-sammuline juhend](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)", et peenhäälestada ja juurutada oma Phi-3 / Phi-3.5 mudel, on protsess mudeli ühendamiseks Prompt flow'ga veidi erinev. Õpite seda protsessi selles harjutuses.

Jätkamiseks peate integreerima oma peenhäälestatud Phi-3 / Phi-3.5 mudeli Prompt flow'ga Azure AI Foundry's.

#### Azure AI Foundry Hubi loomine

Enne projekti loomist peate looma Hubi. Hub toimib nagu ressursigrupp, võimaldades teil korraldada ja hallata mitut projekti Azure AI Foundry's.

1. Logige sisse [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Valige vasakpoolsest menüüst **Kõik hubid**.

1. Valige navigeerimismenüüst **+ Uus hub**.

    ![Loo hub.](../../../../../../imgs/02/Evaluation-AIFoundry/create-hub.png)
1. Tehke järgmised toimingud:

    - Sisestage **Hubi nimi**. See peab olema unikaalne väärtus.
    - Valige oma Azure'i **Tellijaplaan**.
    - Valige kasutatav **Ressursigrupp** (vajadusel looge uus).
    - Valige **Asukoht**, mida soovite kasutada.
    - Valige **Ühendage Azure AI teenused**, mida soovite kasutada (vajadusel looge uus).
    - Valige **Ühendage Azure AI otsing** ja **Jätke ühendamata**.

    ![Täida hub.](../../../../../../imgs/02/Evaluation-AIFoundry/fill-hub.png)

1. Valige **Järgmine**.

#### Azure AI Foundry projekti loomine

1. Hubis, mille te lõite, valige vasakult külgribalt **Kõik projektid**.

1. Valige navigeerimismenüüst **+ Uus projekt**.

    ![Valige uus projekt.](../../../../../../imgs/03/AIFoundry/select-new-project.png)

1. Sisestage **Projekti nimi**. See peab olema unikaalne väärtus.

    ![Loo projekt.](../../../../../../imgs/03/AIFoundry/create-project.png)

1. Valige **Loo projekt**.

#### Kohandatud ühenduse lisamine peenhäälestatud Phi-3 / Phi-3.5 mudeli jaoks

Et integreerida oma kohandatud Phi-3 / Phi-3.5 mudel Prompt flow'ga, peate salvestama mudeli lõpp-punkti ja võtme kohandatud ühendusse. See seadistus tagab juurdepääsu teie kohandatud Phi-3 / Phi-3.5 mudelile Prompt flow's.

#### Peenhäälestatud Phi-3 / Phi-3.5 mudeli API võtme ja lõpp-punkti URI seadistamine

1. Külastage [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigeerige loodud Azure Machine Learning tööruumi.

1. Valige vasakult külgribalt **Lõpp-punktid**.

    ![Valige lõpp-punktid.](../../../../../../imgs/02/Evaluation-AIFoundry/select-endpoints.png)

1. Valige loodud lõpp-punkt.

    ![Valige loodud lõpp-punkt.](../../../../../../imgs/02/Evaluation-AIFoundry/select-endpoint-created.png)

1. Valige navigeerimismenüüst **Kasutamine**.

1. Kopeerige oma **REST lõpp-punkt** ja **Primaarne võti**.

    ![Kopeeri API võti ja lõpp-punkti URI.](../../../../../../imgs/02/Evaluation-AIFoundry/copy-endpoint-key.png)

#### Kohandatud ühenduse lisamine

1. Külastage [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeerige loodud Azure AI Foundry projekti.

1. Projektis, mille te lõite, valige vasakult külgribalt **Seaded**.

1. Valige **+ Uus ühendus**.

    ![Valige uus ühendus.](../../../../../../imgs/02/Evaluation-AIFoundry/select-new-connection.png)

1. Valige navigeerimismenüüst **Kohandatud võtmed**.

    ![Valige kohandatud võtmed.](../../../../../../imgs/02/Evaluation-AIFoundry/select-custom-keys.png)

1. Tehke järgmised toimingud:

    - Valige **+ Lisa võtme-väärtuse paarid**.
    - Sisestage võtme nimeks **endpoint** ja kleepige Azure ML Studio'st kopeeritud lõpp-punkt väärtuse väljale.
    - Valige uuesti **+ Lisa võtme-väärtuse paarid**.
    - Sisestage võtme nimeks **key** ja kleepige Azure ML Studio'st kopeeritud võti väärtuse väljale.
    - Pärast võtmete lisamist valige **on salajane**, et vältida võtme avalikustamist.

    ![Lisa ühendus.](../../../../../../imgs/02/Evaluation-AIFoundry/add-connection.png)

1. Valige **Lisa ühendus**.

#### Prompt flow loomine

Olete lisanud kohandatud ühenduse Azure AI Foundry's. Nüüd loome Prompt flow järgmiste sammude abil. Seejärel ühendate selle Prompt flow kohandatud ühendusega, et kasutada peenhäälestatud mudelit Prompt flow's.

1. Navigeerige loodud Azure AI Foundry projekti.

1. Valige vasakult külgribalt **Prompt flow**.

1. Valige navigeerimismenüüst **+ Loo**.

    ![Valige Promptflow.](../../../../../../imgs/02/Evaluation-AIFoundry/select-promptflow.png)

1. Valige navigeerimismenüüst **Vestlusvoog**.

    ![Valige vestlusvoog.](../../../../../../imgs/02/Evaluation-AIFoundry/select-flow-type.png)

1. Sisestage kasutatav **Kausta nimi**.

    ![Sisestage vestlusvoo nimi.](../../../../../../imgs/02/Evaluation-AIFoundry/enter-name.png)

1. Valige **Loo**.

#### Prompt flow seadistamine vestlemiseks kohandatud Phi-3 / Phi-3.5 mudeliga

Peate integreerima peenhäälestatud Phi-3 / Phi-3.5 mudeli Prompt flow'sse. Kuid olemasolev Prompt flow ei ole selleks otstarbeks loodud. Seetõttu peate Prompt flow ümber kujundama, et võimaldada kohandatud mudeli integreerimist.

1. Prompt flow's tehke järgmised toimingud, et olemasolev voog ümber ehitada:

    - Valige **Toorfaili režiim**.
    - Kustutage kõik olemasolevad koodid *flow.dag.yml* failist.
    - Lisage järgmine kood *flow.dag.yml* faili.

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

    - Valige **Salvesta**.

    ![Valige toorfaili režiim.](../../../../../../imgs/02/Evaluation-AIFoundry/select-raw-file-mode.png)

1. Lisage järgmine kood *integrate_with_promptflow.py* faili, et kasutada kohandatud Phi-3 / Phi-3.5 mudelit Prompt flow's.

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

    ![Kleepige Prompt flow kood.](../../../../../../imgs/02/Evaluation-AIFoundry/paste-promptflow-code.png)

> [!NOTE]
> Täpsema teabe saamiseks Prompt flow kasutamise kohta Azure AI Foundry's, vaadake [Prompt flow Azure AI Foundry's](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Valige **Vestluse sisend**, **Vestluse väljund**, et võimaldada vestlust oma mudeliga.

    ![Valige sisend ja väljund.](../../../../../../imgs/02/Evaluation-AIFoundry/select-input-output.png)

1. Nüüd olete valmis vestlema oma kohandatud Phi-3 / Phi-3.5 mudeliga. Järgmises harjutuses õpite, kuidas Prompt flow käivitada ja seda kasutada vestlemiseks peenhäälestatud Phi-3 / Phi-3.5 mudeliga.

> [!NOTE]
>
> Ümber ehitatud voog peaks välja nägema nagu alloleval pildil:
>
> ![Voo näide](../../../../../../imgs/02/Evaluation-AIFoundry/graph-example.png)
>

#### Prompt flow käivitamine

1. Valige **Käivita arvutusseansid**, et Prompt flow käivitada.

    ![Käivita arvutusseanss.](../../../../../../imgs/02/Evaluation-AIFoundry/start-compute-session.png)

1. Valige **Valideeri ja parsi sisend**, et uuendada parameetreid.

    ![Valideeri sisend.](../../../../../../imgs/02/Evaluation-AIFoundry/validate-input.png)

1. Valige **Ühenduse** väärtus kohandatud ühendusele, mille te lõite. Näiteks *connection*.

    ![Ühendus.](../../../../../../imgs/02/Evaluation-AIFoundry/select-connection.png)

#### Vestlus kohandatud Phi-3 / Phi-3.5 mudeliga

1. Valige **Vestlus**.

    ![Valige vestlus.](../../../../../../imgs/02/Evaluation-AIFoundry/select-chat.png)

1. Näide tulemustest: Nüüd saate vestelda oma kohandatud Phi-3 / Phi-3.5 mudeliga. Soovitatav on esitada küsimusi andmete põhjal, mida kasutati peenhäälestamiseks.

    ![Vestlus Prompt flow'ga.](../../../../../../imgs/02/Evaluation-AIFoundry/chat-with-promptflow.png)

### Azure OpenAI juurutamine Phi-3 / Phi-3.5 mudeli hindamiseks

Phi-3 / Phi-3.5 mudeli hindamiseks Azure AI Foundry's peate juurutama Azure OpenAI mudeli. Seda mudelit kasutatakse Phi-3 / Phi-3.5 mudeli jõudluse hindamiseks.

#### Azure OpenAI juurutamine

1. Logige sisse [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeerige loodud Azure AI Foundry projekti.

    ![Valige projekt.](../../../../../../imgs/02/Evaluation-AIFoundry/select-project-created.png)

1. Projektis, mille te lõite, valige vasakult külgribalt **Juurutused**.

1. Valige navigeerimismenüüst **+ Juuruta mudel**.

1. Valige **Juuruta baas-mudel**.

    ![Valige juurutused.](../../../../../../imgs/02/Evaluation-AIFoundry/deploy-openai-model.png)

1. Valige Azure OpenAI mudel, mida soovite kasutada. Näiteks **gpt-4o**.

    ![Valige Azure OpenAI mudel, mida soovite kasutada.](../../../../../../imgs/02/Evaluation-AIFoundry/select-openai-model.png)

1. Valige **Kinnita**.

### Peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamine Azure AI Foundry Prompt flow hindamise abil

### Uue hindamise alustamine

1. Külastage [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeerige loodud Azure AI Foundry projekti.

    ![Valige projekt.](../../../../../../imgs/02/Evaluation-AIFoundry/select-project-created.png)

1. Projektis, mille te lõite, valige vasakult külgribalt **Hindamine**.

1. Valige navigeerimismenüüst **+ Uus hindamine**.

    ![Valige hindamine.](../../../../../../imgs/02/Evaluation-AIFoundry/select-evaluation.png)

1. Valige **Prompt flow** hindamine.

    ![Valige Prompt flow hindamine.](../../../../../../imgs/02/Evaluation-AIFoundry/promptflow-evaluation.png)

1. Tehke järgmised toimingud:

    - Sisestage hindamise nimi. See peab olema unikaalne väärtus.
    - Valige ülesande tüübiks **Küsimus ja vastus ilma kontekstita**. Seda seetõttu, et **UlTRACHAT_200k** andmestik, mida selles juhendis kasutatakse, ei sisalda konteksti.
    - Valige Prompt flow, mida soovite hinnata.

    ![Prompt flow hindamine.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting1.png)

1. Valige **Järgmine**.

1. Tehke järgmised toimingud:

    - Valige **Lisa oma andmestik**, et üles laadida andmestik. Näiteks saate üles laadida testandmestiku faili, nagu *test_data.json1*, mis on kaasas **ULTRACHAT_200k** andmestiku allalaadimisel.
    - Valige sobiv **Andmestiku veerg**, mis vastab teie andmestikule. Näiteks, kui kasutate **ULTRACHAT_200k** andmestikku, valige **${data.prompt}** andmestiku veeruks.

    ![Prompt flow hindamine.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting2.png)

1. Valige **Järgmine**.

1. Tehke järgmised toimingud, et seadistada jõudluse ja kvaliteedi mõõdikud:

    - Valige jõudluse ja kvaliteedi mõõdikud, mida soovite kasutada.
    - Valige Azure OpenAI mudel, mille te hindamiseks lõite. Näiteks valige **gpt-4o**.

    ![Prompt flow hindamine.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting3-1.png)

1. Tehke järgmised toimingud, et seadistada riskide ja ohutuse mõõdikud:

    - Valige riskide ja ohutuse mõõdikud, mida soovite kasutada.
    - Valige defektide määra arvutamiseks kasutatav lävi. Näiteks valige **Keskmine**.
    - **Küsimuse** jaoks valige **Andmeallikas** väärtuseks **{$data.prompt}**.
    - **Vastuse** jaoks valige **Andmeallikas** väärtuseks **{$run.outputs.answer}**.
    - **Tõeväärtuse** jaoks valige **Andmeallikas** väärtuseks **{$data.message}**.

    ![Prompt flow hindamine.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting3-2.png)

1. Valige **Järgmine**.

1. Valige **Esita**, et hindamist alustada.

1. Hindamine võtab aega. Saate jälgida edenemist **Hindamise** vahekaardil.

### Hindamistulemuste ülevaatamine

> [!NOTE]
> Allpool esitatud tulemused on mõeldud hindamisprotsessi illustreerimiseks. Selles juhendis oleme kasutanud mudelit, mis on peenhäälestatud suhteliselt väikese andmestiku põhjal, mis võib viia mitteoptimaalsete tulemusteni. Tegelikud tulemused võivad oluliselt erineda sõltuvalt kasutatud andmestiku suurusest, kvaliteedist ja mitmekesisusest, samuti mudeli spetsiifilisest konfiguratsioonist.

Kui hindamine on lõpule viidud, saate üle vaadata tulemused nii jõudluse kui ka ohutuse mõõdikute osas.

1. Jõudluse ja kvaliteedi mõõdikud:

    - Hinnake mudeli tõhusust sidusate, ladusate ja asjakohaste vastuste genereerimisel.

    ![Hindamistulemus.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-result-gpu.png)

1. Riskide ja ohutuse mõõdikud:
- Veendu, et mudeli väljundid oleksid turvalised ja vastaksid vastutustundliku tehisintellekti põhimõtetele, vältides kahjulikku või solvavat sisu.

![Hindamistulemus.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-result-gpu-2.png)

1. Saate alla kerida, et vaadata **Üksikasjalikke mõõdikute tulemusi**.

![Hindamistulemus.](../../../../../../imgs/02/Evaluation-AIFoundry/detailed-metrics-result.png)

1. Hinnates oma kohandatud Phi-3 / Phi-3.5 mudelit nii jõudluse kui ka turvalisuse mõõdikute alusel, saate kinnitada, et mudel on mitte ainult tõhus, vaid järgib ka vastutustundliku tehisintellekti praktikaid, muutes selle valmis reaalseks kasutamiseks.

## Palju õnne!

### Olete selle juhendi lõpetanud

Olete edukalt hinnanud peenhäälestatud Phi-3 mudelit, mis on integreeritud Prompt flow'ga Azure AI Foundry's. See on oluline samm, et tagada teie tehisintellekti mudelite mitte ainult hea jõudlus, vaid ka vastavus Microsofti vastutustundliku tehisintellekti põhimõtetele, aidates teil luua usaldusväärseid ja töökindlaid tehisintellekti rakendusi.

![Arhitektuur.](../../../../../../imgs/02/Evaluation-AIFoundry/architecture.png)

## Azure'i ressursside puhastamine

Puhastage oma Azure'i ressursid, et vältida täiendavaid kulusid teie kontole. Minge Azure'i portaali ja kustutage järgmised ressursid:

- Azure Machine Learning ressurss.
- Azure Machine Learning mudeli lõpp-punkt.
- Azure AI Foundry projekti ressurss.
- Azure AI Foundry Prompt flow ressurss.

### Järgmised sammud

#### Dokumentatsioon

- [Tehisintellekti süsteemide hindamine vastutustundliku tehisintellekti armatuurlaua abil](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Generatiivse tehisintellekti hindamise ja jälgimise mõõdikud](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry dokumentatsioon](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokumentatsioon](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Koolitusmaterjalid

- [Sissejuhatus Microsofti vastutustundliku tehisintellekti lähenemisviisi](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Sissejuhatus Azure AI Foundry'sse](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Viited

- [Mis on vastutustundlik tehisintellekt?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Uute tööriistade tutvustamine Azure AI-s, mis aitavad teil luua turvalisemaid ja usaldusväärsemaid generatiivse tehisintellekti rakendusi](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Generatiivse tehisintellekti rakenduste hindamine](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.