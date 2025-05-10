<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-05-09T18:36:39+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "it"
}
-->
# MLflow

[MLflow](https://mlflow.org/) è una piattaforma open-source progettata per gestire l'intero ciclo di vita del machine learning.

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.it.png)

MLFlow viene utilizzato per gestire il ciclo di vita del ML, inclusi sperimentazione, riproducibilità, deployment e un registro centrale dei modelli. Attualmente MLflow offre quattro componenti.

- **MLflow Tracking:** Registra e interroga esperimenti, codice, configurazioni dati e risultati.
- **MLflow Projects:** Confeziona il codice di data science in un formato che permette di riprodurre le esecuzioni su qualsiasi piattaforma.
- **Mlflow Models:** Distribuisce modelli di machine learning in diversi ambienti di serving.
- **Model Registry:** Archivia, annota e gestisce i modelli in un repository centrale.

Include funzionalità per tracciare gli esperimenti, confezionare il codice in esecuzioni riproducibili, condividere e distribuire modelli. MLFlow è integrato in Databricks e supporta diverse librerie di ML, risultando quindi indipendente dalla libreria utilizzata. Può essere usato con qualsiasi libreria di machine learning e in qualsiasi linguaggio di programmazione, grazie alla disponibilità di un'API REST e di una CLI per comodità.

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.it.png)

Le caratteristiche principali di MLFlow includono:

- **Experiment Tracking:** Registra e confronta parametri e risultati.
- **Model Management:** Distribuisce modelli su varie piattaforme di serving e inferenza.
- **Model Registry:** Gestisce in modo collaborativo il ciclo di vita dei modelli MLflow, inclusa la versione e le annotazioni.
- **Projects:** Confeziona il codice ML per condivisione o utilizzo in produzione.

MLFlow supporta anche il ciclo MLOps, che comprende la preparazione dei dati, la registrazione e gestione dei modelli, il confezionamento dei modelli per l’esecuzione, il deployment dei servizi e il monitoraggio dei modelli. Mira a semplificare il passaggio da prototipo a flusso di lavoro di produzione, specialmente in ambienti cloud e edge.

## Scenario E2E - Costruire un wrapper e usare Phi-3 come modello MLFlow

In questo esempio E2E mostreremo due approcci diversi per costruire un wrapper attorno al modello di linguaggio piccolo Phi-3 (SLM) e poi eseguirlo come modello MLFlow, sia localmente che nel cloud, ad esempio in Azure Machine Learning workspace.

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.it.png)

| Progetto | Descrizione | Posizione |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline è l’opzione più semplice per costruire un wrapper se vuoi usare un modello HuggingFace con il flavour sperimentale transformers di MLFlow. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | Al momento della scrittura, il transformer pipeline non supportava la generazione di wrapper MLFlow per modelli HuggingFace in formato ONNX, neanche con il pacchetto Python sperimentale optimum. In casi come questo, puoi costruire un wrapper Python personalizzato per il modello MLFlow | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Progetto: Transformer Pipeline

1. Avrai bisogno dei pacchetti Python rilevanti da MLFlow e HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Successivamente, devi inizializzare una transformer pipeline facendo riferimento al modello Phi-3 target nel registro HuggingFace. Come si vede dalla scheda modello di _Phi-3-mini-4k-instruct_, il suo task è di tipo “Text Generation”:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Ora puoi salvare la transformer pipeline del modello Phi-3 in formato MLFlow e fornire dettagli aggiuntivi come il percorso degli artefatti di destinazione, configurazioni specifiche del modello e il tipo di API di inferenza:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Progetto: Custom Python Wrapper

1. Qui possiamo utilizzare l’API generate() di Microsoft [ONNX Runtime](https://github.com/microsoft/onnxruntime-genai) per l’inferenza del modello ONNX e per la codifica/decodifica dei token. Devi scegliere il pacchetto _onnxruntime_genai_ per il tuo compute target, nell’esempio sotto si punta a CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. La nostra classe personalizzata implementa due metodi: _load_context()_ per inizializzare il **modello ONNX** di Phi-3 Mini 4K Instruct, i **parametri del generatore** e il **tokenizer**; e _predict()_ per generare i token di output a partire dal prompt fornito:

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

1. Ora puoi usare la funzione _mlflow.pyfunc.log_model()_ per generare un wrapper Python personalizzato (in formato pickle) per il modello Phi-3, insieme al modello ONNX originale e alle dipendenze necessarie:

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

## Signature dei modelli MLFlow generati

1. Nel passo 3 del progetto Transformer Pipeline sopra, abbiamo impostato il task del modello MLFlow su “_llm/v1/chat_”. Questa istruzione genera un wrapper API per il modello, compatibile con l’API Chat di OpenAI come mostrato di seguito:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Di conseguenza, puoi inviare il tuo prompt nel formato seguente:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Poi, usa il post-processing compatibile con OpenAI API, ad esempio _response[0][‘choices’][0][‘message’][‘content’]_, per formattare il tuo output in qualcosa del genere:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. Nel passo 3 del progetto Custom Python Wrapper sopra, permettiamo al pacchetto MLFlow di generare la signature del modello a partire da un esempio di input. La signature del nostro wrapper MLFlow sarà simile a questa:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Quindi, il nostro prompt dovrà contenere la chiave dizionario "prompt", simile a questo:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. L’output del modello sarà quindi fornito in formato stringa:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.