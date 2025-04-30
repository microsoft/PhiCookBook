<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c7a7f2a07dc176c19e1ab9f249b548c9",
  "translation_date": "2025-04-04T05:33:42+00:00",
  "source_file": "code\\08.RAG\\rag_webgpu_chat\\README.md",
  "language_code": "tw"
}
-->
Phi-3-mini WebGPU RAG 聊天機器人

## 展示 WebGPU 和 RAG 模式的示範
使用 Phi-3 Onnx Hosted 模型的 RAG 模式採用檢索增強生成（Retrieval-Augmented Generation）方法，結合 Phi-3 模型的強大功能和 ONNX 託管技術，提供高效的 AI 部署。此模式在微調模型以滿足特定領域任務方面具有重要作用，兼具品質、成本效益及長上下文理解能力。這是 Azure AI 套件的一部分，提供一系列易於查找、試用和使用的模型，滿足各行業的客製化需求。Phi-3 模型（包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium）可在 Azure AI 模型目錄中找到，並能自我管理微調和部署，也可通過 HuggingFace 和 ONNX 平台使用，展現了 Microsoft 致力於提供便捷高效 AI 解決方案的承諾。

## 什麼是 WebGPU
WebGPU 是一個現代化的網頁圖形 API，旨在直接從網頁瀏覽器高效地訪問設備的圖形處理單元（GPU）。它被設計為 WebGL 的後繼者，並提供以下幾項主要改進：

1. **兼容現代 GPU**：WebGPU 能夠無縫適配當代 GPU 架構，利用系統 API 如 Vulkan、Metal 和 Direct3D 12。
2. **提升性能**：它支持通用 GPU 計算和更快速的操作，適合圖形渲染和機器學習任務。
3. **高級功能**：WebGPU 提供更多高級 GPU 功能的訪問，支持更複雜且動態的圖形和計算工作負載。
4. **減少 JavaScript 負擔**：通過將更多任務交給 GPU，WebGPU 顯著降低 JavaScript 的負擔，從而提升性能並提供更流暢的體驗。

目前 WebGPU 已在 Google Chrome 等瀏覽器中支持，並正努力擴展到其他平台。

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

#### 打開您的瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 訪問 Flags 頁面：
在地址欄中輸入 `chrome://flags`，然後按 Enter。

#### 搜索標誌：
在頁面頂部的搜索框中輸入 'enable-unsafe-webgpu'。

#### 啟用標誌：
在搜索結果中找到 #enable-unsafe-webgpu 標誌。

點擊旁邊的下拉菜單，選擇 Enabled。

#### 重啟瀏覽器：

啟用標誌後，您需要重啟瀏覽器以使更改生效。點擊頁面底部出現的重新啟動按鈕。

- 對於 Linux，用 `--enable-features=Vulkan` 啟動瀏覽器。
- Safari 18 (macOS 15) 預設啟用 WebGPU。
- 在 Firefox Nightly 中，輸入 about:config 到地址欄，然後 `set dom.webgpu.enabled to true`。

### 在 Microsoft Edge 中設置 GPU 

以下是為 Microsoft Edge 設置高性能 GPU 的步驟（Windows 系統）：

- **打開設定：** 點擊開始菜單並選擇設定。
- **系統設定：** 前往系統，然後點擊顯示。
- **圖形設定：** 向下滾動並點擊圖形設定。
- **選擇應用程式：** 在“選擇應用程式以設置偏好”下選擇桌面應用程式，然後點擊瀏覽。
- **選擇 Edge：** 導航到 Edge 的安裝文件夾（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），選擇 `msedge.exe`。
- **設置偏好：** 點擊選項，選擇高性能，然後點擊保存。
這將確保 Microsoft Edge 使用您的高性能 GPU 以提升性能。
- **重啟**您的設備以使這些設定生效。

### 打開您的 Codespace：
前往 GitHub 上的倉庫。
點擊代碼按鈕，選擇用 Codespaces 打開。

如果尚未創建 Codespace，可以點擊新建 Codespace。

**注意** 在您的 Codespace 中安裝 Node 環境
在 GitHub Codespace 中運行 npm 示範是測試和開發項目的好方法。以下是操作指南：

### 設置您的環境：
打開 Codespace 後，確保已安裝 Node.js 和 npm。您可以通過運行以下命令檢查：
```
node -v
```
```
npm -v
```

如果尚未安裝，可以通過以下命令進行安裝：
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### 導航到您的項目目錄：
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
依賴項安裝完成後，您可以運行示範腳本。通常在 package.json 的 scripts 部分中指定。例如，如果示範腳本名為 start，可以運行：

```
npm run build
```
```
npm run dev
```

### 訪問示範：
如果示範涉及到 Web 服務器，Codespaces 將提供一個 URL 供您訪問。查看通知或檢查 Ports 標籤以找到 URL。

**注意：** 模型需要在瀏覽器中緩存，因此可能需要一些時間加載。

### RAG 示範
上傳 markdown 文件 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### 選擇您的文件：
點擊顯示“選擇文件”的按鈕以選擇您想上傳的文檔。

### 上傳文檔：
選擇文件後，點擊“上傳”按鈕以加載文檔用於 RAG（檢索增強生成）。

### 開始聊天：
文檔上傳完成後，您可以基於文檔內容使用 RAG 開始聊天。

**免責聲明**：  
本文檔使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。