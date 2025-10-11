<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-10-11T12:10:27+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "ta"
}
-->
# MLflow

[MLflow](https://mlflow.org/) என்பது முழுமையான இயந்திரக் கற்றல் வாழ்க்கைச் சுழற்சியை நிர்வகிக்க வடிவமைக்கப்பட்ட திறந்த மூல தளம் ஆகும்.

![MLFlow](../../../../../../imgs/02/mlflow/MlFlowmlops.png)

MLFlow இயந்திரக் கற்றல் வாழ்க்கைச் சுழற்சியை நிர்வகிக்கப் பயன்படுகிறது, இதில் பரிசோதனைகள், மீளஉருவாக்கம், பிரசாரம் மற்றும் மைய மாடல் பதிவேடு ஆகியவை அடங்கும். MLFlow தற்போது நான்கு கூறுகளை வழங்குகிறது:

- **MLflow Tracking:** பரிசோதனைகள், குறியீடு, தரவுக் கட்டமைப்பு மற்றும் முடிவுகளை பதிவு செய்து கேட்க.
- **MLflow Projects:** தரவியல் அறிவியல் குறியீட்டை எந்த தளத்திலும் இயக்கங்களை மீளஉருவாக்கும் வடிவத்தில் தொகுக்க.
- **Mlflow Models:** இயந்திரக் கற்றல் மாடல்களை பல்வேறு சேவை சூழல்களில் பிரசாரம் செய்ய.
- **Model Registry:** மையக் களஞ்சியத்தில் மாடல்களை சேமிக்க, குறிப்பிட்டு நிர்வகிக்க.

இது பரிசோதனைகளைப் பதிவு செய்வதற்கான திறன்களை, மீளஉருவாக்கக்கூடிய இயக்கங்களுக்கான குறியீட்டை தொகுப்பதற்கான திறன்களை, மற்றும் மாடல்களைப் பகிர்ந்து பிரசாரம் செய்வதற்கான திறன்களை உள்ளடக்கியது. MLFlow Databricks-இல் ஒருங்கிணைக்கப்பட்டுள்ளது மற்றும் பல்வேறு ML நூலகங்களை ஆதரிக்கிறது, இதனால் இது நூலகத்திற்கு சார்பற்றது. இது எந்த இயந்திரக் கற்றல் நூலகத்துடனும் மற்றும் எந்த நிரலாக்க மொழியுடனும் பயன்படுத்தப்படலாம், ஏனெனில் இது வசதிக்காக REST API மற்றும் CLI-ஐ வழங்குகிறது.

![MLFlow](../../../../../../imgs/02/mlflow/MLflow2.png)

MLFlow-இன் முக்கிய அம்சங்கள்:

- **Experiment Tracking:** அளவுருக்கள் மற்றும் முடிவுகளைப் பதிவு செய்து ஒப்பிடுங்கள்.
- **Model Management:** மாடல்களை பல்வேறு சேவை மற்றும் தீர்மானம் செய்யும் தளங்களுக்கு பிரசாரம் செய்யுங்கள்.
- **Model Registry:** MLFlow மாடல்களின் வாழ்க்கைச் சுழற்சியை ஒத்துழைத்துப் நிர்வகிக்க, பதிப்பீடு மற்றும் குறிப்புகளை உள்ளடக்கியது.
- **Projects:** பகிர்வதற்காக அல்லது உற்பத்தி பயன்பாட்டிற்காக ML குறியீட்டை தொகுக்க.

MLFlow MLOps சுழற்சியையும் ஆதரிக்கிறது, இதில் தரவுகளைத் தயாரித்தல், மாடல்களைப் பதிவு செய்து நிர்வகித்தல், மாடல்களை செயல்படுத்த தொகுப்பதற்கான செயல்பாடுகள், சேவைகளை பிரசாரம் செய்தல் மற்றும் மாடல்களை கண்காணித்தல் ஆகியவை அடங்கும். இது குறிப்பாக மேக மற்றும் விளிம்பு சூழல்களில் ஒரு மாதிரியில் இருந்து உற்பத்தி வேலைப்பாடுகளுக்கு நகரும் செயல்முறையை எளிமையாக்க முயற்சிக்கிறது.

## E2E காட்சி - ஒரு மடக்கியை உருவாக்குதல் மற்றும் Phi-3 ஐ MLFlow மாடலாக பயன்படுத்துதல்

இந்த E2E மாதிரியில், Phi-3 சிறிய மொழி மாடல் (SLM) சுற்றி ஒரு மடக்கியை உருவாக்குவதற்கான இரண்டு வெவ்வேறு அணுகுமுறைகளை விளக்கி, அதை உள்ளூர் அல்லது மேகத்தில், உதாரணமாக Azure Machine Learning workspace-இல் MLFlow மாடலாக இயக்குவோம்.

![MLFlow](../../../../../../imgs/02/mlflow/MlFlow1.png)

| திட்டம் | விளக்கம் | இடம் |
| ------------ | ----------- | -------- |
| Transformer Pipeline | HuggingFace மாடலை MLFlow இன் பரிசோதனையான transformers flavour உடன் பயன்படுத்த விரும்பினால், Transformer Pipeline ஒரு மடக்கியை உருவாக்குவதற்கான எளிய விருப்பமாகும். | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | இந்த நேரத்தில், transformer pipeline ONNX வடிவத்தில் HuggingFace மாடல்களுக்கு MLFlow மடக்கி உருவாக்கலை ஆதரிக்கவில்லை, பரிசோதனையான optimum Python தொகுப்புடன் கூட. இவ்வாறான சந்தர்ப்பங்களில், MLFlow முறைமைக்கு உங்கள் தனிப்பயன் Python மடக்கியை உருவாக்கலாம். | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## திட்டம்: Transformer Pipeline

1. MLFlow மற்றும் HuggingFace-இன் தொடர்புடைய Python தொகுப்புகள் தேவைப்படும்:

    ``` Python
    import mlflow
    import transformers
    ```

2. HuggingFace பதிவேட்டில் உள்ள இலக்கு Phi-3 மாடலை குறிப்பிடுவதன் மூலம் ஒரு transformer pipeline-ஐ தொடங்க வேண்டும். _Phi-3-mini-4k-instruct_ மாடல் கார்டில் இருந்து தெரிகிறது, இதன் பணியானது "Text Generation" வகையைச் சேர்ந்தது:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. இப்போது உங்கள் Phi-3 மாடலின் transformer pipeline-ஐ MLFlow வடிவத்தில் சேமித்து, இலக்கு கலைப்பொருட்கள் பாதை, குறிப்பிட்ட மாடல் கட்டமைப்பு அமைப்புகள் மற்றும் தீர்மான API வகை போன்ற கூடுதல் விவரங்களை வழங்கலாம்:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## திட்டம்: Custom Python Wrapper

1. ONNX மாடலின் தீர்மானம் மற்றும் டோக்கன்கள் குறியாக்கம் / குறியீடாக்கத்திற்காக Microsoft's [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai)-ஐ இங்கு பயன்படுத்தலாம். உங்கள் இலக்கு கணினிக்கான _onnxruntime_genai_ தொகுப்பை தேர்ந்தெடுக்க வேண்டும், கீழே உள்ள உதாரணம் CPU-ஐ இலக்காகக் கொண்டது:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. எங்கள் தனிப்பயன் வகுப்பு இரண்டு முறைகளை செயல்படுத்துகிறது: _load_context()_ என்பது Phi-3 Mini 4K Instruct இன் **ONNX மாடல்**, **தீர்மான அளவுருக்கள்** மற்றும் **tokenizer**-ஐ தொடங்க; மற்றும் _predict()_ என்பது வழங்கப்பட்ட prompt-க்கு output tokens-ஐ உருவாக்க:

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

1. இப்போது _mlflow.pyfunc.log_model()_ செயல்பாட்டைப் பயன்படுத்தி Phi-3 மாடலுக்கான தனிப்பயன் Python மடக்கியை (pickle வடிவத்தில்) உருவாக்கலாம், அதற்குடன் மூல ONNX மாடல் மற்றும் தேவையான சார்புகளை சேர்த்துக் கொள்ளலாம்:

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

## உருவாக்கப்பட்ட MLFlow மாடல்களின் கையொப்பங்கள்

1. Transformer Pipeline திட்டத்தின் 3-வது படியில், MLFlow மாடலின் பணியை "_llm/v1/chat_" என்று அமைத்தோம். இவ்வாறான வழிகாட்டுதல் OpenAI இன் Chat API உடன் இணக்கமான மாடல் API மடக்கியை உருவாக்குகிறது, கீழே காட்டப்பட்டுள்ளபடி:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. இதன் விளைவாக, உங்கள் prompt-ஐ பின்வரும் வடிவத்தில் சமர்ப்பிக்கலாம்:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. பின்னர், OpenAI API-இன் இணக்கமான post-processing, உதாரணமாக _response[0][‘choices’][0][‘message’][‘content’]_ போன்றவற்றைப் பயன்படுத்தி, உங்கள் output-ஐ கீழே உள்ள மாதிரி போல அழகுபடுத்தலாம்:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. Custom Python Wrapper திட்டத்தின் 3-வது படியில், கொடுக்கப்பட்ட உள்ளீடு உதாரணத்திலிருந்து MLFlow தொகுப்பை மாடலின் கையொப்பத்தை உருவாக்க அனுமதிக்கிறோம். எங்கள் MLFlow மடக்கியின் கையொப்பம் இதுபோல இருக்கும்:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. எனவே, எங்கள் prompt "prompt" என்ற dictionary key-ஐ கொண்டிருக்க வேண்டும், இதுபோல:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. பின்னர், மாடலின் output string வடிவத்தில் வழங்கப்படும்:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.