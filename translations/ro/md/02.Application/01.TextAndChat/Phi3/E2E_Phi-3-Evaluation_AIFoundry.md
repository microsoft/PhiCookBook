# Evaluarea modelului Phi-3 / Phi-3.5 ajustat fin în Microsoft Foundry, concentrându-se pe principiile AI responsabile Microsoft

Acest exemplu end-to-end (E2E) se bazează pe ghidul "[Evaluarea modelelor Phi-3 / 3.5 ajustate fin în Microsoft Foundry, concentrându-se pe AI responsabil al Microsoft](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" din Microsoft Tech Community.

## Prezentare generală

### Cum poți evalua siguranța și performanța unui model Phi-3 / Phi-3.5 ajustat fin în Microsoft Foundry?

Ajustarea fină a unui model poate duce uneori la răspunsuri neintenționate sau nedorite. Pentru a asigura că modelul rămâne sigur și eficient, este important să evaluezi potențialul modelului de a genera conținut dăunător și capacitatea sa de a produce răspunsuri precise, relevante și coerente. În acest tutorial, vei învăța cum să evaluezi siguranța și performanța unui model Phi-3 / Phi-3.5 ajustat fin, integrat cu Prompt flow în Microsoft Foundry.

Iată procesul de evaluare Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/ro/architecture.10bec55250f5d6a4.webp)

*Sursa imaginii: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Pentru informații mai detaliate și pentru a explora resurse suplimentare despre Phi-3 / Phi-3.5, te rugăm să vizitezi [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Precondiții

- [Python](https://www.python.org/downloads)
- [Abonament Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Model Phi-3 / Phi-3.5 ajustat fin

### Cuprins

1. [**Scenariul 1: Introducere în evaluarea Prompt flow din Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Introducere în evaluarea siguranței](#introducere-în-evaluarea-siguranței)
    - [Introducere în evaluarea performanței](#introducere-în-evaluarea-performanței)

1. [**Scenariul 2: Evaluarea modelului Phi-3 / Phi-3.5 în Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Înainte de a începe](#înainte-de-a-începe)
    - [Implementarea Azure OpenAI pentru evaluarea modelului Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Evaluarea modelului Phi-3 / Phi-3.5 ajustat fin folosind evaluarea Prompt flow din Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Felicitări!](#felicitări)

## **Scenariul 1: Introducere în evaluarea Prompt flow din Microsoft Foundry**

### Introducere în evaluarea siguranței

Pentru a asigura că modelul tău AI este etic și sigur, este esențial să-l evaluezi conform principiilor AI responsabile ale Microsoft. În Microsoft Foundry, evaluările de siguranță îți permit să verifici vulnerabilitatea modelului la atacuri de tip jailbreak și potențialul său de a genera conținut dăunător, ceea ce este direct aliniat cu aceste principii.

![Safaty evaluation.](../../../../../../translated_images/ro/safety-evaluation.083586ec88dfa950.webp)

*Sursa imaginii: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principiile AI responsabile Microsoft

Înainte de a începe pașii tehnici, este esențial să înțelegi Principiile AI responsabile Microsoft, un cadru etic conceput pentru a ghida dezvoltarea responsabilă, implementarea și operarea sistemelor AI. Aceste principii conduc designul responsabil, dezvoltarea și implementarea sistemelor AI, asigurând că tehnologiile AI sunt construite într-un mod echitabil, transparent și incluziv. Aceste principii sunt fundamentul evaluării siguranței modelelor AI.

Principiile AI responsabile Microsoft includ:

- **Echitate și incluziune**: Sistemele AI ar trebui să trateze toți în mod echitabil și să evite să afecteze diferit grupuri similare de persoane. De exemplu, atunci când sistemele AI oferă recomandări privind tratamente medicale, cereri de împrumut sau angajare, ele ar trebui să facă aceleași recomandări tuturor celor cu simptome, circumstanțe financiare sau calificări profesionale similare.

- **Fiabilitate și siguranță**: Pentru a construi încredere, este esențial ca sistemele AI să funcționeze fiabil, în siguranță și consecvent. Aceste sisteme trebuie să opereze așa cum au fost proiectate inițial, să răspundă în siguranță la condiții neașteptate și să reziste manipulării dăunătoare. Comportamentul și varietatea condițiilor pe care le pot gestiona reflectă gama situațiilor anticipate de dezvoltatori în timpul proiectării și testării.

- **Transparență**: Când sistemele AI ajută la luarea deciziilor cu impact major asupra vieților oamenilor, este esențial ca oamenii să înțeleagă cum au fost luate aceste decizii. De exemplu, o bancă ar putea folosi un sistem AI pentru a decide dacă o persoană este dignă de credit. O companie ar putea folosi un sistem AI pentru a determina candidații cei mai calificați pentru angajare.

- **Confidențialitate și securitate**: Pe măsură ce AI devine tot mai prezentă, protejarea confidențialității și securizarea informațiilor personale și de afaceri devin din ce în ce mai importante și mai complexe. În cazul AI, confidențialitatea și securitatea datelor necesită o atenție atentă, deoarece accesul la date este esențial pentru ca sistemele AI să facă predicții și decizii corecte și informate despre persoane.

- **Responsabilitate**: Persoanele care proiectează și implementează sistemele AI trebuie să fie responsabile pentru modul în care funcționează acestea. Organizațiile ar trebui să se bazeze pe standardele din industrie pentru a dezvolta norme de responsabilitate. Aceste norme pot asigura că sistemele AI nu sunt autoritatea finală în nici o decizie ce afectează viețile oamenilor. De asemenea, pot asigura că oamenii păstrează un control semnificativ asupra sistemelor AI altfel foarte autonome.

![Fill hub.](../../../../../../translated_images/ro/responsibleai2.c07ef430113fad8c.webp)

*Sursa imaginii: [Ce este AI Responsabil?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Pentru a afla mai multe despre Principiile AI responsabile Microsoft, vizitează [Ce este AI responsabil?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metrici de siguranță

În acest tutorial, vei evalua siguranța modelului Phi-3 ajustat fin folosind metricile de siguranță Microsoft Foundry. Aceste metrici te ajută să evaluezi potențialul modelului de a genera conținut dăunător și vulnerabilitatea sa la atacuri jailbreak. Metricile de siguranță includ:

- **Conținut legat de auto-vătămare**: Evaluează dacă modelul are o tendință de a produce conținut legat de auto-vătămare.
- **Conținut urât și nedrept**: Evaluează dacă modelul are o tendință de a produce conținut urât sau nedrept.
- **Conținut violent**: Evaluează dacă modelul are o tendință de a produce conținut violent.
- **Conținut sexual**: Evaluează dacă modelul are o tendință de a produce conținut sexual nepotrivit.

Evaluarea acestor aspecte asigură că modelul AI nu produce conținut dăunător sau ofensator, aliniindu-l la valorile societale și standardele de reglementare.

![Evaluate based on safety.](../../../../../../translated_images/ro/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introducere în evaluarea performanței

Pentru a te asigura că modelul AI funcționează cum te aștepți, este important să îi evaluezi performanța pe baza unor metrici de performanță. În Microsoft Foundry, evaluările de performanță îți permit să evaluezi eficacitatea modelului în generarea unor răspunsuri precise, relevante și coerente.

![Safaty evaluation.](../../../../../../translated_images/ro/performance-evaluation.48b3e7e01a098740.webp)

*Sursa imaginii: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metrici de performanță

În acest tutorial, vei evalua performanța modelului Phi-3 / Phi-3.5 ajustat fin folosind metricile de performanță Microsoft Foundry. Aceste metrici te ajută să evaluezi eficacitatea modelului în generarea unor răspunsuri precise, relevante și coerente. Metricile de performanță includ:

- **Fundamentare**: Evaluează cât de bine răspunsurile generate se aliniază cu informațiile din sursa de intrare.
- **Relevanță**: Evaluează pertinența răspunsurilor generate la întrebările date.
- **Coerență**: Evaluează cât de fluent curge textul generat, dacă este natural și seamănă cu limbajul uman.
- **Fluență**: Evaluează competența lingvistică a textului generat.
- **Similaritate GPT**: Compară răspunsul generat cu adevărul de bază pentru similaritate.
- **Scor F1**: Calculează raportul cuvintelor comune între răspunsul generat și datele sursă.

Aceste metrici te ajută să evaluezi eficacitatea modelului în generarea unor răspunsuri precise, relevante și coerente.

![Evaluate based on performance.](../../../../../../translated_images/ro/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenariul 2: Evaluarea modelului Phi-3 / Phi-3.5 în Microsoft Foundry**

### Înainte de a începe

Acest tutorial este o continuare a postărilor anterioare pe blog, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" și "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." În aceste postări, am parcurs procesul de ajustare fină a unui model Phi-3 / Phi-3.5 în Microsoft Foundry și integrarea acestuia cu Prompt flow.

În acest tutorial, vei implementa un model Azure OpenAI ca evaluator în Microsoft Foundry și îl vei folosi pentru a evalua modelul tău Phi-3 / Phi-3.5 ajustat fin.

Înainte de a începe acest tutorial, asigură-te că ai următoarele precondiții, așa cum au fost descrise în tutorialele anterioare:

1. Un set de date pregătit pentru evaluarea modelului Phi-3 / Phi-3.5 ajustat fin.
1. Un model Phi-3 / Phi-3.5 ajustat fin și implementat în Azure Machine Learning.
1. Un Prompt flow integrat cu modelul tău Phi-3 / Phi-3.5 ajustat fin în Microsoft Foundry.

> [!NOTE]
> Vei folosi fișierul *test_data.jsonl*, situat în folderul data din dataset-ul **ULTRACHAT_200k** descărcat în postările anterioare de pe blog, ca set de date pentru evaluarea modelului Phi-3 / Phi-3.5 ajustat fin.

#### Integrează modelul personalizat Phi-3 / Phi-3.5 cu Prompt flow în Microsoft Foundry (Abordare bazată pe cod)

> [!NOTE]
> Dacă ai urmat abordarea low-code descrisă în "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", poți sări peste acest exercițiu și să continui cu următorul.
> Totuși, dacă ai urmat abordarea bazată pe cod descrisă în "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" pentru a ajusta fin și implementa modelul tău Phi-3 / Phi-3.5, procesul de conectare a modelului la Prompt flow este ușor diferit. Vei învăța acest proces în acest exercițiu.

Pentru a continua, trebuie să integrezi modelul Phi-3 / Phi-3.5 ajustat fin în Prompt flow în Microsoft Foundry.

#### Creează Microsoft Foundry Hub

Trebuie să creezi un Hub înainte de a crea Proiectul. Un Hub funcționează ca un Grup de Resurse, permițându-ți să organizezi și să gestionezi mai multe Proiecte în Microsoft Foundry.
1. Autentificați-vă la [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selectați **All hubs** din fila din partea stângă.

1. Selectați **+ New hub** din meniul de navigație.

    ![Create hub.](../../../../../../translated_images/ro/create-hub.5be78fb1e21ffbf1.webp)

1. Efectuați următoarele sarcini:

    - Introduceți **Hub name**. Trebuie să fie o valoare unică.
    - Selectați **Subscription**-ul Azure.
    - Selectați **Resource group**-ul pe care doriți să îl utilizați (creați unul nou dacă este necesar).
    - Selectați **Location** pe care doriți să o utilizați.
    - Selectați **Connect Azure AI Services** pe care doriți să o utilizați (creați una nouă dacă este necesar).
    - Selectați **Connect Azure AI Search** pentru a **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/ro/fill-hub.baaa108495c71e34.webp)

1. Selectați **Next**.

#### Creați un proiect Microsoft Foundry

1. În Hub-ul pe care l-ați creat, selectați **All projects** din fila din partea stângă.

1. Selectați **+ New project** din meniul de navigație.

    ![Select new project.](../../../../../../translated_images/ro/select-new-project.cd31c0404088d7a3.webp)

1. Introduceți **Project name**. Trebuie să fie o valoare unică.

    ![Create project.](../../../../../../translated_images/ro/create-project.ca3b71298b90e420.webp)

1. Selectați **Create a project**.

#### Adăugarea unei conexiuni personalizate pentru modelul fine-tuned Phi-3 / Phi-3.5

Pentru a integra modelul personalizat Phi-3 / Phi-3.5 cu Prompt flow, trebuie să salvați endpoint-ul și cheia modelului într-o conexiune personalizată. Această configurație asigură accesul la modelul personalizat Phi-3 / Phi-3.5 în Prompt flow.

#### Configurați cheia API și URI-ul endpoint-ului pentru modelul fine-tuned Phi-3 / Phi-3.5

1. Vizitați [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigați la spațiul de lucru Azure Machine Learning pe care l-ați creat.

1. Selectați **Endpoints** din fila din partea stângă.

    ![Select endpoints.](../../../../../../translated_images/ro/select-endpoints.ee7387ecd68bd18d.webp)

1. Selectați endpoint-ul pe care l-ați creat.

    ![Select endpoints.](../../../../../../translated_images/ro/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Selectați **Consume** din meniul de navigație.

1. Copiați **REST endpoint** și **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ro/copy-endpoint-key.0650c3786bd646ab.webp)

#### Adăugați conexiunea personalizată

1. Vizitați [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigați la proiectul Microsoft Foundry pe care l-ați creat.

1. În proiectul pe care l-ați creat, selectați **Settings** din fila din partea stângă.

1. Selectați **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/ro/select-new-connection.fa0f35743758a74b.webp)

1. Selectați **Custom keys** din meniul de navigație.

    ![Select custom keys.](../../../../../../translated_images/ro/select-custom-keys.5a3c6b25580a9b67.webp)

1. Efectuați următoarele sarcini:

    - Selectați **+ Add key value pairs**.
    - Pentru numele cheii, introduceți **endpoint** și inserați endpoint-ul pe care l-ați copiat din Azure ML Studio în câmpul pentru valoare.
    - Selectați din nou **+ Add key value pairs**.
    - Pentru numele cheii, introduceți **key** și inserați cheia pe care ați copiat-o din Azure ML Studio în câmpul pentru valoare.
    - După adăugarea cheilor, selectați **is secret** pentru a preveni expunerea cheii.

    ![Add connection.](../../../../../../translated_images/ro/add-connection.ac7f5faf8b10b0df.webp)

1. Selectați **Add connection**.

#### Creați un Prompt flow

Ați adăugat o conexiune personalizată în Microsoft Foundry. Acum, să creăm un Prompt flow folosind pașii următori. Apoi, veți conecta acest Prompt flow la conexiunea personalizată pentru a utiliza modelul fine-tuned în cadrul Prompt flow.

1. Navigați la proiectul Microsoft Foundry pe care l-ați creat.

1. Selectați **Prompt flow** din fila din partea stângă.

1. Selectați **+ Create** din meniul de navigație.

    ![Select Promptflow.](../../../../../../translated_images/ro/select-promptflow.18ff2e61ab9173eb.webp)

1. Selectați **Chat flow** din meniul de navigație.

    ![Select chat flow.](../../../../../../translated_images/ro/select-flow-type.28375125ec9996d3.webp)

1. Introduceți **Folder name** pe care doriți să îl utilizați.

    ![Select chat flow.](../../../../../../translated_images/ro/enter-name.02ddf8fb840ad430.webp)

1. Selectați **Create**.

#### Configurați Prompt flow pentru a discuta cu modelul personalizat Phi-3 / Phi-3.5

Trebuie să integrați modelul fine-tuned Phi-3 / Phi-3.5 într-un Prompt flow. Totuși, Prompt flow-ul existent nu este conceput pentru acest scop. Prin urmare, trebuie să reproiectați Prompt flow-ul pentru a permite integrarea modelului personalizat.

1. În Prompt flow, efectuați următoarele sarcini pentru a reconstrui fluxul existent:

    - Selectați **Raw file mode**.
    - Ștergeți tot codul existent din fișierul *flow.dag.yml*.
    - Adăugați următorul cod în *flow.dag.yml*.

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

    - Selectați **Save**.

    ![Select raw file mode.](../../../../../../translated_images/ro/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Adăugați următorul cod în *integrate_with_promptflow.py* pentru a folosi modelul personalizat Phi-3 / Phi-3.5 în Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Configurarea jurnalizării
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

        # "connection" este numele Conexiunii Personalizate, "endpoint", "key" sunt cheile din Conexiunea Personalizată
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
            
            # Înregistrează răspunsul complet JSON
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

    ![Paste prompt flow code.](../../../../../../translated_images/ro/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Pentru informații mai detaliate despre utilizarea Prompt flow în Microsoft Foundry, vă puteți consulta cu [Prompt flow în Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selectați **Chat input**, **Chat output** pentru a activa chat-ul cu modelul dvs.

    ![Select Input Output.](../../../../../../translated_images/ro/select-input-output.c187fc58f25fbfc3.webp)

1. Acum sunteți gata să purtați conversații cu modelul personalizat Phi-3 / Phi-3.5. În exercițiul următor, veți învăța cum să porniți Prompt flow și să îl folosiți pentru a discuta cu modelul fine-tuned Phi-3 / Phi-3.5.

> [!NOTE]
>
> Fluxul reconstruit ar trebui să arate ca în imaginea de mai jos:
>
> ![Flow example](../../../../../../translated_images/ro/graph-example.82fd1bcdd3fc545b.webp)
>

#### Porniți Prompt flow

1. Selectați **Start compute sessions** pentru a porni Prompt flow.

    ![Start compute session.](../../../../../../translated_images/ro/start-compute-session.9acd8cbbd2c43df1.webp)

1. Selectați **Validate and parse input** pentru a reînnoi parametrii.

    ![Validate input.](../../../../../../translated_images/ro/validate-input.c1adb9543c6495be.webp)

1. Selectați **Value** pentru **connection** și alegeți conexiunea personalizată pe care ați creat-o. De exemplu, *connection*.

    ![Connection.](../../../../../../translated_images/ro/select-connection.1f2b59222bcaafef.webp)

#### Purtați o conversație cu modelul personalizat Phi-3 / Phi-3.5

1. Selectați **Chat**.

    ![Select chat.](../../../../../../translated_images/ro/select-chat.0406bd9687d0c49d.webp)

1. Iată un exemplu de rezultate: Acum puteți discuta cu modelul personalizat Phi-3 / Phi-3.5. Se recomandă să puneți întrebări bazate pe datele folosite pentru fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/ro/chat-with-promptflow.1cf8cea112359ada.webp)

### Implementați Azure OpenAI pentru a evalua modelul Phi-3 / Phi-3.5

Pentru a evalua modelul Phi-3 / Phi-3.5 în Microsoft Foundry, trebuie să implementați un model Azure OpenAI. Acest model va fi folosit pentru evaluarea performanței modelului Phi-3 / Phi-3.5.

#### Implementați Azure OpenAI

1. Autentificați-vă la [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigați la proiectul Microsoft Foundry pe care l-ați creat.

    ![Select Project.](../../../../../../translated_images/ro/select-project-created.5221e0e403e2c9d6.webp)

1. În proiectul pe care l-ați creat, selectați **Deployments** din fila din partea stângă.

1. Selectați **+ Deploy model** din meniul de navigație.

1. Selectați **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/ro/deploy-openai-model.95d812346b25834b.webp)

1. Selectați modelul Azure OpenAI pe care doriți să îl utilizați. De exemplu, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/ro/select-openai-model.959496d7e311546d.webp)

1. Selectați **Confirm**.

### Evaluați modelul fine-tuned Phi-3 / Phi-3.5 utilizând evaluarea Prompt flow din Microsoft Foundry

### Începeți o evaluare nouă

1. Vizitați [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigați la proiectul Microsoft Foundry pe care l-ați creat.

    ![Select Project.](../../../../../../translated_images/ro/select-project-created.5221e0e403e2c9d6.webp)

1. În proiectul pe care l-ați creat, selectați **Evaluation** din fila din partea stângă.

1. Selectați **+ New evaluation** din meniul de navigație.

    ![Select evaluation.](../../../../../../translated_images/ro/select-evaluation.2846ad7aaaca7f4f.webp)

1. Selectați evaluarea **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/ro/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Efectuați următoarele sarcini:

    - Introduceți numele evaluării. Trebuie să fie o valoare unică.
    - Selectați tipul sarcinii **Question and answer without context** deoarece setul de date **ULTRACHAT_200k** folosit în acest tutorial nu conține context.
    - Selectați prompt flow-ul pe care doriți să îl evaluați.

    ![Prompt flow evaluation.](../../../../../../translated_images/ro/evaluation-setting1.4aa08259ff7a536e.webp)

1. Selectați **Next**.

1. Efectuați următoarele sarcini:

    - Selectați **Add your dataset** pentru a încărca setul de date. De exemplu, puteți încărca fișierul de test al setului de date, cum ar fi *test_data.json1*, care este inclus când descărcați setul de date **ULTRACHAT_200k**.
    - Selectați coloana potrivită a setului de date care corespunde cu datele dvs. De exemplu, dacă utilizați setul de date **ULTRACHAT_200k**, selectați **${data.prompt}** ca și coloană a setului de date.

    ![Prompt flow evaluation.](../../../../../../translated_images/ro/evaluation-setting2.07036831ba58d64e.webp)

1. Selectați **Next**.

1. Configurați următoarele pentru metricele de performanță și calitate:

    - Selectați metricele de performanță și calitate pe care doriți să le utilizați.
    - Selectați modelul Azure OpenAI pe care l-ați creat pentru evaluare. De exemplu, selectați **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/ro/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Configurați următoarele pentru metricele de risc și siguranță:

    - Selectați metricele de risc și siguranță pe care doriți să le utilizați.
    - Selectați pragul pentru calcularea ratei de defect pe care doriți să îl utilizați. De exemplu, selectați **Medium**.
    - Pentru **question**, selectați **Data source** la **{$data.prompt}**.
    - Pentru **answer**, selectați **Data source** la **{$run.outputs.answer}**.
    - Pentru **ground_truth**, selectați **Data source** la **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/ro/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Selectați **Next**.

1. Selectați **Submit** pentru a începe evaluarea.

1. Evaluarea va dura ceva timp. Puteți monitoriza progresul în fila **Evaluation**.

### Revizuiți rezultatele evaluării

> [!NOTE]
> Rezultatele prezentate mai jos sunt menite să ilustreze procesul de evaluare. În acest tutorial, am folosit un model fine-tuned pe un set de date relativ mic, ceea ce poate conduce la rezultate sub-optime. Rezultatele reale pot varia semnificativ în funcție de dimensiunea, calitatea și diversitatea setului de date utilizat, precum și de configurația specifică a modelului.

După finalizarea evaluării, puteți examina rezultatele atât pentru metricele de performanță, cât și pentru cele de siguranță.
1. Metrice de performanță și calitate:

    - evaluează eficacitatea modelului în generarea unor răspunsuri coerente, fluente și relevante.

    ![Evaluation result.](../../../../../../translated_images/ro/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Metrice de risc și siguranță:

    - Asigură că rezultatele modelului sunt sigure și conforme cu Principiile AI Responsabile, evitând orice conținut dăunător sau ofensator.

    ![Evaluation result.](../../../../../../translated_images/ro/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Poți derula în jos pentru a vedea **Rezultatul detaliat al metricilor**.

    ![Evaluation result.](../../../../../../translated_images/ro/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Prin evaluarea modelului personalizat Phi-3 / Phi-3.5 atât în funcție de metricile de performanță, cât și de cele de siguranță, poți confirma că modelul este nu doar eficient, ci și conform practicilor responsabile de AI, fiind pregătit pentru implementarea în lumea reală.

## Felicitări!

### Ai finalizat acest tutorial

Ai evaluat cu succes modelul Phi-3 ajustat, integrat cu Prompt flow în Microsoft Foundry. Acesta este un pas important pentru a asigura că modelele tale AI nu doar funcționează bine, ci respectă și principiile Responsible AI ale Microsoft, ajutându-te să construiești aplicații AI de încredere și fiabile.

![Architecture.](../../../../../../translated_images/ro/architecture.10bec55250f5d6a4.webp)

## Curățarea resurselor Azure

Curăță resursele Azure pentru a evita taxe suplimentare pe contul tău. Accesează portalul Azure și șterge următoarele resurse:

- Resursa Azure Machine learning.
- Endpoint-ul modelului Azure Machine learning.
- Resursa proiect Microsoft Foundry.
- Resursa Prompt flow Microsoft Foundry.

### Pașii următori

#### Documentație

- [Evaluarea sistemelor AI prin utilizarea tabloului de bord Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metrice de evaluare și monitorizare pentru AI generativ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentația Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentația Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Conținut de instruire

- [Introducere în abordarea Responsible AI a Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introducere în Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referințe

- [Ce este Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Anunțarea unor noi instrumente în Azure AI pentru a te ajuta să construiești aplicații AI generative mai sigure și de încredere](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluarea aplicațiilor AI generative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa oficială. Pentru informații critice, se recomandă traducerea profesională umană. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite ce pot apărea în urma utilizării acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->