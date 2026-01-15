<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-07-17T02:48:33+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "my"
}
-->
# **OnnxRuntime GenAI Windows GPU အတွက် လမ်းညွှန်ချက်**

ဤလမ်းညွှန်ချက်သည် Windows ပေါ်တွင် GPU များနှင့် ONNX Runtime (ORT) ကို စတင်တပ်ဆင်ပြီး အသုံးပြုနည်းအဆင့်များကို ဖော်ပြထားသည်။ သင့်မော်ဒယ်များအတွက် GPU အမြန်နှုန်းမြှင့်တင်မှုကို အသုံးချနိုင်ရန်၊ စွမ်းဆောင်ရည်နှင့် ထိရောက်မှုကို တိုးတက်စေဖို့ ရည်ရွယ်ထားသည်။

စာရွက်တွင် ပါဝင်သော အကြောင်းအရာများမှာ -

- ပတ်ဝန်းကျင် တပ်ဆင်ခြင်း - CUDA, cuDNN နှင့် ONNX Runtime ကဲ့သို့ လိုအပ်သော အခြေခံပစ္စည်းများ တပ်ဆင်နည်း။
- ဖွဲ့စည်းမှု - GPU အရင်းအမြစ်များကို ထိရောက်စွာ အသုံးပြုနိုင်ရန် ပတ်ဝန်းကျင်နှင့် ONNX Runtime ကို ပြင်ဆင်နည်း။
- အကောင်းဆုံး စွမ်းဆောင်ရည်ရရှိစေရန် GPU ဆက်တင်များကို ပြင်ဆင်ခြင်းအကြံပြုချက်များ။

### **1. Python 3.10.x /3.11.8**

   ***Note*** သင့် Python ပတ်ဝန်းကျင်အဖြစ် [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) ကို အသုံးပြုရန် အကြံပြုသည်။

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Reminder*** Python ONNX library များကို တပ်ဆင်ထားပါက အရင်ဆုံး ဖယ်ရှားပစ်ပါ။

### **2. winget ဖြင့် CMake တပ်ဆင်ခြင်း**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Visual Studio 2022 - Desktop Development with C++ တပ်ဆင်ခြင်း**

   ***Note*** သင် compile မလုပ်ချင်ပါက ဤအဆင့်ကို ကျော်လွှားနိုင်သည်။

![CPP](../../../../../../translated_images/my/01.42f52a2b2aedff02.png)

### **4. NVIDIA Driver တပ်ဆင်ခြင်း**

1. **NVIDIA GPU Driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Reminder*** တပ်ဆင်ရာတွင် ပုံမှန် အဆင့်ဆင့်ကို အသုံးပြုပါ။

### **5. NVIDIA ပတ်ဝန်းကျင် ပြင်ဆင်ခြင်း**

NVIDIA CUDNN 9.4 ရဲ့ lib, bin, include ဖိုင်များကို NVIDIA CUDA 12.4 ရဲ့ lib, bin, include ထဲသို့ ကူးယူပါ။

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* ဖိုင်များကို *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'* ထဲသို့ ကူးပါ။

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* ဖိုင်များကို *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'* ထဲသို့ ကူးပါ။

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* ဖိုင်များကို *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'* ထဲသို့ ကူးပါ။

### **6. Phi-3.5-mini-instruct-onnx ကို ဒေါင်းလုပ်လုပ်ခြင်း**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. InferencePhi35Instruct.ipynb ကို လည်ပတ်ခြင်း**

   [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) ကို ဖွင့်ပြီး အကောင်အထည်ဖော်ပါ။

![RESULT](../../../../../../translated_images/my/02.b9b06996cf7255d5.png)

### **8. ORT GenAI GPU ကို Compile လုပ်ခြင်း**

   ***Note*** 
   
   1. onnx, onnxruntime နှင့် onnxruntime-genai အားလုံးကို အရင်ဆုံး ဖယ်ရှားပစ်ပါ။

   ```bash

   pip list 
   
   ```

   ထို့နောက် onnxruntime library များအားလုံးကို ဖယ်ရှားပစ်ပါ။

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Visual Studio Extension ကို စစ်ဆေးပါ။

   C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras တွင် C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration ဖိုင်လ်ရှိမရှိ စစ်ဆေးပါ။ မရှိပါက အခြား Cuda toolkit driver ဖိုလ်ဒါများထဲမှ visual_studio_integration ဖိုလ်ဒါနှင့် အတွင်းဖိုင်များကို ကူးယူပြီး C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration ထဲသို့ ထည့်ပါ။

   - compile မလုပ်ချင်ပါက ဤအဆင့်ကို ကျော်လွှားနိုင်သည်။

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip) ကို ဒေါင်းလုပ်လုပ်ပါ။

   - onnxruntime-win-x64-gpu-1.19.2.zip ကို ဖွင့်ပြီး **ort** ဟု အမည်ပြောင်းပြီး onnxruntime-genai ထဲသို့ ကူးပါ။

   - Windows Terminal ကို အသုံးပြု၍ Developer Command Prompt for VS 2022 သို့ ဝင်ပြီး onnxruntime-genai သို့ သွားပါ။

![RESULT](../../../../../../translated_images/my/03.b83ce473d5ff9b9b.png)

   - သင့် Python ပတ်ဝန်းကျင်ဖြင့် compile လုပ်ပါ။

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။