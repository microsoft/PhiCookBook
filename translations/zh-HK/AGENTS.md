# AGENTS.md

## Project Overview

PhiCookBook 是一個全面的食譜庫，包含了 Microsoft Phi 系列小語言模型（SLMs）的實作範例、教學及文件。此庫展示了包括推論、微調、量化、RAG 實現及多模態應用於不同平台與框架的多種使用案例。

**關鍵技術：**
- **語言:** Python、C#/.NET、JavaScript/Node.js
- **框架:** ONNX Runtime、PyTorch、Transformers、MLX、OpenVINO、Semantic Kernel
- **平台:** Microsoft Foundry、GitHub Models、Hugging Face、Ollama
- **模型類型:** Phi-3、Phi-3.5、Phi-4（文字、視覺、多模態、推理變體）

**倉庫結構：**
- `/code/` - 工作代碼範例與示範實作
- `/md/` - 詳細文件、教學及操作指南  
- `/translations/` - 多語言翻譯（通過自動化工作流程支持超過50種語言）
- `/.devcontainer/` - 開發容器設定（含 Python 3.12 與 Ollama）

## Development Environment Setup

### Using GitHub Codespaces or Dev Containers (Recommended)

1. Open in GitHub Codespaces (fastest):
   - Click the "Open in GitHub Codespaces" badge in README
   - Container auto-configures with Python 3.12 and Ollama with Phi-3

2. Open in VS Code Dev Containers:
   - Use the "Open in Dev Containers" badge from README
   - Container requires 16GB host memory minimum

### Local Setup

**Prerequisites:**
- Python 3.12 or later
- .NET 8.0 SDK (for C# examples)
- Node.js 18+ and npm (for JavaScript examples)
- 16GB RAM minimum recommended

**Installation:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**For Python Examples:**
Navigate to specific example directories and install dependencies:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # 如果 requirements.txt 存在
```

**For .NET Examples:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**For JavaScript/Web Examples:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # 啟動開發伺服器
npm run build  # 建立生產版本
```

## Repository Organization

### Code Examples (`/code/`)

- **01.Introduce/** - 基本介紹與入門範例
- **03.Finetuning/** 和 **04.Finetuning/** - 多種方法的微調範例
- **03.Inference/** - 在不同硬體（AIPC、MLX）上的推論範例
- **06.E2E/** - 端到端應用範例
- **07.Lab/** - 實驗室/實驗性實作
- **08.RAG/** - 檢索增強生成範例
- **09.UpdateSamples/** - 最新更新範例

### Documentation (`/md/`)

- **01.Introduction/** - 介紹指南、環境設置、平台指南
- **02.Application/** - 按應用類型組織的實作範例（文字、代碼、視覺、音頻等）
- **02.QuickStart/** - Microsoft Foundry 和 GitHub Models 快速入門指南
- **03.FineTuning/** - 微調文件及教學
- **04.HOL/** - 實作實驗室（含 .NET 範例）

### File Formats

- **Jupyter Notebooks (`.ipynb`)** - 互動式 Python 教學腳本，README 中以 📓 標示
- **Python Scripts (`.py`)** - 獨立執行的 Python 範例
- **C# Projects (`.csproj`, `.sln`)** - .NET 應用與範例
- **JavaScript (`.js`, `package.json`)** - 網頁及 Node.js 範例
- **Markdown (`.md`)** - 文件及指南

## Working with Examples

### Running Jupyter Notebooks

Most examples are provided as Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # 開啟瀏覽器介面
# 導航至所需的 .ipynb 檔案
```

### Running Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Running .NET Examples

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Or build entire solution:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Running JavaScript/Web Examples

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # 熱重載開發
```

## Testing

此倉庫包含範例代碼與教學，而非傳統含單元測試的軟件專案。驗證通常依據：

1. <strong>執行範例</strong> - 確保範例無錯誤執行
2. <strong>核對輸出</strong> - 核實模型回應是否恰當
3. <strong>跟隨教程</strong> - 教學步驟正常運作

**常見驗證方式：**
- 在目標環境中測試範例執行
- 確認依賴安裝正確
- 檢查模型能成功下載/加載
- 確認預期行為符合文檔

## Code Style and Conventions

### General Guidelines

- 範例需清晰、具有註解且具教學意義
- 遵循語言特定慣例（Python 遵循 PEP 8、C# 遵循 .NET 標準）
- 範例聚焦於展示特定 Phi 模型能力
- 包含解釋關鍵概念與模型參數的註解

### Documentation Standards

**URL Formatting:**
- 使用 `[text](../../url)` 格式無多餘空格
- 相對鏈接使用 `./` 表示當前目錄，`../` 表示父目錄
- 不使用國家特定的本地化網址（避免 `/en-us/`, `/en/`）

**Images:**
- 所有圖片儲存在 `/imgs/` 目錄
- 使用包含英文字母、數字及連字號的描述性名稱
- 範例：`phi-3-architecture.png`

**Markdown Files:**
- 文件中參照實際可運行的 `/code/` 目錄範例
- 文件要與代碼同步更新
- 在 README 中以 📓 表情標記 Jupyter 筆記本鏈接

### File Organization

- `/code/` 中的代碼範例依主題/功能分類
- `/md/` 的文件結構與代碼結構相呼應（如適用）
- 相關文件（筆記本、腳本、設定）放於子目錄以保持整齊

## Pull Request Guidelines

### Before Submitting

1. **Fork 倉庫** 到自己的帳戶
2. **分 PR 類型：**
   - Bug 修正放一個 PR
   - 文件更新放另一個 PR 
   - 新範例獨立 PR
   - 拼寫錯誤修正可合併

3. **處理合併衝突：**
   - 先更新本地 `main` 分支
   - 常與官方同步

4. **翻譯 PR：**
   - 必須涵蓋資料夾內所有文件翻譯
   - 保持與原語言目錄結構一致

### Required Checks

PR 會自動執行 GitHub 工作流程驗證：

1. <strong>相對路徑驗證</strong> - 內部鏈接必須有效
   - 在 VS Code 按 Ctrl+點擊測試
   - 利用 VS Code 內建路徑建議 (`./` 或 `../`)

2. **URL 本地化檢查** - 網址不得包含國家語言代碼
   - 移除 `/en-us/`，`/en/` 或其他語言碼
   - 使用通用國際網址

3. <strong>網址有效檢查</strong> - 網址需正確返回 200 狀態
   - 提交前確認鏈接可訪問
   - 部分失敗可能因網絡限制

### PR Title Format

```
[component] Brief description
```

Examples:
- `[docs] Add Phi-4 inference tutorial`
- `[code] Fix ONNX Runtime integration example`
- `[translation] Add Japanese translation for intro guides`

## Common Development Patterns

### Working with Phi Models

**Model Loading:**
- 範例使用 Transformers、ONNX Runtime、MLX、OpenVINO 等不同框架
- 模型通常從 Hugging Face、Azure 或 GitHub Models 下載
- 確認模型與硬體（CPU、GPU、NPU）相容

**Inference Patterns:**
- 文字生成：大部分範例使用聊天/指令變體
- 視覺：Phi-3-vision 與 Phi-4-multimodal 用於圖像理解
- 音頻：Phi-4-multimodal 支援音頻輸入
- 推理：Phi-4-reasoning 變體用於進階推理任務

### Platform-Specific Notes

**Microsoft Foundry:**
- 需要 Azure 訂閱與 API 關鍵
- 請參閱 `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- 免費測試等級可用
- 請參閱 `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Local Inference:**
- ONNX Runtime：跨平臺，優化推論
- Ollama：便捷本地模型管理（開發容器已預配置）
- Apple MLX：針對蘋果晶片優化

## Troubleshooting

### Common Issues

**Memory Issues:**
- Phi 模型需大量記憶體（特別是視覺/多模態版本）
- 資源受限環境建議使用量化模型
- 請參閱 `/md/01.Introduction/04/QuantifyingPhi.md`

**Dependency Conflicts:**
- Python 範例可能對版本有特定要求
- 為每個範例使用虛擬環境
- 檢查個別 `requirements.txt`

**Model Download Failures:**
- 大型模型在慢速連線下可能超時
- 建議使用雲端環境（Codespaces、Azure）
- 檢查 Hugging Face 快取：`~/.cache/huggingface/`

**.NET Project Issues:**
- 確保已安裝 .NET 8.0 SDK
- 建構前執行 `dotnet restore`
- 部分專案有專用的 CUDA 配置（Debug_Cuda）

**JavaScript/Web Examples:**
- 使用 Node.js 18+ 保證相容性
- 如有問題刪除 `node_modules` 並重裝
- 檢查瀏覽器控制檯的 WebGPU 兼容性錯誤

### Getting Help

- **Discord:** 參加 Microsoft Foundry 社群 Discord
- **GitHub Issues:** 報告錯誤與問題
- **GitHub Discussions:** 提問與分享知識

## Additional Context

### Responsible AI

所有 Phi 模型的使用應遵循 Microsoft 的負責任 AI 原則：
- 公平性、可靠性、安全性
- 隱私與安全  
- 包容性、透明度、問責制
- 生產應用採用 Azure AI 內容安全
- 請參閱 `/md/01.Introduction/01/01.AISafety.md`

### Translations

- 透過自動化 GitHub Action 支援超過50種語言
- 翻譯檔案存放於 `/translations/` 目錄
- 由協作翻譯工作流程維護
- 請勿手動編輯自動生成的翻譯文件

### Contributing

- 遵循 `CONTRIBUTING.md` 中的指南
- 接受貢獻者授權協議（CLA）
- 遵守 Microsoft 開源行為守則
- 務必避免在提交中包含安全資訊和憑證

### Multi-Language Support

此倉庫為多語言專案，包含以下語言範例：
- **Python** - ML/AI 工作流程、Jupyter 筆記本、微調
- **C#/.NET** - 企業應用、ONNX Runtime 整合
- **JavaScript** - Web AI、使用 WebGPU 的瀏覽器推論

請選擇最符合您使用場景與部署目標的語言。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->