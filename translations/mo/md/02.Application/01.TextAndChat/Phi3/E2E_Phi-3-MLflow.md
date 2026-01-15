<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:27:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "mo"
}
-->
# MLflow

[MLflow](https://mlflow.org/) 是一個開源平台，旨在管理機器學習的端到端生命週期。

![MLFlow](../../../../../../translated_images/mo/MlFlowmlops.ed16f47809d74d9a.webp)

MLFlow 用於管理機器學習生命週期，包括實驗、可重現性、部署以及中央模型註冊庫。MLflow 目前提供四個組件。

- **MLflow Tracking：** 記錄和查詢實驗、程式碼、資料配置和結果。
- **MLflow Projects：** 以可重現的格式封裝資料科學程式碼，能在任何平台上執行。
- **Mlflow Models：** 在多種服務環境中部署機器學習模型。
- **Model Registry：** 在中央儲存庫中存放、註解和管理模型。

它具備追蹤實驗、將程式碼封裝成可重現執行、分享及部署模型的功能。MLFlow 已整合至 Databricks，並支援多種機器學習函式庫，具備函式庫無關性。它可與任何機器學習函式庫及任何程式語言搭配使用，並提供 REST API 和 CLI 以方便操作。

![MLFlow](../../../../../../translated_images/mo/MLflow2.5a22eb718f6311d1.webp)

MLFlow 的主要功能包括：

- **實驗追蹤：** 記錄並比較參數與結果。
- **模型管理：** 將模型部署至各種服務與推論平台。
- **模型註冊庫：** 協作管理 MLflow 模型的生命週期，包括版本控制與註解。
- **Projects：** 封裝機器學習程式碼以便分享或生產使用。

MLFlow 也支援 MLOps 循環，包括資料準備、模型註冊與管理、模型封裝執行、服務部署及模型監控。它旨在簡化從原型到生產工作流程的過程，特別是在雲端與邊緣環境中。

## 端到端範例 - 建立包裝器並將 Phi-3 作為 MLFlow 模型使用

在此端到端範例中，我們將展示兩種不同方法，來建立 Phi-3 小型語言模型（SLM）的包裝器，並將其作為 MLFlow 模型在本地或雲端（例如 Azure Machine Learning 工作區）執行。

![MLFlow](../../../../../../translated_images/mo/MlFlow1.fd745e47dbd3fecf.webp)

| 專案 | 說明 | 位置 |
| ------------ | ----------- | -------- |
| Transformer Pipeline | 如果想使用 HuggingFace 模型搭配 MLFlow 的實驗性 transformers 風格，Transformer Pipeline 是建立包裝器最簡單的選擇。 | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | 撰寫本文時，transformer pipeline 尚不支援為 ONNX 格式的 HuggingFace 模型產生 MLFlow 包裝器，即使使用實驗性 optimum Python 套件。針對此類情況，可自行建立自訂 Python 包裝器以用於 MLFlow 模式。 | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## 專案：Transformer Pipeline

1. 你需要安裝 MLFlow 和 HuggingFace 相關的 Python 套件：

    ``` Python
    import mlflow
    import transformers
    ```

2. 接著，應透過 HuggingFace 註冊庫中目標 Phi-3 模型，初始化 transformer pipeline。從 _Phi-3-mini-4k-instruct_ 的模型卡可見，其任務類型為「文字生成」：

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. 現在你可以將 Phi-3 模型的 transformer pipeline 儲存為 MLFlow 格式，並提供額外資訊，如目標 artifact 路徑、特定模型配置設定及推論 API 類型：

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## 專案：Custom Python Wrapper

1. 這裡我們可以使用 Microsoft 的 [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) 來進行 ONNX 模型的推論及 token 編碼/解碼。你必須選擇適合目標運算環境的 _onnxruntime_genai_ 套件，以下範例以 CPU 為目標：

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. 我們的自訂類別實作了兩個方法：_load_context()_ 用於初始化 Phi-3 Mini 4K Instruct 的 **ONNX 模型**、**生成器參數**及**分詞器**；_predict()_ 用於根據輸入提示產生輸出 token：

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

1. 現在你可以使用 _mlflow.pyfunc.log_model()_ 函式，為 Phi-3 模型產生自訂 Python 包裝器（pickle 格式），並包含原始 ONNX 模型及所需依賴：

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

## 產生的 MLFlow 模型簽名

1. 在上述 Transformer Pipeline 專案的第 3 步中，我們將 MLFlow 模型的任務設定為「_llm/v1/chat_」。此設定會產生一個與 OpenAI Chat API 相容的模型 API 包裝器，如下所示：

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. 因此，你可以用以下格式提交提示：

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. 接著，使用與 OpenAI API 相容的後處理，例如 _response[0][‘choices’][0][‘message’][‘content’]_，將輸出美化成如下形式：

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. 在上述 Custom Python Wrapper 專案的第 3 步中，我們讓 MLFlow 套件根據給定的輸入範例自動產生模型簽名。我們的 MLFlow 包裝器簽名將如下：

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. 因此，我們的提示需包含名為 "prompt" 的字典鍵，類似如下：

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. 模型輸出將以字串格式提供：

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。