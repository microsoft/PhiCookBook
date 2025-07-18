<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:51:32+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ne"
}
-->
# **Microsoft Phi-3.5 tflite प्रयोग गरेर Android एप बनाउने**

यो Microsoft Phi-3.5 tflite मोडेलहरू प्रयोग गरी बनाइएको Android नमूना हो।

## **📚 ज्ञान**

Android LLM Inference API ले तपाईंलाई Android एपहरूमा ठूलो भाषा मोडेलहरू (LLMs) पूर्ण रूपमा डिभाइसमै चलाउन अनुमति दिन्छ, जसले तपाईंलाई विभिन्न कार्यहरू गर्न मद्दत गर्छ, जस्तै पाठ सिर्जना गर्नु, प्राकृतिक भाषामा जानकारी प्राप्त गर्नु, र कागजातहरू संक्षेप गर्नु। यो कार्यले धेरै पाठ-देखि-पाठ ठूलो भाषा मोडेलहरूको built-in समर्थन प्रदान गर्दछ, जसले तपाईंलाई नवीनतम on-device जनरेटिभ AI मोडेलहरू तपाईंको Android एपहरूमा लागू गर्न सक्षम बनाउँछ।

Google AI Edge Torch एक python लाइब्रेरी हो जसले PyTorch मोडेलहरूलाई .tflite ढाँचामा रूपान्तरण गर्न समर्थन गर्छ, जुन पछि TensorFlow Lite र MediaPipe सँग चलाउन सकिन्छ। यसले Android, iOS र IoT का लागि पूर्ण रूपमा डिभाइसमै मोडेलहरू चलाउन सक्ने एप्लिकेसनहरू सक्षम बनाउँछ। AI Edge Torch ले CPU को व्यापक समर्थन दिन्छ, प्रारम्भिक GPU र NPU समर्थनसहित। AI Edge Torch ले PyTorch सँग नजिकबाट एकीकृत हुन खोज्छ, torch.export() माथि निर्माण गर्दै र Core ATen अपरेटरहरूको राम्रो समर्थन प्रदान गर्दै।

## **🪬 मार्गनिर्देशन**

### **🔥 Microsoft Phi-3.5 लाई tflite समर्थनमा रूपान्तरण गर्ने**

0. यो नमूना Android 14+ का लागि हो

1. Python 3.10.12 इन्स्टल गर्नुहोस्

***सुझाव:*** conda प्रयोग गरेर आफ्नो Python वातावरण इन्स्टल गर्नुहोस्

2. Ubuntu 20.04 / 22.04 (कृपया [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) मा ध्यान दिनुहोस्)

***सुझाव:*** Azure Linux VM वा तेस्रो पक्षको क्लाउड VM प्रयोग गरेर आफ्नो वातावरण तयार गर्नुहोस्

3. आफ्नो Linux bash मा जानुहोस् र Python लाइब्रेरी इन्स्टल गर्नुहोस्

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging face बाट Microsoft-3.5-Instruct डाउनलोड गर्नुहोस्

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 लाई tflite मा रूपान्तरण गर्नुहोस्

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 लाई Android Mediapipe Bundle मा रूपान्तरण गर्ने**

पहिले mediapipe इन्स्टल गर्नुहोस्

```bash

pip install mediapipe

```

यो कोड [तपाईंको नोटबुक](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) मा चलाउनुहोस्

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

### **🔥 adb push प्रयोग गरेर मोडेललाई तपाईंको Android उपकरणको पथमा पठाउने**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 तपाईंको Android कोड चलाउने**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.ne.png)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।