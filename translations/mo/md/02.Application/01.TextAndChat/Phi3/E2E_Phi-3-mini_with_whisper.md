<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-07T14:11:24+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "mo"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

Interactive Phi 3 Mini 4K Instruct Chatbot သည် Microsoft Phi 3 Mini 4K instruct demo နှင့် စာသား သို့မဟုတ် အသံအချက်အလက်ဖြင့် အပြန်အလှန် ဆက်သွယ်နိုင်သော ကိရိယာတစ်ခုဖြစ်သည်။ ဤ chatbot ကို ဘာသာပြန်ခြင်း၊ မိုးလေဝသ အချက်အလက်များ ရယူခြင်း၊ သတင်းအချက်အလက် စုဆောင်းခြင်း စသည့် အလုပ်များအတွက် အသုံးပြုနိုင်သည်။

### Getting Started

ဤ chatbot ကို အသုံးပြုရန် အောက်ပါ အဆင့်များကို လိုက်နာပါ-

1. အသစ်သော [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ဖိုင်ကို ဖွင့်ပါ။
2. notebook ရဲ့ အဓိက ပြတင်းပေါ်တွင် စကားပြောမှုအတွက် စာသား ထည့်ရန် နေရာနှင့် "Send" ခလုတ်ပါသော chatbox interface ကို တွေ့မြင်ရမည်။
3. စာသားအခြေခံ chatbot ကို အသုံးပြုလိုပါက စာသား ထည့်သွင်းရန် နေရာတွင် မက်ဆေ့ခ်ျ ရိုက်ထည့်ပြီး "Send" ခလုတ်ကို နှိပ်ပါ။ chatbot သည် notebook အတွင်းမှ တိုက်ရိုက်ဖွင့်၍ နားဆင်နိုင်သော အသံဖိုင်ဖြင့် တုံ့ပြန်မည်ဖြစ်သည်။

**Note**: ဤကိရိယာသည် GPU နှင့် Microsoft Phi-3 နှင့် OpenAI Whisper မော်ဒယ်များသို့ ဝင်ရောက်ခွင့်လိုအပ်ပြီး၊ Whisper ကို အသံမှ စာသားသို့ ပြောင်းခြင်းနှင့် ဘာသာပြန်ခြင်းအတွက် အသုံးပြုသည်။

### GPU Requirements

ဤ demonstration ကို ပြေးရန် 12Gb GPU မှတ်ဉာဏ် လိုအပ်သည်။

**Microsoft-Phi-3-Mini-4K instruct** demo ကို GPU ပေါ်တွင် ပြေးရန် လိုအပ်သော မှတ်ဉာဏ်ပမာဏမှာ input data (အသံ သို့မဟုတ် စာသား) အရွယ်အစား၊ ဘာသာပြန်ရန် သုံးသော ဘာသာစကား၊ မော်ဒယ်၏ အမြန်နှုန်းနှင့် GPU တွင် ရနိုင်သော မှတ်ဉာဏ် ပမာဏ စသည်တို့ပေါ် မူတည်သည်။

Whisper မော်ဒယ်သည် GPU ပေါ်တွင် ပြေးရန် ဒီဇိုင်းထုတ်ထားပြီး၊ Whisper မော်ဒယ်အတွက် အနည်းဆုံး GPU မှတ်ဉာဏ်အရေအတွက်မှာ 8 GB ဖြစ်သော်လည်း လိုအပ်ပါက ပိုမိုမြင့်မားသော မှတ်ဉာဏ်ကို ဆက်လက်ကိုင်တွယ်နိုင်သည်။

အချက်အလက်များ အများအပြား သို့မဟုတ် မော်ဒယ်အပေါ် အမိန့်များ အများကြီး ပေးပို့သည်ဆိုပါက ပိုမိုများသော GPU မှတ်ဉာဏ် လိုအပ်နိုင်ပြီး စွမ်းဆောင်ရည် ပြဿနာများ ဖြစ်ပေါ်နိုင်သည်။ သင့်အသုံးပြုမှုအတွက် အမျိုးမျိုးသော ဆက်တင်များဖြင့် စမ်းသပ်ပြီး မှတ်ဉာဏ်အသုံးပြုမှုကို စောင့်ကြည့်ကာ သင့်လိုအပ်ချက်များအတွက် အကောင်းဆုံး ဆက်တင်များကို ရှာဖွေရန် အကြံပြုသည်။

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ဟုခေါ်သော jupyter notebook သည် Microsoft Phi 3 Mini 4K instruct Demo ကို အသံ သို့မဟုတ် စာသား input မှ စာသား ထုတ်ယူရန် ဘယ်လို အသုံးပြုရမည်ကို ဖော်ပြသည်။ notebook တွင် function များအတော်များများကို သတ်မှတ်ထားသည်-

1. `tts_file_name(text)`: စာသား input အပေါ် မူတည်၍ ဖိုင်နာမည်တစ်ခု ထုတ်ပေးပြီး ထုတ်လုပ်ထားသော အသံဖိုင်ကို သိမ်းဆည်းရန် အသုံးပြုသည်။
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Edge TTS API ကို အသုံးပြု၍ စာသား input ချုပ်စုများ စာရင်းမှ အသံဖိုင်တစ်ခု ထုတ်လုပ်သည်။ input parameters တွင် ချုပ်စုများစာရင်း၊ စကားပြောနှုန်း၊ အသံအမည်နှင့် ထုတ်လုပ်ထားသော အသံဖိုင် သိမ်းဆည်းမည့် လမ်းကြောင်း ပါဝင်သည်။
1. `talk(input_text)`: Edge TTS API ကို အသုံးပြု၍ အသံဖိုင်တစ်ခု ထုတ်လုပ်ပြီး /content/audio ဖိုလ်ဒါတွင် အမည်မသိ ဖိုင်အမည်ဖြင့် သိမ်းဆည်းသည်။ input parameter သည် အသံသို့ ပြောင်းလိုသော စာသားဖြစ်သည်။
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instruct demo ကို အသုံးပြု၍ မက်ဆေ့ခ်ျ input မှ အသံဖိုင်တစ်ခု ထုတ်လုပ်ပြီး chat history တွင် ထည့်သွင်းသည်။
1. `run_audio_prompt(audio, chat_history)`: Whisper model API ကို အသုံးပြု၍ အသံဖိုင်ကို စာသားသို့ ပြောင်းပြီး `run_text_prompt()` function သို့ ပေးပို့သည်။
1. code သည် Gradio app ကို စတင်ကာ အသုံးပြုသူများအား မက်ဆေ့ခ်ျ ရိုက်ထည့်ခြင်း သို့မဟုတ် အသံဖိုင်တင်ခြင်းဖြင့် Phi 3 Mini 4K instruct demo နှင့် ဆက်သွယ်နိုင်စေရန် ခွင့်ပြုသည်။ output ကို app အတွင်း စာသား မက်ဆေ့ခ်ျအဖြစ် ပြသသည်။

## Troubleshooting

Cuda GPU drivers 설치하기

1. သင့် Linux application များကို နောက်ဆုံး version သို့ update လုပ်ပါ

    ```bash
    sudo apt update
    ```

1. Cuda Drivers 설치하기

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. cuda driver တည်နေရာ မှတ်ပုံတင်ပါ

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU မှတ်ဉာဏ် အရွယ်အစား စစ်ဆေးခြင်း (12GB GPU Memory လိုအပ်သည်)

    ```bash
    nvidia-smi
    ```

1. Cache ဖျက်ခြင်း: PyTorch ကို အသုံးပြုပါက torch.cuda.empty_cache() ကို ခေါ်၍ မသုံးသော cached memory များအားလုံးကို လွှတ်ပေးနိုင်ပြီး အခြား GPU application များအသုံးပြုနိုင်ပါသည်။

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda စစ်ဆေးခြင်း

    ```bash
    nvcc --version
    ```

1. Hugging Face token တစ်ခု ဖန်တီးရန် အောက်ပါ လုပ်ဆောင်ချက်များ ပြုလုပ်ပါ-

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) သို့ သွားပါ။
    - **New token** ကို ရွေးချယ်ပါ။
    - အသုံးပြုလိုသော project **Name** ကို ထည့်သွင်းပါ။
    - **Type** ကို **Write** အဖြစ် ရွေးချယ်ပါ။

> **Note**
>
> အောက်ပါ error ကို ကြုံတွေ့ပါက-
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> ပြဿနာကို ဖြေရှင်းရန် terminal အတွင်း အောက်ပါ command ကို ရိုက်ထည့်ပါ။
>
> ```bash
> sudo ldconfig
> ```

**Disclaimer**:  
Dis document ha bin transleit yuseng AI transleit serviss [Co-op Translator](https://github.com/Azure/co-op-translator). Wai wi traiv for akyurasie, plis no dat otomated transleits mebi get erors or inakyerasis. Di orijinal document in im neitiv langwij shud bi konsiderd di otoritetiv sors. For kritikol informashon, profeshonal human transleit iz rekomended. Wi no responsibol for eni misandastandin or misinterpretashon dat kam from yus of dis transleit.