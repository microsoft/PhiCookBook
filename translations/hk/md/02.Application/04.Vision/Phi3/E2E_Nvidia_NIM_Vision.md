<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "99474e9687279d0657412c806856b559",
  "translation_date": "2025-04-04T18:40:34+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_Nvidia_NIM_Vision.md",
  "language_code": "hk"
}
-->
### 示例情境

假設你有一張圖片 (`demo.png`)，你想生成處理這張圖片並保存其新版本的 Python 代碼 (`phi-3-vision.jpg`)。

上面的代碼自動化了這個過程，具體步驟如下：

1. 設置環境和必要的配置。
2. 創建一個提示，指示模型生成所需的 Python 代碼。
3. 將提示發送給模型並收集生成的代碼。
4. 提取並執行生成的代碼。
5. 顯示原始圖片和處理後的圖片。

這種方法利用了 AI 的強大功能來自動化圖像處理任務，使你更輕鬆快捷地實現目標。

[範例代碼解決方案](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

接下來我們一步步解析整段代碼的作用：

1. **安裝所需套件**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    該命令安裝了 `langchain_nvidia_ai_endpoints` 套件，並確保其為最新版本。

2. **導入必要模組**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    這些導入負責與 NVIDIA AI 端點交互、安全處理密碼、與操作系統交互，以及以 base64 格式編碼/解碼數據。

3. **設置 API 金鑰**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    這段代碼檢查環境變量 `NVIDIA_API_KEY` 是否已設置。如果未設置，則提示用戶安全地輸入 API 金鑰。

4. **定義模型和圖片路徑**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    這裡設置了要使用的模型，創建了一個 `ChatNVIDIA` 實例並指定了圖片文件的路徑。

5. **創建文字提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    這裡定義了一個文字提示，指示模型生成用於處理圖片的 Python 代碼。

6. **將圖片編碼為 Base64**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    這段代碼讀取圖片文件，將其編碼為 Base64，並生成帶有編碼數據的 HTML 圖片標籤。

7. **將文字和圖片結合到提示中**：
    ```python
    prompt = f"{text} {image}"
    ```
    這裡將文字提示和 HTML 圖片標籤結合為一個字符串。

8. **使用 ChatNVIDIA 生成代碼**：
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    這段代碼將提示發送給 `ChatNVIDIA`，並將生成的代碼存儲到 `code` 字符串中。

9. **從生成的內容中提取 Python 代碼**：
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    這裡通過去除 markdown 格式提取實際的 Python 代碼。

10. **運行生成的代碼**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    這段代碼以子進程方式運行提取的 Python 代碼，並捕獲其輸出。

11. **顯示圖片**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    這些行使用 `IPython.display` 模組顯示圖片。

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。如涉及關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋概不負責。