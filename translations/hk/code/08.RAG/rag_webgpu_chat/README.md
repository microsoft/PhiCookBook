<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-08T06:47:48+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "hk"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## 展示 WebGPU 同 RAG 模式嘅示範
用 Phi-3 Onnx Hosted model 嘅 RAG 模式採用 Retrieval-Augmented Generation 方法，結合咗 Phi-3 模型同 ONNX hosting 嘅優勢，令 AI 部署更加高效。呢個模式對於針對特定領域任務嘅模型微調非常重要，提供質素、成本效益同長上下文理解嘅平衡。佢係 Azure AI 嘅一部分，提供多款容易搵到、試用同使用嘅模型，滿足唔同行業嘅定制需求。Phi-3 系列模型，包括 Phi-3-mini、Phi-3-small 同 Phi-3-medium，都喺 Azure AI Model Catalog 上架，可以自行微調同部署，或者透過 HuggingFace 同 ONNX 等平台，展示咗 Microsoft 致力於提供易用同高效 AI 解決方案嘅承諾。

## 乜嘢係 WebGPU
WebGPU 係一個現代網頁圖形 API，設計用嚟直接喺瀏覽器入面高效使用裝置嘅圖形處理器（GPU）。佢係 WebGL 嘅後繼者，帶嚟幾個主要改進：

1. **兼容現代 GPU**：WebGPU 專為現代 GPU 架構設計，利用 Vulkan、Metal 同 Direct3D 12 等系統 API。
2. **提升效能**：支持通用 GPU 運算同更快嘅操作，適合圖形渲染同機器學習任務。
3. **先進功能**：提供更多高級 GPU 能力，支持更複雜同動態嘅圖形同計算工作負載。
4. **減輕 JavaScript 負擔**：將更多工作交畀 GPU 處理，大大減少 JavaScript 嘅運算量，令效能更好同體驗更流暢。

而家 WebGPU 已經喺 Google Chrome 等瀏覽器支援，仲有持續努力擴展到其他平台。

### 03.WebGPU
所需環境：

**支援嘅瀏覽器：**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly。

### 啟用 WebGPU：

- 喺 Chrome/Microsoft Edge

啟用 `chrome://flags/#enable-unsafe-webgpu` 標誌。

#### 打開瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 進入 Flags 頁面：
喺地址欄輸入 `chrome://flags`，然後按 Enter。

#### 搜尋標誌：
喺頁面頂部嘅搜尋框輸入 'enable-unsafe-webgpu'。

#### 啟用標誌：
喺結果列表搵到 #enable-unsafe-webgpu 標誌。

喺旁邊嘅下拉菜單揀選 Enabled。

#### 重啟瀏覽器：

啟用後，需要重啟瀏覽器先會生效。點擊頁面底部出現嘅 Relaunch 按鈕。

- Linux 用戶，啟動瀏覽器時加 `--enable-features=Vulkan` 參數。  
- Safari 18 (macOS 15) 預設已啟用 WebGPU。  
- Firefox Nightly，喺地址欄輸入 about:config，然後 `set dom.webgpu.enabled to true`。

### 喺 Microsoft Edge 設置 GPU

喺 Windows 上為 Microsoft Edge 設置高性能 GPU 嘅步驟：

- **打開設定：** 點擊開始菜單，揀 Settings。  
- **系統設定：** 進入 System，再揀 Display。  
- **圖形設定：** 向下捲動，點擊 Graphics settings。  
- **選擇應用程式：** 喺「Choose an app to set preference」底下，揀 Desktop app，再點 Browse。  
- **揀 Edge：** 去到 Edge 安裝資料夾（通常係 `C:\Program Files (x86)\Microsoft\Edge\Application`），揀 `msedge.exe`。  
- **設定偏好：** 點 Options，揀 High performance，跟住按 Save。  
咁樣可以確保 Microsoft Edge 用高性能 GPU，提升效能。  
- **重啟** 電腦，令設定生效。

### 打開你嘅 Codespace：
去 GitHub 上你嘅 repository。  
點 Code 按鈕，揀 Open with Codespaces。

如果未有 Codespace，可以點 New codespace 建立一個。

**Note** 安裝 Node 環境喺你嘅 codespace  
喺 GitHub Codespace 運行 npm 示範係測試同開發項目嘅好方法。以下係一步步指引：

### 設置環境：
Codespace 開啟後，確保已安裝 Node.js 同 npm。可以用以下指令檢查：  
```
node -v
```  
```
npm -v
```

如果未安裝，可以用以下指令安裝：  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### 進入項目目錄：
用終端機去到你嘅 npm 項目目錄：  
```
cd path/to/your/project
```

### 安裝依賴：
執行以下指令安裝 package.json 裏面嘅所有依賴：  
```
npm install
```

### 運行示範：
依賴安裝完成後，可以運行示範腳本。通常喺 package.json 嘅 scripts 裏面指定，例如腳本名係 start，就用：  
```
npm run build
```  
```
npm run dev
```

### 訪問示範：
如果示範涉及網頁服務器，Codespaces 會提供訪問 URL。留意通知或喺 Ports 標籤頁搵 URL。

**Note:** 模型需要喺瀏覽器緩存，所以加載可能會花啲時間。

### RAG 示範
上載 markdown 文件 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### 選擇文件：
點擊「Choose File」按鈕，揀你想上載嘅文件。

### 上載文件：
揀好文件後，點「Upload」按鈕，將文件上載用嚟做 RAG（Retrieval-Augmented Generation）。

### 開始對話：
文件上載完成後，可以根據文件內容開始 RAG 對話。

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件以其原始語言版本為準。對於重要資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而引致的任何誤解或誤釋承擔責任。