# **כימות משפחת Phi באמצעות הרחבות בינה מלאכותית גנרטיבית ל-onnxruntime**

## **מהן הרחבות בינה מלאכותית גנרטיבית ל-onnxruntime**

הרחבות אלו מאפשרות להריץ בינה מלאכותית גנרטיבית באמצעות ONNX Runtime( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). הן מספקות את הלולאה של בינה מלאכותית גנרטיבית עבור מודלים של ONNX, כולל אינפרנס עם ONNX Runtime, עיבוד לוגיטים, חיפוש ודגימה, וניהול מטמון KV. מפתחים יכולים לקרוא לשיטת generate() ברמה גבוהה, או להריץ כל איטרציה של המודל בלולאה, לייצר טוקן אחד בכל פעם, ואפשרות לעדכן פרמטרים של ההפקה בתוך הלולאה. היא תומכת בחיפוש greedy/beam ודגימת TopP, TopK ליצירת רצפי טוקנים ועיבוד לוגיטים מובנה כמו עונשי חזרה. אפשר גם להוסיף בקלות דירוג מותאם אישית.

ברמת היישום, ניתן להשתמש בהרחבות בינה מלאכותית גנרטיבית ל-onnxruntime כדי לבנות יישומים בשפות C++/ C# / Python. ברמת המודל, ניתן להשתמש בה למיזוג מודלים מוסדרים ולבצע עבודה כמותית קשורה לפריסה.


## **כימות Phi-3.5 עם הרחבות בינה מלאכותית גנרטיבית ל-onnxruntime**

### **מודלים נתמכים**

הרחבות בינה מלאכותית גנרטיבית ל-onnxruntime תומכות בהמרת כימות של Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **בונה מודלים בהרחבות בינה מלאכותית גנרטיבית ל-onnxruntime**

בונה המודלים מאיץ משמעותית את יצירת המודלים המותאמים והמכילים כימות של ONNX שפועלים עם ממשק generate() של ONNX Runtime.

דרך בונה המודלים, ניתן לכמת את המודל ל-INT4, INT8, FP16, FP32, ולשלב שיטות האצת חומרה שונות כמו CPU, CUDA, DirectML, Mobile ועוד.

לשימוש בבונה המודלים נדרש להתקין

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

לאחר ההתקנה, ניתן להריץ את הסקריפט של בונה המודלים מהטרמינל לביצוע המרת פורמט ומעבר כימות.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

הבנת הפרמטרים הרלוונטיים

1. **model_name** זהו המודל ב-Hugging face, כמו microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, וכדומה. זה יכול להיות גם הנתיב בו שמרתם את המודל

2. **path_to_output_folder** נתיב שמירת ההמרה עם הכימות

3. **execution_provider** תמיכה בשיטות האצת חומרה שונות, כמו cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** אנו מורידים את המודל מה-Hugging face ומטמיעים אותו במטמון מקומי




***הערה：*** <ul>למרות שהרחבות בינה מלאכותית גנרטיבית ל-onnxruntime נמצאות בבחינה מוקדמת, הן שולבו בתוך Microsoft Olive, ואתם יכולים גם לקרוא לפונקציות בונה המודלים של ההרחבות דרך Microsoft Olive.</ul>

## **כיצד להשתמש בבונה המודלים לכימות Phi-3.5**

בונה המודלים תומך כעת בכימות מודל ONNX עבור Phi-3.5 Instruct ו-Phi-3.5-Vision

### **Phi-3.5-Instruct**


**המרה מואצת באמצעות CPU של כימות INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**המרה מואצת באמצעות CUDA של כימות INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. הגדר סביבה בטרמינל

```bash

mkdir models

cd models 

```

2. הורד את microsoft/Phi-3.5-vision-instruct לתיקיית המודלים
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. אנא הורד את הקבצים הבאים לתיקיית Phi-3.5-vision-instruct שלך

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. הורד קובץ זה לתיקיית המודלים
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. עבור לטרמינל

    המר תמיכה ONNX עם FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **הערה：**

1. בונה המודלים כרגע תומך בהמרת Phi-3.5-Instruct ו-Phi-3.5-Vision, אך לא ב-Phi-3.5-MoE

2. לשימוש במודל המכווץ של ONNX, ניתן להשתמש ב-SDK של הרחבות בינה מלאכותית גנרטיבית של onnxruntime

3. עלינו לקחת בחשבון בינה מלאכותית אחראית יותר, לכן לאחר המרת כימות המודל מומלץ לבצע בדיקות תוצאה אפקטיביות יותר

4. על ידי כימות מודל CPU INT4, אנו יכולים לפרוס אותו למכשירי קצה, שיש להם תרחישי שימוש טובים יותר, לכן סיימנו את Phi-3.5-Instruct בסביבות INT 4


## **משאבים**

1. למידע נוסף על הרחבות בינה מלאכותית גנרטיבית ל-onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. מאגר GitHub להרחבות בינה מלאכותית גנרטיבית ל-onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->