<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-09T19:09:54+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "my"
}
-->
# Lab. စက်ပစ္စည်းပေါ်တွင် AI မော်ဒယ်များ inference အတွက် အကောင်းဆုံးပြုလုပ်ခြင်း

## နိဒါန်း

> [!IMPORTANT]
> ဤ lab တွင် **Nvidia A10 သို့မဟုတ် A100 GPU** နှင့် ဆက်စပ်သော driver များနှင့် CUDA toolkit (ဗားရှင်း 12+) တပ်ဆင်ထားရန် လိုအပ်ပါသည်။

> [!NOTE]
> ဤ lab သည် **၃၅ မိနစ်** ကြာပြီး OLIVE ကို အသုံးပြု၍ စက်ပစ္စည်းပေါ် inference အတွက် မော်ဒယ်များ အကောင်းဆုံးပြုလုပ်ခြင်း၏ အခြေခံအယူအဆများကို လက်တွေ့ လေ့လာသင်ကြားပေးမည်ဖြစ်သည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤ lab အပြီးတွင် OLIVE ကို အသုံးပြု၍ အောက်ပါအရာများ ပြုလုပ်နိုင်ပါမည်-

- AWQ quantization နည်းလမ်းဖြင့် AI မော်ဒယ်ကို Quantize ပြုလုပ်ခြင်း။
- AI မော်ဒယ်ကို အထူးတာဝန်အတွက် Fine-tune ပြုလုပ်ခြင်း။
- ONNX Runtime ပေါ်တွင် စက်ပစ္စည်းပေါ် inference အတွက် ထိရောက်စွာ အသုံးပြုနိုင်သော LoRA adapters (fine-tuned မော်ဒယ်) များ ဖန်တီးခြင်း။

### Olive ဆိုတာဘာလဲ

Olive (*O*NNX *live*) သည် ONNX runtime +++https://onnxruntime.ai+++ အတွက် မော်ဒယ်များကို အရည်အသွေးနှင့် စွမ်းဆောင်ရည်ကောင်းစွာ ဖြန့်ချိနိုင်ရန် CLI ပါရှိသော မော်ဒယ် အကောင်းဆုံးပြုလုပ်ရေး ကိရိယာတစ်ခုဖြစ်သည်။

![Olive Flow](../../../../../md/03.FineTuning/olive-lab/images/olive-flow.png)

Olive သို့ input အနေဖြင့် ပုံမှန်အားဖြင့် PyTorch သို့မဟုတ် Hugging Face မော်ဒယ်တစ်ခုကို ထည့်သွင်းပြီး output အနေဖြင့် ONNX runtime ဖြင့် စက်ပစ္စည်း (deployment target) ပေါ်တွင် အကောင်အထည်ဖော်နိုင်သော optimized ONNX မော်ဒယ်တစ်ခု ထွက်ရှိသည်။ Olive သည် deployment target ၏ AI accelerator (NPU, GPU, CPU) ကို Qualcomm, AMD, Nvidia သို့မဟုတ် Intel ကဲ့သို့သော hardware vendor များမှ ပံ့ပိုးပေးသည့်အတိုင်း မော်ဒယ်ကို အကောင်းဆုံးပြုလုပ်ပေးသည်။

Olive သည် *workflow* တစ်ခုကို အကောင်အထည်ဖော်သည်။ workflow သည် *passes* ဟုခေါ်သော မော်ဒယ် optimization လုပ်ငန်းစဉ်များ စဉ်ဆက်မပြတ် လုပ်ဆောင်ခြင်းဖြစ်ပြီး ဥပမာ passes များမှာ မော်ဒယ် ဖိအားချခြင်း၊ graph ဖမ်းဆီးခြင်း၊ quantization၊ graph optimization စသည်ဖြစ်သည်။ pass တစ်ခုစီတွင် parameter များရှိပြီး accuracy နှင့် latency ကဲ့သို့သော အကဲဖြတ်သူများမှ တိုင်းတာသည့် metrics များအတွက် အကောင်းဆုံးရလဒ်ရရှိရန် ပြင်ဆင်နိုင်သည်။ Olive သည် search algorithm ကို အသုံးပြု၍ pass တစ်ခုချင်းစီ သို့မဟုတ် pass များစုစုပေါင်းကို အလိုအလျောက် တိုက်ရိုက်ပြင်ဆင်ပေးသည်။

#### Olive ၏ အကျိုးကျေးဇူးများ

- graph optimization, compression နှင့် quantization နည်းလမ်းများကို လက်တွေ့စမ်းသပ်ရာတွင် trial-and-error လုပ်ရခြင်းကြောင့် ဖြစ်ပေါ်နိုင်သော စိတ်ညစ်မှုနှင့် အချိန်ကုန်ဆုံးမှုကို လျော့နည်းစေသည်။ သင့်ရဲ့ အရည်အသွေးနှင့် စွမ်းဆောင်ရည် ကန့်သတ်ချက်များကို သတ်မှတ်ပြီး Olive ကို အကောင်းဆုံး မော်ဒယ်ကို အလိုအလျောက် ရှာဖွေစေပါ။
- quantization, compression, graph optimization နှင့် finetuning အတွက် နောက်ဆုံးပေါ်နည်းပညာများ ပါဝင်သည့် **40+ built-in model optimization components** များ။
- မော်ဒယ် optimization လုပ်ငန်းများအတွက် အသုံးပြုရ လွယ်ကူသော CLI (ဥပမာ- olive quantize, olive auto-opt, olive finetune)။
- မော်ဒယ် ထုပ်ပိုးခြင်းနှင့် ဖြန့်ချိခြင်း ပါဝင်သည်။
- **Multi LoRA serving** အတွက် မော်ဒယ်များ ဖန်တီးပေးနိုင်သည်။
- YAML/JSON အသုံးပြု၍ မော်ဒယ် optimization နှင့် deployment လုပ်ငန်းစဉ်များကို စီမံခန့်ခွဲနိုင်သည်။
- **Hugging Face** နှင့် **Azure AI** ပေါင်းစပ်မှု။
- **ကုန်ကျစရိတ် လျော့ချရန်** built-in **caching** စနစ်။

## Lab လမ်းညွှန်ချက်များ

> [!NOTE]
> Lab 1 အတိုင်း Azure AI Hub နှင့် Project ကို ပြင်ဆင်ပြီး A100 compute ကို စတင်ထားကြောင်း သေချာစေပါ။

### အဆင့် 0: Azure AI Compute နှင့် ချိတ်ဆက်ခြင်း

**VS Code** ၏ remote feature ကို အသုံးပြု၍ Azure AI compute နှင့် ချိတ်ဆက်ပါ။

1. **VS Code** desktop application ကို ဖွင့်ပါ။
2. **Shift+Ctrl+P** ဖြင့် command palette ကို ဖွင့်ပါ။
3. command palette တွင် **AzureML - remote: Connect to compute instance in New Window** ကို ရှာပါ။
4. Azure Subscription, Resource Group, Project နှင့် Lab 1 တွင် သတ်မှတ်ထားသော Compute name ကို ရွေးချယ်ပြီး ချိတ်ဆက်ပါ။
5. ချိတ်ဆက်ပြီးပါက Visual Code ၏ ဘယ်ဘက်အောက်ခြေတွင် `><Azure ML: Compute Name` ဟူ၍ ပြပါမည်။

### အဆင့် 1: Repo ကို Clone ပြုလုပ်ခြင်း

VS Code တွင် **Ctrl+J** ဖြင့် terminal အသစ်ဖွင့်ပြီး repo ကို clone ပြုလုပ်ပါ-

terminal တွင် prompt ကို တွေ့ရပါမည်-

```
azureuser@computername:~/cloudfiles/code$ 
```  
Clone the solution  

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### အဆင့် 2: VS Code တွင် ဖိုလ်ဒါ ဖွင့်ခြင်း

terminal တွင် အောက်ပါ command ကို ရိုက်ထည့်ပါ၊ အသစ်သော window တစ်ခု ဖွင့်မည်-

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

သို့မဟုတ် **File** > **Open Folder** ကို ရွေး၍ ဖိုလ်ဒါကို ဖွင့်နိုင်ပါသည်။

### အဆင့် 3: Dependencies များ ထည့်သွင်းခြင်း

VS Code ၏ Azure AI Compute Instance တွင် terminal (Ctrl+J) ဖွင့်ပြီး အောက်ပါ command များဖြင့် dependencies များ ထည့်သွင်းပါ-

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> dependencies များ ထည့်သွင်းရန် ~၅ မိနစ် ကြာပါမည်။

ဤ lab တွင် မော်ဒယ်များကို Azure AI Model catalog သို့ ဒေါင်းလုပ်နှင့် အပ်လုဒ်လုပ်မည်ဖြစ်သောကြောင့် Azure သို့ login ဝင်ရန် လိုအပ်ပါသည်-

```bash
az login
```

> [!NOTE]
> login အချိန်တွင် subscription ရွေးချယ်ရန် မေးမည်။ lab အတွက် ပေးထားသော subscription ကို သေချာရွေးချယ်ပါ။

### အဆင့် 4: Olive command များ အကောင်အထည်ဖော်ခြင်း

VS Code ၏ Azure AI Compute Instance တွင် terminal ဖွင့်ပြီး `olive-ai` conda environment ကို ဖွင့်ထားပါ-

```bash
conda activate olive-ai
```

ထို့နောက် အောက်ပါ Olive command များကို command line တွင် အကောင်အထည်ဖော်ပါ-

1. **ဒေတာကို စစ်ဆေးခြင်း:** ဤဥပမာတွင် Phi-3.5-Mini မော်ဒယ်ကို ခရီးသွားဆိုင်ရာ မေးခွန်းများကို ဖြေဆိုရာတွင် အထူးပြုရန် fine-tune ပြုလုပ်မည်ဖြစ်သည်။ အောက်ပါ code သည် JSON lines format ဖြင့် ရှိသော ဒေတာ၏ အစောပိုင်း မှတ်တမ်းများကို ပြသသည်-

    ```bash
    head data/data_sample_travel.jsonl
    ```

2. **မော်ဒယ်ကို Quantize ပြုလုပ်ခြင်း:** မော်ဒယ်ကို သင်ကြားမတိုင်မီ Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ နည်းလမ်းဖြင့် quantize ပြုလုပ်မည်။ AWQ သည် inference အတွင်း ထုတ်လုပ်သော activation များကို စဉ်းစားကာ မော်ဒယ်၏ အလေးချိန်များကို quantize ပြုလုပ်သည်။ ၎င်းသည် activation များရှိ ဒေတာဖြန့်ဖြူးမှုကို ထည့်သွင်းစဉ်းစားခြင်းဖြစ်ပြီး ရိုးရိုး weight quantization နည်းလမ်းများထက် မော်ဒယ်တိကျမှုကို ပိုမိုကောင်းမွန်စေသည်။

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ quantization ပြီးစီးရန် **~၈ မိနစ်** ကြာပြီး မော်ဒယ်အရွယ်အစားကို ~7.5GB မှ ~2.5GB သို့ လျော့နည်းစေပါသည်။

    ဤ lab တွင် Hugging Face မှ မော်ဒယ်များ (ဥပမာ- `microsoft/Phi-3.5-mini-instruct`) ကို input အဖြစ် အသုံးပြုသော်လည်း Azure AI catalog မှ မော်ဒယ်များကို `model_name_or_path` argument ကို Azure AI asset ID (ဥပမာ- `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) ဖြင့် ပြောင်းလဲ၍ input ပြုလုပ်နိုင်ပါသည်။

3. **မော်ဒယ်ကို သင်ကြားခြင်း:** နောက်တစ်ဆင့်မှာ `olive finetune` command ဖြင့် quantize ပြုလုပ်ပြီး မော်ဒယ်ကို fine-tune ပြုလုပ်မည်။ Quantize ပြုလုပ်ပြီးနောက် fine-tune ပြုလုပ်ခြင်းသည် accuracy ပိုမိုကောင်းမွန်စေသည်၊ fine-tuning သည် quantization မှ ဖြစ်ပေါ်သည့် အနည်းငယ်သော အနုတ်လက္ခဏာများကို ပြန်လည်ကောင်းမွန်စေသည်။

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

    Fine-tuning ပြီးစီးရန် **~၆ မိနစ်** ကြာသည် (100 steps ဖြင့်)။

4. **အကောင်းဆုံးပြုလုပ်ခြင်း:** မော်ဒယ်သင်ကြားပြီးနောက် Olive ၏ `auto-opt` command ဖြင့် ONNX graph ကို ဖမ်းဆီးပြီး မော်ဒယ်ကို CPU အတွက် ဖိအားချခြင်း၊ fusion များပြုလုပ်ခြင်းဖြင့် စွမ်းဆောင်ရည် တိုးတက်စေရန် အလိုအလျောက် optimization များ ပြုလုပ်မည်။ NPU သို့မဟုတ် GPU အတွက် optimize ပြုလုပ်လိုပါက `--device` နှင့် `--provider` arguments များကို ပြောင်းလဲနိုင်သော်လည်း ဤ lab အတွက် CPU ကို အသုံးပြုမည်ဖြစ်သည်။

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

    Optimization ပြီးစီးရန် **~၅ မိနစ်** ကြာသည်။

### အဆင့် 5: မော်ဒယ် inference အမြန်စမ်းသပ်ခြင်း

မော်ဒယ် inference စမ်းသပ်ရန် သင့်ဖိုလ်ဒါတွင် **app.py** ဟု Python ဖိုင်တစ်ခု ဖန်တီးပြီး အောက်ပါ code ကို ကူးထည့်ပါ-

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

အောက်ပါ command ဖြင့် code ကို အကောင်အထည်ဖော်ပါ-

```bash
python app.py
```

### အဆင့် 6: မော်ဒယ်ကို Azure AI သို့ အပ်လုဒ်လုပ်ခြင်း

မော်ဒယ်ကို Azure AI model repository သို့ အပ်လုဒ်ခြင်းဖြင့် သင့်ဖွံ့ဖြိုးတိုးတက်ရေးအဖွဲ့ဝင်များနှင့် မော်ဒယ်ကို မျှဝေခြင်းနှင့် မော်ဒယ် version control ကို စီမံခန့်ခွဲနိုင်သည်။ မော်ဒယ်ကို အပ်လုဒ်ရန် အောက်ပါ command ကို အသုံးပြုပါ-

> [!NOTE]
> `{}` placeholder များကို သင့် resource group နာမည်နှင့် Azure AI Project နာမည်ဖြင့် ပြောင်းလဲထည့်သွင်းပါ။

resource group နာမည်နှင့် Azure AI Project နာမည် ရှာဖွေရန် အောက်ပါ command ကို အသုံးပြုပါ-

```
az ml workspace show
```

သို့မဟုတ် +++ai.azure.com+++ သို့ သွား၍ **management center** > **project** > **overview** ကို ရွေးချယ်ပါ။

`{}` placeholder များကို သင့် resource group နာမည်နှင့် Azure AI Project နာမည်ဖြင့် ပြောင်းလဲထည့်သွင်းပါ-

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

အပ်လုဒ်ပြီးနောက် သင့်မော်ဒယ်ကို https://ml.azure.com/model/list တွင် ကြည့်ရှု၍ ဖြန့်ချိနိုင်ပါသည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မခံပါ။