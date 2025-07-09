<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-09T20:14:16+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "my"
}
-->
# Lab. Optimize AI models for on-device inference

## နိဒါန်း

> [!IMPORTANT]
> ဒီ lab မှာ **Nvidia A10 သို့မဟုတ် A100 GPU** နဲ့ အတူ driver တွေနဲ့ CUDA toolkit (version 12+) တပ်ဆင်ထားဖို့ လိုအပ်ပါတယ်။

> [!NOTE]
> ဒီ lab က **၃၅ မိနစ်** ကြာပြီး OLIVE ကို အသုံးပြုပြီး on-device inference အတွက် မော်ဒယ်များကို optimize လုပ်ခြင်း၏ အခြေခံအကြောင်းအရာများကို လက်တွေ့ လေ့လာသင်ကြားပေးမှာ ဖြစ်ပါတယ်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီ lab အပြီးမှာ OLIVE ကို အသုံးပြုပြီး -

- AWQ quantization နည်းလမ်းဖြင့် AI မော်ဒယ်ကို Quantize လုပ်နိုင်မည်။
- AI မော်ဒယ်ကို အထူးတာဝန်အတွက် Fine-tune လုပ်နိုင်မည်။
- ONNX Runtime ပေါ်တွင် ထိရောက်စွာ on-device inference ပြုလုပ်နိုင်ရန် LoRA adapters (fine-tuned model) များကို ဖန်တီးနိုင်မည်။

### Olive ဆိုတာဘာလဲ

Olive (*O*NNX *live*) သည် ONNX runtime +++https://onnxruntime.ai+++ အတွက် မော်ဒယ်များကို အရည်အသွေးနှင့် စွမ်းဆောင်ရည်ကောင်းမွန်စွာ ပို့ဆောင်နိုင်ရန် မော်ဒယ် optimize လုပ်ရာတွင် အသုံးပြုသော toolkit တစ်ခုဖြစ်ပြီး CLI ပါဝင်သည်။

![Olive Flow](../../../../../code/04.Finetuning/olive-lab/images/olive-flow.png)

Olive သို့ input အနေဖြင့် ပုံမှန်အားဖြင့် PyTorch သို့မဟုတ် Hugging Face မော်ဒယ်တစ်ခုကို ထည့်သွင်းပြီး output အနေဖြင့် ONNX runtime ပေါ်တွင် အကောင်အထည်ဖော်မည့် optimized ONNX မော်ဒယ်ကို ထုတ်ပေးသည်။ Olive သည် deployment target အဖြစ် သတ်မှတ်ထားသော စက်ပစ္စည်း၏ AI accelerator (NPU, GPU, CPU) ကို Qualcomm, AMD, Nvidia သို့မဟုတ် Intel ကဲ့သို့သော hardware vendor များမှ ပံ့ပိုးပေးသည့်အတိုင်း မော်ဒယ်ကို optimize လုပ်ပေးသည်။

Olive သည် *workflow* တစ်ခုကို အကောင်အထည်ဖော်ပြီး၊ workflow သည် *passes* ဟုခေါ်သော မော်ဒယ် optimize လုပ်ခြင်းဆိုင်ရာ တစ်ခုချင်းစီသော အဆင့်များ၏ အစဉ်လိုက် စဉ်ဆက်ဖြစ်သည်။ ဥပမာ passes များမှာ မော်ဒယ်ဖိအားချခြင်း၊ graph capture, quantization, graph optimization တို့ဖြစ်သည်။ Pass တစ်ခုစီတွင် parameter များရှိပြီး accuracy နှင့် latency ကဲ့သို့သော metrics များကို အကောင်းဆုံးရရှိရန် တိုက်ရိုက်ပြင်ဆင်နိုင်သည်။ Olive သည် search algorithm တစ်ခုကို အသုံးပြုပြီး pass တစ်ခုချင်းစီ သို့မဟုတ် pass များစုစုပေါင်းကို auto-tune လုပ်ပေးသည်။

#### Olive ၏ အကျိုးကျေးဇူးများ

- graph optimization, compression နှင့် quantization နည်းလမ်းများကို လက်တွေ့စမ်းသပ်ရာတွင် trial-and-error manual experimentation မှ ဖြစ်ပေါ်နိုင်သည့် စိတ်ညစ်မှုနှင့် အချိန်ကုန်ကျမှုကို လျော့နည်းစေသည်။ သင့်ရဲ့ quality နှင့် performance ကန့်သတ်ချက်များကို သတ်မှတ်ပြီး Olive ကို အကောင်းဆုံး မော်ဒယ်ကို အလိုအလျောက် ရှာဖွေစေပါ။
- quantization, compression, graph optimization နှင့် finetuning ဆိုင်ရာ နောက်ဆုံးပေါ်နည်းပညာများကို ဖုံးလွှမ်းသည့် **40+ built-in model optimization components** များပါဝင်သည်။
- မော်ဒယ် optimize လုပ်ခြင်းဆိုင်ရာ ပုံမှန်လုပ်ငန်းများအတွက် အသုံးပြုရ လွယ်ကူသော CLI ရှိသည်။ ဥပမာ - olive quantize, olive auto-opt, olive finetune။
- မော်ဒယ် package ပြုလုပ်ခြင်းနှင့် deployment ကို built-in ဖြင့် ပံ့ပိုးသည်။
- **Multi LoRA serving** အတွက် မော်ဒယ်များ ဖန်တီးပေးနိုင်သည်။
- YAML/JSON အသုံးပြုပြီး မော်ဒယ် optimize နှင့် deployment လုပ်ငန်းစဉ်များကို စီမံခန့်ခွဲနိုင်သည်။
- **Hugging Face** နှင့် **Azure AI** ပေါင်းစည်းမှု။
- ကုန်ကျစရိတ် လျော့ချရန် built-in **caching** mechanism ပါဝင်သည်။

## Lab လမ်းညွှန်ချက်များ

> [!NOTE]
> Lab 1 အတိုင်း Azure AI Hub နှင့် Project ကို provision ပြုလုပ်ပြီး A100 compute ကို စနစ်တကျ ပြင်ဆင်ထားကြောင်း သေချာပါစေ။

### အဆင့် 0: Azure AI Compute နှင့် ချိတ်ဆက်ခြင်း

**VS Code** ၏ remote feature ကို အသုံးပြုပြီး Azure AI compute နှင့် ချိတ်ဆက်ပါ။

1. **VS Code** desktop application ကို ဖွင့်ပါ။
2. **Shift+Ctrl+P** ဖြင့် command palette ကို ဖွင့်ပါ။
3. command palette တွင် **AzureML - remote: Connect to compute instance in New Window** ကို ရှာဖွေပါ။
4. Azure Subscription, Resource Group, Project နှင့် Lab 1 တွင် သတ်မှတ်ထားသော Compute name ကို ရွေးချယ်ပြီး ချိတ်ဆက်ပါ။
5. ချိတ်ဆက်ပြီးပါက Visual Code ၏ ဘယ်ဘက်အောက်ခြေတွင် `><Azure ML: Compute Name` ဟူ၍ ပြသမည်ဖြစ်သည်။

### အဆင့် 1: Repo ကို Clone လုပ်ခြင်း

VS Code တွင် **Ctrl+J** ဖြင့် terminal အသစ်ဖွင့်ပြီး repo ကို clone လုပ်ပါ။

terminal တွင် prompt ကို တွေ့ရမည် -

```
azureuser@computername:~/cloudfiles/code$ 
```  
Clone the solution  

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### အဆင့် 2: VS Code တွင် Folder ဖွင့်ခြင်း

terminal တွင် အောက်ပါ command ကို ရိုက်ထည့်ပါ၊ ထို့နောက် window အသစ်တစ်ခု ဖွင့်မည်။

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

သို့မဟုတ် **File** > **Open Folder** ကို ရွေး၍ folder ကို ဖွင့်နိုင်သည်။

### အဆင့် 3: Dependencies များ ထည့်သွင်းခြင်း

VS Code ၏ Azure AI Compute Instance တွင် terminal ဖွင့်ပြီး (အကြံပြုချက် - **Ctrl+J**) အောက်ပါ command များကို ရိုက်ထည့်ကာ dependencies များ ထည့်သွင်းပါ။

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Dependencies များ ထည့်သွင်းရန် ~၅ မိနစ်ခန့် ကြာနိုင်သည်။

ဒီ lab မှာ မော်ဒယ်များကို Azure AI Model catalog သို့ download နှင့် upload ပြုလုပ်မည်ဖြစ်သောကြောင့် Azure သို့ login ဝင်ရန်လိုအပ်သည်။

```bash
az login
```

> [!NOTE]
> Login ဝင်စဉ်တွင် subscription ရွေးချယ်ရန် မေးမြန်းမည်ဖြစ်ပြီး lab အတွက် ပေးထားသော subscription ကို သေချာရွေးချယ်ပါ။

### အဆင့် 4: Olive command များ အကောင်အထည်ဖော်ခြင်း

VS Code ၏ Azure AI Compute Instance တွင် terminal ဖွင့်ပြီး `olive-ai` conda environment ကို ဖွင့်ထားကြောင်း သေချာစေပါ။

```bash
conda activate olive-ai
```

နောက်တစ်ဆင့်မှာ အောက်ပါ Olive command များကို command line တွင် အကောင်အထည်ဖော်ပါ။

1. **ဒေတာကို စစ်ဆေးခြင်း:** ဤဥပမာတွင် Phi-3.5-Mini မော်ဒယ်ကို ခရီးသွားဆိုင်ရာ မေးခွန်းများကို ဖြေဆိုရာတွင် အထူးပြုရန် fine-tune လုပ်မည်ဖြစ်သည်။ အောက်ပါ code သည် JSON lines format ဖြင့် ရှိသော ဒေတာ၏ အစောပိုင်း မှတ်တမ်းများကို ပြသသည်။

    ```bash
    head data/data_sample_travel.jsonl
    ```

2. **မော်ဒယ်ကို Quantize လုပ်ခြင်း:** မော်ဒယ်ကို သင်ကြားမတိုင်မီ Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ နည်းလမ်းဖြင့် quantize လုပ်မည်။ AWQ သည် inference အတွင်း ထုတ်လုပ်သော activations များကို စဉ်းစားကာ မော်ဒယ်၏ အလေးချိန်များကို quantize လုပ်သည်။ ဒါကြောင့် quantization လုပ်ငန်းစဉ်သည် activations တွင် ရှိသော ဒေတာဖြန့်ဖြူးမှုကို ထည့်သွင်းစဉ်းစားခြင်းဖြင့် မော်ဒယ်တိကျမှုကို ပိုမိုကောင်းမွန်စေသည်။

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ quantization ပြီးမြောက်ရန် **~၈ မိနစ်** ကြာပြီး မော်ဒယ်အရွယ်အစားကို ~7.5GB မှ ~2.5GB သို့ လျော့နည်းစေမည်ဖြစ်သည်။

    ဒီ lab မှာ Hugging Face မှ မော်ဒယ်များ (ဥပမာ - `microsoft/Phi-3.5-mini-instruct`) ကို input အဖြစ် အသုံးပြုသော်လည်း Azure AI catalog မှ မော်ဒယ်များကို `model_name_or_path` argument ကို Azure AI asset ID (ဥပမာ - `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) ဖြင့် ပြောင်းလဲ၍ input လုပ်နိုင်သည်။

3. **မော်ဒယ်ကို သင်ကြားခြင်း:** နောက်တစ်ဆင့်မှာ `olive finetune` command ဖြင့် quantize လုပ်ပြီး မော်ဒယ်ကို fine-tune လုပ်မည်။ Quantize လုပ်ပြီးနောက် fine-tune လုပ်ခြင်းသည် fine-tune လုပ်ပြီးနောက် quantize လုပ်ခြင်းထက် တိကျမှုပိုမိုကောင်းမွန်စေသည်၊ အကြောင်းမှာ fine-tuning လုပ်စဉ် quantization မှ ဖြစ်ပေါ်သည့် အနုတ်လက္ခဏာများကို ပြန်လည်ပြုပြင်နိုင်ခြင်း ဖြစ်သည်။

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

    Fine-tuning ပြီးမြောက်ရန် **~၆ မိနစ်** (၁၀၀ ခြေလှမ်း) ကြာသည်။

4. **Optimize လုပ်ခြင်း:** မော်ဒယ်ကို သင်ကြားပြီးနောက် Olive ၏ `auto-opt` command ဖြင့် optimize လုပ်မည်။ ONNX graph ကို ဖမ်းဆီးပြီး မော်ဒယ်ကို CPU အတွက် ပိုမိုထိရောက်စေရန် compression နှင့် fusion များ ပြုလုပ်မည်ဖြစ်သည်။ အခြားစက်ပစ္စည်းများ (NPU, GPU) အတွက် optimize လုပ်လိုပါက `--device` နှင့် `--provider` arguments များကို ပြောင်းလဲနိုင်သော်လည်း ဒီ lab အတွက် CPU ကိုသာ အသုံးပြုမည်။

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

    Optimize ပြီးမြောက်ရန် **~၅ မိနစ်** ကြာသည်။

### အဆင့် 5: မော်ဒယ် inference အမြန်စမ်းသပ်ခြင်း

မော်ဒယ် inference စမ်းသပ်ရန် သင့် folder တွင် **app.py** ဆိုသော Python ဖိုင်တစ်ခု ဖန်တီးပြီး အောက်ပါ code ကို ကူးထည့်ပါ။

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

အောက်ပါ command ဖြင့် code ကို အကောင်အထည်ဖော်ပါ။

```bash
python app.py
```

### အဆင့် 6: မော်ဒယ်ကို Azure AI သို့ Upload လုပ်ခြင်း

မော်ဒယ်ကို Azure AI model repository သို့ upload လုပ်ခြင်းဖြင့် သင့်ဖွံ့ဖြိုးတိုးတက်ရေးအဖွဲ့ဝင်များနှင့် မော်ဒယ်ကို မျှဝေခြင်းနှင့် မော်ဒယ် version control ကို စီမံခန့်ခွဲနိုင်သည်။ မော်ဒယ် upload လုပ်ရန် အောက်ပါ command ကို အသုံးပြုပါ။

> [!NOTE]
> `{}` placeholders များကို သင့် resource group နာမည်နှင့် Azure AI Project နာမည်ဖြင့် ပြောင်းလဲထည့်သွင်းပါ။

resource group နာမည်နှင့် Azure AI Project နာမည် ရှာဖွေရန် အောက်ပါ command ကို အသုံးပြုပါ။

```
az ml workspace show
```

သို့မဟုတ် +++ai.azure.com+++ သို့ သွား၍ **management center** > **project** > **overview** ကို ရွေးချယ်ပါ။

`{}` placeholders များကို သင့် resource group နာမည်နှင့် Azure AI Project နာမည်ဖြင့် ပြောင်းလဲထည့်သွင်းပါ။

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

သင့် upload လုပ်ထားသော မော်ဒယ်ကို https://ml.azure.com/model/list တွင် ကြည့်ရှုနိုင်ပြီး မော်ဒယ်ကို deploy လုပ်နိုင်ပါသည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မခံပါ။