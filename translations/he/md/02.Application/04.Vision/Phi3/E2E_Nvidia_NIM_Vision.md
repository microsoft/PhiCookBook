<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:57:00+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "he"
}
-->
### תרחיש לדוגמה

תדמיין שיש לך תמונה (`demo.png`) ואתה רוצה ליצור קוד Python שמעבד את התמונה הזו ושומר גרסה חדשה שלה (`phi-3-vision.jpg`).

הקוד שלמעלה מאוטומט את התהליך על ידי:

1. הגדרת הסביבה וההגדרות הנחוצות.
2. יצירת פרומפט שמנחה את המודל לייצר את קוד ה-Python הנדרש.
3. שליחת הפרומפט למודל ואיסוף הקוד שנוצר.
4. חילוץ והרצת הקוד שנוצר.
5. הצגת התמונה המקורית והתמונה המעובדת.

גישה זו מנצלת את כוח ה-AI לאוטומציה של משימות עיבוד תמונה, מה שמקל ומהיר להשגת המטרות שלך.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

בואו נפרק את כל הקוד שלב אחר שלב:

1. **התקנת חבילה דרושה**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    הפקודה הזו מתקינה את החבילה `langchain_nvidia_ai_endpoints`, ומוודאת שהיא הגרסה העדכנית ביותר.

2. **ייבוא מודולים נחוצים**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    הייבוא הזה מביא את המודולים הדרושים לאינטראקציה עם נקודות הקצה של NVIDIA AI, טיפול מאובטח בסיסמאות, אינטראקציה עם מערכת ההפעלה, וקידוד/פענוח נתונים בפורמט base64.

3. **הגדרת מפתח API**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    הקוד בודק אם משתנה הסביבה `NVIDIA_API_KEY` מוגדר. אם לא, הוא מבקש מהמשתמש להזין את מפתח ה-API בצורה מאובטחת.

4. **הגדרת מודל ונתיב לתמונה**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    כאן מוגדר המודל שישמש, נוצרת מופע של `ChatNVIDIA` עם המודל שנבחר, ומוגדר הנתיב לקובץ התמונה.

5. **יצירת פרומפט טקסטואלי**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    מוגדר פרומפט טקסטואלי שמנחה את המודל לייצר קוד Python לעיבוד תמונה.

6. **קידוד התמונה ב-base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    הקוד קורא את קובץ התמונה, מקודד אותה ב-base64, ויוצר תגית HTML של תמונה עם הנתונים המקודדים.

7. **שילוב הטקסט והתמונה לפרומפט אחד**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    כאן משולבים פרומפט הטקסט ותגית ה-HTML של התמונה למחרוזת אחת.

8. **יצירת קוד באמצעות ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    הקוד שולח את הפרומפט למופע `ChatNVIDIA` ומקבל את מחרוזת ה-`code` שנוצרה.

9. **חילוץ קוד Python מהתוכן שנוצר**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    הקוד מחלץ את קוד ה-Python האמיתי מתוך התוכן שנוצר על ידי הסרת הפורמט של markdown.

10. **הרצת הקוד שנוצר**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    הקוד מריץ את קוד ה-Python שחולץ כתהליך משנה ולוכד את הפלט שלו.

11. **הצגת התמונות**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    שורות אלו מציגות את התמונות באמצעות המודול `IPython.display`.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי שיש להתייחס אליו. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא אחראים לכל אי הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.