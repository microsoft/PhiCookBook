<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:33:33+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "he"
}
-->
## כיצד להשתמש ברכיבי chat-completion מרישום המערכת של Azure ML לכוונון מדויק של מודל

בדוגמה זו נבצע כוונון מדויק למודל Phi-3-mini-4k-instruct להשלמת שיחה בין שני אנשים באמצעות מערך הנתונים ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35.he.png)

הדוגמה תראה כיצד לבצע כוונון מדויק באמצעות Azure ML SDK ו-Python, ולאחר מכן לפרוס את המודל המכוונן לנקודת קצה מקוונת להסקת מסקנות בזמן אמת.

### נתוני אימון

נשתמש במערך הנתונים ultrachat_200k. זהו גרסה מסוננת מאוד של מערך הנתונים UltraChat, ששימשה לאימון Zephyr-7B-β, מודל שיחה מתקדם בגודל 7 מיליארד פרמטרים.

### מודל

נשתמש במודל Phi-3-mini-4k-instruct כדי להראות כיצד משתמש יכול לכוונן מודל למשימת השלמת שיחה. אם פתחתם פנקס זה מתוך כרטיס מודל ספציפי, זכרו להחליף את שם המודל הספציפי.

### משימות

- לבחור מודל לכוונון מדויק.
- לבחור ולחקור את נתוני האימון.
- להגדיר את משימת הכוונון המדויק.
- להריץ את משימת הכוונון המדויק.
- לסקור מדדי אימון והערכה.
- לרשום את המודל המכוונן.
- לפרוס את המודל המכוונן להסקת מסקנות בזמן אמת.
- לנקות משאבים.

## 1. הגדרת דרישות מוקדמות

- התקנת תלותיות
- התחברות ל-AzureML Workspace. למידע נוסף ראו set up SDK authentication. החליפו את <WORKSPACE_NAME>, <RESOURCE_GROUP> ו-<SUBSCRIPTION_ID> למטה.
- התחברות לרישום המערכת של azureml
- הגדרת שם ניסוי אופציונלי
- בדיקה או יצירת מחשוב.

> [!NOTE]
> דרישות: צומת GPU יחיד יכול להכיל מספר כרטיסי GPU. לדוגמה, בצומת אחד מסוג Standard_NC24rs_v3 יש 4 כרטיסי NVIDIA V100, בעוד שב-Standard_NC12s_v3 יש 2 כרטיסים כאלה. עיינו בתיעוד למידע זה. מספר כרטיסי ה-GPU לכל צומת מוגדר בפרמטר gpus_per_node למטה. הגדרה נכונה של ערך זה תבטיח שימוש בכל כרטיסי ה-GPU בצומת. ניתן למצוא את SKU המומלצים למחשוב GPU כאן וכאן.

### ספריות Python

התקינו את התלותיות על ידי הרצת התא למטה. זהו שלב חובה בסביבה חדשה.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### אינטראקציה עם Azure ML

1. סקריפט Python זה משמש לאינטראקציה עם שירות Azure Machine Learning (Azure ML). להלן פירוט הפעולות:

    - מייבא מודולים נדרשים מ-packages azure.ai.ml, azure.identity, ו-azure.ai.ml.entities. כמו כן מייבא את מודול time.

    - מנסה לאמת באמצעות DefaultAzureCredential(), שמספק חווית אימות פשוטה להתחלת פיתוח מהירה בענן Azure. אם זה נכשל, עובר ל-InteractiveBrowserCredential(), שמאפשר התחברות אינטראקטיבית בדפדפן.

    - מנסה ליצור מופע MLClient באמצעות from_config, שקורא את ההגדרות מקובץ הקונפיגורציה (config.json). אם זה נכשל, יוצר MLClient באופן ידני עם subscription_id, resource_group_name ו-workspace_name.

    - יוצר מופע MLClient נוסף, הפעם עבור רישום Azure ML בשם "azureml". רישום זה משמש לאחסון מודלים, צינורות כוונון מדויק וסביבות.

    - מגדיר את experiment_name ל-"chat_completion_Phi-3-mini-4k-instruct".

    - מייצר חותמת זמן ייחודית על ידי המרת הזמן הנוכחי (בשניות מאז האפוק, כמספר עשרוני) למספר שלם ואז למחרוזת. חותמת זו משמשת ליצירת שמות וגרסאות ייחודיות.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. בחירת מודל בסיס לכוונון מדויק

1. Phi-3-mini-4k-instruct הוא מודל קל משקל עם 3.8 מיליארד פרמטרים, מתקדם, שנבנה על מערכי הנתונים ששימשו ל-Phi-2. המודל שייך למשפחת Phi-3, וגרסת Mini מגיעה בשתי וריאציות: 4K ו-128K, המייצגות את אורך ההקשר (במונחי טוקנים) שהמודל תומך בו. יש לכוונן את המודל למטרה הספציפית שלנו כדי להשתמש בו. ניתן לעיין במודלים אלה בקטלוג המודלים ב-AzureML Studio, עם סינון לפי משימת chat-completion. בדוגמה זו, אנו משתמשים במודל Phi-3-mini-4k-instruct. אם פתחתם פנקס זה עבור מודל אחר, החליפו את שם המודל והגרסה בהתאם.

    > [!NOTE]
    > מזהה המודל (model id) הוא תכונה של המודל. הוא יועבר כקלט למשימת הכוונון המדויק. מזהה זה זמין גם בשדה Asset ID בדף פרטי המודל בקטלוג המודלים של AzureML Studio.

2. סקריפט Python זה מתקשר עם שירות Azure Machine Learning (Azure ML). להלן פירוט הפעולות:

    - מגדיר את model_name ל-"Phi-3-mini-4k-instruct".

    - משתמש בשיטת get של models מתוך registry_ml_client כדי לקבל את הגרסה העדכנית ביותר של המודל עם השם שצויין מרישום Azure ML. השיטה get נקראת עם שני ארגומנטים: שם המודל ותווית שמציינת שיש לקבל את הגרסה העדכנית ביותר.

    - מדפיס הודעה לקונסול עם שם, גרסה ומזהה המודל שישמש לכוונון המדויק. שיטת format של המחרוזת משמשת להוספת הערכים המתאימים. שם, גרסה ומזהה המודל ניגשים כתכונות של foundation_model.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. יצירת מחשוב לשימוש במשימה

משימת הכוונון המדויק פועלת רק עם מחשוב GPU. גודל המחשוב תלוי בגודל המודל, וברוב המקרים קשה לזהות את המחשוב המתאים למשימה. בתא זה אנו מדריכים את המשתמש לבחור את המחשוב הנכון.

> [!NOTE]
> המחשובים המפורטים למטה פועלים עם התצורה המיטבית ביותר. כל שינוי בתצורה עלול לגרום לשגיאת Cuda Out Of Memory. במקרים כאלה, נסו לשדרג את המחשוב לגודל גדול יותר.

> [!NOTE]
> בעת בחירת compute_cluster_size למטה, ודאו שהמחשוב זמין בקבוצת המשאבים שלכם. אם מחשוב מסוים אינו זמין, ניתן לבקש גישה למשאבי המחשוב.

### בדיקת תמיכה בכוונון מדויק במודל

1. סקריפט Python זה מתקשר עם מודל Azure Machine Learning (Azure ML). להלן פירוט הפעולות:

    - מייבא את מודול ast, המספק פונקציות לעיבוד עצי תחביר מופשט של Python.

    - בודק אם לאובייקט foundation_model (המשקף מודל ב-Azure ML) יש תג בשם finetune_compute_allow_list. תגיות ב-Azure ML הן זוגות מפתח-ערך שניתן ליצור ולהשתמש בהם לסינון ומיון מודלים.

    - אם התג finetune_compute_allow_list קיים, משתמש בפונקציה ast.literal_eval כדי לפרש בבטחה את ערך התג (מחרוזת) לרשימת Python. רשימה זו מוקצית למשתנה computes_allow_list. לאחר מכן מדפיס הודעה שממליצה ליצור מחשוב מתוך הרשימה.

    - אם התג finetune_compute_allow_list אינו קיים, מגדיר את computes_allow_list ל-None ומדפיס הודעה שהתג אינו חלק מתגיות המודל.

    - לסיכום, הסקריפט בודק תג מסוים במטא-דאטה של המודל, ממיר את ערך התג לרשימה אם קיים, ומספק משוב למשתמש בהתאם.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### בדיקת מופע מחשוב

1. סקריפט Python זה מתקשר עם שירות Azure Machine Learning (Azure ML) ומבצע מספר בדיקות על מופע מחשוב. להלן פירוט הפעולות:

    - מנסה לקבל את מופע המחשוב בשם המאוחסן ב-compute_cluster מתוך Azure ML workspace. אם מצב ההקצאה של המופע הוא "failed", מעלה שגיאת ValueError.

    - בודק אם computes_allow_list אינו None. אם כן, ממיר את כל גדלי המחשוב ברשימה לאותיות קטנות ובודק אם גודל המופע הנוכחי נמצא ברשימה. אם לא, מעלה שגיאת ValueError.

    - אם computes_allow_list הוא None, בודק אם גודל המופע נמצא ברשימת גדלים של VM GPU לא נתמכים. אם כן, מעלה שגיאת ValueError.

    - מקבל רשימה של כל גדלי המחשוב הזמינים ב-workspace. עובר על הרשימה, ובודק אם שם הגודל תואם לגודל המופע הנוכחי. אם כן, מקבל את מספר כרטיסי ה-GPU עבור גודל זה ומגדיר gpu_count_found ל-True.

    - אם gpu_count_found הוא True, מדפיס את מספר כרטיסי ה-GPU במופע המחשוב. אם לא, מעלה שגיאת ValueError.

    - לסיכום, הסקריפט מבצע בדיקות שונות על מופע מחשוב ב-Azure ML workspace, כולל בדיקת מצב הקצאה, גודל מול רשימת הרשאות או איסורים, ומספר כרטיסי ה-GPU.

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. בחירת מערך הנתונים לכוונון המדויק של המודל

1. אנו משתמשים במערך הנתונים ultrachat_200k. המערך מחולק לארבעה חלקים, המתאימים לכוונון מפוקח (Supervised fine-tuning - sft). דירוג יצירה (generation ranking - gen). מספר הדוגמאות בכל חלק מוצג להלן:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. התאים הבאים מציגים הכנה בסיסית של הנתונים לכוונון מדויק:

### הצגת שורות נתונים לדוגמה

רוצים שהדוגמה תרוץ מהר, לכן נשמור את הקבצים train_sft ו-test_sft המכילים 5% מהשורות שכבר קוצצו. משמעות הדבר היא שהמודל המכוונן יהיה בעל דיוק נמוך יותר, ולכן לא ישמש לשימוש בעולם האמיתי.  
הסקריפט download-dataset.py משמש להורדת מערך הנתונים ultrachat_200k ולהמרתו לפורמט שניתן לצריכה על ידי רכיב צינור הכוונון המדויק. מאחר שמערך הנתונים גדול, כאן יש רק חלק ממנו.

1. הרצת הסקריפט למטה מורידה רק 5% מהנתונים. ניתן להגדיל זאת על ידי שינוי הפרמטר dataset_split_pc לאחוז הרצוי.

    > [!NOTE]
    > למודלים של שפה מסוימים יש קודי שפה שונים, ולכן שמות העמודות במערך הנתונים צריכים לשקף זאת.

1. דוגמה לאופן שבו הנתונים אמורים להיראות:  
מערך הנתונים של השלמת שיחה מאוחסן בפורמט parquet כאשר כל רשומה משתמשת בסכימה הבאה:

    - זהו מסמך JSON (JavaScript Object Notation), פורמט נפוץ להחלפת נתונים. זה לא קוד להרצה, אלא דרך לאחסן ולהעביר נתונים. להלן פירוט המבנה:

    - "prompt": מפתח זה מחזיק מחרוזת המייצגת משימה או שאלה שהוצגה לעוזר AI.

    - "messages": מפתח זה מחזיק מערך של אובייקטים. כל אובייקט מייצג הודעה בשיחה בין משתמש לעוזר AI. לכל אובייקט הודעה שני מפתחות:

    - "content": מפתח זה מחזיק מחרוזת המייצגת את תוכן ההודעה.
    - "role": מפתח זה מחזיק מחרוזת המייצגת את תפקיד השולח של ההודעה. יכול להיות "user" או "assistant".
    - "prompt_id": מפתח זה מחזיק מחרוזת המייצגת מזהה ייחודי לפרומפט.

1. במסמך JSON הספציפי הזה, מוצגת שיחה שבה משתמש מבקש מהעוזר ליצור גיבור לסיפור דיסטופי. העוזר מגיב, והמשתמש מבקש פרטים נוספים. העוזר מסכים לספק פרטים נוספים. כל השיחה מקושרת למזהה פרומפט ספציפי.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### הורדת נתונים

1. סקריפט Python זה משמש להורדת מערך נתונים באמצעות סקריפט עזר בשם download-dataset.py. להלן פירוט הפעולות:

    - מייבא את מודול os, המספק דרך ניידת להשתמש בפונקציות התלויות במערכת ההפעלה.

    - משתמש בפונקציה os.system להריץ את הסקריפט download-dataset.py ב-shell עם ארגומנטים מסוימים בשורת הפקודה. הארגומנטים מציינים את מערך הנתונים להורדה (HuggingFaceH4/ultrachat_200k), את התיקייה להורדה אליה (ultrachat_200k_dataset), ואת אחוז החלוקה במערך הנתונים (5). הפונקציה os.system מחזירה את סטטוס היציאה של הפקודה; סטטוס זה נשמר במשתנה exit_status.

    - בודק אם exit_status שונה מ-0. במערכות הפעלה דמויות יוניקס, סטטוס יציאה 0 מציין הצלחה, וכל מספר אחר מציין שגיאה. אם exit_status שונה מ-0, מעלה חריגה עם הודעה על שגיאה בהורדת מערך הנתונים.

    - לסיכום, הסקריפט מריץ פקודה להורדת מערך נתונים באמצעות סקריפט עזר, ומעלה חריגה אם הפקודה נכשלה.

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### טעינת נתונים ל-DataFrame

1. סקריפט Python זה טוען קובץ JSON Lines לתוך pandas DataFrame ומציג את חמש השורות הראשונות. להלן פירוט הפעולות:

    - מייבא את ספריית pandas, שהיא ספרייה חזקה לעיבוד וניתוח נתונים.

    - מגדיר את רוחב העמודה המקסימלי באפשרויות התצוגה של pandas ל-0. משמעות הדבר היא שהטקסט המלא של כל עמודה יוצג ללא קיצוץ בעת הדפסת ה-DataFrame. 

    - משתמש בפונקציה pd.read_json כדי לטעון את הקובץ train_sft.jsonl מתיקיית ultrachat_200k_dataset לתוך DataFrame. הפרמטר lines=True מציין שהקובץ בפורמט JSON Lines, שבו כל שורה היא אובייקט JSON נפרד.
- הוא משתמש בשיטת head כדי להציג את 5 השורות הראשונות של ה-DataFrame. אם ל-DataFrame יש פחות מ-5 שורות, הוא יציג את כולן.

- לסיכום, הסקריפט הזה טוען קובץ JSON Lines ל-DataFrame ומציג את 5 השורות הראשונות עם הטקסט המלא של העמודות.

```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. הגשת משימת ה-fine tuning באמצעות המודל והנתונים כקלטים

צור את המשימה שמשתמשת ברכיב pipeline של chat-completion. למידע נוסף על כל הפרמטרים הנתמכים ל-fine tuning.

### הגדרת פרמטרי fine tune

1. פרמטרי ה-fine tune יכולים להתחלק ל-2 קטגוריות - פרמטרי אימון, ופרמטרי אופטימיזציה

1. פרמטרי האימון מגדירים את היבטי האימון כגון -

    - האופטימייזר, ה-scheduler שיש להשתמש בהם
    - המדד לאופטימיזציה של ה-fine tune
    - מספר שלבי האימון וגודל ה-batch וכן הלאה
    - פרמטרי האופטימיזציה מסייעים באופטימיזציה של זיכרון ה-GPU ושימוש יעיל במשאבי המחשוב.

1. להלן כמה מהפרמטרים השייכים לקטגוריה זו. פרמטרי האופטימיזציה משתנים בין מודלים ונארזים יחד עם המודל כדי להתמודד עם השינויים הללו.

    - הפעלת deepspeed ו-LoRA
    - הפעלת אימון במדויק מעורב (mixed precision)
    - הפעלת אימון מרובה-צמתים (multi-node)

> [!NOTE]
> אימון מפוקח עשוי לגרום לאובדן יישור או לשכחה קטסטרופלית. אנו ממליצים לבדוק בעיה זו ולהריץ שלב יישור לאחר ה-fine tune.

### פרמטרי Fine Tuning

1. הסקריפט בפייתון הזה מגדיר פרמטרים ל-fine-tuning של מודל למידת מכונה. הנה פירוט של מה שהוא עושה:

    - הוא מגדיר פרמטרי אימון ברירת מחדל כמו מספר epochs לאימון, גדלי batch לאימון והערכה, שיעור הלמידה וסוג ה-scheduler של שיעור הלמידה.

    - הוא מגדיר פרמטרי אופטימיזציה ברירת מחדל כמו האם להפעיל Layer-wise Relevance Propagation (LoRa) ו-DeepSpeed, ושלב ה-DeepSpeed.

    - הוא משלב את פרמטרי האימון והאופטימיזציה למילון אחד בשם finetune_parameters.

    - הוא בודק אם ל-foundation_model יש פרמטרים ספציפיים למודל כברירת מחדל. אם כן, הוא מדפיס הודעת אזהרה ומעדכן את מילון finetune_parameters עם ברירות המחדל הספציפיות למודל. הפונקציה ast.literal_eval משמשת להמרת ברירות המחדל הספציפיות למודל ממחרוזת למילון פייתון.

    - הוא מדפיס את קבוצת הפרמטרים הסופית של ה-fine-tuning שתשמש להרצה.

    - לסיכום, הסקריפט מגדיר ומציג את הפרמטרים ל-fine-tuning של מודל למידת מכונה, עם אפשרות להחליף את ברירות המחדל בפרמטרים ספציפיים למודל.

```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline לאימון

1. הסקריפט בפייתון הזה מגדיר פונקציה ליצירת שם תצוגה עבור pipeline לאימון למידת מכונה, ואז קורא לפונקציה זו כדי ליצור ולהדפיס את שם התצוגה. הנה פירוט של מה שהוא עושה:

1. מוגדרת הפונקציה get_pipeline_display_name. פונקציה זו יוצרת שם תצוגה בהתבסס על פרמטרים שונים הקשורים ל-pipeline האימון.

1. בתוך הפונקציה, היא מחשבת את גודל ה-batch הכולל על ידי הכפלת גודל ה-batch לכל מכשיר, מספר שלבי הצטברות הגרדיאנט, מספר ה-GPU לכל node, ומספר ה-nodes המשמשים ל-fine-tuning.

1. היא שולפת פרמטרים נוספים כמו סוג ה-scheduler של שיעור הלמידה, האם DeepSpeed מופעל, שלב ה-DeepSpeed, האם Layer-wise Relevance Propagation (LoRa) מופעל, המגבלה על מספר נקודות הבדיקה של המודל לשמירה, ואורך הרצף המקסימלי.

1. היא בונה מחרוזת הכוללת את כל הפרמטרים הללו, מופרדים בקווים מפרידים. אם DeepSpeed או LoRa מופעלים, המחרוזת כוללת "ds" ואחריו שלב ה-DeepSpeed, או "lora" בהתאמה. אם לא, היא כוללת "nods" או "nolora" בהתאמה.

1. הפונקציה מחזירה את המחרוזת הזו, המשמשת כשם התצוגה של pipeline האימון.

1. לאחר שהפונקציה מוגדרת, היא נקראת כדי ליצור את שם התצוגה, ואז מדפיסה אותו.

1. לסיכום, הסקריפט יוצר שם תצוגה ל-pipeline אימון למידת מכונה בהתבסס על פרמטרים שונים, ואז מדפיס את שם התצוגה.

```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### הגדרת ה-Pipeline

הסקריפט בפייתון הזה מגדיר ומגדיר pipeline למידת מכונה באמצעות Azure Machine Learning SDK. הנה פירוט של מה שהוא עושה:

1. מייבא מודולים נחוצים מ-Azure AI ML SDK.

1. מושך רכיב pipeline בשם "chat_completion_pipeline" מהרשימה.

1. מגדיר משימת pipeline באמצעות הדקורטור `@pipeline` והפונקציה `create_pipeline`. שם ה-pipeline מוגדר כ-`pipeline_display_name`.

1. בתוך הפונקציה `create_pipeline`, הוא מאתחל את רכיב ה-pipeline שנמשה עם פרמטרים שונים, כולל נתיב המודל, אשכולות מחשוב לשלבים שונים, חלוקות מערכי נתונים לאימון ובדיקה, מספר ה-GPU לשימוש ב-fine-tuning, ופרמטרים נוספים של fine-tuning.

1. ממפה את הפלט של משימת ה-fine-tuning לפלט של משימת ה-pipeline. זה נעשה כדי לאפשר רישום קל של המודל המותאם, הנדרש לפריסת המודל לנקודת קצה מקוונת או אצווה.

1. יוצר מופע של ה-pipeline על ידי קריאה לפונקציה `create_pipeline`.

1. מגדיר את ההגדרה `force_rerun` של ה-pipeline ל-`True`, כלומר תוצאות מטמון ממשימות קודמות לא ישמשו.

1. מגדיר את ההגדרה `continue_on_step_failure` של ה-pipeline ל-`False`, כלומר ה-pipeline ייפסק אם שלב כלשהו נכשל.

1. לסיכום, הסקריפט מגדיר ומגדיר pipeline למידת מכונה למשימת השלמת שיחה באמצעות Azure Machine Learning SDK.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### הגשת המשימה

1. הסקריפט בפייתון הזה מגיש משימת pipeline למידת מכונה לסביבת עבודה של Azure Machine Learning ואז ממתין לסיום המשימה. הנה פירוט של מה שהוא עושה:

    - קורא לפונקציה create_or_update של האובייקט jobs ב-workspace_ml_client כדי להגיש את משימת ה-pipeline. ה-pipeline להרצה מוגדר על ידי pipeline_object, והניסוי תחתיו מוגדר על ידי experiment_name.

    - לאחר מכן קורא לפונקציה stream של האובייקט jobs ב-workspace_ml_client כדי להמתין לסיום משימת ה-pipeline. המשימה להמתין לה מוגדרת על ידי המאפיין name של האובייקט pipeline_job.

    - לסיכום, הסקריפט מגיש משימת pipeline למידת מכונה לסביבת עבודה של Azure Machine Learning, ואז ממתין לסיום המשימה.

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. רישום המודל המותאם בסביבת העבודה

נרשום את המודל מתוך הפלט של משימת ה-fine tuning. זה יעקוב אחרי הקשר בין המודל המותאם למשימת ה-fine tuning. משימת ה-fine tuning, בתורה, עוקבת אחרי הקשר למודל הבסיס, לנתונים ולקוד האימון.

### רישום מודל ה-ML

1. הסקריפט בפייתון הזה רושם מודל למידת מכונה שאומן ב-pipeline של Azure Machine Learning. הנה פירוט של מה שהוא עושה:

    - מייבא מודולים נחוצים מ-Azure AI ML SDK.

    - בודק אם הפלט trained_model זמין ממשימת ה-pipeline על ידי קריאה לפונקציה get של האובייקט jobs ב-workspace_ml_client וגישה למאפיין outputs שלו.

    - בונה נתיב למודל המאומן על ידי עיצוב מחרוזת עם שם משימת ה-pipeline ושם הפלט ("trained_model").

    - מגדיר שם למודל המותאם על ידי הוספת "-ultrachat-200k" לשם המקורי של המודל והחלפת כל הסלאשים בקווים מפרידים.

    - מתכונן לרישום המודל על ידי יצירת אובייקט Model עם פרמטרים שונים, כולל הנתיב למודל, סוג המודל (MLflow model), שם וגרסת המודל, ותיאור המודל.

    - רושם את המודל על ידי קריאה לפונקציה create_or_update של האובייקט models ב-workspace_ml_client עם אובייקט ה-Model כארגומנט.

    - מדפיס את המודל שנרשם.

1. לסיכום, הסקריפט רושם מודל למידת מכונה שאומן ב-pipeline של Azure Machine Learning.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. פריסת המודל המותאם לנקודת קצה מקוונת

נקודות קצה מקוונות מספקות API REST עמיד שניתן להשתמש בו לשילוב עם יישומים שצריכים להשתמש במודל.

### ניהול נקודת קצה

1. הסקריפט בפייתון הזה יוצר נקודת קצה מקוונת מנוהלת ב-Azure Machine Learning עבור מודל שנרשם. הנה פירוט של מה שהוא עושה:

    - מייבא מודולים נחוצים מ-Azure AI ML SDK.

    - מגדיר שם ייחודי לנקודת הקצה המקוונת על ידי הוספת חותמת זמן למחרוזת "ultrachat-completion-".

    - מתכונן ליצירת נקודת הקצה על ידי יצירת אובייקט ManagedOnlineEndpoint עם פרמטרים שונים, כולל שם הנקודה, תיאור הנקודה, ומצב אימות ("key").

    - יוצר את נקודת הקצה המקוונת על ידי קריאה לפונקציה begin_create_or_update של workspace_ml_client עם אובייקט ManagedOnlineEndpoint כארגומנט. לאחר מכן ממתין לסיום הפעולה על ידי קריאה לפונקציה wait.

1. לסיכום, הסקריפט יוצר נקודת קצה מקוונת מנוהלת ב-Azure Machine Learning עבור מודל שנרשם.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> ניתן למצוא כאן את רשימת ה-SKU הנתמכים לפריסה - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### פריסת מודל ML

1. הסקריפט בפייתון הזה מפרוס מודל למידת מכונה שנרשם לנקודת קצה מקוונת מנוהלת ב-Azure Machine Learning. הנה פירוט של מה שהוא עושה:

    - מייבא את המודול ast, המספק פונקציות לעיבוד עצי תחביר מופשט של פייתון.

    - מגדיר את סוג המופע לפריסה כ-"Standard_NC6s_v3".

    - בודק אם התג inference_compute_allow_list קיים ב-foundation model. אם כן, הוא ממיר את ערך התג ממחרוזת לרשימת פייתון ומקצה אותו ל-inference_computes_allow_list. אם לא, הוא מגדיר את inference_computes_allow_list כ-None.

    - בודק אם סוג המופע שצויין נמצא ברשימת ההרשאות. אם לא, הוא מדפיס הודעה שמבקשת מהמשתמש לבחור סוג מופע מתוך רשימת ההרשאות.

    - מתכונן ליצירת הפריסה על ידי יצירת אובייקט ManagedOnlineDeployment עם פרמטרים שונים, כולל שם הפריסה, שם נקודת הקצה, מזהה המודל, סוג המופע ומספר המופעים, הגדרות בדיקת חיים (liveness probe), והגדרות בקשות.

    - יוצר את הפריסה על ידי קריאה לפונקציה begin_create_or_update של workspace_ml_client עם אובייקט ManagedOnlineDeployment כארגומנט. לאחר מכן ממתין לסיום הפעולה על ידי קריאה לפונקציה wait.

    - מגדיר את התנועה של נקודת הקצה כך שתפנה 100% מהתנועה לפריסת "demo".

    - מעדכן את נקודת הקצה על ידי קריאה לפונקציה begin_create_or_update של workspace_ml_client עם אובייקט נקודת הקצה כארגומנט. לאחר מכן ממתין לסיום העדכון על ידי קריאה לפונקציה result.

1. לסיכום, הסקריפט מפרוס מודל למידת מכונה שנרשם לנקודת קצה מקוונת מנוהלת ב-Azure Machine Learning.

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. בדיקת נקודת הקצה עם נתוני דוגמה

נשלוף נתוני דוגמה ממערך הנתונים לבדיקות ונגיש אותם לנקודת הקצה המקוונת לצורך אינפרנס. לאחר מכן נציג את התוויות המדורגות לצד התוויות האמיתיות.

### קריאת התוצאות

1. הסקריפט בפייתון הזה קורא קובץ JSON Lines ל-DataFrame של pandas, לוקח דגימה אקראית, ומאפס את האינדקס. הנה פירוט של מה שהוא עושה:

    - קורא את הקובץ ./ultrachat_200k_dataset/test_gen.jsonl ל-DataFrame של pandas. הפונקציה read_json משמשת עם הפרמטר lines=True כי הקובץ בפורמט JSON Lines, שבו כל שורה היא אובייקט JSON נפרד.

    - לוקח דגימה אקראית של שורה אחת מה-DataFrame. הפונקציה sample משמשת עם הפרמטר n=1 כדי לציין את מספר השורות האקראיות שיש לבחור.

    - מאפס את האינדקס של ה-DataFrame. הפונקציה reset_index משמשת עם הפרמטר drop=True כדי להסיר את האינדקס המקורי ולהחליפו באינדקס חדש של ערכי מספרים שלמים ברירת מחדל.

    - מציג את 2 השורות הראשונות של ה-DataFrame באמצעות הפונקציה head עם הפרמטר 2. עם זאת, מאחר שה-DataFrame מכיל רק שורה אחת לאחר הדגימה, יוצג רק שורה זו.

1. לסיכום, הסקריפט קורא קובץ JSON Lines ל-DataFrame של pandas, לוקח דגימה אקראית של שורה אחת, מאפס את האינדקס, ומציג את השורה הראשונה.

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### יצירת אובייקט JSON

1. הסקריפט בפייתון הזה יוצר אובייקט JSON עם פרמטרים ספציפיים ושומר אותו לקובץ. הנה פירוט של מה שהוא עושה:

    - מייבא את המודול json, המספק פונקציות לעבודה עם נתוני JSON.

    - יוצר מילון parameters עם מפתחות וערכים המייצגים פרמטרים למודל למידת מכונה. המפתחות הם "temperature", "top_p", "do_sample", ו-"max_new_tokens", והערכים המתאימים הם 0.6, 0.9, True, ו-200 בהתאמה.

    - יוצר מילון נוסף test_json עם שני מפתחות: "input_data" ו-"params". הערך של "input_data" הוא מילון נוסף עם המפתחות "input_string" ו-"parameters". הערך של "input_string" הוא רשימה המכילה את ההודעה הראשונה מתוך ה-DataFrame test_df. הערך של "parameters" הוא המילון parameters שנוצר קודם. הערך של "params" הוא מילון ריק.
- הוא פותח קובץ בשם sample_score.json

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### קריאה לנקודת קצה

1. סקריפט הפייתון הזה קורא לנקודת קצה מקוונת ב-Azure Machine Learning כדי לבצע ניקוד לקובץ JSON. הנה פירוט מה הוא עושה:

    - הוא קורא למתודה invoke של התכונה online_endpoints של האובייקט workspace_ml_client. מתודה זו משמשת לשליחת בקשה לנקודת קצה מקוונת ולקבלת תגובה.

    - הוא מגדיר את שם נקודת הקצה ואת הפריסה באמצעות הפרמטרים endpoint_name ו-deployment_name. במקרה זה, שם נקודת הקצה מאוחסן במשתנה online_endpoint_name ושם הפריסה הוא "demo".

    - הוא מגדיר את הנתיב לקובץ ה-JSON שצריך לנקד באמצעות הפרמטר request_file. במקרה זה, הקובץ הוא ./ultrachat_200k_dataset/sample_score.json.

    - הוא מאחסן את התגובה מנקודת הקצה במשתנה response.

    - הוא מדפיס את התגובה הגולמית.

1. לסיכום, הסקריפט קורא לנקודת קצה מקוונת ב-Azure Machine Learning כדי לנקד קובץ JSON ומדפיס את התגובה.

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. מחיקת נקודת הקצה המקוונת

1. אל תשכחו למחוק את נקודת הקצה המקוונת, אחרת תמשיכו לצבור חיובים עבור המשאבים שהנקודה משתמשת בהם. שורת קוד פייתון זו מוחקת נקודת קצה מקוונת ב-Azure Machine Learning. הנה פירוט מה היא עושה:

    - היא קוראת למתודה begin_delete של התכונה online_endpoints של האובייקט workspace_ml_client. מתודה זו משמשת להתחלת מחיקת נקודת קצה מקוונת.

    - היא מגדירה את שם נקודת הקצה למחיקה באמצעות הפרמטר name. במקרה זה, שם נקודת הקצה מאוחסן במשתנה online_endpoint_name.

    - היא קוראת למתודה wait כדי להמתין לסיום פעולת המחיקה. זוהי פעולה חוסמת, כלומר היא מונעת מהסקריפט להמשיך עד שהמחיקה מסתיימת.

    - לסיכום, שורת קוד זו מתחילה את מחיקת נקודת הקצה המקוונת ב-Azure Machine Learning וממתינה לסיום הפעולה.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.