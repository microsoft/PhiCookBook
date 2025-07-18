<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:57:53+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "my"
}
-->
# **Apple MLX Framework ဖြင့် Phi-3.5 ကို Quantize လုပ်ခြင်း**

MLX သည် Apple silicon ပေါ်တွင် စက်သင်ယူမှု သုတေသနအတွက် Apple machine learning သုတေသနမှ တီထွင်ထားသော array framework ဖြစ်သည်။

MLX ကို စက်သင်ယူမှု သုတေသနပညာရှင်များအတွက် စက်သင်ယူမှု သုတေသနပညာရှင်များက ဒီဇိုင်းဆွဲထားသည်။ ဤ framework သည် အသုံးပြုရ လွယ်ကူပြီး မော်ဒယ်များကို လေ့ကျင့်ခြင်းနှင့် တပ်ဆင်ခြင်းတွင် ထိရောက်စွာ အသုံးပြုနိုင်ရန် ရည်ရွယ်ထားသည်။ Framework ၏ ဒီဇိုင်းကိုလည်း အကြောင်းအရာအရ ရိုးရှင်းစွာ ဖန်တီးထားသည်။ သုတေသနပညာရှင်များအနေဖြင့် MLX ကို တိုးချဲ့ပြီး တိုးတက်အောင် လွယ်ကူစွာ ပြုလုပ်နိုင်ရန် ရည်ရွယ်ထားသည်၊ ထို့ကြောင့် အသစ်သော အတွေးအခေါ်များကို မြန်ဆန်စွာ စမ်းသပ်နိုင်မည်ဖြစ်သည်။

Apple Silicon စက်ပစ္စည်းများတွင် MLX ဖြင့် LLM များကို မြန်ဆန်စွာ လည်ပတ်နိုင်ပြီး မော်ဒယ်များကို ဒေသတွင်းတွင် အလွယ်တကူ အသုံးပြုနိုင်သည်။

ယခု Apple MLX Framework သည် Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), နှင့် Phi-3.5-MoE(**Apple MLX Framework support**) များ၏ quantization ပြောင်းလဲမှုကို ထောက်ပံ့ပေးသည်။ အောက်တွင် စမ်းသပ်ကြည့်ကြပါစို့။

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Apple MLX ဖြင့် Phi-3.5 အတွက် နမူနာများ**

| Labs    | မိတ်ဆက်ချက် | သွားရန် |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX framework ဖြင့် Phi-3.5 Instruct ကို ဘယ်လို အသုံးပြုမလဲ သင်ယူပါ   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX framework ဖြင့် Phi-3.5 Vision ကို ပုံများ စိစစ်ရန် ဘယ်လို အသုံးပြုမလဲ သင်ယူပါ     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX framework ဖြင့် Phi-3.5 MoE ကို ဘယ်လို အသုံးပြုမလဲ သင်ယူပါ  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **အရင်းအမြစ်များ**

1. Apple MLX Framework အကြောင်း သင်ယူရန် [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။