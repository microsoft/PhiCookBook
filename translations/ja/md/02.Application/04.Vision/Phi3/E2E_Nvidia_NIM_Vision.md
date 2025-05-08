<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-08T05:26:10+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "ja"
}
-->
### 例のシナリオ

画像 (`demo.png`) があり、この画像を処理して新しいバージョン (`phi-3-vision.jpg`) を保存するPythonコードを生成したいと想像してください。

上記のコードは以下の手順を自動化しています：

1. 環境と必要な設定を整える。
2. モデルに必要なPythonコードを生成するよう指示するプロンプトを作成する。
3. プロンプトをモデルに送信し、生成されたコードを受け取る。
4. 生成されたコードを抽出して実行する。
5. 元の画像と処理後の画像を表示する。

この方法はAIの力を活用して画像処理の作業を自動化し、目標達成をより簡単かつ迅速にします。

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

コード全体が何をしているか、ステップごとに見ていきましょう：

1. **必要なパッケージをインストール**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    このコマンドは `langchain_nvidia_ai_endpoints` パッケージを最新バージョンでインストールします。

2. **必要なモジュールをインポート**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    これらのインポートは、NVIDIA AIエンドポイントとのやり取り、パスワードの安全な取り扱い、OS操作、base64のエンコード/デコードに必要なモジュールを読み込みます。

3. **APIキーの設定**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    ここでは `NVIDIA_API_KEY` 環境変数が設定されているか確認し、なければユーザーに安全にAPIキーの入力を促します。

4. **モデルと画像パスの定義**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    使用するモデルを設定し、指定したモデルで `ChatNVIDIA` のインスタンスを作成し、画像ファイルのパスを定義します。

5. **テキストプロンプトの作成**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    モデルに画像処理用のPythonコードを生成するよう指示するテキストプロンプトを定義します。

6. **画像をBase64でエンコード**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    画像ファイルを読み込み、base64でエンコードし、そのデータを埋め込んだHTMLのimgタグを作成します。

7. **テキストと画像をプロンプトに結合**:
    ```python
    prompt = f"{text} {image}"
    ```
    テキストプロンプトとHTMLの画像タグを一つの文字列にまとめます。

8. **ChatNVIDIAでコードを生成**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    このコードはプロンプトを `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` 文字列に送信します。

9. **生成された内容からPythonコードを抽出**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    これはマークダウンの書式を取り除き、実際のPythonコードだけを抽出します。

10. **生成されたコードを実行**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    抽出したPythonコードをサブプロセスとして実行し、その出力を取得します。

11. **画像を表示**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    これらの行は `IPython.display` モジュールを使って画像を表示します。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。