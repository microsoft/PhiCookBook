<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:33:51+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "cs"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

Interactive Phi 3 Mini 4K Instruct Chatbot הוא כלי המאפשר למשתמשים לתקשר עם דמו ההוראות של Microsoft Phi 3 Mini 4K באמצעות קלט טקסט או קול. הצ'אטבוט ניתן לשימוש במגוון משימות, כמו תרגום, עדכוני מזג אוויר ואיסוף מידע כללי.

### Getting Started

כדי להשתמש בצ'אטבוט הזה, פשוט עקבו אחרי ההוראות הבאות:

1. פתחו את הקובץ [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. בחלון הראשי של המחברת תראו ממשק צ'אט עם תיבת קלט טקסט וכפתור "Send".
3. לשימוש בצ'אטבוט מבוסס טקסט, פשוט הקלידו את ההודעה שלכם בתיבת הקלט ולחצו על כפתור "Send". הצ'אטבוט יגיב בקובץ שמע שניתן להאזין לו ישירות בתוך המחברת.

**Note**: הכלי דורש GPU וגישה למודלים Microsoft Phi-3 ו-OpenAI Whisper, המשמשים לזיהוי דיבור ותרגום.

### GPU Requirements

כדי להריץ את הדמו הזה, דרוש זיכרון GPU של 12GB.

דרישות הזיכרון להרצת דמו **Microsoft-Phi-3-Mini-4K instruct** על GPU תלויות בכמה גורמים, כגון גודל הנתונים (קול או טקסט), השפה לתרגום, מהירות המודל והזיכרון הזמין ב-GPU.

באופן כללי, מודל Whisper מיועד להרצה על GPUs. הכמות המומלצת המינימלית של זיכרון GPU להרצת מודל Whisper היא 8GB, אך הוא יכול להתמודד עם כמויות גדולות יותר במידת הצורך.

חשוב לזכור שהפעלת כמויות גדולות של נתונים או בקשות מרובות למודל עלולה לדרוש יותר זיכרון GPU ועלולה להשפיע על הביצועים. מומלץ לבדוק את השימוש שלכם עם הגדרות שונות ולנטר את צריכת הזיכרון כדי למצוא את ההגדרות האופטימליות לצרכים שלכם.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

מחברת ה-Jupyter בשם [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) מראה כיצד להשתמש בדמו Microsoft Phi 3 Mini 4K Instruct כדי ליצור טקסט מקלט קול או טקסט כתוב. המחברת מגדירה מספר פונקציות:

1. `tts_file_name(text)`: פונקציה שיוצרת שם קובץ על בסיס הטקסט שנכנס לשמירת קובץ השמע שנוצר.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: פונקציה שמשתמשת ב-Edge TTS API כדי ליצור קובץ שמע מרשימת קטעי טקסט. הפרמטרים הם רשימת הקטעים, קצב הדיבור, שם הקול ונתיב הפלט לשמירת קובץ השמע.
1. `talk(input_text)`: פונקציה שיוצרת קובץ שמע באמצעות Edge TTS API ושומרת אותו בשם קובץ אקראי בתיקיית /content/audio. הפרמטר הוא הטקסט לקול.
1. `run_text_prompt(message, chat_history)`: פונקציה שמשתמשת בדמו Microsoft Phi 3 Mini 4K instruct כדי ליצור קובץ שמע מהודעה ומוסיפה אותו להיסטוריית הצ'אט.
1. `run_audio_prompt(audio, chat_history)`: פונקציה שממירה קובץ שמע לטקסט באמצעות מודל Whisper ומעבירה אותו לפונקציה `run_text_prompt()`.
1. הקוד מפעיל אפליקציית Gradio שמאפשרת למשתמשים לתקשר עם דמו Phi 3 Mini 4K instruct על ידי הקלדת הודעות או העלאת קבצי שמע. הפלט מוצג כהודעת טקסט בתוך האפליקציה.

## Troubleshooting

התקנת דרייברים ל-Cuda GPU

1. ודאו שהמערכת שלכם בלינוקס מעודכנת

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

1. בדיקת גודל זיכרון Nvidia GPU (דרוש 12GB זיכרון GPU)

    ```bash
    nvidia-smi
    ```

1. ריקון Cache: אם אתם משתמשים ב-PyTorch, ניתן לקרוא לפונקציה torch.cuda.empty_cache() כדי לשחרר את כל הזיכרון המטמון הלא בשימוש כך שיוכל לשמש אפליקציות GPU אחרות

    ```python
    torch.cuda.empty_cache() 
    ```

1. בדיקת Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. בצעו את השלבים הבאים ליצירת טוקן ב-Hugging Face.

    - עברו ל-[Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - בחרו **New token**.
    - הזינו את שם הפרויקט שברצונכם להשתמש בו.
    - בחרו **Type** ל-**Write**.

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

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.