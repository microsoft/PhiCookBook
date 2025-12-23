<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-12-21T16:44:53+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "ml"
}
-->
# ലാബ്. ഓൺ-ഡിവൈസിൽ ഇൻഫറൻസിന് AI മോഡലുകൾ ഓപ്റ്റിമൈസ് ചെയ്യുക

## പരിചയം 

> [!IMPORTANT]
> ഈ ലാബിന് അനുബന്ധ ഡ്രൈവർകളും CUDA ടൂൾകിറ്റും (പതിപ്പ് 12+) സ്ഥാപിച്ച **Nvidia A10 അല്ലെങ്കിൽ A100 GPU** ആവശ്യമുണ്ട്.

> [!NOTE]
> ഇത് **35-മിനിറ്റ്** ദൈർഘ്യമുള്ള ലാബാണ്, ഇത് OLIVE ഉപയോഗിച്ച് ഓൺ-ഡിവൈസ് ഇൻഫറൻസിനായുള്ള മോഡൽ ഓപ്റ്റിമൈസേഷനിന്റെ негізгі ആശയങ്ങളിൽ പ്രായോഗിക പരിചയം നൽകും.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ ലാബിന്റെ അവസാനം നിങ്ങൾ OLIVE ഉപയോഗിച്ച് ചെയ്യാൻ കഴിയും:

- AWQ അളക്കൽ രീതിയുടെ ഉപയോഗത്തോടെ ഒരു AI മോഡൽ ക്വാന്തൈസ് ചെയ്യുക.
- ഒരു പ്രത്യേക ജോലി కోసం AI മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യുക.
- ONNX റൺടൈമിൽ തയ്യൽ-പ്രവർത്തനശേഷിയുള്ള ഓൺ-ഡിവൈസ് ഇൻഫറൻസിനായി LoRA അഡാപ്റ്ററുകൾ (ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡൽ) ജനറേറ്റ് ചെയ്യുക.

### Olive എന്താണ്

Olive (*O*NNX *live*) ഒരു മോഡൽ ഓപ്റ്റിമൈസേഷൻ ടൂള്കിറ്റ് ആണ്, കൂടാതെ അതിനൊപ്പം വരുന്ന CLI കൂടിയാണ്, ഇത് ONNX runtime +++https://onnxruntime.ai+++ വേണ്ടി ഗുണനിലവാരവും പ്രകടനവും ഉറപ്പാക്കിയ മോഡലുകൾ ഷിപ്പ് ചെയ്യാൻ സഹായിക്കുന്നു.

![ഓലൈവ് ഫ്ലോ](../../../../../translated_images/olive-flow.a47985655a756dcba73521511ea42eef359509a3a33cbd4b9ac04ba433287b80.ml.png)

Olive-ലേക്കുള്ള ഇൻപുട്ട് സാധാരണയായി PyTorch അല്ലെങ്കിൽ Hugging Face മോഡൽ ആയിരിക്കും, ഔട്ട്പുട്ട് ഒരു ഓപ്റ്റിമൈസ്ഡ് ONNX മോഡൽ ആകുകയും അത് ONNX runtime ഓടുന്ന ഡിവൈസിൽ (ഡിപ്ളോയ്മെന്റ് ലക്ഷ്യം) എക്സിക്യൂട്ട് ചെയ്യപ്പെടുകയും ചെയ്യുന്നു. Olive ഡിപ்ளോയ്മെന്റ് ടാർഗറ്റിന്റെ AI ആക്സലറേറ്റർ (NPU, GPU, CPU) എന്നതനുസരിച്ച് മോഡൽ ഓപ്റ്റിമൈസ് ചെയ്യും, അതുവഴി Qualcomm, AMD, Nvidia അല്ലെങ്കിൽ Intel പോലുള്ള ഹാർഡ്‌വെയർ വൃന്ദങ്ങൾ പ്രദാനം ചെയ്യുന്നു.

Olive ഒരു *workflow* എക്സിക്യൂട്ട് ചെയ്യുന്നു, ഇത് *passes* എന്നു വിളിക്കുന്ന വ്യക്തിഗത മോഡൽ ഓപ്റ്റിമൈസേഷൻ ടാസ്കുകളുടെ ക്രമീകരിച്ച ശൃംഖലയാണ് — ഉദാഹരണമായി passes ൽ മോഡൽ കംപ്രഷൻ, ഗ്രാഫ് ക്യാച്ചർ, ക്വാന്തൈസേഷൻ, ഗ്രാഫ് ഓപ്റ്റിമൈസേഷൻ എന്നിവ ഉൾപ്പെടുന്നു. ഓരോ പാസിനും മികച്ച മീട്രിക്കുകൾ (ഉദാഹരണം: കൃത്യതയും ലാറ്റൻസിയും) നേടാൻ ട്യൂൺ ചെയ്യാവുന്ന പരാമീറ്ററുകൾ ഉണ്ടായി വരും. Olive, ഓരോ പാസും ഒറ്റയ്ക്ക് അല്ലെങ്കിൽ പാസുകളുടെ സെറ്റായി ഓട്ടോ-ട്യൂൺ ചെയ്യുന്നതിനുള്ള ഒരു സെർച്ച് ആൽഗോറിതം ഉപയോഗിച്ച് ഒരു സെർച്ച് നയം പ്രയോഗിക്കുന്നു.

#### Olive ഉപയോഗിക്കുന്ന ഗുണങ്ങൾ

- **പരീക്ഷണ-തെറ്റു രീതികളിലൂടെ മാനുവൽ പരീക്ഷണങ്ങളിൽ നിന്നുള്ള നിരാശയും സമയവും കുറയ്ക്കുക.** ഗ്രാഫ് ഓപ്റ്റിമൈസേഷൻ, കംപ്രഷൻ, ക്വാന്തൈസേഷൻ എന്നിവയ്ക്ക് വിവിധ տեխնികുകൾ പരീക്ഷിക്കുന്ന ബുദ്ധിമുട്ട് ഒഴിവാക്കി നിങ്ങളുടെ ഗുണനിലവാരവും പ്രകടനപരിധികളും നിർദ്ദിഷ്ടമാക്കി Olive മികച്ച മോഡൽ അതിനനുസരിച്ച് സ്വയം കണ്ടെത്താൻ അനുവദിക്കുക.
- **40+ ബിൽറ്റ്-ഇൻ മോഡൽ ഓപ്റ്റിമൈസേഷൻ ഘടകങ്ങൾ** ക്വാന്തൈസേഷൻ, കംപ്രഷൻ, ഗ്രാഫ് ഓപ്റ്റിമൈസേഷൻ, ഫൈൻറ്റ്യൂണിങ്ങ് എന്നിവയിലെ ഏറ്റവും പുതിയ സാങ്കേതിക വിദ്യകൾ കാര്യാർത്ഥമാക്കുന്നു.
- സാധാരണ മോഡൽ ഓപ്റ്റിമൈസേഷൻ ടാസ്കുകൾക്കുള്ള **സൗകര്യപ്രദമായ CLI**. ഉദാഹരണത്തിന്: olive quantize, olive auto-opt, olive finetune.
- മോഡൽ പാക്കേജിംഗ് এবং ഡിപ്ലോയ്‌മെന്റ് ഉൾക്കൊള്ളിതുണ്ട്.
- **മൾട്ടി LoRA സർവിങ്** ജനറേറ്റ് ചെയ്യുന്നതിന് പിന്തുണ.
- YAML/JSON ഉപയോഗിച്ച് വർക്ക്‌ഫ്ലോകൾ നിർമ്മിച്ച് മോഡൽ ഓപ്റ്റിമൈസേഷൻ և ഡിപ്ലോയ്മെന്റ് ടാസ്കുകൾ ഓർക്കസ്ട്രേറ്റ് ചെയ്യുക.
- **Hugging Face** மற்றும் **Azure AI** ഇന്റഗ്രേഷൻ.
- ചെലവ് ലഘൂകരിക്കാൻ സഹായിക്കുന്ന ബിൽറ്റ്-ഇൻ **ക്യാഷിംഗ്** മെക്കനിസം.

## ലാബ് നിർദ്ദേശങ്ങൾ
> [!NOTE]
> කරුණාකර നിങ്ങൾ നിങ്ങളുടെ Azure AI Hub, പ്രൊജക്റ്റ് പ്രൊവിഷൻ ചെയ്തിട്ടുണ്ടെന്നും Lab 1 അനുസരിച്ച് A100.compute സെറ്റ് ചെയ്തിട്ടുണ്ടെന്നും ഉറപ്പാക്കുക.

### ഘട്ടം 0: നിങ്ങളുടെ Azure AI Compute-നോട് ബന്ധിപ്പിക്കുക

നിങ്ങൾ **VS Code**-ന്റെ റിമോട്ട് ഫീച്ചർ ഉപയോഗിച്ച് Azure AI compute-നോട് ബന്ധിപ്പിക്കുകയാകും.

1. നിങ്ങളുടെ **VS Code** ഡെസ്ക്ടോപ് അപ്ലിക്കേഷൻ തുറക്കുക:
1. **Shift+Ctrl+P** ഉപയോഗിച്ച് **command palette** തുറക്കുക
1. കമാൻഡ് പല്ലറ്റിൽ **AzureML - remote: Connect to compute instance in New Window** തിരയുക.
1. Compute-നോട് ബന്ധിപ്പിക്കാൻ സ്ക്രീനിലെ നിർദ്ദേശങ്ങൾ പാലിക്കുക. ഇതിൽ നിങ്ങളുടെ Azure Subscription, Resource Group, Project, Lab 1-ൽ നിങ്ങൾ സജ്ജമാക്കിയ Compute നാമം എന്നിവ തിരഞ്ഞെടുക്കേണ്ടി വരും.
1. നിങ്ങൾ Azure ML Compute നോട് കണക്ട് ചെയ്തപ്പോൾ ഇത് **Visual Code**-ന്റെ വലത്തുഭാഗം താഴെ `><Azure ML: Compute Name` എന്ന നിലയിൽ കാണിക്കും

### Step 1: Clone this repo

VS Code-ൽ **Ctrl+J** ഉപയോഗിച്ച് പുതിയ ഒരു ടെർമിനൽ തുറന്ന് ഈ റെപ്പോ ക്ലോൺ ചെയ്യാം:

In the terminal you should see the prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Clone the solution 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Step 2: Open Folder in VS Code

ഈ അനുയോജ്യമായ ഫോൾഡറിൽ VS Code തുറക്കുന്നതിന് ടെർമിനലിൽ താഴെ കാണുന്ന കമാൻഡ് എക്സിക്യൂട്ട് ചെയ്യുക, ഇത് പുതിയ ഒരു വിൻഡോ തുറക്കും:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

അല്ലെങ്കിൽ, **File** > **Open Folder** തിരഞ്ഞെടുക്കിക്കൊണ്ട് ഫോൾഡർ തുറക്കാം. 

### Step 3: Dependencies

നിങ്ങളുടെ Azure AI Compute ഇൻസ്റ്റൻസിൽ VS Code-ൽ ഒരു ടെർമിനൽ വിൻഡോ തുറന്ന് (സൂചന: **Ctrl+J**) അനാവശ്യ ആശ്രിതത്വങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ താഴെ കാണുന്ന കമാൻഡുകൾ اجرا ചെയ്യുക:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> എല്ലാ ആശ്രിതത്വങ്ങളും ഇൻസ്റ്റാൾ ചെയ്യാൻ ഏകദേശം ~5mins വേണ്ടി വരാം.

ഈ ലാബിൽ നിങ്ങൾ മോഡലുകൾ Azure AI മോഡൽ കാറ്റലോഗിലേക്ക് ഡൗൺലോഡ് ചെയ്ത് അപ്‌ലോഡ് ചെയ്യാൻ പോകുന്നു. മോഡൽ കാറ്റലോഗ് ആക്സസ് ചെയ്യാൻ Azure-ലേക്ക് ലോഗിൻ ചെയ്യേണ്ടതുണ്ട്:

```bash
az login
```

> [!NOTE]
> ലോഗിൻ സമയത്ത് നിങ്ങളുടെ സബ്സ്ക്രിപ്ഷൻ തിരഞ്ഞെടുക്കാൻ പറയപ്പെടും. ലാബിനായി നൽകിയ സബ്സ്ക്രിപ്ഷൻ സെറ്റ് ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക.

### Step 4: Execute Olive commands 

നിങ്ങളുടെ Azure AI Compute ഇൻസ്റ്റൻസിൽ VS Code-ൽ ഒരു ടെർമിനൽ വിൻഡോ തുറന്ന് (സൂചന: **Ctrl+J**) `olive-ai` conda environment സജീവമാണെന്ന് ഉറപ്പാക്കുക:

```bash
conda activate olive-ai
```

തുടർന്ന്, കമാൻഡ് ലൈൻ വഴിയാണ് താഴെ കാണുന്ന Olive കമാൻഡുകൾ എക്സിക്യൂട്ട് ചെയ്യേണ്ടത്.

1. **Inspect the data:** ഈ ഉദാഹരണത്തിൽ, യാത്രാവിവരങ്ങളുമായി ബന്ധപ്പെട്ട ചോദ്യങ്ങൾക്ക് പ്രത്യേക പരിഭാഷ ലഭ്യമാക്കാൻ Phi-3.5-Mini മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യാൻ പോകുന്നു. താഴെയുള്ള കോഡ് dataset-ന്റെ ആദ്യ нескольких റെക്കോർഡുകൾ (JSON lines ഫോർമാറ്റിൽ)_display ചെയ്യുന്നു:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Quantize the model:** മോഡൽ ട്രെയിനിംഗ് തുടങ്ങുന്നതിന് മുമ്പ്, താഴെ കാണുന്ന കമാൻഡ് ഉപയോഗിച്ച് Active Aware Quantization (AWQ) എന്ന സാങ്കേതിക വിദ്യ ഉപയോഗിച്ച് ക്വാന്തൈസ് ചെയ്യുക +++https://arxiv.org/abs/2306.00978+++. AWQ ഇൻഫറൻസ് സമയത്ത് ഉത്പാദിപ്പിക്കപ്പെടുന്ന ആക്ടിവേഷനുകൾ പരിഗണിച്ച് മോഡലിന്റെ വെയ്റ്റുകൾ ക്വാന്തൈസ് ചെയ്യുന്നു. അതിനാൽ ക്വാന്തൈസേഷൻ പ്രക്രിയ ആക്ടിവേഷനുകളിലെ യഥാർത്ഥ ഡാറ്റ വിതരണത്തെ പ്രതിബിംബിപ്പിക്കുന്നതിനാൽ പരമ്പരാഗത വെയ്റ്റ് ക്വാന്തൈസേഷൻ രീതികളേക്കാൾ മോഡൽ കൃത്യത എളുപ്പത്തിൽ സംരക്ഷിക്കുന്നു.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    ഇതിന് പൂർത്തിയാക്കാൻ **~8mins** വേണ്ടിവരും, അത് മോഡൽ സൈസ് ഏകദേശം **7.5GB-ൽ നിന്ന് ~2.5GB** ആയി കുറക്കും.
   
   ഈ ലാബിൽ ഞങ്ങൾ Hugging Face-ിൽ നിന്നുള്ള മോഡലുകൾ നൽകുന്നത് കാണിച്ചുതരുന്നു (ഉദാഹരണം: `microsoft/Phi-3.5-mini-instruct`). എന്നിരുന്നാലും, Olive മുഖേന Azure AI കാറ്റലോഗിൽ നിന്നുള്ള മോഡലുകൾ നൽകാനും സാധ്യമാണ് — അതിനായി `model_name_or_path` ആർഗുമെന്റ് ഒരു Azure AI ആസ്‌സറ്റ് ID ആയി (ഉദാഹരണം:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) അപ്ഡേറ്റ് ചെയ്യുക. 

1. **Train the model:** തുടർന്ന്, ക്വാന്തൈസ്ഡ് മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യാൻ `olive finetune` കമാൻഡ് ഉപയോഗിക്കുന്നു. ക്വാന്തൈസേഷൻ നടത്തുന്നതിന് മുമ്പെ മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യുന്നതിന് പകരം ക്വാന്തൈസ് ചെയ്ത് പിന്നീട് ഫൈൻ-ട്യൂൺ ചെയ്യുന്നത് കൃത്യത മെച്ചപ്പെടുത്തുന്നതിന് നന്നാണ്, കാരണം ഫൈൻ-ട്യൂണിംഗ് പ്രക്രിയ ക്വാന്തൈസേഷനിൽ നിന്നുള്ള കുറവിന്റെ ചില ഭാഗം വീണ്ടെടുക്കും.
    
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
    
    ഫൈൻ-ട്യൂണിങ്ങ് (100 സ്‌റ്റെപ്പുകൾ) പൂർത്തിയാക്കാൻ **~6mins** വേണ്ടി വരും.

1. **Optimize:** മോഡൽ ട്രൈൻ ചെയ്തശേഷം, Olive-യുടെ `auto-opt` കമാൻഡ് ഉപയോഗിച്ച് മോഡൽ ഓപ്റ്റിമൈസ് ചെയ്യുക; ഇത് ONNX ഗ്രാഫ് ക്യാച്ച് ചെയ്ത് CPU-നായി മോഡൽ പ്രകടനം മെച്ചപ്പെടുത്താൻ മോഡൽ കംപ്രെസ് ചെയ്ത് ഫ്യൂഷനുകൾ ഉൾപ്പെടെ പല ഓപ്റ്റിമൈസേഷനുകളും സ്വയമേവ നടത്തും. മറ്റ് ডിവൈസുകൾക്കായും (ഉദാഹരണം: NPU അല്ലെങ്കിൽ GPU) optimize ചെയ്യാൻ `--device` և `--provider` ആർഗുമെന്റുകൾ അപ്ഡേറ്റ് ചെയ്യിക്കാമെങ്കിലും ഈ ലാബിനു വേണ്ടി നാം CPU ഉപയോഗിച്ചാണ് കാണിക്കുന്നത്.

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
    
    ഓപ്റ്റിമൈസേഷൻ പൂർത്തിയാക്കാൻ **~5mins** വേണ്ടിവരും.

### Step 5: Model inference quick test

മോഡലിന്റെ ഇൻഫറൻസ് പരിശോദിക്കാൻ, നിങ്ങളുടെ ഫോൾഡറിൽ **app.py** എന്ന പേരിൽ ഒരു Python ഫയൽ ക്രിയേറ്റ് ചെയ്ത് താഴെയുള്ള കോഡ് കോപ്പി-പേസ്റ്റ് ചെയ്യുക:

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

കോഡ് 실행 ചെയ്യാൻ:

```bash
python app.py
```

### Step 6: Upload model to Azure AI

മോഡൽ Azure AI മോഡൽ റിപ്പോസിറ്ററിയിൽ അപ്‌ലോഡ് ചെയ്യുന്നത് നിങ്ങളുടെ ഡെവൽപ്മെന്റ് ടീമിന്റെ മറ്റ് അംഗങ്ങളുമായി മോഡൽ പങ്കുവെക്കാനായും മോഡലിന്റെ വേർഷൻ നിയന്ത്രണം കൈകാര്യം ചെയ്യാനുമായി സഹായിക്കുകയും ചെയ്യും. മോഡൽ അപ്‌ലോഡ് ചെയ്യാൻ താഴെ കാണുന്ന കമാൻഡ് اجرا ചെയ്യുക:

> [!NOTE]
> `{}` പ്ലേസ്‌ഹോൾഡറുകൾ നിങ്ങളുടെ റിസോഴ്‌സ് ഗ്രൂപ്പിന്റെയും Azure AI പ്രൊജക്ടിന്റെ നാമത്തെയും ഉപയോഗിച്ച് അപ്ഡേറ്റ് ചെയ്യുക. 

നിങ്ങളുടെ റിസോഴ്‌സ് ഗ്രൂപ്പ് `"resourceGroup"and` Azure AI Project നാമം കണ്ടെത്താൻ, താഴെ കാണുന്ന കമാൻഡ് اجرا ചെയ്യുക 

```
az ml workspace show
```

അല്ലെങ്കിൽ +++ai.azure.com+++ സന്ദർശിച്ച് **management center** **project** **overview** തിരഞ്ഞെടുക്കാം

`{}` പ്ലേസ്‌ഹോൾഡറുകൾ നിങ്ങളുടെ റിസോഴ്‌സ് ഗ്രൂപ്പിന്റെ നാമത്തിലും Azure AI Project നാമത്തിലും അപ്ഡേറ്റ് ചെയ്യുക.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
You can then see your uploaded model and deploy your model at https://ml.azure.com/model/list

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അസ്വീകാര്യ പ്രഖ്യാപനം:
ഈ രേഖ AI വിവർത്തന സേവനം Co‑op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വ്യാഖ്യാനിച്ചതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിച്ചുകൊണ്ടിരിക്കുമ്പോഴും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായി വ്യാഖ്യാനിക്കപ്പെടുന്ന ഭാഗങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ടെന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൂലഭാഷയിലുള്ള രേഖ ഇപ്പോഴത്തെ അധികാരപരമായ ഉറവിടമായി പരിഗണിക്കണം. നിർണ്ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യവിഭാഷകൻ വഴി വിവർത്തനം ചെയ്യുന്നത് ശുപാർശിക്കപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ചതിനെ തുടർന്ന് ഉണ്ടായേക്കാവുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->