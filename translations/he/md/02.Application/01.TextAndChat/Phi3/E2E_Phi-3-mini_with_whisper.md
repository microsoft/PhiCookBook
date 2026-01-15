<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:51:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "he"
}
-->
# צ'טבוט אינטראקטיבי Phi 3 Mini 4K Instruct עם Whisper

## סקירה כללית

הצ'טבוט האינטראקטיבי Phi 3 Mini 4K Instruct הוא כלי שמאפשר למשתמשים לתקשר עם הדמו של Microsoft Phi 3 Mini 4K instruct באמצעות קלט טקסט או שמע. הצ'טבוט יכול לשמש למגוון משימות, כגון תרגום, עדכוני מזג אוויר ואיסוף מידע כללי.

### התחלה מהירה

כדי להשתמש בצ'טבוט הזה, פשוט פעל לפי ההוראות הבאות:

1. פתחו את [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. בחלון הראשי של המחברת, תראה ממשק תיבת שיחה עם תיבת קלט טקסט וכפתור "Send".
3. כדי להשתמש בצ'טבוט מבוסס טקסט, פשוט הקלד את ההודעה שלך בתיבת הקלט של הטקסט ולחץ על כפתור "Send". הצ'טבוט יגיב בקובץ שמע שניתן להפעיל ישירות מתוך המחברת.

**הערה**: כלי זה דורש GPU וגישה למודלים Microsoft Phi-3 ו-OpenAI Whisper, המשמשים לזיהוי דיבור ותרגום.

### דרישות חומרה (GPU)

להפעלת הדמו יש צורך בזיכרון GPU של 12GB.

דרישות הזיכרון להפעלת הדמו של **Microsoft-Phi-3-Mini-4K instruct** על GPU תלויות במספר גורמים, כגון גודל הנתונים הקלטיים (שמע או טקסט), השפה שבה משתמשים לתרגום, מהירות המודל והזיכרון הזמין ב-GPU.

באופן כללי, מודל Whisper תוכנן לפעול על GPUs. כמות הזיכרון המינימלית המומלצת להפעלת מודל Whisper היא 8GB, אך הוא יכול להתמודד עם כמויות גדולות יותר במידה ויש צורך.

חשוב לציין שהפעלת כמות גדולה של נתונים או נפח גבוה של בקשות למודל עשויה לדרוש זיכרון GPU נוסף ו/או עלולה לגרום לבעיות ביצועים. מומלץ לבדוק את מקרה השימוש שלך תוך שימוש בתצורות שונות ולנטר את שימוש הזיכרון על מנת לקבוע את ההגדרות האופטימליות לצרכים הספציפיים שלך.

## דוגמת E2E לצ'טבוט אינטראקטיבי Phi 3 Mini 4K Instruct עם Whisper

מחברת היופיטר שכותרתה [צ'טבוט אינטראקטיבי Phi 3 Mini 4K Instruct עם Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) מדגימה כיצד להשתמש בדמו של Microsoft Phi 3 Mini 4K instruct ליצירת טקסט מקלט שמע או טקסט כתוב. המחברת מגדירה מספר פונקציות:

1. `tts_file_name(text)`: פונקציה זו יוצרת שם קובץ המבוסס על הטקסט הקלט לשם שמירת קובץ השמע שנוצר.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: פונקציה זו משתמשת ב-Edge TTS API ליצירת קובץ שמע מרשימת חתיכות טקסט. הפרמטרים הנכנסים הם רשימת החתיכות, קצב הדיבור, שם הקול ונתיב הפלט לשמירת קובץ השמע שנוצר.
1. `talk(input_text)`: פונקציה זו יוצרת קובץ שמע באמצעות Edge TTS API ושומרת אותו בשם קובץ אקראי בספריית /content/audio. הפרמטר הנכנס הוא הטקסט להמרה לדיבור.
1. `run_text_prompt(message, chat_history)`: פונקציה זו משתמשת בדמו של Microsoft Phi 3 Mini 4K instruct ליצירת קובץ שמע מהודעה קלט ומוסיפה אותו להיסטוריית השיחה.
1. `run_audio_prompt(audio, chat_history)`: פונקציה זו ממירה קובץ שמע לטקסט באמצעות Whisper model API ומעבירה אותו לפונקציית `run_text_prompt()`.
1. הקוד מפעיל אפליקציית Gradio שמאפשרת למשתמשים לתקשר עם הדמו של Phi 3 Mini 4K instruct על ידי הקלדת הודעות או העלאת קבצי שמע. הפלט מוצג כהודעת טקסט בתוך האפליקציה.

## פתרון תקלות

התקנת דרייברים ל-Cuda GPU

1. ודא שהאפליקציות בלינוקס מעודכנות

    ```bash
    sudo apt update
    ```

1. התקן דרייברים של Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. רשם את מיקום הדרייבר של cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. בדוק את גודל הזיכרון של Nvidia GPU (דרוש 12GB זיכרון GPU)

    ```bash
    nvidia-smi
    ```

1. ריקון מטמון: אם אתה משתמש ב-PyTorch, תוכל לקרוא ל-torch.cuda.empty_cache() כדי לשחרר את כל זיכרון המטמון שלא בשימוש, כך שיוכל לשמש יישומי GPU אחרים

    ```python
    torch.cuda.empty_cache() 
    ```

1. בדוק את Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. בצע את המשימות הבאות ליצירת טוקן Hugging Face.

    - עבור לעמוד [הגדרות טוקן Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - בחר **New token**.
    - הזן את **Name** של הפרויקט שברצונך להשתמש בו.
    - בחר את **Type** ל-**Write**.

> [!NOTE]
>
> אם נתקלת בשגיאה הבאה:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> כדי לפתור זאת, הקלד את הפקודה הבאה בתוך הטרמינל שלך.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**הסתייגות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית הוא המקור המוסמך. למידע קריטי מומלץ להיעזר בתרגום מקצועי וידני. אנו לא נושאים באחריות על אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->