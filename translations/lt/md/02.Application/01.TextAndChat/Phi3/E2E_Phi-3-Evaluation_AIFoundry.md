<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-09-12T14:29:52+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "lt"
}
-->
# Įvertinkite pritaikytą Phi-3 / Phi-3.5 modelį Azure AI Foundry, laikydamiesi Microsoft atsakingo dirbtinio intelekto principų

Šis nuo pradžios iki pabaigos (E2E) pavyzdys yra pagrįstas vadovu "[Įvertinkite pritaikytus Phi-3 / 3.5 modelius Azure AI Foundry, laikydamiesi Microsoft atsakingo dirbtinio intelekto principų](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" iš Microsoft Tech Community.

## Apžvalga

### Kaip įvertinti pritaikyto Phi-3 / Phi-3.5 modelio saugumą ir našumą Azure AI Foundry?

Modelio pritaikymas kartais gali sukelti netikėtus ar nepageidaujamus atsakymus. Siekiant užtikrinti, kad modelis išliktų saugus ir efektyvus, svarbu įvertinti jo potencialą generuoti žalingą turinį bei gebėjimą pateikti tikslius, aktualius ir nuoseklius atsakymus. Šiame vadove sužinosite, kaip įvertinti pritaikyto Phi-3 / Phi-3.5 modelio saugumą ir našumą, integruotą su Prompt flow Azure AI Foundry.

Štai Azure AI Foundry vertinimo procesas.

![Pamokos architektūra.](../../../../../../imgs/02/Evaluation-AIFoundry/architecture.png)

*Vaizdo šaltinis: [Generatyvaus dirbtinio intelekto programų vertinimas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Daugiau informacijos ir papildomų išteklių apie Phi-3 / Phi-3.5 rasite [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Reikalingi įrankiai

- [Python](https://www.python.org/downloads)
- [Azure prenumerata](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Pritaikytas Phi-3 / Phi-3.5 modelis

### Turinys

1. [**Scenarijus 1: Azure AI Foundry Prompt flow vertinimo įvadas**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Saugumo vertinimo įvadas](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Našumo vertinimo įvadas](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenarijus 2: Phi-3 / Phi-3.5 modelio vertinimas Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Prieš pradedant](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure OpenAI diegimas Phi-3 / Phi-3.5 modelio vertinimui](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pritaikyto Phi-3 / Phi-3.5 modelio vertinimas naudojant Azure AI Foundry Prompt flow vertinimą](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Sveikiname!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenarijus 1: Azure AI Foundry Prompt flow vertinimo įvadas**

### Saugumo vertinimo įvadas

Siekiant užtikrinti, kad jūsų AI modelis būtų etiškas ir saugus, būtina jį įvertinti pagal Microsoft atsakingo dirbtinio intelekto principus. Azure AI Foundry saugumo vertinimai leidžia įvertinti modelio pažeidžiamumą jailbreak atakoms ir jo potencialą generuoti žalingą turinį, kas tiesiogiai atitinka šiuos principus.

![Saugumo vertinimas.](../../../../../../imgs/02/Evaluation-AIFoundry/safety-evaluation.png)

*Vaizdo šaltinis: [Generatyvaus dirbtinio intelekto programų vertinimas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft atsakingo dirbtinio intelekto principai

Prieš pradedant techninius žingsnius, svarbu suprasti Microsoft atsakingo dirbtinio intelekto principus – etinį pagrindą, skirtą atsakingam AI sistemų kūrimui, diegimui ir veikimui. Šie principai užtikrina, kad AI technologijos būtų kuriamos sąžiningai, skaidriai ir įtraukiai. Jie yra pagrindas AI modelių saugumo vertinimui.

Microsoft atsakingo dirbtinio intelekto principai apima:

- **Sąžiningumą ir įtraukimą**: AI sistemos turėtų elgtis sąžiningai su visais ir vengti skirtingo poveikio panašiai situacijose esančioms žmonių grupėms. Pavyzdžiui, kai AI sistemos teikia rekomendacijas dėl medicininio gydymo, paskolų paraiškų ar darbo, jos turėtų pateikti tas pačias rekomendacijas visiems, turintiems panašius simptomus, finansines aplinkybes ar profesinę kvalifikaciją.

- **Patikimumą ir saugumą**: Siekiant sukurti pasitikėjimą, svarbu, kad AI sistemos veiktų patikimai, saugiai ir nuosekliai. Šios sistemos turėtų veikti taip, kaip buvo suprojektuotos, saugiai reaguoti į nenumatytas sąlygas ir atsispirti žalingam manipuliavimui. Jų elgesys ir sąlygų įvairovė, kurias jos gali valdyti, atspindi situacijų ir aplinkybių, kurias kūrėjai numatė projektavimo ir testavimo metu, spektrą.

- **Skaidrumą**: Kai AI sistemos padeda priimti sprendimus, turinčius didelį poveikį žmonių gyvenimams, svarbu, kad žmonės suprastų, kaip tie sprendimai buvo priimti. Pavyzdžiui, bankas gali naudoti AI sistemą, kad nuspręstų, ar asmuo yra kreditingas. Įmonė gali naudoti AI sistemą, kad nustatytų tinkamiausius kandidatus į darbą.

- **Privatumą ir saugumą**: Kadangi AI tampa vis labiau paplitęs, privatumo apsauga ir asmeninės bei verslo informacijos saugumas tampa vis svarbesni ir sudėtingesni. Naudojant AI, privatumas ir duomenų saugumas reikalauja ypatingo dėmesio, nes prieiga prie duomenų yra būtina, kad AI sistemos galėtų tiksliai ir informuotai prognozuoti bei priimti sprendimus apie žmones.

- **Atsakomybę**: Žmonės, kurie kuria ir diegia AI sistemas, turi būti atsakingi už tai, kaip jų sistemos veikia. Organizacijos turėtų remtis pramonės standartais, kad sukurtų atsakomybės normas. Šios normos gali užtikrinti, kad AI sistemos nebūtų galutinis autoritetas priimant sprendimus, kurie turi įtakos žmonių gyvenimams. Jos taip pat gali užtikrinti, kad žmonės išlaikytų prasmingą kontrolę prieš labai autonomines AI sistemas.

![Atsakingo dirbtinio intelekto centras.](../../../../../../imgs/02/Evaluation-AIFoundry/responsibleai2.png)

*Vaizdo šaltinis: [Kas yra atsakingas dirbtinis intelektas?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Norėdami sužinoti daugiau apie Microsoft atsakingo dirbtinio intelekto principus, apsilankykite [Kas yra atsakingas dirbtinis intelektas?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Saugumo metrikos

Šiame vadove jūs įvertinsite pritaikyto Phi-3 modelio saugumą naudodami Azure AI Foundry saugumo metrikas. Šios metrikos padeda įvertinti modelio potencialą generuoti žalingą turinį ir jo pažeidžiamumą jailbreak atakoms. Saugumo metrikos apima:

- **Turinys, susijęs su savęs žalojimu**: Įvertina, ar modelis turi tendenciją generuoti turinį, susijusį su savęs žalojimu.
- **Neapykantos ir nesąžiningas turinys**: Įvertina, ar modelis turi tendenciją generuoti neapykantos ar nesąžiningą turinį.
- **Smurtinis turinys**: Įvertina, ar modelis turi tendenciją generuoti smurtinį turinį.
- **Seksualinis turinys**: Įvertina, ar modelis turi tendenciją generuoti netinkamą seksualinį turinį.

Šių aspektų vertinimas užtikrina, kad AI modelis negeneruotų žalingo ar įžeidžiančio turinio, atitinkančio visuomenės vertybes ir reguliavimo standartus.

![Vertinimas pagal saugumą.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluate-based-on-safety.png)

### Našumo vertinimo įvadas

Siekiant užtikrinti, kad jūsų AI modelis veiktų taip, kaip tikimasi, svarbu įvertinti jo našumą pagal našumo metrikas. Azure AI Foundry našumo vertinimai leidžia įvertinti modelio efektyvumą generuojant tikslius, aktualius ir nuoseklius atsakymus.

![Našumo vertinimas.](../../../../../../imgs/02/Evaluation-AIFoundry/performance-evaluation.png)

*Vaizdo šaltinis: [Generatyvaus dirbtinio intelekto programų vertinimas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Našumo metrikos

Šiame vadove jūs įvertinsite pritaikyto Phi-3 / Phi-3.5 modelio našumą naudodami Azure AI Foundry našumo metrikas. Šios metrikos padeda įvertinti modelio efektyvumą generuojant tikslius, aktualius ir nuoseklius atsakymus. Našumo metrikos apima:

- **Pagrįstumas**: Įvertina, kaip gerai generuoti atsakymai atitinka informaciją iš įvesties šaltinio.
- **Aktualumas**: Įvertina generuotų atsakymų tinkamumą pateiktiems klausimams.
- **Nuoseklumas**: Įvertina, kaip sklandžiai generuotas tekstas teka, skamba natūraliai ir primena žmogaus kalbą.
- **Sklandumas**: Įvertina generuoto teksto kalbos įgūdžius.
- **GPT panašumas**: Palygina generuotą atsakymą su pagrindine tiesa dėl panašumo.
- **F1 balas**: Apskaičiuoja bendrų žodžių santykį tarp generuoto atsakymo ir šaltinio duomenų.

Šios metrikos padeda įvertinti modelio efektyvumą generuojant tikslius, aktualius ir nuoseklius atsakymus.

![Vertinimas pagal našumą.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluate-based-on-performance.png)

## **Scenarijus 2: Phi-3 / Phi-3.5 modelio vertinimas Azure AI Foundry**

### Prieš pradedant

Šis vadovas yra tęsinys ankstesnių tinklaraščio įrašų "[Pritaikykite ir integruokite pritaikytus Phi-3 modelius su Prompt Flow: žingsnis po žingsnio vadovas](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ir "[Pritaikykite ir integruokite pritaikytus Phi-3 modelius su Prompt Flow Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Šiuose įrašuose aptarėme Phi-3 / Phi-3.5 modelio pritaikymo procesą Azure AI Foundry ir jo integravimą su Prompt flow.

Šiame vadove jūs diegsite Azure OpenAI modelį kaip vertintoją Azure AI Foundry ir naudosite jį pritaikyto Phi-3 / Phi-3.5 modelio vertinimui.

Prieš pradedant šį vadovą, įsitikinkite, kad turite šiuos reikalavimus, kaip aprašyta ankstesniuose vadovuose:

1. Paruoštą duomenų rinkinį pritaikyto Phi-3 / Phi-3.5 modelio vertinimui.
1. Phi-3 / Phi-3.5 modelį, kuris buvo pritaikytas ir įdiegtas Azure Machine Learning.
1. Prompt flow, integruotą su jūsų pritaikytu Phi-3 / Phi-3.5 modeliu Azure AI Foundry.

> [!NOTE]
> Jūs naudosite *test_data.jsonl* failą, esantį duomenų aplanke iš **ULTRACHAT_200k** duomenų rinkinio, atsisiųsto ankstesniuose tinklaraščio įrašuose, kaip duomenų rinkinį pritaikyto Phi-3 / Phi-3.5 modelio vertinimui.

#### Integruokite pritaikytą Phi-3 / Phi-3.5 modelį su Prompt flow Azure AI Foundry (kodo pirmasis požiūris)
> [!NOTE]  
> Jei laikėtės mažo kodo metodo, aprašyto "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", galite praleisti šią užduotį ir pereiti prie kitos.  
> Tačiau, jei naudojotės kodo pirmumo metodu, aprašytu "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)", kad pritaikytumėte ir įdiegtumėte savo Phi-3 / Phi-3.5 modelį, modelio prijungimo prie Prompt Flow procesas šiek tiek skiriasi. Šioje užduotyje išmoksite šį procesą.
### Integruokite savo pritaikytą Phi-3 / Phi-3.5 modelį į Prompt flow Azure AI Foundry platformoje.

#### Sukurkite Azure AI Foundry Hub

Prieš kuriant projektą, reikia sukurti Hub. Hub veikia kaip resursų grupė, leidžianti organizuoti ir valdyti kelis projektus Azure AI Foundry platformoje.

1. Prisijunkite prie [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pasirinkite **Visi hub'ai** iš kairiojo meniu.

1. Pasirinkite **+ Naujas hub'as** iš navigacijos meniu.

    ![Sukurti hub'ą.](../../../../../../imgs/02/Evaluation-AIFoundry/create-hub.png)

1. Atlikite šiuos veiksmus:

    - Įveskite **Hub'o pavadinimą**. Jis turi būti unikalus.
    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Resursų grupę**, kurią norite naudoti (jei reikia, sukurkite naują).
    - Pasirinkite **Vietą**, kurią norite naudoti.
    - Pasirinkite **Prisijungti prie Azure AI paslaugų** (jei reikia, sukurkite naują).
    - Pasirinkite **Prisijungti prie Azure AI paieškos** ir **Praleisti prisijungimą**.

    ![Užpildyti hub'ą.](../../../../../../imgs/02/Evaluation-AIFoundry/fill-hub.png)

1. Pasirinkite **Toliau**.

#### Sukurkite Azure AI Foundry projektą

1. Sukurtame hub'e pasirinkite **Visi projektai** iš kairiojo meniu.

1. Pasirinkite **+ Naujas projektas** iš navigacijos meniu.

    ![Pasirinkti naują projektą.](../../../../../../imgs/03/AIFoundry/select-new-project.png)

1. Įveskite **Projekto pavadinimą**. Jis turi būti unikalus.

    ![Sukurti projektą.](../../../../../../imgs/03/AIFoundry/create-project.png)

1. Pasirinkite **Sukurti projektą**.

#### Pridėkite pritaikytą ryšį Phi-3 / Phi-3.5 modeliui

Norėdami integruoti savo pritaikytą Phi-3 / Phi-3.5 modelį į Prompt flow, turite išsaugoti modelio galutinio taško adresą ir raktą pritaikytame ryšyje. Ši konfigūracija užtikrina prieigą prie jūsų pritaikyto modelio Prompt flow aplinkoje.

#### Nustatykite API raktą ir galutinio taško URI Phi-3 / Phi-3.5 modeliui

1. Apsilankykite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Eikite į sukurtą Azure Machine Learning darbo sritį.

1. Pasirinkite **Galutiniai taškai** iš kairiojo meniu.

    ![Pasirinkti galutinius taškus.](../../../../../../imgs/02/Evaluation-AIFoundry/select-endpoints.png)

1. Pasirinkite sukurtą galutinį tašką.

    ![Pasirinkti sukurtą galutinį tašką.](../../../../../../imgs/02/Evaluation-AIFoundry/select-endpoint-created.png)

1. Pasirinkite **Naudoti** iš navigacijos meniu.

1. Nukopijuokite savo **REST galutinio taško adresą** ir **Pirminį raktą**.

    ![Nukopijuoti API raktą ir galutinio taško URI.](../../../../../../imgs/02/Evaluation-AIFoundry/copy-endpoint-key.png)

#### Pridėkite pritaikytą ryšį

1. Apsilankykite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Eikite į sukurtą Azure AI Foundry projektą.

1. Sukurtame projekte pasirinkite **Nustatymai** iš kairiojo meniu.

1. Pasirinkite **+ Naujas ryšys**.

    ![Pasirinkti naują ryšį.](../../../../../../imgs/02/Evaluation-AIFoundry/select-new-connection.png)

1. Pasirinkite **Pritaikyti raktai** iš navigacijos meniu.

    ![Pasirinkti pritaikytus raktus.](../../../../../../imgs/02/Evaluation-AIFoundry/select-custom-keys.png)

1. Atlikite šiuos veiksmus:

    - Pasirinkite **+ Pridėti raktų poras**.
    - Raktų pavadinimui įveskite **endpoint** ir įklijuokite galutinio taško adresą, kurį nukopijavote iš Azure ML Studio, į vertės lauką.
    - Pasirinkite **+ Pridėti raktų poras** dar kartą.
    - Raktų pavadinimui įveskite **key** ir įklijuokite raktą, kurį nukopijavote iš Azure ML Studio, į vertės lauką.
    - Po raktų pridėjimo pasirinkite **yra slapta**, kad raktas nebūtų matomas.

    ![Pridėti ryšį.](../../../../../../imgs/02/Evaluation-AIFoundry/add-connection.png)

1. Pasirinkite **Pridėti ryšį**.

#### Sukurkite Prompt flow

Jūs pridėjote pritaikytą ryšį Azure AI Foundry platformoje. Dabar sukurkite Prompt flow naudodami šiuos veiksmus. Tada prijunkite šį Prompt flow prie pritaikyto ryšio, kad galėtumėte naudoti pritaikytą modelį Prompt flow aplinkoje.

1. Eikite į sukurtą Azure AI Foundry projektą.

1. Pasirinkite **Prompt flow** iš kairiojo meniu.

1. Pasirinkite **+ Kurti** iš navigacijos meniu.

    ![Pasirinkti Prompt flow.](../../../../../../imgs/02/Evaluation-AIFoundry/select-promptflow.png)

1. Pasirinkite **Pokalbio srautas** iš navigacijos meniu.

    ![Pasirinkti pokalbio srautą.](../../../../../../imgs/02/Evaluation-AIFoundry/select-flow-type.png)

1. Įveskite **Aplanko pavadinimą**, kurį norite naudoti.

    ![Pasirinkti pokalbio srautą.](../../../../../../imgs/02/Evaluation-AIFoundry/enter-name.png)

1. Pasirinkite **Kurti**.

#### Konfigūruokite Prompt flow pokalbiui su pritaikytu Phi-3 / Phi-3.5 modeliu

Jums reikia integruoti pritaikytą Phi-3 / Phi-3.5 modelį į Prompt flow. Tačiau esamas Prompt flow nėra pritaikytas šiam tikslui. Todėl turite pertvarkyti Prompt flow, kad galėtumėte integruoti pritaikytą modelį.

1. Prompt flow aplinkoje atlikite šiuos veiksmus, kad pertvarkytumėte esamą srautą:

    - Pasirinkite **Neapdoroto failo režimą**.
    - Ištrinkite visą esamą kodą *flow.dag.yml* faile.
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

    - Pasirinkite **Išsaugoti**.

    ![Pasirinkti neapdoroto failo režimą.](../../../../../../imgs/02/Evaluation-AIFoundry/select-raw-file-mode.png)

1. Pridėkite šį kodą į *integrate_with_promptflow.py*, kad galėtumėte naudoti pritaikytą Phi-3 / Phi-3.5 modelį Prompt flow aplinkoje.

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

    ![Įklijuoti Prompt flow kodą.](../../../../../../imgs/02/Evaluation-AIFoundry/paste-promptflow-code.png)

> [!NOTE]
> Daugiau informacijos apie Prompt flow naudojimą Azure AI Foundry platformoje rasite [Prompt flow Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pasirinkite **Pokalbio įvestis**, **Pokalbio išvestis**, kad įgalintumėte pokalbį su savo modeliu.

    ![Pasirinkti įvestį ir išvestį.](../../../../../../imgs/02/Evaluation-AIFoundry/select-input-output.png)

1. Dabar galite pradėti pokalbį su savo pritaikytu Phi-3 / Phi-3.5 modeliu. Kitame pratime sužinosite, kaip pradėti Prompt flow ir naudoti jį pokalbiui su pritaikytu modeliu.

> [!NOTE]
>
> Pertvarkytas srautas turėtų atrodyti kaip paveikslėlyje žemiau:
>
> ![Srauto pavyzdys](../../../../../../imgs/02/Evaluation-AIFoundry/graph-example.png)
>

#### Pradėkite Prompt flow

1. Pasirinkite **Pradėti skaičiavimo sesijas**, kad pradėtumėte Prompt flow.

    ![Pradėti skaičiavimo sesiją.](../../../../../../imgs/02/Evaluation-AIFoundry/start-compute-session.png)

1. Pasirinkite **Patvirtinti ir analizuoti įvestį**, kad atnaujintumėte parametrus.

    ![Patvirtinti įvestį.](../../../../../../imgs/02/Evaluation-AIFoundry/validate-input.png)

1. Pasirinkite **Ryšio vertę**, kad prijungtumėte pritaikytą ryšį, kurį sukūrėte. Pavyzdžiui, *connection*.

    ![Ryšys.](../../../../../../imgs/02/Evaluation-AIFoundry/select-connection.png)

#### Pokalbis su pritaikytu Phi-3 / Phi-3.5 modeliu

1. Pasirinkite **Pokalbis**.

    ![Pasirinkti pokalbį.](../../../../../../imgs/02/Evaluation-AIFoundry/select-chat.png)

1. Štai pavyzdys rezultatų: Dabar galite pradėti pokalbį su savo pritaikytu Phi-3 / Phi-3.5 modeliu. Rekomenduojama užduoti klausimus, pagrįstus duomenimis, naudotais modelio pritaikymui.

    ![Pokalbis su Prompt flow.](../../../../../../imgs/02/Evaluation-AIFoundry/chat-with-promptflow.png)

### Diegti Azure OpenAI modelį Phi-3 / Phi-3.5 modelio vertinimui

Norėdami įvertinti Phi-3 / Phi-3.5 modelį Azure AI Foundry platformoje, turite diegti Azure OpenAI modelį. Šis modelis bus naudojamas Phi-3 / Phi-3.5 modelio našumui įvertinti.

#### Diegti Azure OpenAI

1. Prisijunkite prie [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Eikite į sukurtą Azure AI Foundry projektą.

    ![Pasirinkti projektą.](../../../../../../imgs/02/Evaluation-AIFoundry/select-project-created.png)

1. Sukurtame projekte pasirinkite **Diegimai** iš kairiojo meniu.

1. Pasirinkite **+ Diegti modelį** iš navigacijos meniu.

1. Pasirinkite **Diegti bazinį modelį**.

    ![Pasirinkti diegimus.](../../../../../../imgs/02/Evaluation-AIFoundry/deploy-openai-model.png)

1. Pasirinkite Azure OpenAI modelį, kurį norite naudoti. Pavyzdžiui, **gpt-4o**.

    ![Pasirinkti Azure OpenAI modelį.](../../../../../../imgs/02/Evaluation-AIFoundry/select-openai-model.png)

1. Pasirinkite **Patvirtinti**.

### Įvertinti pritaikytą Phi-3 / Phi-3.5 modelį naudojant Azure AI Foundry Prompt flow vertinimą

### Pradėti naują vertinimą

1. Apsilankykite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Eikite į sukurtą Azure AI Foundry projektą.

    ![Pasirinkti projektą.](../../../../../../imgs/02/Evaluation-AIFoundry/select-project-created.png)

1. Sukurtame projekte pasirinkite **Vertinimas** iš kairiojo meniu.

1. Pasirinkite **+ Naujas vertinimas** iš navigacijos meniu.

    ![Pasirinkti vertinimą.](../../../../../../imgs/02/Evaluation-AIFoundry/select-evaluation.png)

1. Pasirinkite **Prompt flow** vertinimą.

    ![Pasirinkti Prompt flow vertinimą.](../../../../../../imgs/02/Evaluation-AIFoundry/promptflow-evaluation.png)

1. Atlikite šiuos veiksmus:

    - Įveskite vertinimo pavadinimą. Jis turi būti unikalus.
    - Pasirinkite **Klausimai ir atsakymai be konteksto** kaip užduoties tipą. Kadangi **ULTRACHAT_200k** duomenų rinkinys, naudotas šiame vadove, neturi konteksto.
    - Pasirinkite Prompt flow, kurį norite įvertinti.

    ![Prompt flow vertinimas.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting1.png)

1. Pasirinkite **Toliau**.

1. Atlikite šiuos veiksmus:

    - Pasirinkite **Pridėti savo duomenų rinkinį**, kad įkeltumėte duomenų rinkinį. Pavyzdžiui, galite įkelti testavimo duomenų failą, pvz., *test_data.json1*, kuris yra įtrauktas, kai atsisiunčiate **ULTRACHAT_200k** duomenų rinkinį.
    - Pasirinkite tinkamą **Duomenų rinkinio stulpelį**, kuris atitinka jūsų duomenų rinkinį. Pavyzdžiui, jei naudojate **ULTRACHAT_200k** duomenų rinkinį, pasirinkite **${data.prompt}** kaip duomenų rinkinio stulpelį.

    ![Prompt flow vertinimas.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting2.png)

1. Pasirinkite **Toliau**.

1. Atlikite šiuos veiksmus, kad sukonfigūruotumėte našumo ir kokybės metrikas:

    - Pasirinkite našumo ir kokybės metrikas, kurias norite naudoti.
    - Pasirinkite Azure OpenAI modelį, kurį sukūrėte vertinimui. Pavyzdžiui, pasirinkite **gpt-4o**.

    ![Prompt flow vertinimas.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting3-1.png)

1. Atlikite šiuos veiksmus, kad sukonfigūruotumėte rizikos ir saugumo metrikas:

    - Pasirinkite rizikos ir saugumo metrikas, kurias norite naudoti.
    - Pasirinkite slenkstį, kad apskaičiuotumėte defektų rodiklį, kurį norite naudoti. Pavyzdžiui, pasirinkite **Vidutinis**.
    - **Klausimui** pasirinkite **Duomenų šaltinis** kaip **{$data.prompt}**.
    - **Atsakymui** pasirinkite **Duomenų šaltinis** kaip **{$run.outputs.answer}**.
    - **Tikslui** pasirinkite **Duomenų šaltinis** kaip **{$data.message}**.

    ![Prompt flow vertinimas.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting3-2.png)

1. Pasirinkite **Toliau**.

1. Pasirinkite **Pateikti**, kad pradėtumėte vertinimą.

1. Vertinimas užtruks šiek tiek laiko. Progresą galite stebėti **Vertinimo** skiltyje.

### Peržiūrėkite vertinimo rezultatus
> [!NOTE]  
> Rezultatai, pateikti žemiau, skirti iliustruoti vertinimo procesą. Šiame vadove naudojome modelį, pritaikytą pagal palyginti mažą duomenų rinkinį, todėl rezultatai gali būti neoptimalūs. Tikrieji rezultatai gali labai skirtis priklausomai nuo naudojamo duomenų rinkinio dydžio, kokybės ir įvairovės, taip pat nuo konkrečios modelio konfigūracijos.
Kai vertinimas bus baigtas, galite peržiūrėti rezultatus tiek našumo, tiek saugumo metrikų atžvilgiu.

1. Našumo ir kokybės metrikos:

    - Įvertinkite modelio efektyvumą generuojant nuoseklius, sklandžius ir aktualius atsakymus.

    ![Vertinimo rezultatas.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-result-gpu.png)

1. Rizikos ir saugumo metrikos:

    - Užtikrinkite, kad modelio rezultatai būtų saugūs ir atitiktų Atsakingo AI principus, vengiant bet kokio žalingo ar įžeidžiančio turinio.

    ![Vertinimo rezultatas.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-result-gpu-2.png)

1. Galite slinkti žemyn, kad peržiūrėtumėte **Išsamių metrikų rezultatus**.

    ![Vertinimo rezultatas.](../../../../../../imgs/02/Evaluation-AIFoundry/detailed-metrics-result.png)

1. Vertindami savo pritaikytą Phi-3 / Phi-3.5 modelį pagal našumo ir saugumo metrikas, galite patvirtinti, kad modelis ne tik efektyvus, bet ir laikosi atsakingo AI praktikos, todėl yra pasiruošęs realiam naudojimui.

## Sveikiname!

### Jūs baigėte šį mokymą

Jūs sėkmingai įvertinote pritaikytą Phi-3 modelį, integruotą su Prompt flow Azure AI Foundry platformoje. Tai svarbus žingsnis užtikrinant, kad jūsų AI modeliai ne tik veiktų gerai, bet ir laikytųsi „Microsoft“ Atsakingo AI principų, padedančių kurti patikimas ir patikimas AI programas.

![Architektūra.](../../../../../../imgs/02/Evaluation-AIFoundry/architecture.png)

## Išvalykite Azure išteklius

Išvalykite savo Azure išteklius, kad išvengtumėte papildomų mokesčių savo paskyrai. Eikite į Azure portalą ir ištrinkite šiuos išteklius:

- Azure Machine learning išteklius.
- Azure Machine learning modelio galinį tašką.
- Azure AI Foundry projekto išteklius.
- Azure AI Foundry Prompt flow išteklius.

### Kiti žingsniai

#### Dokumentacija

- [AI sistemų vertinimas naudojant Atsakingo AI prietaisų skydelį](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Generatyvaus AI vertinimo ir stebėjimo metrikos](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry dokumentacija](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokumentacija](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Mokymo turinys

- [Įvadas į „Microsoft“ Atsakingo AI požiūrį](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Įvadas į Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Nuorodos

- [Kas yra Atsakingas AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Nauji įrankiai Azure AI, padedantys kurti saugesnes ir patikimesnes generatyvaus AI programas](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Generatyvaus AI programų vertinimas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.