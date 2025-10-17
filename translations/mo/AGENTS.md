<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T10:49:02+00:00",
  "source_file": "AGENTS.md",
  "language_code": "mo"
}
-->
# AGENTS.md

## 專案概述

PhiCookBook 是一個全面的食譜資源庫，包含了使用 Microsoft Phi 系列小型語言模型 (SLMs) 的實作範例、教程和文件。此資源庫展示了多種使用案例，包括推論、微調、量化、RAG 實作以及跨不同平台和框架的多模態應用。

**主要技術：**
- **語言：** Python、C#/.NET、JavaScript/Node.js
- **框架：** ONNX Runtime、PyTorch、Transformers、MLX、OpenVINO、Semantic Kernel
- **平台：** Azure AI Foundry、GitHub Models、Hugging Face、Ollama
- **模型類型：** Phi-3、Phi-3.5、Phi-4（文本、視覺、多模態、推理變體）

**資源庫結構：**
- `/code/` - 工作代碼範例和樣本實作
- `/md/` - 詳細文件、教程和操作指南  
- `/translations/` - 多語言翻譯（透過自動化工作流程支持 50+ 種語言）
- `/.devcontainer/` - 開發容器配置（Python 3.12 搭配 Ollama）

## 開發環境設置

### 使用 GitHub Codespaces 或開發容器（推薦）

1. 在 GitHub Codespaces 中開啟（最快速）：
   - 點擊 README 中的 "Open in GitHub Codespaces" 徽章
   - 容器會自動配置 Python 3.12 和搭載 Phi-3 的 Ollama

2. 在 VS Code 開發容器中開啟：
   - 使用 README 中的 "Open in Dev Containers" 徽章
   - 容器需要至少 16GB 主機記憶體

### 本地設置

**先決條件：**
- Python 3.12 或更新版本
- .NET 8.0 SDK（用於 C# 範例）
- Node.js 18+ 和 npm（用於 JavaScript 範例）
- 建議至少 16GB RAM

**安裝：**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**針對 Python 範例：**
進入特定範例目錄並安裝依賴：
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**針對 .NET 範例：**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**針對 JavaScript/網頁範例：**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## 資源庫組織

### 代碼範例 (`/code/`)

- **01.Introduce/** - 基本介紹和入門範例
- **03.Finetuning/** 和 **04.Finetuning/** - 使用多種方法進行微調的範例
- **03.Inference/** - 在不同硬體（AIPC、MLX）上的推論範例
- **06.E2E/** - 端到端應用範例
- **07.Lab/** - 實驗室/試驗性實作
- **08.RAG/** - 檢索增強生成範例
- **09.UpdateSamples/** - 最新更新的範例

### 文件 (`/md/`)

- **01.Introduction/** - 入門指南、環境設置、平台指南
- **02.Application/** - 按類型組織的應用範例（文本、代碼、視覺、音頻等）
- **02.QuickStart/** - Azure AI Foundry 和 GitHub Models 的快速入門指南
- **03.FineTuning/** - 微調文件和教程
- **04.HOL/** - 實作實驗室（包含 .NET 範例）

### 文件格式

- **Jupyter 筆記本 (`.ipynb`)** - README 中標記為 📓 的互動式 Python 教程
- **Python 腳本 (`.py`)** - 獨立的 Python 範例
- **C# 專案 (`.csproj`, `.sln`)** - .NET 應用和範例
- **JavaScript (`.js`, `package.json`)** - 基於網頁和 Node.js 的範例
- **Markdown (`.md`)** - 文件和指南

## 使用範例

### 執行 Jupyter 筆記本

大多數範例以 Jupyter 筆記本形式提供：
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### 執行 Python 腳本

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### 執行 .NET 範例

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

或建置整個解決方案：
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### 執行 JavaScript/網頁範例

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## 測試

此資源庫包含範例代碼和教程，而非傳統的軟體專案單元測試。驗證通常通過以下方式進行：

1. **執行範例** - 每個範例應無錯誤地執行
2. **驗證輸出** - 確認模型回應是否合適
3. **遵循教程** - 按步驟操作指南應如文件所述正常運作

**常見驗證方法：**
- 在目標環境中測試範例執行
- 驗證依賴是否正確安裝
- 確認模型成功下載/加載
- 確保預期行為與文件一致

## 代碼風格和規範

### 一般指南

- 範例應清晰、註解充分且具教育性
- 遵循語言特定的規範（Python 遵循 PEP 8，.NET 遵循 C# 標準）
- 範例應專注於展示特定 Phi 模型的功能
- 包含註解以解釋關鍵概念和模型特定參數

### 文件標準

**URL 格式：**
- 使用 `[文字](../../url)` 格式，避免多餘空格
- 相對連結：使用 `./` 表示當前目錄，`../` 表示父目錄
- 網址中避免使用國家/地區特定語言代碼（避免 `/en-us/`、`/en/`）

**圖片：**
- 所有圖片存放於 `/imgs/` 目錄
- 使用描述性名稱，包含英文字符、數字和連字號
- 範例：`phi-3-architecture.png`

**Markdown 文件：**
- 參考 `/code/` 目錄中的實際工作範例
- 確保文件與代碼變更同步
- 在 README 中使用 📓 表示 Jupyter 筆記本連結

### 文件組織

- `/code/` 中的代碼範例按主題/功能組織
- `/md/` 中的文件在適用時與代碼結構保持一致
- 將相關文件（筆記本、腳本、配置）集中存放於子目錄

## 拉取請求指南

### 提交前

1. **Fork 資源庫** 到您的帳戶
2. **按類型分開 PR：**
   - Bug 修復放在一個 PR
   - 文件更新放在另一個 PR
   - 新範例放在單獨的 PR
   - 拼寫錯誤修正可以合併

3. **處理合併衝突：**
   - 在進行更改前更新本地 `main` 分支
   - 經常與上游同步

4. **翻譯 PR：**
   - 必須包含文件夾中所有文件的翻譯
   - 結構需與原始語言一致

### 必要檢查

PR 會自動運行 GitHub 工作流程以驗證：

1. **相對路徑驗證** - 所有內部連結必須有效
   - 在本地測試連結：在 VS Code 中按 Ctrl+Click
   - 使用 VS Code 提供的路徑建議（`./` 或 `../`）

2. **URL 語言代碼檢查** - 網址中不得包含國家/地區語言代碼
   - 移除 `/en-us/`、`/en/` 或其他語言代碼
   - 使用通用的國際網址

3. **無效網址檢查** - 所有網址必須返回 200 狀態碼
   - 提交前確認連結可正常訪問
   - 注意：某些失敗可能由網絡限制引起

### PR 標題格式

```
[component] Brief description
```

範例：
- `[docs] 新增 Phi-4 推論教程`
- `[code] 修復 ONNX Runtime 整合範例`
- `[translation] 新增入門指南的日文翻譯`

## 常見開發模式

### 使用 Phi 模型

**模型加載：**
- 範例使用多種框架：Transformers、ONNX Runtime、MLX、OpenVINO
- 模型通常從 Hugging Face、Azure 或 GitHub Models 下載
- 確認模型與您的硬體（CPU、GPU、NPU）兼容

**推論模式：**
- 文本生成：大多數範例使用聊天/指令變體
- 視覺：Phi-3-vision 和 Phi-4-multimodal 用於圖像理解
- 音頻：Phi-4-multimodal 支持音頻輸入
- 推理：Phi-4-reasoning 變體用於高級推理任務

### 平台特定注意事項

**Azure AI Foundry：**
- 需要 Azure 訂閱和 API 金鑰
- 請參閱 `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models：**
- 免費層可用於測試
- 請參閱 `/md/02.QuickStart/GitHubModel_QuickStart.md`

**本地推論：**
- ONNX Runtime：跨平台，優化推論
- Ollama：簡易本地模型管理（開發容器中已預配置）
- Apple MLX：針對 Apple Silicon 優化

## 疑難排解

### 常見問題

**記憶體問題：**
- Phi 模型需要大量 RAM（尤其是視覺/多模態變體）
- 在資源有限的環境中使用量化模型
- 請參閱 `/md/01.Introduction/04/QuantifyingPhi.md`

**依賴衝突：**
- Python 範例可能有特定版本要求
- 為每個範例使用虛擬環境
- 檢查個別 `requirements.txt` 文件

**模型下載失敗：**
- 大型模型可能在慢速連接上超時
- 考慮使用雲環境（Codespaces、Azure）
- 檢查 Hugging Face 快取：`~/.cache/huggingface/`

**.NET 專案問題：**
- 確保已安裝 .NET 8.0 SDK
- 在建置前使用 `dotnet restore`
- 某些專案有 CUDA 特定配置（Debug_Cuda）

**JavaScript/網頁範例：**
- 使用 Node.js 18+ 以確保兼容性
- 清除 `node_modules` 並重新安裝以解決問題
- 檢查瀏覽器控制台的 WebGPU 兼容性問題

### 尋求幫助

- **Discord：** 加入 Azure AI Foundry 社群 Discord
- **GitHub Issues：** 在資源庫中回報錯誤和問題
- **GitHub Discussions：** 提問並分享知識

## 其他背景資訊

### 負責任的人工智慧

所有 Phi 模型的使用應遵循 Microsoft 的負責任 AI 原則：
- 公平性、可靠性、安全性
- 隱私和安全性  
- 包容性、透明度、問責性
- 生產應用中使用 Azure AI Content Safety
- 請參閱 `/md/01.Introduction/01/01.AISafety.md`

### 翻譯

- 透過自動化 GitHub Action 支持 50+ 種語言
- 翻譯存放於 `/translations/` 目錄
- 由 co-op-translator 工作流程維護
- 請勿手動編輯翻譯文件（自動生成）

### 貢獻

- 遵循 `CONTRIBUTING.md` 中的指南
- 同意貢獻者許可協議（CLA）
- 遵守 Microsoft 開源行為準則
- 確保提交中不包含安全性問題或憑證

### 多語言支持

這是一個多語言資源庫，包含以下語言的範例：
- **Python** - 機器學習/人工智慧工作流、Jupyter 筆記本、微調
- **C#/.NET** - 企業應用、ONNX Runtime 整合
- **JavaScript** - 基於網頁的人工智慧、使用 WebGPU 的瀏覽器推論

請選擇最適合您的使用案例和部署目標的語言。

---

**免責聲明**：  
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。