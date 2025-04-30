<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "faa063cfc6d50047bbfdb58a90d520ad",
  "translation_date": "2025-04-04T18:25:35+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\WebGPUWithPhi35Readme.md",
  "language_code": "hk"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## 展示 WebGPU 和 RAG 模式的示範

使用 Phi-3.5 Onnx Hosted 模型的 RAG 模式採用檢索增強生成（Retrieval-Augmented Generation）方法，結合 Phi-3.5 模型的能力與 ONNX 託管進行高效的 AI 部署。這種模式對於針對特定領域的任務進行模型微調非常重要，提供了品質、成本效益和長篇內容理解的完美結合。它是 Azure AI 套件的一部分，提供多樣化的模型，方便用戶尋找、試用和使用，滿足各行業的定制需求。

## 什麼是 WebGPU
WebGPU 是一個現代化的網頁圖形 API，旨在直接從網頁瀏覽器高效訪問設備的圖形處理單元（GPU）。它是 WebGL 的繼任者，並提供了以下幾個主要改進：

1. **兼容現代 GPU**：WebGPU 專為當前 GPU 架構而設計，利用系統 API（如 Vulkan、Metal 和 Direct3D 12），實現無縫運作。
2. **性能提升**：支持通用 GPU 計算和更快的操作，適用於圖形渲染和機器學習任務。
3. **高級功能**：提供對更高級 GPU 功能的訪問，能處理更複雜且動態的圖形和計算工作負載。
4. **減少 JavaScript 負擔**：通過將更多任務交給 GPU 處理，WebGPU 大幅降低 JavaScript 的負擔，帶來更好的性能和更流暢的使用體驗。

目前 WebGPU 支持於 Google Chrome 等瀏覽器，並且正在努力擴展到其他平台。

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
在地址欄中輸入 `chrome://flags`，然後按下 Enter。

#### 搜索標誌：
在頁面頂部的搜索框中輸入 'enable-unsafe-webgpu'

#### 啟用標誌：
在搜索結果中找到 #enable-unsafe-webgpu 標誌。

點擊旁邊的下拉菜單並選擇 Enabled。

#### 重啟瀏覽器：

啟用標誌後，您需要重啟瀏覽器以使更改生效。點擊頁面底部顯示的 Relaunch 按鈕。

- 對於 Linux，用 `--enable-features=Vulkan` 啟動瀏覽器。
- Safari 18 (macOS 15) 預設啟用 WebGPU。
- 在 Firefox Nightly 中，輸入 about:config 到地址欄並 `set dom.webgpu.enabled to true`。

### 為 Microsoft Edge 設置 GPU

以下是在 Windows 上為 Microsoft Edge 設置高性能 GPU 的步驟：

- **打開設置：** 點擊開始菜單並選擇設置。
- **系統設置：** 進入系統，然後選擇顯示。
- **圖形設置：** 向下滾動並點擊圖形設置。
- **選擇應用：** 在“選擇應用以設置偏好”下，選擇桌面應用，然後點擊瀏覽。
- **選擇 Edge：** 導航到 Edge 安裝文件夾（通常為 `C:\Program Files (x86)\Microsoft\Edge\Application`），然後選擇 `msedge.exe`。
- **設置偏好：** 點擊選項，選擇高性能，然後點擊保存。
這將確保 Microsoft Edge 使用您的高性能 GPU，以提升性能。
- **重啟**您的機器以使這些設置生效。

### 示例：請 [點擊此鏈接](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免責聲明**:  
此文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。如涉及關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。