<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-09T20:13:44+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "my"
}
-->
# Olive ကို အသုံးပြုပြီး Phi3 ကို Fine-tune လုပ်ခြင်း

ဤဥပမာတွင် Olive ကို အသုံးပြုပြီး -

1. LoRA adapter ကို fine-tune လုပ်၍ စကားစုများကို Sad, Joy, Fear, Surprise အဖြစ် သတ်မှတ်ခြင်း။
1. Adapter အလေးချိန်များကို base model ထဲသို့ ပေါင်းစပ်ခြင်း။
1. Model ကို optimize လုပ်ပြီး `int4` အဖြစ် quantize လုပ်ခြင်း။

ထို့အပြင် ONNX Runtime (ORT) Generate API ကို အသုံးပြု၍ fine-tuned model ကို inference ပြုလုပ်နည်းကိုလည်း ပြသပါမည်။

> **⚠️ Fine-tuning အတွက် သင့်တော်သော GPU တစ်ခု လိုအပ်ပါသည် - ဥပမာ A10, V100, A100 စသည်ဖြစ်သည်။**

## 💾 설치

Python virtual environment အသစ်တစ်ခု ဖန်တီးပါ (ဥပမာ `conda` ကို အသုံးပြု၍)။

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

နောက်တစ်ဆင့်မှာ Olive နှင့် fine-tuning workflow အတွက် လိုအပ်သော dependencies များကို 설치 လုပ်ပါ။

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive ကို အသုံးပြုပြီး Phi3 ကို Fine-tune လုပ်ခြင်း
[Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) တွင် *workflow* တစ်ခုပါရှိပြီး အောက်ပါ *passes* များပါဝင်သည် -

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

အထွေထွေ အဆင့်မြင့်မှာ workflow သည် -

1. Phi3 ကို (150 steps အထိ၊ ပြင်ဆင်နိုင်သည်) [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) ဒေတာဖြင့် fine-tune လုပ်ခြင်း။
1. LoRA adapter အလေးချိန်များကို base model ထဲသို့ ပေါင်းစပ်ခြင်း။ ၎င်းက ONNX format ဖြင့် model artifact တစ်ခုကို ရရှိစေပါသည်။
1. Model Builder သည် ONNX runtime အတွက် model ကို optimize လုပ်ပြီး `int4` အဖြစ် quantize လုပ်ပါသည်။

Workflow ကို အကောင်အထည်ဖော်ရန် -

```bash
olive run --config phrase-classification.json
```

Olive ပြီးဆုံးသည့်အခါ သင့် optimized `int4` fine-tuned Phi3 model ကို `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model` တွင် ရရှိနိုင်ပါသည်။

## 🧑‍💻 Fine-tuned Phi3 ကို သင့် application ထဲသို့ ပေါင်းစပ်ခြင်း

App ကို run ဖို့ -

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

ဤတုံ့ပြန်ချက်သည် စကားစု၏ တစ်လုံးတည်းသော အမျိုးအစား (Sad/Joy/Fear/Surprise) ဖြစ်ရမည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။