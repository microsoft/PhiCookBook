<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c7a7f2a07dc176c19e1ab9f249b548c9",
  "translation_date": "2025-04-04T17:23:31+00:00",
  "source_file": "code\\08.RAG\\rag_webgpu_chat\\README.md",
  "language_code": "hk"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## 示範展示 WebGPU 和 RAG 模式
使用 Phi-3 Onnx Hosted 模型的 RAG 模式採用 Retrieval-Augmented Generation 方法，結合 Phi-3 模型的強大功能和 ONNX 託管，以實現高效的 AI 部署。這種模式在模型微調方面非常有用，適用於特定領域任務，提供了質量、成本效益和長上下文理解的良好平衡。它是 Azure AI 套件的一部分，提供多種易於找到、試用和使用的模型，滿足各行業的定制需求。Phi-3 模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，可在 Azure AI Model Catalog 上找到，並可進行自管理部署或通過 HuggingFace 和 ONNX 平台部署，展示了 Microsoft 致力於提供可訪問和高效 AI 解決方案的承諾。

## 什麼是 WebGPU
WebGPU 是一種現代化的網頁圖形 API，旨在直接從網頁瀏覽器高效訪問設備的圖形處理單元（GPU）。它被設計為 WebGL 的繼任者，提供了以下幾個重要改進：

1. **兼容現代 GPU**：WebGPU 專為當代 GPU 架構設計，利用系統 API 如 Vulkan、Metal 和 Direct3D 12。
2. **性能提升**：支持通用 GPU 計算和更快的操作，適用於圖形渲染和機器學習任務。
3. **高級功能**：提供更高級的 GPU 功能，能夠處理更複雜和動態的圖形及計算工作負載。
4. **減少 JavaScript 負擔**：通過將更多任務交給 GPU，WebGPU 大幅減少了 JavaScript 的工作量，從而提升性能和流暢度。

目前 WebGPU 在 Google Chrome 等瀏覽器中得到支持，並在擴展到其他平台的工作中。

### 03.WebGPU
所需環境：

**支持的瀏覽器：**
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly

### 啟用 WebGPU：

- 在 Chrome/Microsoft Edge 中

啟用 `chrome://flags/#enable-unsafe-webgpu` 標誌。

#### 打開瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 訪問 Flags 頁面：
在地址欄中輸入 `chrome://flags`，然後按 Enter。

#### 搜索標誌：
在頁面頂部的搜索框中輸入 'enable-unsafe-webgpu'

#### 啟用標誌：
在搜索結果中找到 #enable-unsafe-webgpu 標誌。

點擊旁邊的下拉菜單並選擇 Enabled。

#### 重啟瀏覽器：

啟用標誌後，需重啟瀏覽器以使更改生效。點擊頁面底部出現的重新啟動按鈕。

- 對於 Linux，用 `--enable-features=Vulkan` 啟動瀏覽器。
- Safari 18 (macOS 15) 默認啟用了 WebGPU。
- 在 Firefox Nightly 中，進入地址欄輸入 about:config 並 `set dom.webgpu.enabled to true`。

### 為 Microsoft Edge 設置 GPU 

以下是在 Windows 上為 Microsoft Edge 設置高性能 GPU 的步驟：

- **打開設置：** 點擊開始菜單並選擇設置。
- **系統設置：** 進入系統，然後選擇顯示。
- **圖形設置：** 滾動到下方並點擊圖形設置。
- **選擇應用：** 在“選擇應用設置偏好”下選擇桌面應用，然後瀏覽。
- **選擇 Edge：** 導航到 Edge 安裝文件夾（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），然後選擇 `msedge.exe`。
- **設置偏好：** 點擊選項，選擇高性能，然後點擊保存。
這樣可以確保 Microsoft Edge 使用您的高性能 GPU 以提升性能。
- **重啟**機器以使設置生效。

### 打開 Codespace：
導航到您的 GitHub 存儲庫。
點擊 Code 按鈕並選擇 Open with Codespaces。

如果您還沒有 Codespace，可以點擊 New codespace 創建一個。

**注意** 在您的 Codespace 中安裝 Node 環境
在 GitHub Codespace 中運行 npm 示範是測試和開發項目的絕佳方式。以下是幫助您入門的分步指南：

### 設置環境：
打開 Codespace 後，確保已安裝 Node.js 和 npm。您可以通過運行以下命令進行檢查：
```
node -v
```
```
npm -v
```

如果尚未安裝，可以使用以下命令進行安裝：
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### 導航到項目目錄：
使用終端導航到 npm 項目所在的目錄：
```
cd path/to/your/project
```

### 安裝依賴項：
運行以下命令以安裝 package.json 文件中列出的所有必要依賴項：

```
npm install
```

### 運行示範：
依賴項安裝完成後，您可以運行示範腳本。通常在 package.json 的 scripts 部分中指定。例如，如果您的示範腳本名為 start，可以運行：

```
npm run build
```
```
npm run dev
```

### 訪問示範：
如果您的示範涉及到網頁服務器，Codespaces 會提供一個 URL 供您訪問。查看通知或檢查 Ports 標籤以找到 URL。

**注意：** 模型需要在瀏覽器中緩存，因此可能需要一些時間加載。

### RAG 示範
上傳 markdown 文件 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### 選擇文件：
點擊“Choose File”按鈕選擇您要上傳的文檔。

### 上傳文檔：
選擇文件後，點擊“Upload”按鈕加載您的文檔以進行 RAG（Retrieval-Augmented Generation）。

### 開始聊天：
文檔上傳完成後，您可以根據文檔內容使用 RAG 開始聊天會話。

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文作為權威來源。對於關鍵信息，建議尋求專業的人工翻譯。我們對因使用本翻譯而引起的任何誤解或錯誤解釋概不負責。