<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:49:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "he"
}
-->
# **שימוש ב-Microsoft Phi-3.5 tflite ליצירת אפליקציית אנדרואיד**

זהו דוגמה לאנדרואיד המשתמשת במודלים של Microsoft Phi-3.5 tflite.

## **📚 ידע**

Android LLM Inference API מאפשר להריץ מודלים גדולים של שפה (LLMs) בצורה מלאה במכשיר עבור אפליקציות אנדרואיד, מה שניתן להשתמש בו לביצוע מגוון רחב של משימות, כמו יצירת טקסט, שליפת מידע בצורה של שפה טבעית, וסיכום מסמכים. המשימה תומכת באופן מובנה במודלים גדולים של טקסט-לטקסט, כך שניתן להחיל את מודלי ה-AI הגנרטיביים העדכניים ביותר במכשיר על האפליקציות שלכם.

Googld AI Edge Torch היא ספריית פייתון התומכת בהמרת מודלים מ-PyTorch לפורמט .tflite, שניתן להריץ עם TensorFlow Lite ו-MediaPipe. זה מאפשר אפליקציות לאנדרואיד, iOS ו-IoT שיכולות להריץ מודלים בצורה מלאה במכשיר. AI Edge Torch מציעה תמיכה רחבה ב-CPU, עם תמיכה ראשונית ב-GPU ו-NPU. AI Edge Torch שואפת להשתלב היטב עם PyTorch, מתבססת על torch.export() ומספקת תמיכה טובה באופרציות Core ATen.

## **🪬 הנחיות**

### **🔥 המרת Microsoft Phi-3.5 לתמיכה ב-tflite**

0. הדוגמה מיועדת ל-Android 14+

1. התקן Python 3.10.12

***המלצה:*** השתמש ב-conda להתקנת סביבת הפייתון שלך

2. Ubuntu 20.04 / 22.04 (יש להתמקד ב-[google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***המלצה:*** השתמש ב-Azure Linux VM או ב-VM בענן צד שלישי ליצירת הסביבה שלך

3. עבור לטרמינל הלינוקס שלך, להתקנת ספריית פייתון

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. הורד את Microsoft-3.5-Instruct מ-Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. המר את Microsoft Phi-3.5 ל-tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 המרת Microsoft Phi-3.5 ל-Mediapipe Bundle לאנדרואיד**

אנא התקן את mediapipe תחילה

```bash

pip install mediapipe

```

הפעל את הקוד הזה ב-[המחברת שלך](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 העברת מודל המשימה למכשירי האנדרואיד שלך באמצעות adb push**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 הרצת קוד האנדרואיד שלך**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.he.png)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתירגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי של אדם. אנו לא אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.