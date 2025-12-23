<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-12-21T20:54:11+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "pcm"
}
-->
# MLflow

[MLflow](https://mlflow.org/) na open-source platform wey dem design to manage the end-to-end machine learning lifecycle.

![MLFlow](../../../../../../translated_images/MlFlowmlops.ed16f47809d74d9ac0407bf43985ec022ad01f3d970083e465326951e43b2e01.pcm.png)

MLFlow dey used to manage di ML lifecycle, including experimentation, reproducibility, deployment and central model registry. MLflow now get four components.

- **MLflow Tracking:** Record and query experiments, code, data config and results.
- **MLflow Projects:** Package data science code inside format wey fit reproduce runs for any platform.
- **Mlflow Models:** Deploy machine learning models for different serving environments.
- **Model Registry:** Store, annotate and manage models for central repository.

E get capabilities for tracking experiments, packaging code into reproducible runs, and sharing and deploying models. MLFlow dey integrated into Databricks and e support plenty ML libraries, so e no dey tied to one library. You fit use am with any machine learning library and for any programming language, becos e get REST API and CLI for convenience.

![MLFlow](../../../../../../translated_images/MLflow2.5a22eb718f6311d16f1a1952a047dc6b9e392649f1e0fc7bc3c3dcd65e3af07c.pcm.png)

Key features of MLFlow include:

- **Experiment Tracking:** Record and compare parameters and results.
- **Model Management:** Deploy models to different serving and inference platforms.
- **Model Registry:** Collaboratively manage the lifecycle of MLflow Models, including versioning and annotations.
- **Projects:** Package ML code for sharing or production use.
MLFlow still support di MLOps loop, wey include preparing data, registering and managing models, packaging models for execution, deploying services, and monitoring models. Di aim na to simplify di process to move from prototype go production workflow, specially for cloud and edge environments.

## E2E Scenario - Building a wrapper and using Phi-3 as an MLFlow model

For dis E2E sample we go show two different ways to build wrapper around Phi-3 small language model (SLM) and then run am as MLFlow model either locally or for cloud, for example for Azure Machine Learning workspace.

![MLFlow](../../../../../../translated_images/MlFlow1.fd745e47dbd3fecfee254096d496cdf1cb3e1789184f9efcead9c2a96e5a979b.pcm.png)

| Project | Description | Location |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer PIpeline na di easiest option to build wrapper if you wan use HuggingFace model with MLFlow’s experimental transformers flavour. | [**TransformerPipeline.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | As of time wey dem write dis, transformer pipeline no support MLFlow wrapper generation for HuggingFace models wey dey ONNX format, even with di experimental optimum Python package. For cases like dis, you fit build your custom Python wrapper for MLFlow model | [**CustomPythonWrapper.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Project: Transformer Pipeline

1. You go need relevant Python packages from MLFlow and HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Next, you suppose initiate a transformer pipeline by referring to di target Phi-3 model for di HuggingFace registry. As you fit see from di _Phi-3-mini-4k-instruct_’s model card, di task na “Text Generation” type:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. You fit now save your Phi-3 model’s transformer pipeline into MLFlow format and give additional details like di target artifacts path, specific model configuration settings and inference API type:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Project: Custom Python Wrapper

1. For here we fit use Microsoft’s [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) for ONNX model inference and tokens encoding / decoding. You go choose _onnxruntime_genai_ package for your target compute, for di example below we target CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Our custom class dey implement two methods: _load_context()_ to initialise di **ONNX model** of Phi-3 Mini 4K Instruct, **generator parameters** and **tokenizer**; and _predict()_ to generate output tokens for di prompt wey dem give:

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # Dey fetch di model from di artifacts
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # Dey define di model
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # Dey define di tokenizer
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # Dey fetch di prompt from di input
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # Dey generate di model response
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

1. You fit use _mlflow.pyfunc.log_model()_ function now to generate custom Python wrapper (for pickle format) for di Phi-3 model, together with di original ONNX model and required dependencies:

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

## Signatures of generated MLFlow models

1. For step 3 of Transformer Pipeline project wey dey above, we set MLFlow model’s task to “_llm/v1/chat_”. Dis instruction go generate model’s API wrapper wey compatible with OpenAI’s Chat API as e show below:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. As result, you fit submit your prompt for di following format:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Then, use OpenAI API-compatible post-processing, for example _response[0][‘choices’][0][‘message’][‘content’]_, to make your output fine like dis:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. For step 3 of Custom Python Wrapper project wey dey above, we make MLFlow package generate di model’s signature from one input example. Our MLFlow wrapper signature go look like dis:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. So, our prompt suppose get "prompt" dictionary key, something like this:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Di model's output go dey provided as string format:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate by AI translation service Co‑op Translator (https://github.com/Azure/co-op-translator). We try make am correct, but abeg note say machine/automatic translation fit get mistakes or wrong parts. Di original document for im own language na di main/authoritative source. If na important matter, e better make person wey sabi do professional human translation check am. We no dey responsible for any misunderstanding or wrong interpretation wey fit show because of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->