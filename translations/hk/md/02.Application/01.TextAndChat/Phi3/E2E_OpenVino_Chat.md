<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5621d23b682762686e0eccc7ce8bd9ec",
  "translation_date": "2025-04-04T18:04:59+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_OpenVino_Chat.md",
  "language_code": "hk"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

呢段程式碼會將模型轉換成 OpenVINO 格式，載入模型，並用嚟根據輸入嘅提示生成回應。

1. **模型匯出**：
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 呢個指令使用 `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`。

2. **導入必要嘅庫**：
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 呢幾行係從 `transformers` library and the `optimum.intel.openvino` 模組導入所需嘅類，用嚟載入同使用模型。

3. **設置模型目錄同配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` 係一個字典，配置咗 OpenVINO 模型以優先低延遲、使用一條推理流，並且唔使用緩存目錄。

4. **載入模型**：
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - 呢行會根據之前定義嘅配置設置，從指定目錄載入模型。同時，如果需要，仲可以允許遠端程式碼執行。

5. **載入分詞器**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 呢行會載入分詞器，用嚟將文字轉換成模型可以理解嘅 token。

6. **設置分詞器參數**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 呢個字典指定咗唔會喺分詞結果中加入特殊 token。

7. **定義提示**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 呢個字串設置咗一個對話提示，內容係用戶請求 AI 助手介紹自己。

8. **分詞提示**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 呢行將提示轉換成模型可以處理嘅 token，並以 PyTorch tensor 嘅形式返回結果。

9. **生成回應**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 呢行使用模型根據輸入 token 生成回應，最多可以生成 1024 個新 token。

10. **解碼回應**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 呢行將生成嘅 token 轉換成可讀嘅文字，跳過任何特殊 token，並提取第一個結果。

**免責聲明**:  
本文件已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業的人工翻譯。我們不對因使用此翻譯而產生的任何誤解或錯誤解釋承擔責任。