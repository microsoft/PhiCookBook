<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-17T10:10:05+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "my"
}
-->
# **Apple MLX Framework ဖြင့် Phi-3 ကို အနုညာတစွာ ခန့်မှန်းခြေခြင်း**

## **MLX Framework ဆိုတာဘာလဲ**

MLX သည် Apple silicon ပေါ်တွင် စက်သင်ယူမှု သုတေသနအတွက် အသုံးပြုသော array framework ဖြစ်ပြီး Apple ၏ စက်သင်ယူမှု သုတေသနမှ တီထွင်ပေးထားသည်။

MLX ကို စက်သင်ယူမှု သုတေသနပညာရှင်များအတွက် ဒီဇိုင်းဆွဲထားပြီး သုတေသနပညာရှင်များအတွက် အသုံးပြုရ လွယ်ကူစေရန် ရည်ရွယ်ထားသည်။ ဒီ framework သည် အသုံးပြုရ လွယ်ကူသော်လည်း မော်ဒယ်များကို လေ့ကျင့်ခြင်းနှင့် တပ်ဆင်ခြင်းတွင် ထိရောက်မှုရှိစေရန် ရည်ရွယ်ထားသည်။ Framework ၏ ဒီဇိုင်းကိုလည်း အကြောင်းအရာအရ ရိုးရှင်းစွာ ဖန်တီးထားသည်။ သုတေသနပညာရှင်များအနေဖြင့် MLX ကို အလွယ်တကူ တိုးချဲ့ပြီး တိုးတက်အောင် ပြုလုပ်နိုင်ရန် ရည်ရွယ်ထားသည်။

Apple Silicon စက်ပစ္စည်းများတွင် MLX ဖြင့် LLM များကို မြန်ဆန်စွာ လည်ပတ်နိုင်ပြီး မော်ဒယ်များကို ဒေသတွင်းတွင် အလွယ်တကူ အသုံးပြုနိုင်သည်။

## **MLX ဖြင့် Phi-3-mini ကို ခန့်မှန်းခြေခြင်း**

### **1. MLX ပတ်ဝန်းကျင်ကို ပြင်ဆင်ခြင်း**

1. Python 3.11.x
2. MLX Library ကို ထည့်သွင်းပါ


```bash

pip install mlx-lm

```

### **2. Terminal မှာ MLX ဖြင့် Phi-3-mini ကို လည်ပတ်ခြင်း**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ရလဒ် (ကျွန်ုပ်၏ ပတ်ဝန်းကျင်မှာ Apple M1 Max, 64GB ဖြစ်သည်)မှာ

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9.my.png)

### **3. Terminal မှာ MLX ဖြင့် Phi-3-mini ကို Quantize လုပ်ခြင်း**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** မော်ဒယ်ကို mlx_lm.convert ဖြင့် quantize လုပ်နိုင်ပြီး ပုံမှန် quantization သည် INT4 ဖြစ်သည်။ ဤဥပမာတွင် Phi-3-mini ကို INT4 သို့ quantize လုပ်ထားသည်။

မော်ဒယ်ကို mlx_lm.convert ဖြင့် quantize လုပ်နိုင်ပြီး ပုံမှန် quantization သည် INT4 ဖြစ်သည်။ ဤဥပမာတွင် Phi-3-mini ကို INT4 သို့ quantize လုပ်ထားသည်။ Quantize ပြီးနောက် မော်ဒယ်ကို ပုံမှန် ဒိုင်ရက်ထရီ ./mlx_model တွင် သိမ်းဆည်းထားမည်။

Terminal မှာ MLX ဖြင့် quantize လုပ်ထားသော မော်ဒယ်ကို စမ်းသပ်နိုင်သည်။


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ရလဒ်မှာ

![INT4](../../../../../translated_images/02.7b188681a8eadbc1.my.png)


### **4. Jupyter Notebook မှာ MLX ဖြင့် Phi-3-mini ကို လည်ပတ်ခြင်း**


![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9.my.png)

***Note:*** ဤနမူနာကို [ဒီလင့်ခ်ကိုနှိပ်ပါ](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb) မှာ ဖတ်ရှုနိုင်ပါသည်။


## **အရင်းအမြစ်များ**

1. Apple MLX Framework အကြောင်း လေ့လာရန် [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။