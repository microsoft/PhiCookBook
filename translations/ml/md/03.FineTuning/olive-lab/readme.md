<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-12-21T22:22:05+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "ml"
}
-->
# ലാബ്. ഡിവൈസിൽ ഇൻഫറന്‍സിനായുള്ള AI മോഡലുകൾ ആപ്റ്റിമൈസ് ചെയ്യുക

## പരിചയം 

> [!IMPORTANT]
> ഈ ലാബിന് അനുബന്ധ ഡ്രൈവർകളും CUDA toolkit (version 12+) ഇൻസ്റ്റാൾ ചെയ്ത **Nvidia A10 അല്ലെങ്കിൽ A100 GPU** ആവശ്യമുണ്ട്.

> [!NOTE]
> ഇത് **35-മിനിറ്റ്** ദൈർഘ്യമുള്ള ഒരു ലാബ് ആണ്, ഇത് OLIVE ഉപയോഗിച്ച് ഡിവൈസിൽ ഇൻഫറന്‍സിനായി മോഡലുകൾ ആപ്റ്റിമൈസ് ചെയ്യുന്നതിനുള്ള പ്രധാന ആശയങ്ങളിലേക്ക് പ്രായോഗിക പരിചയം നൽകും.

## പഠനലക്ഷ്യങ്ങൾ

ഈ ലാബ് തീരുമ്പോൾ, OLIVE ഉപയോഗിച്ച് നിങ്ങൾക്ക് കഴിയും:

- AWQ ക്വാൻടൈസേഷൻ രീതി ഉപയോഗിച്ച് ഒരു AI മോഡൽ ക്വാൻടൈസ് ചെയ്യുക.
- ഒരു പ്രത്യേക ടാസ്കിനായി AI മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യുക.
- ONNX Runtime-ൽ ഫലപ്രദമായ ഡിവൈസ്-ഓൺ ഇൻഫറൻസിനായി LoRA അഡാപ്റ്ററുകൾ (ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡൽ) ജെനറേറ്റ് ചെയ്യുക.

### Olive എന്താണ്

Olive (*O*NNX *live*) ഒരു മോഡൽ ഓപ്റ്റിമൈസേഷൻ ടൂള്കിറ്റാണ്, കൂടെ ഒരു CLI ഉണ്ട്, ഇത് നിങ്ങളെ ONNX runtime +++https://onnxruntime.ai+++ നു വേണ്ടി ഗുണനിലവാരത്തോടും പ്രകടനത്തോടും கூடிய മോഡലുകൾ ഷിപ്പ് ചെയ്യാൻ സഹായിക്കുന്നു.

![ഒലിവ് ഫ്ലോ](../../../../../translated_images/olive-flow.5daf97340275f8b61397e91430ff02724a2547937b352e7fdfc2f669c56dcd35.ml.png)

Olive-ലേക്കുള്ള ഇൻപുട്ട് സാധാരണയായി PyTorch അല്ലെങ്കിൽ Hugging Face മോഡൽ ആണ്, ഔട്ട്പുട്ട് ഒരു ഓപ്റ്റിമൈസ്ഡ് ONNX മോഡലിാണ്, അത് ONNX runtime പ്രവർത്തിക്കുന്ന ഒരു ഡിവൈസിൽ (deployment target) എക്സിക്യൂട്ട് ചെയ്യപ്പെടുന്നു. Olive മോഡലിനെ ഡിപ്ലോയ്മെന്റ് ടാർഗറ്റിന്റെ AI ആക്സിലറേറ്റർ (NPU, GPU, CPU) അനുസരിച്ച് ഓപ്റ്റിമൈസ് ചെയ്യും, ഉദാ: Qualcomm, AMD, Nvidia അല്ലെങ്കിൽ Intel പോലുള്ള ഹാർഡ്വെയർ വെൻഡറുകൾ നൽകുന്ന ആക്സിലറേറ്ററുകൾക്കാണ് ഇത് ലക്ഷ്യമിടുന്നത്.

Olive ഒരു *workflow* പ്രവർത്തിപ്പിക്കുന്നു, ഇത് ക്രമീകരിച്ചുള്ള വ്യക്തിഗത മോഡൽ ഓപ്റ്റിമൈസേഷൻ ടാസ്ക്‌സ് എന്നറിയപ്പെടുന്ന *passes* എന്ന ക്രമം ആണ് — ഉദാഹരണങ്ങളായി passes ൽ model compression, graph capture, quantization, graph optimization എന്നിവ ഉൾപ്പെടുന്നു. ഓരോ pass-ക്കും മികച്ച മെത്രിക്ക്‌സ് (ഉദാ. കൃത്യത, ലേറ്റൻസി) കൈവരിക്കാൻ ട്യൂൺ ചെയ്യാവുന്ന ചില പാരാമീറ്ററുകൾ ഉണ്ടാകുന്നു, ഇവ പ്രത്യേക evaluator-ൽ മൂല്യനിർണയം നടത്തപ്പെടുന്നു. Olive ഓരോ pass-ഉം ഒറ്റയ്ക്ക് അല്ലെങ്കിൽ പാസ്സുകളുടെ ഒരു സെറ്റ് ആയി ഓട്ടോ-ട്യൂൺ ചെയ്യാൻ search algorithm ഉപയോഗിക്കുന്ന ഒരു search strategy പ്രയോഗിക്കുന്നു.

#### Olive-ന്റെ പ്രയോജനങ്ങൾ

- ഗ്രാഫ് ഓപ്റ്റിമൈസേഷൻ, കമ്പ്രഷൻ, ക്വാൻറൈസേഷൻ എന്നിവക്ക് വിവിധ സാങ്കേതിക വിദ്യകൾ കൈകാര്യം ചെയ്യുമ്പോഴുള്ള ശ്രമവും സമയവും കുറക്കുക. നിങ്ങളുടെ ഗുണനിലവാരവും പ്രകടന നിയന്ത്രണങ്ങളും നിർവചിച്ച് Olive automatisch ആയി മികച്ച മോഡൽ കണ്ടെത്തും.
- ക്വാൻറൈസേഷൻ, കമ്പ്രഷൻ, ഗ്രാഫ് ഓപ്റ്റിമൈസേഷൻ, ഫൈൻട്യൂണിംഗ് എന്നിവയിൽ ആധുനിക സാങ്കേതികങ്ങളെ ഉൾക്കൊള്ളുന്ന 40+ ബിൽറ്റ്-ഇൻ മോഡൽ ഓപ്റ്റിമൈസേഷൻ ഘടകങ്ങൾ.
- സാധാരണ മോഡൽ ഓപ്റ്റിമൈസേഷൻ ടാസ്കുകള്ക്കുള്ള എളുപ്പത്തിൽ ഉപയോഗിക്കാവുന്ന CLI. ഉദാഹരണത്തിന്, olive quantize, olive auto-opt, olive finetune.
- മോഡൽ പാക്കേജിംഗ് ಮತ್ತು ഡെപ്ലോയ്‌മെന്റ് ഉൾപ്പെടുത്തിയിട്ടുണ്ട്.
- **മൾട്ടി LoRA സര്‍വിങ്ങിന്** മോഡലുകൾ ജനറേറ്റ് ചെയ്യുന്നതിന് പിന്തുണ.
- YAML/JSON ഉപയോഗിച്ച് വർക്ക്‌ഫ്ലോകൾ നിർമ്മിച്ച് മോഡൽ ഓപ്റ്റിമൈസേഷൻ ಮತ್ತು ഡെപ്ലോയ്‌മെന്റ് ടാസ്കുകൾ ഓർക്കസ്ട്രേറ്റ് ചെയ്യുക.
- **Hugging Face**യും **Azure AI**യും ഇന്റഗ്രേഷനുകൾ.
- ചെലവ് ലഘൂകരിക്കാൻ ബിൽറ്റ്-ഇൻ **caching** മെക്കാനിസം.

## ലാബ് നിർദ്ദേശങ്ങൾ
> [!NOTE]
> ദയവായി ഉറപ്പാക്കുക നിങ്ങൾക്ക് നിങ്ങളുടെ Azure AI Hub, Project എന്നിവ പ്രൊവിഷൻ ചെയ്‌തിട്ടുണ്ടെന്ന് കൂടാതെ Lab 1 അനുസരിച്ച് നിങ്ങളുടെ A100 compute സജ്ജമാക്കിയിട്ടുണ്ടെന്ന്.

### Step 0: Connect to your Azure AI Compute

നിങ്ങൾ **VS Code**-ൽ ഉള്ള remote ഫീച്ചർ ഉപയോഗിച്ച് Azure AI compute-hez കണക്റ്റുചെയ്യേണ്ടതാണ്.

1. നിങ്ങളുടെ **VS Code** ഡെസ്ക്ടോപ്പ് ആപ്ലിക്കേഷൻ തുറക്കുക:
1. **command palette** തുറക്കാൻ **Shift+Ctrl+P** ഉപയോഗിക്കുക
1. command palette-ൽ **AzureML - remote: Connect to compute instance in New Window** തിരയുക.
1. Compute-നുമായി കണക്റ്റ് ചെയ്യാൻ സ്ക്രീനിൽ ഉള്ള നിർദ്ദേശങ്ങൾ പിന്തുടരുക. ഇതിൽ നിങ്ങളുടെ Azure Subscription, Resource Group, Project, Lab 1-ൽ സജ്ജീകരിച്ച Compute നാമം എന്നിവ തിരഞ്ഞെടുക്കലും ഉൾപ്പെടും.
1. നിങ്ങൾ Azure ML Compute നോട് കണക്റ്റ് ചെയ്‌ത ശേഷം ഇത് **Visual Code-ന്റെ താഴെ ഇടത്** ഭാഗത്ത് `><Azure ML: Compute Name` എന്ന രൂപത്തിൽ കാണിക്കും

### Step 1: Clone this repo

VS Code-ൽ, **Ctrl+J** ഉപയോഗിച്ച് പുതിയ ടെർമിനൽ തുറന്ന് ഈ റിപ്പോ ക്ലോൺ ചെയ്യാം:

In the terminal you should see the prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
റിപ്പോസിറ്ററി ക്ലോൺ ചെയ്യുക 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Step 2: Open Folder in VS Code

നിലവിലെ ഫോൾഡറിൽ VS Code തുറക്കാൻ ടرمينലിൽ താഴെയുള്ള കമാൻഡ് 실행 ചെയ്യുക, ഇത് ഒരു പുതിയ വിൻഡോ തുറക്കും:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

വികല്പമായി, **File** > **Open Folder** തിരഞ്ഞെടുക്കുകയും ഫോൾഡർ തുറക്കാം. 

### Step 3: Dependencies

നിങ്ങളുടെ Azure AI Compute Instance-ൽ VS Code-ൽ ഒരു ടെർമിനൽ വിൻഡോ തുറക്കുക (സൂചന: **Ctrl+J**) এবং ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ താഴെയുള്ള കമാൻഡുകൾ 실행 ചെയ്യുക:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> എല്ലാ ഡിപ്പൻഡൻസികളും ഇൻസ്റ്റാൾ ചെയ്യാൻ ഏകദേശം ~5 മിനിറ്റ് സമയമെടുക്കും.

ഈ ലാബിൽ നിങ്ങൾ Azure AI മോഡൽ കാറ്റലോഗിൽ മോഡലുകൾ ഡൗൺലോഡ് ചെയ്യുകയും അപ്‌ലോഡ് ചെയ്യുകയും ചെയ്യും. അതിനാൽ മോഡൽ കാറ്റലോഗിൽ പ്രവേശിക്കാൻ, Azure-ലേക്ക് ലോഗിൻ ചെയ്യേണ്ടതാണ്:

```bash
az login
```

> [!NOTE]
> ലോഗിൻ സമയത്ത് നിങ്ങൾക്ക് നിങ്ങളുടെ subscription തിരഞ്ഞെടുക്കാൻ ചോദിക്കും. ഈ ലാബിന് നൽകിയ subscription തിരഞ്ഞെടുക്കാൻ ഉറപ്പാക്കുക.

### Step 4: Execute Olive commands 

VS Code-ൽ നിങ്ങളുടെ Azure AI Compute Instance-ൽ ഒരു ടെർമിനൽ തുറന്ന് `olive-ai` conda environment ആക്ടിവേറ്റ് ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക:

```bash
conda activate olive-ai
```

ഇനിഞ്, താഴെയുള്ള Olive കമാൻഡുകൾ കമാൻഡ് ലൈനിൽ 실행 ചെയ്യുക.

1. **Inspect the data:** ഈ ഉദാഹരണത്തിൽ, Phi-3.5-Mini മോഡൽ യാത്ര സംബന്ധിച്ച ചോദ്യങ്ങൾക്കു പ്രത്യേകമായി പരിശീലിപ്പിക്കാൻ ഫൈൻ-ട്യൂൺ ചെയ്യാൻ പോകുന്നു. താഴെയുള്ള കോഡ് ഡാറ്റാസെറ്റിലെ ആദ്യ കുറച്ച് റെക്കോർഡുകൾ പ്രദർശിപ്പിക്കുന്നു, ഇവ JSON lines ഫോർമാറ്റിലാണ്:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Quantize the model:** പരിശീലനത്തിന് മുമ്പ്, നിങ്ങൾ AWQ (Active Aware Quantization) എന്ന സാങ്കേതികവിദ്യ ഉപയോഗിച്ച് മോഡൽ ക്വാൻടൈസ് ചെയ്യുവാൻ താഴെയുള്ള കമാൻഡ് ഉപയോഗിക്കും +++https://arxiv.org/abs/2306.00978+++. AWQ ഇൻഫറൻസിന് സമയത്ത് ഉണ്ടാകുന്ന ആക്റ്റിവേഷനുകൾ പരിഗണിച്ചാണ് മോഡൽവെയ്റ്റുകൾ ക്വാൻടൈസ് ചെയ്യുന്നത്. അതായത് ക്വാൻടൈസേഷൻ പ്രക്രിയ ആക്റ്റിവേഷനുകളുടെ യഥാർഥ ഡാറ്റ വിതരണത്തെ പരിഗണിക്കുന്നതിനാൽ പരമ്പരാഗത വെയ്റ്റ് ക്വാൻടൈസേഷൻ രീതികളേക്കാൾ മോഡൽ കൃത്യത നിലനിർത്താൻ സഹായിക്കുന്നു.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ ക്വാൻടൈസേഷൻ പൂർത്തിയാക്കാൻ ഏകദേശം **~8 മിനിറ്റ്** എടുത്തേക്കാം, ഇത് മോഡൽ സൈസ് ഏകദേശം ~7.5GB-ൽ നിന്ന് ~2.5GBവരെ കുറയ്‌ക്കും.
   
   ഈ ലാബിൽ ഞങ്ങൾ Hugging Face-ൽ നിന്നുള്ള മോഡലുകൾ എങ്ങനെ ഇൻപുട്ട് ചെയ്യാമെന്ന് കാണിക്കുന്നു (ഉദാഹരണം: `microsoft/Phi-3.5-mini-instruct`). എന്നിരുന്നാലും, Olive-ൽ `model_name_or_path` argument-നെ Azure AI asset ID ആയി അപ്ഡേറ്റ് ചെയ്ത് Azure AI കാറ്റലോഗിൽ നിന്നുള്ള മോഡലുകൾ ഇൻപുട്ട് ചെയ്യാനും കഴിയും (ഉദാഹരണം: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** തുടർന്ന്, `olive finetune` കമാൻഡ് ക്വാൻടൈസ് ചെയ്ത മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യും. ക്വാൻടൈസേഷൻ ചെയ്തത് ഫൈൻ-ട്യൂണിനുമുമ്പ് (*മുൻപ്*) ചെയ്യുന്നത് ഫൈൻ-ട്യൂണിങ്ങ് പ്രക്രിയ കൊണ്ട് ക്വാൻടൈസേഷനിൽ ഉണ്ടായ കുറവ് പുനഃസ്ഥാപിക്കപ്പെട്ടത് കൊണ്ട് മെച്ചപ്പെട്ട കൃത്യത നൽകും.
    
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
    
    Fine-tuning (100 steps ഉൾപ്പെടെ) പൂര്‍ത്തിയാക്കാൻ ഏകദേശം **~6 മിനിറ്റ്** എടുക്കും.

1. **Optimize:** മോഡൽ ട്രെയിൻ ചെയ്‌തതിനുശേഷം, Olive-യുടെ `auto-opt` കമാൻഡ് ഉപയോഗിച്ച് മോഡൽ optimize ചെയ്യുക; ഇത് ONNX ഗ്രാഫ് capture ചെയ്ത് മോഡൽ ചുരുക്കി ഫ്യൂഷനുകൾ പോലുള്ള നിരവധി ഓപ്റ്റിമൈസേഷനുകൾ സ്വയം നടപ്പാക്കും، CPU-നുള്ള പ്രകടനം മെച്ചപ്പെടുത്താൻ. ശ്രദ്ധിക്കേണ്ടത്, `--device` және `--provider` arguments ആണ് അപ്ഡേറ്റ് ചെയ്യുക വഴി നിങ്ങൾ NPU അല്ലെങ്കിൽ GPU പോലുള്ള മറ്റു ഡിവൈസുകൾക്കും optimize ചെയ്യാൻ കഴിയും — എന്നാൽ ഈ ലാബിന്റെ ആവശ്യകത ക്കായി ഞങ്ങൾ CPU ഉപയോഗിക്കും.
 
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
    
    ഓപ്റ്റിമൈസേഷൻ പൂർത്തിയാക്കാൻ ഏകദേശം **~5 മിനിറ്റ്** എടുക്കും.

### Step 5: Model inference quick test

മോഡൽ ഇൻഫറൻസും പരിശോധിക്കാൻ, നിങ്ങളുടെ ഫോൾഡറിൽ **app.py** എന്ന പേരിൽ ഒരു Python ഫയൽ സൃഷ്ടിച്ച് താഴെയുള്ള കോഡ് പകർത്തി നടത്തുക:

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

മോഡൽ Azure AI മോഡൽ റിപോസിറ്ററിയിലേയ്ക്ക് അപ്‌ലോഡ് ചെയ്യുന്നത് നിങ്ങളുടെ ഡവലപ്പ്മെന്റ് ടീമിലെ മറ്റ് അംഗങ്ങളോടൊപ്പം മോഡൽ ഷെയർ ചെയ്യാവുന്നതാക്കുകയും മോഡലിന്റെ വേർഷൻ കൺട്രോൾ കൈകാര്യം ചെയ്യുന്നതും ആണ്. മോഡൽ അപ്‌ലോഡ് ചെയ്യാൻ താഴെയുള്ള കമാൻഡ് 실행 ചെയ്യുക:

> [!NOTE]
> `{}` പ്ലേസ്ഹോൾഡറുകൾ നിങ്ങളുടെ resource group നാമത്തോടും Azure AI Project നാമത്തോടും അപ്ഡേറ്റ് ചെയ്യുക. 

നിങ്ങളുടെ resource group `"resourceGroup"` and Azure AI Project നാമം കണ്ടെത്താൻ, താഴെയുള്ള കമാൻഡ് 실행 ചെയ്യുക 

```
az ml workspace show
```

അല്ലെങ്കിൽ +++ai.azure.com+++-ൽ പോയി **management center** **project** **overview** തിരഞ്ഞെടുക്കുക

`{}` പ്ലേസ്ഹോൾഡറുകൾ നിങ്ങളുടെ resource group നാമത്തോടും Azure AI Project നാമത്തോടും അപ്ഡേറ്റ് ചെയ്യുക.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
തുടർന്ന് നിങ്ങൾ അപ്‌ലോഡ് ചെയ്ത മോഡൽ കാണാനും നിങ്ങളുടെ മോഡൽ https://ml.azure.com/model/list-ൽ ഡിപ്ലോയു ചെയ്യാനും കഴിയും.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്ലെയിമർ:
ഈ രേഖ AI വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിക്കുന്നതാണെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിഴവുകളും അസമത്വങ്ങളും ഉണ്ടായിരിക്കാമെന്നതു ദയവായി അറിയിക്കുക. മാതൃഭാഷയിലുള്ള ഒറിജിനൽ ഡോക്യുമെന്റ് ആണ് അധികാരപരമായി പ്രാമാണികമെന്നായി കരുതേണ്ടത്. നിർണായക വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ചതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കുമായി ഞങ്ങൾ ഉത്തരവാദിത്തം ഏറ്റെടുക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->