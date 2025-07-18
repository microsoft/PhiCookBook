<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-16T15:59:51+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "my"
}
-->
# Lab. Optimize AI models for on-device inference

## နိဒါန်း

> [!IMPORTANT]
> ဒီ lab မှာ **Nvidia A10 သို့မဟုတ် A100 GPU** နဲ့ အတူ driver တွေနဲ့ CUDA toolkit (version 12+) တပ်ဆင်ထားဖို့ လိုအပ်ပါတယ်။

> [!NOTE]
> ဒီ lab က **၃၅ မိနစ်** ကြာပြီး OLIVE ကို အသုံးပြုပြီး on-device inference အတွက် မော်ဒယ်များကို optimize လုပ်ခြင်း၏ အခြေခံအကြောင်းအရာများကို လက်တွေ့ လေ့လာသင်ယူနိုင်မယ့် lab ဖြစ်ပါတယ်။

## သင်ယူရမယ့် ရည်မှန်းချက်များ

ဒီ lab ပြီးဆုံးတဲ့အချိန်မှာ OLIVE ကို အသုံးပြုပြီး -

- AWQ quantization နည်းလမ်းဖြင့် AI မော်ဒယ်ကို Quantize လုပ်နိုင်ပါမယ်။
- AI မော်ဒယ်ကို အထူးတာဝန်အတွက် Fine-tune လုပ်နိုင်ပါမယ်။
- ONNX Runtime ပေါ်မှာ ထိရောက်စွာ on-device inference လုပ်နိုင်ဖို့ LoRA adapters (fine-tuned model) ကို ဖန်တီးနိုင်ပါမယ်။

### Olive ဆိုတာဘာလဲ

Olive (*O*NNX *live*) ဆိုတာ ONNX runtime +++https://onnxruntime.ai+++ အတွက် မော်ဒယ်များကို အရည်အသွေးနဲ့ စွမ်းဆောင်ရည်ကောင်းမွန်စွာ ပို့ဆောင်နိုင်ဖို့ မော်ဒယ် optimize လုပ်တဲ့ toolkit တစ်ခုဖြစ်ပြီး CLI ပါဝင်ပါတယ်။

![Olive Flow](../../../../../translated_images/olive-flow.a47985655a756dcba73521511ea42eef359509a3a33cbd4b9ac04ba433287b80.my.png)

Olive သို့ input အနေနဲ့ ပုံမှန်အားဖြင့် PyTorch သို့မဟုတ် Hugging Face မော်ဒယ်တစ်ခုကို ထည့်သွင်းပြီး output အနေနဲ့ ONNX runtime ပေါ်မှာ အကောင်အထည်ဖော်မယ့် optimized ONNX မော်ဒယ်ကို ထုတ်ပေးပါတယ်။ Olive က မော်ဒယ်ကို deployment target ရဲ့ AI accelerator (NPU, GPU, CPU) အတွက် optimize လုပ်ပေးမှာဖြစ်ပြီး Qualcomm, AMD, Nvidia သို့မဟုတ် Intel ကဲ့သို့သော hardware vendor များမှ ပံ့ပိုးပေးတဲ့ accelerator များအတွက် ဖြစ်ပါတယ်။

Olive က *workflow* တစ်ခုကို အကောင်အထည်ဖော်ပြီး workflow ဆိုတာက မော်ဒယ် optimize လုပ်တဲ့ တစ်ခုချင်းစီလုပ်ငန်းစဉ်များကို အစဉ်လိုက် စီစဉ်ထားတဲ့ အဆင့်လိုက်လုပ်ငန်းစဉ်ဖြစ်ပြီး *passes* လို့ခေါ်ပါတယ်။ ဥပမာ passes တွေမှာ မော်ဒယ်ဖိအားချခြင်း၊ graph capture, quantization, graph optimization စတဲ့ pass များ ပါဝင်ပါတယ်။ pass တစ်ခုချင်းစီမှာ parameter များရှိပြီး အကောင်းဆုံး metrics (ဥပမာ တိကျမှုနဲ့ latency) ရရှိအောင် တိုက်ရိုက်ပြင်ဆင်နိုင်ပါတယ်။ Olive က search algorithm တစ်ခုကို အသုံးပြုပြီး pass တစ်ခုချင်းစီ သို့မဟုတ် pass များစုစုပေါင်းကို auto-tune လုပ်ပေးပါတယ်။

#### Olive ရဲ့ အကျိုးကျေးဇူးများ

- graph optimization, compression နဲ့ quantization နည်းလမ်းများကို လက်တွေ့စမ်းသပ်ရာမှာ trial-and-error manual experimentation ကြောင့် ဖြစ်တတ်တဲ့ စိတ်ညစ်မှုနဲ့ အချိန်ကုန်မှုကို လျော့နည်းစေပါတယ်။ သင့်ရဲ့ quality နဲ့ performance ကန့်သတ်ချက်များကို သတ်မှတ်ပြီး Olive ကို အကောင်းဆုံး မော်ဒယ်ကို အလိုအလျောက် ရှာဖွေစေပါ။
- quantization, compression, graph optimization နဲ့ finetuning နယ်ပယ်များမှာ နောက်ဆုံးပေါ်နည်းပညာများ ပါဝင်တဲ့ **40+ built-in model optimization components** များ။
- မော်ဒယ် optimize လုပ်ရာမှာ အသုံးပြုရ လွယ်ကူတဲ့ CLI (ဥပမာ olive quantize, olive auto-opt, olive finetune)။
- မော်ဒယ် package လုပ်ခြင်းနဲ့ deployment ကို built-in ပံ့ပိုးမှု။
- **Multi LoRA serving** အတွက် မော်ဒယ်ဖန်တီးခြင်းကို ပံ့ပိုးသည်။
- YAML/JSON ဖြင့် workflow များ ဖန်တီးပြီး မော်ဒယ် optimize နဲ့ deployment လုပ်ငန်းစဉ်များကို စီမံခန့်ခွဲနိုင်သည်။
- **Hugging Face** နဲ့ **Azure AI** ပေါင်းစပ်မှု။
- ကုန်ကျစရိတ် လျော့ချဖို့ built-in **caching** mechanism ပါဝင်သည်။

## Lab လမ်းညွှန်ချက်များ

> [!NOTE]
> Lab 1 အတိုင်း Azure AI Hub နဲ့ Project ကို ပြင်ဆင်ပြီး A100 compute ကို စတင်ထားကြောင်း သေချာပါစေ။

### အဆင့် 0: Azure AI Compute နဲ့ ချိတ်ဆက်ခြင်း

**VS Code** ရဲ့ remote feature ကို အသုံးပြုပြီး Azure AI compute နဲ့ ချိတ်ဆက်ပါ။

1. **VS Code** desktop application ကို ဖွင့်ပါ။
2. **Shift+Ctrl+P** ဖြင့် command palette ကို ဖွင့်ပါ။
3. command palette မှာ **AzureML - remote: Connect to compute instance in New Window** ကို ရှာပါ။
4. Azure Subscription, Resource Group, Project နဲ့ Lab 1 မှာ သတ်မှတ်ထားတဲ့ Compute name ကို ရွေးချယ်ပြီး ချိတ်ဆက်ပါ။
5. ချိတ်ဆက်ပြီးရင် Visual Code ရဲ့ ဘယ်ဘက်အောက်ဆုံးမှာ `><Azure ML: Compute Name` လို့ ပြပါလိမ့်မယ်။

### အဆင့် 1: Repo ကို Clone လုပ်ခြင်း

VS Code မှာ **Ctrl+J** ဖြင့် terminal အသစ်ဖွင့်ပြီး ဒီ repo ကို clone လုပ်ပါ။

terminal မှာ prompt ကို တွေ့ရပါမယ်။

```
azureuser@computername:~/cloudfiles/code$ 
```  
Clone the solution  

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### အဆင့် 2: VS Code မှာ Folder ဖွင့်ခြင်း

terminal မှာ အောက်ပါ command ကို ရိုက်ထည့်ပြီး VS Code ကို သက်ဆိုင်ရာ folder နဲ့ ဖွင့်ပါ။ အဲဒါက နောက်ထပ် window တစ်ခု ဖွင့်ပေးပါလိမ့်မယ်။

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

ဒါမှမဟုတ် **File** > **Open Folder** ကို ရွေးပြီး folder ကို ဖွင့်နိုင်ပါတယ်။

### အဆင့် 3: Dependencies များ ထည့်သွင်းခြင်း

VS Code ရဲ့ Azure AI Compute Instance မှာ terminal ဖွင့်ပြီး (အကြံပြုချက်: **Ctrl+J**) အောက်ပါ command များကို ရိုက်ထည့်ပြီး dependencies များကို ထည့်သွင်းပါ။

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> dependencies အားလုံး ထည့်သွင်းဖို့ ~၅ မိနစ်ခန့် ကြာနိုင်ပါတယ်။

ဒီ lab မှာ မော်ဒယ်များကို Azure AI Model catalog မှာ ဒေါင်းလုပ်လုပ်ပြီး အပ်လုဒ်လုပ်မှာဖြစ်လို့ Azure မှာ login လုပ်ဖို့လိုပါတယ်။

```bash
az login
```

> [!NOTE]
> login လုပ်တဲ့အချိန်မှာ subscription ရွေးချယ်ဖို့ တောင်းဆိုပါမယ်။ ဒီ lab အတွက် ပေးထားတဲ့ subscription ကို သေချာရွေးချယ်ပါ။

### အဆင့် 4: Olive command များ အကောင်အထည်ဖော်ခြင်း

VS Code ရဲ့ Azure AI Compute Instance မှာ terminal ဖွင့်ပြီး `olive-ai` conda environment ကို အလုပ်လုပ်နေကြောင်း သေချာစေပါ။

```bash
conda activate olive-ai
```

နောက်တစ်ဆင့်မှာ အောက်ပါ Olive command များကို command line မှာ အကောင်အထည်ဖော်ပါ။

1. **ဒေတာကို စစ်ဆေးခြင်း:** ဤဥပမာမှာ Phi-3.5-Mini မော်ဒယ်ကို ခရီးသွားဆိုင်ရာ မေးခွန်းများကို ဖြေဆိုနိုင်အောင် fine-tune လုပ်မှာဖြစ်ပါတယ်။ အောက်ပါ code က JSON lines format ဖြင့် ရှိတဲ့ dataset ရဲ့ ပထမဆုံး အချက်အလက်အနည်းငယ်ကို ပြသပါတယ်။

    ```bash
    head data/data_sample_travel.jsonl
    ```

2. **မော်ဒယ်ကို Quantize လုပ်ခြင်း:** မော်ဒယ်ကို သင်ကြားမလုပ်ခင် Active Aware Quantization (AWQ) နည်းလမ်း +++https://arxiv.org/abs/2306.00978+++ ကို အသုံးပြုပြီး quantize လုပ်ပါမယ်။ AWQ က inference အတွင်း ထုတ်လုပ်တဲ့ activations ကို စဉ်းစားပြီး မော်ဒယ်အလေးချိန်များကို quantize လုပ်တာဖြစ်ပါတယ်။ ဒါကြောင့် quantization လုပ်စဉ်မှာ activations ရဲ့ ဒေတာဖြန့်ဖြူးမှုကို ထည့်သွင်းစဉ်းစားတာကြောင့် ရိုးရိုး weight quantization နည်းလမ်းထက် တိကျမှုပိုမိုကောင်းမွန်စေပါတယ်။

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ quantization ပြီးမြောက်ဖို့ **~၈ မိနစ်** ကြာပြီး မော်ဒယ်အရွယ်အစားကို ~7.5GB မှ ~2.5GB သို့ လျော့နည်းစေပါမယ်။

    ဒီ lab မှာ Hugging Face မှ မော်ဒယ်များ (ဥပမာ `microsoft/Phi-3.5-mini-instruct`) ကို input အနေနဲ့ သုံးပြသထားပေမယ့် Olive က Azure AI catalog မှ မော်ဒယ်များကိုလည်း `model_name_or_path` argument ကို Azure AI asset ID (ဥပမာ `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) ဖြင့် ပြောင်းလဲသုံးနိုင်ပါတယ်။

3. **မော်ဒယ်ကို သင်ကြားခြင်း:** နောက်တစ်ဆင့်မှာ `olive finetune` command က quantize လုပ်ပြီး မော်ဒယ်ကို fine-tune လုပ်ပေးမှာဖြစ်ပါတယ်။ Quantize လုပ်ပြီးနောက် fine-tune လုပ်ခြင်းက quantization မှာ ဖြစ်ပေါ်လာတဲ့ accuracy လျော့နည်းမှုကို ပြန်လည်ကောင်းမွန်စေပါတယ်။

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

    Fine-tuning ပြီးမြောက်ဖို့ **~၆ မိနစ်** (၁၀၀ steps) ကြာပါမယ်။

4. **Optimize လုပ်ခြင်း:** မော်ဒယ်ကို သင်ကြားပြီးနောက် Olive ရဲ့ `auto-opt` command ကို အသုံးပြုပြီး ONNX graph ကို ဖမ်းဆီးပြီး မော်ဒယ်ကို CPU အတွက် ဖိအားချခြင်း၊ fusion စတဲ့ optimization များကို အလိုအလျောက် လုပ်ဆောင်ပေးမှာဖြစ်ပါတယ်။ အခြား device များ (NPU, GPU) အတွက် optimize လုပ်ချင်ရင် `--device` နဲ့ `--provider` arguments ကို ပြောင်းလဲနိုင်ပါတယ်။ ဒီ lab အတွက်တော့ CPU ကို အသုံးပြုမှာဖြစ်ပါတယ်။

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

    Optimization ပြီးမြောက်ဖို့ **~၅ မိနစ်** ကြာပါမယ်။

### အဆင့် 5: မော်ဒယ် inference အမြန်စမ်းသပ်ခြင်း

မော်ဒယ်ကို inference စမ်းသပ်ဖို့ သင့် folder ထဲမှာ **app.py** ဆိုတဲ့ Python ဖိုင်တစ်ခု ဖန်တီးပြီး အောက်ပါ code ကို ကူးထည့်ပါ။

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

### အဆင့် 6: မော်ဒယ်ကို Azure AI သို့ အပ်လုဒ်လုပ်ခြင်း

မော်ဒယ်ကို Azure AI model repository သို့ အပ်လုဒ်လုပ်ခြင်းက သင့်ဖွံ့ဖြိုးရေးအဖွဲ့ဝင်များနဲ့ မော်ဒယ်ကို မျှဝေဖို့နဲ့ မော်ဒယ် version control ကို စီမံခန့်ခွဲဖို့ အထောက်အကူဖြစ်ပါတယ်။ မော်ဒယ်ကို အပ်လုဒ်လုပ်ဖို့ အောက်ပါ command ကို အသုံးပြုပါ။

> [!NOTE]
> `{}` placeholders တွေကို သင့် resource group နဲ့ Azure AI Project နာမည်နဲ့ ပြောင်းလဲထည့်သွင်းပါ။

resource group နဲ့ Azure AI Project နာမည်ကို ရှာဖွေရန် အောက်ပါ command ကို အသုံးပြုပါ။

```
az ml workspace show
```

သို့မဟုတ် +++ai.azure.com+++ သို့ ဝင်ပြီး **management center** > **project** > **overview** ကို ရွေးချယ်ပါ။

`{}` placeholders တွေကို သင့် resource group နဲ့ Azure AI Project နာမည်နဲ့ ပြောင်းလဲထည့်သွင်းပါ။

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

ပြီးရင် သင့်အပ်လုဒ်လုပ်ထားတဲ့ မော်ဒယ်ကို https://ml.azure.com/model/list မှာ ကြည့်ရှုနိုင်ပြီး မော်ဒယ်ကို deploy လုပ်နိုင်ပါပြီ။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။