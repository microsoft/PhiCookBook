<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:38:40+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "he"
}
-->
## **כיצד להשתמש ב-Model Builder לכימות Phi-3.5**

Model Builder תומך כיום בכימות מודל ONNX עבור Phi-3.5 Instruct ו-Phi-3.5-Vision

### **Phi-3.5-Instruct**

**המרה מואצת על ידי CPU של כימות INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**המרה מואצת על ידי CUDA של כימות INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. הגדרת סביבה בטרמינל

```bash

mkdir models

cd models 

```

2. הורדת microsoft/Phi-3.5-vision-instruct לתיקיית models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. הורד את הקבצים הבאים לתיקיית Phi-3.5-vision-instruct שלך

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. הורד קובץ זה לתיקיית models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. עבור לטרמינל

    המר תמיכה ב-ONNX עם FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **הערה：**

1. Model Builder תומך כרגע בהמרה של Phi-3.5-Instruct ו-Phi-3.5-Vision, אך לא ב-Phi-3.5-MoE

2. לשימוש במודל הכמותי של ONNX, ניתן להשתמש בו דרך Generative AI extensions for onnxruntime SDK

3. יש לקחת בחשבון אחריות AI רבה יותר, לכן מומלץ לבצע בדיקות תוצאות יעילות לאחר המרת הכימות של המודל

4. באמצעות כימות מודל CPU INT4, ניתן לפרוס אותו למכשירי Edge, מה שמציע תרחישי שימוש טובים יותר, ולכן השלמנו את Phi-3.5-Instruct סביב INT4

## **משאבים**

1. למידע נוסף על Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. מאגר GitHub של Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא אחראים על אי-הבנות או פרשנויות שגויות הנובעות מהשימוש בתרגום זה.