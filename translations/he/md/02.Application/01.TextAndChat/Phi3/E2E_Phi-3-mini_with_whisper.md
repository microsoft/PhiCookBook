# אינטראקטיבי Phi 3 Mini 4K אינסטרקט צ'אטבוט עם Whisper

## סקירה כללית

האינטראקטיבי Phi 3 Mini 4K אינסטרקט צ'אטבוט הוא כלי שמאפשר למשתמשים לתקשר עם הדמו של Microsoft Phi 3 Mini 4K באמצעות קלט טקסט או אודיו. הצ'אטבוט יכול לשמש למגוון משימות, כמו תרגום, עדכוני מזג אוויר ואיסוף מידע כללי.

### התחלת עבודה

כדי להשתמש בצ'אטבוט, פשוט בצעו את ההוראות הבאות:

1. פתחו קובץ [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. בחלון הראשי של המחברת, תראו ממשק צ'אט עם תיבת קלט טקסט וכפתור "Send".
3. כדי להשתמש בצ'אטבוט מבוסס טקסט, הקלידו את ההודעה שלכם בתיבת הקלט ולחצו על כפתור "Send". הצ'אטבוט יגיב עם קובץ אודיו שניתן לנגן ישירות מתוך המחברת.

**הערה**: כלי זה דורש GPU וגישה למודלים Microsoft Phi-3 ו-OpenAI Whisper, המשמשים לזיהוי דיבור ותרגום.

### דרישות GPU

כדי להפעיל את הדמו הזה, נדרשת זיכרון GPU בנפח 12GB.

דרישות הזיכרון להפעלת הדמו **Microsoft-Phi-3-Mini-4K אינסטרקט** על GPU תלויות במספר גורמים, כגון גודל נתוני הקלט (אודיו או טקסט), השפה המשמשת לתרגום, מהירות המודל והזיכרון הזמין ב-GPU.

באופן כללי, מודל Whisper מיועד לפעול על GPUs. כמות הזיכרון המינימלית המומלצת להפעלת המודל היא 8GB, אך הוא יכול להתמודד עם כמויות זיכרון גדולות יותר במידת הצורך.

חשוב לציין כי הפעלת כמות גדולה של נתונים או נפח גבוה של בקשות על המודל עשויה לדרוש יותר זיכרון GPU ו/או לגרום לבעיות בביצועים. מומלץ לבדוק את המקרה שלכם עם תצורות שונות ולנטר את השימוש בזיכרון כדי לקבוע את ההגדרות האופטימליות לצרכים הספציפיים שלכם.

## דוגמה E2E לאינטראקטיבי Phi 3 Mini 4K אינסטרקט צ'אטבוט עם Whisper

המחברת Jupyter בשם [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) מדגימה כיצד להשתמש בדמו Microsoft Phi 3 Mini 4K אינסטרקט ליצירת טקסט מקלט אודיו או טקסט כתוב. המחברת מגדירה מספר פונקציות:

1. `tts_file_name(text)`: פונקציה זו מייצרת שם קובץ המבוסס על טקסט הקלט לצורך שמירת קובץ האודיו שנוצר.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: פונקציה זו משתמשת ב-Edge TTS API ליצירת קובץ אודיו מרשימת מקטעי טקסט קלט. הפרמטרים הם רשימת המקטעים, מהירות הדיבור, שם הקול ונתיב הפלט לשמירת קובץ האודיו.
1. `talk(input_text)`: פונקציה זו מייצרת קובץ אודיו באמצעות Edge TTS API ושומרת אותו בשם קובץ אקראי בתיקיית /content/audio. הפרמטר הוא טקסט הקלט להמרה לדיבור.
1. `run_text_prompt(message, chat_history)`: פונקציה זו משתמשת בדמו Microsoft Phi 3 Mini 4K אינסטרקט ליצירת קובץ אודיו מקלט הודעה ומוסיפה אותו להיסטוריית הצ'אט.
1. `run_audio_prompt(audio, chat_history)`: פונקציה זו ממירה קובץ אודיו לטקסט באמצעות Whisper model API ומעבירה אותו לפונקציה `run_text_prompt()`.
1. הקוד מפעיל אפליקציית Gradio שמאפשרת למשתמשים לתקשר עם הדמו Phi 3 Mini 4K אינסטרקט על ידי הקלדת הודעות או העלאת קבצי אודיו. הפלט מוצג כהודעת טקסט בתוך האפליקציה.

## פתרון בעיות

התקנת דרייברים של Cuda GPU

1. ודאו שהאפליקציות בלינוקס מעודכנות

    ```bash
    sudo apt update
    ```

1. התקנת דרייברים של Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. רישום מיקום הדרייבר של Cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. בדיקת גודל זיכרון Nvidia GPU (נדרשים 12GB זיכרון GPU)

    ```bash
    nvidia-smi
    ```

1. ריקון מטמון: אם אתם משתמשים ב-PyTorch, ניתן לקרוא לפונקציה torch.cuda.empty_cache() כדי לשחרר את כל הזיכרון הלא מנוצל כך שניתן יהיה להשתמש בו באפליקציות GPU אחרות

    ```python
    torch.cuda.empty_cache() 
    ```

1. בדיקת Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. בצעו את המשימות הבאות ליצירת טוקן של Hugging Face.

    - נווטו אל [דף הגדרות הטוקן של Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - בחרו **טוקן חדש**.
    - הזינו את **שם** הפרויקט שברצונכם להשתמש בו.
    - בחרו **סוג** ל-**Write**.

> **הערה**
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
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.