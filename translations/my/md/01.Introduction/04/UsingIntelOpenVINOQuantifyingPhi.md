<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-09T19:45:16+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "my"
}
-->
# **Intel OpenVINO ဖြင့် Phi-3.5 ကို Quantize လုပ်ခြင်း**

Intel သည် အသုံးပြုသူများစွာရှိသော အကြာကြီးတည်ရှိနေသော CPU ထုတ်လုပ်သူဖြစ်သည်။ မက်ရှင်လေ့လာမှုနှင့် နက်ရှိုင်းသောလေ့လာမှုများ တိုးတက်လာခြင်းနှင့်အမျှ Intel သည် AI အမြန်ဆောင်မှုယှဉ်ပြိုင်မှုတွင်ပါဝင်လာသည်။ မော်ဒယ် inference အတွက် Intel သည် GPU နှင့် CPU များသာမက NPU များကိုလည်း အသုံးပြုသည်။

Phi-3.x မျိုးဆက်ကို အဆုံးပိုင်းတွင် တပ်ဆင်ရန် မျှော်လင့်ထားပြီး AI PC နှင့် Copilot PC အတွက် အရေးကြီးဆုံး အစိတ်အပိုင်းဖြစ်လာရန် ရည်ရွယ်သည်။ အဆုံးပိုင်းတွင် မော်ဒယ်ကို တင်သွင်းခြင်းသည် ကွဲပြားသော hardware ထုတ်လုပ်သူများ၏ ပူးပေါင်းဆောင်ရွက်မှုပေါ် မူတည်သည်။ ဤအခန်းတွင် Intel OpenVINO ကို quantitative မော်ဒယ်အဖြစ် အသုံးပြုမှုအခြေအနေကို အဓိကထား ရေးသားထားသည်။

## **OpenVINO ဆိုတာဘာလဲ**

OpenVINO သည် cloud မှ edge အထိ နက်ရှိုင်းသောလေ့လာမှု မော်ဒယ်များကို အမြန်ဆုံး အကောင်းဆုံး ပြုပြင်တိုးတက်စေပြီး တပ်ဆင်နိုင်ရန် အတွက် ဖွင့်လှစ်ထားသော ကိရိယာစုစည်းမှုတစ်ခုဖြစ်သည်။ PyTorch, TensorFlow, ONNX စသည့် လူကြိုက်များသော framework များမှ မော်ဒယ်များကို အသုံးပြု၍ generative AI, ဗီဒီယို၊ အသံနှင့် ဘာသာစကားကဲ့သို့သော အသုံးပြုမှုအမျိုးမျိုးတွင် နက်ရှိုင်းသောလေ့လာမှု inference ကို မြန်ဆန်စေသည်။ မော်ဒယ်များကို ပြောင်းလဲ optimize လုပ်ပြီး Intel® hardware နှင့် ပတ်ဝန်းကျင်များတွင်၊ on-premises နှင့် on-device၊ browser သို့မဟုတ် cloud တွင် တပ်ဆင်နိုင်သည်။

ယခု OpenVINO ဖြင့် Intel hardware တွင် GenAI မော်ဒယ်ကို အလျင်အမြန် quantize လုပ်၍ မော်ဒယ်ကို မြန်ဆန်စွာ ရည်ညွှန်းနိုင်ပါပြီ။

ယခု OpenVINO သည် Phi-3.5-Vision နှင့် Phi-3.5 Instruct မော်ဒယ်များ၏ quantization ပြောင်းလဲမှုကို ထောက်ပံ့ပေးသည်။

### **ပတ်ဝန်းကျင် ပြင်ဆင်ခြင်း**

အောက်ပါ ပတ်ဝန်းကျင်လိုအပ်ချက်များကို ထည့်သွင်းထားကြောင်း သေချာစေပါ၊ ၎င်းသည် requirement.txt ဖြစ်သည်။

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO ဖြင့် Phi-3.5-Instruct ကို Quantize လုပ်ခြင်း**

Terminal တွင် အောက်ပါ script ကို ပြေးပါ။

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO ဖြင့် Phi-3.5-Vision ကို Quantize လုပ်ခြင်း**

Python သို့မဟုတ် Jupyter lab တွင် အောက်ပါ script ကို ပြေးပါ။

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Intel OpenVINO နှင့် Phi-3.5 အတွက် နမူနာများ**

| Labs    | မိတ်ဆက်ချက် | သွားရန် |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | AI PC တွင် Phi-3.5 Instruct ကို မည်သို့ အသုံးပြုရမည်ကို သင်ယူပါ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | AI PC တွင် Phi-3.5 Vision ဖြင့် ပုံများကို မည်သို့ စိစစ်ရမည်ကို သင်ယူပါ      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | AI PC တွင် Phi-3.5 Vision ဖြင့် ဗီဒီယိုများကို မည်သို့ စိစစ်ရမည်ကို သင်ယူပါ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **အရင်းအမြစ်များ**

1. Intel OpenVINO အကြောင်း ပိုမိုလေ့လာရန် [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းသည် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။