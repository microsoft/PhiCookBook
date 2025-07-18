<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:02:05+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "mo"
}
-->
[OpenVino Chat 範例](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

這段程式碼將模型匯出為 OpenVINO 格式，載入後用來根據給定的提示產生回應。

1. **匯出模型**：
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 此指令使用 `optimum-cli` 工具將模型匯出為 OpenVINO 格式，該格式針對高效推論進行優化。
   - 匯出的模型是 `"microsoft/Phi-3-mini-4k-instruct"`，用於根據過去上下文生成文字的任務。
   - 模型權重被量化為 4 位元整數（`int4`），有助於減少模型大小並加快處理速度。
   - 其他參數如 `group-size`、`ratio` 和 `sym` 用來微調量化過程。
   - 匯出的模型會儲存在目錄 `./model/phi3-instruct/int4`。

2. **匯入必要的函式庫**：
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 這些程式碼行從 `transformers` 函式庫和 `optimum.intel.openvino` 模組匯入類別，這些是載入和使用模型所需的。

3. **設定模型目錄與配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` 指定模型檔案所在的位置。
   - `ov_config` 是一個字典，用來設定 OpenVINO 模型優先低延遲、使用單一推論串流，且不使用快取目錄。

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
   - 這行程式碼從指定目錄載入模型，並使用先前定義的配置設定。若有需要，也允許遠端程式碼執行。

5. **載入分詞器**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 這行程式碼載入分詞器，負責將文字轉換成模型能理解的標記。

6. **設定分詞器參數**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 這個字典指定不在分詞結果中加入特殊標記。

7. **定義提示語句**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 這段字串設定一個對話提示，使用者請 AI 助手自我介紹。

8. **對提示進行分詞**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 這行程式碼將提示轉換成模型可處理的標記，並以 PyTorch 張量形式回傳。

9. **產生回應**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 這行程式碼使用模型根據輸入標記生成回應，最多產生 1024 個新標記。

10. **解碼回應**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 這行程式碼將生成的標記轉回可讀文字，跳過任何特殊標記，並取得第一個結果。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。