<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T13:58:55+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "he"
}
-->
# **כיווץ Phi-3.5 באמצעות Intel OpenVINO**

Intel היא יצרנית ה-CPU המסורתית ביותר עם משתמשים רבים. עם עליית הלמידה המכונה והלמידה העמוקה, Intel גם הצטרפה לתחרות להאצת AI. עבור אינפרנס של מודלים, Intel לא משתמשת רק ב-GPUs ו-CPUs, אלא גם ב-NPUs.

אנו מקווים לפרוס את משפחת Phi-3.x בקצה הקצה, בתקווה להפוך לחלק החשוב ביותר במחשב AI ובמחשב Copilot. טעינת המודל בקצה תלויה בשיתוף פעולה עם יצרני חומרה שונים. פרק זה מתמקד בעיקר בתרחיש היישום של Intel OpenVINO כמודל כמותי.

## **מה זה OpenVINO**

OpenVINO הוא כלי קוד פתוח לאופטימיזציה ופריסה של מודלים ללמידה עמוקה מהענן ועד הקצה. הוא מאיץ אינפרנס של למידה עמוקה במגוון תרחישים, כמו AI גנרטיבי, וידאו, אודיו ושפה עם מודלים ממסגרות פופולריות כמו PyTorch, TensorFlow, ONNX ועוד. המרת מודלים ואופטימיזציה שלהם, ופריסה במגוון חומרות וסביבות של Intel®, מקומית ומכשירית, בדפדפן או בענן.

כעת עם OpenVINO, ניתן במהירות לכווץ את מודל ה-GenAI בחומרת Intel ולהאיץ את הרפרנס למודל.

כעת OpenVINO תומך בהמרת כיווץ של Phi-3.5-Vision ו-Phi-3.5 Instruct

### **הגדרת סביבה**

אנא ודא שהתקנת את התלויות הבאות בסביבה, זהו requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **כיווץ Phi-3.5-Instruct באמצעות OpenVINO**

בטרמינל, אנא הרץ את הסקריפט הבא

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **כיווץ Phi-3.5-Vision באמצעות OpenVINO**

אנא הרץ את הסקריפט הזה ב-Python או ב-Jupyter lab

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

### **🤖 דוגמאות ל-Phi-3.5 עם Intel OpenVINO**

| מעבדות    | הקדמה | עבור ל- |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | למד כיצד להשתמש ב-Phi-3.5 Instruct במחשב AI שלך    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (תמונה) | למד כיצד להשתמש ב-Phi-3.5 Vision לניתוח תמונות במחשב AI שלך      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (וידאו)   | למד כיצד להשתמש ב-Phi-3.5 Vision לניתוח וידאו במחשב AI שלך    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **משאבים**

1. למידע נוסף על Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. מאגר GitHub של Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.