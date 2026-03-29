# AGENTS.md

## 項目概覽

PhiCookBook 是一個全面的廚房書庫，包含針對微軟 Phi 系列小型語言模型（SLMs）進行操作的實務範例、教學和文件。該庫展示了多種使用案例，包括推理、微調、量化、RAG 實作以及跨不同平台與框架的多模態應用。

**主要技術：**
- **語言：** Python、C#/.NET、JavaScript/Node.js
- **框架：** ONNX Runtime、PyTorch、Transformers、MLX、OpenVINO、Semantic Kernel
- **平台：** Microsoft Foundry、GitHub Models、Hugging Face、Ollama
- **模型類型：** Phi-3、Phi-3.5、Phi-4（文本、視覺、多模態、推理變體）

**倉庫結構：**
- `/code/` - 實作程式碼範例及樣本
- `/md/` - 詳細的文件、教程和操作指南  
- `/translations/` - 多語言翻譯（50 多種語言通過自動化工作流程）
- `/.devcontainer/` - 開發容器配置（Python 3.12 搭配 Ollama）

## 開發環境設定

### 使用 GitHub Codespaces 或 Dev Containers（推薦）

1. 在 GitHub Codespaces 中開啟（最快速）：
   - 點擊 README 中的 "Open in GitHub Codespaces" 徽章
   - 容器自動配置 Python 3.12 和搭載 Phi-3 的 Ollama

2. 在 VS Code Dev Containers 開啟：
   - 使用 README 中的 "Open in Dev Containers" 徽章
   - 容器要求主機至少 16GB 記憶體

### 本地設置

**先決條件：**
- Python 3.12 或更新版本
- .NET 8.0 SDK（用於 C# 範例）
- Node.js 18+ 及 npm（用於 JavaScript 範例）
- 建議最低 16GB RAM

**安裝：**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python 範例：**
進入指定範例目錄並安裝依賴：
```bash
cd code/<example-directory>
pip install -r requirements.txt  # 如果存在 requirements.txt
```

**.NET 範例：**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Web 範例：**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # 啟動開發伺服器
npm run build  # 為生產環境建置
```

## 倉庫組織

### 程式碼範例 (`/code/`)

- **01.Introduce/** - 基本介紹與入門範例
- **03.Finetuning/** 和 **04.Finetuning/** - 使用各種方法的微調範例
- **03.Inference/** - 不同硬體上的推理範例（AIPC、MLX）
- **06.E2E/** - 端到端應用範例
- **07.Lab/** - 實驗室／實驗性實作
- **08.RAG/** - 檢索增強生成範例
- **09.UpdateSamples/** - 最新更新範例

### 文件 (`/md/`)

- **01.Introduction/** - 介紹指南、環境設定、平台指南
- **02.Application/** - 按類型組織的應用範例（文本、程式碼、視覺、音訊等）
- **02.QuickStart/** - Microsoft Foundry 與 GitHub Models 快速入門
- **03.FineTuning/** - 微調文件和教程
- **04.HOL/** - 實務實驗室（包含 .NET 範例）

### 檔案格式

- **Jupyter 筆記本（`.ipynb`）** - 互動式 Python 教程，README 中以 📓 標註
- **Python 腳本（`.py`）** - 獨立 Python 範例
- **C# 專案（`.csproj`、`.sln`）** - .NET 應用與範例
- **JavaScript（`.js`、`package.json`）** - 基於網頁與 Node.js 的範例
- **Markdown（`.md`）** - 文件與指南

## 使用範例

### 執行 Jupyter 筆記本

大多數範例以 Jupyter 筆記本形式提供：
```bash
pip install jupyter notebook
jupyter notebook  # 打開瀏覽器介面
# 導航到所需的 .ipynb 文件
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

或是編譯整個方案：
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### 執行 JavaScript/Web 範例

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # 支援熱重載的開發
```

## 測試

本倉庫包含範例代碼及教程，而非傳統帶有單元測試的軟件項目。驗證通常通過以下方式完成：

1. <strong>執行範例</strong> – 每個範例應無錯誤地運行
2. <strong>核對輸出</strong> – 檢查模型回應是否合適
3. <strong>遵循教程</strong> – 分步指南應照文件正常執行

**常見驗證方式：**
- 在目標環境中測試範例執行
- 驗證依賴安裝正確
- 確認模型下載及加載成功
- 確保預期行為與文件吻合

## 程式碼風格與規範

### 一般準則

- 範例應清晰、良好註解且具教育意義
- 遵循語言特定規範（Python 依照 PEP 8，.NET 遵循 C# 標準）
- 範例聚焦展示特定 Phi 模型能力
- 包含關鍵概念和模型專用參數解說

### 文件標準

**URL 格式：**
- 使用 `[text](../../url)` 格式，避免多餘空格
- 相對連結：當前目錄用 `./`，上層目錄用 `../`
- URL 不包含國家或語言特定地區碼（避免 `/en-us/`、`/en/`）

**圖片：**
- 所有圖片放在 `/imgs/` 目錄
- 使用英文、數字及連字元的描述性名稱
- 範例：`phi-3-architecture.png`

**Markdown 檔案：**
- 參考真實可用的 `/code/` 範例
- 文件保持與程式碼更動同步
- README 中以 📓 表示 Jupyter 筆記本鏈結

### 檔案組織

- `/code/` 中的範例依主題與功能組織
- `/md/` 中文件與範例結構相符（適用時）
- 相關檔案（筆記本、腳本、配置）放於同一子目錄

## 拉取請求指南

### 提交前準備

1. **Fork 本倉庫** 到您的帳號
2. **依類型分開 PR：**
   - Bug 修正一個 PR
   - 文件更新另一個 PR
   - 新範例分開 PR
   - 打字錯誤可合併處理

3. **處理合併衝突：**
   - 變動前先更新本地 `main` 分支
   - 頻繁與上游同步

4. **翻譯 PR：**
   - 必須包含該資料夾所有檔案的翻譯
   - 維持與原語言一致的結構

### 必須通過的檢查

PR 會自動運行 GitHub 工作流程驗證：

1. <strong>相對路徑驗證</strong> - 內部連結必須有效
   - 在 VS Code 中 Ctrl+點擊測試連結
   - 依 VS Code 路徑提示使用 `./` 或 `../`

2. **URL 語系檢查** - 網頁 URL 不得含語系代碼
   - 移除 `/en-us/`、`/en/` 或其他語言碼
   - 使用通用國際化 URL

3. <strong>壞鏈結檢查</strong> - 所有 URL 必須回傳 200 狀態
   - 提交前驗證鏈結可用
   - 注意部分失敗可能因網路限制

### PR 標題範例

```
[component] Brief description
```

範例：
- `[docs] Add Phi-4 inference tutorial`
- `[code] Fix ONNX Runtime integration example`
- `[translation] Add Japanese translation for intro guides`

## 常見開發模式

### 使用 Phi 模型

**模型載入：**
- 範例使用多種框架：Transformers、ONNX Runtime、MLX、OpenVINO
- 模型多從 Hugging Face、Azure 或 GitHub Models 下載
- 確認模型與硬體相容（CPU、GPU、NPU）

**推理模式：**
- 文字生成：大部分範例使用對話/指令型 variant
- 視覺：Phi-3-vision 與 Phi-4-multimodal 用於影像理解
- 聲音：Phi-4-multimodal 支援音訊輸入
- 推理：Phi-4-reasoning 變體用於進階推理任務

### 平台特有說明

**Microsoft Foundry：**
- 需要 Azure 訂閱及 API 金鑰
- 參見 `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models：**
- 免費層可用於測試
- 參見 `/md/02.QuickStart/GitHubModel_QuickStart.md`

**本地推理：**
- ONNX Runtime：跨平台、經過優化的推理
- Ollama：易於本地模型管理（開發容器預設配置）
- Apple MLX：為 Apple Silicon 優化

## 疑難排解

### 常見問題

**記憶體問題：**
- Phi 模型尤其是視覺／多模態版需大量 RAM
- 資源有限時可用量化模型
- 參見 `/md/01.Introduction/04/QuantifyingPhi.md`

**依賴衝突：**
- Python 範例可能有特定版本限制
- 每個範例使用虛擬環境
- 查看各自的 `requirements.txt`

**模型下載失敗：**
- 大型模型慢速網路時易超時
- 建議使用雲端環境（Codespaces、Azure）
- 檢查 Hugging Face 緩存：`~/.cache/huggingface/`

**.NET 專案問題：**
- 確保安裝 .NET 8.0 SDK
- 編譯前執行 `dotnet restore`
- 部分專案有 CUDA 專用配置（Debug_Cuda）

**JavaScript/Web 範例：**
- 使用 Node.js 18+ 確保兼容性
- 遇問題刪除 `node_modules` 重新安裝
- 偵錯時查看瀏覽器控制臺 WebGPU 相關信息

### 尋求協助

- **Discord：** 加入 Microsoft Foundry 社群 Discord
- **GitHub Issues：** 報告錯誤和問題
- **GitHub Discussions：** 問問題與分享知識

## 附加說明

### 負責任的 AI

所有 Phi 模型使用應遵循微軟負責任 AI 原則：
- 公平性、可靠性、安全
- 隱私與安全  
- 包容性、透明度、問責制
- 生產應用使用 Azure AI Content Safety
- 參見 `/md/01.Introduction/01/01.AISafety.md`

### 翻譯

- 支援 50 多種語言，通過自動化 GitHub Action
- 翻譯檔案位於 `/translations/` 目錄
- 由 co-op-translator 工作流程維護
- 禁止手動編輯翻譯檔（自動生成）

### 貢獻

- 遵循 `CONTRIBUTING.md` 指南
- 同意 Contributor License Agreement (CLA)
- 遵守微軟開源行為守則
- 保持安全與憑證不入提交

### 多語言支援

本倉庫為多語言範例庫，包含：
- **Python** - ML/AI 工作流程、Jupyter 筆記本、微調
- **C#/.NET** - 企業應用、ONNX Runtime 集成
- **JavaScript** - 網頁 AI、透過 WebGPU 進行瀏覽器端推理

請選擇最適合您用途與部署目標的語言。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->