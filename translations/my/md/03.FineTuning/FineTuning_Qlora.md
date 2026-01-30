**QLoRA ဖြင့် Phi-3 ကို အတိအကျ ပြင်ဆင်ခြင်း**

Microsoft ၏ Phi-3 Mini ဘာသာစကားမော်ဒယ်ကို [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) အသုံးပြု၍ အတိအကျ ပြင်ဆင်ခြင်း။

QLoRA သည် စကားပြောနားလည်မှုနှင့် တုံ့ပြန်မှု ဖန်တီးမှုကို တိုးတက်စေမှာ ဖြစ်သည်။

transformers နှင့် bitsandbytes ဖြင့် 4bits မော်ဒယ်များကို ဖွင့်ရန်အတွက် accelerate နှင့် transformers ကို source မှ ထည့်သွင်းရမည်ဖြစ်ပြီး bitsandbytes စာကြည့်တိုက်၏ နောက်ဆုံးဗားရှင်းရှိကြောင်း သေချာစေရမည်။

**နမူနာများ**
- [ဤနမူနာ notebook ဖြင့် ပိုမိုလေ့လာရန်](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning နမူနာ ဥပမာ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub တွင် LORA ဖြင့် Fine Tuning ဥပမာ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub တွင် QLORA ဖြင့် Fine Tuning ဥပမာ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။