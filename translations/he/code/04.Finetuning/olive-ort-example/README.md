<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:46:03+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "he"
}
-->
# כוונון עדין של Phi3 באמצעות Olive

בדוגמה זו תשתמש ב-Olive כדי:

1. לכוונן עדין מתאם LoRA כדי לסווג ביטויים ל-Sad, Joy, Fear, Surprise.
1. למזג את משקלי המתאם לתוך המודל הבסיסי.
1. לאופטם ולכמת את המודל ל-`int4`.

נראה גם כיצד לבצע אינפרנס למודל המכוונן עדין באמצעות ONNX Runtime (ORT) Generate API.

> **⚠️ עבור כוונון עדין, תזדקק לכרטיס גרפי מתאים - למשל A10, V100, A100.**

## 💾 התקנה

צור סביבת פייתון וירטואלית חדשה (למשל, באמצעות `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

לאחר מכן, התקן את Olive ואת התלויות עבור תהליך כוונון עדין:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 כוונון עדין של Phi3 באמצעות Olive
קובץ התצורה של [Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) מכיל *workflow* עם *שלבים* הבאים:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

ברמה גבוהה, תהליך זה יבצע:

1. כוונון עדין של Phi3 (למשך 150 צעדים, שניתן לשנות) באמצעות הנתונים מ-[dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. מיזוג משקלי מתאם LoRA לתוך המודל הבסיסי. כך תקבל ארטיפקט מודל יחיד בפורמט ONNX.
1. Model Builder יאופטם את המודל עבור ONNX runtime *ו* יכמת את המודל ל-`int4`.

כדי להפעיל את התהליך, הרץ:

```bash
olive run --config phrase-classification.json
```

כאשר Olive יסיים, המודל המכוונן עדין והמאופטם ל-`int4` זמין בכתובת: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 שילוב Phi3 המכוונן עדין באפליקציה שלך

להפעלת האפליקציה:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

התשובה צריכה להיות סיווג של מילה אחת בלבד של הביטוי (Sad/Joy/Fear/Surprise).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור המוסמך והמהימן. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.