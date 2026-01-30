# MLflow

[MLflow](https://mlflow.org/) yra atvirojo kodo platforma, skirta valdyti visą mašininio mokymosi gyvavimo ciklą.

![MLFlow](../../../../../../imgs/02/mlflow/MlFlowmlops.png)

MLFlow naudojamas ML gyvavimo ciklui valdyti, įskaitant eksperimentavimą, atkuriamumą, diegimą ir centrinį modelių registrą. Šiuo metu MLFlow siūlo keturis komponentus:

- **MLflow Tracking:** Eksperimentų, kodo, duomenų konfigūracijų ir rezultatų registravimas bei užklausos.
- **MLflow Projects:** Duomenų mokslo kodo paketavimas formatu, leidžiančiu atkurti vykdymą bet kurioje platformoje.
- **MLflow Models:** Mašininio mokymosi modelių diegimas įvairiose aptarnavimo aplinkose.
- **Model Registry:** Modelių saugojimas, anotavimas ir valdymas centrinėje saugykloje.

MLFlow apima funkcijas eksperimentų stebėjimui, kodo paketavimui į atkuriamus vykdymus, modelių dalijimuisi ir diegimu. MLFlow yra integruotas į Databricks ir palaiko įvairias ML bibliotekas, todėl yra nepriklausomas nuo bibliotekų. Jis gali būti naudojamas su bet kuria mašininio mokymosi biblioteka ir bet kuria programavimo kalba, nes siūlo REST API ir CLI patogumui.

![MLFlow](../../../../../../imgs/02/mlflow/MLflow2.png)

Pagrindinės MLFlow savybės:

- **Eksperimentų stebėjimas:** Parametrų ir rezultatų registravimas bei palyginimas.
- **Modelių valdymas:** Modelių diegimas įvairiose aptarnavimo ir prognozavimo platformose.
- **Modelių registras:** Bendradarbiavimas valdant MLFlow modelių gyvavimo ciklą, įskaitant versijavimą ir anotacijas.
- **Projektai:** ML kodo paketavimas dalijimuisi arba naudojimui gamyboje.

MLFlow taip pat palaiko MLOps ciklą, kuris apima duomenų paruošimą, modelių registravimą ir valdymą, modelių paketavimą vykdymui, paslaugų diegimą ir modelių stebėjimą. Jo tikslas yra supaprastinti perėjimą nuo prototipo prie gamybinio darbo proceso, ypač debesų ir kraštinėse aplinkose.

## E2E scenarijus - Apvalkalo kūrimas ir Phi-3 naudojimas kaip MLFlow modelis

Šiame E2E pavyzdyje demonstruosime du skirtingus būdus, kaip sukurti apvalkalą aplink mažą kalbos modelį Phi-3 (SLM) ir paleisti jį kaip MLFlow modelį vietoje arba debesyje, pvz., Azure Machine Learning darbo erdvėje.

![MLFlow](../../../../../../imgs/02/mlflow/MlFlow1.png)

| Projektas | Aprašymas | Vieta |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline yra lengviausias būdas sukurti apvalkalą, jei norite naudoti HuggingFace modelį su MLFlow eksperimentiniu transformatorių formatu. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | Rašymo metu transformatorių pipeline nepalaikė MLFlow apvalkalo generavimo HuggingFace modeliams ONNX formatu, net naudojant eksperimentinį optimum Python paketą. Tokiais atvejais galite sukurti savo Python apvalkalą MLFlow modeliui. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Projektas: Transformer Pipeline

1. Jums reikės atitinkamų Python paketų iš MLFlow ir HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Toliau turėtumėte inicijuoti transformatorių pipeline, nurodydami tikslinį Phi-3 modelį HuggingFace registre. Kaip matyti iš _Phi-3-mini-4k-instruct_ modelio kortelės, jo užduotis yra „Teksto generavimas“:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Dabar galite išsaugoti Phi-3 modelio transformatorių pipeline MLFlow formatu ir pateikti papildomą informaciją, pvz., tikslinį artefaktų kelią, specifinius modelio konfigūracijos nustatymus ir prognozavimo API tipą:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Projektas: Custom Python Wrapper

1. Čia galime pasinaudoti Microsoft [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) ONNX modelio prognozavimui ir žetonų kodavimui / dekodavimui. Turite pasirinkti _onnxruntime_genai_ paketą savo tiksliniam kompiuteriui, pavyzdžiui, žemiau pateiktame pavyzdyje, skirtame CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Mūsų pasirinktinė klasė įgyvendina du metodus: _load_context()_ inicializuoti **ONNX modelį** Phi-3 Mini 4K Instruct, **generatoriaus parametrus** ir **tokenizer**; ir _predict()_ generuoti išvesties žetonus pagal pateiktą užklausą:

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

1. Dabar galite naudoti _mlflow.pyfunc.log_model()_ funkciją, kad sukurtumėte pasirinktinį Python apvalkalą (pickle formatu) Phi-3 modeliui, kartu su originaliu ONNX modeliu ir reikalingomis priklausomybėmis:

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

## Sukurtų MLFlow modelių parašai

1. 3 žingsnyje Transformer Pipeline projekte aukščiau, mes nustatėme MLFlow modelio užduotį kaip „_llm/v1/chat_“. Tokia instrukcija generuoja modelio API apvalkalą, suderinamą su OpenAI Chat API, kaip parodyta žemiau:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Dėl to galite pateikti savo užklausą tokiu formatu:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Tada naudokite OpenAI API suderinamą post-apdorojimą, pvz., _response[0][‘choices’][0][‘message’][‘content’]_, kad gražintumėte išvestį į kažką panašaus:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. 3 žingsnyje Custom Python Wrapper projekte aukščiau, leidžiame MLFlow paketui generuoti modelio parašą pagal pateiktą įvesties pavyzdį. Mūsų MLFlow apvalkalo parašas atrodys taip:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Taigi, mūsų užklausa turėtų turėti „prompt“ žodyno raktą, panašų į šį:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Modelio išvestis bus pateikta tada kaip eilutės formatas:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.