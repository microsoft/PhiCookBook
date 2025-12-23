<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-12-21T15:35:52+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "kn"
}
-->
# ಪ್ರಾಯೋಗಶಾಲೆ. ಸಾಧನದಲ್ಲಿ ಇನ್ಫರೆನ್ಸ್‌ಗಾಗಿ AI ಮಾದರಿಗಳನ್ನು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುವುದು

## ಪರಿಚಯ 

> [!IMPORTANT]
> ಈ ಪ್ರಯೋಗಶಾಲೆಗೆ ಸಂಭಂಧಿತ ಡ್ರೈವರ್‌ಗಳು ಮತ್ತು CUDA ಟೂಲ್ಕಿಟ್ (ಆವೃತ್ತಿ 12+) ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲಾದ **Nvidia A10 ಅಥವಾ A100 GPU** ಅಗತ್ಯವಿದೆ.

> [!NOTE]
> ಇದು **35 ನಿಮಿಷಗಳ** ಪ್ರಯೋಗಶಾಲೆ ಆಗಿದ್ದು, OLIVE ಬಳಸಿ ಸಾಧನದಲ್ಲಿ ಇನ್ಫರೆನ್ಸ್‌ಗಾಗಿ ಮಾದರಿಗಳನ್ನು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುವ بنيادي ತತ್ವಗಳ ಬಗ್ಗೆ ಕೈಯಲ್ಲಿ ತರಬೇತಿ ಪರಿಚಯವನ್ನು ನಿಮಗೆ ನೀಡುತ್ತದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯ ಅಂತ್ಯಕ್ಕೆ, ನೀವು OLIVE ಅನ್ನು ಬಳಸಲು ಸಮರ್ಥರಾಗಿರುತ್ತೀರಿ:

- AWQ ಕ್ವಾಂಟೈಸೇಶನ್ ವಿಧಾನವನ್ನು ಬಳಸಿ AI ಮಾದರಿಯನ್ನು ಕ್ವಾಂಟೈಸ್ ಮಾಡುವುದು.
- ನಿರ್ದಿಷ್ಟ ಕಾರ್ಯಕ್ಕಾಗಿ AI ಮಾದರಿಯನ್ನು ಫೈನ್‌ಟ್ಯೂನ್ ಮಾಡುವುದು.
- ONNX Runtime ಮೇಲೆ ಸಾಧನದಲ್ಲಿ ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಇನ್ಫರೆನ್ಸ್ ಮಾಡಲು LoRA ಅಡಾಪ್ಟರ್‌ಗಳನ್ನು (ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡಲಾದ ಮಾದರಿ) ರಚಿಸುವುದು.

### Olive ಎಂದರೇನು

Olive (*O*NNX *live*) ಒಂದು ಮಾದರಿ ಆಪ್ಟಿಮೈಜೆಷನ್ ಟೂಲ್ಕಿಟ್ ಮತ್ತು ಅದಕ್ಕೆ ಸಂಬಂಧಿಸಿದ CLI ಆಗಿದ್ದು, ಇದು ನಿಮಗೆ ONNX runtime +++https://onnxruntime.ai+++ ನಲ್ಲಿಗಾಗಿ ಗುಣಮಟ್ಟ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆಯೊಂದಿಗೆ ಮಾದರಿಗಳನ್ನು ರವಾನಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

![Olive Flow](../../../../../translated_images/olive-flow.c4f76d9142c579b2462b631b8aa862093b595bb89064fa33e6d4fa90f937f52d.kn.png)

Olive ಗೆ ಇನ್ಪುಟ್ ಸಾಮಾನ್ಯವಾಗಿ PyTorch ಅಥವಾ Hugging Face ಮಾದರಿ ಆಗಿದ್ದು, ಔಟ್‌ಪುಟ್ ಆಗಿ ಒಂದು ಆಪ್ಟಿಮೈಸ್ ಮಾಡಲಾದ ONNX ಮಾದರಿ ಸಿಗುತ್ತದೆ ಮತ್ತು ಅದು ONNX runtime ಅನ್ನು ಚಾಲನೆಯಲ್ಲಿರುವ ಸಾಧನದಲ್ಲಿ (ಡಿಪ್ಲೋಯ್ ಗುರಿ) ನಿರ್ವಹಣೆಗೊಳ್ಳುತ್ತದೆ. Olive ನಿರ್ಧಿಷ್ಟ ಹಾರ್ಡ್‌ವೇರ್ ವendors ಗಳಾದ Qualcomm, AMD, Nvidia ಅಥವಾ Intel ಒದಗಿಸುವ ಗುರಿ ಡಿಪ್ಲೋಯ್ಮೆಂಟ್‌ನ AI ಅಕ್ಸೆಲರೇಟರ್ (NPU, GPU, CPU) ಗಾಗಿ ಮಾದರಿಯನ್ನು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುತ್ತದೆ.

Olive ಒಂದು *workflow* ಅನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಇದು ಕ್ರಮಬದ್ಧವಾದ ವೈಯಕ್ತಿಕ ಮಾದರಿ ಆಪ್ಟಿಮೈಜೆಷನ್ ಕಾರ್ಯಗಳ ಅನುಕ್ರಮ; ಇವುಗಳನ್ನು *passes* ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ — ಉದಾಹರಣೆಗೆ passes ಗಳಿಗೆ: ಮಾದರಿ ಸಂಕುಚನ, ಗ್ರಾಫ್ ಕ್ಯಾಪ್ಚರ್, ಕ್ವಾಂಟೈಸೇಶನ್, ಗ್ರಾಫ್ ಆಪ್ಟಿಮೈಜೆಷನ್ ಸೇರಿವೆ. ಪ್ರತಿ pass ಗೆ ಉತ್ತಮ ಮೌಲ್ಯಗಳನ್ನು (ಉದಾಹರಣೆ: ಶುದ್ದತೆ ಮತ್ತು ಲೇಟೆನ್ಸಿ) ಸಾಧಿಸಲು ಟ್ಯೂನ್ ಮಾಡಬಹುದಾದ ಪರಿಮಾಣಗಳಾಗಿವೆ, ಮತ್ತು ಅವುಗಳನ್ನು ಸಂಬಂಧಿತ ಮೌಲ್ಯಮಾಪಕರಿಂದ ಮೌಲ್ಯಮಾಪನ ಮಾಡಲಾಗುತ್ತದೆ. Olive ಪ್ರತಿ pass ಅನ್ನು ಏಕೈಕವಾಗಿ ಅಥವಾ ಕೆಲ pass ಗಳನ್ನು ಒಟ್ಟಿಗೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಟ್ಯೂನ್ ಮಾಡಲು ಸರ್ಚ್ ಆಲ್ಗೋರಿಥಮ್ ಬಳಸಿ ಸರ್ಚ್ ತಂತ್ರಗಳನ್ನು ಬಳಸುತ್ತದೆ.

#### Olive ನ ಪ್ರಯೋಜನಗಳು

- **ಪ್ರಯಾಸ ಮತ್ತು ಸಮಯವನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ**: ಗ್ರಾಫ್ ಆಪ್ಟಿಮೈಜೆಷನ್, ಸಂಕುಚನ ಮತ್ತು ಕ್ವಾಂಟೈಸೇಶನ್‌ಗಾಗಿ ವಿಭಿನ್ನ ತಂತ್ರಗಳ ಮೇಲೆ ಕೈಯಿಂದ ಪ್ರಯೋಗಿಸುವ ತಪಾಸಣೆ-ತಿದ್ದುಪಡಿಯ ಕ್ರಿಯೆಯಿಂದ ಉಂಟಾಗುವ ನಿರಾಸೆ ಮತ್ತು ಸಮಯವನ್ನು ಕಡಿಮೆ ಮಾಡಿ. ನಿಮ್ಮ ಗುಣಮಟ್ಟ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತಾ ನಿರ್ಬಂಧಗಳನ್ನು ನಿರ್ಧರಿಸಿ ಮತ್ತು Olive ನಿಮಗಾಗಿ ಅತ್ಯುತ್ತಮ ಮಾದರಿಯನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಂಡುಹಿಡಿಯಲಿ.
- **40+ ಒಳಗೊಂಡ ಮಾದರಿ ಆಪ್ಟಿಮೈಜೆಶನ್ ಘಟಕಗಳು** ಕ್ವಾಂಟೈಸೇಶನ್, ಸಂಕುಚನ, ಗ್ರಾಫ್ ಆಪ್ಟಿಮೈಜೆಷನ್ ಮತ್ತು ಫೈನ್‌ಟ್ಯೂನಿಂಗ್ ನಲ್ಲಿ ಆಧುನಿಕ ತಂತ್ರಗಳನ್ನು ಒಳಗೊಂಡಂತೆ.
- **ಬಳಸಲು ಸುಲಭವಾದ CLI** ಸಾಮಾನ್ಯ ಮಾದರಿ ಆಪ್ಟಿಮೈಜೇಶನ್ ಕಾರ್ಯಗಳಿಗೆ. ಉದಾಹರಣೆಗೆ, olive quantize, olive auto-opt, olive finetune.
- ಮಾದರಿ ಪ್ಯಾಕೇಜಿಂಗ್ ಮತ್ತು ಡಿಪ್ಲಾಯ್ ಒಳಗೊಂಡಿದೆ.
- **Multi LoRA ಸೇವಿಂಗ್** ರಚನೆಗಳಿಗೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ.
- YAML/JSON ಬಳಸಿ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ರಚಿಸಿ ಮಾದರಿ ಆಪ್ಟಿಮೈಜೇಶನ್ ಮತ್ತು ಡಿಪ್ಲಾಯ್ ಕಾರ್ಯಗಳನ್ನು ಸಂಯೋಜಿಸಬಹುದು.
- **Hugging Face** ಮತ್ತು **Azure AI** ಇಂಟಿಗ್ರೇಶನ್.
- ಒಳಗೊಂಡ **caching** ಯಂತ್ರವ್ಯವಸ್ಥೆ ಮೂಲಕ **ವೆಚ್ಚವನ್ನು ಉಳಿತಾಯ** ಮಾಡುವದು.

## ಪ್ರಯೋಗಶಾಲೆ ಸೂಚನೆಗಳು
> [!NOTE]
> ದಯವಿಟ್ಟು ಖಚಿತಪಡಿಸಿ ನೀವು ನಿಮ್ಮ Azure AI Hub ಮತ್ತು Project ಅನ್ನು ಪ್ರೊವಿಷನ್ ಮಾಡಿರುವಿರಿ ಮತ್ತು Lab 1 ಮುನ್ನಡೆ ಅನುಸಾರ ನಿಮ್ಮ A100 compute ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿರುವಿರಿ.

### ಹಂತ 0: ನಿಮ್ಮ Azure AI Compute ಗೆ ಸಂಪರ್ಕವಾಗಿರಿ

ನೀವು **VS Code** ನಲ್ಲಿ ರಿಮೋಟ್ ವೈಶಿಷ್ಟ್ಯವನ್ನು ಬಳಸಿ Azure AI compute ಗೆ ಸಂಪರ್ಕ ಹೊಂದುವಿರಿ. 

1. ನಿಮ್ಮ **VS Code** ಡೆಸ್ಕ್‌ಟಾಪ್ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ತೆರೆಯಿರಿ:
1. **Shift+Ctrl+P** ಬಳಸಿ **command palette** ಅನ್ನು ತೆರೆಯಿರಿ
1. command palette ನಲ್ಲಿ **AzureML - remote: Connect to compute instance in New Window** ಅನ್ನು ಹುಡುಕಿ.
1. Compute ಗೆ ಸಂಪರ್ಕ ಸಾಧಿಸಲು.Screen ನಲ್ಲಿ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ. ಇದಕ್ಕೆ ನಿಮ್ಮ Azure Subscription, Resource Group, Project ಮತ್ತು Lab 1 ನಲ್ಲಿ ಸಿದ್ಧಪಡಿಸಿಕೊಂಡ Compute ಹೆಸರನ್ನು ಆಯ್ಕೆಮಾಡುವುದು ಸೇರಿದೆ.
1. ನೀವು Azure ML Compute ನೋಡಿಗೆ ಸಂಪರ್ಕಿಸಿದ ನಂತರ ಇದು **Visual Code** ನ ಕೆಳಬಲ ಭಾಗದಲ್ಲಿ `><Azure ML: Compute Name` ಎಂದು ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ

### ಹಂತ 1: ಈ ರೆಪೊ ಅನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ

VS Code ನಲ್ಲಿ ಹೊಸ ಟರ್ಮಿನಲ್ ಅನ್ನು **Ctrl+J** ಬಳಸಿ ತೆರೆಯಿರಿ ಮತ್ತು ಈ ರೆಪೊ ಅನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ:

In the terminal you should see the prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Clone the solution 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### ಹಂತ 2: VS Code ನಲ್ಲಿ ಫೋಲ್ಡರ್ ತೆರೆಯಿರಿ

ಸಂಬಂಧಿಸಿದ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ VS Code ತೆರೆಯಲು ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು 실행ಿಸಿ; ಇದು ಹೊಸ ವಿಂಡೋವನ್ನು ತೆರೆಯುತ್ತದೆ:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

ಅಥವಾ, ನೀವು **File** > **Open Folder** ಆಯ್ಕೆಮಾಡಿ ಫೋಲ್ಡರ್ ಅನ್ನು ತೆರೆಯಬಹುದು. 

### ಹಂತ 3: ಅವಲಂಬನೆಗಳು

ನಿಮ್ಮ Azure AI Compute Instance ನಲ್ಲಿ VS Code ನಲ್ಲಿ ಟರ್ಮಿನಲ್ ವಿಂಡೋ ತೆರೆಯಿ (ಗಳಿವು: **Ctrl+J**) ಮತ್ತು ಅವಲಂಬನೆಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲು ಕೆಳಕಂಡ ಕಮಾಂಡ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸಿ:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> ಎಲ್ಲಾ ಅವಲಂಬನೆಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲು ~5 ನಿಮಿಷಗಳು ಬೇಕಾಗುತ್ತವೆ.

ಈ ಪ್ರಯೋಗಶಾಲೆಯಲ್ಲಿ ನೀವು ಮಾದರಿಗಳನ್ನು Azure AI Model ಕ್ಯಾಟಲೋಗ್‌ಗೆ ಡೌನ್‌ಲೋಡ್ ಮತ್ತು ಅಪ್‌ಲೋಡ್ ಮಾಡುತ್ತೀರಿ. ಆದ್ದರಿಂದ ಮಾದರಿ ಕ್ಯಾಟಲೋಗ್‌ಗೆ ಪ್ರವೇಶಿಸಲು, ನೀವು Azure ಗೆ ಲಾಗಿನ್ ಮಾಡಬೇಕಾಗುತ್ತದೆ:

```bash
az login
```

> [!NOTE]
> ಲಾಗಿನ್ ಮಾಡುವ ಸಮಯದಲ್ಲಿ ನಿಮಗೆ ನಿಮ್ಮ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ಆಯ್ಕೆ ಮಾಡಬೇಕಾಗಿ ಕೇಳಲಾಗುತ್ತದೆ. ಈ ಪ್ರಯೋಗಶಾಲೆಗೆ ಒದಗಿಸಲಾದ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ಅನ್ನು ಸೆಟ್ ಮಾಡಿದರೆ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

### ಹಂತ 4: Olive ಕಮಾಂಡ್‌ಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ 

ನಿಮ್ಮ Azure AI Compute Instance ನಲ್ಲಿ VS Code ನಲ್ಲಿ ಟರ್ಮಿನಲ್ ವಿಂಡೋ ತೆರೆಯಿರಿ (ಗುಟ್ಟು: **Ctrl+J**) ಮತ್ತು `olive-ai` conda ಪರಿಸರ ಸಕ್ರಿಯವಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:

```bash
conda activate olive-ai
```

ಆಗಲಾದ ಬಳಿಕ, ಕೆಳತಮ್ಮ Olive ಕಮಾಂಡ್‌ಗಳನ್ನು ಕಮಾಂಡ್ ಲೈನ್‌ನಲ್ಲಿ 실행ಿಸಿ.

1. **ಡೇಟಾ ಪರಿಶೀಲಿಸಿ:** ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನೀವುPhi-3.5-Mini ಮಾದರಿಯನ್ನು ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡಿ ಅದು ಪ್ರಯಾಣ ಸಂಬಂಧಿತ ಪ್ರಶ್ನೆಗಳಿಗೆ ವಿಶೇಷ ಜವಾಬ್ದಾರಿ ನೀಡುವಂತೆ ಮಾಡಲಿದ್ದೀರಿ. ಕೆಳಗಿನ ಕೋಡ್‌ವು ಡೇಟಾಸೆಟ್‌ನ ಮೊದಲ ಕೆಲವು ದಾಖಲೆಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ, ಅವು JSON ಲೈನ್ಸ್ ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಇರುತ್ತವೆ:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **ಮಾದರಿಯನ್ನು ಕ್ವಾಂಟೈಸ್ ಮಾಡಿ:** ತರಬೇತಿ ಆರಂಭಿಸುವ ಮೊದಲು, ಕೆಳಗಿನ ಕಮಾಂಡ್ ಬಳಸಿ Active Aware Quantization (AWQ) ಎಂಬ ತಂತ್ರವನ್ನು ಬಳಸಿಕೊಂಡು ಮೊದಲು ಕ್ವಾಂಟೈಸೇಶನ್ ಮಾಡುತ್ತಾರೆ +++https://arxiv.org/abs/2306.00978+++. AWQ ಅನ್ನು ಬಳಸುವುದರಿಂದ ಮಾದರಿಯ ವೈಟ್‌ಗಳನ್ನು ಇನ್ಫರೆನ್ಸ್ ಸಂದರ್ಭದಲ್ಲಿ生成 ಆಗುವ ಆಕ್ಟಿವೇಶನ್‌ಗಳನ್ನು ಪರಿಗಣಿಸಿ ಕ್ವಾಂಟೈಸ್ ಮಾಡಲಾಗುತ್ತದೆ. ಇದರಿಂದ ಕ್ವಾಂಟೈಸೇಶನ್ ಪ್ರಕ್ರಿಯೆ ಆಕ್ಟಿವೇಶನ್‌ಗಳಲ್ಲಿನ ವಾಸ್ತವಿಕ ಡೇಟಾ ವಿತರಣೆAccount ಗೆ ಗಮನ ಹರಿಸುತ್ತದೆ, ಇದರಿಂದ ಪರಂಪರागत ವೈಟ್ ಕ್ವಾಂಟೈಸೇಶನ್ രീതಿಗಳಿಗಿಂತ ಮಾದರಿ ಶುದ್ದತೆಯ ರಕ್ಷಣೆ ಉತ್ತಮವಾಗುತ್ತದೆ.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    ಇದು ಪೂರ್ಣಗೊಳ್ಳಲು **~8mins** ಬೇಕಾಗುತ್ತದೆ, ಮತ್ತು ಇದು ಮಾದರಿಯ ಗಾತ್ರವನ್ನು ಸುಮಾರು **~7.5GB ರಿಂದ ~2.5GB** ತಗ್ಗಿಸುತ್ತದೆ.
   
   ಈ ಪ್ರಯೋಗಶಾಲೆಯಲ್ಲಿ, ನಾವು Hugging Face ನಿಂದ ಮಾದರಿಗಳನ್ನು ಇನ್ಪುಟ್ ಮಾಡುವ ವಿಧಾನವನ್ನು ತೋರಿಸುತ್ತಿದ್ದೇವೆ (ಉದಾಹರಣೆಗಾಗಿ: `microsoft/Phi-3.5-mini-instruct`). ಆದಾಗ್ಯೂ, Olive ಮೂಲಕ ನೀವು Azure AI ಕ್ಯಾಟಲೋಗ್ನಿಂದ ಮಾದರಿಗಳನ್ನು ಇನ್ಪುಟ್ ಮಾಡಬಹುದು — ಇದಕ್ಕಾಗಿ `model_name_or_path` ಆರ್ಗುಮೆಂಟ್ ಅನ್ನು Azure AI ಐಟಂ ID (ಉದಾಹರಣೆ:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) ಗೆ ಅಪ್ಡೇಟ್ ಮಾಡಿ. 

1. **ಮಾದರಿಯನ್ನು ತರಬೇತು ಮಾಡಿ:** ಮುಂದಿನ ಹಂತದಲ್ಲಿ, `olive finetune` ಕಮಾಂಡ್ ಕ್ವಾಂಟೈಜ್ ಮಾಡಿದ ಮಾದರಿಯನ್ನು ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡುತ್ತದೆ. ಕ್ವಾಂಟೈಸೇಶನ್ ಅನ್ನು ಫೈನ್-ಟ್ಯೂನಿನ ಮೊದಲು ಮಾಡುವುದು ನಂತರ ಮಾಡಲು ಭರತಾದರೆ ಹೆಚ್ಚು ಸರಿ ಆಗುತ್ತದೆ, ಏಕೆಂದರೆ ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಪ್ರಕ್ರಿಯೆ ಕ್ವಾಂಟೈಸೇಶನ್‌ನಿಂದ ಉಂಟಾದ ಕೆಲ ನಷ್ಟವನ್ನು ಪೂರೈಸುತ್ತದೆ.
    
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
    
    ಫೈನ್-ಟ್ಯೂನಿಂಗ್ (100 ಸ್ಟೆಪ್ಸ್‌ಗಳೊಂದಿಗೆ) ಪೂರ್ಣಗೊಳ್ಳಲು **~6mins** ಬೇಕಾಗುತ್ತದೆ.

1. **ಆಪ್ಟಿಮೈಸ್ ಮಾಡಿ:** ಮಾದರಿ ತರಬೇತ್ತುಗೊಂಡ ನಂತರ, ನೀವು Olive ನ `auto-opt` ಕಮಾಂಡ್ ಬಳಸಿ ಮಾದರಿಯನ್ನು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುತ್ತೀರಿ, ಇದು ONNX ಗ್ರಾಫ್ ಅನ್ನು ಕ್ಯಾಪ್ಚರ್ ಮಾಡಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅನೇಕ ಆಪ್ಟಿಮೈಜೆಷನ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ – ಮಾದರಿಯನ್ನು ಸಂಕುಚಿಸಿ ಮತ್ತು ಫ್ಯೂಶನ್ ಮಾಡಿ CPU ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸುಧಾರಿಸುವುದಕ್ಕೆ. ಗಮನಿಸಿ, ನೀವು `--device` ಮತ್ತು `--provider` ಆರ್ಗುಮೆಂಟ್‌ಗಳನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡುವ ಮೂಲಕ NPU ಅಥವಾ GPU ಇತ್ಯಾದಿ ಇತರ ಸಾಧನಗಳಿಗಾಗಿ ಸಹ ಆಪ್ಟಿಮೈಸ್ ಮಾಡಬಹುದು — ಆದರೆ ಈ ಪ್ರಯೋಗಶಾಲೆಯ ಉದ್ದೇಶಕ್ಕಾಗಿ ನಾವು CPU ನ್ನೇ ಬಳಸುತ್ತೇವೆ.

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
    
    ಆಪ್ಟಿಮೈಜೇಶನ್ ಪೂರ್ಣಗೊಳ್ಳಲು **~5mins** ಬೇಕಾಗುತ್ತದೆ.

### ಹಂತ 5: ಮಾದರಿ ಇನ್ಫರೆನ್ಸ್ ತ್ವರಿತ ಪರೀಕ್ಷೆ

ಮಾದರಿಯ ಇನ್ಫರೆನ್ಸಿಂಗ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಲು, ನಿಮ್ಮ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ **app.py** ಎಂಬ Python ಫೈಲ್ ರಚಿಸಿ ಮತ್ತು ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಕಾಪಿ-ಅನುಸೃತಿಯಾಗಿ ಅಂಟಿಸಿ:

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

ಕೋಡ್ ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಲು:

```bash
python app.py
```

### ಹಂತ 6: ಮಾದರಿಯನ್ನು Azure AI ಗೆ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ

ಮಾದರಿಯನ್ನು Azure AI ಮಾದರಿ ರೆಪೊಸಿಟರಿಗೆ ಅಪ್‌ಲೋಡ್ ಮಾಡಿದರೆ, ಅದು ನಿಮ್ಮ ಅಭಿವೃದ್ಧಿ ತಂಡದ ಇತರೆ ಸದಸ್ಯರೊಡನೆ ಹಂಚಿಕೊಳ್ಳಬಹುದಾಗಿದ್ದು ಮತ್ತು ಮಾದರಿಯ ವರ್ಸನ್ ನಿಯಂತ್ರಣವನ್ನು ಸಹ ನಿರ್ವಹಿಸುತ್ತದೆ. ಮಾದರಿಯನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಲು ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ:

> [!NOTE]
> `{}` ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್‌ಗಳನ್ನು ನಿಮ್ಮ resource group ಮತ್ತು Azure AI Project ಹೆಸರಾದೊಂದಿಗೆ ಅಪ್ಡೇಟ್ ಮಾಡಿ. 

To find your resource group `"resourceGroup"and Azure AI Project name, run the following command 

```
az ml workspace show
```

ಅಥವಾ +++ai.azure.com+++ ಗೆ ಹೋಗಿ ಮತ್ತು **management center** **project** **overview** ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ

`{}` ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್‌ಗಳನ್ನು ನಿಮ್ಮ resource group ಮತ್ತು Azure AI Project ಹೆಸರಿನಿಂದ ಅಪ್ಡೇಟ್ ಮಾಡಿ.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
ನೀವು ನಂತರ ನಿಮ್ಮ ಅಪ್ಲೋಡ್ ಮಾಡಿದ ಮಾದರಿಯನ್ನು ನೋಡಬಹುದು ಮತ್ತು ನಿಮ್ಮ ಮಾದರಿಯನ್ನು https://ml.azure.com/model/list ನಲ್ಲಿ ಡಿಪ್ಲಾಯ್ ಮಾಡಬಹುದು

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಅಸ್ವೀಕರಣ:
ಈ ದಾಖಲೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಆಧಾರಿತ ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸ್ಪಷ್ಟತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆವನ್ನು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗೊಳ್ಳುವಿಕೆಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರಿಯಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->