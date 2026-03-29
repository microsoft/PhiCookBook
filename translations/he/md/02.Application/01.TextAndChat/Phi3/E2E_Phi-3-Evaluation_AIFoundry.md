# הערכת מודל Phi-3 / Phi-3.5 המותאם אישית ב-Microsoft Foundry בהתמקדות בעקרונות הבינה המלאכותית האחראית של מייקרוסופט

דוגמת קצה-לקצה (E2E) זו מבוססת על המדריך "[הערכת מודלים מותאמים אישית של Phi-3 / 3.5 ב-Microsoft Foundry בהתמקדות בבינה מלאכותית אחראית של מייקרוסופט](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" מתוך קהילת הטכנולוגיה של מייקרוסופט.

## סקירה כללית

### איך ניתן להעריך את הבטיחות והביצועים של מודל Phi-3 / Phi-3.5 מותאם אישית ב-Microsoft Foundry?

כיוונון מודל יכול לעיתים להוביל לתגובות לא רצויות או בלתי מכוונות. כדי להבטיח שהמודל יישאר בטוח ויעיל, חשוב להעריך את הפוטנציאל שלו ליצירת תוכן מזיק ואת יכולתו לספק תגובות מדויקות, רלוונטיות והרמוניות. במדריך זה תלמד כיצד להעריך את הבטיחות והביצועים של מודל Phi-3 / Phi-3.5 מותאם אישית המשולב עם Prompt flow ב-Microsoft Foundry.

זוהי תהליך ההערכה של Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/he/architecture.10bec55250f5d6a4.webp)

*מקור התמונה: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> למידע מפורט נוסף ולחקר משאבים נוספים אודות Phi-3 / Phi-3.5, אנא בקרו ב-[Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### דרישות מוקדמות

- [Python](https://www.python.org/downloads)
- [מנוי Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- מודל Phi-3 / Phi-3.5 מותאם אישית

### תוכן העניינים

1. [**תרחיש 1: מבוא להערכת Prompt flow של Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [מבוא להערכת בטיחות](#מבוא-להערכת-בטיחות)
    - [מבוא להערכת ביצועים](#מבוא-להערכת-ביצועים)

1. [**תרחיש 2: הערכת מודל Phi-3 / Phi-3.5 ב-Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [לפני שמתחילים](#לפני-שמתחילים)
    - [פריסה של Azure OpenAI להערכת מודל Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [הערכת מודל Phi-3 / Phi-3.5 המותאם אישית באמצעות הערכת Prompt flow של Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [מזל טוב!](#מזל-טוב)

## **תרחיש 1: מבוא להערכת Prompt flow של Microsoft Foundry**

### מבוא להערכת בטיחות

כדי לוודא שמודל הבינה המלאכותית שלך אתי ובטוח, חשוב להעריך אותו מול עקרונות הבינה המלאכותית האחראית של מייקרוסופט. ב-Microsoft Foundry, הערכות בטיחות מאפשרות לך לבדוק את הפגיעות של המודל שלך לתקיפות jailbreak ואת הפוטנציאל שלו ליצירת תוכן מזיק, שתואם ישירות לעקרונות אלה.

![Safaty evaluation.](../../../../../../translated_images/he/safety-evaluation.083586ec88dfa950.webp)

*מקור התמונה: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### עקרונות הבינה המלאכותית האחראית של מייקרוסופט

לפני תחילת השלבים הטכניים, חיוני להבין את עקרונות הבינה המלאכותית האחראית של מייקרוסופט, מסגרת אתית שנועדה להנחות פיתוח, פריסה ותפעול אחראי של מערכות בינה מלאכותית. עקרונות אלה מכוונים לעיצוב, פיתוח ופריסה אחראיים של מערכות בינה מלאכותית, ומבטיחים שטכנולוגיות הבינה הבנייתיות נבנות באופן הוגן, שקוף וכוללני. עקרונות אלו מהווים בסיס להערכת בטיחות מודלים.

עקרונות הבינה המלאכותית האחראית של מייקרוסופט כוללים:

- **הוגנות והכלה**: מערכות בינה מלאכותית צריכות להתייחס לכל האנשים בהוגנות ולהימנע מהשפעה שונה על קבוצות דומות של אנשים. לדוגמה, כאשר מערכות בינה מלאכותית מספקות המלצות לטיפול רפואי, בקשות להלוואות או העסקה, הן צריכות לתת את אותן ההמלצות לכולם עם תסמינים, נסיבות כלכליות או הכשרות מקצועיות דומות.

- **אמינות ובטיחות**: כדי לבנות אמון, חשוב שמערכת הבינה תפעל באופן אמין, בטוח ועקבי. מערכות אלו צריכות להיות מסוגלות לפעול כפי שתוכננו במקור, להגיב בצורה בטוחה למצבים לא צפויים ולהתנגד למניפולציות מזיקות. האופן שבו הן מתנהגות ומגוון המצבים שהן יכולות להתמודד איתם משקף את טווח המקרים והנסיבות שהמפתחים ציפו להם במהלך העיצוב והבדיקות.

- **שקיפות**: כאשר מערכות בינה מלאכותית תורמות להחלטות שיש להן השפעה משמעותית על חיי אנשים, הכרחי שהאנשים יבינו כיצד התקבלו ההחלטות. לדוגמה, בנק עשוי להשתמש במערכת בינה מלאכותית כדי להחליט האם מישהו הוא זכאי לאשראי. חברה עשויה להשתמש במערכת בינה מלאכותית כדי לקבוע מי המועמדים המוסמכים ביותר להעסקה.

- **פרטיות ואבטחה**: ככל שהבינה המלאכותית הופכת לנפוצה יותר, ההגנה על פרטיות ואבטחת מידע אישי ועסקי הופכת לקריטית ומורכבת. עם בינה מלאכותית, פרטיות ואבטחת מידע מצריכות תשומת לב קפדנית מכיוון שגישה לנתונים חיונית למערכות לבצע תחזיות והחלטות מדויקות ומושכלות על אנשים.

- **אחריות**: האנשים שמעצבים ומפעילים מערכות בינה מלאכותית חייבים לשאת באחריות לאופן פעולתן. ארגונים צריכים לפתח נורמות אחריות בהתבסס על תקנים תעשייתיים. נורמות אלה יכולות להבטיח שמערכות בינה מלאכותית אינן הסמכות הסופית בקבלת כל החלטה שמשפיעה על חיי אנשים. הן גם יכולות להבטיח שיש לאנשים שליטה משמעותית על מערכות בינה מלאכותית אוטונומיות מאוד.

![Fill hub.](../../../../../../translated_images/he/responsibleai2.c07ef430113fad8c.webp)

*מקור התמונה: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> למידע נוסף על עקרונות הבינה המלאכותית האחראית של מייקרוסופט, בקרו ב-[What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### מדדי בטיחות

במדריך זה תעריך את הבטיחות של מודל Phi-3 המותאם אישית באמצעות מדדי הבטיחות של Microsoft Foundry. מדדים אלו מסייעים להעריך את הפוטנציאל של המודל ליצירת תוכן מזיק ואת הפגיעות שלו לתקיפות jailbreak. מדדי הבטיחות כוללים:

- **תוכן הקשור לפגיעה עצמית**: מעריך האם למודל יש נטייה לייצר תוכן הקשור לפגיעה עצמית.
- **תוכן שנאה ואפליה**: מעריך האם למודל יש נטייה לייצר תוכן שנאה או לא הוגן.
- **תוכן אלים**: מעריך האם למודל יש נטייה לייצר תוכן אלים.
- **תוכן מיני**: מעריך האם למודל יש נטייה לייצר תוכן מיני בלתי הולם.

הערכת היבטים אלה מבטיחה שמודל הבינה המלאכותית אינו מייצר תוכן מזיק או פוגעני, וכי הוא עומד בערכי החברה ובתקנות.

![Evaluate based on safety.](../../../../../../translated_images/he/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### מבוא להערכת ביצועים

כדי לוודא שמודל הבינה המלאכותית שלך עובד כפי שציפית, חשוב להעריך את הביצועים שלו מול מדדי ביצועים. ב-Microsoft Foundry, הערכות ביצועים מאפשרות לך לבדוק את יעילות המודל ביצירת תגובות מדויקות, רלוונטיות והרמוניות.

![Safaty evaluation.](../../../../../../translated_images/he/performance-evaluation.48b3e7e01a098740.webp)

*מקור התמונה: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### מדדי ביצועים

במדריך זה תעריך את ביצועי מודל Phi-3 / Phi-3.5 המותאם אישית באמצעות מדדי הביצועים של Microsoft Foundry. מדדים אלו מסייעים להעריך את יעילות המודל ביצירת תגובות מדויקות, רלוונטיות והרמוניות. מדדי הביצועים כוללים:

- **מוצקות (Groundedness)**: הערכת מידת ההתאמה בין התשובות המופקות למידע שמקורו במקור הקלט.
- **רלוונטיות**: הערכת מידת ההתאמה של התגובות שנוצרו לשאלות שנשאלו.
- **הרמוניה**: הערכה כיצד הטקסט שנוצר זורם בצורה חלקה, נקריא באופן טבעי ודומה לשפה אנושית.
- **שפה וזרימה (Fluency)**: הערכה של רמת המיומנות הלשונית של הטקסט שנוצר.
- **דמיון ל-GPT**: השוואת התגובה שנוצרה לתגובה אמתית לצורך הערכת דמיון.
- **ציון F1**: חישוב היחס של מילים משותפות בין התגובה שנוצרה לנתוני המקור.

מדדים אלה מסייעים להעריך את יעילות המודל ביצירת תגובות מדויקות, רלוונטיות והרמוניות.

![Evaluate based on performance.](../../../../../../translated_images/he/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **תרחיש 2: הערכת מודל Phi-3 / Phi-3.5 ב-Microsoft Foundry**

### לפני שמתחילים

מדריך זה הוא המשך לפוסטים קודמים בבלוג, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ו-"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." בפוסטים אלה עברנו את תהליך הכיוונון של מודל Phi-3 / Phi-3.5 ב-Microsoft Foundry ואת שילובו עם Prompt flow.

במדריך זה תפיץ מודל Azure OpenAI כמעריך ב-Microsoft Foundry ותשתמש בו כדי להעריך את מודל Phi-3 / Phi-3.5 המותאם אישית שלך.

לפני תחילת מדריך זה, ודא שיש לך את הדרישות המוקדמות הבאות, כפי שתואר במדריכים הקודמים:

1. מערך נתונים מוכן להערכת מודל Phi-3 / Phi-3.5 המותאם אישית.
1. מודל Phi-3 / Phi-3.5 שכיוונתו הושלמה ופורס ב-Azure Machine Learning.
1. Prompt flow משולב עם מודל Phi-3 / Phi-3.5 המותאם שלך ב-Microsoft Foundry.

> [!NOTE]
> תשתמש בקובץ *test_data.jsonl*, הנמצא בתיקיית ה-data מתוך מערך הנתונים **ULTRACHAT_200k** שהורד בפוסטים הקודמים בבלוג, כמערך הנתונים להערכת מודל Phi-3 / Phi-3.5 המותאם.

#### שילוב מודל Phi-3 / Phi-3.5 מותאם אישית עם Prompt flow ב-Microsoft Foundry (גישה מבוססת קוד ראשון)

> [!NOTE]
> אם עקבת אחר הגישה הנמוכה בקוד שתוארה ב-"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", תוכל לדלג על התרגיל הזה ולהמשיך לתרגיל הבא.
> עם זאת, אם עקבת אחר הגישה מבוססת קוד ראשון שתוארה ב-"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" לכוונן ולפרוס את מודל Phi-3 / Phi-3.5 שלך, תהליך החיבור של המודל ל-Prompt flow שונה במקצת. תלמד תהליך זה בתרגיל זה.

כדי להתקדם, עליך לשלב את מודל Phi-3 / Phi-3.5 המותאם שלך בתוך Prompt flow ב-Microsoft Foundry.

#### יצירת Hub ב-Microsoft Foundry

עליך ליצור Hub לפני יצירת הפרויקט. Hub מתפקד כמו Resource Group, ומאפשר לך לארגן ולנהל מספר פרויקטים בתוך Microsoft Foundry.
1. היכנס ל-[Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. בחר **All hubs** מהכרטיסייה בצד שמאל.

1. בחר **+ New hub** מתפריט הניווט.

    ![Create hub.](../../../../../../translated_images/he/create-hub.5be78fb1e21ffbf1.webp)

1. בצע את המשימות הבאות:

    - הזן **Hub name**. חייב להיות ערך ייחודי.
    - בחר את **Subscription** של Azure שלך.
    - בחר את ה-**Resource group** לשימוש (צור חדש אם יש צורך).
    - בחר את ה-**Location** שברצונך להשתמש בה.
    - בחר את **Connect Azure AI Services** לשימוש (צור חדש אם יש צורך).
    - בחר **Connect Azure AI Search** כדי **דלג על התחברות**.

    ![Fill hub.](../../../../../../translated_images/he/fill-hub.baaa108495c71e34.webp)

1. בחר **Next**.

#### צור פרויקט Microsoft Foundry

1. ב-Hub שיצרת, בחר **All projects** מהכרטיסייה בצד שמאל.

1. בחר **+ New project** מתפריט הניווט.

    ![Select new project.](../../../../../../translated_images/he/select-new-project.cd31c0404088d7a3.webp)

1. הזן **Project name**. חייב להיות ערך ייחודי.

    ![Create project.](../../../../../../translated_images/he/create-project.ca3b71298b90e420.webp)

1. בחר **Create a project**.

#### הוסף חיבור מותאם אישית למודל Phi-3 / Phi-3.5 המעודן

כדי לשלב את מודל ה-Phi-3 / Phi-3.5 המותאם שלך עם Prompt flow, עליך לשמור את נקודת הקצה וה-key של המודל בחיבור מותאם אישית. הגדרה זו מבטיחה גישה למודל ה-Phi-3 / Phi-3.5 המותאם שלך ב-Prompt flow.

#### הגדר את מפתח ה-API ו-URI של נקודת הקצה של מודל Phi-3 / Phi-3.5 המעודן

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. עבור למרחב העבודה של Azure Machine learning שיצרת.

1. בחר **Endpoints** מהכרטיסייה בצד שמאל.

    ![Select endpoints.](../../../../../../translated_images/he/select-endpoints.ee7387ecd68bd18d.webp)

1. בחר את נקודת הקצה שיצרת.

    ![Select endpoints.](../../../../../../translated_images/he/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. בחר **Consume** מתפריט הניווט.

1. העתק את **REST endpoint** ו-**Primary key** שלך.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/he/copy-endpoint-key.0650c3786bd646ab.webp)

#### הוסף את החיבור המותאם אישית

1. בקר ב-[Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. עבור לפרויקט Microsoft Foundry שיצרת.

1. בפרויקט שיצרת, בחר **Settings** מהכרטיסייה בצד שמאל.

1. בחר **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/he/select-new-connection.fa0f35743758a74b.webp)

1. בחר **Custom keys** מתפריט הניווט.

    ![Select custom keys.](../../../../../../translated_images/he/select-custom-keys.5a3c6b25580a9b67.webp)

1. בצע את המשימות הבאות:

    - בחר **+ Add key value pairs**.
    - עבור שם המפתח, הזן **endpoint** והדבק את נקודת הקצה שהעתקת מ-Azure ML Studio בשדה הערך.
    - בחר שוב **+ Add key value pairs**.
    - עבור שם המפתח, הזן **key** והדבק את המפתח שהעתקת מ-Azure ML Studio בשדה הערך.
    - לאחר הוספת המפתחות, בחר **is secret** כדי למנוע חשיפת המפתח.

    ![Add connection.](../../../../../../translated_images/he/add-connection.ac7f5faf8b10b0df.webp)

1. בחר **Add connection**.

#### צור Prompt flow

הוספת חיבור מותאם אישית ב-Microsoft Foundry. כעת, ניצור Prompt flow באמצעות השלבים הבאים. לאחר מכן, תחבר Prompt flow זה לחיבור המותאם אישית כדי להשתמש במודל המותאם ב-Prompt flow.

1. עבור לפרויקט Microsoft Foundry שיצרת.

1. בחר **Prompt flow** מהכרטיסייה בצד שמאל.

1. בחר **+ Create** מתפריט הניווט.

    ![Select Promptflow.](../../../../../../translated_images/he/select-promptflow.18ff2e61ab9173eb.webp)

1. בחר **Chat flow** מתפריט הניווט.

    ![Select chat flow.](../../../../../../translated_images/he/select-flow-type.28375125ec9996d3.webp)

1. הזן **Folder name** לשימוש.

    ![Select chat flow.](../../../../../../translated_images/he/enter-name.02ddf8fb840ad430.webp)

1. בחר **Create**.

#### הגדר את Prompt flow לשיחה עם מודל Phi-3 / Phi-3.5 המותאם שלך

עליך לשלב את מודל ה-Phi-3 / Phi-3.5 המעודן ב-Prompt flow. עם זאת, ה-Prompt flow הקיים אינו מיועד למטרה זו. לכן, עליך לעצב מחדש את ה-Prompt flow כדי לאפשר את השילוב של המודל המותאם.

1. ב-Prompt flow, בצע את המשימות הבאות כדי לבנות מחדש את ה-flow הקיים:

    - בחר **Raw file mode**.
    - מחק את כל הקוד הקיים בקובץ *flow.dag.yml*.
    - הוסף את הקוד הבא ל-*flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/he/select-raw-file-mode.06c1eca581ce4f53.webp)

1. הוסף את הקוד הבא ל-*integrate_with_promptflow.py* כדי להשתמש במודל ה-Phi-3 / Phi-3.5 המותאם ב-Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # הגדרת יומן
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" הוא שם החיבור המותאם אישית, "endpoint", "key" הם המפתחות בחיבור המותאם אישית
        endpoint_url = connection.endpoint
        api_key = connection.key

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
            
            # רשם את תגובת ה-JSON המלאה
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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/he/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> למידע מפורט יותר על שימוש ב-Prompt flow במיקרוסופט Foundry, ניתן לעיין ב-[Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. בחר **Chat input**, **Chat output** כדי לאפשר שיחה עם המודל שלך.

    ![Select Input Output.](../../../../../../translated_images/he/select-input-output.c187fc58f25fbfc3.webp)

1. כעת אתה מוכן לשוחח עם מודל ה-Phi-3 / Phi-3.5 המותאם שלך. בתרגיל הבא תלמד כיצד להתחיל את ה-Prompt flow ולהשתמש בו לשיחה עם המודל המעודן.

> [!NOTE]
>
> ה-flow שנבנה מחדש אמור להיראות כמו התמונה הבאה:
>
> ![Flow example](../../../../../../translated_images/he/graph-example.82fd1bcdd3fc545b.webp)
>

#### הפעל את ה-Prompt flow

1. בחר **Start compute sessions** כדי להתחיל את ה-Prompt flow.

    ![Start compute session.](../../../../../../translated_images/he/start-compute-session.9acd8cbbd2c43df1.webp)

1. בחר **Validate and parse input** כדי לחדש פרמטרים.

    ![Validate input.](../../../../../../translated_images/he/validate-input.c1adb9543c6495be.webp)

1. בחר את **Value** של **connection** לחיבור המותאם אישית שיצרת. לדוגמה, *connection*.

    ![Connection.](../../../../../../translated_images/he/select-connection.1f2b59222bcaafef.webp)

#### שוחח עם מודל ה-Phi-3 / Phi-3.5 המותאם שלך

1. בחר **Chat**.

    ![Select chat.](../../../../../../translated_images/he/select-chat.0406bd9687d0c49d.webp)

1. הנה דוגמה לתוצאות: כעת תוכל לשוחח עם מודל ה-Phi-3 / Phi-3.5 המותאם שלך. מומלץ לשאול שאלות בהתבסס על הנתונים ששימשו לכוונון עדין.

    ![Chat with prompt flow.](../../../../../../translated_images/he/chat-with-promptflow.1cf8cea112359ada.webp)

### פרוס Azure OpenAI כדי להעריך את מודל Phi-3 / Phi-3.5

כדי להעריך את מודל ה-Phi-3 / Phi-3.5 ב-Microsoft Foundry, עליך לפרוס מודל Azure OpenAI. מודל זה ישמש להערכת ביצועי מודל ה-Phi-3 / Phi-3.5.

#### פרוס Azure OpenAI

1. היכנס אל [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. עבור לפרויקט Microsoft Foundry שיצרת.

    ![Select Project.](../../../../../../translated_images/he/select-project-created.5221e0e403e2c9d6.webp)

1. בפרויקט שיצרת, בחר **Deployments** מהכרטיסייה בצד שמאל.

1. בחר **+ Deploy model** מתפריט הניווט.

1. בחר **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/he/deploy-openai-model.95d812346b25834b.webp)

1. בחר את דגם Azure OpenAI שברצונך להשתמש בו. לדוגמה, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/he/select-openai-model.959496d7e311546d.webp)

1. בחר **Confirm**.

### הערכת מודל ה-Phi-3 / Phi-3.5 המעודן באמצעות הערכת Prompt flow של Microsoft Foundry

### התחלת הערכה חדשה

1. בקר ב-[Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. עבור לפרויקט Microsoft Foundry שיצרת.

    ![Select Project.](../../../../../../translated_images/he/select-project-created.5221e0e403e2c9d6.webp)

1. בפרויקט שיצרת, בחר **Evaluation** מהכרטיסייה בצד שמאל.

1. בחר **+ New evaluation** מתפריט הניווט.

    ![Select evaluation.](../../../../../../translated_images/he/select-evaluation.2846ad7aaaca7f4f.webp)

1. בחר הערכת **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/he/promptflow-evaluation.cb9758cc19b4760f.webp)

1. בצע את המשימות הבאות:

    - הזן שם הערכה. חייב להיות ערך ייחודי.
    - בחר **Question and answer without context** כסוג המשימה, משום שמאגר הנתונים **UlTRACHAT_200k** בו השתמשנו במדריך זה לא כולל הקשר.
    - בחר את ה-prompt flow שברצונך להעריך.

    ![Prompt flow evaluation.](../../../../../../translated_images/he/evaluation-setting1.4aa08259ff7a536e.webp)

1. בחר **Next**.

1. בצע את המשימות הבאות:

    - בחר **Add your dataset** כדי להעלות את מאגר הנתונים. לדוגמה, תוכל להעלות את קובץ מאגר הנתונים למבחן, כגון *test_data.json1*, שמצורף בעת הורדת מאגר הנתונים **ULTRACHAT_200k**.
    - בחר את **Dataset column** המתאים התואם את מאגר הנתונים שלך. לדוגמה, אם אתה משתמש במאגר הנתונים **ULTRACHAT_200k**, בחר **${data.prompt}** כעמודת מאגר הנתונים.

    ![Prompt flow evaluation.](../../../../../../translated_images/he/evaluation-setting2.07036831ba58d64e.webp)

1. בחר **Next**.

1. בצע את המשימות הבאות כדי להגדיר את מדדי הביצועים והאיכות:

    - בחר את מדדי הביצועים והאיכות שברצונך להשתמש בהם.
    - בחר את מודל Azure OpenAI שיצרת עבור ההערכה. לדוגמה, בחר **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/he/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. בצע את המשימות הבאות כדי להגדיר את מדדי הסיכון והבטיחות:

    - בחר את מדדי הסיכון והבטיחות שברצונך להשתמש בהם.
    - בחר את הסף לחישוב שיעור הפגמים שברצונך להשתמש בו. לדוגמה, בחר **Medium**.
    - עבור **question**, בחר **Data source** ל-**{$data.prompt}**.
    - עבור **answer**, בחר **Data source** ל-**{$run.outputs.answer}**.
    - עבור **ground_truth**, בחר **Data source** ל-**{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/he/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. בחר **Next**.

1. בחר **Submit** כדי להתחיל את ההערכה.

1. ההערכה תיקח זמן להשלמה. ניתן לעקוב אחרי ההתקדמות בכרטיסייה **Evaluation**.

### סקור את תוצאות ההערכה

> [!NOTE]
> התוצאות המוצגות להלן מיועדות להמחשת תהליך ההערכה. במדריך זה השתמשנו במודל שעבר כוונון עדין על מאגר נתונים קטן יחסית, דבר שעשוי להוביל לתוצאות תת-אופטימליות. תוצאות בפועל עשויות להשתנות משמעותית בהתאם לגודל, איכות ומגוון נתוני המאגר, וכן בהתאם לקונפיגורציה הספציפית של המודל.

כאשר ההערכה תסתיים, תוכל לסקור את התוצאות הן עבור מדדי הביצועים והן עבור מדדי הבטיחות.
1. מדדי ביצועים ואיכות:

    - הערכת היעילות של המודל ביצירת תגובות קוהרנטיות, שוטפות ורלוונטיות.

    ![Evaluation result.](../../../../../../translated_images/he/evaluation-result-gpu.85f48b42dfb74254.webp)

1. מדדי סיכון ובטיחות:

    - ודא שתוצאות המודל בטוחות ובהלימה עם עקרונות ה-AI האחראי, תוך הימנעות מתוכן מזיק או פוגעני.

    ![Evaluation result.](../../../../../../translated_images/he/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. באפשרותך לגלול למטה כדי לצפות ב**תוצאות מדדים מפורטים**.

    ![Evaluation result.](../../../../../../translated_images/he/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. על ידי הערכת מודל הפאי-3 / פאי-3.5 המותאם אישית שלך כנגד מדדי ביצועים ובטיחות, תוכל לאשר שהמודל לא רק יעיל, אלא גם עומד בשיטות ה-AI האחראי, מה שהופך אותו למוכן לפריסת עולם אמיתי.

## מזל טוב!

### סיימת את המדריך הזה

הערכת בהצלחה את מודל הפאי-3 המותאם אישית המשולב עם Prompt flow ב- Microsoft Foundry. זו היא נקודת חשובה לוודא שמודלי ה-AI שלך לא רק מבצעים היטב, אלא גם עומדים בעקרונות ה-AI האחראי של מייקרוסופט כדי לעזור לך לבנות אפליקציות AI אמינות ומהימנות.

![Architecture.](../../../../../../translated_images/he/architecture.10bec55250f5d6a4.webp)

## ניקוי משאבי Azure

נקה את משאבי Azure שלך כדי להימנע מחיובים נוספים בחשבונך. עבור לפורטל Azure ומחק את המשאבים הבאים:

- משאבי ה-Azure Machine Learning.
- נקודת הקצה של מודל ה-Azure Machine Learning.
- משאבי פרויקט Microsoft Foundry.
- משאבי ה-Prompt flow של Microsoft Foundry.

### צעדים הבאים

#### תיעוד

- [הערכת מערכות AI באמצעות לוח הבקרה של AI האחראי](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [מדדי הערכה ומעקב ל-AI גנרטיבי](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [תיעוד Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [תיעוד Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### תוכן הכשרה

- [הקדמה לגישת ה-AI האחראי של מייקרוסופט](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [הקדמה ל-Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### מקורות

- [מהו AI אחראי?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [הכרזה על כלים חדשים ב-Azure AI שיעזרו לך לבנות אפליקציות AI גנרטיביות בטוחות ומהימנות יותר](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [הערכת אפליקציות AI גנרטיביות](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך כי תרגומים ממוחשבים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכות. עבור מידע קריטי, מומלץ לבצע תרגום מקצועי על ידי מתרגם אנושי. אנו לא נושא באחריות לכל אי-הבנה או פרשנות שגויה הנובעת מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->