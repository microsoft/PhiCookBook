<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-09T19:29:54+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "my"
}
-->
### ဥပမာအခြေအနေ

သင်မှာ `demo.png` ဆိုတဲ့ပုံတစ်ပုံရှိပြီး ဒီပုံကို ပြုပြင်ပြီး အသစ်ထုတ်တဲ့ပုံ (`phi-3-vision.jpg`) ကို သိမ်းဆည်းဖို့ Python ကုဒ်ရေးချင်တယ်လို့ စဉ်းစားပါ။

အထက်ပါကုဒ်က ဒီလုပ်ငန်းစဉ်ကို အလိုအလျောက်လုပ်ဆောင်ပေးတာဖြစ်ပြီး -

1. ပတ်ဝန်းကျင်နဲ့ လိုအပ်တဲ့ ဆက်တင်တွေကို ပြင်ဆင်ခြင်း။
2. မော်ဒယ်ကို Python ကုဒ်ထုတ်ပေးဖို့ အမိန့်စာတစ်ခု ဖန်တီးခြင်း။
3. အမိန့်စာကို မော်ဒယ်ထံ ပို့ပြီး ထုတ်ပေးတဲ့ကုဒ်ကို စုဆောင်းခြင်း။
4. ထုတ်ပေးတဲ့ကုဒ်ကို ခွဲထုတ်ပြီး လုပ်ဆောင်ခြင်း။
5. မူလပုံနဲ့ ပြုပြင်ပြီးပုံကို ပြသခြင်း။

ဒီနည်းလမ်းက AI ၏စွမ်းအားကို အသုံးပြုပြီး ပုံပြင်ဆင်ခြင်းလုပ်ငန်းတွေကို အလိုအလျောက် လုပ်ဆောင်ပေးတာဖြစ်ပြီး သင့်ရဲ့ ရည်မှန်းချက်တွေကို ပိုမိုလွယ်ကူမြန်ဆန်စေပါတယ်။

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

ကုဒ်တစ်ခုလုံး ဘယ်လိုလုပ်ဆောင်တာလဲ ဆိုတာကို အဆင့်ဆင့် ခွဲခြမ်းကြည့်ကြရအောင် -

1. **လိုအပ်တဲ့ Package ကို ထည့်သွင်းခြင်း**  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    ဒီ command က `langchain_nvidia_ai_endpoints` package ကို ထည့်သွင်းပေးပြီး နောက်ဆုံးဗားရှင်းဖြစ်စေပါတယ်။

2. **လိုအပ်တဲ့ Modules တွေကို Import လုပ်ခြင်း**  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    ဒီ imports တွေက NVIDIA AI endpoints နဲ့ ဆက်သွယ်ဖို့၊ password ကို လုံခြုံစွာ ကိုင်တွယ်ဖို့၊ operating system နဲ့ ဆက်သွယ်ဖို့၊ base64 format နဲ့ data encode/decode လုပ်ဖို့ လိုအပ်တဲ့ modules တွေပါ။

3. **API Key ကို သတ်မှတ်ခြင်း**  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    ဒီကုဒ်က `NVIDIA_API_KEY` environment variable ရှိမရှိ စစ်ဆေးပြီး မရှိရင် အသုံးပြုသူကို API key ကို လုံခြုံစွာ ထည့်ရန် တောင်းဆိုပါတယ်။

4. **Model နဲ့ ပုံလမ်းကြောင်း သတ်မှတ်ခြင်း**  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    ဒီမှာ အသုံးပြုမယ့် model ကို သတ်မှတ်ပြီး `ChatNVIDIA` instance တစ်ခု ဖန်တီးထားပြီး ပုံဖိုင်လမ်းကြောင်းကို သတ်မှတ်ထားပါတယ်။

5. **စာသား Prompt ဖန်တီးခြင်း**  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    ဒီမှာ မော်ဒယ်ကို ပုံကို ပြုပြင်ဖို့ Python ကုဒ်ထုတ်ပေးဖို့ အမိန့်စာတစ်ခု သတ်မှတ်ထားပါတယ်။

6. **ပုံကို Base64 ဖြင့် encode လုပ်ခြင်း**  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    ဒီကုဒ်က ပုံဖိုင်ကို ဖတ်ပြီး base64 ဖြင့် encode လုပ်ပြီး HTML image tag တစ်ခု ဖန်တီးထားပါတယ်။

7. **စာသားနဲ့ ပုံကို Prompt တစ်ခုအဖြစ် ပေါင်းစပ်ခြင်း**  
    ```python
    prompt = f"{text} {image}"
    ```  
    စာသား prompt နဲ့ HTML image tag ကို တစ်ခုတည်းသော string အဖြစ် ပေါင်းစပ်ထားပါတယ်။

8. **ChatNVIDIA ကို အသုံးပြုပြီး ကုဒ်ထုတ်ယူခြင်း**  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    ဒီကုဒ်က prompt ကို `ChatNVIDIA` model ထံ ပို့ပြီး ထုတ်ပေးတဲ့ကုဒ်ကို အပိုင်းပိုင်း စုဆောင်း၊ ပုံနှိပ်ပြီး `code` string ထဲ ထည့်သွင်းပါတယ်။

9. **ထုတ်ပေးတဲ့အကြောင်းအရာထဲက Python ကုဒ်ကို ခွဲထုတ်ခြင်း**  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    ဒီနည်းလမ်းက markdown ဖော်မတ်တွေကို ဖယ်ရှားပြီး အမှန်တကယ် Python ကုဒ်ကို ခွဲထုတ်ယူတာဖြစ်ပါတယ်။

10. **ထုတ်ယူထားတဲ့ ကုဒ်ကို လုပ်ဆောင်ခြင်း**  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    ဒီကုဒ်က ခွဲထုတ်ထားတဲ့ Python ကုဒ်ကို subprocess အဖြစ် run လိုက်ပြီး output ကို ဖမ်းယူပါတယ်။

11. **ပုံတွေကို ပြသခြင်း**  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    ဒီလိုင်းတွေက `IPython.display` module ကို အသုံးပြုပြီး ပုံတွေကို ပြသပေးတာဖြစ်ပါတယ်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများ သို့မဟုတ် မှားဖတ်ရှုမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။