<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-08T05:43:22+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "tw"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## 展示 WebGPU 與 RAG 模式的 Demo

搭配 Phi-3.5 Onnx Hosted 模型的 RAG 模式，運用了檢索增強生成（Retrieval-Augmented Generation）的方法，結合 Phi-3.5 模型與 ONNX 托管的強大功能，實現高效的 AI 部署。這個模式對於針對特定領域任務微調模型非常有幫助，兼具品質、成本效益與長上下文理解能力。它是 Azure AI 套件的一部分，提供多種容易尋找、試用與使用的模型，滿足各行各業的客製化需求。

## 什麼是 WebGPU  
WebGPU 是一個現代化的網頁圖形 API，設計用來直接從瀏覽器高效存取裝置的圖形處理器（GPU）。它被定位為 WebGL 的後繼者，帶來以下幾項主要改進：

1. **與現代 GPU 相容**：WebGPU 能無縫配合當代 GPU 架構，利用 Vulkan、Metal 和 Direct3D 12 等系統 API。
2. **效能提升**：支援通用 GPU 計算與更快速的運算，適合圖形渲染和機器學習任務。
3. **進階功能**：提供更多進階 GPU 能力，能處理更複雜且動態的圖形與運算工作負載。
4. **減輕 JavaScript 負擔**：將更多工作交給 GPU，顯著降低 JavaScript 的負擔，帶來更佳效能與流暢體驗。

目前 WebGPU 已在 Google Chrome 等瀏覽器支援，並持續擴展到其他平台。

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
在網址列輸入 `chrome://flags`，然後按 Enter。

#### 搜尋標誌：  
在頁面頂端的搜尋框輸入 'enable-unsafe-webgpu'。

#### 啟用標誌：  
在結果列表中找到 #enable-unsafe-webgpu 標誌。

點選旁邊的下拉選單，選擇 Enabled。

#### 重新啟動瀏覽器：

啟用標誌後，需要重新啟動瀏覽器讓設定生效。點選頁面底部出現的 Relaunch 按鈕。

- Linux 系統請使用 `--enable-features=Vulkan` 來啟動瀏覽器。  
- Safari 18（macOS 15）預設已啟用 WebGPU。  
- Firefox Nightly 在網址列輸入 about:config 並 `set dom.webgpu.enabled to true`。

### 在 Microsoft Edge 設定 GPU

以下是在 Windows 上為 Microsoft Edge 設定高效能 GPU 的步驟：

- **開啟設定：** 點選開始選單並選擇設定。  
- **系統設定：** 進入系統，然後選擇顯示。  
- **圖形設定：** 向下捲動並點選圖形設定。  
- **選擇應用程式：** 在「選擇要設定偏好的應用程式」下，選擇桌面應用程式，然後點選瀏覽。  
- **選擇 Edge：** 導覽到 Edge 安裝資料夾（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），選擇 `msedge.exe`。  
- **設定偏好：** 點選選項，選擇高效能，然後按儲存。  
這樣就能確保 Microsoft Edge 使用你的高效能 GPU 以提升效能。  
- **重新啟動** 電腦讓設定生效。

### 範例：請[點此連結](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。