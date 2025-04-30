<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "faa063cfc6d50047bbfdb58a90d520ad",
  "translation_date": "2025-04-04T06:33:47+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\WebGPUWithPhi35Readme.md",
  "language_code": "tw"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## 展示 WebGPU 和 RAG 模式的示範

Phi-3.5 Onnx Hosted 模型的 RAG 模式採用了檢索增強生成（Retrieval-Augmented Generation）方法，結合 Phi-3.5 模型的強大功能與 ONNX 主機的高效 AI 部署。此模式在針對特定領域任務進行模型微調時非常重要，提供了高品質、成本效益以及長文本理解的平衡。這是 Azure AI 套件的一部分，提供多樣化的模型選擇，方便各行業的使用者找到、嘗試並使用，滿足定制化需求。

## 什麼是 WebGPU
WebGPU 是一種現代化的網頁圖形 API，旨在直接從網頁瀏覽器高效存取設備的圖形處理單元（GPU）。它被設計為 WebGL 的後繼技術，具備以下幾項重要改進：

1. **與現代 GPU 的相容性**：WebGPU 專為當代 GPU 架構設計，利用系統 API，如 Vulkan、Metal 和 Direct3D 12。
2. **提升效能**：支援通用 GPU 計算及更快的操作，適合圖形渲染和機器學習任務。
3. **進階功能**：WebGPU 提供更高級的 GPU 功能，能處理更複雜且動態的圖形及計算工作負載。
4. **減少 JavaScript 負擔**：透過將更多任務交由 GPU 處理，WebGPU 大幅減少 JavaScript 的負擔，提升效能並提供更流暢的使用體驗。

目前 WebGPU 已在 Google Chrome 等瀏覽器中提供支援，並正在努力擴展至其他平台。

### 03.WebGPU
所需環境：

**支援的瀏覽器：** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly

### 啟用 WebGPU：

- 在 Chrome/Microsoft Edge 中

啟用 `chrome://flags/#enable-unsafe-webgpu` 標籤。

#### 打開瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 訪問 Flags 頁面：
在地址欄輸入 `chrome://flags` 並按 Enter。

#### 搜尋標籤：
在頁面頂部的搜尋框中輸入 "enable-unsafe-webgpu"。

#### 啟用標籤：
在搜尋結果中找到 #enable-unsafe-webgpu 標籤。

點擊旁邊的下拉選單並選擇 Enabled。

#### 重啟瀏覽器：

啟用標籤後，需重啟瀏覽器以使更改生效。點擊頁面底部出現的 Relaunch 按鈕。

- 對於 Linux，用 `--enable-features=Vulkan` 啟動瀏覽器。
- Safari 18 (macOS 15) 預設啟用 WebGPU。
- 在 Firefox Nightly 中，於地址欄輸入 about:config 並 `set dom.webgpu.enabled to true`。

### 在 Microsoft Edge 上設置 GPU 

以下是為 Windows 上的 Microsoft Edge 設置高效能 GPU 的步驟：

- **打開設定：** 點擊開始選單並選擇設定。
- **系統設定：** 前往系統，然後選擇顯示。
- **圖形設定：** 向下滾動並點擊圖形設定。
- **選擇應用程式：** 在「選擇應用程式設置偏好」下，選擇桌面應用程式，然後點擊瀏覽。
- **選擇 Edge：** 導航至 Edge 的安裝文件夾（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），然後選擇 `msedge.exe`。
- **設置偏好：** 點擊選項，選擇高效能，然後點擊儲存。
這將確保 Microsoft Edge 使用您的高效能 GPU，以獲得更好的效能。
- **重啟**您的設備以使這些設定生效。

### 示例：請[點擊此鏈接](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能會包含錯誤或不精確之處。原始語言的文件應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤解概不負責。