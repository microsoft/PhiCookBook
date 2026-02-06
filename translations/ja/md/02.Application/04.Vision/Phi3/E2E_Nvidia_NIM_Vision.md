### 例のシナリオ

画像（`demo.png`）があり、この画像を処理して新しいバージョン（`phi-3-vision.jpg`）を保存するPythonコードを生成したいとします。

上記のコードは以下の手順でこのプロセスを自動化しています：

1. 環境と必要な設定を整える。
2. モデルに必要なPythonコードを生成するよう指示するプロンプトを作成する。
3. プロンプトをモデルに送信し、生成されたコードを受け取る。
4. 生成されたコードを抽出して実行する。
5. 元の画像と処理後の画像を表示する。

この方法はAIの力を活用して画像処理タスクを自動化し、目標達成をより簡単かつ迅速にします。

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

コード全体が何をしているのか、ステップごとに見ていきましょう：

1. **必要なパッケージをインストール**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    このコマンドは`langchain_nvidia_ai_endpoints`パッケージをインストールし、最新バージョンであることを保証します。

2. **必要なモジュールをインポート**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    これらのインポートは、NVIDIA AIエンドポイントとのやり取り、パスワードの安全な取り扱い、OS操作、base64形式でのデータのエンコード/デコードに必要なモジュールを読み込みます。

3. **APIキーの設定**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    このコードは`NVIDIA_API_KEY`環境変数が設定されているか確認し、設定されていなければユーザーに安全にAPIキーの入力を促します。

4. **モデルと画像パスの定義**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    使用するモデルを設定し、指定したモデルで`ChatNVIDIA`のインスタンスを作成し、画像ファイルのパスを定義します。

5. **テキストプロンプトの作成**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    画像を処理するPythonコードを生成するようモデルに指示するテキストプロンプトを定義します。

6. **画像をBase64でエンコード**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    画像ファイルを読み込み、base64でエンコードし、エンコードされたデータを含むHTMLの画像タグを作成します。

7. **テキストと画像をプロンプトに結合**:
    ```python
    prompt = f"{text} {image}"
    ```
    テキストプロンプトとHTML画像タグを一つの文字列にまとめます。

8. **ChatNVIDIAを使ってコードを生成**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    このコードはプロンプトを`ChatNVIDIA`モデルに送り、生成されたコードをチャンクごとに受け取り、表示しながら`code`文字列に追加します。

9. **生成された内容からPythonコードを抽出**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    生成された内容からマークダウンのフォーマットを取り除き、実際のPythonコードを抽出します。

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
    これらの行は`IPython.display`モジュールを使って画像を表示します。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。