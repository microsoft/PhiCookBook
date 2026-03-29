# Įvertinkite Microsoft Foundry smulkiai sureguliuotą Phi-3 / Phi-3.5 modelį, orientuotą į Microsoft atsakingo dirbtinio intelekto principus

Šis end-to-end (E2E) pavyzdys remiasi Microsoft Tech Community vadovu „[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)“.

## Apžvalga

### Kaip galite įvertinti smulkiai sureguliuoto Phi-3 / Phi-3.5 modelio saugumą ir veikimą Microsoft Foundry aplinkoje?

Modelio smulkus reguliavimas kartais gali sukelti nenumatytų ar nepageidaujamų atsakymų. Siekiant užtikrinti, kad modelis išliktų saugus ir veiksmingas, svarbu įvertinti modelio galimybę generuoti žalingą turinį bei gebėjimą pateikti tikslius, aktualius ir nuoseklius atsakymus. Šiame vadove sužinosite, kaip įvertinti smulkiai suregulioto Phi-3 / Phi-3.5 modelio saugumą ir veikimą, integruotą su Prompt flow Microsoft Foundry aplinkoje.

Čia pateikiamas Microsoft Foundry vertinimo procesas.

![Architecture of tutorial.](../../../../../../translated_images/lt/architecture.10bec55250f5d6a4.webp)

*Vaizdo šaltinis: [Generatyviosios DI programų vertinimas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Daugiau išsamios informacijos ir papildomų išteklių apie Phi-3 / Phi-3.5 rasite adresu [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Reikalavimai

- [Python](https://www.python.org/downloads)
- [Azure prenumerata](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Smulkiai sureguliuotas Phi-3 / Phi-3.5 modelis

### Turinys

1. [**Scenarijus 1: Įvadas į Microsoft Foundry Prompt flow vertinimą**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Įvadas į saugumo vertinimą](#įvadas-į-saugumo-vertinimą)
    - [Įvadas į veikimo vertinimą](#įvadas-į-veikimo-vertinimą)

1. [**Scenarijus 2: Phi-3 / Phi-3.5 modelio vertinimas Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Prieš pradėdami](#prieš-pradėdami)
    - [Diegti Azure OpenAI Phi-3 / Phi-3.5 modelio vertinimui](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Įvertinkite smulkiai sureguliuotą Phi-3 / Phi-3.5 modelį naudojant Microsoft Foundry Prompt flow vertinimą](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Sveikiname!](#sveikiname)

## **Scenarijus 1: Įvadas į Microsoft Foundry Prompt flow vertinimą**

### Įvadas į saugumo vertinimą

Siekiant užtikrinti, kad jūsų DI modelis būtų etiškas ir saugus, labai svarbu jį įvertinti pagal Microsoft atsakingo DI principus. Microsoft Foundry aplinkoje saugumo vertinimai leidžia įvertinti modelio atsparumą jailbreik atakoms ir jo galimą žalingo turinio kūrimo riziką, kuris tiesiogiai atitinka šiuos principus.

![Safaty evaluation.](../../../../../../translated_images/lt/safety-evaluation.083586ec88dfa950.webp)

*Vaizdo šaltinis: [Generatyviosios DI programų vertinimas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft atsakingo DI principai

Prieš pradedant techninius veiksmus, svarbu suprasti Microsoft atsakingo DI principus, tai yra etinis pagrindas, skirtas atsakingam DI sistemų kūrimui, diegimui ir eksploatavimui. Šie principai nukreipia atsakingą DI sistemų dizainą, kūrimą ir diegimą, užtikrindami, kad DI technologijos būtų kuriamos sąžiningai, skaidriai ir įtraukiant visus. Šie principai yra pagrindas vertinant DI modelių saugumą.

Microsoft atsakingo DI principai apima:

- **Sąžiningumą ir įtrauktį**: DI sistemos turėtų elgtis sąžiningai su visais ir vengti skirtingai paveikti panašiose situacijose esančių žmonių grupių. Pavyzdžiui, kai DI sistemos teikia rekomendacijas medicininiam gydymui, paskolų suteikimui ar įdarbinimui, jos turi siūlyti tas pačias rekomendacijas visiems, kurie turi panašius simptomus, finansines aplinkybes ar profesinius įgūdžius.

- **Patikimumą ir saugumą**: Siekiant užtikrinti pasitikėjimą, svarbu, kad DI sistemos veiktų patikimai, saugiai ir nuosekliai. Šios sistemos turi veikti taip, kaip buvo numatytos, saugiai reaguoti į netikėtas situacijas ir būti atsparios kenksmingiems manipuliavimams. Jų elgesys ir gebėjimas susidoroti su įvairiomis sąlygomis atspindi situacijų ir aplinkybių, į kurias projektuotojai atsižvelgė kurdami ir testuodami, spektrą.

- **Skaidrumą**: Kai DI sistemos padeda priimti sprendimus, turinčius didelę įtaką žmonių gyvenimams, svarbu, kad žmonės suprastų, kaip šie sprendimai buvo priimti. Pavyzdžiui, bankas gali naudoti DI sistemą, kad nuspręstų, ar asmuo yra kreditingas. Įmonė gali naudoti DI sistemą atrinkti tinkamiausius kandidatus į darbą.

- **Privatumą ir saugumą**: DI taikymas sparčiai plečiasi, todėl vis labiau svarbu ir sudėtinga apsaugoti privatumą ir asmeninę bei verslo informaciją. DI kontekste privatumas ir duomenų saugumas reikalauja ypatingo dėmesio, nes prieiga prie duomenų reikalinga tiksliai ir informuotai prognozei bei sprendimams priimti.

- **Atsakomybę**: Asmenys, kurie kuria ir diegia DI sistemas, turi būti atsakingi už savo sistemų veikimą. Organizacijos turėtų naudoti industrijos standartus atsakomybės normoms kurti. Šios normos gali užtikrinti, kad DI sistemos nebūtų galutinė autoritetė priimant sprendimus, turinčius įtakos žmonių gyvenimams. Jos taip pat gali garantuoti, kad žmonės išlaikytų prasmingą kontrolę priešingai labai autonomiškoms DI sistemoms.

![Fill hub.](../../../../../../translated_images/lt/responsibleai2.c07ef430113fad8c.webp)

*Vaizdo šaltinis: [Kas yra atsakingas DI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Daugiau sužinoti apie Microsoft atsakingo DI principus galite apsilankę [Kas yra atsakingas DI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Saugumo rodikliai

Šiame vadove įvertinsite smulkiai sureguliuoto Phi-3 modelio saugumą naudodami Microsoft Foundry saugumo rodiklius. Šie rodikliai padeda įvertinti modelio galimybę generuoti žalingą turinį ir jo pažeidžiamumą jailbreik atakoms. Saugumo rodikliai apima:

- **Savarankiškos žalos susijęs turinys**: įvertina, ar modelis linkęs generuoti turinį, susijusį su savęs žalojimu.
- **Neršanti ir neteisinga informacija**: įvertina, ar modelis linkęs kurti neapykantos ar neteisingą turinį.
- **Smurtinis turinys**: įvertina, ar modelis linkęs generuoti smurtinį turinį.
- **Seksualinis turinys**: įvertina, ar modelis linkęs generuoti netinkamą seksualinį turinį.

Šių aspektų vertinimas užtikrina, kad DI modelis nepateiktų žalingo ar įžeidžiančio turinio, atitinkančio visuomenės vertybes ir reglamentus.

![Evaluate based on safety.](../../../../../../translated_images/lt/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Įvadas į veikimo vertinimą

Siekiant užtikrinti, kad jūsų DI modelis veiktų kaip tikėtasi, svarbu įvertinti jo veikimą pagal veiklos rodiklius. Microsoft Foundry aplinkoje veikimo vertinimai leidžia įvertinti modelio efektyvumą generuojant tikslius, aktualius ir nuoseklius atsakymus.

![Safaty evaluation.](../../../../../../translated_images/lt/performance-evaluation.48b3e7e01a098740.webp)

*Vaizdo šaltinis: [Generatyviosios DI programų vertinimas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Veikimo rodikliai

Šiame vadove įvertinsite smulkiai suregulioto Phi-3 / Phi-3.5 modelio veikimą naudodami Microsoft Foundry veikimo rodiklius. Šie rodikliai padės įvertinti modelio efektyvumą generuojant tikslius, aktualius ir nuoseklius atsakymus. Veiklos rodikliai apima:

- **Pagrįstumas**: vertinama, kaip gerai sugeneruoti atsakymai atitinka informaciją iš įvesties šaltinio.
- **Aktualumas**: įvertina sugeneruotų atsakymų tinkamumą pateiktiems klausimams.
- **Nuoseklumas**: vertina, kaip sklandžiai teksto srautas teka, skaitosi natūraliai ir panašiai į žmogaus kalbą.
- **Sklandumas**: vertina sugeneruoto teksto kalbos įgūdžius.
- **GPT panašumas**: lygina sugeneruotą atsakymą su teisingu atsakymu panašumo atžvilgiu.
- **F1 balas**: apskaičiuoja bendrų žodžių dalį tarp sugeneruoto atsakymo ir šaltinio duomenų.

Šie rodikliai padeda įvertinti modelio efektyvumą generuojant tikslius, aktualius ir nuoseklius atsakymus.

![Evaluate based on performance.](../../../../../../translated_images/lt/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenarijus 2: Phi-3 / Phi-3.5 modelio vertinimas Microsoft Foundry**

### Prieš pradėdami

Šis vadovas yra tęsinys ankstesniems tinklaraščio įrašams „[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)“ ir „[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)“. Šiuose įrašuose išsamiai aprašyta Phi-3 / Phi-3.5 modelio smulkiojo reguliavimo procesas Microsoft Foundry ir jo integravimas su Prompt flow.

Šiame vadove diegsite Azure OpenAI modelį vertintojui Microsoft Foundry ir naudositės juo savo smulkiai sureguliuoto Phi-3 / Phi-3.5 modelio vertinimui.

Prieš pradėdami vadovą, įsitikinkite, kad turite šiuos reikalavimus, aprašytus ankstesniuose vadovuose:

1. Paruoštą duomenų rinkinį smulkiai sureguliuoto Phi-3 / Phi-3.5 modelio vertinimui.
1. Smulkiai sureguliuotą Phi-3 / Phi-3.5 modelį, įdiegtą Azure Machine Learning aplinkoje.
1. Prompt flow integruotą su jūsų smulkiai sureguliuotu Phi-3 / Phi-3.5 modeliu Microsoft Foundry aplinkoje.

> [!NOTE]
> Naudosite *test_data.jsonl* failą, esantį duomenų aplanke iš **ULTRACHAT_200k** duomenų rinkinio, atsisiųsto ankstesniuose tinklaraščio įrašuose, kaip duomenų rinkinį smulkiai sureguliuoto Phi-3 / Phi-3.5 modelio vertinimui.

#### Integruokite pasirinktą Phi-3 / Phi-3.5 modelį su Prompt flow Microsoft Foundry (Kodas pirmiausia)

> [!NOTE]
> Jei vykdėte žemo kodo metodą, aprašytą „[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)“, šią užduotį galite praleisti ir tęsti kitą.
> Tačiau jei vykdėte „kodas pirmiausia“ metodą, aprašytą „[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)“ smulkiai reguliuojant ir diegiant savo Phi-3 / Phi-3.5 modelį, procesas, kaip prijungti modelį prie Prompt flow, šiek tiek skiriasi. Šią procedūrą išmoksite šioje užduotyje.

Norėdami tęsti, turite integruoti savo smulkiai sureguliuotą Phi-3 / Phi-3.5 modelį į Prompt flow Microsoft Foundry.

#### Sukurkite Microsoft Foundry Hub

Prieš kuriant projektą, turite sukurti Hub. Hub veikia kaip Resursų Grupė, leidžianti organizuoti ir valdyti kelis projektus Microsoft Foundry aplinkoje.
1. Prisijunkite prie [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Kairiajame skirtuke pasirinkite **All hubs**.

1. Naršymo meniu pasirinkite **+ New hub**.

    ![Create hub.](../../../../../../translated_images/lt/create-hub.5be78fb1e21ffbf1.webp)

1. Atlikite šiuos veiksmus:

    - Įveskite **Hub name**. Jis turi būti unikalus.
    - Pasirinkite savo Azure **Subscription**.
    - Pasirinkite naudoti **Resource group** (jei reikia, sukurkite naują).
    - Pasirinkite pageidaujamą **Location**.
    - Pasirinkite naudoti **Connect Azure AI Services** (jei reikia, sukurkite naują).
    - Pasirinkite **Connect Azure AI Search** ir pažymėkite **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/lt/fill-hub.baaa108495c71e34.webp)

1. Paspauskite **Next**.

#### Sukurti Microsoft Foundry projektą

1. Sukurtame Hub pasirinkite kairiajame skirtuke **All projects**.

1. Naršymo meniu pasirinkite **+ New project**.

    ![Select new project.](../../../../../../translated_images/lt/select-new-project.cd31c0404088d7a3.webp)

1. Įveskite **Project name**. Jis turi būti unikalus.

    ![Create project.](../../../../../../translated_images/lt/create-project.ca3b71298b90e420.webp)

1. Paspauskite **Create a project**.

#### Pridėti pasirinktą ryšį su specialiai paruoštu Phi-3 / Phi-3.5 modeliu

Norėdami integruoti savo pritaikytą Phi-3 / Phi-3.5 modelį su Prompt flow, turite išsaugoti modelio galinį tašką ir raktą kaip pasirinktą ryšį. Šis nustatymas užtikrina prieigą prie jūsų pritaikyto Phi-3 / Phi-3.5 modelio Prompt flow aplinkoje.

#### Nustatyti api raktą ir galinio taško uri specialiai paruoštam Phi-3 / Phi-3.5 modeliui

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Eikite į sukurtą Azure Machine learning darbo sritį.

1. Kairiajame skirtuke pasirinkite **Endpoints**.

    ![Select endpoints.](../../../../../../translated_images/lt/select-endpoints.ee7387ecd68bd18d.webp)

1. Pasirinkite sukurtą galinį tašką.

    ![Select endpoints.](../../../../../../translated_images/lt/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Naršymo meniu pasirinkite **Consume**.

1. Nukopijuokite savo **REST endpoint** ir **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/lt/copy-endpoint-key.0650c3786bd646ab.webp)

#### Pridėti pasirinktą ryšį

1. Apsilankykite [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Eikite į sukurtą Microsoft Foundry projektą.

1. Projekto kairiajame skirtuke pasirinkite **Settings**.

1. Pasirinkite **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/lt/select-new-connection.fa0f35743758a74b.webp)

1. Naršymo meniu pasirinkite **Custom keys**.

    ![Select custom keys.](../../../../../../translated_images/lt/select-custom-keys.5a3c6b25580a9b67.webp)

1. Atlikite šiuos veiksmus:

    - Paspauskite **+ Add key value pairs**.
    - Raktui įveskite **endpoint** ir įklijuokite iš Azure ML Studio nukopijuotą galinį tašką į vertės lauką.
    - Vėl paspauskite **+ Add key value pairs**.
    - Raktui įveskite **key** ir įklijuokite iš Azure ML Studio nukopijuotą raktą į vertės lauką.
    - Po raktų pridėjimo pažymėkite **is secret**, kad raktas nebūtų viešai matomas.

    ![Add connection.](../../../../../../translated_images/lt/add-connection.ac7f5faf8b10b0df.webp)

1. Paspauskite **Add connection**.

#### Sukurti Prompt flow

Pridėjote pasirinktą ryšį Microsoft Foundry. Dabar sukurkime Prompt flow atlikdami šiuos veiksmus. Po to prijungsite šį Prompt flow prie pasirinkto ryšio norėdami naudoti specialiai paruoštą modelį Prompt flow aplinkoje.

1. Eikite į sukurtą Microsoft Foundry projektą.

1. Kairiajame skirtuke pasirinkite **Prompt flow**.

1. Naršymo meniu pasirinkite **+ Create**.

    ![Select Promptflow.](../../../../../../translated_images/lt/select-promptflow.18ff2e61ab9173eb.webp)

1. Naršymo meniu pasirinkite **Chat flow**.

    ![Select chat flow.](../../../../../../translated_images/lt/select-flow-type.28375125ec9996d3.webp)

1. Įveskite norimą **Folder name**.

    ![Select chat flow.](../../../../../../translated_images/lt/enter-name.02ddf8fb840ad430.webp)

1. Paspauskite **Create**.

#### Nustatyti Prompt flow pokalbiui su jūsų pasirinktu Phi-3 / Phi-3.5 modeliu

Jums reikia integruoti specialiai paruoštą Phi-3 / Phi-3.5 modelį į Prompt flow. Tačiau esamas pateiktas Prompt flow nėra sukurtas šiam tikslui, todėl turite perdaryti Prompt flow, kad būtų galima integruoti pasirinktą modelį.

1. Prompt flow atlikite šiuos veiksmus, kad pertvarkytumėte esamą srautą:

    - Pasirinkite **Raw file mode**.
    - Ištrinkite visą esamą kodą faile *flow.dag.yml*.
    - Pridėkite šį kodą į *flow.dag.yml*.

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

    - Paspauskite **Save**.

    ![Select raw file mode.](../../../../../../translated_images/lt/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Pridėkite šį kodą faile *integrate_with_promptflow.py*, kad naudotumėte pasirinktą Phi-3 / Phi-3.5 modelį Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Žurnalo nustatymas
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

        # "connection" yra individualaus ryšio pavadinimas, "endpoint", "key" yra raktai individualiame ryšyje
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
            
            # Užfiksuoti visą JSON atsakymą
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

    ![Paste prompt flow code.](../../../../../../translated_images/lt/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Daugiau informacijos apie Prompt flow naudojimą Microsoft Foundry rasite čia: [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pasirinkite **Chat input**, **Chat output**, kad įgalintumėte pokalbį su savo modeliu.

    ![Select Input Output.](../../../../../../translated_images/lt/select-input-output.c187fc58f25fbfc3.webp)

1. Dabar esate pasiruošę bendrauti su savo specialiai paruoštu Phi-3 / Phi-3.5 modeliu. Kitame pratime išmoksite, kaip paleisti Prompt flow ir naudoti jį pokalbiui su modeliu.

> [!NOTE]
>
> Išdėstytas srautas turėtų atrodyti kaip paveikslėlyje:
>
> ![Flow example](../../../../../../translated_images/lt/graph-example.82fd1bcdd3fc545b.webp)
>

#### Paleisti Prompt flow

1. Paspauskite **Start compute sessions**, kad paleistumėte Prompt flow.

    ![Start compute session.](../../../../../../translated_images/lt/start-compute-session.9acd8cbbd2c43df1.webp)

1. Paspauskite **Validate and parse input**, kad atnaujintumėte parametrus.

    ![Validate input.](../../../../../../translated_images/lt/validate-input.c1adb9543c6495be.webp)

1. Pasirinkite **Value** lauką prie **connection** ir pasirinkite sukurtą pasirinktą ryšį, pvz., *connection*.

    ![Connection.](../../../../../../translated_images/lt/select-connection.1f2b59222bcaafef.webp)

#### Bendrauti su savo pasirinktu Phi-3 / Phi-3.5 modeliu

1. Paspauskite **Chat**.

    ![Select chat.](../../../../../../translated_images/lt/select-chat.0406bd9687d0c49d.webp)

1. Štai pavyzdys, kaip atrodo rezultatai: dabar galite bendrauti su savo pasirinktu Phi-3 / Phi-3.5 modeliu. Rekomenduojama užduoti klausimus remiantis duomenimis, naudotais modeliui tobulinti.

    ![Chat with prompt flow.](../../../../../../translated_images/lt/chat-with-promptflow.1cf8cea112359ada.webp)

### Diegti Azure OpenAI, kad įvertintumėte Phi-3 / Phi-3.5 modelį

Norėdami įvertinti Phi-3 / Phi-3.5 modelį Microsoft Foundry, turite įdiegti Azure OpenAI modelį. Šis modelis bus naudojamas Phi-3 / Phi-3.5 modelio našumo vertinimui.

#### Diegti Azure OpenAI

1. Prisijunkite prie [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Eikite į sukurtą Microsoft Foundry projektą.

    ![Select Project.](../../../../../../translated_images/lt/select-project-created.5221e0e403e2c9d6.webp)

1. Projekto kairiajame skirtuke pasirinkite **Deployments**.

1. Naršymo meniu pasirinkite **+ Deploy model**.

1. Pasirinkite **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/lt/deploy-openai-model.95d812346b25834b.webp)

1. Pasirinkite norimą naudoti Azure OpenAI modelį, pvz., **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/lt/select-openai-model.959496d7e311546d.webp)

1. Paspauskite **Confirm**.

### Įvertinti specialiai paruoštą Phi-3 / Phi-3.5 modelį naudojant Microsoft Foundry Prompt flow vertinimą

### Pradėti naują vertinimą

1. Apsilankykite [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Eikite į sukurtą Microsoft Foundry projektą.

    ![Select Project.](../../../../../../translated_images/lt/select-project-created.5221e0e403e2c9d6.webp)

1. Projekto kairiajame skirtuke pasirinkite **Evaluation**.

1. Naršymo meniu pasirinkite **+ New evaluation**.

    ![Select evaluation.](../../../../../../translated_images/lt/select-evaluation.2846ad7aaaca7f4f.webp)

1. Pasirinkite **Prompt flow** vertinimą.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/lt/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Atlikite šiuos veiksmus:

    - Įveskite vertinimo pavadinimą. Jis turi būti unikalus.
    - Pasirinkite **Question and answer without context** kaip užduoties tipą, nes **UlTRACHAT_200k** duomenų rinkinys šiame vadove neturi konteksto.
    - Pasirinkite norimą vertinti prompt flow.

    ![Prompt flow evaluation.](../../../../../../translated_images/lt/evaluation-setting1.4aa08259ff7a536e.webp)

1. Paspauskite **Next**.

1. Atlikite šiuos veiksmus:

    - Paspauskite **Add your dataset**, kad įkeltumėte duomenų rinkinį. Pvz., galite įkelti testavimo duomenų failą, pvz., *test_data.json1*, kuris įtrauktas atsisiunčiant **ULTRACHAT_200k** duomenų rinkinį.
    - Pasirinkite tinkamą **Dataset column**, atitinkančią jūsų duomenis. Pvz., jei naudojate **ULTRACHAT_200k**, pasirinkite **${data.prompt}** kaip duomenų stulpelį.

    ![Prompt flow evaluation.](../../../../../../translated_images/lt/evaluation-setting2.07036831ba58d64e.webp)

1. Paspauskite **Next**.

1. Atlikite šiuos veiksmus konfiguracijai pagal našumo ir kokybės matavimus:

    - Pasirinkite našumo ir kokybės metrikas, kurias norite naudoti.
    - Pasirinkite Azure OpenAI modelį, sukurtą vertinimui. Pvz., pasirinkite **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/lt/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Atlikite šiuos veiksmus rizikos ir saugumo matavimų konfigūracijai:

    - Pasirinkite rizikos ir saugumo metrikas, kurias norite naudoti.
    - Pasirinkite ribinę vertę defektų normos skaičiavimui. Pvz., pasirinkite **Medium**.
    - Už **question** nustatykite **Data source** kaip **{$data.prompt}**.
    - Už **answer** nustatykite **Data source** kaip **{$run.outputs.answer}**.
    - Už **ground_truth** nustatykite **Data source** kaip **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/lt/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Paspauskite **Next**.

1. Paspauskite **Submit**, kad pradėtumėte vertinimą.

1. Vertinimas užtruks šiek tiek laiko. Progresą galite stebėti skirtuke **Evaluation**.

### Peržiūrėti vertinimo rezultatus

> [!NOTE]
> Žemiau pateikti rezultatai yra skirti iliustruoti vertinimo procesą. Šiame vadove naudotas modelis buvo paruoštas naudojant palyginti nedidelį duomenų rinkinį, todėl rezultatai gali būti neoptimalūs. Tikrieji rezultatai gali ženkliai skirtis priklausomai nuo duomenų rinkinio dydžio, kokybės, įvairovės ir modelio specifinės konfigūracijos.

Baigus vertinimą, galite peržiūrėti rezultatus tiek našumo, tiek saugumo matavimams.
1. Veiklos ir kokybės rodikliai:

    - įvertinkite modelio efektyvumą generuojant nuoseklias, sklandžias ir aktualias atsakymus.

    ![Įvertinimo rezultatas.](../../../../../../translated_images/lt/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Rizikos ir saugumo rodikliai:

    - Užtikrinkite, kad modelio rezultatai būtų saugūs ir atitiktų Atsakingo AI principus, vengiant žalingo ar įžeidžiančio turinio.

    ![Įvertinimo rezultatas.](../../../../../../translated_images/lt/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Galite slinkti žemyn, kad peržiūrėtumėte **Išsamių rodiklių rezultatą**.

    ![Įvertinimo rezultatas.](../../../../../../translated_images/lt/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Vertindami savo tinkintą Phi-3 / Phi-3.5 modelį pagal tiek veiklos, tiek saugumo rodiklius, galite patvirtinti, kad modelis yra ne tik efektyvus, bet ir laikosi atsakingo AI praktikų, todėl yra pasirengęs realiam naudojimui.

## Sveikiname!

### Jūs baigėte šią pamoką

Sėkmingai įvertinote patobulintą Phi-3 modelį, integruotą su Prompt flow Microsoft Foundry platformoje. Tai svarbus žingsnis siekiant užtikrinti, kad jūsų AI modeliai ne tik gerai veiktų, bet ir atitiktų Microsoft Atsakingo AI principus, padedančius kurti patikimas ir patikimas AI programas.

![Architektūra.](../../../../../../translated_images/lt/architecture.10bec55250f5d6a4.webp)

## Išvalykite Azure išteklius

Išvalykite savo Azure išteklius, kad išvengtumėte papildomų sąskaitos mokesčių. Eikite į Azure portalą ir ištrinkite šiuos išteklius:

- Azure Machine Learning išteklius.
- Azure Machine Learning modelio galinį tašką.
- Microsoft Foundry projekto išteklius.
- Microsoft Foundry Prompt flow išteklius.

### Tolimesni žingsniai

#### Dokumentacija

- [Įvertinkite AI sistemas naudodami Atsakingo AI informacijos suvestinę](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Generatyvaus AI vertinimo ir stebėjimo rodikliai](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry dokumentacija](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokumentacija](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Mokymo turinys

- [Įvadas į Microsoft Atsakingo AI požiūrį](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Įvadas į Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Nuorodos

- [Kas yra Atsakingas AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Pranešimas apie naujus Azure AI įrankius, padedančius kurti saugesnes ir patikimesnes generatyvaus AI programas](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Generatyvaus AI programų įvertinimas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turi būti laikomas teisėtu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->