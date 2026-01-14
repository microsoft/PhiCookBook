<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:29:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "pa"
}
-->
# MLflow

[MLflow](https://mlflow.org/) ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਪਲੇਟਫਾਰਮ ਹੈ ਜੋ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਦੇ ਪੂਰੇ ਲਾਈਫਸਾਈਕਲ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ।

![MLFlow](../../../../../../translated_images/pa/MlFlowmlops.ed16f47809d74d9a.png)

MLFlow ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਦੇ ਲਾਈਫਸਾਈਕਲ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਪ੍ਰਯੋਗ, ਦੁਹਰਾਅਯੋਗਤਾ, ਡਿਪਲੋਇਮੈਂਟ ਅਤੇ ਕੇਂਦਰੀ ਮਾਡਲ ਰਜਿਸਟਰੀ ਸ਼ਾਮਲ ਹਨ। MLflow ਇਸ ਸਮੇਂ ਚਾਰ ਹਿੱਸੇ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

- **MLflow Tracking:** ਪ੍ਰਯੋਗਾਂ, ਕੋਡ, ਡਾਟਾ ਕਨਫਿਗ ਅਤੇ ਨਤੀਜਿਆਂ ਨੂੰ ਦਰਜ ਅਤੇ ਪੁੱਛਗਿੱਛ ਕਰੋ।
- **MLflow Projects:** ਡਾਟਾ ਸਾਇੰਸ ਕੋਡ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਪੈਕੇਜ ਕਰੋ ਕਿ ਕਿਸੇ ਵੀ ਪਲੇਟਫਾਰਮ 'ਤੇ ਦੁਹਰਾਏ ਜਾ ਸਕਣ।
- **Mlflow Models:** ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਸਰਵਿੰਗ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਡਿਪਲੋਇ ਕਰੋ।
- **Model Registry:** ਮਾਡਲਾਂ ਨੂੰ ਕੇਂਦਰੀ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ ਸਟੋਰ, ਟਿੱਪਣੀ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰੋ।

ਇਸ ਵਿੱਚ ਪ੍ਰਯੋਗਾਂ ਦੀ ਟ੍ਰੈਕਿੰਗ, ਕੋਡ ਨੂੰ ਦੁਹਰਾਅਯੋਗ ਰਨ ਵਿੱਚ ਪੈਕੇਜ ਕਰਨ ਅਤੇ ਮਾਡਲਾਂ ਨੂੰ ਸਾਂਝਾ ਕਰਨ ਅਤੇ ਡਿਪਲੋਇ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਹੈ। MLFlow ਨੂੰ Databricks ਵਿੱਚ ਇੰਟੀਗ੍ਰੇਟ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਇਹ ਕਈ ML ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ, ਇਸ ਲਈ ਇਹ ਲਾਇਬ੍ਰੇਰੀ-ਅਗਨੋਸਟਿਕ ਹੈ। ਇਹ ਕਿਸੇ ਵੀ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ ਕਿਸੇ ਵੀ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾ ਨਾਲ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਕਿਉਂਕਿ ਇਹ ਸੁਵਿਧਾ ਲਈ REST API ਅਤੇ CLI ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

![MLFlow](../../../../../../translated_images/pa/MLflow2.5a22eb718f6311d1.png)

MLFlow ਦੀਆਂ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

- **Experiment Tracking:** ਪੈਰਾਮੀਟਰਾਂ ਅਤੇ ਨਤੀਜਿਆਂ ਨੂੰ ਦਰਜ ਅਤੇ ਤੁਲਨਾ ਕਰੋ।
- **Model Management:** ਮਾਡਲਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਸਰਵਿੰਗ ਅਤੇ ਇੰਫਰੈਂਸ ਪਲੇਟਫਾਰਮਾਂ 'ਤੇ ਡਿਪਲੋਇ ਕਰੋ।
- **Model Registry:** MLflow ਮਾਡਲਾਂ ਦੇ ਲਾਈਫਸਾਈਕਲ ਨੂੰ ਸਾਂਝੇ ਤੌਰ 'ਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰੋ, ਜਿਸ ਵਿੱਚ ਵਰਜਨਿੰਗ ਅਤੇ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਲ ਹਨ।
- **Projects:** ML ਕੋਡ ਨੂੰ ਸਾਂਝਾ ਕਰਨ ਜਾਂ ਉਤਪਾਦਨ ਲਈ ਪੈਕੇਜ ਕਰੋ।

MLFlow MLOps ਲੂਪ ਨੂੰ ਵੀ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਡਾਟਾ ਤਿਆਰ ਕਰਨਾ, ਮਾਡਲਾਂ ਨੂੰ ਰਜਿਸਟਰ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰਨਾ, ਮਾਡਲਾਂ ਨੂੰ ਚਲਾਉਣ ਲਈ ਪੈਕੇਜ ਕਰਨਾ, ਸੇਵਾਵਾਂ ਨੂੰ ਡਿਪਲੋਇ ਕਰਨਾ ਅਤੇ ਮਾਡਲਾਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ। ਇਹ ਪ੍ਰੋਟੋਟਾਈਪ ਤੋਂ ਉਤਪਾਦਨ ਵਰਕਫਲੋ ਤੱਕ ਦੇ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਆਸਾਨ ਬਣਾਉਣ ਦਾ ਲਕਸ਼ ਹੈ, ਖਾਸ ਕਰਕੇ ਕਲਾਉਡ ਅਤੇ ਐਜ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ।

## E2E ਸਿਨਾਰੀਓ - ਇੱਕ ਰੈਪਰ ਬਣਾਉਣਾ ਅਤੇ Phi-3 ਨੂੰ MLFlow ਮਾਡਲ ਵਜੋਂ ਵਰਤਣਾ

ਇਸ E2E ਉਦਾਹਰਨ ਵਿੱਚ ਅਸੀਂ ਦੋ ਵੱਖ-ਵੱਖ ਤਰੀਕੇ ਦਿਖਾਵਾਂਗੇ ਜਿਨ੍ਹਾਂ ਨਾਲ Phi-3 ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਦੇ ਆਲੇ-ਦੁਆਲੇ ਇੱਕ ਰੈਪਰ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ ਫਿਰ ਇਸਨੂੰ MLFlow ਮਾਡਲ ਵਜੋਂ ਸਥਾਨਕ ਜਾਂ ਕਲਾਉਡ ਵਿੱਚ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ, ਉਦਾਹਰਨ ਵਜੋਂ Azure Machine Learning ਵਰਕਸਪੇਸ ਵਿੱਚ।

![MLFlow](../../../../../../translated_images/pa/MlFlow1.fd745e47dbd3fecf.png)

| ਪ੍ਰੋਜੈਕਟ | ਵੇਰਵਾ | ਸਥਾਨ |
| ------------ | ----------- | -------- |
| Transformer Pipeline | ਜੇ ਤੁਸੀਂ MLFlow ਦੇ ਪ੍ਰਯੋਗਾਤਮਕ transformers ਫਲੇਵਰ ਨਾਲ HuggingFace ਮਾਡਲ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ Transformer Pipeline ਰੈਪਰ ਬਣਾਉਣ ਦਾ ਸਭ ਤੋਂ ਆਸਾਨ ਵਿਕਲਪ ਹੈ। | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | ਲਿਖਣ ਦੇ ਸਮੇਂ, transformer pipeline ਨੇ ONNX ਫਾਰਮੈਟ ਵਿੱਚ HuggingFace ਮਾਡਲਾਂ ਲਈ MLFlow ਰੈਪਰ ਜਨਰੇਸ਼ਨ ਦਾ ਸਹਿਯੋਗ ਨਹੀਂ ਦਿੱਤਾ ਸੀ, ਭਾਵੇਂ ਪ੍ਰਯੋਗਾਤਮਕ optimum Python ਪੈਕੇਜ ਦੇ ਨਾਲ ਵੀ। ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਮਾਮਲਿਆਂ ਲਈ, ਤੁਸੀਂ MLFlow ਮੋਡ ਲਈ ਆਪਣਾ ਕਸਟਮ Python ਰੈਪਰ ਬਣਾ ਸਕਦੇ ਹੋ। | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## ਪ੍ਰੋਜੈਕਟ: Transformer Pipeline

1. ਤੁਹਾਨੂੰ MLFlow ਅਤੇ HuggingFace ਤੋਂ ਸਬੰਧਤ Python ਪੈਕੇਜਾਂ ਦੀ ਲੋੜ ਹੋਵੇਗੀ:

    ``` Python
    import mlflow
    import transformers
    ```

2. ਅਗਲਾ ਕਦਮ ਹੈ transformer pipeline ਸ਼ੁਰੂ ਕਰਨਾ, ਜਿਸ ਵਿੱਚ HuggingFace ਰਜਿਸਟਰੀ ਵਿੱਚ ਟਾਰਗਟ Phi-3 ਮਾਡਲ ਨੂੰ ਦਰਸਾਇਆ ਗਿਆ ਹੈ। ਜਿਵੇਂ ਕਿ _Phi-3-mini-4k-instruct_ ਦੇ ਮਾਡਲ ਕਾਰਡ ਤੋਂ ਪਤਾ ਲੱਗਦਾ ਹੈ, ਇਸਦਾ ਟਾਸਕ "Text Generation" ਕਿਸਮ ਦਾ ਹੈ:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. ਹੁਣ ਤੁਸੀਂ ਆਪਣੇ Phi-3 ਮਾਡਲ ਦੀ transformer pipeline ਨੂੰ MLFlow ਫਾਰਮੈਟ ਵਿੱਚ ਸੇਵ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਵਾਧੂ ਜਾਣਕਾਰੀਆਂ ਜਿਵੇਂ ਟਾਰਗਟ ਆਰਟੀਫੈਕਟ ਪਾਥ, ਖਾਸ ਮਾਡਲ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈਟਿੰਗਜ਼ ਅਤੇ ਇੰਫਰੈਂਸ API ਕਿਸਮ ਦੇ ਸਕਦੇ ਹੋ:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## ਪ੍ਰੋਜੈਕਟ: Custom Python Wrapper

1. ਅਸੀਂ ਇੱਥੇ Microsoft ਦੀ [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) ਨੂੰ ONNX ਮਾਡਲ ਦੀ ਇੰਫਰੈਂਸ ਅਤੇ ਟੋਕਨ ਐਨਕੋਡਿੰਗ/ਡਿਕੋਡਿੰਗ ਲਈ ਵਰਤ ਸਕਦੇ ਹਾਂ। ਤੁਹਾਨੂੰ ਆਪਣੇ ਟਾਰਗਟ ਕੰਪਿਊਟ ਲਈ _onnxruntime_genai_ ਪੈਕੇਜ ਚੁਣਨਾ ਪਵੇਗਾ, ਹੇਠਾਂ ਦਿੱਤੇ ਉਦਾਹਰਨ ਵਿੱਚ CPU ਟਾਰਗਟ ਕੀਤਾ ਗਿਆ ਹੈ:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. ਸਾਡੀ ਕਸਟਮ ਕਲਾਸ ਦੋ ਮੈਥਡਾਂ ਨੂੰ ਲਾਗੂ ਕਰਦੀ ਹੈ: _load_context()_ ਜੋ Phi-3 Mini 4K Instruct ਦੇ **ONNX ਮਾਡਲ**, **ਜਨਰੇਟਰ ਪੈਰਾਮੀਟਰ** ਅਤੇ **ਟੋਕਨਾਈਜ਼ਰ** ਨੂੰ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ; ਅਤੇ _predict()_ ਜੋ ਦਿੱਤੇ ਗਏ ਪ੍ਰਾਂਪਟ ਲਈ ਆਉਟਪੁੱਟ ਟੋਕਨ ਬਣਾਉਂਦਾ ਹੈ:

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

1. ਹੁਣ ਤੁਸੀਂ _mlflow.pyfunc.log_model()_ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3 ਮਾਡਲ ਲਈ ਇੱਕ ਕਸਟਮ Python ਰੈਪਰ (pickle ਫਾਰਮੈਟ ਵਿੱਚ) ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ, ਜਿਸ ਵਿੱਚ ਮੂਲ ONNX ਮਾਡਲ ਅਤੇ ਲੋੜੀਂਦੇ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਸ਼ਾਮਲ ਹਨ:

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

## ਜਨਰੇਟ ਕੀਤੇ MLFlow ਮਾਡਲਾਂ ਦੇ ਸਿਗਨੇਚਰ

1. ਉਪਰ Transformer Pipeline ਪ੍ਰੋਜੈਕਟ ਦੇ ਕਦਮ 3 ਵਿੱਚ, ਅਸੀਂ MLFlow ਮਾਡਲ ਦਾ ਟਾਸਕ "_llm/v1/chat_" ਸੈੱਟ ਕੀਤਾ ਸੀ। ਇਸ ਤਰ੍ਹਾਂ ਦੀ ਹਦਾਇਤ ਮਾਡਲ ਦਾ API ਰੈਪਰ ਬਣਾਉਂਦੀ ਹੈ, ਜੋ OpenAI ਦੇ Chat API ਨਾਲ ਅਨੁਕੂਲ ਹੈ, ਜਿਵੇਂ ਹੇਠਾਂ ਦਿਖਾਇਆ ਗਿਆ ਹੈ:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. ਨਤੀਜੇ ਵਜੋਂ, ਤੁਸੀਂ ਆਪਣਾ ਪ੍ਰਾਂਪਟ ਹੇਠਾਂ ਦਿੱਤੇ ਫਾਰਮੈਟ ਵਿੱਚ ਭੇਜ ਸਕਦੇ ਹੋ:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. ਫਿਰ, OpenAI API-ਅਨੁਕੂਲ ਪੋਸਟ-ਪ੍ਰੋਸੈਸਿੰਗ ਵਰਤੋਂ, ਜਿਵੇਂ ਕਿ _response[0][‘choices’][0][‘message’][‘content’]_, ਆਪਣੇ ਆਉਟਪੁੱਟ ਨੂੰ ਸੁੰਦਰ ਬਣਾਉਣ ਲਈ:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. ਉਪਰ Custom Python Wrapper ਪ੍ਰੋਜੈਕਟ ਦੇ ਕਦਮ 3 ਵਿੱਚ, ਅਸੀਂ MLFlow ਪੈਕੇਜ ਨੂੰ ਦਿੱਤੇ ਗਏ ਇਨਪੁੱਟ ਉਦਾਹਰਨ ਤੋਂ ਮਾਡਲ ਦਾ ਸਿਗਨੇਚਰ ਜਨਰੇਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੱਤੀ ਸੀ। ਸਾਡਾ MLFlow ਰੈਪਰ ਦਾ ਸਿਗਨੇਚਰ ਇਸ ਤਰ੍ਹਾਂ ਹੋਵੇਗਾ:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. ਇਸ ਲਈ, ਸਾਡੇ ਪ੍ਰਾਂਪਟ ਵਿੱਚ "prompt" ਡਿਕਸ਼ਨਰੀ ਕੁੰਜੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ, ਇਸ ਤਰ੍ਹਾਂ:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. ਮਾਡਲ ਦਾ ਆਉਟਪੁੱਟ ਫਿਰ ਸਟਰਿੰਗ ਫਾਰਮੈਟ ਵਿੱਚ ਦਿੱਤਾ ਜਾਵੇਗਾ:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।