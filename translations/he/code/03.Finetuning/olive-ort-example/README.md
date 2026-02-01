# כוונון עדין של Phi3 באמצעות Olive

בדוגמה זו תשתמשו ב-Olive כדי:

1. לכוונן עדין מתאם LoRA לסיווג ביטויים ל- Sad, Joy, Fear, Surprise.
1. למזג את משקלי המתאם לתוך המודל הבסיסי.
1. לאופטימיזציה וכימות של המודל ל- `int4`.

נראה גם כיצד לבצע אינפרנס למודל המכוונן בעזרת ONNX Runtime (ORT) Generate API.

> **⚠️ לכוונון עדין, תזדקקו לכרטיס גרפי מתאים - לדוגמה, A10, V100, A100.**

## 💾 התקנה

צרו סביבה וירטואלית חדשה בפייתון (לדוגמה, באמצעות `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

לאחר מכן, התקינו את Olive ואת התלויות עבור תהליך כוונון עדין:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 כוונון עדין של Phi3 באמצעות Olive
[קובץ התצורה של Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) מכיל *תהליך עבודה* עם ה-*שלבים* הבאים:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

ברמה גבוהה, תהליך העבודה הזה יבצע:

1. כוונון עדין של Phi3 (למשך 150 צעדים, שניתן לשנות) באמצעות הנתונים שב-[dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. מיזוג משקלי מתאם ה-LoRA לתוך המודל הבסיסי. כך תקבלו ארטיפקט מודל יחיד בפורמט ONNX.
1. Model Builder יבצע אופטימיזציה למודל עבור ONNX runtime *וגם* יכמת את המודל ל- `int4`.

להרצת תהליך העבודה, הריצו:

```bash
olive run --config phrase-classification.json
```

כאשר Olive יסיים, מודל Phi3 המכוונן והמאופטם ב- `int4` יהיה זמין בכתובת: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 שילוב Phi3 המכוונן באפליקציה שלכם

להרצת האפליקציה:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

התשובה צריכה להיות סיווג חד-מילה של הביטוי (Sad/Joy/Fear/Surprise).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.