<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-08T06:48:13+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "tw"
}
-->
Phi-3-mini WebGPU RAG 聊天機器人

## 展示 WebGPU 與 RAG 模式的示範
搭配 Phi-3 Onnx 託管模型的 RAG 模式，運用了檢索增強生成（Retrieval-Augmented Generation）的方法，結合 Phi-3 模型與 ONNX 託管的優勢，實現高效的 AI 部署。這個模式對於針對特定領域任務的模型微調非常重要，兼具品質、成本效益與長上下文理解能力。它是 Azure AI 服務的一部分，提供多種易於搜尋、試用與使用的模型，滿足各行各業的客製化需求。Phi-3 系列模型，包括 Phi-3-mini、Phi-3-small 與 Phi-3-medium，都可在 Azure AI Model Catalog 找到，並且能夠自行管理微調與部署，或透過 HuggingFace 和 ONNX 等平台，展現微軟致力於打造易用且高效 AI 解決方案的決心。

## 什麼是 WebGPU
WebGPU 是一個現代化的網頁圖形 API，設計用來讓瀏覽器能夠直接有效率地存取裝置的圖形處理器（GPU）。它是 WebGL 的下一代，帶來多項重要改進：

1. **與現代 GPU 相容**：WebGPU 專為當代 GPU 架構打造，並利用 Vulkan、Metal、Direct3D 12 等系統 API。
2. **效能提升**：支援通用 GPU 運算與更快的操作，適合用於圖形渲染和機器學習任務。
3. **進階功能**：提供更多先進的 GPU 能力，能處理更複雜且動態的圖形與運算工作負載。
4. **減輕 JavaScript 負擔**：將更多工作交給 GPU 處理，大幅降低 JavaScript 的負擔，帶來更佳效能與流暢體驗。

目前 WebGPU 已在 Google Chrome 等瀏覽器支援，並持續擴展至其他平台。

### 03.WebGPU
必要環境：

**支援瀏覽器：**  
- Google Chrome 113 以上  
- Microsoft Edge 113 以上  
- Safari 18（macOS 15）  
- Firefox Nightly  

### 啟用 WebGPU：

- 在 Chrome/Microsoft Edge  

啟用 `chrome://flags/#enable-unsafe-webgpu` 旗標。

#### 開啟瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 進入 Flags 頁面：
在網址列輸入 `chrome://flags`，然後按 Enter。

#### 搜尋旗標：
在頁面頂端的搜尋框輸入 'enable-unsafe-webgpu'

#### 啟用旗標：
在結果中找到 #enable-unsafe-webgpu 旗標。

點擊旁邊的下拉選單，選擇 Enabled。

#### 重新啟動瀏覽器：

啟用旗標後，必須重新啟動瀏覽器才能生效。點擊頁面底部出現的 Relaunch 按鈕。

- Linux 系統可用 `--enable-features=Vulkan` 參數啟動瀏覽器。  
- Safari 18（macOS 15）預設已啟用 WebGPU。  
- Firefox Nightly 在網址列輸入 about:config，並 `set dom.webgpu.enabled to true`。

### 在 Microsoft Edge 設定 GPU

以下是在 Windows 上為 Microsoft Edge 設定高效能 GPU 的步驟：

- **開啟設定：** 點擊開始選單並選擇設定。  
- **系統設定：** 進入系統，然後選擇顯示。  
- **圖形設定：** 向下捲動並點擊圖形設定。  
- **選擇應用程式：** 在「選擇應用程式以設定偏好」中，選擇桌面應用程式，然後點擊瀏覽。  
- **選擇 Edge：** 導航至 Edge 安裝資料夾（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），並選擇 `msedge.exe`。  
- **設定偏好：** 點擊選項，選擇高效能，然後點擊儲存。  
這樣可以確保 Microsoft Edge 使用高效能 GPU 以提升效能。  
- **重新啟動** 電腦以讓設定生效。

### 開啟你的 Codespace：
前往 GitHub 上你的儲存庫。  
點擊 Code 按鈕，選擇 Open with Codespaces。

如果還沒有 Codespace，可以點擊 New codespace 新建。

**注意** 安裝 Node 環境於你的 Codespace  
從 GitHub Codespace 執行 npm 示範是測試與開發專案的好方法。以下是入門步驟：

### 設定環境：
Codespace 開啟後，確認已安裝 Node.js 與 npm。可透過執行以下指令檢查：  
```
node -v
```  
```
npm -v
```

若尚未安裝，可使用以下指令安裝：  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### 移動到專案目錄：
使用終端機切換到 npm 專案所在的目錄：  
```
cd path/to/your/project
```

### 安裝相依套件：
執行以下指令，安裝 package.json 中列出的所有相依套件：  

```
npm install
```

### 執行示範：
安裝完成後，即可執行示範腳本。通常在 package.json 的 scripts 區段指定，假設示範腳本名稱為 start，可執行：  

```
npm run build
```  
```
npm run dev
```

### 存取示範：
若示範包含網頁伺服器，Codespaces 會提供可存取的 URL。請留意通知或在 Ports 標籤中查找 URL。

**注意：** 模型需要在瀏覽器中快取，載入可能需要一些時間。

### RAG 示範
上傳 markdown 檔案 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### 選擇你的檔案：
點擊「Choose File」按鈕，選擇要上傳的文件。

### 上傳文件：
選擇檔案後，點擊「Upload」按鈕，將文件載入以進行 RAG（檢索增強生成）。

### 開始聊天：
文件上傳完成後，即可根據文件內容開始使用 RAG 進行聊天。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。本公司不對因使用本翻譯而產生之任何誤解或誤釋負責。