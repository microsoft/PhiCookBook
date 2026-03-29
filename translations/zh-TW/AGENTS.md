# AGENTS.md

## 專案概述

PhiCookBook 是一個綜合性的食譜存放庫，包含針對 Microsoft Phi 系列小型語言模型（SLMs）的實作範例、教學與文件。此存放庫展示多種使用案例，涵蓋推論、微調、量化、RAG 實作，以及跨不同平台和框架的多模態應用。

**主要技術：**
- **語言：** Python、C#/.NET、JavaScript/Node.js
- **框架：** ONNX Runtime、PyTorch、Transformers、MLX、OpenVINO、Semantic Kernel
- **平台：** Microsoft Foundry、GitHub Models、Hugging Face、Ollama
- **模型類型：** Phi-3、Phi-3.5、Phi-4（文本、視覺、多模態、推理變種）

**存放庫結構：**
- `/code/` - 可操作的程式碼範例與示範實作
- `/md/` - 詳細文件、教學與操作指南  
- `/translations/` - 多語言翻譯（超過50種語言透過自動化工作流程）
- `/.devcontainer/` - 開發容器配置（Python 3.12 與 Ollama）

## 開發環境設定

### 使用 GitHub Codespaces 或 Dev Containers（建議）

1. 在 GitHub Codespaces 開啟（最快速）：
   - 點擊 README 中的「Open in GitHub Codespaces」徽章
   - 容器會自動預設配置 Python 3.12 與搭載 Phi-3 的 Ollama

2. 在 VS Code Dev Containers 開啟：
   - 使用 README 中的「Open in Dev Containers」徽章
   - 容器最低需求主機記憶體為16GB

### 本機設定

**前置需求：**
- Python 3.12 或更新版本
- .NET 8.0 SDK（用於 C# 範例）
- Node.js 18+ 與 npm（用於 JavaScript 範例）
- 建議記憶體至少16GB

**安裝步驟：**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python 範例：**
進入特定範例目錄並安裝相依套件：
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

**JavaScript/網頁範例：**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # 啟動開發伺服器
npm run build  # 建構生產版本
```

## 存放庫組織

### 程式碼範例（`/code/`）

- **01.Introduce/** - 基本入門與初學範例
- **03.Finetuning/** 及 **04.Finetuning/** - 各式微調範例
- **03.Inference/** - 於不同硬體（AIPC、MLX）執行推論範例
- **06.E2E/** - 端到端應用範例
- **07.Lab/** - 實驗室/試驗性實作
- **08.RAG/** - 檢索增強生成範例
- **09.UpdateSamples/** - 最新更新範例

### 文件資料（`/md/`）

- **01.Introduction/** - 入門指引、環境設定、平台導覽
- **02.Application/** - 依類型組織的應用範例（文本、程式碼、視覺、音訊等）
- **02.QuickStart/** - Microsoft Foundry 與 GitHub Models 快速入門指南
- **03.FineTuning/** - 微調相關文件與教學
- **04.HOL/** - 實作實驗室（含 .NET 範例）

### 檔案格式

- **Jupyter 筆記本（`.ipynb`）** - 互動式 Python 教學，README 中以 📓 標記
- **Python 腳本（`.py`）** - 獨立 Python 範例
- **C# 專案（`.csproj`, `.sln`）** - .NET 應用與範例
- **JavaScript（`.js`, `package.json`）** - 網頁與 Node.js 範例
- **Markdown（`.md`）** - 文件與教學指南

## 使用範例

### 執行 Jupyter 筆記本

大部分範例均為 Jupyter 筆記本形式：
```bash
pip install jupyter notebook
jupyter notebook  # 開啟瀏覽器介面
# 導航至目標 .ipynb 檔案
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
npm run dev  # 開發中使用熱重載
```

## 測試

本存放庫提供的是範例程式碼與教學，而非傳統軟體專案單元測試。驗證通常透過：

1. <strong>執行範例程式</strong> - 各範例應無錯誤執行完成
2. <strong>確認輸出</strong> - 檢查模型回應是否正確合理
3. <strong>跟隨教學</strong> - 教學步驟順利並達成預期結果

**常見驗證方式：**
- 在目標環境測試範例執行
- 確認套件正確安裝
- 驗證模型能下載/載入成功
- 確保行為符合文件說明

## 程式碼風格與慣例

### 一般指引

- 範例應清晰、詳盡註解且具教育性
- 遵循語言特定慣例（Python 遵循 PEP 8，.NET 遵循 C# 標準）
- 範例重點展示特定 Phi 模型功能
- 包含解說註解說明重要概念與模型參數

### 文件標準

**URL 格式：**
- 使用 `[text](../../url)` 格式，避免多餘空白
- 相對連結：當前目錄用 `./`，父目錄用 `../`
- URL 不含國家特定區域設定（避免 `/en-us/`、`/en/`）

**圖片：**
- 所有圖片皆放置於 `/imgs/` 目錄
- 檔名採用英文半形字元、數字及連字號命名
- 例：`phi-3-architecture.png`

**Markdown 檔案：**
- 指向 `/code/` 目錄中實際有效的範例
- 文件需與程式碼版本保持同步
- README 中以 📓 emoji 標示 Jupyter 筆記本連結

### 檔案組織

- 程式碼範例依主題功能分類置於 `/code/`
- 文件資料於 `/md/` 目錄結構對應程式碼時，同步排列
- 將相關的筆記本、腳本、設定文件集中於子目錄

## Pull Request 指南

### 提交之前

1. **Fork 存放庫** 至個人帳號
2. **PR 按類型分開：**
   - 錯誤修正一個 PR
   - 文件更新另一個 PR
   - 新範例獨立 PR
   - 拼字錯誤修正可合併提交

3. **處理合併衝突：**
   - 在修改前先更新本機 `main` 分支
   - 經常與 upstream 同步

4. **翻譯 PR：**
   - 必須包含該資料夾所有檔案的翻譯
   - 保持與原始語言結構一致

### 必要檢查

PR 會自動執行 GitHub 工作流程驗證：

1. <strong>相對路徑驗證</strong> - 所有內部連結皆須可用
   - 本機測試連結：VS Code 按 Ctrl+點擊
   - 使用 VS Code 提示的路徑（`./` 或 `../`）

2. **URL 區域檢查** - 網頁 URL 不得含國家區域碼
   - 移除 `/en-us/`、`/en/` 或其他語言代碼
   - 使用通用國際 URL

3. **破損 URL 檢查** - 所有 URL 回傳必須為 200 狀態
   - 提交前確認連結可用
   - 注意：部分失敗可能因網路限制所致

### PR 標題格式

```
[component] Brief description
```

範例：
- `[docs] 添加 Phi-4 推論教學`
- `[code] 修正 ONNX Runtime 整合範例`
- `[translation] 添加日文入門導覽翻譯`

## 常用開發模式

### Phi 模型操作

**模型載入：**
- 範例使用多種框架：Transformers、ONNX Runtime、MLX、OpenVINO
- 模型多由 Hugging Face、Azure 或 GitHub Models 下載
- 請確認模型與硬體相容（CPU、GPU、NPU）

**推論模式：**
- 文字生成：多數使用聊天/指令版本
- 視覺：Phi-3-vision 與 Phi-4-multimodal 用於影像理解
- 音訊：Phi-4-multimodal 支援音訊輸入
- 推理：Phi-4-reasoning 變種用於進階推理任務

### 平台特定說明

**Microsoft Foundry：**
- 需 Azure 訂閱與 API 金鑰
- 參見 `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models：**
- 免費方案可用於測試
- 參見 `/md/02.QuickStart/GitHubModel_QuickStart.md`

**本地推論：**
- ONNX Runtime：跨平台，優化推論
- Ollama：簡易本地模型管理（開發容器已預設配置）
- Apple MLX：針對 Apple Silicon 最佳化

## 疑難排解

### 常見問題

**記憶體問題：**
- Phi 模型尤其視覺/多模態版本需大量 RAM
- 資源受限環境建議使用量化模型
- 參見 `/md/01.Introduction/04/QuantifyingPhi.md`

**相依性衝突：**
- Python 範例對版本有特定要求
- 建議各範例使用虛擬環境
- 檢查個別 `requirements.txt`

**模型下載失敗：**
- 大型模型於慢速連線可能逾時
- 可考慮使用雲端環境（Codespaces、Azure）
- 檢查 Hugging Face 快取位置：`~/.cache/huggingface/`

**.NET 專案問題：**
- 確保已安裝 .NET 8.0 SDK
- 建置前執行 `dotnet restore`
- 部分專案含 CUDA 特定設定（Debug_Cuda）

**JavaScript/網頁範例：**
- 請使用 Node.js 18+ 版以確保相容性
- 須清除 `node_modules` 並重裝依賴以解決問題
- 檢視瀏覽器主控台是否有 WebGPU 相容性錯誤

### 尋求幫助

- **Discord：** 加入 Microsoft Foundry 社群 Discord
- **GitHub Issues：** 回報錯誤與問題
- **GitHub Discussions：** 提問與分享知識

## 其他背景資訊

### 負責任的 AI

使用所有 Phi 模型應遵守 Microsoft 的負責任 AI 原則：
- 公平性、可靠性、安全性
- 隱私與資安  
- 包容性、透明度、問責制
- 正式應用請使用 Azure AI Content Safety
- 參見 `/md/01.Introduction/01/01.AISafety.md`

### 翻譯資訊

- 支援超過50種語言，透過自動化 GitHub Action
- 翻譯檔置於 `/translations/` 目錄
- 由協同翻譯工作流程維護
- 請勿手動編輯翻譯檔（自動生成）

### 貢獻指南

- 遵守 `CONTRIBUTING.md` 中指導原則
- 同意貢獻者授權協議（CLA）
- 遵守 Microsoft 開源行為準則
- 請勿將安全憑證納入提交紀錄

### 多語言支援

此存放庫為多語言範例庫，包括：
- **Python** - 機器學習/人工智慧工作流程、Jupyter 筆記本、微調
- **C#/.NET** - 企業應用、ONNX Runtime 整合
- **JavaScript** - 網頁 AI、瀏覽器 WebGPU 推論

請依需求與部署目標選擇最適用的語言。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於準確性，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人員進行人工翻譯。因使用本翻譯所引起的任何誤解或錯誤詮釋，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->