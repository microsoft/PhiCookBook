# Hinnake Microsoft Foundry's peenhäälestatud Phi-3 / Phi-3.5 mudelit, keskendudes Microsofti vastutustundliku tehisintellekti põhimõtetele

See lõpp-punktist-lõppu (E2E) näidis põhineb Microsoft Tech Community juhendil "[Hinnake peenhäälestatud Phi-3 / 3.5 mudeleid Microsoft Foundry's, keskendudes Microsofti vastutustundlikule tehisintellektile](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)".

## Ülevaade

### Kuidas hinnata peenhäälestatud Phi-3 / Phi-3.5 mudeli ohutust ja jõudlust Microsoft Foundry's?

Mudeli peenhäälestamine võib mõnikord viia soovimatute või ootamatute vastusteni. Selleks, et tagada mudeli ohutus ja tõhusus, on oluline hinnata mudeli potentsiaali toota kahjulikku sisu ning selle võimekust pakkuda täpseid, asjakohaseid ja sidusaid vastuseid. Selles juhendis õpite, kuidas hinnata peenhäälestatud Phi-3 / Phi-3.5 mudeli ohutust ja jõudlust, mis on integreeritud Prompt flow'sse Microsoft Foundry's.

Siin on Microsoft Foundry hindamisprotsess.

![Architecture of tutorial.](../../../../../../translated_images/et/architecture.10bec55250f5d6a4.webp)

*Pildiallikas: [Generatiivse tehisintellekti rakenduste hindamine](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Täpsema info ja lisavahendite jaoks Phi-3 / Phi-3.5 kohta külastage palun [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Nõuded

- [Python](https://www.python.org/downloads)
- [Azure tellimus](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Peenhäälestatud Phi-3 / Phi-3.5 mudel

### Sisukord

1. [**Stsenaarium 1: Sissejuhatus Microsoft Foundry's Prompt flow hindamisse**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Sissejuhatus ohutuse hindamisse](#sissejuhatus-ohutuse-hindamisse)
    - [Sissejuhatus jõudluse hindamisse](#sissejuhatus-jõudluse-hindamisse)

1. [**Stsenaarium 2: Phi-3 / Phi-3.5 mudeli hindamine Microsoft Foundry's**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Enne alustamist](#enne-alustamist)
    - [Azure OpenAI juurutamine Phi-3 / Phi-3.5 mudeli hindamiseks](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamine Microsoft Foundry's Prompt flow hindamise kaudu](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Õnnitleme!](#palju-õnne)

## **Stsenaarium 1: Sissejuhatus Microsoft Foundry's Prompt flow hindamisse**

### Sissejuhatus ohutuse hindamisse

Selleks, et teie tehisintellekti mudel oleks eetiline ja ohutu, on oluline hinnata seda Microsofti vastutustundliku AI põhimõtete vastu. Microsoft Foundry's võimaldavad ohutuse hindamised hinnata teie mudeli haavatavust jailbreak-rünnakute suhtes ja potentsiaali toota kahjulikku sisu, mis on otseselt kooskõlas nende põhimõtetega.

![Safaty evaluation.](../../../../../../translated_images/et/safety-evaluation.083586ec88dfa950.webp)

*Pildiallikas: [Generatiivse tehisintellekti rakenduste hindamine](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofti vastutustundliku AI põhimõtted

Enne tehniliste sammude alustamist on oluline mõista Microsofti vastutustundliku AI põhimõtteid, mis on eetiline raamistik AI süsteemide vastutustundlikuks arendamiseks, juurutamiseks ja toimimiseks. Need põhimõtted juhivad AI süsteemide vastutustundlikku projekteerimist, arendamist ja juurutamist, tagades, et AI tehnoloogiad on loodud õiglaselt, läbipaistvalt ja kaasavalt. Need põhimõtted on aluseks AI mudelite ohutuse hindamisele.

Microsofti vastutustundliku AI põhimõtted hõlmavad:

- **Õiglus ja kaasatus**: AI süsteemid peaksid kohtlema kõiki õiglaselt ega tohi erineval moel mõjutada sarnases olukorras olevaid inimrühmi. Näiteks kui AI süsteemid annavad juhiseid meditsiinilise ravi, laenutaotluste või töötamise kohta, peaksid nad kõigile, kellel on sarnased sümptomid, finantsolukord või kutseoskused, pakkuma samu soovitusi.

- **Usaldusväärsus ja ohutus**: Usalduse loomiseks on oluline, et AI süsteemid töötaksid usaldusväärselt, ohutult ja järjepidevalt. Need süsteemid peaksid suudama toimida vastavalt oma algsele kavandile, reageerima ohutult ootamatutele olukordadele ning vastu seisma kahjulikele manipulatsioonidele. Nende käitumine ja võimekuse ulatus peegeldavad olukordi ja tingimusi, mida arendajad kavandasid disaini- ja testimisetappidel.

- **Läbipaistvus**: Kui AI süsteemid aitavad kaasa otsustele, millel on inimeste elule suured mõjud, on oluline, et inimesed mõistaksid, kuidas need otsused tehti. Näiteks võib pank kasutada AI süsteemi, et otsustada, kas inimene on krediidivõimeline. Ettevõte võib kasutada AI süsteemi, et määrata sobivaimad tööle kandideerijad.

- **Privaatsus ja turvalisus**: AI laiemaks levikuks muutub privaatsuse kaitse ja isiku- ning ärilise teabe turvalisus üha olulisemaks ja keerulisemaks. AI puhul nõuab privaatsus ja andmete turvalisus erilist tähelepanu, kuna juurdepääs andmetele on AI süsteemide täpsete ja teadlike prognooside ning otsuste tegemiseks inimestega seotud küsimustes hädavajalik.

- **Vastutustundlikkus**: Isikud, kes kavandavad ja juurutavad AI süsteeme, peavad olema vastutavad oma süsteemide toimimise eest. Organisatsioonid peaksid tuginema tööstusharu standarditele, et välja töötada vastutustundlikkuse norme. Need normid võivad tagada, et AI süsteemid ei ole lõplik autoriteet ühegi otsuse puhul, mis mõjutab inimeste elu. Nad tagavad ka selle, et inimesed hoiaksid olulist kontrolli kõrge autonoomiaga AI süsteemide üle.

![Fill hub.](../../../../../../translated_images/et/responsibleai2.c07ef430113fad8c.webp)

*Pildiallikas: [Mis on vastutustundlik AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsofti vastutustundlike AI põhimõtete kohta lisateabe saamiseks külastage lehte [Mis on vastutustundlik AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Ohutusmõõdikud

Selles juhendis hindate peenhäälestatud Phi-3 mudeli ohutust Microsoft Foundry's oleva ohutusmõõdikute abil. Need mõõdikud aitavad hinnata mudeli potentsiaali toota kahjulikku sisu ja selle haavatavust jailbreak-rünnakute suhtes. Ohutusmõõdikud hõlmavad:

- **Enesevigastusega seotud sisu**: Hinnatakse, kas mudel kipub tootma enesevigastusega seotud sisu.
- **Vihkava ja ebaõiglase sisu**: Hinnatakse, kas mudel kipub tootma vihkavat või ebaõiglase sisuga sisu.
- **Vägivaldne sisu**: Hinnatakse, kas mudel kipub tootma vägivaldset sisu.
- **Seksuaalne sisu**: Hinnatakse, kas mudel kipub tootma sobimatut seksuaalset sisu.

Nende aspektide hindamine tagab, et AI mudel ei tooda kahjulikku ega solvavat sisu, hoides kooskõlas ühiskondlike väärtuste ja regulatiivsete normidega.

![Evaluate based on safety.](../../../../../../translated_images/et/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Sissejuhatus jõudluse hindamisse

Selleks, et tagada AI mudeli oodatud jõudlus, on oluline hinnata seda jõudlusmõõdikute alusel. Microsoft Foundry's võimaldavad jõudluse hindamised hinnata mudeli efektiivsust pakkuda täpseid, asjakohaseid ja sidusaid vastuseid.

![Safaty evaluation.](../../../../../../translated_images/et/performance-evaluation.48b3e7e01a098740.webp)

*Pildiallikas: [Generatiivse tehisintellekti rakenduste hindamine](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Jõudlusmõõdikud

Selles juhendis hindate peenhäälestatud Phi-3 / Phi-3.5 mudeli jõudlust Microsoft Foundry's oleva jõudlusmõõdikute abil. Need mõõdikud aitavad hinnata mudeli efektiivsust täpsete, asjakohaste ja sidusate vastuste loomisel. Jõudlusmõõdikud hõlmavad:

- **Tuginevus**: Hinnatakse, kui hästi genereeritud vastused vastavad sisendi allikast pärinevale teabele.
- **Asjakohasus**: Hinnatakse genereeritud vastuste olulisust esitatud küsimustele.
- **Sidusus**: Hinnatakse, kui sujuvalt genereeritud tekst kulgeb, loeb loomulikult ja meenutab inimkeelt.
- **Ladinaoskus**: Hinnatakse genereeritud teksti keeleosavust.
- **GPT sarnasuse**: Võrdleb genereeritud vastust tõese põhivastusega sarnasuse osas.
- **F1 skoor**: Arvutab genereeritud vastuse ja lähteandmete vahel jagatud sõnade suhte.

Need mõõdikud aitavad teil hinnata mudeli efektiivsust täpsete, asjakohaste ja sidusate vastuste genereerimisel.

![Evaluate based on performance.](../../../../../../translated_images/et/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Stsenaarium 2: Phi-3 / Phi-3.5 mudeli hindamine Microsoft Foundry's**

### Enne alustamist

See juhend on jätk eelnevatele blogipostitustele, "[Peenhäälestage ja integreerige kohandatud Phi-3 mudelid Prompt Flow’ga: Samm-sammult juhend](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ja "[Peenhäälestage ja integreerige kohandatud Phi-3 mudelid Prompt Flow's Microsoft Foundry's](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)". Nendes postitustes juhendasime teid Phi-3 / Phi-3.5 mudeli peenhäälestamise protsessis Microsoft Foundry's ning selle integreerimisel Prompt flow'sse.

Selles juhendis juurutate Azure OpenAI mudeli hindajana Microsoft Foundry's ning kasutate seda oma peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamiseks.

Enne selle juhendi alustamist veenduge, et teil on järgmised eeltingimused, nagu kirjeldatud eelnevates juhendites:

1. Valmis andmekogu peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamiseks.
1. Phi-3 / Phi-3.5 mudel, mis on peenhäälestatud ja juurutatud Azure Machine Learning'i.
1. Prompt flow, mis on integreeritud teie peenhäälestatud Phi-3 / Phi-3.5 mudeliga Microsoft Foundry's.

> [!NOTE]
> Kasutate *test_data.jsonl* faili, mis asub eelnevates blogipostitustes alla laaditud **ULTRACHAT_200k** andmekogu andmekataloogis, andmekoguna peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamiseks.

#### Kohandatud Phi-3 / Phi-3.5 mudeli integreerimine Prompt flow'sse Microsoft Foundry's (esimesena koodipõhine lähenemine)

> [!NOTE]
> Kui järgsite madala koodiga lähenemist, mis on kirjeldatud juhendis "[Peenhäälestage ja integreerige kohandatud Phi-3 mudelid Prompt Flow's Microsoft Foundry's](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", võite selle harjutuse vahele jätta ja edasi minna järgmise juurde.
> Kui aga kasutasite esimesena koodipõhist lähenemist, mis on kirjeldatud juhendis "[Peenhäälestage ja integreerige kohandatud Phi-3 mudelid Prompt Flow'ga: Samm-sammult juhend](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)", et peenhäälestada ja juurutada oma Phi-3 / Phi-3.5 mudel, siis mudeli ühendamise protsess Prompt flow'ga on veidi erinev. Õpite selle protsessi selles harjutuses.

Jätkamiseks peate integreerima oma peenhäälestatud Phi-3 / Phi-3.5 mudeli Prompt flow'sse Microsoft Foundry's.

#### Looge Microsoft Foundry Hub

Enne projekti loomist peate looma Hubi. Hub toimib nagu Ressursigrupp, võimaldades teil organiseerida ja hallata mitut projekti Microsoft Foundry's.
1. Logi sisse aadressil [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Vali vasakpoolsest vahekaardist **Kõik keskused**.

1. Vali navigeerimismenüüst **+ Uus keskus**.

    ![Loo keskus.](../../../../../../translated_images/et/create-hub.5be78fb1e21ffbf1.webp)

1. Täida järgmised tegevused:

    - Sisesta **Keskuse nimi**. See peab olema unikaalne väärtus.
    - Vali oma Azure **Tellimus**.
    - Vali kasutatav **Resursside grupp** (loo uus vajadusel).
    - Vali kasutatav **Asukoht**.
    - Vali kasutamiseks **Ühenda Azure AI teenustega** (loo uus vajadusel).
    - Vali **Ühenda Azure AI otsinguga** ja vali **Jäta ühendamata**.

    ![Täida keskus.](../../../../../../translated_images/et/fill-hub.baaa108495c71e34.webp)

1. Vali **Järgmine**.

#### Loo Microsoft Foundry projekt

1. Vali loodud keskuses vasakult **Kõik projektid**.

1. Vali navigeerimismenüüst **+ Uus projekt**.

    ![Vali uus projekt.](../../../../../../translated_images/et/select-new-project.cd31c0404088d7a3.webp)

1. Sisesta **Projekti nimi**. See peab olema unikaalne väärtus.

    ![Loo projekt.](../../../../../../translated_images/et/create-project.ca3b71298b90e420.webp)

1. Vali **Loo projekt**.

#### Lisa kohandatud ühendus peenhäälestatud Phi-3 / Phi-3.5 mudelile

Et integreerida oma kohandatud Phi-3 / Phi-3.5 mudelit Prompt flow’ga, tuleb mudeli lõpp-punkt ja võti salvestada kohandatud ühendusse. See seadistus tagab ligipääsu teie kohandatud Phi-3 / Phi-3.5 mudelile Prompt flow’s.

#### Määra peenhäälestatud Phi-3 / Phi-3.5 mudeli api võti ja lõpp-punkti uri

1. Külastage [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Liigu loodud Azure Machine learning tööruumi.

1. Vali vasakul vahekaardilt **Lõpp-punktid**.

    ![Vali lõpp-punktid.](../../../../../../translated_images/et/select-endpoints.ee7387ecd68bd18d.webp)

1. Vali loodud lõpp-punkt.

    ![Vali loodud lõpp-punkt.](../../../../../../translated_images/et/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Vali navigeerimismenüüst **Kasutamine**.

1. Kopeeri oma **REST lõpp-punkt** ja **Põhivõti**.

    ![Kopeeri api võti ja lõpp-punkt.](../../../../../../translated_images/et/copy-endpoint-key.0650c3786bd646ab.webp)

#### Lisa kohandatud ühendus

1. Külastage aadressi [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Liigu loodud Microsoft Foundry projekti.

1. Projekti sees vali vasaku vahekaardi alt **Seaded**.

1. Vali **+ Uus ühendus**.

    ![Vali uus ühendus.](../../../../../../translated_images/et/select-new-connection.fa0f35743758a74b.webp)

1. Vali navigeerimismenüüst **Kohandatud võtmed**.

    ![Vali kohandatud võtmed.](../../../../../../translated_images/et/select-custom-keys.5a3c6b25580a9b67.webp)

1. Tee järgmised toimingud:

    - Vali **+ Lisa võtme-väärtuse paarid**.
    - Võtme nimeks sisesta **endpoint** ning kleebi Azure ML Studiost kopeeritud lõpp-punkt väärtuse lahtrisse.
    - Vali uuesti **+ Lisa võtme-väärtuse paarid**.
    - Võtme nimeks sisesta **key** ning kleebi Azure ML Studiost kopeeritud võti väärtuse lahtrisse.
    - Pärast võtmete lisamist märgi **on salajane**, et võti ei oleks nähtav.

    ![Lisa ühendus.](../../../../../../translated_images/et/add-connection.ac7f5faf8b10b0df.webp)

1. Vali **Lisa ühendus**.

#### Loo Prompt flow

Oled lisanud Microsoft Foundrys kohandatud ühenduse. Järgmiseks loo Prompt flow järgmiste sammudega. Seejärel ühendad selle Prompt flow kohandatud ühendusega, et kasutada peenhäälestatud mudelit Prompt flow’s.

1. Liigu loodud Microsoft Foundry projekti.

1. Vali vasakult vahekaardilt **Prompt flow**.

1. Vali navigeerimismenüüst **+ Loo**.

    ![Vali Promptflow.](../../../../../../translated_images/et/select-promptflow.18ff2e61ab9173eb.webp)

1. Vali navigeerimismenüüst **Vestluse voog**.

    ![Vali vestluse voog.](../../../../../../translated_images/et/select-flow-type.28375125ec9996d3.webp)

1. Sisesta kasutatav **Kausta nimi**.

    ![Sisesta nimi.](../../../../../../translated_images/et/enter-name.02ddf8fb840ad430.webp)

1. Vali **Loo**.

#### Seadista Prompt flow vestluseks oma kohandatud Phi-3 / Phi-3.5 mudeliga

Pead integreerima peenhäälestatud Phi-3 / Phi-3.5 mudeli Prompt flow’sse. Eksisteeriv Prompt flow ei ole selleks otstarbeks kavandatud, seega pead ümber kujundama Prompt flow, et lubada kohandatud mudeli kasutamist.

1. Prompt flow’s täida järgmised toimingud, et olemasolev voog uuesti üles ehitada:

    - Vali **Toorna faili režiim**.
    - Kustuta kogu olemasolev kood failist *flow.dag.yml*.
    - Lisa alljärgnev kood faili *flow.dag.yml*.

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

    - Vali **Salvesta**.

    ![Vali toorna faili režiim.](../../../../../../translated_images/et/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Lisa järgmine kood faili *integrate_with_promptflow.py*, et kasutada kohandatud Phi-3 / Phi-3.5 mudelit Prompt flow’s.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logimise seadistamine
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

        # "connection" on Kohandatud Ühenduse nimi, "endpoint", "key" on võtmed Kohandatud Ühenduses
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
            
            # Logi täis JSON vastus
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

    ![Kleebi prompt flow kood.](../../../../../../translated_images/et/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Täpsema info saamiseks Prompt flow kasutamise kohta Microsoft Foundrys, vaata [Prompt flow Microsoft Foundrys](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vali **Vestluse sisend**, **Vestluse väljund**, et võimaldada vestlus mudeliga.

    ![Vali sisend ja väljund.](../../../../../../translated_images/et/select-input-output.c187fc58f25fbfc3.webp)

1. Nüüd oled valmis vestlema oma kohandatud Phi-3 / Phi-3.5 mudeliga. Järgmises harjutuses õpid, kuidas alustada Prompt flow’d ja seda kasutada vestluseks peenhäälestatud Phi-3 / Phi-3.5 mudeliga.

> [!NOTE]
>
> Ümber ehitatud voog peaks välja nägema järgmiselt:
>
> ![Voo näide](../../../../../../translated_images/et/graph-example.82fd1bcdd3fc545b.webp)
>

#### Käivita Prompt flow

1. Vali **Alusta arvutussessioone**, et alustad Prompt flow’d.

    ![Alusta arvutussessiooni.](../../../../../../translated_images/et/start-compute-session.9acd8cbbd2c43df1.webp)

1. Vali **Kinnita ja parsi sisend**, et uuendada parameetreid.

    ![Kinnita sisend.](../../../../../../translated_images/et/validate-input.c1adb9543c6495be.webp)

1. Vali **ühenduse** väärtus, mis viitab loodud kohandatud ühendusele. Näiteks *connection*.

    ![Ühendus.](../../../../../../translated_images/et/select-connection.1f2b59222bcaafef.webp)

#### Vestle oma kohandatud Phi-3 / Phi-3.5 mudeliga

1. Vali **Vestlus**.

    ![Vali vestlus.](../../../../../../translated_images/et/select-chat.0406bd9687d0c49d.webp)

1. Siin on tulemustest näide: nüüd saad vestelda oma kohandatud Phi-3 / Phi-3.5 mudeliga. Soovitatav on esitada küsimusi, mis põhinevad peenhäälestuseks kasutatud andmetel.

    ![Vestlus prompt flow’ga.](../../../../../../translated_images/et/chat-with-promptflow.1cf8cea112359ada.webp)

### Juhi läbi Azure OpenAI kasutuselevõtt Phi-3 / Phi-3.5 mudeli hindamiseks

Phi-3 / Phi-3.5 mudeli hindamiseks Microsoft Foundrys tuleb juurutada Azure OpenAI mudel. Seda mudelit kasutatakse Phi-3 / Phi-3.5 mudeli jõudluse hindamiseks.

#### Juuruta Azure OpenAI

1. Logi sisse aadressil [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Liigu loodud Microsoft Foundry projekti.

    ![Vali projekt.](../../../../../../translated_images/et/select-project-created.5221e0e403e2c9d6.webp)

1. Projekti sisse vali vasakult vahekaardilt **Juurutused**.

1. Vali navigeerimismenüüst **+ Juuruta mudel**.

1. Vali **Juuruta baas-mudel**.

    ![Vali juurutused.](../../../../../../translated_images/et/deploy-openai-model.95d812346b25834b.webp)

1. Vali kasutatav Azure OpenAI mudel. Näiteks **gpt-4o**.

    ![Vali soovitud Azure OpenAI mudel.](../../../../../../translated_images/et/select-openai-model.959496d7e311546d.webp)

1. Vali **Kinnita**.

### Hinda peenhäälestatud Phi-3 / Phi-3.5 mudelit Microsoft Foundry Prompt flow hindamise abil

### Alusta uut hindamist

1. Külastage aadressi [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Liigu loodud Microsoft Foundry projekti.

    ![Vali projekt.](../../../../../../translated_images/et/select-project-created.5221e0e403e2c9d6.webp)

1. Projekti sees vali vasakul vahekaart **Hindamine**.

1. Vali navigeerimismenüüst **+ Uus hindamine**.

    ![Vali hindamine.](../../../../../../translated_images/et/select-evaluation.2846ad7aaaca7f4f.webp)

1. Vali hindamiseks **Prompt flow** hindamine.

    ![Vali Prompt flow hindamine.](../../../../../../translated_images/et/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Täida järgmised toimingud:

    - Sisesta hindamise nimi. See peab olema unikaalne väärtus.
    - Vali ülesande tüübiks **Küsimus ja vastus ilma kontekstita**, sest selles juhendis kasutatav **ULTRACHAT_200k** andmekogum ei sisalda konteksti.
    - Vali hindamiseks sobiv prompt flow.

    ![Prompt flow hindamine.](../../../../../../translated_images/et/evaluation-setting1.4aa08259ff7a536e.webp)

1. Vali **Järgmine**.

1. Täida järgmised toimingud:

    - Vali **Lisa oma andmekogu**, et üles laadida andmekogu. Näiteks üles laadida testandmestikuna fail *test_data.json1*, mis on kaasas **ULTRACHAT_200k** andmekoguga.
    - Vali sobiv **Andmekogu veerg**, mis vastab sinu andmekogule. Näiteks ULTRACHAT_200k kasutamiseks vali **${data.prompt}** andmekogu veeruks.

    ![Prompt flow hindamine.](../../../../../../translated_images/et/evaluation-setting2.07036831ba58d64e.webp)

1. Vali **Järgmine**.

1. Tee tulemuste ja kvaliteedi mõõdikute seadistused:

    - Vali kasutamiseks sobivad jõudluse ja kvaliteedi mõõdikud.
    - Vali hindamiseks loodud Azure OpenAI mudel. Näiteks **gpt-4o**.

    ![Prompt flow hindamine.](../../../../../../translated_images/et/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Tee riskide ja turvalisuse mõõdikute seadistused:

    - Vali kasutamiseks sobivad riskide ja turvalisuse mõõdikud.
    - Vali defektimäära arvutamiseks sobiv lävi. Näiteks **Keskmine**.
    - Küsimuse puhul vali **Andmeallikas** väärtuseks **{$data.prompt}**.
    - Vastuse puhul vali **Andmeallikas** väärtuseks **{$run.outputs.answer}**.
    - Tõeväärtuse puhul vali **Andmeallikas** väärtuseks **{$data.message}**.

    ![Prompt flow hindamine.](../../../../../../translated_images/et/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Vali **Järgmine**.

1. Vali **Esita**, et alustada hindamist.

1. Hindamine võtab aega. Edusamme näed vahekaardil **Hindamine**.

### Jälgi hindamistulemusi

> [!NOTE]
> Järgnevalt toodud tulemused on illustratiivse tähendusega hindamisprotsessi tutvustamiseks. Selles juhendis kasutatud mudel on peenhäälestatud suhteliselt väikesele andmekogule, mis võib põhjustada suboptimaalseid tulemusi. Tegelikud tulemused võivad oluliselt varieeruda sõltuvalt kasutatud andmekogu mahust, kvaliteedist, mitmekesisusest ja mudeli konkreetsetest seadistustest.

Kui hindamine on lõpetatud, saad vaadata tulemusi nii jõudluse kui ka turvalisuse mõõdikute osas.
1. Tulemuslikkuse ja kvaliteedi mõõdikud:

    - hinnake mudeli tõhusust sidusate, sujuvate ja asjakohaste vastuste genereerimisel.

    ![Evaluation result.](../../../../../../translated_images/et/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Riskide ja ohutuse mõõdikud:

    - Tagage, et mudeli väljundid on ohutud ja vastavad Vastutustundliku Tehisintellekti põhimõtetele, vältides kahjulikke või solvangulisi sisusid.

    ![Evaluation result.](../../../../../../translated_images/et/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Võite kerida alla, et vaadata **Üksikasjalikke mõõdikute tulemusi**.

    ![Evaluation result.](../../../../../../translated_images/et/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Oma kohandatud Phi-3 / Phi-3.5 mudeli hindamisega nii tulemuslikkuse kui ka ohutuse mõõdikute alusel saate kinnitada, et mudel ei ole mitte ainult tõhus, vaid järgib ka vastutustundliku tehisintellekti praktikaid, muutes selle valmis reaalseks kasutuselevõtuks.

## Palju õnne!

### Olete selle juhendi lõpetanud

Olete edukalt hinnanud peenhäälestatud Phi-3 mudelit, mis on integreeritud Prompt flow’ga Microsoft Foundry keskkonnas. See on oluline samm selle tagamiseks, et teie tehisintellekti mudelid mitte ainult ei tööta hästi, vaid järgivad ka Microsofti vastutustundliku AI põhimõtteid, aidates teil luua usaldusväärseid ja töökindlaid tehisintellekti rakendusi.

![Architecture.](../../../../../../translated_images/et/architecture.10bec55250f5d6a4.webp)

## Azure'i ressursside puhastamine

Puhastage oma Azure’i ressursid, et vältida täiendavaid tasusid kontol. Minge Azure’i portaalile ja kustutage järgmised ressursid:

- Azure Machine Learningi ressurss.
- Azure Machine Learningi mudeli lõpp-punkt.
- Microsoft Foundry projekti ressurss.
- Microsoft Foundry Prompt flow ressurss.

### Järgmised sammud

#### Dokumentatsioon

- [AI-süsteemide hindamine Vastutustundliku AI juhtpaneeli abil](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Generatiivse AI hindamis- ja jälgimismõõdikud](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry dokumentatsioon](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokumentatsioon](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Koolitusmaterjalid

- [Sissejuhatus Microsofti Vastutustundliku AI lähenemisviisi](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Sissejuhatus Microsoft Foundry keskkonda](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Viited

- [Mis on Vastutustundlik AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Uute tööriistade väljakuulutamine Azure AI-s, mis aitavad teil luua turvalisemaid ja usaldusväärsemaid generatiivse AI rakendusi](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Generatiivsete AI rakenduste hindamine](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, olge teadlikud, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument oma emakeeles on käsitletav autoriteetse allikana. Olulise info puhul soovitatakse kasutada professionaalse inimese tõlget. Me ei vastuta käesoleva tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->