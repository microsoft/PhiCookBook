<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-05-09T18:38:59+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "vi"
}
-->
# MLflow

[MLflow](https://mlflow.org/) là một nền tảng mã nguồn mở được thiết kế để quản lý toàn bộ vòng đời học máy.

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.vi.png)

MLFlow được sử dụng để quản lý vòng đời ML, bao gồm thử nghiệm, tái hiện, triển khai và một kho trung tâm cho mô hình. Hiện tại MLFlow cung cấp bốn thành phần.

- **MLflow Tracking:** Ghi lại và truy vấn các thử nghiệm, mã, cấu hình dữ liệu và kết quả.
- **MLflow Projects:** Đóng gói mã khoa học dữ liệu dưới dạng có thể tái hiện trên bất kỳ nền tảng nào.
- **Mlflow Models:** Triển khai các mô hình học máy trong các môi trường phục vụ đa dạng.
- **Model Registry:** Lưu trữ, chú thích và quản lý các mô hình trong kho trung tâm.

Nó bao gồm các khả năng để theo dõi thử nghiệm, đóng gói mã thành các lần chạy có thể tái tạo, và chia sẻ cũng như triển khai mô hình. MLFlow được tích hợp trong Databricks và hỗ trợ nhiều thư viện ML khác nhau, giúp nó không phụ thuộc vào thư viện cụ thể nào. Bạn có thể sử dụng nó với bất kỳ thư viện học máy nào và trong bất kỳ ngôn ngữ lập trình nào, vì nó cung cấp API REST và CLI cho sự tiện lợi.

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.vi.png)

Các tính năng chính của MLFlow bao gồm:

- **Experiment Tracking:** Ghi lại và so sánh các tham số và kết quả.
- **Model Management:** Triển khai mô hình lên các nền tảng phục vụ và suy luận khác nhau.
- **Model Registry:** Quản lý vòng đời của các mô hình MLflow một cách hợp tác, bao gồm phiên bản và chú thích.
- **Projects:** Đóng gói mã ML để chia sẻ hoặc sử dụng trong sản xuất.
MLFlow cũng hỗ trợ vòng lặp MLOps, bao gồm chuẩn bị dữ liệu, đăng ký và quản lý mô hình, đóng gói mô hình để thực thi, triển khai dịch vụ và giám sát mô hình. Nó nhằm đơn giản hóa quá trình chuyển từ nguyên mẫu sang quy trình sản xuất, đặc biệt trong môi trường đám mây và edge.

## Kịch bản E2E - Xây dựng wrapper và sử dụng Phi-3 như một mô hình MLFlow

Trong ví dụ E2E này, chúng ta sẽ trình bày hai cách tiếp cận khác nhau để xây dựng một wrapper cho mô hình ngôn ngữ nhỏ Phi-3 (SLM) và sau đó chạy nó như một mô hình MLFlow, có thể là chạy cục bộ hoặc trên đám mây, ví dụ như trong workspace Azure Machine Learning.

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.vi.png)

| Dự án | Mô tả | Vị trí |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline là lựa chọn đơn giản nhất để xây dựng wrapper nếu bạn muốn sử dụng mô hình HuggingFace với flavor thử nghiệm transformers của MLFlow. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | Tại thời điểm viết, transformer pipeline chưa hỗ trợ tạo wrapper MLFlow cho các mô hình HuggingFace ở định dạng ONNX, ngay cả với gói Python experimental optimum. Trong những trường hợp như vậy, bạn có thể tự xây dựng wrapper Python tùy chỉnh cho MLFlow mode | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Dự án: Transformer Pipeline

1. Bạn sẽ cần các gói Python liên quan từ MLFlow và HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Tiếp theo, bạn nên khởi tạo một transformer pipeline bằng cách tham chiếu đến mô hình Phi-3 mục tiêu trong registry HuggingFace. Như có thể thấy trong thẻ mô hình của _Phi-3-mini-4k-instruct_, nhiệm vụ của nó là loại “Text Generation”:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Bây giờ bạn có thể lưu pipeline transformer của mô hình Phi-3 vào định dạng MLFlow và cung cấp các thông tin bổ sung như đường dẫn lưu artifacts, cấu hình mô hình cụ thể và loại API suy luận:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Dự án: Custom Python Wrapper

1. Ở đây chúng ta có thể sử dụng API generate() của [ONNX Runtime của Microsoft](https://github.com/microsoft/onnxruntime-genai) cho việc suy luận mô hình ONNX và mã hóa / giải mã token. Bạn cần chọn gói _onnxruntime_genai_ phù hợp với máy tính mục tiêu, ví dụ dưới đây hướng tới CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Lớp tùy chỉnh của chúng ta triển khai hai phương thức: _load_context()_ để khởi tạo **mô hình ONNX** của Phi-3 Mini 4K Instruct, **tham số generator** và **tokenizer**; và _predict()_ để tạo token đầu ra cho prompt được cung cấp:

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

1. Bây giờ bạn có thể sử dụng hàm _mlflow.pyfunc.log_model()_ để tạo wrapper Python tùy chỉnh (dưới dạng pickle) cho mô hình Phi-3, cùng với mô hình ONNX gốc và các phụ thuộc cần thiết:

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

## Chữ ký của các mô hình MLFlow được tạo

1. Ở bước 3 của dự án Transformer Pipeline phía trên, chúng ta đặt nhiệm vụ của mô hình MLFlow là “_llm/v1/chat_”. Hướng dẫn này tạo ra wrapper API cho mô hình, tương thích với OpenAI’s Chat API như dưới đây:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Kết quả là, bạn có thể gửi prompt theo định dạng sau:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Sau đó, sử dụng xử lý hậu kỳ tương thích OpenAI API, ví dụ _response[0][‘choices’][0][‘message’][‘content’]_, để làm đẹp đầu ra thành dạng như sau:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. Ở bước 3 của dự án Custom Python Wrapper phía trên, ta cho phép gói MLFlow tạo chữ ký mô hình từ ví dụ đầu vào đã cho. Chữ ký wrapper MLFlow của ta sẽ trông như sau:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Do đó, prompt của ta cần chứa khóa dictionary "prompt", tương tự như sau:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Đầu ra của mô hình sẽ được cung cấp dưới dạng chuỗi:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được xem là nguồn thông tin chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.