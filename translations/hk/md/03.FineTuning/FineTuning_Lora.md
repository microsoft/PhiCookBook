<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-08T05:16:51+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "hk"
}
-->
# **用 Lora 微調 Phi-3**

用 [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 於自訂聊天指令數據集微調 Microsoft 的 Phi-3 Mini 語言模型。

LORA 有助提升對話理解及回應生成能力。

## Phi-3 Mini 微調逐步教學：

**匯入及設定**

安裝 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

先匯入所需庫，例如 datasets、transformers、peft、trl 及 torch。
設定日誌以追蹤訓練過程。

你可以選擇用 loralib 實作的對應層來替換部分層。我們目前只支援 nn.Linear、nn.Embedding 同 nn.Conv2d。對於某些情況下單一 nn.Linear 代表多層（例如部分 attention qkv 投影實作，詳見附註），我們亦支援 MergedLinear。

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

在訓練迴圈開始前，只標記 LoRA 參數為可訓練。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

儲存檢查點時，只產生包含 LoRA 參數的 state_dict。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

用 load_state_dict 載入檢查點時，記得設定 strict=False。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

現在訓練就可以照常進行。

**超參數**

定義兩個字典：training_config 和 peft_config。training_config 包含訓練的超參數，例如學習率、批次大小及日誌設定。

peft_config 則指定 LoRA 相關參數，如 rank、dropout 及任務類型。

**模型及分詞器載入**

指定預訓練 Phi-3 模型路徑（例如 "microsoft/Phi-3-mini-4k-instruct"）。設定模型參數，包括快取使用、資料類型（bfloat16 用於混合精度）及注意力實作。

**訓練**

用自訂聊天指令數據集微調 Phi-3 模型。利用 peft_config 中的 LoRA 設定進行高效適應。用指定的日誌策略監控訓練進度。
評估及儲存：評估微調後的模型。
訓練過程中儲存檢查點以便後續使用。

**範例**
- [用呢個範例筆記本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub 用 LORA 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 模型卡 - LORA 微調範例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub 用 QLORA 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件以其母語版本為權威來源。對於重要資料，建議採用專業人工翻譯。我哋對因使用本翻譯而引致嘅任何誤解或誤釋概不負責。