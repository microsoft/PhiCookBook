<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:33:04+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "he"
}
-->
# כוונון עדין של Phi3 באמצעות Olive

בדוגמה זו תשתמש ב-Olive כדי:

1. לכוונן עדין מתאם LoRA לסיווג ביטויים ל- Sad, Joy, Fear, Surprise.
1. למזג את משקלי המתאם לתוך המודל הבסיסי.
1. לאופטם ולכמת את המודל ל-`int4`.

נראה גם איך לבצע אינפרנס למודל המכוון עדין באמצעות ONNX Runtime (ORT) Generate API.

> **⚠️ לכוונון עדין, תצטרך GPU מתאים - למשל A10, V100, A100.**

## 💾 התקנה

צור סביבה וירטואלית חדשה לפייתון (למשל, באמצעות `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

לאחר מכן, התקן את Olive ואת התלויות של תהליך הכוונון העדין:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 כוונון עדין של Phi3 באמצעות Olive
קובץ התצורה של [Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) מכיל *תהליך עבודה* עם ה*שלבים* הבאים:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

ברמה גבוהה, תהליך העבודה יבצע:

1. כוונון עדין ל-Phi3 (למשך 150 צעדים, שניתן לשנות) באמצעות הנתונים שב-[dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. מיזוג משקלי מתאם ה-LoRA לתוך המודל הבסיסי. תקבל ארטיפקט מודל יחיד בפורמט ONNX.
1. Model Builder יאטם את המודל עבור ONNX runtime *וגם* יכמת את המודל ל-`int4`.

כדי להריץ את תהליך העבודה, הפעל:

```bash
olive run --config phrase-classification.json
```

כאשר Olive יסיים, המודל המכוון עדין והמאופטם ל-`int4` זמין בכתובת: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 שילוב Phi3 המכוון עדין באפליקציה שלך

להרצת האפליקציה:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

התשובה תהיה סיווג מילה אחת של הביטוי (Sad/Joy/Fear/Surprise).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי של מתרגם אנושי. איננו אחראים לכל אי-הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.