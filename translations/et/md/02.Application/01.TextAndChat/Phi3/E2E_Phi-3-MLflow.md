# MLflow

[MLflow](https://mlflow.org/) on avatud lähtekoodiga platvorm, mis on loodud masinõppe elutsükli haldamiseks algusest lõpuni.

![MLFlow](../../../../../../imgs/02/mlflow/MlFlowmlops.png)

MLFlow-d kasutatakse ML elutsükli haldamiseks, sealhulgas katsetamiseks, reprodutseeritavuseks, juurutamiseks ja keskse mudeliregistri haldamiseks. MLFlow pakub praegu nelja komponenti:

- **MLflow Tracking:** Eksperimentide, koodi, andmekonfiguratsioonide ja tulemuste salvestamine ja päringud.
- **MLflow Projects:** Andmeteaduse koodi pakendamine formaadis, mis võimaldab käivitada seda mis tahes platvormil.
- **MLflow Models:** Masinõppe mudelite juurutamine erinevates teeninduskeskkondades.
- **Model Registry:** Mudelite salvestamine, märkuste lisamine ja haldamine keskse repository kaudu.

MLFlow sisaldab funktsioone eksperimentide jälgimiseks, koodi pakendamiseks reprodutseeritavateks käivitusteks ning mudelite jagamiseks ja juurutamiseks. MLFlow on integreeritud Databricksiga ja toetab mitmesuguseid ML teeke, muutes selle teekide suhtes neutraalseks. Seda saab kasutada mis tahes masinõppe teegiga ja mis tahes programmeerimiskeeles, kuna see pakub REST API-d ja CLI-d mugavuse huvides.

![MLFlow](../../../../../../imgs/02/mlflow/MLflow2.png)

MLFlow peamised omadused:

- **Eksperimentide jälgimine:** Parameetrite ja tulemuste salvestamine ja võrdlemine.
- **Mudelihaldus:** Mudelite juurutamine erinevates teenindus- ja järelduskeskkondades.
- **Mudeliregister:** MLFlow mudelite elutsükli koostööhaldus, sealhulgas versioonihaldus ja märkused.
- **Projektid:** ML koodi pakendamine jagamiseks või tootmiskasutuseks.

MLFlow toetab ka MLOps-i tsüklit, mis hõlmab andmete ettevalmistamist, mudelite registreerimist ja haldamist, mudelite pakendamist käivitamiseks, teenuste juurutamist ja mudelite jälgimist. Selle eesmärk on lihtsustada prototüübist tootmisvoogu üleminekut, eriti pilve- ja servakeskkondades.

## E2E stsenaarium - Wrapperi loomine ja Phi-3 kasutamine MLFlow mudelina

Selles E2E näites demonstreerime kahte erinevat lähenemist wrapperi loomisele Phi-3 väikese keelemudeli (SLM) ümber ja selle käivitamist MLFlow mudelina kas lokaalselt või pilves, näiteks Azure Machine Learning tööruumis.

![MLFlow](../../../../../../imgs/02/mlflow/MlFlow1.png)

| Projekt | Kirjeldus | Asukoht |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline on lihtsaim võimalus wrapperi loomiseks, kui soovite kasutada HuggingFace mudelit MLFlow eksperimentaalse transformerite maitsega. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Kohandatud Python Wrapper | Kirjutamise ajal ei toetanud transformer pipeline MLFlow wrapperi genereerimist HuggingFace mudelite jaoks ONNX formaadis, isegi eksperimentaalse optimum Python paketi abil. Selliste juhtumite jaoks saate luua kohandatud Python wrapperi MLFlow mudeli jaoks. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Projekt: Transformer Pipeline

1. Vajalikud Python paketid MLFlow ja HuggingFace jaoks:

    ``` Python
    import mlflow
    import transformers
    ```

2. Järgmisena peaksite algatama transformer pipeline'i, viidates sihtmudelile Phi-3 HuggingFace registris. Nagu näha _Phi-3-mini-4k-instruct_ mudelikaardilt, on selle ülesanne "Teksti genereerimine":

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Nüüd saate salvestada oma Phi-3 mudeli transformer pipeline'i MLFlow formaadis ja lisada täiendavaid detaile, nagu sihtarifaktide tee, spetsiifilised mudeli konfiguratsiooniseaded ja järeldus API tüüp:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Projekt: Kohandatud Python Wrapper

1. Siin saame kasutada Microsofti [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) ONNX mudeli järelduste ja tokenite kodeerimise/dekodeerimise jaoks. Peate valima _onnxruntime_genai_ paketi oma sihtarvutuse jaoks, allolevas näites sihtides CPU-d:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Meie kohandatud klass rakendab kahte meetodit: _load_context()_ Phi-3 Mini 4K Instruct **ONNX mudeli**, **generaatori parameetrite** ja **tokenizeri** algatamiseks; ning _predict()_ väljundtokenite genereerimiseks antud prompti jaoks:

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # Retrieving model from the artifacts
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # Defining the model
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # Defining the tokenizer
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # Retrieving prompt from the input
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # Generating the model's response
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

1. Nüüd saate kasutada _mlflow.pyfunc.log_model()_ funktsiooni, et genereerida kohandatud Python wrapper (pickle formaadis) Phi-3 mudeli jaoks koos algse ONNX mudeli ja vajalike sõltuvustega:

    ``` Python
    model_info = mlflow.pyfunc.log_model(
        artifact_path = artifact_path,
        python_model = Phi3Model(),
        artifacts = {
            "phi3-mini-onnx": "cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4",
        },
        input_example = input_example,
        signature = infer_signature(input_example, ["Run"]),
        extra_pip_requirements = ["torch", "onnxruntime_genai", "numpy"],
    )
    ```

## Genereeritud MLFlow mudelite signatuurid

1. Transformer Pipeline projekti 3. sammus määrasime MLFlow mudeli ülesandeks "_llm/v1/chat_". Selline juhis genereerib mudeli API wrapperi, mis on ühilduv OpenAI Chat API-ga, nagu allpool näidatud:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Selle tulemusena saate esitada oma prompti järgmises formaadis:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Seejärel kasutage OpenAI API-ga ühilduvat järeltöötlust, näiteks _response[0][‘choices’][0][‘message’][‘content’]_, et muuta oma väljund millekski selliseks:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. Kohandatud Python Wrapper projekti 3. sammus lubame MLFlow paketil genereerida mudeli signatuuri antud sisendi näite põhjal. Meie MLFlow wrapperi signatuur näeb välja selline:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Seega peab meie prompt sisaldama "prompt" sõnastiku võtit, mis näeb välja selline:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Mudeli väljund esitatakse seejärel stringi formaadis:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.