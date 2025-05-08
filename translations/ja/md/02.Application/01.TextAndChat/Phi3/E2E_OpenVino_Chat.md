<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-08T05:42:34+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "ja"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

このコードはモデルをOpenVINO形式にエクスポートし、それを読み込んで与えられたプロンプトに対する応答を生成します。

1. **モデルのエクスポート**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - このコマンドは `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` を使用しています。

2. **必要なライブラリのインポート**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - これらの行は、モデルの読み込みと使用に必要な `transformers` library and the `optimum.intel.openvino` モジュールからクラスをインポートしています。

3. **モデルディレクトリと設定の準備**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifies where the model files are stored.
   - `ov_config` は、OpenVINOモデルの設定で、低レイテンシを優先し、推論ストリームを1つに設定し、キャッシュディレクトリを使用しないようにしています。

4. **モデルの読み込み**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - この行は指定したディレクトリからモデルを読み込み、先に定義した設定を適用します。必要に応じてリモートコード実行も許可します。

5. **トークナイザーの読み込み**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - この行はテキストをモデルが理解できるトークンに変換するトークナイザーを読み込みます。

6. **トークナイザーの引数設定**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - この辞書は、トークン化された出力に特殊トークンを追加しないよう指定しています。

7. **プロンプトの定義**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - この文字列は、ユーザーがAIアシスタントに自己紹介を求める会話のプロンプトを設定しています。

8. **プロンプトのトークン化**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - この行はプロンプトをモデルが処理できるトークンに変換し、PyTorchのテンソルとして返します。

9. **応答の生成**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - この行は入力トークンを基にモデルで応答を生成し、最大1024トークンまで生成します。

10. **応答のデコード**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - この行は生成されたトークンを人間が読める文字列に戻し、特殊トークンをスキップして最初の結果を取得します。

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご了承ください。原文の言語で記載された文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、一切の責任を負いかねます。