# כוונון מדויק ואינטגרציה של מודלים מותאמים אישית Phi-3 עם Prompt flow ב- Microsoft Foundry

דוגמת סיום-הקצה (E2E) זו מבוססת על המדריך "[כוונון מדויק ואינטגרציה של מודלים מותאמים אישית Phi-3 עם Prompt Flow ב- Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" מקהילת הטכנולוגיה של מייקרוסופט. היא מציגה את התהליכים של כוונון מדויק, פריסה ואינטגרציה של מודלים מותאמים אישית Phi-3 עם Prompt flow ב- Microsoft Foundry.
בניגוד לדוגמת ה-E2E, "[כוונון מדויק ואינטגרציה של מודלים מותאמים אישית Phi-3 עם Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", שכללה הרצת קוד מקומית, מדריך זה מתמקד כולו בכוונון מדויק ואינטגרציה של המודל שלך בתוך Azure AI / ML Studio.

## סקירה כללית

בדוגמת E2E זו, תלמד כיצד לכוון את מודל Phi-3 במדויק ולשלב אותו עם Prompt flow ב- Microsoft Foundry. תוך שימוש ב- Azure AI / ML Studio, תבנה זרימת עבודה לפריסה ושימוש במודלים מותאמים אישית של AI. דוגמת E2E זו מחולקת לשלושה תרחישים:

**תרחיש 1: הגדרת משאבי Azure והכנה לכוונון מדויק**

**תרחיש 2: כוונון מדויק של מודל Phi-3 ופריסה ב- Azure Machine Learning Studio**

**תרחיש 3: אינטגרציה עם Prompt flow ושיחה עם המודל המותאם אישית שלך ב- Microsoft Foundry**

הנה סקירה של דוגמת E2E זו.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/he/00-01-architecture.198ba0f1ae6d841a.webp)

### תוכן עניינים

1. **[תרחיש 1: הגדרת משאבי Azure והכנה לכוונון מדויק](#תרחיש-1-הגדרת-משאבי-azure-והכנה-לכוונון-מדויק)**
    - [צור סביבת עבודה ב- Azure Machine Learning](#צור-סביבת-עבודה-ב-azure-machine-learning)
    - [בקש הקצאות GPU במנוי Azure](#בקשת-הקצאות-gpu-במנוי-azure)
    - [הוסף מקצה תפקידים](#הוסף-מקצה-תפקידים)
    - [הגדרת פרויקט](#הגדרת-פרויקט)
    - [הכן מערך נתונים לכוונון מדויק](#הכנת-קובץ-הנתונים-למידה-מעודנת)

1. **[תרחיש 2: כוונון מדויק של מודל Phi-3 ופריסה ב- Azure Machine Learning Studio](#תרחיש-2-למידה-מעודנת-של-מודל-phi-3-ופריסה-ב-azure-machine-learning-studio)**
    - [כוונן את מודל Phi-3](#למידה-מעודנת-של-מודל-phi-3)
    - [פרוס את מודל Phi-3 המכוונן](#פרוס-את-המודל-phi-3-שלמדת)

1. **[תרחיש 3: אינטגרציה עם Prompt flow ושיחה עם המודל המותאם שלך ב- Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [שלב את מודל Phi-3 המותאם אישית עם Prompt flow](#אינטגרציה-של-מודל-phi-3-מותאם-עם-prompt-flow)
    - [שוחח עם מודל Phi-3 המותאם אישית שלך](#שוחח-עם-מודל-ה-phi-3-המותאם-אישית-שלך)

## תרחיש 1: הגדרת משאבי Azure והכנה לכוונון מדויק

### צור סביבת עבודה ב- Azure Machine Learning

1. הקלד *azure machine learning* בסרגל **החיפוש** בראש דף הפורטל ובחר **Azure Machine Learning** מתוך האפשרויות שמופיעות.

    ![Type azure machine learning.](../../../../../../translated_images/he/01-01-type-azml.acae6c5455e67b4b.webp)

2. בחר **+ יצירה** מתפריט הניווט.

3. בחר **סביבת עבודה חדשה** מתפריט הניווט.

    ![Select new workspace.](../../../../../../translated_images/he/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. בצע את המשימות הבאות:

    - בחר את **המנוי** שלך ב- Azure.
    - בחר את **קבוצת המשאבים** לשימוש (צור חדשה אם יש צורך).
    - הזן **שם סביבת העבודה**. חייב להיות ערך ייחודי.
    - בחר את **האזור** שברצונך להשתמש בו.
    - בחר את **חשבון האחסון** לשימוש (צור חדש אם יש צורך).
    - בחר את **מחשב המפתחות (Key vault)** לשימוש (צור חדש אם יש צורך).
    - בחר את **Application insights** לשימוש (צור חדש אם יש צורך).
    - בחר את **רישום המכולות (Container registry)** לשימוש (צור חדש אם יש צורך).

    ![Fill azure machine learning.](../../../../../../translated_images/he/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. בחר **סקירה + יצירה**.

6. בחר **צור**.

### בקשת הקצאות GPU במנוי Azure

במדריך זה תלמד כיצד לכוון מדויק ולהפעיל מודל Phi-3, תוך שימוש ב-GPU-ים. לצורך כוונון מדויק תשתמש ב-GPU מסוג *Standard_NC24ads_A100_v4*, שדורש בקשת הקצאה. לצורך הפריסה תשתמש ב-GPU מסוג *Standard_NC6s_v3*, שגם הוא דורש בקשה להקצאה.

> [!NOTE]
>
> רק מנויי Pay-As-You-Go (סוג המנוי הסטנדרטי) זכאים להקצאת GPU; מנויים מסוג "הטבות" אינם נתמכים כיום.
>

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בצע את המשימות הבאות כדי לבקש הקצאת משאבים עבור *Standard NCADSA100v4 Family*:

    - בחר **הקצאה** מהכרטיסייה בצד שמאל.
    - בחר את **משפחת המחשב הווירטואלי** לשימוש. לדוגמה, בחר **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, שכולל את ה-GPU *Standard_NC24ads_A100_v4*.
    - בחר **בקשת הקצאה** מתפריט הניווט.

        ![Request quota.](../../../../../../translated_images/he/02-02-request-quota.c0428239a63ffdd5.webp)

    - בדף בקשת ההקצאה, הזן את **המגבלה החדשה של הליבות** שברצונך להשתמש. לדוגמה, 24.
    - בדף בקשת ההקצאה, בחר **שלח** כדי לבקש את הקצאת ה-GPU.

1. בצע את המשימות הבאות כדי לבקש הקצאת משאבים עבור *Standard NCSv3 Family*:

    - בחר **הקצאה** מהכרטיסייה בצד שמאל.
    - בחר את **משפחת המחשב הווירטואלי** לשימוש. לדוגמה, בחר **Standard NCSv3 Family Cluster Dedicated vCPUs**, שכולל את ה-GPU *Standard_NC6s_v3*.
    - בחר **בקשת הקצאה** מתפריט הניווט.
    - בדף בקשת ההקצאה, הזן את **המגבלה החדשה של הליבות** שברצונך להשתמש. לדוגמה, 24.
    - בדף בקשת ההקצאה, בחר **שלח** כדי לבקש את הקצאת ה-GPU.

### הוסף מקצה תפקידים

כדי לכוון ולהפעיל את המודלים שלך, עליך קודם ליצור זהות מנוהלת מוקצית למשתמש (UAI) ולהקצות לה הרשאות מתאימות. זהות זו תשמש לאימות בזמן הפריסה.

#### יצירת זהות מנוהלת מוקצית למשתמש (UAI)

1. הקלד *managed identities* בסרגל **החיפוש** בראש דף הפורטל ובחר **Managed Identities** מתוך האפשרויות שמופיעות.

    ![Type managed identities.](../../../../../../translated_images/he/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. בחר **+ יצירה**.

    ![Select create.](../../../../../../translated_images/he/03-02-select-create.92bf8989a5cd98f2.webp)

1. בצע את המשימות הבאות:

    - בחר את **המנוי** שלך ב- Azure.
    - בחר את **קבוצת המשאבים** לשימוש (צור חדשה אם יש צורך).
    - בחר את **האזור** שברצונך להשתמש בו.
    - הזן את **שם**. חייב להיות ערך ייחודי.

    ![Select create.](../../../../../../translated_images/he/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. בחר **סקירה + יצירה**.

1. בחר **+ יצירה**.

#### הוסף מקצה תפקיד Contributor לזהות המנוהלת

1. נווט למשאב זהות מנוהלת שיצרת.

1. בחר **הקצאות תפקיד Azure** מהכרטיסייה בצד שמאל.

1. בחר **+הוסף הקצאת תפקיד** מתפריט הניווט.

1. בדף הוספת הקצאת תפקיד, בצע את המשימות הבאות:
    - בחר את **תחום** ל- **קבוצת משאבים**.
    - בחר את **המנוי** שלך ב- Azure.
    - בחר את **קבוצת המשאבים** לשימוש.
    - בחר את **התפקיד** ל- **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/he/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. בחר **שמור**.

#### הוסף מקצה תפקיד Storage Blob Data Reader לזהות המנוהלת

1. הקלד *storage accounts* בסרגל **החיפוש** בראש דף הפורטל ובחר **Storage accounts** מתוך האפשרויות שמופיעות.

    ![Type storage accounts.](../../../../../../translated_images/he/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. בחר את חשבון האחסון המשויך לסביבת העבודה Azure Machine Learning שיצרת. לדוגמה, *finetunephistorage*.

1. בצע את המשימות הבאות כדי לנווט לדף הוספת הקצאת תפקיד:

    - נווט לחשבון האחסון של Azure שיצרת.
    - בחר **בקרת גישה (IAM)** מהכרטיסייה בצד שמאל.
    - בחר **+ הוסף** מתפריט הניווט.
    - בחר **הוסף הקצאת תפקיד** מתפריט הניווט.

    ![Add role.](../../../../../../translated_images/he/03-06-add-role.353ccbfdcf0789c2.webp)

1. בדף הוספת הקצאת תפקיד, בצע את המשימות הבאות:

    - בדף התפקיד, הקלד *Storage Blob Data Reader* בסרגל ה**חיפוש** ובחר **Storage Blob Data Reader** מתוך האפשרויות שמופיעות.
    - בדף התפקיד, בחר **הבא**.
    - בעמוד החברים, בחר **הקצה גישה ל-** **Managed identity**.
    - בעמוד החברים, בחר **+ בחר חברים**.
    - בעמוד בחירת זהויות מנוהלות, בחר את **המנוי** שלך ב- Azure.
    - בעמוד בחירת זהויות מנוהלות, בחר את **הזהות המנוהלת** ל- **Manage Identity**.
    - בעמוד בחירת זהויות מנוהלות, בחר את זהות הניהול שיצרת. לדוגמה, *finetunephi-managedidentity*.
    - בעמוד בחירת זהויות מנוהלות, בחר **בחר**.

    ![Select managed identity.](../../../../../../translated_images/he/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. בחר **סקירה + הקצה**.

#### הוסף מקצה תפקיד AcrPull לזהות המנוהלת

1. הקלד *container registries* בסרגל **החיפוש** בראש דף הפורטל ובחר **Container registries** מתוך האפשרויות שמופיעות.

    ![Type container registries.](../../../../../../translated_images/he/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. בחר את רישום המכולות המשויך לסביבת העבודה Azure Machine Learning. לדוגמה, *finetunephicontainerregistry*

1. בצע את המשימות הבאות כדי לנווט לדף הוספת הקצאת תפקיד:

    - בחר **בקרת גישה (IAM)** מהכרטיסייה בצד שמאל.
    - בחר **+ הוסף** מתפריט הניווט.
    - בחר **הוסף הקצאת תפקיד** מתפריט הניווט.

1. בדף הוספת הקצאת תפקיד, בצע את המשימות הבאות:

    - בדף התפקיד, הקלד *AcrPull* בסרגל ה**חיפוש** ובחר **AcrPull** מתוך האפשרויות שמופיעות.
    - בדף התפקיד, בחר **הבא**.
    - בעמוד החברים, בחר **הקצה גישה ל-** **Managed identity**.
    - בעמוד החברים, בחר **+ בחר חברים**.
    - בעמוד בחירת זהויות מנוהלות, בחר את **המנוי** שלך ב- Azure.
    - בעמוד בחירת זהויות מנוהלות, בחר את **הזהות המנוהלת** ל- **Manage Identity**.
    - בעמוד בחירת זהויות מנוהלות, בחר את זהות הניהול שיצרת. לדוגמה, *finetunephi-managedidentity*.
    - בעמוד בחירת זהויות מנוהלות, בחר **בחר**.
    - בחר **סקירה + הקצה**.

### הגדרת פרויקט

כדי להוריד את מערכי הנתונים הנדרשים לכוונון מדויק, תקבע סביבה מקומית.

בניסוי זה, תבצע

- יצירת תיקייה לעבודה בתוכה.
- יצירת סביבה וירטואלית.
- התקנת החבילות הדרושות.
- יצירת קובץ *download_dataset.py* להורדת מערך הנתונים.

#### יצירת תיקייה לעבודה בתוכה

1. פתח חלון טרמינל והקלד את הפקודה הבאה ליצירת תיקייה בשם *finetune-phi* בנתיב ברירת המחדל.

    ```console
    mkdir finetune-phi
    ```

2. הקלד את הפקודה הבאה בטרמינל שלך כדי לנווט לתיקיית *finetune-phi* שיצרת.

    ```console
    cd finetune-phi
    ```

#### יצירת סביבה וירטואלית

1. הקלד את הפקודה הבאה בטרמינל שלך כדי ליצור סביבה וירטואלית בשם *.venv*.
    ```console
    python -m venv .venv
    ```

2. הקלד את הפקודה הבאה בתוך הטרמינל שלך כדי להפעיל את סביבת העבודה הווירטואלית.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> אם זה הצליח, אתה אמור לראות *(.venv)* לפני שורת הפקודה.

#### התקן את החבילות הנדרשות

1. הקלד את הפקודות הבאות בתוך הטרמינל שלך כדי להתקין את החבילות הנדרשות.

    ```console
    pip install datasets==2.19.1
    ```

#### צור את `donload_dataset.py`

> [!NOTE]
> מבנה התיקייה המלא:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. פתח את **Visual Studio Code**.

1. בחר **File** מהסרגל העליון.

1. בחר **Open Folder**.

1. בחר את תיקיית *finetune-phi* שיצרת, שממוקמת בכתובת *C:\Users\yourUserName\finetune-phi*.

    ![בחר את התיקייה שיצרת.](../../../../../../translated_images/he/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. בפאנל השמאלי של Visual Studio Code, לחץ קליק ימני ובחר **New File** כדי ליצור קובץ חדש בשם *download_dataset.py*.

    ![צור קובץ חדש.](../../../../../../translated_images/he/04-02-create-new-file.cf9a330a3a9cff92.webp)

### הכנת קובץ הנתונים למידה מעודנת

באימון זה, תריץ את קובץ *download_dataset.py* כדי להוריד את ערכות הנתונים *ultrachat_200k* לסביבת העבודה המקומית שלך. לאחר מכן תשתמש בערכות נתונים אלו כדי לבצע למידה מעודנת על המודל Phi-3 ב-Azure Machine Learning.

באימון זה, תעשה את הדברים הבאים:

- הוסף קוד לקובץ *download_dataset.py* להורדת ערכות הנתונים.
- הרץ את הקובץ *download_dataset.py* כדי להוריד את ערכות הנתונים לסביבת העבודה המקומית.

#### הורד את ערכת הנתונים שלך באמצעות *download_dataset.py*

1. פתח את הקובץ *download_dataset.py* ב-Visual Studio Code.

1. הוסף את הקוד הבא לתוך הקובץ *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # טען את מערכת הנתונים עם השם, התצורה, ויחס החלוקה שצוינו
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # חלק את מערכת הנתונים לסטים של אימון ובדיקה (80% אימון, 20% בדיקה)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # צור את התיקייה אם היא לא קיימת
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # פתח את הקובץ במצב כתיבה
        with open(filepath, 'w', encoding='utf-8') as f:
            # עבור על כל רשומה במערכת הנתונים
            for record in dataset:
                # המשל רשומה כאובייקט JSON וכתוב אותה לקובץ
                json.dump(record, f)
                # כתוב תו שורה חדשה כדי להפריד בין הרשומות
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # טען וחלק את מערכת הנתונים ULTRACHAT_200k עם תצורה ויחס חלוקה ספציפיים
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # הפק את מערכות הנתונים לאימון ולבדיקה מהחלוקה
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # שמור את מערכת האימון לקובץ JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # שמור את מערכת הבדיקה לקובץ JSONL נפרד
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. הקלד את הפקודה הבאה בתוך הטרמינל כדי להריץ את הסקריפט ולהוריד את ערכת הנתונים לסביבת העבודה המקומית שלך.

    ```console
    python download_dataset.py
    ```

1. אמת שערכות הנתונים נשמרו בהצלחה בתיקיית *finetune-phi/data* המקומית שלך.

> [!NOTE]
>
> #### הערה על גודל ערכת הנתונים וזמן הלמידה המעודנת
>
> במדריך זה, אתה משתמש רק ב-1% מהערכת הנתונים (`split='train[:1%]'`). זה מקטין משמעותית את כמות הנתונים, ומאיץ את תהליך ההעלאה והלמידה המעודנת. ניתן להתאים את האחוז כדי למצוא את האיזון הנכון בין זמן האימון לביצועי המודל. שימוש בתת-קבוצה קטנה יותר של ערכת הנתונים מקצר את משך הלמידה המעודנת, ומאפשר תהליך נוח יותר למדריך.

## תרחיש 2: למידה מעודנת של מודל Phi-3 ופריסה ב-Azure Machine Learning Studio

### למידה מעודנת של מודל Phi-3

באימון זה, תבצע למידה מעודנת למודל Phi-3 ב-Azure Machine Learning Studio.

בתרגיל זה, תעשה את הדברים הבאים:

- צור אשכול מחשבים ללמידה מעודנת.
- בצע למידה מעודנת למודל Phi-3 ב-Azure Machine Learning Studio.

#### צור אשכול מחשבים ללמידה מעודנת

1. עבור אל [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בחר **Compute** מתוך לשונית הצד.

1. בחר **Compute clusters** מתפריט הניווט.

1. בחר **+ New**.

    ![בחר מחשוב.](../../../../../../translated_images/he/06-01-select-compute.a29cff290b480252.webp)

1. בצע את הפעולות הבאות:

    - בחר את **האזור** שברצונך להשתמש בו.
    - בחר את **רמת מכונת הווירטואלית** ל-**Dedicated**.
    - בחר את **סוג מכונת הווירטואלית** ל-**GPU**.
    - הגבל את **גודל מכונת הווירטואלית** ל-**Select from all options**.
    - בחר את **גודל מכונת הווירטואלית** ל-**Standard_NC24ads_A100_v4**.

    ![צור אשכול.](../../../../../../translated_images/he/06-02-create-cluster.f221b65ae1221d4e.webp)

1. בחר **Next**.

1. בצע את הפעולות הבאות:

    - הכנס את **שם המחשב**. חייב להיות ערך ייחודי.
    - הגדר את **מספר מינימום של צמתים** ל-**0**.
    - הגדר את **מספר מקסימום של צמתים** ל-**1**.
    - הגדר את **שניות בהמתנה לפני הקטנת האשכול** ל-**120**.

    ![צור אשכול.](../../../../../../translated_images/he/06-03-create-cluster.4a54ba20914f3662.webp)

1. בחר **Create**.

#### בצע למידה מעודנת למודל Phi-3

1. עבור אל [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בחר את סביבת העבודה Azure Machine Learning שיצרת.

    ![בחר סביבת עבודה שיצרת.](../../../../../../translated_images/he/06-04-select-workspace.a92934ac04f4f181.webp)

1. בצע את הפעולות הבאות:

    - בחר **Model catalog** מתוך לשונית הצד.
    - הקלד *phi-3-mini-4k* בשורת החיפוש ובחר **Phi-3-mini-4k-instruct** מתוך האפשרויות שיופיעו.

    ![הקלד phi-3-mini-4k.](../../../../../../translated_images/he/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. בחר **Fine-tune** מתפריט הניווט.

    ![בחר למידה מעודנת.](../../../../../../translated_images/he/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. בצע את הפעולות הבאות:

    - בחר **Select task type** ל-**Chat completion**.
    - בחר **+ Select data** להעלאת **נתוני אימון**.
    - בחר באפשרות העלאת נתוני אימות ל-**Provide different validation data**.
    - בחר **+ Select data** להעלאת **נתוני אימות**.

    ![מלא את דף הלמידה המעודנת.](../../../../../../translated_images/he/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> ניתן לבחור **Advanced settings** כדי להתאים אישית פרמטרים כמו **learning_rate** ו-**lr_scheduler_type** כדי לייעל את תהליך הלמידה המעודנת בהתאם לצרכים הספציפיים שלך.

1. בחר **Finish**.

1. באימון זה, ביצעת בהצלחה למידה מעודנת למודל Phi-3 באמצעות Azure Machine Learning. שים לב שתהליך הלמידה המעודנת יכול לקחת זמן משמעותי. לאחר הפעלת עבודת הלמידה המעודנת, יש להמתין לסיומה. ניתן לעקוב אחרי מצב המשימה בלשונית Jobs בצד שמאל של סביבת העבודה שלך ב-Azure Machine Learning. בסדרה הבאה, תפרוס את המודל שלמדת ותשלב אותו עם Prompt flow.

    ![ראה פעולת למידה מעודנת.](../../../../../../translated_images/he/06-08-output.2bd32e59930672b1.webp)

### פרוס את המודל Phi-3 שלמדת

כדי לשלב את המודל Phi-3 שעבר למידה מעודנת עם Prompt flow, יש לפרוס את המודל כך שיהיה נגיש להסקה בזמן אמת. התהליך כולל רישום המודל, יצירת נקודת קצה מקוונת, ופריסת המודל.

בתרגיל זה, תעשה את הדברים הבאים:

- תרשם את המודל שלמדת בסביבת העבודה Azure Machine Learning.
- תיצור נקודת קצה מקוונת.
- תפרוס את המודל Phi-3 שנרשם.

#### רישום המודל שלמדת

1. עבור אל [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בחר את סביבת העבודה Azure Machine Learning שיצרת.

    ![בחר סביבת עבודה שיצרת.](../../../../../../translated_images/he/06-04-select-workspace.a92934ac04f4f181.webp)

1. בחר **Models** מתוך לשונית הצד.

1. בחר **+ Register**.

1. בחר **From a job output**.

    ![רשם מודל.](../../../../../../translated_images/he/07-01-register-model.ad1e7cc05e4b2777.webp)

1. בחר את העבודה שיצרת.

    ![בחר עבודה.](../../../../../../translated_images/he/07-02-select-job.3e2e1144cd6cd093.webp)

1. בחר **Next**.

1. בחר את **Model type** ל-**MLflow**.

1. ודא ש-**Job output** מסומן; זה אמור להיבחר אוטומטית.

    ![בחר פלט.](../../../../../../translated_images/he/07-03-select-output.4cf1a0e645baea1f.webp)

2. בחר **Next**.

3. בחר **Register**.

    ![בחר רישום.](../../../../../../translated_images/he/07-04-register.fd82a3b293060bc7.webp)

4. תוכל לצפות במודל שרשמת בלשונית **Models** מתוך לשונית הצד.

    ![מודל שרשם.](../../../../../../translated_images/he/07-05-registered-model.7db9775f58dfd591.webp)

#### פריסת המודל שלמדת

1. עבור אל סביבת העבודה Azure Machine Learning שיצרת.

1. בחר **Endpoints** מתוך לשונית הצד.

1. בחר **Real-time endpoints** מתוך תפריט הניווט.

    ![צור נקודת קצה.](../../../../../../translated_images/he/07-06-create-endpoint.1ba865c606551f09.webp)

1. בחר **Create**.

1. בחר את המודל שנרשם שיצרת.

    ![בחר מודל שנרשם.](../../../../../../translated_images/he/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. בחר **Select**.

1. בצע את הפעולות הבאות:

    - בחר **Virtual machine** ל-*Standard_NC6s_v3*.
    - בחר את **מספר המופעים** שברצונך להשתמש בו, למשל *1*.
    - בחר את **Endpoint** ל-**New** כדי ליצור נקודת קצה חדשה.
    - הזן **שם נקודת קצה**. חייב להיות ערך ייחודי.
    - הזן **שם פריסה**. חייב להיות ערך ייחודי.

    ![מלא הגדרות פריסה.](../../../../../../translated_images/he/07-08-deployment-setting.43ddc4209e673784.webp)

1. בחר **Deploy**.

> [!WARNING]
> כדי למנוע חיובים נוספים בחשבונך, הקפד למחוק את נקודת הקצה שיצרת בסביבת העבודה של Azure Machine Learning.
>

#### בדוק את מצב הפריסה בסביבת העבודה Azure Machine Learning

1. עבור אל סביבת העבודה Azure Machine Learning שיצרת.

1. בחר **Endpoints** מתוך לשונית הצד.

1. בחר את נקודת הקצה שיצרת.

    ![בחר נקודת קצה](../../../../../../translated_images/he/07-09-check-deployment.325d18cae8475ef4.webp)

1. בעמוד זה, תוכל לנהל את נקודות הקצה במהלך תהליך הפריסה.

> [!NOTE]
> לאחר סיום הפריסה, ודא ש-**תעבורת חיה** מוגדרת ל-**100%**. אם לא, בחר **Update traffic** כדי להתאים את הגדרות התעבורה. שים לב שאי אפשר לבדוק את המודל אם התעבורה מוגדרת ל-0%.
>
> ![הגדר תעבורה.](../../../../../../translated_images/he/07-10-set-traffic.085b847e5751ff3d.webp)
>

## תרחיש 3: אינטגרציה עם Prompt flow ושיחה עם המודל המותאם שלך ב-Microsoft Foundry

### אינטגרציה של מודל Phi-3 מותאם עם Prompt flow

לאחר שפרסת בהצלחה את המודל שלך שעבר למידה מעודנת, כעת תוכל לשלב אותו עם Prompt Flow כדי להשתמש במודל שלך ביישומים בזמן אמת, ולבצע מגוון פעולות אינטראקטיביות עם מודל Phi-3 המותאם שלך.

בתרגיל זה, תעשה את הדברים הבאים:

- צור Microsoft Foundry Hub.
- צור פרויקט Microsoft Foundry.
- צור Prompt flow.
- הוסף חיבור מותאם למודל Phi-3 שעבר למידה מעודנת.
- הגדר את Prompt flow לשיחה עם מודל Phi-3 המותאם שלך.

> [!NOTE]
> ניתן גם לשלב עם Promptflow באמצעות Azure ML Studio. אותו תהליך אינטגרציה תקף גם ל-Azure ML Studio.

#### צור Microsoft Foundry Hub

עליך ליצור Hub לפני יצירת הפרויקט. ה-Hub פועל כקבוצת משאבים, ומאפשר לך לארגן ולנהל מספר פרויקטים בתוך Microsoft Foundry.
1. בקר ב-[Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. בחר **All hubs** מהכרטיסייה בצד שמאל.

1. בחר **+ New hub** מתפריט הניווט.

    ![Create hub.](../../../../../../translated_images/he/08-01-create-hub.8f7dd615bb8d9834.webp)

1. בצע את המשימות הבאות:

    - הזן **Hub name**. חייב להיות ערך ייחודי.
    - בחר את **Subscription** של Azure שלך.
    - בחר את **Resource group** לשימוש (צור קבוצה חדשה אם יש צורך).
    - בחר את **Location** שבו תרצה להשתמש.
    - בחר ב-**Connect Azure AI Services** לשימוש (צור שירות חדש אם יש צורך).
    - בחר ב-**Connect Azure AI Search** ב-**Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/he/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. בחר **Next**.

#### צור פרויקט במיקרוסופט Foundry

1. ב-Hub שיצרת, בחר **All projects** מהכרטיסייה בצד שמאל.

1. בחר **+ New project** מתפריט הניווט.

    ![Select new project.](../../../../../../translated_images/he/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. הזן **Project name**. חייב להיות ערך ייחודי.

    ![Create project.](../../../../../../translated_images/he/08-05-create-project.4d97f0372f03375a.webp)

1. בחר **Create a project**.

#### הוסף חיבור מותאם אישית למודל Phi-3 שעבר כיוונון עדין

כדי לשלב את מודל ה-Phi-3 המותאם אישית עם Prompt flow, עליך לשמור את נקודת הקצה והמפתח של המודל בחיבור מותאם אישית. הגדרה זו מבטיחה גישה למודל ה-Phi-3 המותאם אישית ב-Prompt flow.

#### הגדר מפתח API וכתובת נקודת הקצה של מודל Phi-3 שעבר כיוונון עדין

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. עבור לחלל העבודה של Azure Machine learning שיצרת.

1. בחר **Endpoints** מהכרטיסייה בצד שמאל.

    ![Select endpoints.](../../../../../../translated_images/he/08-06-select-endpoints.aff38d453bcf9605.webp)

1. בחר את נקודת הקצה שיצרת.

    ![Select endpoints.](../../../../../../translated_images/he/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. בחר **Consume** מתפריט הניווט.

1. העתק את **REST endpoint** ו-**Primary key** שלך.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/he/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### הוסף את החיבור המותאם האישית

1. בקר ב-[Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. עבור לפרויקט Microsoft Foundry שיצרת.

1. בפרויקט שיצרת, בחר **Settings** מהכרטיסייה בצד שמאל.

1. בחר **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/he/08-09-select-new-connection.02eb45deadc401fc.webp)

1. בחר **Custom keys** מתפריט הניווט.

    ![Select custom keys.](../../../../../../translated_images/he/08-10-select-custom-keys.856f6b2966460551.webp)

1. בצע את המשימות הבאות:

    - בחר **+ Add key value pairs**.
    - עבור שם המפתח, הזן **endpoint** והדבק את נקודת הקצה שהעתקת מ-Azure ML Studio בשדה הערך.
    - בחר שוב **+ Add key value pairs**.
    - עבור שם המפתח, הזן **key** והדבק את המפתח שהעתקת מ-Azure ML Studio בשדה הערך.
    - לאחר הוספת המפתחות, בחר **is secret** כדי למנוע חשיפת המפתח.

    ![Add connection.](../../../../../../translated_images/he/08-11-add-connection.785486badb4d2d26.webp)

1. בחר **Add connection**.

#### צור Prompt flow

הוספת חיבור מותאם אישית ב-Microsoft Foundry. כעת, ניצור Prompt flow באמצעות השלבים הבאים. לאחר מכן, תחבר Prompt flow זה לחיבור המותאם כדי שתוכל להשתמש במודל שעבר כיוונון עדין בתוך Prompt flow.

1. עבור לפרויקט Microsoft Foundry שיצרת.

1. בחר **Prompt flow** מהכרטיסייה בצד שמאל.

1. בחר **+ Create** מתפריט הניווט.

    ![Select Promptflow.](../../../../../../translated_images/he/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. בחר **Chat flow** מתפריט הניווט.

    ![Select chat flow.](../../../../../../translated_images/he/08-13-select-flow-type.2ec689b22da32591.webp)

1. הזן **Folder name** לשימוש.

    ![Enter name.](../../../../../../translated_images/he/08-14-enter-name.ff9520fefd89f40d.webp)

2. בחר **Create**.

#### הגדר Prompt flow לשיחה עם מודל Phi-3 מותאם אישית

יש לשלב את מודל ה-Phi-3 שעבר כיוונון עדין בתוך Prompt flow. עם זאת, ה-Prompt flow הקיים לא מיועד למטרה זו. לכן, עליך לעצב מחדש את Prompt flow כדי לאפשר את השילוב של המודל המותאם אישית.

1. ב-Prompt flow, בצע את המשימות הבאות כדי לבנות מחדש את הזרימה הקיימת:

    - בחר **Raw file mode**.
    - מחק את כל הקוד הקיים בקובץ *flow.dag.yml*.
    - הוסף את הקוד הבא לקובץ *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - בחר **Save**.

    ![Select raw file mode.](../../../../../../translated_images/he/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. הוסף את הקוד הבא לקובץ *integrate_with_promptflow.py* לשימוש במודל Phi-3 המותאם ב-Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # הגדרת יומן רישום
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" הוא שם החיבור המותאם אישית, "endpoint", "key" הם המפתחות בחיבור המותאם אישית
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # רישום תגובת JSON המלאה
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/he/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> למידע מפורט יותר על שימוש ב-Prompt flow ב-Microsoft Foundry, ניתן לעיין ב-[Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. בחר **Chat input**, **Chat output** כדי לאפשר שיחה עם המודל שלך.

    ![Input Output.](../../../../../../translated_images/he/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. כעת אתה מוכן לשוחח עם מודל ה-Phi-3 המותאם אישית שלך. בתרגיל הבא תלמד כיצד להתחיל את Prompt flow ולהשתמש בו לשיחה עם מודל ה-Phi-3 שעבר כיוונון עדין.

> [!NOTE]
>
> הזרימה שנבנתה מחדש אמורה להיראות דומה לתמונה שלהלן:
>
> ![Flow example.](../../../../../../translated_images/he/08-18-graph-example.d6457533952e690c.webp)
>

### שוחח עם מודל ה-Phi-3 המותאם אישית שלך

כעת לאחר שכיוונת ושילבת את מודל ה-Phi-3 המותאם אישית שלך עם Prompt flow, אתה מוכן להתחיל באינטראקציה איתו. תרגיל זה ינחה אותך בתהליך ההגדרה והפעלה של שיחה עם המודל באמצעות Prompt flow. על ידי ביצוע שלבים אלה, תוכל למצות במלואן את היכולות של מודל ה-Phi-3 שעבר כיוונון עדין למשימות ושיחות שונות.

- שוחח עם מודל ה-Phi-3 המותאם אישית שלך באמצעות Prompt flow.

#### התחל את Prompt flow

1. בחר **Start compute sessions** כדי להתחיל את Prompt flow.

    ![Start compute session.](../../../../../../translated_images/he/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. בחר **Validate and parse input** כדי לחדש פרמטרים.

    ![Validate input.](../../../../../../translated_images/he/09-02-validate-input.317c76ef766361e9.webp)

1. בחר את **Value** של ה-**connection** לחיבור המותאם שיצרת. לדוגמה, *connection*.

    ![Connection.](../../../../../../translated_images/he/09-03-select-connection.99bdddb4b1844023.webp)

#### שוחח עם המודל המותאם אישית שלך

1. בחר **Chat**.

    ![Select chat.](../../../../../../translated_images/he/09-04-select-chat.61936dce6612a1e6.webp)

1. הנה דוגמה לתוצאות: כעת אתה יכול לשוחח עם מודל ה-Phi-3 המותאם אישית שלך. מומלץ לשאול שאלות בהתבסס על הנתונים ששימשו לכיוונון העדין.

    ![Chat with prompt flow.](../../../../../../translated_images/he/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להביא בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. עבור מידע קריטי, מומלץ לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנה או פרשנות שגויה הנובעים משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->