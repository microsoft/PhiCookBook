<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-05-09T17:39:12+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "he"
}
-->
# כוונון מדויק ואינטגרציה של דגמי Phi-3 מותאמים אישית עם Prompt flow

דוגמת קצה-לקצה (E2E) זו מבוססת על המדריך "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" מקהילת הטכנולוגיה של מיקרוסופט. היא מציגה את התהליכים של כוונון מדויק, פריסה ואינטגרציה של דגמי Phi-3 מותאמים אישית עם Prompt flow.

## סקירה כללית

בדוגמת ה-E2E הזו תלמד כיצד לכוונן במדויק את דגם Phi-3 ולשלב אותו עם Prompt flow. באמצעות Azure Machine Learning ו-Prompt flow, תיצור תהליך עבודה לפריסה ושימוש בדגמי AI מותאמים אישית. דוגמת ה-E2E מחולקת לשלושה תרחישים:

**תרחיש 1: הקמת משאבי Azure והכנה לכוונון מדויק**

**תרחיש 2: כוונון מדויק של דגם Phi-3 ופריסה ב-Azure Machine Learning Studio**

**תרחיש 3: אינטגרציה עם Prompt flow וצ'אט עם הדגם המותאם שלך**

להלן סקירה של דוגמת ה-E2E הזו.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.he.png)

### תוכן העניינים

1. **[תרחיש 1: הקמת משאבי Azure והכנה לכוונון מדויק](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [יצירת סביבת עבודה ב-Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [בקשת מכסות GPU במנוי Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [הוספת שיוך תפקיד](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [הקמת פרויקט](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [הכנת מאגר נתונים לכוונון מדויק](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[תרחיש 2: כוונון מדויק של דגם Phi-3 ופריסה ב-Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [הקמת Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [כוונון מדויק של דגם Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [פריסת הדגם המכוונן](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[תרחיש 3: אינטגרציה עם Prompt flow וצ'אט עם הדגם המותאם שלך](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [אינטגרציה של דגם Phi-3 מותאם אישית עם Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [צ'אט עם הדגם המותאם שלך](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## תרחיש 1: הקמת משאבי Azure והכנה לכוונון מדויק

### יצירת סביבת עבודה ב-Azure Machine Learning

1. הקלד *azure machine learning* בשורת החיפוש בראש דף הפורטל ובחר **Azure Machine Learning** מתוך האפשרויות שמופיעות.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.he.png)

1. בחר **+ Create** מתפריט הניווט.

1. בחר **New workspace** מתפריט הניווט.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.he.png)

1. בצע את המשימות הבאות:

    - בחר את **המנוי** שלך ב-Azure.
    - בחר את **קבוצת המשאבים** לשימוש (צור חדשה אם צריך).
    - הזן **שם סביבת העבודה**. חייב להיות ערך ייחודי.
    - בחר את **האזור** שבו תרצה להשתמש.
    - בחר את **חשבון האחסון** לשימוש (צור חדש אם צריך).
    - בחר את **Key vault** לשימוש (צור חדש אם צריך).
    - בחר את **Application insights** לשימוש (צור חדש אם צריך).
    - בחר את **רישום המכולות** לשימוש (צור חדש אם צריך).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.he.png)

1. בחר **Review + Create**.

1. בחר **Create**.

### בקשת מכסות GPU במנוי Azure

בדוגמת ה-E2E הזו, תשתמש ב-*Standard_NC24ads_A100_v4 GPU* לכוונון מדויק, שדורש בקשת מכסה, וב-*Standard_E4s_v3* CPU לפריסה, שאינה דורשת בקשת מכסה.

> [!NOTE]
>
> רק מנויי Pay-As-You-Go (סוג המנוי הסטנדרטי) זכאים להקצאת GPU; מנויי הטבות אינם נתמכים כרגע.
>
> למשתמשים במנויי הטבות (כמו Visual Studio Enterprise Subscription) או למי שרוצה לבדוק במהירות את תהליך הכוונון והפריסה, מדריך זה מספק גם הנחיות לכוונון מדויק עם מאגר נתונים מינימלי באמצעות CPU. עם זאת, חשוב לציין שהתוצאות של הכוונון המדויק טובות משמעותית כאשר משתמשים ב-GPU עם מאגרי נתונים גדולים יותר.

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בצע את המשימות הבאות כדי לבקש מכסת *Standard NCADSA100v4 Family*:

    - בחר **Quota** בלשונית בצד שמאל.
    - בחר את **משפחת המכונות הווירטואליות** לשימוש. לדוגמה, בחר **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, הכוללת את ה-*Standard_NC24ads_A100_v4* GPU.
    - בחר **Request quota** מתפריט הניווט.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.he.png)

    - בדף בקשת המכסה, הזן את **מגבלת הליבות החדשה** שברצונך להשתמש בה. לדוגמה, 24.
    - בדף בקשת המכסה, בחר **Submit** כדי לבקש את מכסת ה-GPU.

> [!NOTE]
> ניתן לבחור את ה-GPU או ה-CPU המתאים לצרכיך על ידי עיון במסמך [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### הוספת שיוך תפקיד

כדי לכוונן ולפרוס את הדגמים שלך, עליך קודם ליצור User Assigned Managed Identity (UAI) ולהקצות לה את ההרשאות המתאימות. ה-UAI ישמש לאימות במהלך הפריסה.

#### יצירת User Assigned Managed Identity (UAI)

1. הקלד *managed identities* בשורת החיפוש בראש דף הפורטל ובחר **Managed Identities** מתוך האפשרויות שמופיעות.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.he.png)

1. בחר **+ Create**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.he.png)

1. בצע את המשימות הבאות:

    - בחר את **המנוי** שלך ב-Azure.
    - בחר את **קבוצת המשאבים** לשימוש (צור חדשה אם צריך).
    - בחר את **האזור** שבו תרצה להשתמש.
    - הזן את **השם**. חייב להיות ערך ייחודי.

1. בחר **Review + create**.

1. בחר **+ Create**.

#### הוספת שיוך תפקיד Contributor ל-Managed Identity

1. נווט למשאב Managed Identity שיצרת.

1. בחר **Azure role assignments** בלשונית בצד שמאל.

1. בחר **+Add role assignment** מתפריט הניווט.

1. בדף הוספת שיוך תפקיד, בצע את המשימות הבאות:
    - בחר את **היקף** ל-**Resource group**.
    - בחר את **המנוי** שלך ב-Azure.
    - בחר את **קבוצת המשאבים** לשימוש.
    - בחר את **התפקיד** ל-**Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.he.png)

1. בחר **Save**.

#### הוספת שיוך תפקיד Storage Blob Data Reader ל-Managed Identity

1. הקלד *storage accounts* בשורת החיפוש בראש דף הפורטל ובחר **Storage accounts** מתוך האפשרויות שמופיעות.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.he.png)

1. בחר את חשבון האחסון המשויך לסביבת העבודה של Azure Machine Learning שיצרת. לדוגמה, *finetunephistorage*.

1. בצע את המשימות הבאות כדי לנווט לדף הוספת שיוך תפקיד:

    - נווט לחשבון האחסון של Azure שיצרת.
    - בחר **Access Control (IAM)** בלשונית בצד שמאל.
    - בחר **+ Add** מתפריט הניווט.
    - בחר **Add role assignment** מתפריט הניווט.

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.he.png)

1. בדף הוספת שיוך תפקיד, בצע את המשימות הבאות:

    - בדף התפקיד, הקלד *Storage Blob Data Reader* בשורת החיפוש ובחר **Storage Blob Data Reader** מתוך האפשרויות שמופיעות.
    - בדף התפקיד, בחר **Next**.
    - בדף החברים, בחר **Assign access to** **Managed identity**.
    - בדף החברים, בחר **+ Select members**.
    - בדף בחירת managed identities, בחר את **המנוי** שלך ב-Azure.
    - בדף בחירת managed identities, בחר את **Managed identity** ל-**Manage Identity**.
    - בדף בחירת managed identities, בחר את ה-Managed Identity שיצרת. לדוגמה, *finetunephi-managedidentity*.
    - בדף בחירת managed identities, בחר **Select**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.he.png)

1. בחר **Review + assign**.

#### הוספת שיוך תפקיד AcrPull ל-Managed Identity

1. הקלד *container registries* בשורת החיפוש בראש דף הפורטל ובחר **Container registries** מתוך האפשרויות שמופיעות.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.he.png)

1. בחר את רישום המכולות המשויך לסביבת העבודה של Azure Machine Learning. לדוגמה, *finetunephicontainerregistries*

1. בצע את המשימות הבאות כדי לנווט לדף הוספת שיוך תפקיד:

    - בחר **Access Control (IAM)** בלשונית בצד שמאל.
    - בחר **+ Add** מתפריט הניווט.
    - בחר **Add role assignment** מתפריט הניווט.

1. בדף הוספת שיוך תפקיד, בצע את המשימות הבאות:

    - בדף התפקיד, הקלד *AcrPull* בשורת החיפוש ובחר **AcrPull** מתוך האפשרויות שמופיעות.
    - בדף התפקיד, בחר **Next**.
    - בדף החברים, בחר **Assign access to** **Managed identity**.
    - בדף החברים, בחר **+ Select members**.
    - בדף בחירת managed identities, בחר את **המנוי** שלך ב-Azure.
    - בדף בחירת managed identities, בחר את **Managed identity** ל-**Manage Identity**.
    - בדף בחירת managed identities, בחר את ה-Managed Identity שיצרת. לדוגמה, *finetunephi-managedidentity*.
    - בדף בחירת managed identities, בחר **Select**.
    - בחר **Review + assign**.

### הקמת פרויקט

כעת, תיצור תיקייה לעבודה ותגדיר סביבה וירטואלית לפיתוח תוכנית שמתקשרת עם משתמשים ומשתמשת בהיסטוריית הצ'אט השמורה ב-Azure Cosmos DB כדי להעשיר את התגובות שלה.

#### יצירת תיקייה לעבודה בתוכה

1. פתח חלון טרמינל והקלד את הפקודה הבאה כדי ליצור תיקייה בשם *finetune-phi* בנתיב ברירת המחדל.

    ```console
    mkdir finetune-phi
    ```

1. הקלד את הפקודה הבאה בטרמינל כדי לנווט לתיקיית *finetune-phi* שיצרת.

    ```console
    cd finetune-phi
    ```

#### יצירת סביבה וירטואלית

1. הקלד את הפקודה הבאה בטרמינל כדי ליצור סביבה וירטואלית בשם *.venv*.

    ```console
    python -m venv .venv
    ```

1. הקלד את הפקודה הבאה בטרמינל כדי להפעיל את הסביבה הווירטואלית.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> אם ההפעלה הצליחה, תראה את *( .venv )* לפני שורת הפקודה.

#### התקנת החבילות הנדרשות

1. הקלד את הפקודות הבאות בטרמינל כדי להתקין את החבילות הנדרשות.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### יצירת קבצי הפרויקט

בתרגיל זה, תיצור את הקבצים החיוניים לפרויקט שלנו. קבצים אלה כוללים סקריפטים להורדת מאגר הנתונים, הקמת סביבת Azure Machine Learning, כוונון מדויק של דגם Phi-3, ופריסת הדגם המכוונן. כמו כן, תיצור קובץ *conda.yml* להגדרת סביבת הכוונון המדויק.

בתרגיל זה תבצע:

- יצירת קובץ *download_dataset.py* להורדת מאגר הנתונים.
- יצירת קובץ *setup_ml.py* להקמת סביבת Azure Machine Learning.
- יצירת קובץ *fine_tune.py* בתיקיית *finetuning_dir* לכוונון מדויק של דגם Phi-3 באמצעות מאגר הנתונים.
- יצירת קובץ *conda.yml* להגדרת סביבת הכוונון המדויק.
- יצירת קובץ *deploy_model.py* לפריסת הדגם המכוונן.
- יצירת קובץ *integrate_with_promptflow.py* לאינטגרציה עם Prompt flow ולהפעלת הדגם.
- יצירת קובץ flow.dag.yml להגדרת מבנה תהליך העבודה ב-Prompt flow.
- יצירת קובץ *config.py* להזנת מידע על Azure.

> [!NOTE]
>
> מבנה התיקייה המלא:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. פתח את **Visual Studio Code**.

1. בחר **File** משורת התפריטים.

1. בחר **Open Folder**.

1. בחר את תיקיית *finetune-phi* שיצרת, שנמצאת ב-*C:\Users\yourUserName\finetune-phi*.

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.he.png)

1. בחלונית השמאלית של Visual Studio Code, לחץ קליק ימני ובחר **New File** כדי ליצור קובץ חדש בשם *download_dataset.py*.

1. בחלונית השמאלית של Visual Studio Code, לחץ קליק ימני ובחר **New File** כדי ליצור קובץ חדש בשם *setup_ml.py*.

1. בחלונית השמאלית של Visual Studio Code, לחץ קליק ימני ובחר **New File** כדי ליצור קובץ חדש בשם *deploy_model.py*.

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.he.png)

1. בחלונית השמאלית של Visual Studio Code, לחץ קליק ימני ובחר **New Folder** כדי ליצור תיקייה חדשה בשם *finetuning_dir*.

1. בתיקיית *finetuning_dir*, צור קובץ חדש בשם *fine_tune.py*.

#### יצירה והגדרת קובץ *conda.yml*

1. בחלונית השמאלית של Visual Studio Code, לחץ קליק ימני ובחר **New File** כדי ליצור קובץ חדש בשם *conda.yml*.

1. הוסף את הקוד הבא לקובץ *conda.yml* כדי להגדיר את סביבת הכוונון המדויק עבור דגם Phi-3.

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### יצירה והגדרת קובץ *config.py*

1. בחלונית השמאלית של Visual Studio Code, לחץ קליק ימני ובחר **New File** כדי ליצור קובץ חדש בשם *config.py*.

1. הוסף את הקוד הבא לקובץ *config.py* כדי לכל
![מצא מזהה מנוי.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.he.png)

1. בצע את המשימות הבאות כדי להוסיף את שם סביבת העבודה של Azure:

    - נווט למשאב Azure Machine Learning שיצרת.
    - העתק והדבק את שם החשבון שלך לתוך קובץ *config.py*.

    ![מצא שם Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.he.png)

1. בצע את המשימות הבאות כדי להוסיף את שם קבוצת המשאבים של Azure:

    - נווט למשאב Azure Machine Learning שיצרת.
    - העתק והדבק את שם קבוצת המשאבים של Azure לתוך קובץ *config.py*.

    ![מצא שם קבוצת משאבים.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.he.png)

2. בצע את המשימות הבאות כדי להוסיף את שם הזהות המנוהלת של Azure

    - נווט למשאב Managed Identities שיצרת.
    - העתק והדבק את שם הזהות המנוהלת של Azure לתוך קובץ *config.py*.

    ![מצא UAI.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.he.png)

### הכנת מערך הנתונים לכוונון עדין

בתרגיל זה, תריץ את קובץ *download_dataset.py* כדי להוריד את מערכי הנתונים *ULTRACHAT_200k* לסביבת העבודה המקומית שלך. לאחר מכן תשתמש במערכי הנתונים האלה כדי לכוונן עדין את מודל Phi-3 ב-Azure Machine Learning.

#### הורדת מערך הנתונים שלך באמצעות *download_dataset.py*

1. פתח את קובץ *download_dataset.py* ב-Visual Studio Code.

1. הוסף את הקוד הבא לתוך *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **הנחיות לכוונון עדין עם מערך נתונים מינימלי באמצעות מעבד (CPU)**
>
> אם ברצונך להשתמש במעבד לכוונון עדין, גישה זו מתאימה למי שיש לו מנויי הטבות (כגון Visual Studio Enterprise Subscription) או למי שרוצה לבדוק במהירות את תהליך הכוונון והפריסה.
>
> החלף את `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. הקלד את הפקודה הבאה בתוך הטרמינל שלך כדי להריץ את הסקריפט ולהוריד את מערך הנתונים לסביבת העבודה המקומית שלך.

    ```console
    python download_data.py
    ```

1. ודא שמערכי הנתונים נשמרו בהצלחה בתיקייה המקומית *finetune-phi/data*.

> [!NOTE]
>
> **גודל מערך הנתונים וזמן הכוונון**
>
> בדוגמת E2E זו, אתה משתמש רק ב-1% ממערך הנתונים (`train_sft[:1%]`). זה מקטין משמעותית את כמות הנתונים, ומאיץ את תהליך ההעלאה והכוונון. ניתן להתאים את האחוז כדי למצוא את האיזון המתאים בין זמן האימון לביצועי המודל. שימוש בתת-מערך קטן יותר מקצר את זמן הכוונון, מה שהופך את התהליך לנוח יותר לדוגמת E2E.

## תרחיש 2: כוונון עדין של מודל Phi-3 ופריסה ב-Azure Machine Learning Studio

### הגדרת Azure CLI

יש להגדיר את Azure CLI לאימות הסביבה שלך. Azure CLI מאפשר לך לנהל משאבי Azure ישירות משורת הפקודה ומספק את האישורים הדרושים ל-Azure Machine Learning לגישה למשאבים אלה. כדי להתחיל התקן את [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. פתח חלון טרמינל והקלד את הפקודה הבאה כדי להיכנס לחשבון Azure שלך.

    ```console
    az login
    ```

1. בחר את חשבון Azure שלך לשימוש.

1. בחר את מנוי Azure שלך לשימוש.

    ![מצא שם קבוצת משאבים.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.he.png)

> [!TIP]
>
> אם יש לך קושי בהתחברות ל-Azure, נסה להשתמש בקוד מכשיר. פתח חלון טרמינל והקלד את הפקודה הבאה כדי להתחבר לחשבון Azure שלך:
>
> ```console
> az login --use-device-code
> ```
>

### כוונון עדין של מודל Phi-3

בתרגיל זה, תכוונן עדין את מודל Phi-3 באמצעות מערך הנתונים שסופק. תחילה תגדיר את תהליך הכוונון בקובץ *fine_tune.py*. לאחר מכן תגדיר את סביבת Azure Machine Learning ותפעיל את תהליך הכוונון על ידי הרצת קובץ *setup_ml.py*. סקריפט זה מוודא שהתהליך מתבצע בסביבת Azure Machine Learning.

בהרצת *setup_ml.py* תבצע את תהליך הכוונון בסביבת Azure Machine Learning.

#### הוסף קוד לקובץ *fine_tune.py*

1. נווט לתיקיית *finetuning_dir* ופתח את קובץ *fine_tune.py* ב-Visual Studio Code.

1. הוסף את הקוד הבא לתוך *fine_tune.py*.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. שמור וסגור את קובץ *fine_tune.py*.

> [!TIP]
> **ניתן לכוונן עדין את מודל Phi-3.5**
>
> בקובץ *fine_tune.py*, ניתן לשנות את השדה `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` בסקריפט שלך.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="כוונון עדין של Phi-3.5.":::
>

#### הוסף קוד לקובץ *setup_ml.py*

1. פתח את קובץ *setup_ml.py* ב-Visual Studio Code.

1. הוסף את הקוד הבא לתוך *setup_ml.py*.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. החלף את `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` בפרטים הספציפיים שלך.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **הנחיות לכוונון עדין עם מערך נתונים מינימלי באמצעות מעבד (CPU)**
>
> אם ברצונך להשתמש במעבד לכוונון עדין, גישה זו מתאימה למי שיש לו מנויי הטבות (כגון Visual Studio Enterprise Subscription) או למי שרוצה לבדוק במהירות את תהליך הכוונון והפריסה.
>
> 1. פתח את קובץ *setup_ml*.
> 1. החלף את `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` בפרטים הספציפיים שלך.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. הקלד את הפקודה הבאה כדי להריץ את סקריפט *setup_ml.py* ולהתחיל את תהליך הכוונון בסביבת Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. בתרגיל זה, כווננת בהצלחה את מודל Phi-3 באמצעות Azure Machine Learning. בהרצת סקריפט *setup_ml.py*, הקמת את סביבת Azure Machine Learning והפעלת את תהליך הכוונון שהוגדר בקובץ *fine_tune.py*. שים לב שתהליך הכוונון עלול לקחת זמן משמעותי. לאחר הרצת `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.he.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` עם השם הרצוי לפריסה שלך.

#### הוסף קוד לקובץ *deploy_model.py*

הרצת קובץ *deploy_model.py* מאוטומטת את כל תהליך הפריסה. הקובץ רושם את המודל, יוצר נקודת קצה ומבצע את הפריסה על פי ההגדרות שבקובץ config.py, הכוללות את שם המודל, שם נקודת הקצה ושם הפריסה.

1. פתח את קובץ *deploy_model.py* ב-Visual Studio Code.

1. הוסף את הקוד הבא לתוך *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. בצע את המשימות הבאות כדי לקבל את `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` עם הפרטים הספציפיים שלך.

1. הקלד את הפקודה הבאה כדי להריץ את סקריפט *deploy_model.py* ולהתחיל את תהליך הפריסה ב-Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> כדי למנוע חיובים נוספים בחשבונך, הקפד למחוק את נקודת הקצה שיצרת בסביבת Azure Machine Learning.
>

#### בדוק את מצב הפריסה בסביבת Azure Machine Learning

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. נווט לסביבת Azure Machine Learning שיצרת.

1. בחר **Studio web URL** כדי לפתוח את סביבת Azure Machine Learning.

1. בחר **Endpoints** מהתפריט בצד שמאל.

    ![בחר נקודות קצה.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.he.png)

2. בחר את נקודת הקצה שיצרת.

    ![בחר נקודות קצה שיצרת.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.he.png)

3. בדף זה תוכל לנהל את נקודות הקצה שנוצרו במהלך תהליך הפריסה.

## תרחיש 3: אינטגרציה עם Prompt flow ושיחה עם המודל המותאם אישית שלך

### אינטגרציה של מודל Phi-3 מותאם אישית עם Prompt flow

לאחר שהפרסת בהצלחה את המודל המכוונן שלך, כעת תוכל לשלב אותו עם Prompt flow כדי להשתמש במודל שלך באפליקציות בזמן אמת, המאפשרות מגוון משימות אינטראקטיביות עם מודל Phi-3 המותאם אישית שלך.

#### הגדר את מפתח ה-API וכתובת נקודת הקצה של מודל Phi-3 המכוונן

1. נווט לסביבת Azure Machine Learning שיצרת.
1. בחר **Endpoints** מהתפריט בצד שמאל.
1. בחר את נקודת הקצה שיצרת.
1. בחר **Consume** מתפריט הניווט.
1. העתק והדבק את **REST endpoint** שלך לתוך קובץ *config.py*, תוך החלפת `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` עם ה**מפתח הראשי** שלך.

    ![העתק מפתח API וכתובת נקודת הקצה.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.he.png)

#### הוסף קוד לקובץ *flow.dag.yml*

1. פתח את קובץ *flow.dag.yml* ב-Visual Studio Code.

1. הוסף את הקוד הבא לתוך *flow.dag.yml*.

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

#### הוסף קוד לקובץ *integrate_with_promptflow.py*

1. פתח את קובץ *integrate_with_promptflow.py* ב-Visual Studio Code.

1. הוסף את הקוד הבא לתוך *integrate_with_promptflow.py*.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### שיחה עם המודל המותאם אישית שלך

1. הקלד את הפקודה הבאה כדי להריץ את סקריפט *deploy_model.py* ולהתחיל את תהליך הפריסה ב-Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. הנה דוגמה לתוצאות: כעת תוכל לשוחח עם מודל Phi-3 המותאם אישית שלך. מומלץ לשאול שאלות בהתבסס על הנתונים ששימשו לכוונון עדין.

    ![דוגמת Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.he.png)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.