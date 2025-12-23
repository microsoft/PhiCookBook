<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-12-21T16:47:27+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "kn"
}
-->
# ಲ್ಯಾಬ್. ಡಿವೈಸ್ನಲ್ಲಿ ಇನ್ಫರೆನ್ಸ್‌ಗಾಗಿ AI ಮಾದರಿಗಳನ್ನು ಅನುಕೂಲಗೊಳಿಸಿ

## ಪರಿಚಯ 

> [!IMPORTANT]
> ಈ ಲ್ಯಾಬ್‌ಗೆ ಹೊಂದಿಸಿದ ಚಾಲಕಗಳು ಮತ್ತು CUDA ಟೂಲ್‍ಕಿಟ್ (ಆವೃತ್ತಿ 12+) ಸ್ಥಾಪಿಸಲ್ಪಟ್ಟಿರುವ **Nvidia A10 ಅಥವಾ A100 GPU** ಅಗತ್ಯವಿದೆ.

> [!NOTE]
> ಇದು OLIVE ಬಳಸಿ ಡಿವೈಸ್ನಲ್ಲಿ ಇನ್ಫರೆನ್ಸ್‌ಗಾಗಿ ಮಾದರಿಗಳನ್ನು ಅನುಕೂಲಗೊಳಿಸುವ ಮೂಲ ಸಿದ್ಧಾಂತಗಳ ಕೈಯಲ್ಲಿ ಪರಿಚಯ ನೀಡುವ **35-ನಿಮಿಷಗಳ** ಲ್ಯಾಬ್ ಆಗಿದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಲ್ಯಾಬ್ ಮುಗಿದಾಗ, ನೀವು OLIVE ಅನ್ನು ಬಳಸಿಕೊಂಡು ಕೆಳಕಂಡವುಗಳನ್ನು ಮಾಡಲು ಸಾಮರ್ಥ್ಯ ಹೊಂದಿರುತ್ತೀರಿ:

- AWQ ಕ್ವಾಂಟೈಜೇಶನ್ ವಿಧಾನವನ್ನು ಬಳಸಿಕೊಂಡು AI ಮಾದರಿಯನ್ನು ಕ್ವಾಂಟೈಸ್ ಮಾಡುವುದು.
- ನಿರ್ದಿಷ್ಟ ಕಾರ್ಯಕ್ಕೆ AI ಮಾದರಿಯನ್ನು ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡುವುದು.
- ONNX Runtime ಮೇಲೆ ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಡಿವೈನ್ಸ್ ಇನ್ಫರೆನ್ಸ್‌‌ಗಾಗಿ LoRA ಅಡಾಪ್ಟರ್‌ಗಳು (ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡಿದ ಮಾದರಿ) ತಯಾರಿಸುವುದು.

### Olive ಎಂದರೆ ಏನು

Olive (*O*NNX *live*) ಒಂದು ಮಾದರಿ ಅನುಕೂಲಗೊಳಿಸುವ ಟೂಲ್‌ಕಿಟ್ ಆಗಿದ್ದು, ಜೊತೆಗೆ CLI ಕೂಡ ಹೊಂದಿದೆ, ಇದು ನಿಮಗೆ ONNX runtime +++https://onnxruntime.ai+++ ಗಾಗಿ ಗುಣಮಟ್ಟ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆಯೊಂದಿಗೆ ಮಾದರಿಗಳನ್ನು ಶಿಪ್ ಮಾಡುವಂತೆ ಮಾಡುತ್ತದೆ.

![Olive ಪ್ರಯಾಹ](../../../../../translated_images/olive-flow.a47985655a756dcba73521511ea42eef359509a3a33cbd4b9ac04ba433287b80.kn.png)

Olive ಗೆ ಇನ್ಪುಟ್ ಸಾಮಾನ್ಯವಾಗಿ PyTorch ಅಥವಾ Hugging Face ಮಾದರಿ ಆಗಿದ್ದು, ಔಟ್‌ಪುಟ್ ಒಂದು ಅನುಕೂಲಗೊಳಿಸಿದ ONNX ಮಾದರಿ ಆಗುತ್ತದೆ, ಮತ್ತು ಅದು ONNX runtime ಅನ್ನು ಚಲಾಯಿಸುತ್ತಿರುವ ಸಾಧನ (ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಗುರಿ) ಮೇಲೆ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ. Olive ಮಾದರಿಯನ್ನು ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಗುರಿಯ AI ಆಕ್ಸಲೆರೆಟರ್‌ಗಾದ (NPU, GPU, CPU) — ಉದಾಹರಣೆಗೆ Qualcomm, AMD, Nvidia ಅಥವಾ Intel ಇಂತಹ ಹಾರ್ಡ್‌ವೇರ್ ಒದಗಿಸುವವರಿಂದ — ಅನುಕೂಲಗೊಳಿಸುತ್ತದೆ.

Olive ಒಂದು *workflow* ಅನ್ನು ರನ್ ಮಾಡುತ್ತದೆ, ಇದು ಕ್ರಮವಾಗಿ ಆಗುವ ವೈಯಕ್ತಿಕ ಮಾದರಿ ಅನುಕೂಲಗೊಳಿಸುವ ಕರ್ತವ್ಯಗಳ ಸರಣಿಯಾಗಿರುತ್ತದೆ, ಮತ್ತು ಅವುಗಳನ್ನು *passes* ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ — ಉದಾಹರಣೆಗೆ: model compression, graph capture, quantization, graph optimization. ಪ್ರತಿ pass ಗೆ ಟ್ಯೂನ್ ಮಾಡಬಹುದಾದ ಕೆಲ ಪರಿಮಾಣಗಳು ಇರುತ್ತವೆ, ಅವುಗಳನ್ನು ಸಂಬಂಧಿತ ಮೌಲ್ಯಮಾಪಕರಿಂದ ಶುದ್ಧತೆ ಮತ್ತು ವಿಳಂಬಂತಹ ಉತ್ತಮ ಮೆಟ್ರಿಕ್ಸ್ ಗಳನ್ನು ಪಡೆಯಲು ಅಳವಡಿಸಬಹುದಾಗಿರುತ್ತವೆ. Olive ಪ್ರತಿ pass ಅನ್ನು ಒಂದೊಂದಾಗಿ ಅಥವಾ ಕೆಲವು pass ಗಳನ್ನು ಒಟ್ಟಿಗೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಟ್ಯೂನ್ ಮಾಡಲು ಹುಡುಕಾಟ ಆಲ್ಗಾರಿತಮ್ ಬಳಸುವ ಹುಡುಕಾಟ ರಣನೀತಿಯನ್ನು ಬಳಸುತ್ತದೆ.

#### Olive ನ ಪ್ರಯೋಜನಗಳು

- **ಕೋಪ ಮತ್ತು ಸಮಯವನ್ನು ಕಡಿಮೆ ಮಾಡಿ**: ಗ್ರಾಫ್ ಅನುಕೂಲಗೊಳಿಸುವಿಕೆ, ಸಂಕೋಚನ ಮತ್ತು ಕ್ವಾಂಟೈಜೇಶನ್‌ಗೆ ವಿವಿಧ ತಂತ್ರಗಳ ಪ್ರಯತ್ನ-ಮತ್ತು-ದೋಷ ಕೈಯಾದ ಪ್ರಯೋಗಗಳ ಮೂಲಕ ಉಂಟಾಗುವ ಕೋಪ ಮತ್ತು ಸಮಯವನ್ನು ಕಡಿಮೆ ಮಾಡಿ. ನಿಮ್ಮ ಗುಣಮಟ್ಟ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತಾ ನಿರ್ಬಂಧಗಳನ್ನು ನಿರ್ಧರಿಸಿ ಮತ್ತು Olive ಗೆ ಅತ್ಯುತ್ತಮ ಮಾದರಿಯನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಹುಡುಕಲು ಬಿಡಿ.
- **40+ ಒಳಗೊಂಡಿರುವ ಮಾದರಿ ಅನುಕೂಲಗೊಳಿಸುವ ಘಟಕಗಳು** ಕ್ವಾಂಟೈಜೇಶನ್, ಸಂಕೋಚನ, ಗ್ರಾಫ್ ಅನ್ಕೂಲುಗೊಳಿಕೆ ಮತ್ತು ಫೈನ್‌ಟ್ಯೂನಿಂಗ್‌ನ ಮುಂಚೂಣಿಯ ತಂತ್ರಗಳನ್ನೊಳಗೊಂಡಿವೆ.
- **ಉಪಯೋಗಿಸಲು ಸುಲಭ CLI** ಸಾಮಾನ್ಯ ಮಾದರಿ ಅನುಕೂಲಗೊಳಿಸುವ ಕಾರ್ಯಗಳಿಗಾಗಿ. ಉದಾಹರಣೆಗೆ, olive quantize, olive auto-opt, olive finetune.
- ಮಾದರಿ ಪ್ಯಾಕೇಜಿಂಗ್ ಮತ್ತು ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಒಳಗೊಂಡಿದೆ.
- **Multi LoRA serving** ಗಾಗಿ ಮಾದರಿಗಳನ್ನು ತಯಾರಿಸುವುದನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.
- ಮಾದರಿ ಅನುಕೂಲಗೊಳಿಸುವಿಕೆ ಮತ್ತು ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಕಾರ್ಯಗಳನ್ನು ಕಲೆ ಹಾಕಲು YAML/JSON ಬಳಸಿ workflows ರಚಿಸಬಹುದು.
- **Hugging Face** ಮತ್ತು **Azure AI** ಸಂಯೋಜನೆ.
- ವೆಚ್ಚವನ್ನು **ಉಳಿತಾಯ ಮಾಡಲು** ಒಳಗೊಂಡ **ಕ್ಯಾಚಿಂಗ್** ಯಂತ್ರಣೆಯನ್ನು ಹೊಂದಿದೆ.

## ಲ್ಯಾಬ್ ಸೂಚನೆಗಳು
> [!NOTE]
> ದಯವಿಟ್ಟು ನೀವು ನಿಮ್ಮ Azure AI Hub ಮತ್ತು Project ಅನ್ನು ಒದಗಿಸಿಕೊಂಡಿದ್ದೀರಿ ಮತ್ತು Lab 1 ಪ್ರಕಾರ ನಿಮ್ಮ A100 compute ಅನ್ನು ಸಜ್ಜುಗೊಳಿಸಿದ್ದೀರಿ ಎಂಬುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

### ಹಂತ 0: ನಿಮ್ಮ Azure AI Compute ಗೆ ಸಂಪರ್ಕಗೊಳ್ಳಿ

ನೀವು **VS Code** ನಲ್ಲಿ ಇರುವ ರಿಮೋಟ್ ವೈಶಿಷ್ಟ್ಯವನ್ನು ಬಳಸಿ Azure AI compute ಗೆ ಸಂಪರ್ಕಗೊಳ್ಳುತ್ತೀರಿ. 

1. ನಿಮ್ಮ **VS Code** ಡೆಸ್ಕ್‌ಟಾಪ್ ಅಪ್ಲಿಕೇಶನ್ ತೆರೆಯಿರಿ:
1. **Shift+Ctrl+P** を ಬಳಸಿ **command palette** ತೆರೆಯಿರಿ
1. command palette ನಲ್ಲಿ **AzureML - remote: Connect to compute instance in New Window** ಅನ್ನು ಹುಡುಕಿ.
1. Compute ಗೆ ಸಂಪರ್ಕಗೊಳ್ಳಲು ಪರದೆ ಮೇಲಿನ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ. ಇದರಲ್ಲಿ ನಿಮ್ಮ Azure Subscription, Resource Group, Project ಮತ್ತು Lab 1 ನಲ್ಲಿ ನೀವು ಸಂಯೋಜಿಸಿದ Compute ಹೆಸರುಗಳನ್ನು ಆಯ್ಕೆಮಾಡುವುದು ಸೇರಿದೆ.
1. ನಿಮ್ಮ Azure ML Compute ನೋಡ್‌ಗೆ ಸಂಪರ್ಕವಾದ ನಂತರ, ಇದು **Visual Code ನ ಕೆಳಬಲ ಭಾಗದಲ್ಲಿ** `><Azure ML: Compute Name` ಎಂದು ಪ್ರದರ್ಶನವಾಗುತ್ತದೆ

### ಹಂತ 1: ಈ ರೆಪೊ ಕ್ಲೋನ್ ಮಾಡಿ

VS Code ನಲ್ಲಿ, ಹೊಸ ಟರ್ಮಿನಲ್ ಅನ್ನು **Ctrl+J** ಮೂಲಕ ತೆರೆಯಬಹುದು ಮತ್ತು ಈ ರೆಪೊ ಅನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ:

In the terminal you should see the prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
ಸೊಲ್ಯೂಶನ್ ಅನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### ಹಂತ 2: VS Code ನಲ್ಲಿ ಫೋಲ್ಡರ್ ತೆರೆಯಿರಿ

ಸಂಬಂಧಿತ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ VS Code ತೆರೆಯಲು ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ, ಇದು ಹೊಸ ವಿಂಡೋವನ್ನು ತೆರೆಯುತ್ತದೆ:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

ಮರೆನಾಗಿ, **File** > **Open Folder** ಆಯ್ಕೆಮಾಡಿ ಫೋಲ್ಡರ್ ತೆರೆಯಬಹುದು. 

### ಹಂತ 3: ಅವಲಂಬಿತತೆಗಳು

ನಿಮ್ಮ Azure AI Compute ಇನ್ಸ್ಟಾನ್ಸ್‌ನಲ್ಲಿ VS Code ನಲ್ಲಿ ಟರ್ಮಿನಲ್ ವಿಂಡೋ ತೆರೆಯಿರಿ (ಟಿಪ್: **Ctrl+J**) ಮತ್ತು ಅವಲಂಬಿತತೆಗಳನ್ನು ಸ್ಥಾಪಿಸಲು ಕೆಳಗಿನ ಆಜ್ಞೆಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> ಎಲ್ಲಾ ಅವಲಂಬಿತತೆಗಳನ್ನು ಸ್ಥಾಪಿಸಲು ಸುಮಾರು ~5 ನಿಮಿಷಗಳು ಕಳೆಯುತ್ತವೆ.

ಈ ಲ್ಯಾಬ್‌ನಲ್ಲಿ ನೀವು Azure AI Model ಕ್ಯಾಟಲಾಗ್ಗೆ ಮಾದರಿಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮತ್ತು ಅಪ್‌ಲೋಡ್ ಮಾಡುತ್ತೀರಿ. ಆದ್ದರಿಂದ ಮಾದರಿ ಕ್ಯಾಟಲಾಗ್‌ಗೆ ಪ್ರವೇಶಿಸಲು, ನೀವು ಕೆಳಗಿನದನ್ನು ಬಳಸಿ Azure ಗೆ ಲಾಗಿನ್ ಆಗಬೇಕಾಗುತ್ತದೆ:

```bash
az login
```

> [!NOTE]
> ಲಾಗಿನ್ ಸಮಯದಲ್ಲಿ ನಿಮಗೆ ನಿಮ್ಮ subscription ಆಯ್ಕೆಮಾಡಲು ಕೇಳಲಾಗುತ್ತದೆ. ದಯವಿಟ್ಟು ಈ ಲ್ಯಾಬ್‌ಗೆ ಒದಗಿಸಿದ subscription ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ.

### ಹಂತ 4: Olive ಆಜ್ಞೆಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ 

ನಿಮ್ಮ Azure AI Compute ಇನ್ಸ್ಟಾನ್ಸ್‌ನಲ್ಲಿ VS Code ನಲ್ಲಿ ಟರ್ಮಿನಲ್ ವಿಂಡೋ ತೆರೆಯಿರಿ (ಟಿಪ್: **Ctrl+J**) ಮತ್ತು `olive-ai` conda ಪರಿಸರ ಸಕ್ರಿಯಗೊಳಿಸಲಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿ:

```bash
conda activate olive-ai
```

ಮುಂದೆ, ಕಮಾಂಡ್ ಲೈನ್‌ನಲ್ಲಿ ಕೆಳಗಿನ Olive ಆಜ್ಞೆಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ.

1. **ಡೇಟಾ ಪರಿಶೀಲನೆ:** ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನೀವು ಪ್ರಯಾಣ ಸಂಬಂಧಿತ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಲು ವಿಶೇಷಗೊಳಿಸುವುದಕ್ಕಾಗಿ Phi-3.5-Mini ಮಾದರಿಯನ್ನು ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡುತ್ತೀರಿ. ಕೆಳಗಿನ ಕೋಡ್ ಡೇಟಾಸೆಟ್‌ನ ಮೊದಲ ಕೆಲವು ದಾಖಲೆಗಳನ್ನು ತೋರಿಸುತ್ತದೆ, ಅವು JSON lines ಸ್ವರೂಪದಲ್ಲಿವೆ:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **ಮಾದರಿಯನ್ನು ಕ್ವಾಂಟೈಸ್ ಮಾಡಿ:** ಮಾದರಿಯನ್ನು ತರಬೇತಿಮಾಡುವ ಮೊದಲು, ನೀವು ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಬಳಸಿ Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ ಎಂಬ ತಂತ್ರವನ್ನು ಬಳಸಿಕೊಂಡು ಮೊದಲಿಗೆ ಕ್ವಾಂಟೈಸ್ ಮಾಡುತ್ತೀರಿ. AWQ ಇನ್ಫರೆನ್ಸ್ ವೇಳೆ ಉಂಟಾಗುವ ಆಕ್ಟಿವೇಶನ್ಗಳನ್ನು ಪರಿಗಣಿಸಿ ಮಾದರಿಯ ತೂಕಗಳನ್ನು ಕ್ವಾಂಟೈಸ್ ಮಾಡುತ್ತದೆ. ಇದರ ಅರ್ಥ, ಕ್ವಾಂಟೈಜೇಶನ್ ಪ್ರಕ್ರಿಯೆ ಆಕ್ಟಿವೇಶನ್ಗಳದಲ್ಲಿನ ವಾಸ್ತವಿಕ ಡೇಟಾ ವಿತರಣೆಗಳನ್ನು ಗಮನದಲ್ಲಿಟ್ಟುಕೊಂಡು ಕೆಲಸ ಮಾಡುತ್ತದೆ, ಇದರಿಂದ ಸಾಂಪ್ರದಾಯಿಕ ತೂಕ ಕ್ವಾಂಟೈಜೇಶನ್ ವಿಧಾನಗಳಿಗಿಂತ ಮಾದರಿ ಶುದ್ಧತೆಯನ್ನು ಉತ್ತಮವಾಗಿ ಸಂರಕ್ಷಿಸುತ್ತದೆ.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    ಇದು AWQ ಕ್ವಾಂಟೈಜೇಶನ್ ಅನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು **ಸುಮಾರು ~8 ನಿಮಿಷಗಳು** ಬೇಕಾಗುತ್ತದೆ, ಮತ್ತು ಇದು ಮಾದರಿಯ ಗಾತ್ರವನ್ನು **ಸುಮಾರು ~7.5GB ರಿಂದ ~2.5GB** ಗೆ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.
   
   ಈ ಲ್ಯಾಬ್‌ನಲ್ಲಿ ನಾವು Hugging Face ನಿಂದ ಮಾದರಿಗಳನ್ನು ಹೇಗೆ ಇನ್ಪುಟ್ ಮಾಡುವುದು ಎಂಬುದನ್ನು ತೋರಿಸುತ್ತಿದ್ದೇವೆ (ಉದಾಹರಣೆ: `microsoft/Phi-3.5-mini-instruct`). ಆದಾಗ್ಯೂ, Olive ನೊಂದಿಗೆ ನೀವು `model_name_or_path` ಆರ್ಗ್ಯುಮೆಂಟ್ ಅನ್ನು Azure AI ಆಸ್ತಿ ID ಗೆ (ಉದಾಹರಣೆ: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) ಅಪ್‌ಡೇಟ್ ಮಾಡುವ ಮೂಲಕ Azure AI ಕ್ಯಾಟಲಾಗ್‌ನಿಂದ ಮಾದರಿಗಳನ್ನು ಇನ್ಪುಟ್ ಮಾಡಬಹುದಾಗಿದೆ. 

1. **ಮಾದರಿಯನ್ನು ತರಬೇತಿಮಾಡಿ:** ಮುಂದಾಗಿ, `olive finetune` ಆಜ್ಞೆ ಕ್ವಾಂಟೈಸ್ ಮಾಡಿದ ಮಾದರಿಯನ್ನು ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡುತ್ತದೆ. ಫೈನ್-ಟ್ಯೂನಿಂಗ್‌ಗೆ ಮೊದಲು ಮಾದರಿಯನ್ನು ಕ್ವಾಂಟೈಸ್ ಮಾಡುವುದರಿಂದ ನಂತರದಲ್ಲಿ ಮಾಡುವುದಕ್ಕಿಂತ ಉತ್ತಮ ಶುದ್ಧತೆ ಸಿಗುತ್ತದೆ ಏಕೆಂದರೆ ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಪ್ರಕ್ರಿಯೆ ಕ್ವಾಂಟೈಜೇಶನ್‌ನಿಂದ ಉಂಟಾದ ಕೆಲವು ನಷ್ಟವನ್ನು ಪುನರುದ್ಧರಿಸುತ್ತದೆ.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    ಫೈನ್-ಟ್ಯೂನಿಂಗ್ (100 ಹಂತಗಳೊಂದಿಗೆ) ಪೂರ್ಣಗೊಳ್ಳಲು **ಸುಮಾರು ~6 ನಿಮಿಷಗಳು** ಬೇಕಾಗುತ್ತದೆ.

1. **ಅನುಕೂಲಗೊಳಿಸಿ:** ಮಾದರಿಯನ್ನು ತರಬೇತಿಮಾಡಿದ ನಂತರ, ನೀವು Olive ನ `auto-opt` ಆಜ್ಞೆಯನ್ನು ಬಳಸಿ ಮಾದರಿಯನ್ನು ಅನುಕೂಲಗೊಳಿಸುತ್ತೀರಿ, ಇದು ONNX ಗ್ರಾಫ್ ಅನ್ನು ಹಿಡಿದುಕೊಳ್ಳುತ್ತದೆ ಮತ್ತು ಮಾದರಿಯನ್ನು ಸಂಕೋಚಿಸಿ ಫ್ಯೂಶನ್ ಮಾಡಿ CPU ರಿಗಾಗಿ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸುಧಾರಿಸಲು ಅನೇಕ ಸ್ವಯಂಚಾಲಿತ ಅಪ್ಟಿಮೈಸೇಶನ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. ಗಮನಿಸಿ, ನೀವು `--device` ಮತ್ತು `--provider` ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಅಪ್‌ಡೇಟ್ ಮಾಡುವ ಮೂಲಕ NPU ಅಥವಾ GPU ಮುಂತಾದ ಇತರ ಸಾಧನಗಳಿಗಾಗಿ ಸಹ ಅನುಕೂಲಗೊಳಿಸಬಹುದು — ಆದರೆ ಈ ಲ್ಯಾಬ್ ಉದ್ದೇಶಕ್ಕಾಗಿ ನಾವು CPU ಅನ್ನು ಬಳಸುತ್ತೇವೆ.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    ಅನುಕೂಲಗೊಳಿಸುವಿಕೆ ಪೂರ್ಣಗೊಳ್ಳಲು **ಸುಮಾರು ~5 ನಿಮಿಷಗಳು** ಅಗತ್ಯವಾಗುತ್ತದೆ.

### ಹಂತ 5: ಮಾದರಿ ಇನ್ಫರೆನ್ಸ್ ತ್ವರಿತ ಪರೀಕ್ಷೆ

ಮಾದರಿ ಇನ್ಫರೆನ್ಸ್ ಪರೀಕ್ಷಿಸಲು, ನಿಮ್ಮ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ **app.py** ಎಂಬ Python ಫೈಲ್ ರಚಿಸಿ ಮತ್ತು ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ನಕಲಿಸಿ-ಅಂಟಿಸಿ:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

ಕೆಳಗಿನಂತೆ ಕೋಡ್ ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ:

```bash
python app.py
```

### ಹಂತ 6: ಮಾದರಿಯನ್ನು Azure AI ಗೆ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ

ಮಾದರಿಯನ್ನು Azure AI ಮಾದರಿ ಸಂಗ್ರಹಣೆಗೆ ಅಪ್‌ಲೋಡ್ ಮಾಡುವುದರಿಂದ ಅದು ನಿಮ್ಮ ಡೆವಲಪ್‌ಮೆಂಟ್ ತಂಡದ ಇತರ ಸದಸ್ಯರೊಂದಿಗೆ ಹಂಚಿಕೊಳ್ಳಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ ಮತ್ತು ಮಾದರಿಯ ವರ್ಜನ್ ಕಂಟ್ರೋಲ್ ಅನ್ನು ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ. ಮಾದರಿಯನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಲು ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ:

> [!NOTE]
> `{}` ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್‌ಗಳನ್ನು ನಿಮ್ಮ resource group ಮತ್ತು Azure AI Project ನ ಹೆಸರಿನಿಂದ ಅಪ್‌ಡೇಟ್ ಮಾಡಿ. 

To find your resource group `"resourceGroup"and Azure AI Project name, run the following command 

```
az ml workspace show
```

ಅಥವಾ +++ai.azure.com+++ ಗೆ ಹೋಗಿ ಮತ್ತು **management center** **project** **overview** ಆಯ್ಕೆಮಾಡಿ

Update the `{}` placeholders with the name of your resource group and Azure AI Project Name.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
ನಂತರ ನೀವು ನಿಮ್ಮ ಅಪ್‌ಲೋಡ್ ಮಾಡಿದ ಮಾದರಿಯನ್ನು ನೋಡಬಹುದು ಮತ್ತು ನಿಮ್ಮ ಮಾದರಿಯನ್ನು https://ml.azure.com/model/list ನಲ್ಲಿ ಡಿಪ್ಲಾಯ್ ಮಾಡಬಹುದು

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಅಸ್ವೀಕರಣ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮರ್ಪಕತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿರಿ. ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅದರ ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗ್ರಹಣೆಗಳು ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->