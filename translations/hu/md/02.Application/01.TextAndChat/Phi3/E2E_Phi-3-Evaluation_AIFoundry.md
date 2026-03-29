# Értékelje a finomhangolt Phi-3 / Phi-3.5 modellt a Microsoft Foundry-ban a Microsoft felelős mesterséges intelligencia elveire fókuszálva

Ez a teljes körű (E2E) minta a Microsoft Tech Community "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" útmutatóján alapul.

## Áttekintés

### Hogyan értékelheti a finomhangolt Phi-3 / Phi-3.5 modell biztonságát és teljesítményét a Microsoft Foundry-ban?

Egy modell finomhangolása néha nem kívánt vagy nem szándékolt válaszokhoz vezethet. Annak érdekében, hogy a modell biztonságos és hatékony maradjon, fontos értékelni a modell potenciálját a káros tartalom előállítására, valamint a pontos, releváns és koherens válaszok előállítására való képességét. Ebben az oktatóanyagban megtanulja, hogyan értékelje a finomhangolt Phi-3 / Phi-3.5 modellt, amely a Prompt flow-val integrált a Microsoft Foundry-ban.

Íme a Microsoft Foundry értékelési folyamata.

![Az oktatóanyag architektúrája.](../../../../../../translated_images/hu/architecture.10bec55250f5d6a4.webp)

*Kép forrása: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Részletesebb információkért és további erőforrásokért a Phi-3 / Phi-3.5 témában kérjük, látogassa meg a [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) oldalát.

### Előfeltételek

- [Python](https://www.python.org/downloads)
- [Azure előfizetés](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Finomhangolt Phi-3 / Phi-3.5 modell

### Tartalomjegyzék

1. [**1. forgatókönyv: Bevezetés a Microsoft Foundry Prompt flow értékelésébe**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Bevezetés a biztonságértékelésbe](#bevezetés-a-biztonságértékelésbe)
    - [Bevezetés a teljesítményértékelésbe](#bevezetés-a-teljesítményértékelésbe)

1. [**2. forgatókönyv: A Phi-3 / Phi-3.5 modell értékelése a Microsoft Foundry-ban**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Mielőtt elkezdené](#mielőtt-elkezdené)
    - [Azure OpenAI telepítése a Phi-3 / Phi-3.5 modell értékeléséhez](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [A finomhangolt Phi-3 / Phi-3.5 modell értékelése a Microsoft Foundry Prompt flow értékelésével](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Gratulálunk!](#gratulálunk)

## **1. forgatókönyv: Bevezetés a Microsoft Foundry Prompt flow értékelésébe**

### Bevezetés a biztonságértékelésbe

Annak biztosítására, hogy mesterséges intelligencia modellje etikus és biztonságos legyen, elengedhetetlen, hogy a Microsoft Felelős MI elveihez igazítva értékeljük azt. A Microsoft Foundry-ban a biztonságértékelések lehetővé teszik, hogy felmérje modellje jailbreak támadásokkal szembeni sérülékenységét és a káros tartalom generálásának potenciálját, amely közvetlenül kapcsolódik ezekhez az elvekhez.

![Biztonságértékelés.](../../../../../../translated_images/hu/safety-evaluation.083586ec88dfa950.webp)

*Kép forrása: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### A Microsoft felelős MI elvei

A technikai lépések megkezdése előtt fontos megérteni a Microsoft Felelős MI elveit, amelyek egy etikai keretrendszert alkotnak az MI rendszerek felelős fejlesztésének, telepítésének és működtetésének irányítására. Ezek az elvek irányítják az MI rendszerek felelős tervezését, fejlesztését és bevezetését, biztosítva, hogy az MI technológiák igazságos, átlátható és befogadó módon épüljenek fel. Ezek az elvek képezik az MI modellek biztonságának értékelésének alapját.

A Microsoft felelős MI elvei a következők:

- **Igazságosság és befogadás**: Az MI rendszereknek mindenkit igazságosan kell kezelniük, és el kell kerülniük, hogy hasonló helyzetben lévő csoportokat különböző módon érintsenek. Például, amikor az MI rendszerek orvosi kezelési javaslatokat, kölcsönkérelmeket vagy foglalkoztatási megoldásokat adnak, ugyanazokat az ajánlásokat kell mindenkinek megadniuk, akik hasonló tünetekkel, pénzügyi helyzettel vagy szakképesítéssel rendelkeznek.

- **Megbízhatóság és biztonság**: A bizalom kiépítéséhez elengedhetetlen, hogy az MI rendszerek megbízhatóan, biztonságosan és következetesen működjenek. Ezeknek a rendszereknek eredeti tervezésük szerint kell működniük, biztonságosan kell reagálniuk a váratlan helyzetekre és ellenállniuk a káros manipulációnak. Viselkedésük és az általuk kezelhető körülmények sokfélesége tükrözi azokat a szituációkat és körülményeket, amelyeket a fejlesztők a tervezés és tesztelés során előreláttak.

- **Átláthatóság**: Amikor az MI rendszerek olyan döntések meghozatalában segítenek, amelyek hatalmas hatással vannak az emberek életére, elengedhetetlen, hogy az emberek megértsék, hogyan születtek ezek a döntések. Például egy bank MI rendszert használhat annak eldöntésére, hogy valaki hitelképes-e. Egy cég MI rendszert használhat a legalkalmasabb jelöltek kiválasztására.

- **Adatvédelem és biztonság**: Ahogy az MI egyre elterjedtebbé válik, az adatvédelem és a személyes, valamint üzleti információk védelme egyre fontosabbá és összetettebbé válik. Az MI esetében az adatvédelem és adatbiztonság különös figyelmet igényel, mert az adatokhoz való hozzáférés alapvető az MI rendszerek számára, hogy pontos és megalapozott előrejelzéseket és döntéseket hozzanak az emberekről.

- **Felelősség**: Azok, akik MI rendszereket terveznek és telepítenek, felelősséggel tartoznak a rendszereik működéséért. A szervezeteknek ipari szabványokat kell alkalmazniuk a felelősségvállalási normák kidolgozásához. Ezek a normák biztosíthatják, hogy az MI rendszerek ne legyenek a végső hatóságok semmilyen, az emberek életét érintő döntésben. Emellett biztosíthatják, hogy az emberek jelentős kontrollt gyakoroljanak máskülönben nagyon autonóm MI rendszerek felett.

![Fill hub.](../../../../../../translated_images/hu/responsibleai2.c07ef430113fad8c.webp)

*Kép forrása: [Mi az a Felelős MI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Ha többet szeretne megtudni a Microsoft felelős MI elveiről, látogassa meg a [Mi az a Felelős MI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) oldalt.

#### Biztonsági mutatók

Ebben az oktatóanyagban a finomhangolt Phi-3 modell biztonságát a Microsoft Foundry biztonsági mutatóinak segítségével értékeli. Ezek a mutatók segítenek felmérni a modell potenciálját káros tartalom generálására és jailbreak támadásokkal szembeni sérülékenységét. A biztonsági mutatók a következők:

- **Önártalommal kapcsolatos tartalom**: Értékeli, hogy a modell hajlamos-e önártalommal kapcsolatos tartalmak előállítására.
- **Gyűlöletkeltő és igazságtalan tartalom**: Értékeli, hogy a modell hajlamos-e gyűlöletkeltő vagy igazságtalan tartalmak előállítására.
- **Erőszakos tartalom**: Értékeli, hogy a modell hajlamos-e erőszakos tartalmak előállítására.
- **Szexuális tartalom**: Értékeli, hogy a modell hajlamos-e nem megfelelő szexuális tartalmak előállítására.

Ezeknek a szempontoknak az értékelése biztosítja, hogy az MI modell ne állítson elő káros vagy sértő tartalmakat, összhangban a társadalmi értékekkel és a szabályozási normákkal.

![Értékelés a biztonság alapján.](../../../../../../translated_images/hu/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Bevezetés a teljesítményértékelésbe

Annak biztosítására, hogy az MI modell az elvárásoknak megfelelően működjön, fontos értékelni a teljesítményét megfelelő mutatók alapján. A Microsoft Foundry-ban a teljesítményértékelés lehetővé teszi a modell hatékonyságának mérését a pontos, releváns és koherens válaszok generálásában.

![Biztonságértékelés.](../../../../../../translated_images/hu/performance-evaluation.48b3e7e01a098740.webp)

*Kép forrása: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Teljesítménymutatók

Ebben az oktatóanyagban a finomhangolt Phi-3 / Phi-3.5 modell teljesítményét a Microsoft Foundry teljesítménymutatóinak segítségével értékeli. Ezek a mutatók segítenek felmérni a modell hatékonyságát a pontos, releváns és koherens válaszok generálásában. A teljesítménymutatók a következők:

- **Megalapozottság**: Értékeli, hogy a generált válasz mennyire illeszkedik az input forrásból származó információkhoz.
- **Relevancia**: Értékeli a generált válaszok kérdésekhez való illeszkedését.
- **Koherencia**: Értékeli, hogy a generált szöveg milyen simán folyik, természetesen olvasható és emberi nyelvhez hasonló-e.
- **Folyékonyság**: Értékeli a generált szöveg nyelvismeretét.
- **GPT Hasonlóság**: Összehasonlítja a generált választ a valósággal a hasonlóság alapján.
- **F1 pontszám**: Kiszámolja a közös szavak arányát a generált válasz és a forrásadatok között.

Ezek a mutatók segítenek értékelni a modell hatékonyságát a pontos, releváns és koherens válaszok előállításában.

![Értékelés a teljesítmény alapján.](../../../../../../translated_images/hu/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **2. forgatókönyv: A Phi-3 / Phi-3.5 modell értékelése a Microsoft Foundry-ban**

### Mielőtt elkezdené

Ez az oktatóanyag folytatása a korábbi blogbejegyzéseknek, amelyek címei: "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" és "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Ezekben a bejegyzésekben végigvezettük a Phi-3 / Phi-3.5 modell finomhangolásának folyamatán a Microsoft Foundry-ban, és integráltuk azt a Prompt flow-val.

Ebben az oktatóanyagban telepíteni fog egy Azure OpenAI modellt értékelőként a Microsoft Foundry-ban, és azt használja majd a finomhangolt Phi-3 / Phi-3.5 modell értékelésére.

Mielőtt elkezdené ezt az oktatóanyagot, győződjön meg róla, hogy rendelkezik a korábbi oktatóanyagokban ismertetett következő előfeltételekkel:

1. Egy előkészített adatállomány a finomhangolt Phi-3 / Phi-3.5 modell értékeléséhez.
1. Egy Phi-3 / Phi-3.5 modell, amelyet finomhangoltak és telepítettek az Azure Machine Learningre.
1. Egy Prompt flow, amely integrálva van a finomhangolt Phi-3 / Phi-3.5 modellel a Microsoft Foundry-ban.

> [!NOTE]
> Az *test_data.jsonl* fájlt, amely a **ULTRACHAT_200k** adatállomány mappájában található, és amelyet a korábbi blogbejegyzésekből töltött le, fogja használni a finomhangolt Phi-3 / Phi-3.5 modell értékelési adathalmazaként.

#### Egyedi Phi-3 / Phi-3.5 modell integrálása Prompt flow-val a Microsoft Foundry-ban (először kód alapú megközelítés)

> [!NOTE]
> Ha a "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" című bejegyzésben ismertetett alacsony kódú megközelítést követte, kihagyhatja ezt a feladatot, és léphet a következőre.
> Azonban, ha a "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" cikkben bemutatott kód alapú megközelítést követte Phi-3 / Phi-3.5 modellje finomhangolására és telepítésére, akkor a modell Prompt flow-hoz való csatlakoztatása kissé eltérő folyamat. Ezt a folyamatot ebben a feladatban fogja megtanulni.

A folytatáshoz integrálnia kell finomhangolt Phi-3 / Phi-3.5 modelljét a Prompt flow-ba a Microsoft Foundry-ban.

#### Microsoft Foundry Hub létrehozása

A Project létrehozása előtt létre kell hoznia egy Hub-ot. A Hub olyan, mint egy erőforráscsoport, amely lehetővé teszi több projekt szervezését és kezelését a Microsoft Foundry-n belül.
1. Jelentkezzen be a [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) fiókjába.

1. Válassza ki a bal oldali fülnél az **All hubs** lehetőséget.

1. Válassza a navigációs menüből a **+ New hub** lehetőséget.

    ![Create hub.](../../../../../../translated_images/hu/create-hub.5be78fb1e21ffbf1.webp)

1. Végezze el a következő feladatokat:

    - Írja be a **Hub name** mezőt. Egyedi értéknek kell lennie.
    - Válassza ki Azure **Subscription** előfizetését.
    - Válassza ki az használni kívánt **Resource group**-ot (szükség esetén hozzon létre újat).
    - Válassza ki a kívánt **Location** helyszínt.
    - Válassza ki az használni kívánt **Connect Azure AI Services** szolgáltatást (szükség esetén hozzon létre újat).
    - Válassza a **Connect Azure AI Search** opcióból a **Skip connecting** lehetőséget.

    ![Fill hub.](../../../../../../translated_images/hu/fill-hub.baaa108495c71e34.webp)

1. Válassza a **Next** lehetőséget.

#### Microsoft Foundry projekt létrehozása

1. A létrehozott Hub-ban válassza ki a bal oldali fülnél az **All projects** lehetőséget.

1. Válassza a navigációs menüből a **+ New project** lehetőséget.

    ![Select new project.](../../../../../../translated_images/hu/select-new-project.cd31c0404088d7a3.webp)

1. Adja meg a **Project name** értéket. Egyedi értéknek kell lennie.

    ![Create project.](../../../../../../translated_images/hu/create-project.ca3b71298b90e420.webp)

1. Válassza a **Create a project** lehetőséget.

#### Egyedi kapcsolat hozzáadása a finomhangolt Phi-3 / Phi-3.5 modellhez

Ahhoz, hogy a finomhangolt Phi-3 / Phi-3.5 modellt integrálja a Prompt flow-val, el kell mentenie a modell végpontját és kulcsát egy egyedi kapcsolatban. Ez a beállítás biztosítja az elérést a finomhangolt Phi-3 / Phi-3.5 modellhez a Prompt flow-n belül.

#### Az api kulcs és a végpont URI beállítása a finomhangolt Phi-3 / Phi-3.5 modellhez

1. Látogasson el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Navigáljon az Azure Machine learning munkaterülethez, amelyet létrehozott.

1. Válassza ki bal oldalon az **Endpoints** lehetőséget.

    ![Select endpoints.](../../../../../../translated_images/hu/select-endpoints.ee7387ecd68bd18d.webp)

1. Válassza ki a létrehozott végpontot.

    ![Select endpoints.](../../../../../../translated_images/hu/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. A navigációs menüből válassza a **Consume** lehetőséget.

1. Másolja ki a **REST endpoint**-ot és az **Primary key**-t.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/hu/copy-endpoint-key.0650c3786bd646ab.webp)

#### Egyedi kapcsolat hozzáadása

1. Látogasson el a [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) oldalra.

1. Navigáljon a létrehozott Microsoft Foundry projekthez.

1. A létrehozott projektben válassza ki bal oldalon a **Settings** fület.

1. Válassza a **+ New connection** lehetőséget.

    ![Select new connection.](../../../../../../translated_images/hu/select-new-connection.fa0f35743758a74b.webp)

1. A navigációs menüből válassza a **Custom keys** lehetőséget.

    ![Select custom keys.](../../../../../../translated_images/hu/select-custom-keys.5a3c6b25580a9b67.webp)

1. Végezze el a következőket:

    - Válassza a **+ Add key value pairs** lehetőséget.
    - A kulcs nevének adja meg: **endpoint**, majd illessze be az Azure ML Studioból másolt végpontot az érték mezőbe.
    - Válassza ismét a **+ Add key value pairs** lehetőséget.
    - A kulcs nevének adja meg: **key**, majd illessze be az Azure ML Studioból másolt kulcsot az érték mezőbe.
    - Miután hozzáadta a kulcsokat, jelölje be az **is secret** opciót, hogy a kulcs ne legyen látható.

    ![Add connection.](../../../../../../translated_images/hu/add-connection.ac7f5faf8b10b0df.webp)

1. Válassza a **Add connection** lehetőséget.

#### Prompt flow létrehozása

Hozzáadott egy egyedi kapcsolatot a Microsoft Foundry-ban. Most hozzunk létre egy Prompt flow-t a következő lépésekkel. Ezután ezt a Prompt flow-t összekapcsolja az egyedi kapcsolattal, hogy a finomhangolt modellt használhassa a Prompt flow-n belül.

1. Navigáljon a létrehozott Microsoft Foundry projekthez.

1. Válassza ki bal oldalon a **Prompt flow** fület.

1. Válassza a navigációs menüből a **+ Create** lehetőséget.

    ![Select Promptflow.](../../../../../../translated_images/hu/select-promptflow.18ff2e61ab9173eb.webp)

1. A navigációs menüből válassza a **Chat flow** lehetőséget.

    ![Select chat flow.](../../../../../../translated_images/hu/select-flow-type.28375125ec9996d3.webp)

1. Adja meg a használni kívánt **Folder name** értéket.

    ![Select chat flow.](../../../../../../translated_images/hu/enter-name.02ddf8fb840ad430.webp)

1. Válassza a **Create** lehetőséget.

#### Prompt flow beállítása a finomhangolt Phi-3 / Phi-3.5 modellel való csevegéshez

Integrálni kell a finomhangolt Phi-3 / Phi-3.5 modellt egy Prompt flow-ba. Azonban a meglévő Prompt flow nem erre a célra készült. Ezért újra kell terveznie a Prompt flow-t, hogy sikeresen integrálhassa az egyedi modellt.

1. A Prompt flow-ban végezze el az alábbi feladatokat a meglévő folyamat újjáépítéséhez:

    - Válassza a **Raw file mode** opciót.
    - Törölje a *flow.dag.yml* fájlban lévő összes meglévő kódot.
    - Másolja be a következő kódot a *flow.dag.yml* fájlba.

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

    - Válassza a **Save** lehetőséget.

    ![Select raw file mode.](../../../../../../translated_images/hu/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Másolja be a következő kódot az *integrate_with_promptflow.py* fájlba, hogy használhassa a finomhangolt Phi-3 / Phi-3.5 modellt a Prompt flow-ban.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Naplózás beállítása
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

        # A "connection" a Custom Connection neve, az "endpoint" és "key" a Custom Connection kulcsai
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
            
            # A teljes JSON választ naplózza
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

    ![Paste prompt flow code.](../../../../../../translated_images/hu/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> A Microsoft Foundry-ban történő Prompt flow használatáról további részletes információkat a [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) oldalon találhat.

1. Válassza ki a **Chat input** és **Chat output** elemeket, hogy engedélyezze a csevegést a modelljével.

    ![Select Input Output.](../../../../../../translated_images/hu/select-input-output.c187fc58f25fbfc3.webp)

1. Most már készen áll arra, hogy csevegjék finomhangolt Phi-3 / Phi-3.5 modelljével. A következő gyakorlatban megtanulja, hogyan indítsa el a Prompt flow-t, és hogyan használja a finomhangolt Phi-3 / Phi-3.5 modelljével való csevegéshez.

> [!NOTE]
>
> Az újjáépített folyamatnak a következő képhez kell hasonlítania:
>
> ![Flow example](../../../../../../translated_images/hu/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow indítása

1. Válassza a **Start compute sessions** opciót a Prompt flow indításához.

    ![Start compute session.](../../../../../../translated_images/hu/start-compute-session.9acd8cbbd2c43df1.webp)

1. Válassza a **Validate and parse input** lehetőséget a paraméterek frissítéséhez.

    ![Validate input.](../../../../../../translated_images/hu/validate-input.c1adb9543c6495be.webp)

1. Válassza ki a **connection** értékét az előzőleg létrehozott egyedi kapcsolatra. Például *connection*.

    ![Connection.](../../../../../../translated_images/hu/select-connection.1f2b59222bcaafef.webp)

#### Csevegés a finomhangolt Phi-3 / Phi-3.5 modellel

1. Válassza a **Chat** lehetőséget.

    ![Select chat.](../../../../../../translated_images/hu/select-chat.0406bd9687d0c49d.webp)

1. Íme egy példa az eredményekre: most már cseveghet a finomhangolt Phi-3 / Phi-3.5 modellel. Ajánlott olyan kérdéseket feltenni, amelyek a finomhangolás során használt adatokra épülnek.

    ![Chat with prompt flow.](../../../../../../translated_images/hu/chat-with-promptflow.1cf8cea112359ada.webp)

### Azure OpenAI telepítése a Phi-3 / Phi-3.5 modell értékeléséhez

Ahhoz, hogy értékelje a Phi-3 / Phi-3.5 modellt a Microsoft Foundry-ban, telepítenie kell egy Azure OpenAI modellt. Ezt a modellt fogják használni a Phi-3 / Phi-3.5 modell teljesítményének értékelésére.

#### Azure OpenAI telepítése

1. Jelentkezzen be a [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) oldalra.

1. Navigáljon a létrehozott Microsoft Foundry projekthez.

    ![Select Project.](../../../../../../translated_images/hu/select-project-created.5221e0e403e2c9d6.webp)

1. A létrehozott projektben válassza ki bal oldalon a **Deployments** fület.

1. Válassza a navigációs menüből a **+ Deploy model** lehetőséget.

1. Válassza a **Deploy base model** lehetőséget.

    ![Select Deployments.](../../../../../../translated_images/hu/deploy-openai-model.95d812346b25834b.webp)

1. Válassza ki azt az Azure OpenAI modellt, amelyet használni szeretne. Például, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/hu/select-openai-model.959496d7e311546d.webp)

1. Válassza a **Confirm** lehetőséget.

### Értékelje a finomhangolt Phi-3 / Phi-3.5 modellt a Microsoft Foundry Prompt flow értékelésével

### Új értékelés indítása

1. Látogasson el a [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) oldalra.

1. Navigáljon a létrehozott Microsoft Foundry projekthez.

    ![Select Project.](../../../../../../translated_images/hu/select-project-created.5221e0e403e2c9d6.webp)

1. A létrehozott projektben válassza ki bal oldalon az **Evaluation** lehetőséget.

1. Válassza a navigációs menüből a **+ New evaluation** lehetőséget.

    ![Select evaluation.](../../../../../../translated_images/hu/select-evaluation.2846ad7aaaca7f4f.webp)

1. Válassza a **Prompt flow** értékelést.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/hu/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Végezze el a következőket:

    - Adja meg az értékelés nevét. Egyedi érték kell legyen.
    - Válassza a feladat típusaként a **Question and answer without context** lehetőséget, mert az ebben a bemutatóban használt **UlTRACHAT_200k** adatállomány nem tartalmaz kontextust.
    - Válassza ki a kiértékelni kívánt prompt flow-t.

    ![Prompt flow evaluation.](../../../../../../translated_images/hu/evaluation-setting1.4aa08259ff7a536e.webp)

1. Válassza a **Next** lehetőséget.

1. Végezze el a következőket:

    - Válassza az **Add your dataset** lehetőséget az adatállomány feltöltéséhez. Például feltöltheti a tesztadatokat tartalmazó fájlt, mint a *test_data.json1*, ami a **ULTRACHAT_200k** adatállomány része.
    - Válassza ki a megfelelő **Dataset column** értéket, amely megfelel az adatállományának. Például, ha a **ULTRACHAT_200k** adatállományt használja, válassza a **${data.prompt}** lehetőséget.

    ![Prompt flow evaluation.](../../../../../../translated_images/hu/evaluation-setting2.07036831ba58d64e.webp)

1. Válassza a **Next** lehetőséget.

1. Végezze el a teljesítmény- és minőségi mutatók beállítását:

    - Válassza ki a használni kívánt teljesítmény- és minőségi mutatókat.
    - Válassza ki a kiértékelésre létrehozott Azure OpenAI modellt. Például válassza a **gpt-4o** modellt.

    ![Prompt flow evaluation.](../../../../../../translated_images/hu/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Végezze el a kockázati és biztonsági mutatók beállítását:

    - Válassza ki a használni kívánt kockázati és biztonsági mutatókat.
    - Válassza ki a hibaarány számításához használandó küszöbértéket. Például válassza a **Medium** lehetőséget.
    - A **question** mezőhöz válassza a **Data source**-t **{$data.prompt}** értékre.
    - A **answer** mezőhöz válassza a **Data source**-t **{$run.outputs.answer}** értékre.
    - A **ground_truth** mezőhöz válassza a **Data source**-t **{$data.message}** értékre.

    ![Prompt flow evaluation.](../../../../../../translated_images/hu/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Válassza a **Next** lehetőséget.

1. Válassza a **Submit** lehetőséget az értékelés elindításához.

1. Az értékelés befejezése eltarthat egy ideig. A folyamat előrehaladását az **Evaluation** lapon követheti nyomon.

### Az értékelés eredményeinek áttekintése

> [!NOTE]
> Az alábbi eredmények az értékelési folyamat illusztrálására szolgálnak. Ebben a bemutatóban egy viszonylag kis adatállományon finomhangolt modellt használtunk, amely alacsonyabb szintű eredményeket eredményezhet. A tényleges eredmények nagymértékben eltérhetnek az adatállomány méretétől, minőségétől, sokféleségétől és a modell konkrét konfigurációjától függően.

Az értékelés befejezése után áttekintheti mind a teljesítmény-, mind a biztonsági mutatók eredményeit.
1. Teljesítmény- és minőségi mutatók:

    - értékelje a modell hatékonyságát a koherens, folyékony és releváns válaszok generálásában.

    ![Értékelés eredménye.](../../../../../../translated_images/hu/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Kockázat és biztonsági mutatók:

    - Biztosítsa, hogy a modell kimenetei biztonságosak legyenek, és megfeleljenek a Felelős MI elveknek, elkerülve bármilyen káros vagy sértő tartalmat.

    ![Értékelés eredménye.](../../../../../../translated_images/hu/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Görgessen lefelé a **Részletes mutatók eredményének** megtekintéséhez.

    ![Értékelés eredménye.](../../../../../../translated_images/hu/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Az egyedi Phi-3 / Phi-3.5 modell teljesítmény- és biztonsági mutatókkal történő értékelésével megerősítheti, hogy a modell nemcsak hatékony, hanem felelős MI gyakorlatokat is követ, így készen áll a valós környezetben történő alkalmazásra.

## Gratulálunk!

### Teljesítette ezt az oktatóanyagot

Sikeresen értékelte a finomhangolt Phi-3 modellt, amely a Prompt flow-val integrálva működik a Microsoft Foundry-ban. Ez egy fontos lépés annak biztosításában, hogy MI modelljei ne csak jól teljesítsenek, hanem megfeleljenek a Microsoft Felelős MI elveinek, segítve Önt megbízható és hiteles MI alkalmazások létrehozásában.

![Architektúra.](../../../../../../translated_images/hu/architecture.10bec55250f5d6a4.webp)

## Azure erőforrások törlése

Törölje Azure erőforrásait a további díjak elkerülése érdekében. Lépjen az Azure portálra, és törölje a következő erőforrásokat:

- Az Azure Machine Learning erőforrást.
- Az Azure Machine Learning modell végpontját.
- A Microsoft Foundry projekt erőforrást.
- A Microsoft Foundry Prompt flow erőforrást.

### Következő lépések

#### Dokumentáció

- [MI rendszerek értékelése a Felelős MI műszerfal használatával](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Generatív MI értékelési és monitorozási mutatói](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry dokumentáció](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokumentáció](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Oktatási tartalom

- [Bevezetés a Microsoft Felelős MI megközelítésébe](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Bevezetés a Microsoft Foundry használatába](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Hivatkozások

- [Mi az a Felelős MI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Új eszközök bejelentése az Azure MI-ben, amelyek segítenek biztonságosabb és megbízhatóbb generatív MI alkalmazások fejlesztésében](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Generatív MI alkalmazások értékelése](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordító szolgáltatásával készült. Bár igyekszünk pontos fordítást biztosítani, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félrefordításokért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->