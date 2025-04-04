<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5621d23b682762686e0eccc7ce8bd9ec",
  "translation_date": "2025-04-04T06:14:22+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_OpenVino_Chat.md",
  "language_code": "tw"
}
-->
[OpenVino Chat 範例](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

此程式碼將模型匯出為 OpenVINO 格式，載入模型，並使用模型生成對給定提示的回應。

1. **匯出模型**：
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 此指令使用 `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`。

2. **匯入必要的函式庫**：
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 這些程式碼行匯入 `transformers` library and the `optimum.intel.openvino` 模組中的類別，這些類別用於載入及使用模型。

3. **設定模型目錄與配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` 是一個字典，用於配置 OpenVINO 模型，優先低延遲，使用一條推理流，且不使用快取目錄。

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
   - 此程式碼行從指定目錄載入模型，並使用先前定義的配置設定。此外，若有需要，還允許遠端程式碼執行。

5. **載入分詞器**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 此程式碼行載入分詞器，用於將文字轉換為模型能理解的 tokens。

6. **設定分詞器參數**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 此字典指定在分詞輸出中不應加入特殊 tokens。

7. **定義提示**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 此字串設置了一個對話提示，讓使用者要求 AI 助手自我介紹。

8. **分詞提示**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 此程式碼行將提示轉換為模型能處理的 tokens，並以 PyTorch tensors 的形式返回結果。

9. **生成回應**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 此程式碼行使用模型根據輸入 tokens 生成回應，最多生成 1024 個新的 tokens。

10. **解碼回應**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 此程式碼行將生成的 tokens 轉換回可讀的字串，跳過任何特殊 tokens，並取回第一個結果。

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保翻譯的準確性，但請注意，機器翻譯可能會包含錯誤或不精確之處。原始語言的文檔應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。