<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5621d23b682762686e0eccc7ce8bd9ec",
  "translation_date": "2025-04-03T07:11:05+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_OpenVino_Chat.md",
  "language_code": "zh"
}
-->
[OpenVino Chat 示例](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

该代码将模型导出为 OpenVINO 格式，加载模型，并根据给定的提示生成回复。

1. **导出模型**：
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 此命令使用 `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`。

2. **导入必要的库**：
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 这些代码行从 `transformers` library and the `optimum.intel.openvino` 模块中导入所需的类，用于加载和使用模型。

3. **设置模型目录和配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` 是一个字典，用于配置 OpenVINO 模型以优先考虑低延迟，使用一个推理流，并且不使用缓存目录。

4. **加载模型**：
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - 此代码行从指定的目录加载模型，并使用之前定义的配置设置。如果需要，还可以允许远程代码执行。

5. **加载分词器**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 此代码行加载分词器，用于将文本转换为模型可以理解的标记。

6. **设置分词器参数**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 此字典指定在标记化输出中不添加特殊标记。

7. **定义提示**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 此字符串设置了一个对话提示，用户要求 AI 助手进行自我介绍。

8. **对提示进行标记化**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 此代码行将提示转换为模型可以处理的标记，并以 PyTorch 张量的形式返回结果。

9. **生成回复**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 此代码行使用模型根据输入标记生成回复，最多生成 1024 个新标记。

10. **解码回复**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 此代码行将生成的标记转换回人类可读的字符串，跳过任何特殊标记，并获取第一个结果。

**免责声明**:  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文档的母语版本应被视为权威来源。对于关键信息，建议使用专业的人工翻译。对于因使用此翻译而产生的任何误解或误读，我们不承担任何责任。