<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "99474e9687279d0657412c806856b559",
  "translation_date": "2025-04-04T06:48:40+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_Nvidia_NIM_Vision.md",
  "language_code": "tw"
}
-->
### 範例情境

假設你有一張圖片 (`demo.png`)，並希望生成處理這張圖片並保存其新版本的 Python 程式碼 (`phi-3-vision.jpg`)。

上述程式碼會自動化這個過程，具體步驟如下：

1. 設置環境和必要的配置。
2. 建立一個提示，指導模型生成所需的 Python 程式碼。
3. 將提示發送給模型並收集生成的程式碼。
4. 提取並執行生成的程式碼。
5. 顯示原始圖片和處理後的圖片。

這種方法利用 AI 的力量自動化影像處理任務，使得目標達成更加簡單和快捷。

[範例程式碼解決方案](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

接下來逐步解析整段程式碼的功能：

1. **安裝必要的套件**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    這個指令安裝 `langchain_nvidia_ai_endpoints` 套件，並確保是最新版本。

2. **導入必要模組**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    這些導入包含與 NVIDIA AI 端點互動、安全處理密碼、與操作系統交互以及進行 Base64 編碼/解碼的必要模組。

3. **設置 API 金鑰**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    此程式碼檢查環境變數 `NVIDIA_API_KEY` 是否已設置。如果未設置，則提示使用者安全輸入 API 金鑰。

4. **定義模型和圖片路徑**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    此部分設置使用的模型，建立指定模型的 `ChatNVIDIA` 實例，並定義圖片檔案的路徑。

5. **建立文字提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    此部分定義了一個文字提示，用於指導模型生成處理圖片的 Python 程式碼。

6. **將圖片編碼為 Base64**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    此程式碼讀取圖片檔案，將其編碼為 Base64，並使用編碼的資料建立 HTML 圖片標籤。

7. **將文字和圖片結合到提示中**：
    ```python
    prompt = f"{text} {image}"
    ```
    此部分將文字提示和 HTML 圖片標籤合併成一個字串。

8. **使用 ChatNVIDIA 生成程式碼**：
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    此程式碼將提示發送至 `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` 字串。

9. **從生成內容中提取 Python 程式碼**：
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    此部分通過移除 Markdown 格式，提取生成內容中的實際 Python 程式碼。

10. **執行生成的程式碼**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    此部分以子程序的形式執行提取的 Python 程式碼並捕捉其輸出。

11. **顯示圖片**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    這些程式碼使用 `IPython.display` 模組來顯示圖片。

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件應被視為具權威性的來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。