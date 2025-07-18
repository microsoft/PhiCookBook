<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:34:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "tl"
}
-->
# MLflow

[MLflow](https://mlflow.org/) ay isang open-source na platform na idinisenyo upang pamahalaan ang buong lifecycle ng machine learning.

![MLFlow](../../../../../../translated_images/MlFlowmlops.ed16f47809d74d9ac0407bf43985ec022ad01f3d970083e465326951e43b2e01.tl.png)

Ginagamit ang MLFlow para pamahalaan ang ML lifecycle, kabilang ang eksperimento, reproducibility, deployment, at isang sentral na model registry. Sa kasalukuyan, nag-aalok ang ML flow ng apat na bahagi.

- **MLflow Tracking:** Itala at i-query ang mga eksperimento, code, data config, at resulta.
- **MLflow Projects:** I-package ang data science code sa isang format para maulit ang mga run sa anumang platform.
- **Mlflow Models:** I-deploy ang mga machine learning model sa iba't ibang serving environment.
- **Model Registry:** Itago, lagyan ng anotasyon, at pamahalaan ang mga modelo sa isang sentral na repositoryo.

Kasama dito ang mga kakayahan para sa pagsubaybay ng mga eksperimento, pag-package ng code para sa reproducible na mga run, at pagbabahagi at pag-deploy ng mga modelo. Ang MLFlow ay naka-integrate sa Databricks at sumusuporta sa iba't ibang ML libraries, kaya ito ay library-agnostic. Maaari itong gamitin sa anumang machine learning library at sa anumang programming language, dahil nagbibigay ito ng REST API at CLI para sa kaginhawaan.

![MLFlow](../../../../../../translated_images/MLflow2.5a22eb718f6311d16f1a1952a047dc6b9e392649f1e0fc7bc3c3dcd65e3af07c.tl.png)

Mga pangunahing tampok ng MLFlow ay kinabibilangan ng:

- **Experiment Tracking:** Itala at ihambing ang mga parameter at resulta.
- **Model Management:** I-deploy ang mga modelo sa iba't ibang serving at inference platform.
- **Model Registry:** Sama-samang pamahalaan ang lifecycle ng MLflow Models, kabilang ang versioning at anotasyon.
- **Projects:** I-package ang ML code para sa pagbabahagi o paggamit sa produksyon.

Sinusuportahan din ng MLFlow ang MLOps loop, na kinabibilangan ng paghahanda ng data, pagrerehistro at pamamahala ng mga modelo, pag-package ng mga modelo para sa pagpapatupad, pag-deploy ng mga serbisyo, at pagmamanman ng mga modelo. Layunin nitong gawing mas madali ang proseso mula prototype hanggang production workflow, lalo na sa cloud at edge na mga kapaligiran.

## E2E Scenario - Paggawa ng wrapper at paggamit ng Phi-3 bilang MLFlow model

Sa E2E na halimbawa na ito, ipapakita namin ang dalawang magkaibang paraan sa paggawa ng wrapper sa paligid ng Phi-3 small language model (SLM) at pagkatapos ay patakbuhin ito bilang MLFlow model, alinman lokal o sa cloud, halimbawa sa Azure Machine Learning workspace.

![MLFlow](../../../../../../translated_images/MlFlow1.fd745e47dbd3fecfee254096d496cdf1cb3e1789184f9efcead9c2a96e5a979b.tl.png)

| Project | Paglalarawan | Lokasyon |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Ang Transformer Pipeline ang pinakamadaling opsyon para gumawa ng wrapper kung nais mong gamitin ang HuggingFace model gamit ang experimental transformers flavour ng MLFlow. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | Sa oras ng pagsulat, hindi pa sinusuportahan ng transformer pipeline ang MLFlow wrapper generation para sa HuggingFace models sa ONNX format, kahit gamit ang experimental optimum Python package. Para sa mga ganitong kaso, maaari kang gumawa ng sarili mong custom Python wrapper para sa MLFlow mode | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Project: Transformer Pipeline

1. Kakailanganin mo ang mga kaugnay na Python packages mula sa MLFlow at HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Susunod, dapat kang mag-umpisa ng transformer pipeline sa pamamagitan ng pagtukoy sa target na Phi-3 model sa HuggingFace registry. Makikita sa model card ng _Phi-3-mini-4k-instruct_ na ang gawain nito ay uri ng “Text Generation”:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Maaari mo nang i-save ang transformer pipeline ng Phi-3 model mo sa MLFlow format at magbigay ng karagdagang detalye tulad ng target artifacts path, partikular na mga setting ng model configuration, at uri ng inference API:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Project: Custom Python Wrapper

1. Maaari nating gamitin dito ang Microsoft's [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) para sa inference ng ONNX model at encoding/decoding ng mga token. Piliin mo ang _onnxruntime_genai_ package para sa target compute mo, sa halimbawa sa ibaba ay naka-target sa CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Ang custom class namin ay nagpapatupad ng dalawang method: _load_context()_ para i-initialize ang **ONNX model** ng Phi-3 Mini 4K Instruct, **generator parameters**, at **tokenizer**; at _predict()_ para gumawa ng output tokens base sa ibinigay na prompt:

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

1. Maaari mo nang gamitin ang _mlflow.pyfunc.log_model()_ function para gumawa ng custom Python wrapper (sa pickle format) para sa Phi-3 model, kasama ang orihinal na ONNX model at mga kinakailangang dependencies:

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

## Mga Signature ng mga generated na MLFlow models

1. Sa hakbang 3 ng Transformer Pipeline project sa itaas, itinakda namin ang task ng MLFlow model sa “_llm/v1/chat_”. Ang ganitong instruction ay gumagawa ng API wrapper ng model, na compatible sa OpenAI’s Chat API tulad ng ipinapakita sa ibaba:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Bilang resulta, maaari mong isumite ang iyong prompt sa sumusunod na format:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Pagkatapos, gamitin ang OpenAI API-compatible post-processing, halimbawa _response[0][‘choices’][0][‘message’][‘content’]_, para pagandahin ang output mo na maging ganito:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. Sa hakbang 3 ng Custom Python Wrapper project sa itaas, pinapayagan namin ang MLFlow package na gumawa ng signature ng model mula sa isang ibinigay na input example. Ang signature ng MLFlow wrapper namin ay magiging ganito:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Kaya, ang prompt natin ay kailangang maglaman ng "prompt" na dictionary key, katulad nito:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Ang output ng model ay ibibigay naman sa string format:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.