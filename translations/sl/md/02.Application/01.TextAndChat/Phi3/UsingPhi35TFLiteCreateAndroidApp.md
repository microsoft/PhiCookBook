<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:51:19+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "sl"
}
-->
# **Microsoft Phi-3.5 tflite භාවිතයෙන් Android ඇප් එකක් සාදන්න**

මෙය Microsoft Phi-3.5 tflite ආකෘති භාවිතා කරන Android නියැදි උදාහරණයකි.

## **📚 දැනුම**

Android LLM Inference API ඔබට Android යෙදුම් සඳහා විශාල භාෂා ආකෘති (LLMs) සම්පූර්ණයෙන්ම උපාංගයේම ධාවනය කිරීමට ඉඩ සලසයි. මෙය පෙළ ජනනය කිරීම, ස්වාභාවික භාෂා ආකාරයෙන් තොරතුරු ලබා ගැනීම, සහ ලේඛන සාරාංශ කිරීම වැනි විවිධ කාර්යයන් සඳහා භාවිතා කළ හැක. මෙම කාර්යය බහු පෙළ-තෙක්ස්ට් විශාල භාෂා ආකෘති සඳහා ඇතුලත් සහාය සපයන අතර, ඔබට නවතම උපාංග-මත ජනක AI ආකෘති ඔබේ Android යෙදුම් සඳහා භාවිතා කළ හැක.

Google AI Edge Torch යනු PyTorch ආකෘති .tflite ආකෘතියකට පරිවර්තනය කිරීමට සහය දක්වන Python පුස්තකාලයක් වන අතර, එම ආකෘති TensorFlow Lite සහ MediaPipe සමඟ ධාවනය කළ හැක. මෙය Android, iOS සහ IoT යෙදුම් සඳහා සම්පූර්ණයෙන්ම උපාංගයේම ආකෘති ධාවනය කිරීමට ඉඩ සලසයි. AI Edge Torch පුළුල් CPU ආවරණයක් සහ ආරම්භක GPU සහ NPU සහාය දක්වයි. AI Edge Torch PyTorch සමඟ ආසන්නව ඒකාබද්ධ වීමට උත්සාහ කරමින් torch.export() මත පදනම්ව Core ATen ක්‍රියාකාරකම් හොඳ ආවරණයක් සපයයි.

## **🪬 මාර්ගෝපදේශය**

### **🔥 Microsoft Phi-3.5 tflite සඳහා පරිවර්තනය කිරීම**

0. මෙම උදාහරණය Android 14+ සඳහා වේ

1. Python 3.10.12 ස්ථාපනය කරන්න

***උපදෙස්:*** conda භාවිතා කර Python පරිසරය ස්ථාපනය කරන්න

2. Ubuntu 20.04 / 22.04 (කරුණාකර [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) වෙත අවධානය යොමු කරන්න)

***උපදෙස්:*** Azure Linux VM හෝ තෙවන පාර්ශව වලාකුළු VM භාවිතා කර පරිසරය සාදන්න

3. Linux bash වෙත ගොස් Python පුස්තකාල ස්ථාපනය කරන්න

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging face වෙතින් Microsoft-3.5-Instruct බාගන්න

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 tflite වෙත පරිවර්තනය කරන්න

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 Android Mediapipe Bundle වෙත පරිවර්තනය කිරීම**

පළමුව mediapipe ස්ථාපනය කරන්න

```bash

pip install mediapipe

```

මෙම කේතය [ඔබගේ notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) තුළ ධාවනය කරන්න

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 adb push භාවිතයෙන් task ආකෘතිය ඔබේ Android උපාංගයේ මාර්ගයට යවන්න**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 ඔබේ Android කේතය ධාවනය කිරීම**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.sl.png)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.