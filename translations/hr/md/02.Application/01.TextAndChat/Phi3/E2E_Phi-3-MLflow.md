<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:36:46+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "hr"
}
-->
# MLflow

[MLflow](https://mlflow.org/) je open-source platforma dizajnirana za upravljanje cjelokupnim životnim ciklusom strojnog učenja.

![MLFlow](../../../../../../translated_images/hr/MlFlowmlops.ed16f47809d74d9a.png)

MLFlow se koristi za upravljanje životnim ciklusom strojnog učenja, uključujući eksperimentiranje, reproducibilnost, implementaciju i centralni registar modela. Trenutno MLflow nudi četiri komponente.

- **MLflow Tracking:** Evidentiranje i pretraživanje eksperimenata, koda, konfiguracije podataka i rezultata.
- **MLflow Projects:** Pakiranje koda za podatkovnu znanost u format koji omogućuje reproduciranje pokretanja na bilo kojoj platformi.
- **Mlflow Models:** Implementacija modela strojnog učenja u različitim okruženjima za posluživanje.
- **Model Registry:** Pohrana, označavanje i upravljanje modelima u centralnom spremištu.

Uključuje mogućnosti za praćenje eksperimenata, pakiranje koda u reproducibilne pokrete te dijeljenje i implementaciju modela. MLFlow je integriran u Databricks i podržava razne ML biblioteke, što ga čini neovisnim o biblioteci. Može se koristiti s bilo kojom bibliotekom strojnog učenja i u bilo kojem programskom jeziku, jer pruža REST API i CLI radi praktičnosti.

![MLFlow](../../../../../../translated_images/hr/MLflow2.5a22eb718f6311d1.png)

Ključne značajke MLFlow uključuju:

- **Praćenje eksperimenata:** Evidentiranje i usporedba parametara i rezultata.
- **Upravljanje modelima:** Implementacija modela na različite platforme za posluživanje i izvođenje.
- **Model Registry:** Zajedničko upravljanje životnim ciklusom MLflow modela, uključujući verzioniranje i označavanje.
- **Projects:** Pakiranje ML koda za dijeljenje ili produkcijsku upotrebu.

MLFlow također podržava MLOps ciklus, koji uključuje pripremu podataka, registraciju i upravljanje modelima, pakiranje modela za izvršavanje, implementaciju servisa i nadzor modela. Cilj mu je pojednostaviti prijelaz od prototipa do produkcijskog tijeka rada, osobito u cloud i edge okruženjima.

## E2E scenarij - Izrada omotača i korištenje Phi-3 kao MLFlow modela

U ovom E2E primjeru prikazat ćemo dva različita pristupa izradi omotača oko malog jezičnog modela Phi-3 (SLM) i njegovo pokretanje kao MLFlow modela lokalno ili u oblaku, npr. u Azure Machine Learning radnom prostoru.

![MLFlow](../../../../../../translated_images/hr/MlFlow1.fd745e47dbd3fecf.png)

| Projekt | Opis | Lokacija |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline je najjednostavnija opcija za izradu omotača ako želite koristiti HuggingFace model s eksperimentalnim transformers okusom MLFlow-a. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | U trenutku pisanja, transformer pipeline nije podržavao generiranje MLFlow omotača za HuggingFace modele u ONNX formatu, čak ni s eksperimentalnim optimum Python paketom. Za takve slučajeve možete izraditi vlastiti Python omotač za MLFlow model. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Projekt: Transformer Pipeline

1. Trebat će vam odgovarajući Python paketi iz MLFlow i HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Zatim biste trebali inicijalizirati transformer pipeline pozivajući ciljani Phi-3 model iz HuggingFace registra. Kao što se vidi iz kartice modela _Phi-3-mini-4k-instruct_, njegov zadatak je tipa „Text Generation“:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Sada možete spremiti transformer pipeline vašeg Phi-3 modela u MLFlow format i pružiti dodatne detalje poput ciljne putanje artefakata, specifičnih postavki konfiguracije modela i tipa inference API-ja:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Projekt: Custom Python Wrapper

1. Ovdje možemo iskoristiti Microsoftov [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) za izvođenje inferencije ONNX modela i kodiranje/dekodiranje tokena. Morate odabrati _onnxruntime_genai_ paket za ciljanu računalnu platformu, a u donjem primjeru je cilj CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Naša prilagođena klasa implementira dvije metode: _load_context()_ za inicijalizaciju **ONNX modela** Phi-3 Mini 4K Instruct, **parametara generatora** i **tokenizatora**; te _predict()_ za generiranje izlaznih tokena za zadani prompt:

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

1. Sada možete koristiti funkciju _mlflow.pyfunc.log_model()_ za generiranje prilagođenog Python omotača (u pickle formatu) za Phi-3 model, zajedno s izvornim ONNX modelom i potrebnim ovisnostima:

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

## Potpisi generiranih MLFlow modela

1. U koraku 3 projekta Transformer Pipeline gore, postavili smo zadatak MLFlow modela na „_llm/v1/chat_“. Takva uputa generira API omotač modela, kompatibilan s OpenAI Chat API-jem kao što je prikazano dolje:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Kao rezultat, možete poslati svoj prompt u sljedećem formatu:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Zatim koristite postprocesiranje kompatibilno s OpenAI API-jem, npr. _response[0][‘choices’][0][‘message’][‘content’]_, kako biste ulazni odgovor oblikovali u nešto poput ovoga:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. U koraku 3 projekta Custom Python Wrapper gore, dopuštamo MLFlow paketu da generira potpis modela na temelju danog primjera ulaza. Potpis našeg MLFlow omotača izgledat će ovako:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Dakle, naš prompt bi trebao sadržavati ključ rječnika "prompt", slično ovome:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Izlaz modela tada će biti dan u obliku stringa:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.