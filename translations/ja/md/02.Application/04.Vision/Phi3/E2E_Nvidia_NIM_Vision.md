<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "99474e9687279d0657412c806856b559",
  "translation_date": "2025-04-04T13:01:14+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_Nvidia_NIM_Vision.md",
  "language_code": "ja"
}
-->
### 例のシナリオ

画像 (`demo.png`) があり、この画像を処理して新しいバージョンとして保存する Python コードを生成したいとします (`phi-3-vision.jpg`)。

上記のコードは以下の手順でこのプロセスを自動化します：

1. 環境と必要な設定を整える。
2. モデルに必要な Python コードを生成するよう指示するプロンプトを作成する。
3. プロンプトをモデルに送信し、生成されたコードを収集する。
4. 生成されたコードを抽出して実行する。
5. 元の画像と処理後の画像を表示する。

このアプローチは、AI の力を活用して画像処理のタスクを自動化し、目標をより簡単かつ迅速に達成できるようにします。

[サンプルコードソリューション](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

コード全体が何をしているかをステップごとに分解してみましょう：

1. **必要なパッケージのインストール**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    このコマンドは `langchain_nvidia_ai_endpoints` パッケージをインストールし、最新バージョンであることを確認します。

2. **必要なモジュールのインポート**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    これらのインポートは、NVIDIA AI エンドポイントとのやり取り、パスワードを安全に扱う、オペレーティングシステムとのやり取り、そしてデータを base64 形式でエンコード/デコードするために必要なモジュールを取り込みます。

3. **APIキーの設定**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    このコードは `NVIDIA_API_KEY` 環境変数が設定されているか確認し、設定されていない場合はユーザーに安全に APIキーを入力するよう促します。

4. **モデルと画像パスの定義**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    使用するモデルを設定し、指定されたモデルで `ChatNVIDIA` のインスタンスを作成し、画像ファイルのパスを定義します。

5. **テキストプロンプトの作成**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    画像を処理する Python コードを生成するようモデルに指示するテキストプロンプトを定義します。

6. **画像を Base64 でエンコード**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    このコードは画像ファイルを読み込み、Base64 でエンコードし、エンコードされたデータを含む HTML の画像タグを作成します。

7. **テキストと画像をプロンプトに統合**:
    ```python
    prompt = f"{text} {image}"
    ```
    テキストプロンプトと HTML 画像タグを1つの文字列に統合します。

8. **ChatNVIDIA を使ってコードを生成**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    このコードはプロンプトを `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` 文字列に送信します。

9. **生成されたコンテンツから Python コードを抽出**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    生成されたコンテンツからマークダウン形式を取り除き、実際の Python コードを抽出します。

10. **生成されたコードを実行**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    抽出された Python コードをサブプロセスとして実行し、その出力をキャプチャします。

11. **画像を表示**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    これらの行は `IPython.display` モジュールを使用して画像を表示します。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性がありますのでご了承ください。元の言語で書かれた文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用によって生じる誤解や誤解釈について、当社は責任を負いません。