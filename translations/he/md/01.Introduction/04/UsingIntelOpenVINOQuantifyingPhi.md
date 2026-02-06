# **כימות Phi-3.5 באמצעות Intel OpenVINO**

Intel היא יצרנית המעבדים המסורתית ביותר עם משתמשים רבים. עם עליית הלמידה המכונה והלמידה העמוקה, Intel הצטרפה גם היא לתחרות להאצת AI. עבור אינפרנס של מודלים, Intel לא משתמשת רק ב-GPUs ו-CPUs, אלא גם ב-NPUs.

אנו מקווים לפרוס את משפחת Phi-3.x בצד הקצה, בתקווה שתהפוך לחלק החשוב ביותר במחשב AI ובמחשב Copilot. טעינת המודל בצד הקצה תלויה בשיתוף פעולה בין יצרני חומרה שונים. פרק זה מתמקד בעיקר בתרחיש השימוש של Intel OpenVINO כמודל כמותי.

## **מה זה OpenVINO**

OpenVINO הוא ערכת כלים בקוד פתוח לאופטימיזציה ופריסה של מודלים ללמידה עמוקה מהענן ועד הקצה. הוא מאיץ אינפרנס של למידה עמוקה במגוון תרחישים, כגון AI גנרטיבי, וידאו, אודיו ושפה, עם מודלים ממסגרות פופולריות כמו PyTorch, TensorFlow, ONNX ועוד. ממיר ומאופטם מודלים, ומפרוס על מגוון חומרות וסביבות של Intel®, הן מקומית והן במכשיר, בדפדפן או בענן.

כעת עם OpenVINO, ניתן במהירות לכמת את מודל ה-GenAI בחומרת Intel ולהאיץ את רפרנס המודל.

כעת OpenVINO תומך בהמרת כימות של Phi-3.5-Vision ו-Phi-3.5 Instruct

### **הגדרת סביבה**

אנא ודא שהתקנת את התלויות הבאות בסביבה, זהו הקובץ requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **כימות Phi-3.5-Instruct באמצעות OpenVINO**

בטרמינל, אנא הרץ את הסקריפט הבא

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **כימות Phi-3.5-Vision באמצעות OpenVINO**

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

| מעבדות    | הקדמה | מעבר |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | למד כיצד להשתמש ב-Phi-3.5 Instruct במחשב ה-AI שלך    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (תמונה) | למד כיצד להשתמש ב-Phi-3.5 Vision לניתוח תמונות במחשב ה-AI שלך      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (וידאו)   | למד כיצד להשתמש ב-Phi-3.5 Vision לניתוח וידאו במחשב ה-AI שלך    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **משאבים**

1. למידע נוסף על Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. מאגר GitHub של Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.