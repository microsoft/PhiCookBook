Phi-3-mini WebGPU RAG 聊天機器人

## 展示 WebGPU 與 RAG 模式的示範
結合 Phi-3 Onnx 託管模型的 RAG 模式，採用檢索增強生成（Retrieval-Augmented Generation）方法，將 Phi-3 模型的強大能力與 ONNX 託管結合，實現高效的 AI 部署。此模式對於針對特定領域任務進行模型微調非常有用，兼具品質、成本效益與長上下文理解能力。它是 Azure AI 套件的一部分，提供多種易於尋找、嘗試和使用的模型，滿足各行各業的客製化需求。Phi-3 系列模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，均可在 Azure AI Model Catalog 上取得，並可自行管理微調與部署，或透過 HuggingFace 和 ONNX 等平台，展現微軟致力於提供易用且高效 AI 解決方案的承諾。

## 什麼是 WebGPU
WebGPU 是一個現代化的網頁圖形 API，設計用來直接從瀏覽器高效存取裝置的圖形處理器（GPU）。它是 WebGL 的後繼者，帶來多項重要改進：

1. **支援現代 GPU 架構**：WebGPU 能無縫配合當代 GPU 架構，利用 Vulkan、Metal 和 Direct3D 12 等系統 API。
2. **提升效能**：支援通用 GPU 運算與更快速的操作，適合圖形渲染與機器學習任務。
3. **進階功能**：提供更多先進 GPU 能力，支援更複雜且動態的圖形與計算工作負載。
4. **減輕 JavaScript 負擔**：將更多任務交由 GPU 處理，大幅降低 JavaScript 的工作量，帶來更佳效能與流暢體驗。

目前 WebGPU 已在 Google Chrome 等瀏覽器支援，並持續擴展至其他平台。

### 03.WebGPU
所需環境：

**支援瀏覽器：**  
- Google Chrome 113 以上  
- Microsoft Edge 113 以上  
- Safari 18（macOS 15）  
- Firefox Nightly

### 啟用 WebGPU：

- 在 Chrome/Microsoft Edge 中

啟用 `chrome://flags/#enable-unsafe-webgpu` 標誌。

#### 開啟瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 進入 Flags 頁面：
在網址列輸入 `chrome://flags`，按下 Enter。

#### 搜尋標誌：
在頁面頂端的搜尋框輸入 'enable-unsafe-webgpu'

#### 啟用標誌：
在結果列表中找到 #enable-unsafe-webgpu 標誌。

點擊旁邊的下拉選單，選擇 Enabled。

#### 重新啟動瀏覽器：

啟用標誌後，需重新啟動瀏覽器使設定生效。點擊頁面底部出現的 Relaunch 按鈕。

- Linux 系統請使用 `--enable-features=Vulkan` 參數啟動瀏覽器。  
- Safari 18（macOS 15）預設已啟用 WebGPU。  
- Firefox Nightly 輸入 about:config，將 `dom.webgpu.enabled` 設為 true。

### 為 Microsoft Edge 設定 GPU

以下是在 Windows 上為 Microsoft Edge 設定高效能 GPU 的步驟：

- **開啟設定：** 點擊開始選單，選擇設定。  
- **系統設定：** 進入系統，然後選擇顯示。  
- **圖形設定：** 向下捲動並點擊圖形設定。  
- **選擇應用程式：** 在「選擇要設定偏好的應用程式」中，選擇桌面應用程式，然後點擊瀏覽。  
- **選擇 Edge：** 導航至 Edge 安裝資料夾（通常為 `C:\Program Files (x86)\Microsoft\Edge\Application`），選擇 `msedge.exe`。  
- **設定偏好：** 點擊選項，選擇高效能，然後點擊儲存。  
這樣可確保 Microsoft Edge 使用高效能 GPU 以提升效能。  
- **重新啟動** 電腦以使設定生效。

### 開啟你的 Codespace：
前往 GitHub 上的你的儲存庫。  
點擊 Code 按鈕，選擇 Open with Codespaces。

如果還沒有 Codespace，可以點擊 New codespace 建立一個。

**注意** 在你的 Codespace 中安裝 Node 環境  
從 GitHub Codespace 執行 npm 示範是測試與開發專案的好方法。以下是入門指南：

### 設定你的環境：
Codespace 開啟後，確認已安裝 Node.js 與 npm。可執行以下指令檢查：  
```
node -v
```  
```
npm -v
```

若未安裝，可使用以下指令安裝：  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### 進入專案目錄：
使用終端機切換到 npm 專案所在目錄：  
```
cd path/to/your/project
```

### 安裝相依套件：
執行以下指令安裝 package.json 中列出的所有相依套件：

```
npm install
```

### 執行示範：
安裝完成後，即可執行示範腳本。通常在 package.json 的 scripts 區段定義，例如示範腳本名稱為 start，則執行：

```
npm run build
```  
```
npm run dev
```

### 存取示範：
若示範包含網頁伺服器，Codespaces 會提供存取 URL。請留意通知或查看 Ports 分頁以取得網址。

**注意：** 模型需先快取於瀏覽器，載入可能需要一些時間。

### RAG 示範
上傳 markdown 檔案 `intro_rag.md` 以完成 RAG 解決方案。若使用 Codespaces，可下載位於 `01.InferencePhi3/docs/` 的檔案。

### 選擇檔案：
點擊「Choose File」按鈕，選擇要上傳的文件。

### 上傳文件：
選擇檔案後，點擊「Upload」按鈕，將文件載入以進行 RAG（檢索增強生成）。

### 開始聊天：
文件上傳完成後，即可根據文件內容開始 RAG 聊天。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。