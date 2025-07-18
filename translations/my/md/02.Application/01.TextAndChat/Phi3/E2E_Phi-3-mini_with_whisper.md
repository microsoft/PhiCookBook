<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:24:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "my"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## အနှစ်ချုပ်

Interactive Phi 3 Mini 4K Instruct Chatbot သည် Microsoft Phi 3 Mini 4K instruct demo နှင့် စာသား သို့မဟုတ် အသံအချက်အလက်ဖြင့် အပြန်အလှန် ဆက်သွယ်နိုင်စေသော ကိရိယာတစ်ခုဖြစ်သည်။ ဤ chatbot ကို ဘာသာပြန်ခြင်း၊ ရာသီဥတု အချက်အလက်များ၊ နှင့် အထွေထွေ သတင်းအချက်အလက် စုဆောင်းခြင်းကဲ့သို့သော အလုပ်များအတွက် အသုံးပြုနိုင်သည်။

### စတင်အသုံးပြုခြင်း

ဤ chatbot ကို အသုံးပြုရန် အောက်ပါ လမ်းညွှန်ချက်များကို လိုက်နာပါ-

1. အသစ်သော [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ဖိုင်ကို ဖွင့်ပါ။
2. notebook ၏ မူလပြတင်းပေါ်တွင် စာသားထည့်ရန် အကွက်နှင့် "Send" ခလုတ်ပါသော chatbox အင်တာဖေ့စ်ကို တွေ့မြင်ရမည်။
3. စာသားအခြေပြု chatbot ကို အသုံးပြုရန် သင်၏စာကို စာသားထည့်သည့်အကွက်တွင် ရိုက်ထည့်ပြီး "Send" ခလုတ်ကို နှိပ်ပါ။ chatbot သည် notebook အတွင်းမှ တိုက်ရိုက်ဖွင့်နိုင်သော အသံဖိုင်ဖြင့် တုံ့ပြန်ပေးမည်ဖြစ်သည်။

**Note**: ဤကိရိယာသည် GPU နှင့် Microsoft Phi-3 နှင့် OpenAI Whisper မော်ဒယ်များသို့ ဝင်ရောက်ခွင့် လိုအပ်ပြီး၊ အသံအသိအမှတ်ပြုခြင်းနှင့် ဘာသာပြန်ခြင်းအတွက် အသုံးပြုသည်။

### GPU လိုအပ်ချက်များ

ဤ demo ကို လည်ပတ်ရန် 12GB GPU မှတ်ဉာဏ် လိုအပ်သည်။

**Microsoft-Phi-3-Mini-4K instruct** demo ကို GPU ပေါ်တွင် လည်ပတ်ရာတွင် အသုံးပြုမည့် မှတ်ဉာဏ်အရေအတွက်သည် အချက်အလက်အမျိုးအစား (အသံ သို့မဟုတ် စာသား), ဘာသာပြန်ရန် အသုံးပြုသော ဘာသာစကား, မော်ဒယ်၏ အမြန်နှုန်းနှင့် GPU တွင် ရရှိနိုင်သော မှတ်ဉာဏ်ပမာဏ စသည့် အချက်အလက်များပေါ် မူတည်သည်။

Whisper မော်ဒယ်ကို GPU ပေါ်တွင် လည်ပတ်ရန် ဒီဇိုင်းဆွဲထားပြီး၊ Whisper မော်ဒယ်ကို လည်ပတ်ရန် အနည်းဆုံး GPU မှတ်ဉာဏ် 8GB ကို အကြံပြုထားသော်လည်း လိုအပ်ပါက ပိုမိုကြီးမားသော မှတ်ဉာဏ်ကိုလည်း ကိုင်တွယ်နိုင်သည်။

အချက်အလက်များ များပြားစွာ သို့မဟုတ် တောင်းဆိုမှုများ အများအပြားကို မော်ဒယ်ပေါ်တွင် လည်ပတ်ပါက ပိုမိုများသော GPU မှတ်ဉာဏ် လိုအပ်နိုင်ပြီး၊ စွမ်းဆောင်ရည် ပြဿနာများ ဖြစ်ပေါ်နိုင်သည်။ သင့်အသုံးပြုမှုအတွက် အကောင်းဆုံး ဆက်တင်များကို သတ်မှတ်ရန် အမျိုးမျိုးသော ဖွဲ့စည်းမှုများဖြင့် စမ်းသပ်ပြီး မှတ်ဉာဏ် အသုံးပြုမှုကို စောင့်ကြည့်ရန် အကြံပြုသည်။

## E2E နမူနာ - Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ဟု ခေါင်းစဉ်ပေးထားသော jupyter notebook သည် Microsoft Phi 3 Mini 4K instruct Demo ကို အသံ သို့မဟုတ် စာသားအချက်အလက်မှ စာသားထုတ်လုပ်ရန် မည်သို့ အသုံးပြုရမည်ကို ပြသသည်။ notebook တွင် အောက်ပါ function များကို သတ်မှတ်ထားသည်-

1. `tts_file_name(text)`: ဤ function သည် ထုတ်လုပ်မည့် အသံဖိုင်ကို သိမ်းဆည်းရန် အခြေခံပြီး စာသားအရ ဖိုင်နာမည်တစ်ခု ဖန်တီးပေးသည်။
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: ဤ function သည် Edge TTS API ကို အသုံးပြု၍ စာသားအပိုင်းများ စာရင်းမှ အသံဖိုင်တစ်ခု ဖန်တီးပေးသည်။ input parameter များမှာ စာသားအပိုင်းများ စာရင်း၊ စကားပြောနှုန်း၊ အသံအမည်နှင့် ထုတ်လုပ်ထားသော အသံဖိုင် သိမ်းဆည်းမည့် လမ်းကြောင်းဖြစ်သည်။
3. `talk(input_text)`: ဤ function သည် Edge TTS API ကို အသုံးပြု၍ အသံဖိုင်တစ်ခု ဖန်တီးပြီး /content/audio ဖိုလ်ဒါအတွင်း အမှတ်မထင် ဖိုင်နာမည်ဖြင့် သိမ်းဆည်းပေးသည်။ input parameter သည် စကားပြောသို့ ပြောင်းလဲလိုသော စာသားဖြစ်သည်။
4. `run_text_prompt(message, chat_history)`: ဤ function သည် Microsoft Phi 3 Mini 4K instruct demo ကို အသုံးပြု၍ စာသား input မှ အသံဖိုင်တစ်ခု ဖန်တီးပြီး chat history ထဲသို့ ထည့်သွင်းပေးသည်။
5. `run_audio_prompt(audio, chat_history)`: ဤ function သည် Whisper model API ကို အသုံးပြု၍ အသံဖိုင်ကို စာသားသို့ ပြောင်းလဲပြီး `run_text_prompt()` function သို့ ပေးပို့သည်။
6. ကုဒ်သည် Gradio app တစ်ခုကို စတင်ပြီး အသုံးပြုသူများအား စာသားရိုက်ထည့်ခြင်း သို့မဟုတ် အသံဖိုင်များ တင်ခြင်းဖြင့် Phi 3 Mini 4K instruct demo နှင့် ဆက်သွယ်နိုင်စေသည်။ ထွက်ရှိလာသော အချက်အလက်ကို app အတွင်း စာသားအဖြစ် ပြသသည်။

## ပြဿနာဖြေရှင်းခြင်း

Cuda GPU driver များ ထည့်သွင်းခြင်း

1. သင့် Linux application များကို နောက်ဆုံးပေါ် အဆင့်သို့ အပ်ဒိတ်လုပ်ထားပါစေ။

    ```bash
    sudo apt update
    ```

2. Cuda Drivers များ ထည့်သွင်းပါ။

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. cuda driver တည်နေရာကို မှတ်ပုံတင်ပါ။

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Nvidia GPU မှတ်ဉာဏ် အရွယ်အစား စစ်ဆေးခြင်း (12GB GPU မှတ်ဉာဏ် လိုအပ်သည်)

    ```bash
    nvidia-smi
    ```

5. Cache ကို ဖျက်ပါ - PyTorch ကို အသုံးပြုပါက torch.cuda.empty_cache() ကို ခေါ်၍ မသုံးသော cache မှတ်ဉာဏ်အားလုံးကို လွှတ်ပေးနိုင်သည်၊ ထို့ကြောင့် အခြား GPU application များ အသုံးပြုနိုင်မည်ဖြစ်သည်။

    ```python
    torch.cuda.empty_cache() 
    ```

6. Nvidia Cuda ကို စစ်ဆေးပါ။

    ```bash
    nvcc --version
    ```

7. Hugging Face token တစ်ခု ဖန်တီးရန် အောက်ပါ အဆင့်များကို လုပ်ဆောင်ပါ။

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) သို့ သွားပါ။
    - **New token** ကို ရွေးချယ်ပါ။
    - အသုံးပြုလိုသော project **Name** ကို ထည့်ပါ။
    - **Type** ကို **Write** အဖြစ် ရွေးချယ်ပါ။

> **Note**
>
> အောက်ပါ error ကို တွေ့ရှိပါက-
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> ဤပြဿနာကို ဖြေရှင်းရန် terminal အတွင်း အောက်ပါ command ကို ရိုက်ထည့်ပါ။
>
> ```bash
> sudo ldconfig
> ```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။