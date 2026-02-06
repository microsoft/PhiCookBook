## **איך להשתמש ב-Model Builder כדי לכמת את Phi-3.5**

כעת Model Builder תומך בכימות מודלי ONNX עבור Phi-3.5 Instruct ו-Phi-3.5-Vision

### **Phi-3.5-Instruct**

**המרה מואצת ב-CPU של כימות INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**המרה מואצת ב-CUDA של כימות INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. הגדר את הסביבה בטרמינל

```bash

mkdir models

cd models 

```

2. הורד את microsoft/Phi-3.5-vision-instruct לתיקיית models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. הורד את הקבצים האלה לתיקיית Phi-3.5-vision-instruct שלך

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. הורד את הקובץ הזה לתיקיית models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. עבור לטרמינל

    המר תמיכה ב-ONNX עם FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **הערה：**

1. Model Builder תומך כרגע בהמרה של Phi-3.5-Instruct ו-Phi-3.5-Vision, אך לא ב-Phi-3.5-MoE

2. כדי להשתמש במודל הכמותי של ONNX, ניתן להשתמש בו דרך ה-SDK של Generative AI extensions for onnxruntime

3. יש לקחת בחשבון אחריות AI, לכן לאחר המרת הכימות מומלץ לבצע בדיקות תוצאה יעילות יותר

4. על ידי כימות מודל CPU INT4, ניתן לפרוס אותו למכשירי Edge, מה שמאפשר תרחישי שימוש טובים יותר, ולכן סיימנו את Phi-3.5-Instruct סביב INT4

## **משאבים**

1. למידע נוסף על Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. מאגר GitHub של Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.