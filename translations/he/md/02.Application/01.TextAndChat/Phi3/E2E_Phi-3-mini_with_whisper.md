<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:32:28+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "he"
}
-->
# צ'אטבוט אינטראקטיבי Phi 3 Mini 4K Instruct עם Whisper

## סקירה כללית

צ'אטבוט האינטראקטיבי Phi 3 Mini 4K Instruct הוא כלי המאפשר למשתמשים לתקשר עם דמו ההדרכה של Microsoft Phi 3 Mini 4K באמצעות קלט טקסט או קול. הצ'אטבוט יכול לשמש למגוון משימות, כמו תרגום, עדכוני מזג אוויר ואיסוף מידע כללי.

### התחלה

כדי להשתמש בצ'אטבוט הזה, פשוט עקבו אחר ההוראות הבאות:

1. פתחו את [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. בחלון הראשי של המחברת, תראו ממשק צ'אט עם תיבת קלט טקסט וכפתור "Send".
3. לשימוש בצ'אטבוט מבוסס טקסט, פשוט הקלידו את ההודעה שלכם בתיבת הקלט ולחצו על כפתור "Send". הצ'אטבוט יגיב בקובץ שמע שניתן להאזין לו ישירות מתוך המחברת.

**Note**: כלי זה דורש GPU וגישה למודלים Microsoft Phi-3 ו-OpenAI Whisper, המשמשים לזיהוי דיבור ותרגום.

### דרישות GPU

כדי להריץ את הדמו הזה דרושים 12GB זיכרון GPU.

דרישות הזיכרון להרצת דמו **Microsoft-Phi-3-Mini-4K instruct** על GPU תלויות בכמה גורמים, כגון גודל קלט הנתונים (קול או טקסט), שפת התרגום, מהירות המודל וזיכרון זמין ב-GPU.

באופן כללי, מודל Whisper מיועד להרצה על GPUs. כמות הזיכרון המומלצת למודל Whisper היא לפחות 8GB, אך הוא יכול להתמודד עם כמויות זיכרון גדולות יותר במידת הצורך.

חשוב לציין שהפעלת כמות גדולה של נתונים או נפח גבוה של בקשות על המודל עלולה לדרוש זיכרון GPU נוסף ו/או לגרום לבעיות ביצועים. מומלץ לבדוק את המקרה שלכם עם תצורות שונות ולעקוב אחר שימוש הזיכרון כדי לקבוע את ההגדרות האופטימליות לצרכים הספציפיים שלכם.

## דוגמת E2E לצ'אטבוט אינטראקטיבי Phi 3 Mini 4K Instruct עם Whisper

מחברת היופיטר בשם [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) מדגימה כיצד להשתמש בדמו ההדרכה של Microsoft Phi 3 Mini 4K כדי ליצור טקסט מקלט קול או טקסט כתוב. המחברת מגדירה מספר פונקציות:

1. `tts_file_name(text)`: פונקציה שיוצרת שם קובץ על בסיס טקסט הקלט לשמירת קובץ השמע שנוצר.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: פונקציה המשתמשת ב-Edge TTS API ליצירת קובץ שמע מרשימת חלקי טקסט. הפרמטרים הם רשימת החלקים, מהירות הדיבור, שם הקול ונתיב השמירה של קובץ השמע שנוצר.
1. `talk(input_text)`: פונקציה שיוצרת קובץ שמע באמצעות Edge TTS API ושומרת אותו בשם אקראי בתיקיית /content/audio. הפרמטר הוא טקסט הקלט שיומר לדיבור.
1. `run_text_prompt(message, chat_history)`: פונקציה המשתמשת בדמו Microsoft Phi 3 Mini 4K Instruct ליצירת קובץ שמע מהודעת קלט ומוסיפה אותו להיסטוריית הצ'אט.
1. `run_audio_prompt(audio, chat_history)`: פונקציה הממירה קובץ שמע לטקסט באמצעות מודל Whisper API ומעבירה אותו לפונקציה `run_text_prompt()`.
1. הקוד מפעיל אפליקציית Gradio המאפשרת למשתמשים לתקשר עם דמו Phi 3 Mini 4K Instruct על ידי הקלדת הודעות או העלאת קבצי שמע. הפלט מוצג כהודעת טקסט בתוך האפליקציה.

## פתרון בעיות

התקנת דרייברים של Cuda GPU

1. ודאו שהאפליקציות בלינוקס מעודכנות

    ```bash
    sudo apt update
    ```

1. התקנת דרייברי Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. רישום מיקום דרייבר ה-cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. בדיקת גודל זיכרון Nvidia GPU (נדרש 12GB זיכרון GPU)

    ```bash
    nvidia-smi
    ```

1. ניקוי Cache: אם אתם משתמשים ב-PyTorch, ניתן לקרוא לפונקציה torch.cuda.empty_cache() כדי לשחרר את כל זיכרון המטמון שלא בשימוש, כך שיוכל לשמש יישומי GPU אחרים

    ```python
    torch.cuda.empty_cache() 
    ```

1. בדיקת Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. בצעו את המשימות הבאות ליצירת טוקן Hugging Face.

    - עברו לעמוד [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - בחרו **New token**.
    - הזינו את שם הפרויקט (**Name**) שברצונכם להשתמש בו.
    - בחרו **Type** כ-**Write**.

> **Note**
>
> אם נתקלתם בשגיאה הבאה:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> כדי לפתור זאת, הקלידו את הפקודה הבאה בתוך הטרמינל שלכם.
>
> ```bash
> sudo ldconfig
> ```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור המוסמך והמהימן. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא אחראים לכל אי-הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.