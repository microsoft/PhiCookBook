<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:40:22+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "he"
}
-->
# כוונון מדויק ואינטגרציה של מודלים מותאמים אישית Phi-3 עם Prompt flow ב-Azure AI Foundry

דוגמת קצה-לקצה (E2E) זו מבוססת על המדריך "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" מתוך קהילת הטכנולוגיה של מיקרוסופט. היא מציגה את התהליכים של כוונון מדויק, פריסה ואינטגרציה של מודלים מותאמים אישית Phi-3 עם Prompt flow ב-Azure AI Foundry.  
בשונה מדוגמת ה-E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", שכללה הרצת קוד מקומית, המדריך הזה מתמקד כולו בכוונון מדויק ואינטגרציה של המודל שלך בתוך Azure AI / ML Studio.

## סקירה כללית

בדוגמת ה-E2E הזו תלמד כיצד לכוונן מדויק את מודל Phi-3 ולשלב אותו עם Prompt flow ב-Azure AI Foundry. באמצעות Azure AI / ML Studio, תקים תהליך עבודה לפריסה ושימוש במודלים מותאמים אישית של בינה מלאכותית. דוגמת ה-E2E מחולקת לשלושה תרחישים:

**תרחיש 1: הקמת משאבי Azure והכנה לכוונון מדויק**

**תרחיש 2: כוונון מדויק של מודל Phi-3 ופריסה ב-Azure Machine Learning Studio**

**תרחיש 3: אינטגרציה עם Prompt flow ושיחה עם המודל המותאם שלך ב-Azure AI Foundry**

להלן סקירה של דוגמת ה-E2E הזו.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.he.png)

### תוכן העניינים

1. **[תרחיש 1: הקמת משאבי Azure והכנה לכוונון מדויק](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [יצירת Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [בקשת מכסות GPU במנוי Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [הוספת שיוך תפקידים](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [הקמת פרויקט](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [הכנת מערך נתונים לכוונון מדויק](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[תרחיש 2: כוונון מדויק של מודל Phi-3 ופריסה ב-Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [כוונון מדויק של מודל Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [פריסת מודל Phi-3 המכוונן](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[תרחיש 3: אינטגרציה עם Prompt flow ושיחה עם המודל המותאם שלך ב-Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [אינטגרציה של מודל Phi-3 מותאם אישית עם Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [שיחה עם מודל Phi-3 המותאם שלך](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## תרחיש 1: הקמת משאבי Azure והכנה לכוונון מדויק

### יצירת Azure Machine Learning Workspace

1. הקלד *azure machine learning* בשורת החיפוש בראש דף הפורטל ובחר **Azure Machine Learning** מתוך האפשרויות שמופיעות.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.he.png)

2. בחר **+ Create** מתפריט הניווט.

3. בחר **New workspace** מתפריט הניווט.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.he.png)

4. בצע את המשימות הבאות:

    - בחר את **Subscription** של Azure שלך.  
    - בחר את **Resource group** לשימוש (צור חדש במידת הצורך).  
    - הזן **Workspace Name**. חייב להיות ערך ייחודי.  
    - בחר את **Region** שבו תרצה להשתמש.  
    - בחר את **Storage account** לשימוש (צור חדש במידת הצורך).  
    - בחר את **Key vault** לשימוש (צור חדש במידת הצורך).  
    - בחר את **Application insights** לשימוש (צור חדש במידת הצורך).  
    - בחר את **Container registry** לשימוש (צור חדש במידת הצורך).  

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.he.png)

5. בחר **Review + Create**.

6. בחר **Create**.

### בקשת מכסות GPU במנוי Azure

במדריך זה תלמד כיצד לכוונן מדויק ולפרוס מודל Phi-3, תוך שימוש ב-GPU. לכוונון מדויק תשתמש ב-GPU מסוג *Standard_NC24ads_A100_v4*, שדורש בקשת מכסה. לפריסה תשתמש ב-GPU מסוג *Standard_NC6s_v3*, שגם הוא דורש בקשת מכסה.

> [!NOTE]  
> רק מנויי Pay-As-You-Go (סוג המנוי הסטנדרטי) זכאים להקצאת GPU; מנויי הטבות אינם נתמכים כרגע.  
>

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בצע את המשימות הבאות כדי לבקש מכסת *Standard NCADSA100v4 Family*:

    - בחר **Quota** מהטאב בצד שמאל.  
    - בחר את **Virtual machine family** לשימוש. לדוגמה, בחר **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, הכולל את ה-GPU *Standard_NC24ads_A100_v4*.  
    - בחר **Request quota** מתפריט הניווט.  

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.he.png)

    - בדף Request quota, הזן את **New cores limit** שברצונך להשתמש בו. לדוגמה, 24.  
    - בדף Request quota, בחר **Submit** כדי לבקש את מכסת ה-GPU.  

1. בצע את המשימות הבאות כדי לבקש מכסת *Standard NCSv3 Family*:

    - בחר **Quota** מהטאב בצד שמאל.  
    - בחר את **Virtual machine family** לשימוש. לדוגמה, בחר **Standard NCSv3 Family Cluster Dedicated vCPUs**, הכולל את ה-GPU *Standard_NC6s_v3*.  
    - בחר **Request quota** מתפריט הניווט.  
    - בדף Request quota, הזן את **New cores limit** שברצונך להשתמש בו. לדוגמה, 24.  
    - בדף Request quota, בחר **Submit** כדי לבקש את מכסת ה-GPU.  

### הוספת שיוך תפקידים

כדי לכוונן מדויק ולפרוס את המודלים שלך, עליך קודם ליצור User Assigned Managed Identity (UAI) ולהקצות לה את ההרשאות המתאימות. ה-UAI ישמש לאימות במהלך הפריסה.

#### יצירת User Assigned Managed Identity (UAI)

1. הקלד *managed identities* בשורת החיפוש בראש דף הפורטל ובחר **Managed Identities** מתוך האפשרויות שמופיעות.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.he.png)

1. בחר **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.he.png)

1. בצע את המשימות הבאות:

    - בחר את **Subscription** של Azure שלך.  
    - בחר את **Resource group** לשימוש (צור חדש במידת הצורך).  
    - בחר את **Region** שבו תרצה להשתמש.  
    - הזן את ה-**Name**. חייב להיות ערך ייחודי.  

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.he.png)

1. בחר **Review + create**.

1. בחר **+ Create**.

#### הוספת שיוך תפקיד Contributor ל-Managed Identity

1. עבור למשאב Managed Identity שיצרת.

1. בחר **Azure role assignments** מהטאב בצד שמאל.

1. בחר **+Add role assignment** מתפריט הניווט.

1. בדף Add role assignment, בצע את המשימות הבאות:  
    - בחר את **Scope** ל-**Resource group**.  
    - בחר את **Subscription** של Azure שלך.  
    - בחר את **Resource group** לשימוש.  
    - בחר את **Role** ל-**Contributor**.  

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.he.png)

2. בחר **Save**.

#### הוספת שיוך תפקיד Storage Blob Data Reader ל-Managed Identity

1. הקלד *storage accounts* בשורת החיפוש בראש דף הפורטל ובחר **Storage accounts** מתוך האפשרויות שמופיעות.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.he.png)

1. בחר את חשבון האחסון המשויך ל-Azure Machine Learning workspace שיצרת. לדוגמה, *finetunephistorage*.

1. בצע את המשימות הבאות כדי לנווט לדף Add role assignment:

    - עבור לחשבון האחסון של Azure שיצרת.  
    - בחר **Access Control (IAM)** מהטאב בצד שמאל.  
    - בחר **+ Add** מתפריט הניווט.  
    - בחר **Add role assignment** מתפריט הניווט.  

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.he.png)

1. בדף Add role assignment, בצע את המשימות הבאות:

    - בדף Role, הקלד *Storage Blob Data Reader* בשורת החיפוש ובחר **Storage Blob Data Reader** מתוך האפשרויות שמופיעות.  
    - בדף Role, בחר **Next**.  
    - בדף Members, בחר **Assign access to** **Managed identity**.  
    - בדף Members, בחר **+ Select members**.  
    - בדף Select managed identities, בחר את **Subscription** של Azure שלך.  
    - בדף Select managed identities, בחר את ה-**Managed identity** ל-**Manage Identity**.  
    - בדף Select managed identities, בחר את ה-Manage Identity שיצרת. לדוגמה, *finetunephi-managedidentity*.  
    - בדף Select managed identities, בחר **Select**.  

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.he.png)

1. בחר **Review + assign**.

#### הוספת שיוך תפקיד AcrPull ל-Managed Identity

1. הקלד *container registries* בשורת החיפוש בראש דף הפורטל ובחר **Container registries** מתוך האפשרויות שמופיעות.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.he.png)

1. בחר את רישום המכולות המשויך ל-Azure Machine Learning workspace. לדוגמה, *finetunephicontainerregistry*

1. בצע את המשימות הבאות כדי לנווט לדף Add role assignment:

    - בחר **Access Control (IAM)** מהטאב בצד שמאל.  
    - בחר **+ Add** מתפריט הניווט.  
    - בחר **Add role assignment** מתפריט הניווט.  

1. בדף Add role assignment, בצע את המשימות הבאות:

    - בדף Role, הקלד *AcrPull* בשורת החיפוש ובחר **AcrPull** מתוך האפשרויות שמופיעות.  
    - בדף Role, בחר **Next**.  
    - בדף Members, בחר **Assign access to** **Managed identity**.  
    - בדף Members, בחר **+ Select members**.  
    - בדף Select managed identities, בחר את **Subscription** של Azure שלך.  
    - בדף Select managed identities, בחר את ה-**Managed identity** ל-**Manage Identity**.  
    - בדף Select managed identities, בחר את ה-Manage Identity שיצרת. לדוגמה, *finetunephi-managedidentity*.  
    - בדף Select managed identities, בחר **Select**.  
    - בחר **Review + assign**.

### הקמת פרויקט

כדי להוריד את מערכי הנתונים הדרושים לכוונון מדויק, תקים סביבה מקומית.

בתרגיל זה תעשה את הדברים הבאים:

- תיצור תיקייה לעבודה בתוכה.  
- תקים סביבה וירטואלית.  
- תתקין את החבילות הנדרשות.  
- תיצור קובץ *download_dataset.py* להורדת מערך הנתונים.

#### יצירת תיקייה לעבודה בתוכה

1. פתח חלון טרמינל והקלד את הפקודה הבאה ליצירת תיקייה בשם *finetune-phi* בנתיב ברירת המחדל.

    ```console
    mkdir finetune-phi
    ```

2. הקלד את הפקודה הבאה בטרמינל כדי לנווט לתיקיית *finetune-phi* שיצרת.
#### יצירת סביבה וירטואלית

1. הקלד את הפקודה הבאה בתוך הטרמינל שלך כדי ליצור סביבה וירטואלית בשם *.venv*.

2. הקלד את הפקודה הבאה בתוך הטרמינל שלך כדי להפעיל את הסביבה הווירטואלית.


> [!NOTE]
> אם זה עבד, תראה את *(.venv)* לפני שורת הפקודה.

#### התקנת החבילות הנדרשות

1. הקלד את הפקודות הבאות בתוך הטרמינל שלך כדי להתקין את החבילות הנדרשות.

#### יצירת `donload_dataset.py`

> [!NOTE]
> מבנה התיקייה המלא:
>
1. פתח את **Visual Studio Code**.

1. בחר ב-**File** בסרגל התפריטים.

1. בחר ב-**Open Folder**.

1. בחר בתיקיית *finetune-phi* שיצרת, שנמצאת ב-*C:\Users\yourUserName\finetune-phi*.

    ![בחר את התיקייה שיצרת.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.he.png)

1. בחלונית השמאלית של Visual Studio Code, לחץ קליק ימני ובחר **New File** כדי ליצור קובץ חדש בשם *download_dataset.py*.

    ![צור קובץ חדש.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.he.png)

### הכנת מערך הנתונים לכוונון עדין

בתרגיל זה, תריץ את הקובץ *download_dataset.py* כדי להוריד את מערכי הנתונים *ultrachat_200k* לסביבה המקומית שלך. לאחר מכן תשתמש במערכי הנתונים האלה כדי לכוונן עדין את מודל Phi-3 ב-Azure Machine Learning.

בתרגיל זה תעשה את הדברים הבאים:

- תוסיף קוד לקובץ *download_dataset.py* להורדת מערכי הנתונים.
- תריץ את הקובץ *download_dataset.py* כדי להוריד את מערכי הנתונים לסביבה המקומית שלך.

#### הורדת מערך הנתונים שלך באמצעות *download_dataset.py*

1. פתח את הקובץ *download_dataset.py* ב-Visual Studio Code.

1. הוסף את הקוד הבא לתוך הקובץ *download_dataset.py*.

1. הקלד את הפקודה הבאה בתוך הטרמינל שלך כדי להריץ את הסקריפט ולהוריד את מערך הנתונים לסביבה המקומית שלך.

1. ודא שמערכי הנתונים נשמרו בהצלחה בתיקיית *finetune-phi/data* המקומית שלך.

> [!NOTE]
>
> #### הערה לגבי גודל מערך הנתונים וזמן הכוונון העדין
>
> במדריך זה, אתה משתמש רק ב-1% ממערך הנתונים (`split='train[:1%]'`). זה מקטין משמעותית את כמות הנתונים, ומאיץ הן את תהליך ההעלאה והן את תהליך הכוונון העדין. ניתן לשנות את האחוז כדי למצוא את האיזון הנכון בין זמן האימון לביצועי המודל. שימוש בתת-קבוצה קטנה יותר של מערך הנתונים מקטין את הזמן הנדרש לכוונון, מה שהופך את התהליך לנוח יותר למדריך.

## תרחיש 2: כוונון עדין של מודל Phi-3 ופריסה ב-Azure Machine Learning Studio

### כוונון עדין של מודל Phi-3

בתרגיל זה, תכוונן עדין את מודל Phi-3 ב-Azure Machine Learning Studio.

בתרגיל זה תעשה את הדברים הבאים:

- יצירת אשכול מחשבים לכוונון עדין.
- כוונון עדין של מודל Phi-3 ב-Azure Machine Learning Studio.

#### יצירת אשכול מחשבים לכוונון עדין

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בחר ב-**Compute** מהכרטיסייה בצד שמאל.

1. בחר ב-**Compute clusters** מתפריט הניווט.

1. בחר ב-**+ New**.

    ![בחר מחשוב.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.he.png)

1. בצע את המשימות הבאות:

    - בחר את **Region** שברצונך להשתמש בו.
    - בחר את **Virtual machine tier** ל-**Dedicated**.
    - בחר את **Virtual machine type** ל-**GPU**.
    - בחר את סינון **Virtual machine size** ל-**Select from all options**.
    - בחר את **Virtual machine size** ל-**Standard_NC24ads_A100_v4**.

    ![צור אשכול.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.he.png)

1. בחר **Next**.

1. בצע את המשימות הבאות:

    - הזן **Compute name**. חייב להיות ערך ייחודי.
    - בחר את **Minimum number of nodes** ל-**0**.
    - בחר את **Maximum number of nodes** ל-**1**.
    - בחר את **Idle seconds before scale down** ל-**120**.

    ![צור אשכול.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.he.png)

1. בחר **Create**.

#### כוונון עדין של מודל Phi-3

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בחר את סביבת העבודה של Azure Machine Learning שיצרת.

    ![בחר את סביבת העבודה שיצרת.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.he.png)

1. בצע את המשימות הבאות:

    - בחר ב-**Model catalog** מהכרטיסייה בצד שמאל.
    - הקלד *phi-3-mini-4k* בשורת החיפוש ובחר ב-**Phi-3-mini-4k-instruct** מהאפשרויות שמופיעות.

    ![הקלד phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.he.png)

1. בחר ב-**Fine-tune** מתפריט הניווט.

    ![בחר כוונון עדין.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.he.png)

1. בצע את המשימות הבאות:

    - בחר ב-**Select task type** ל-**Chat completion**.
    - בחר ב-**+ Select data** להעלאת **Traning data**.
    - בחר את סוג העלאת נתוני האימות ל-**Provide different validation data**.
    - בחר ב-**+ Select data** להעלאת **Validation data**.

    ![מלא את דף הכוונון העדין.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.he.png)

    > [!TIP]
    >
    > ניתן לבחור ב-**Advanced settings** כדי להתאים אישית הגדרות כמו **learning_rate** ו-**lr_scheduler_type** כדי לייעל את תהליך הכוונון העדין בהתאם לצרכים הספציפיים שלך.

1. בחר **Finish**.

1. בתרגיל זה, הצלחת לכוונן עדין את מודל Phi-3 באמצעות Azure Machine Learning. שים לב שתהליך הכוונון העדין עלול לקחת זמן משמעותי. לאחר הרצת משימת הכוונון, יש להמתין לסיומה. ניתן לעקוב אחר מצב המשימה בכרטיסיית Jobs בצד שמאל של סביבת העבודה שלך ב-Azure Machine Learning. בסדרה הבאה, תפרוס את המודל המכוונן ותשלב אותו עם Prompt flow.

    ![ראה את משימת הכוונון העדין.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.he.png)

### פריסת מודל Phi-3 המכוונן עדין

כדי לשלב את מודל Phi-3 המכוונן עם Prompt flow, יש לפרוס את המודל כדי שיהיה נגיש להסקת מסקנות בזמן אמת. תהליך זה כולל רישום המודל, יצירת נקודת קצה מקוונת ופריסת המודל.

בתרגיל זה תעשה את הדברים הבאים:

- רישום המודל המכוונן בסביבת העבודה של Azure Machine Learning.
- יצירת נקודת קצה מקוונת.
- פריסת מודל Phi-3 המכוונן שנרשם.

#### רישום המודל המכוונן

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בחר את סביבת העבודה של Azure Machine Learning שיצרת.

    ![בחר את סביבת העבודה שיצרת.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.he.png)

1. בחר ב-**Models** מהכרטיסייה בצד שמאל.

1. בחר ב-**+ Register**.

1. בחר ב-**From a job output**.

    ![רשום מודל.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.he.png)

1. בחר את המשימה שיצרת.

    ![בחר משימה.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.he.png)

1. בחר **Next**.

1. בחר את **Model type** ל-**MLflow**.

1. ודא ש-**Job output** מסומן; זה אמור להיבחר אוטומטית.

    ![בחר פלט.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.he.png)

2. בחר **Next**.

3. בחר **Register**.

    ![בחר רישום.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.he.png)

4. ניתן לצפות במודל שנרשם על ידי ניווט לתפריט **Models** מהכרטיסייה בצד שמאל.

    ![מודל שנרשם.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.he.png)

#### פריסת המודל המכוונן

1. עבור לסביבת העבודה של Azure Machine Learning שיצרת.

1. בחר ב-**Endpoints** מהכרטיסייה בצד שמאל.

1. בחר ב-**Real-time endpoints** מתפריט הניווט.

    ![צור נקודת קצה.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.he.png)

1. בחר **Create**.

1. בחר את המודל שנרשם שיצרת.

    ![בחר מודל שנרשם.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.he.png)

1. בחר **Select**.

1. בצע את המשימות הבאות:

    - בחר ב-**Virtual machine** ל-*Standard_NC6s_v3*.
    - בחר את מספר המופעים שברצונך להשתמש בו. לדוגמה, *1*.
    - בחר את **Endpoint** ל-**New** כדי ליצור נקודת קצה חדשה.
    - הזן **Endpoint name**. חייב להיות ערך ייחודי.
    - הזן **Deployment name**. חייב להיות ערך ייחודי.

    ![מלא את הגדרות הפריסה.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.he.png)

1. בחר **Deploy**.

> [!WARNING]
> כדי למנוע חיובים נוספים בחשבונך, ודא למחוק את נקודת הקצה שיצרת בסביבת העבודה של Azure Machine Learning.
>

#### בדיקת מצב הפריסה בסביבת העבודה של Azure Machine Learning

1. עבור לסביבת העבודה של Azure Machine Learning שיצרת.

1. בחר ב-**Endpoints** מהכרטיסייה בצד שמאל.

1. בחר את נקודת הקצה שיצרת.

    ![בחר נקודות קצה](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.he.png)

1. בדף זה ניתן לנהל את נקודות הקצה במהלך תהליך הפריסה.

> [!NOTE]
> לאחר שהפריסה הושלמה, ודא ש-**Live traffic** מוגדר ל-**100%**. אם לא, בחר ב-**Update traffic** כדי לעדכן את הגדרות התנועה. שים לב שלא ניתן לבדוק את המודל אם התנועה מוגדרת ל-0%.
>
> ![הגדר תנועה.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.he.png)
>

## תרחיש 3: שילוב עם Prompt flow ושיחה עם המודל המותאם שלך ב-Azure AI Foundry

### שילוב מודל Phi-3 המותאם עם Prompt flow

לאחר שהפרסת בהצלחה את המודל המכוונן שלך, כעת תוכל לשלב אותו עם Prompt Flow כדי להשתמש במודל שלך באפליקציות בזמן אמת, מה שמאפשר מגוון משימות אינטראקטיביות עם מודל Phi-3 המותאם שלך.

בתרגיל זה תעשה את הדברים הבאים:

- יצירת Azure AI Foundry Hub.
- יצירת פרויקט ב-Azure AI Foundry.
- יצירת Prompt flow.
- הוספת חיבור מותאם למודל Phi-3 המכוונן.
- הגדרת Prompt flow לשיחה עם מודל Phi-3 המותאם שלך.
> [!NOTE]
> ניתן גם לשלב עם Promptflow באמצעות Azure ML Studio. ניתן ליישם את אותו תהליך השילוב גם ב-Azure ML Studio.
#### יצירת Azure AI Foundry Hub

עליך ליצור Hub לפני יצירת הפרויקט. ה-Hub מתפקד כמו Resource Group, ומאפשר לך לארגן ולנהל מספר פרויקטים בתוך Azure AI Foundry.

1. בקר ב-[Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. בחר **All hubs** מהטאב בצד שמאל.

1. בחר **+ New hub** מתפריט הניווט.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.he.png)

1. בצע את המשימות הבאות:

    - הזן **Hub name**. חייב להיות ערך ייחודי.
    - בחר את **Subscription** שלך ב-Azure.
    - בחר את **Resource group** לשימוש (צור חדש במידת הצורך).
    - בחר את **Location** הרצוי.
    - בחר את **Connect Azure AI Services** לשימוש (צור חדש במידת הצורך).
    - בחר ב-**Connect Azure AI Search** את האפשרות **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.he.png)

1. בחר **Next**.

#### יצירת פרויקט ב-Azure AI Foundry

1. ב-Hub שיצרת, בחר **All projects** מהטאב בצד שמאל.

1. בחר **+ New project** מתפריט הניווט.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.he.png)

1. הזן **Project name**. חייב להיות ערך ייחודי.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.he.png)

1. בחר **Create a project**.

#### הוספת חיבור מותאם אישית למודל Phi-3 המותאם

כדי לשלב את מודל Phi-3 המותאם שלך עם Prompt flow, עליך לשמור את נקודת הקצה והמפתח של המודל בחיבור מותאם אישית. הגדרה זו מבטיחה גישה למודל Phi-3 המותאם שלך בתוך Prompt flow.

#### הגדרת api key ו-endpoint uri של מודל Phi-3 המותאם

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. עבור לסביבת העבודה של Azure Machine learning שיצרת.

1. בחר **Endpoints** מהטאב בצד שמאל.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.he.png)

1. בחר את נקודת הקצה שיצרת.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.he.png)

1. בחר **Consume** מתפריט הניווט.

1. העתק את **REST endpoint** ואת **Primary key** שלך.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.he.png)

#### הוספת החיבור המותאם

1. בקר ב-[Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. עבור לפרויקט Azure AI Foundry שיצרת.

1. בפרויקט שיצרת, בחר **Settings** מהטאב בצד שמאל.

1. בחר **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.he.png)

1. בחר **Custom keys** מתפריט הניווט.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.he.png)

1. בצע את המשימות הבאות:

    - בחר **+ Add key value pairs**.
    - עבור שם המפתח, הזן **endpoint** והדבק את נקודת הקצה שהעתקת מ-Azure ML Studio בשדה הערך.
    - בחר שוב **+ Add key value pairs**.
    - עבור שם המפתח, הזן **key** והדבק את המפתח שהעתקת מ-Azure ML Studio בשדה הערך.
    - לאחר הוספת המפתחות, סמן **is secret** כדי למנוע חשיפת המפתח.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.he.png)

1. בחר **Add connection**.

#### יצירת Prompt flow

הוספת חיבור מותאם אישית ב-Azure AI Foundry. כעת, ניצור Prompt flow באמצעות השלבים הבאים. לאחר מכן, תחבר את ה-Prompt flow לחיבור המותאם כדי שתוכל להשתמש במודל המותאם בתוך ה-Prompt flow.

1. עבור לפרויקט Azure AI Foundry שיצרת.

1. בחר **Prompt flow** מהטאב בצד שמאל.

1. בחר **+ Create** מתפריט הניווט.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.he.png)

1. בחר **Chat flow** מתפריט הניווט.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.he.png)

1. הזן **Folder name** לשימוש.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.he.png)

2. בחר **Create**.

#### הגדרת Prompt flow לשיחה עם מודל Phi-3 המותאם שלך

עליך לשלב את מודל Phi-3 המותאם לתוך Prompt flow. עם זאת, ה-Prompt flow הקיים אינו מותאם למטרה זו. לכן, יש לעצב מחדש את ה-Prompt flow כדי לאפשר את השילוב של המודל המותאם.

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

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.he.png)

1. הוסף את הקוד הבא לקובץ *integrate_with_promptflow.py* כדי להשתמש במודל Phi-3 המותאם ב-Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
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

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.he.png)

> [!NOTE]
> למידע מפורט יותר על שימוש ב-Prompt flow ב-Azure AI Foundry, ניתן לעיין ב-[Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. בחר **Chat input**, **Chat output** כדי לאפשר שיחה עם המודל שלך.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.he.png)

1. כעת אתה מוכן לשוחח עם מודל Phi-3 המותאם שלך. בתרגיל הבא תלמד כיצד להפעיל את ה-Prompt flow ולהשתמש בו לשיחה עם מודל Phi-3 המותאם שלך.

> [!NOTE]
>
> הזרימה המחודשת אמורה להיראות כמו בתמונה למטה:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.he.png)
>

### שיחה עם מודל Phi-3 המותאם שלך

כעת, לאחר שהכנת ושילבת את מודל Phi-3 המותאם שלך עם Prompt flow, אתה מוכן להתחיל באינטראקציה איתו. תרגיל זה ינחה אותך בתהליך ההגדרה וההפעלה של שיחה עם המודל באמצעות Prompt flow. על ידי ביצוע השלבים, תוכל לנצל במלואן את היכולות של מודל Phi-3 המותאם שלך למשימות ושיחות שונות.

- שוחח עם מודל Phi-3 המותאם שלך באמצעות Prompt flow.

#### הפעלת Prompt flow

1. בחר **Start compute sessions** כדי להפעיל את ה-Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.he.png)

1. בחר **Validate and parse input** כדי לעדכן את הפרמטרים.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.he.png)

1. בחר את **Value** של **connection** לחיבור המותאם שיצרת. לדוגמה, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.he.png)

#### שיחה עם המודל המותאם שלך

1. בחר **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.he.png)

1. הנה דוגמה לתוצאות: כעת תוכל לשוחח עם מודל Phi-3 המותאם שלך. מומלץ לשאול שאלות המבוססות על הנתונים ששימשו לאימון המודל.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.he.png)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפת המקור כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.