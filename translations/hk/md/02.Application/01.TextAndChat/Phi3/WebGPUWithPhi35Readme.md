<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-08T05:43:03+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "hk"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## 展示 WebGPU 同 RAG 模式嘅示範

RAG 模式用 Phi-3.5 Onnx Hosted model，結合 Retrieval-Augmented Generation 方法，將 Phi-3.5 模型同 ONNX hosting 嘅優勢整合，令 AI 部署更高效。呢個模式對於針對特定領域嘅任務做微調好有用，兼顧質素、成本效益同長文本理解能力。佢係 Azure AI 嘅一部分，提供多款易搵、易試、易用嘅模型，滿足唔同行業嘅定制需求。

## 乜嘢係 WebGPU  
WebGPU 係一個現代網頁圖形 API，設計用嚟直接由瀏覽器高效地存取裝置嘅 GPU。佢係 WebGL 嘅後繼者，帶嚟幾個主要改進：

1. **兼容現代 GPU**：WebGPU 可以無縫配合最新嘅 GPU 架構，利用 Vulkan、Metal 同 Direct3D 12 等系統 API。
2. **提升效能**：支援通用 GPU 運算同更快嘅操作，適合圖形渲染同機器學習任務。
3. **先進功能**：WebGPU 提供更高級嘅 GPU 能力，令圖形同計算工作負載更複雜同動態。
4. **減輕 JavaScript 負擔**：將更多任務交俾 GPU 處理，令 JavaScript 工作量大幅減少，提升效能同流暢度。

而家 WebGPU 已經支援 Google Chrome，仲有繼續開發擴展到其他平台。

### 03.WebGPU  
所需環境：

**支援瀏覽器：**  
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
喺頁面頂部嘅搜尋框輸入 'enable-unsafe-webgpu'

#### 啟用標誌：  
喺結果中搵到 #enable-unsafe-webgpu 標誌。

喺旁邊嘅下拉選單揀選 Enabled。

#### 重啟瀏覽器：

啟用標誌後，需要重啟瀏覽器先會生效。點擊頁面底部出現嘅 Relaunch 按鈕。

- Linux 用戶啟動瀏覽器時加上 `--enable-features=Vulkan`。  
- Safari 18 (macOS 15) 預設已啟用 WebGPU。  
- Firefox Nightly 喺地址欄輸入 about:config，然後 `set dom.webgpu.enabled to true`。

### 為 Microsoft Edge 設定 GPU

以下係喺 Windows 上為 Microsoft Edge 設定高效能 GPU 嘅步驟：

- **打開設定：** 點擊開始功能表，揀 Settings。  
- **系統設定：** 去 System，然後揀 Display。  
- **圖形設定：** 向下捲動，點擊 Graphics settings。  
- **揀選應用程式：** 喺 “Choose an app to set preference” 底下，揀 Desktop app，跟住 Browse。  
- **揀選 Edge：** 尋找 Edge 安裝資料夾（通常係 `C:\Program Files (x86)\Microsoft\Edge\Application`），揀 `msedge.exe`。  
- **設定偏好：** 點 Options，揀 High performance，然後儲存。  
咁樣可以確保 Microsoft Edge 使用你嘅高效能 GPU，提升表現。  
- **重啟** 電腦令設定生效。

### 範例：請[點擊呢個連結](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我哋努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我哋對因使用本翻譯而引起嘅任何誤解或誤釋概不負責。