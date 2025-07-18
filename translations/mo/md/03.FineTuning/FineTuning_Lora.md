<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:28:22+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "mo"
}
-->
# **使用 Lora 微調 Phi-3**

使用 [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 在自訂聊天指令資料集上微調微軟的 Phi-3 Mini 語言模型。

LORA 有助於提升對話理解與回應生成能力。

## Phi-3 Mini 微調逐步指南：

**匯入與設定**

安裝 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先匯入必要的函式庫，如 datasets、transformers、peft、trl 和 torch。
設定日誌以追蹤訓練過程。

你可以選擇透過替換部分層為 loralib 實作的對應層來進行調整。目前僅支援 nn.Linear、nn.Embedding 和 nn.Conv2d。我們也支援 MergedLinear，適用於單一 nn.Linear 代表多層的情況，例如某些注意力 qkv 投影的實作（詳見附註）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

在訓練迴圈開始前，僅標記 LoRA 參數為可訓練。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

儲存檢查點時，產生只包含 LoRA 參數的 state_dict。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

使用 load_state_dict 載入檢查點時，請務必設定 strict=False。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

現在即可照常進行訓練。

**超參數**

定義兩個字典：training_config 和 peft_config。training_config 包含訓練的超參數，如學習率、批次大小及日誌設定。

peft_config 指定 LoRA 相關參數，如 rank、dropout 和任務類型。

**模型與分詞器載入**

指定預訓練 Phi-3 模型的路徑（例如 "microsoft/Phi-3-mini-4k-instruct"）。配置模型設定，包括快取使用、資料類型（混合精度使用 bfloat16）及注意力實作。

**訓練**

使用自訂聊天指令資料集微調 Phi-3 模型。利用 peft_config 中的 LoRA 設定進行高效調整。透過指定的日誌策略監控訓練進度。
評估與儲存：評估微調後的模型。
訓練過程中儲存檢查點以供後續使用。

**範例**
- [使用此範例筆記本深入了解](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub 使用 LORA 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 模型卡範例 - LORA 微調](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub 使用 QLORA 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。