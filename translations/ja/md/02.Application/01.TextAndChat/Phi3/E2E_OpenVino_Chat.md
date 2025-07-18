<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:02:34+00:00",
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
   - このコマンドは`optimum-cli`ツールを使って、効率的な推論に最適化されたOpenVINO形式でモデルをエクスポートします。  
   - エクスポートされるモデルは`"microsoft/Phi-3-mini-4k-instruct"`で、過去の文脈に基づいてテキストを生成するタスク用に設定されています。  
   - モデルの重みは4ビット整数（`int4`）に量子化されており、モデルサイズの削減と処理速度の向上に寄与します。  
   - `group-size`、`ratio`、`sym`などのパラメータは量子化プロセスの微調整に使われます。  
   - エクスポートされたモデルは`./model/phi3-instruct/int4`ディレクトリに保存されます。

2. **必要なライブラリのインポート**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - これらの行では、モデルの読み込みと使用に必要な`transformers`ライブラリと`optimum.intel.openvino`モジュールからクラスをインポートしています。

3. **モデルディレクトリと設定の準備**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir`はモデルファイルの保存場所を指定します。  
   - `ov_config`はOpenVINOモデルの設定で、低レイテンシを優先し、推論ストリームを1つに設定し、キャッシュディレクトリを使用しないようにしています。

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
   - この辞書はトークナイズされた出力に特殊トークンを追加しないよう指定しています。

7. **プロンプトの定義**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - この文字列はユーザーがAIアシスタントに自己紹介を依頼する会話のプロンプトを設定しています。

8. **プロンプトのトークナイズ**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - この行はプロンプトをモデルが処理できるトークンに変換し、PyTorchのテンソルとして結果を返します。

9. **応答の生成**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - この行は入力トークンに基づいてモデルが応答を生成し、最大1024トークンまで生成します。

10. **応答のデコード**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - この行は生成されたトークンを人間が読める文字列に変換し、特殊トークンをスキップして最初の結果を取得します。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。