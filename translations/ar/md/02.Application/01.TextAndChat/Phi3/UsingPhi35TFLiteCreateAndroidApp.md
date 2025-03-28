<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-03-27T11:07:06+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ar"
}
-->
# **استخدام Microsoft Phi-3.5 tflite لإنشاء تطبيق أندرويد**

هذا نموذج لتطبيق أندرويد يستخدم نماذج Microsoft Phi-3.5 tflite.

## **📚 المعرفة**

تتيح واجهة برمجة التطبيقات Android LLM Inference تشغيل نماذج اللغة الكبيرة (LLMs) بالكامل على الجهاز لتطبيقات أندرويد، والتي يمكنك استخدامها لأداء مجموعة واسعة من المهام، مثل إنشاء النصوص، واسترجاع المعلومات بصيغة اللغة الطبيعية، وتلخيص المستندات. توفر المهمة دعمًا مدمجًا لعدة نماذج لغة كبيرة تعمل بنظام النص إلى النص، مما يمكنك من تطبيق أحدث نماذج الذكاء الاصطناعي التوليدية على جهازك الأندرويد.

Google AI Edge Torch هي مكتبة بايثون تدعم تحويل نماذج PyTorch إلى صيغة .tflite، والتي يمكن تشغيلها باستخدام TensorFlow Lite و MediaPipe. هذا يتيح تطبيقات لأجهزة أندرويد، iOS، و IoT التي يمكنها تشغيل النماذج بالكامل على الجهاز. توفر AI Edge Torch تغطية واسعة لوحدة المعالجة المركزية، مع دعم مبدئي لوحدة معالجة الرسومات (GPU) ووحدة المعالجة العصبية (NPU). تسعى AI Edge Torch للتكامل الوثيق مع PyTorch، بناءً على وظيفة torch.export() وتقديم تغطية جيدة لمشغلي Core ATen.

## **🪬 الإرشادات**

### **🔥 تحويل Microsoft Phi-3.5 إلى دعم tflite**

0. هذا النموذج مخصص لأندرويد 14+

1. قم بتثبيت Python 3.10.12

***اقتراح:*** استخدام conda لتثبيت بيئة Python الخاصة بك

2. Ubuntu 20.04 / 22.04 (يرجى التركيز على [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***اقتراح:*** استخدام Azure Linux VM أو VM من طرف ثالث لإنشاء بيئتك

3. انتقل إلى bash الخاص بلينكس لتثبيت مكتبة Python 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. قم بتنزيل Microsoft-3.5-Instruct من Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. قم بتحويل Microsoft Phi-3.5 إلى tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 تحويل Microsoft Phi-3.5 إلى حزمة Mediapipe لأندرويد**

يرجى تثبيت mediapipe أولاً

```bash

pip install mediapipe

```

قم بتشغيل هذا الكود في [دفترك](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 استخدام adb لنقل نموذج المهمة إلى مسار جهاز أندرويد الخاص بك**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 تشغيل الكود الخاص بتطبيق أندرويد**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.ar.png)

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الرسمي. للحصول على معلومات حيوية، يُوصى باستخدام ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.