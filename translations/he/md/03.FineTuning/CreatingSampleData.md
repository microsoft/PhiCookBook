# יצירת מערך נתוני תמונות על ידי הורדת DataSet מ-Hugging Face והתמונות המשויכות אליו


### סקירה כללית

הסקריפט הזה מכין מערך נתונים ללמידת מכונה על ידי הורדת התמונות הנדרשות, סינון שורות שבהן ההורדה של התמונות נכשלה, ושמירת מערך הנתונים כקובץ CSV.

### דרישות מוקדמות

לפני הרצת הסקריפט, ודאו שהספריות הבאות מותקנות: `Pandas`, `Datasets`, `requests`, `PIL`, ו-`io`. כמו כן, יש להחליף את `'Insert_Your_Dataset'` בשורה 2 בשם מערך הנתונים שלכם מ-Hugging Face.

ספריות נדרשות:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### פונקציונליות

הסקריפט מבצע את השלבים הבאים:

1. מוריד את מערך הנתונים מ-Hugging Face באמצעות הפונקציה `load_dataset()`.
2. ממיר את מערך הנתונים של Hugging Face ל-Pandas DataFrame לצורך טיפול נוח יותר באמצעות השיטה `to_pandas()`.
3. יוצר תיקיות לשמירת מערך הנתונים והתמונות.
4. מסנן שורות שבהן הורדת התמונה נכשלה על ידי מעבר על כל שורה ב-DataFrame, הורדת התמונה באמצעות הפונקציה המותאמת אישית `download_image()`, והוספת השורה המסוננת ל-DataFrame חדש בשם `filtered_rows`.
5. יוצר DataFrame חדש עם השורות המסוננות ושומר אותו בדיסק כקובץ CSV.
6. מדפיס הודעה שמציינת היכן נשמרו מערך הנתונים והתמונות.

### פונקציה מותאמת אישית

הפונקציה `download_image()` מורידה תמונה מכתובת URL ושומרת אותה מקומית באמצעות ספריית Pillow Image (PIL) ומודול `io`. היא מחזירה True אם התמונה הורדה בהצלחה, ו-False אחרת. הפונקציה גם מעלה חריגה עם הודעת שגיאה כאשר הבקשה נכשלה.

### איך זה עובד

הפונקציה download_image מקבלת שני פרמטרים: image_url, שהיא כתובת ה-URL של התמונה להורדה, ו-save_path, שהוא הנתיב שבו התמונה שהורדה תישמר.

כך הפונקציה פועלת:

היא מתחילה בביצוע בקשת GET ל-image_url באמצעות השיטה requests.get. זה מושך את נתוני התמונה מה-URL.

השורה response.raise_for_status() בודקת אם הבקשה הצליחה. אם קוד הסטטוס של התגובה מצביע על שגיאה (למשל, 404 - לא נמצא), היא תזרוק חריגה. זה מבטיח שנמשיך להוריד את התמונה רק אם הבקשה הצליחה.

נתוני התמונה מועברים לאחר מכן לשיטה Image.open מתוך מודול PIL (Python Imaging Library). שיטה זו יוצרת אובייקט Image מנתוני התמונה.

השורה image.save(save_path) שומרת את התמונה בנתיב ה-save_path שצויין. הנתיב צריך לכלול את שם הקובץ הרצוי והסיומת.

לבסוף, הפונקציה מחזירה True כדי לציין שהתמונה הורדה ונשמרה בהצלחה. אם מתרחשת חריגה במהלך התהליך, היא תופסת את החריגה, מדפיסה הודעת שגיאה שמציינת את הכישלון, ומחזירה False.

פונקציה זו שימושית להורדת תמונות מכתובות URL ושמירתן מקומית. היא מטפלת בשגיאות אפשריות במהלך תהליך ההורדה ומספקת משוב האם ההורדה הצליחה או לא.

ראוי לציין שהספרייה requests משמשת לביצוע בקשות HTTP, ספריית PIL משמשת לעבודה עם תמונות, ומחלקת BytesIO משמשת לטיפול בנתוני התמונה כזרם של בתים.



### סיכום

הסקריפט מספק דרך נוחה להכנת מערך נתונים ללמידת מכונה על ידי הורדת התמונות הנדרשות, סינון שורות שבהן ההורדה נכשלה, ושמירת מערך הנתונים כקובץ CSV.

### סקריפט לדוגמה

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download the dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert the Hugging Face dataset to a Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save the dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows where image download fails
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Create a new DataFrame with the filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save the updated dataset to disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### הורדת קוד לדוגמה  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### מערך נתונים לדוגמה  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.