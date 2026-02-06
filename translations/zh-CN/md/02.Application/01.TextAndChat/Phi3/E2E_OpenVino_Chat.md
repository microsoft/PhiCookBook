[OpenVino Chat 示例](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

这段代码将模型导出为 OpenVINO 格式，加载该模型，并用它生成对给定提示的回复。

1. **导出模型**：
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 该命令使用 `optimum-cli` 工具将模型导出为 OpenVINO 格式，该格式针对高效推理进行了优化。
   - 导出的模型是 `"microsoft/Phi-3-mini-4k-instruct"`，用于基于上下文生成文本的任务。
   - 模型权重被量化为 4 位整数（`int4`），这有助于减小模型大小并加快处理速度。
   - 其他参数如 `group-size`、`ratio` 和 `sym` 用于微调量化过程。
   - 导出的模型保存在目录 `./model/phi3-instruct/int4` 中。

2. **导入必要的库**：
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 这些代码行从 `transformers` 库和 `optimum.intel.openvino` 模块导入了加载和使用模型所需的类。

3. **设置模型目录和配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` 指定了模型文件所在的位置。
   - `ov_config` 是一个字典，用于配置 OpenVINO 模型，优先考虑低延迟，使用单个推理流，并且不使用缓存目录。

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
   - 这行代码根据之前定义的配置设置，从指定目录加载模型，并允许远程代码执行（如果需要）。

5. **加载分词器**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 这行代码加载分词器，负责将文本转换为模型可理解的标记。

6. **设置分词器参数**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 该字典指定不在分词结果中添加特殊标记。

7. **定义提示语**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 该字符串设置了一个对话提示，用户请求 AI 助手进行自我介绍。

8. **对提示语进行分词**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 这行代码将提示语转换为模型可处理的标记，并以 PyTorch 张量形式返回结果。

9. **生成回复**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 这行代码使用模型基于输入标记生成回复，最多生成 1024 个新标记。

10. **解码回复**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 这行代码将生成的标记转换回可读字符串，跳过任何特殊标记，并获取第一个结果。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的原文应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。