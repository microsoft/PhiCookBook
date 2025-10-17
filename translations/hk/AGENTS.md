<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T10:49:25+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hk"
}
-->
# AGENTS.md

## 項目概覽

PhiCookBook 是一個全面的食譜資源庫，包含了實際操作範例、教程以及使用 Microsoft 的 Phi 系列小型語言模型（SLMs）的文檔。該資源庫展示了多種使用案例，包括推理、微調、量化、RAG 實現以及跨不同平台和框架的多模態應用。

**主要技術：**
- **語言：** Python、C#/.NET、JavaScript/Node.js
- **框架：** ONNX Runtime、PyTorch、Transformers、MLX、OpenVINO、Semantic Kernel
- **平台：** Azure AI Foundry、GitHub Models、Hugging Face、Ollama
- **模型類型：** Phi-3、Phi-3.5、Phi-4（文本、視覺、多模態、推理變體）

**資源庫結構：**
- `/code/` - 工作代碼範例和樣本實現
- `/md/` - 詳細文檔、教程和操作指南  
- `/translations/` - 多語言翻譯（通過自動化工作流程支持50多種語言）
- `/.devcontainer/` - 開發容器配置（Python 3.12，配備 Ollama）

## 開發環境設置

### 使用 GitHub Codespaces 或開發容器（推薦）

1. 在 GitHub Codespaces 中打開（最快速）：
   - 點擊 README 中的 "Open in GitHub Codespaces" 徽章
   - 容器自動配置為 Python 3.12 和 Ollama，配備 Phi-3

2. 在 VS Code 開發容器中打開：
   - 使用 README 中的 "Open in Dev Containers" 徽章
   - 容器需要至少 16GB 主機內存

### 本地設置

**先決條件：**
- Python 3.12 或更高版本
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

**針對 JavaScript/Web 範例：**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## 資源庫組織結構

### 代碼範例 (`/code/`)

- **01.Introduce/** - 基本介紹和入門範例
- **03.Finetuning/** 和 **04.Finetuning/** - 使用各種方法進行微調的範例
- **03.Inference/** - 在不同硬件（AIPC、MLX）上的推理範例
- **06.E2E/** - 端到端應用範例
- **07.Lab/** - 實驗室/試驗性實現
- **08.RAG/** - 檢索增強生成範例
- **09.UpdateSamples/** - 最新更新的範例

### 文檔 (`/md/`)

- **01.Introduction/** - 入門指南、環境設置、平台指南
- **02.Application/** - 按類型組織的應用範例（文本、代碼、視覺、音頻等）
- **02.QuickStart/** - Azure AI Foundry 和 GitHub Models 的快速入門指南
- **03.FineTuning/** - 微調文檔和教程
- **04.HOL/** - 實操實驗室（包括 .NET 範例）

### 文件格式

- **Jupyter Notebooks (`.ipynb`)** - README 中標記為 📓 的互動式 Python 教程
- **Python Scripts (`.py`)** - 獨立的 Python 範例
- **C# Projects (`.csproj`, `.sln`)** - .NET 應用和範例
- **JavaScript (`.js`, `package.json`)** - 基於 Web 和 Node.js 的範例
- **Markdown (`.md`)** - 文檔和指南

## 使用範例

### 運行 Jupyter Notebooks

大多數範例以 Jupyter notebooks 提供：
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### 運行 Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### 運行 .NET 範例

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

或者構建整個解決方案：
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### 運行 JavaScript/Web 範例

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## 測試

此資源庫包含範例代碼和教程，而非傳統的軟件項目單元測試。驗證通常通過以下方式進行：

1. **運行範例** - 每個範例應無錯誤執行
2. **驗證輸出** - 檢查模型響應是否合適
3. **遵循教程** - 按步驟操作指南應如文檔所述工作

**常見驗證方法：**
- 在目標環境中測試範例執行
- 驗證依賴項是否正確安裝
- 檢查模型是否成功下載/加載
- 確認預期行為與文檔一致

## 代碼風格和約定

### 一般指南

- 範例應清晰、注釋充分且具有教育性
- 遵循特定語言的約定（Python 遵循 PEP 8，.NET 遵循 C# 標準）
- 保持範例專注於展示特定 Phi 模型功能
- 包括解釋關鍵概念和模型特定參數的注釋

### 文檔標準

**URL 格式：**
- 使用 `[text](../../url)` 格式，無額外空格
- 相對鏈接：使用 `./` 表示當前目錄，`../` 表示父目錄
- 網址中避免使用國家/地區特定的語言代碼（避免 `/en-us/`、`/en/`）

**圖片：**
- 所有圖片存儲在 `/imgs/` 目錄中
- 使用描述性名稱，包含英文字符、數字和連字符
- 範例：`phi-3-architecture.png`

**Markdown 文件：**
- 參考 `/code/` 目錄中的實際工作範例
- 保持文檔與代碼變更同步
- 在 README 中使用 📓 表示 Jupyter notebook 的鏈接

### 文件組織

- `/code/` 中的代碼範例按主題/功能組織
- `/md/` 中的文檔在適用時與代碼結構保持一致
- 將相關文件（notebooks、scripts、configs）集中在子目錄中

## Pull Request 指南

### 提交前

1. **Fork 資源庫** 到您的帳戶
2. **按類型分開 PR：**
   - Bug 修復放在一個 PR
   - 文檔更新放在另一個 PR
   - 新範例放在單獨的 PR
   - 拼寫錯誤修正可以合併

3. **處理合併衝突：**
   - 在進行更改前更新本地 `main` 分支
   - 經常與上游同步

4. **翻譯 PR：**
   - 必須包括文件夾中所有文件的翻譯
   - 保持與原始語言一致的結構

### 必需檢查

PR 會自動運行 GitHub 工作流程以驗證：

1. **相對路徑驗證** - 所有內部鏈接必須有效
   - 在本地測試鏈接：在 VS Code 中按 Ctrl+Click
   - 使用 VS Code 的路徑建議（`./` 或 `../`）

2. **URL 語言代碼檢查** - 網址中不得包含國家/地區語言代碼
   - 移除 `/en-us/`、`/en/` 或其他語言代碼
   - 使用通用國際網址

3. **URL 錯誤檢查** - 所有網址必須返回 200 狀態
   - 在提交前驗證鏈接是否可訪問
   - 注意：某些失敗可能由於網絡限制

### PR 標題格式

```
[component] Brief description
```

範例：
- `[docs] 添加 Phi-4 推理教程`
- `[code] 修復 ONNX Runtime 集成範例`
- `[translation] 添加日語翻譯的入門指南`

## 常見開發模式

### 使用 Phi 模型

**模型加載：**
- 範例使用多種框架：Transformers、ONNX Runtime、MLX、OpenVINO
- 模型通常從 Hugging Face、Azure 或 GitHub Models 下載
- 檢查模型是否與您的硬件（CPU、GPU、NPU）兼容

**推理模式：**
- 文本生成：大多數範例使用聊天/指令變體
- 視覺：Phi-3-vision 和 Phi-4-multimodal 用於圖像理解
- 音頻：Phi-4-multimodal 支持音頻輸入
- 推理：Phi-4-reasoning 變體用於高級推理任務

### 平台特定注意事項

**Azure AI Foundry：**
- 需要 Azure 訂閱和 API 密鑰
- 請參閱 `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models：**
- 免費層可用於測試
- 請參閱 `/md/02.QuickStart/GitHubModel_QuickStart.md`

**本地推理：**
- ONNX Runtime：跨平台，優化推理
- Ollama：簡易本地模型管理（在開發容器中預配置）
- Apple MLX：針對 Apple Silicon 優化

## 故障排除

### 常見問題

**內存問題：**
- Phi 模型需要大量 RAM（特別是視覺/多模態變體）
- 在資源有限的環境中使用量化模型
- 請參閱 `/md/01.Introduction/04/QuantifyingPhi.md`

**依賴衝突：**
- Python 範例可能有特定版本要求
- 為每個範例使用虛擬環境
- 檢查各自的 `requirements.txt` 文件

**模型下載失敗：**
- 大型模型可能在慢速連接上超時
- 考慮使用雲環境（Codespaces、Azure）
- 檢查 Hugging Face 緩存：`~/.cache/huggingface/`

**.NET 項目問題：**
- 確保已安裝 .NET 8.0 SDK
- 在構建前使用 `dotnet restore`
- 某些項目有 CUDA 特定配置（Debug_Cuda）

**JavaScript/Web 範例：**
- 使用 Node.js 18+ 以確保兼容性
- 清除 `node_modules` 並重新安裝以解決問題
- 檢查瀏覽器控制台的 WebGPU 兼容性問題

### 獲取幫助

- **Discord：** 加入 Azure AI Foundry 社區 Discord
- **GitHub Issues：** 在資源庫中報告錯誤和問題
- **GitHub Discussions：** 提問並分享知識

## 附加背景

### 負責任的人工智能

所有 Phi 模型的使用應遵循 Microsoft 的負責任人工智能原則：
- 公平性、可靠性、安全性
- 隱私和安全  
- 包容性、透明度、問責性
- 在生產應用中使用 Azure AI Content Safety
- 請參閱 `/md/01.Introduction/01/01.AISafety.md`

### 翻譯

- 通過自動化 GitHub Action 支持 50 多種語言
- 翻譯存儲在 `/translations/` 目錄中
- 由 co-op-translator 工作流程維護
- 不要手動編輯翻譯文件（自動生成）

### 貢獻

- 遵循 `CONTRIBUTING.md` 中的指南
- 同意貢獻者許可協議（CLA）
- 遵守 Microsoft 開源行為準則
- 不要在提交中包含安全性和憑證

### 多語言支持

這是一個多語言資源庫，範例包括：
- **Python** - 機器學習/人工智能工作流、Jupyter notebooks、微調
- **C#/.NET** - 企業應用、ONNX Runtime 集成
- **JavaScript** - 基於 Web 的人工智能、瀏覽器推理（WebGPU）

選擇最適合您的使用案例和部署目標的語言。

---

**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。