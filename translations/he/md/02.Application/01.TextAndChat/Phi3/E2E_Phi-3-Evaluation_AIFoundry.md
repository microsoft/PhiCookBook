<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:45:36+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "he"
}
-->
# הערכת מודל Phi-3 / Phi-3.5 המותאם אישית ב-Azure AI Foundry עם דגש על עקרונות ה-AI האחראי של מיקרוסופט

דוגמת קצה-לקצה (E2E) זו מבוססת על המדריך "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" מתוך קהילת הטכנולוגיה של מיקרוסופט.

## סקירה כללית

### איך ניתן להעריך את הבטיחות והביצועים של מודל Phi-3 / Phi-3.5 מותאם אישית ב-Azure AI Foundry?

כיוונון מודל עלול לפעמים לגרום לתגובות בלתי צפויות או לא רצויות. כדי להבטיח שהמודל יישאר בטוח ויעיל, חשוב להעריך את הפוטנציאל שלו לייצר תוכן מזיק ואת יכולתו לספק תגובות מדויקות, רלוונטיות וקוהרנטיות. במדריך זה תלמדו כיצד להעריך את הבטיחות והביצועים של מודל Phi-3 / Phi-3.5 מותאם אישית המשולב עם Prompt flow ב-Azure AI Foundry.

להלן תהליך ההערכה של Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.he.png)

*מקור התמונה: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> למידע מפורט יותר ולמשאבים נוספים על Phi-3 / Phi-3.5, אנא בקרו ב-[Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### דרישות מוקדמות

- [Python](https://www.python.org/downloads)
- [מנוי Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- מודל Phi-3 / Phi-3.5 מותאם אישית

### תוכן העניינים

1. [**תרחיש 1: מבוא להערכת Prompt flow ב-Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [מבוא להערכת בטיחות](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [מבוא להערכת ביצועים](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**תרחיש 2: הערכת מודל Phi-3 / Phi-3.5 ב-Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [לפני שמתחילים](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [פריסת Azure OpenAI להערכת מודל Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [הערכת מודל Phi-3 / Phi-3.5 המותאם אישית באמצעות הערכת Prompt flow של Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [ברכות!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **תרחיש 1: מבוא להערכת Prompt flow ב-Azure AI Foundry**

### מבוא להערכת בטיחות

כדי להבטיח שמודל ה-AI שלך אתי ובטוח, חשוב להעריך אותו מול עקרונות ה-AI האחראי של מיקרוסופט. ב-Azure AI Foundry, הערכות בטיחות מאפשרות לך לבדוק את הפגיעות של המודל להתקפות jailbreak ואת הפוטנציאל שלו לייצר תוכן מזיק, בהתאם לעקרונות אלו.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.he.png)

*מקור התמונה: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### עקרונות ה-AI האחראי של מיקרוסופט

לפני שמתחילים בשלבים הטכניים, חשוב להבין את עקרונות ה-AI האחראי של מיקרוסופט, מסגרת אתית שמטרתה להנחות את הפיתוח, הפריסה וההפעלה האחראיים של מערכות AI. עקרונות אלו מנחים את התכנון, הפיתוח והפריסה האחראיים של מערכות AI, ומבטיחים שטכנולוגיות ה-AI נבנות בצורה הוגנת, שקופה ומכלילה. עקרונות אלו מהווים את הבסיס להערכת הבטיחות של מודלי AI.

עקרונות ה-AI האחראי של מיקרוסופט כוללים:

- **הוגנות וכלילה**: מערכות AI צריכות להתייחס לכולם בהוגנות ולהימנע מהבדלים בטיפול בקבוצות דומות של אנשים. לדוגמה, כאשר מערכות AI מספקות הנחיות לטיפול רפואי, בקשות להלוואות או תעסוקה, הן צריכות להמליץ באותה צורה לכל מי שיש לו תסמינים, מצב כלכלי או כישורים מקצועיים דומים.

- **אמינות ובטיחות**: כדי לבנות אמון, חשוב שמערכות AI יפעלו באופן אמין, בטוח ועקבי. מערכות אלו צריכות לפעול כפי שתוכננו במקור, להגיב בבטחה לתנאים בלתי צפויים ולהתנגד למניפולציות מזיקות. האופן שבו הן מתנהגות ומגוון התנאים שהן יכולות להתמודד איתם משקפים את טווח המצבים והנסיבות שהמפתחים צפו במהלך התכנון והבדיקה.

- **שקיפות**: כאשר מערכות AI מסייעות בקבלת החלטות שיש להן השפעה משמעותית על חיי אנשים, חשוב שהאנשים יבינו כיצד התקבלו ההחלטות. לדוגמה, בנק עשוי להשתמש במערכת AI כדי להחליט אם אדם זכאי לאשראי. חברה עשויה להשתמש במערכת AI כדי לקבוע את המועמדים המתאימים ביותר לגיוס.

- **פרטיות ואבטחה**: ככל ש-AI הופך נפוץ יותר, הגנה על פרטיות ואבטחת מידע אישי ועסקי הופכים לחשובים ומורכבים יותר. עם AI, פרטיות ואבטחת מידע דורשים תשומת לב מיוחדת כי גישה לנתונים חיונית למערכות AI כדי לבצע תחזיות והחלטות מדויקות ומבוססות.

- **אחריות**: האנשים שמעצבים ומפרסים מערכות AI חייבים להיות אחראים על אופן פעולת המערכות שלהם. ארגונים צריכים להיעזר בסטנדרטים בתעשייה כדי לפתח נורמות אחריות. נורמות אלו יכולות להבטיח שמערכות AI אינן הסמכות הסופית על כל החלטה שמשפיעה על חיי אנשים, ושהאנשים שומרים על שליטה משמעותית במערכות AI אוטונומיות מאוד.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.he.png)

*מקור התמונה: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> למידע נוסף על עקרונות ה-AI האחראי של מיקרוסופט, בקרו ב-[What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### מדדי בטיחות

במדריך זה תעריך את הבטיחות של מודל Phi-3 המותאם אישית באמצעות מדדי הבטיחות של Azure AI Foundry. מדדים אלו עוזרים לך להעריך את הפוטנציאל של המודל לייצר תוכן מזיק ואת הפגיעות שלו להתקפות jailbreak. מדדי הבטיחות כוללים:

- **תוכן הקשור לפגיעה עצמית**: מעריך האם למודל יש נטייה לייצר תוכן הקשור לפגיעה עצמית.
- **תוכן שנאה ואי-הוגנות**: מעריך האם למודל יש נטייה לייצר תוכן שנאה או לא הוגן.
- **תוכן אלים**: מעריך האם למודל יש נטייה לייצר תוכן אלים.
- **תוכן מיני**: מעריך האם למודל יש נטייה לייצר תוכן מיני לא הולם.

הערכת היבטים אלו מבטיחה שמודל ה-AI לא יפיק תוכן מזיק או פוגעני, בהתאמה לערכי החברה ולתקנות.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.he.png)

### מבוא להערכת ביצועים

כדי להבטיח שמודל ה-AI שלך מתפקד כמצופה, חשוב להעריך את ביצועיו מול מדדי ביצועים. ב-Azure AI Foundry, הערכות ביצועים מאפשרות לך להעריך את יעילות המודל ביצירת תגובות מדויקות, רלוונטיות וקוהרנטיות.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.he.png)

*מקור התמונה: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### מדדי ביצועים

במדריך זה תעריך את ביצועי מודל Phi-3 / Phi-3.5 המותאם אישית באמצעות מדדי הביצועים של Azure AI Foundry. מדדים אלו עוזרים לך להעריך את יעילות המודל ביצירת תגובות מדויקות, רלוונטיות וקוהרנטיות. מדדי הביצועים כוללים:

- **מובססות (Groundedness)**: מעריך עד כמה התשובות שנוצרו תואמות למידע שמקורו בקלט.
- **רלוונטיות**: מעריך את מידת ההתאמה של התגובות שנוצרו לשאלות שניתנו.
- **קוהרנטיות**: מעריך עד כמה הטקסט שנוצר זורם בצורה חלקה, קריא באופן טבעי ודומה לשפה אנושית.
- **שטף (Fluency)**: מעריך את רמת השליטה בשפה של הטקסט שנוצר.
- **דמיון ל-GPT**: משווה את התגובה שנוצרה עם האמת הקרקעית מבחינת דמיון.
- **ציון F1**: מחשב את היחס בין מילים משותפות בין התגובה שנוצרה לנתוני המקור.

מדדים אלו עוזרים לך להעריך את יעילות המודל ביצירת תגובות מדויקות, רלוונטיות וקוהרנטיות.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.he.png)

## **תרחיש 2: הערכת מודל Phi-3 / Phi-3.5 ב-Azure AI Foundry**

### לפני שמתחילים

מדריך זה הוא המשך לפוסטים הקודמים, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ו-"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)". בפוסטים אלו עברנו על תהליך כיוונון מודל Phi-3 / Phi-3.5 ב-Azure AI Foundry ושילובו עם Prompt flow.

במדריך זה תפרוס מודל Azure OpenAI כמעריך ב-Azure AI Foundry ותשתמש בו כדי להעריך את מודל Phi-3 / Phi-3.5 המותאם אישית שלך.

לפני שתתחיל במדריך זה, ודא שיש לך את הדרישות המוקדמות הבאות, כפי שתוארו במדריכים הקודמים:

1. מאגר נתונים מוכן להערכת מודל Phi-3 / Phi-3.5 המותאם אישית.
1. מודל Phi-3 / Phi-3.5 שעבר כיוונון מותאם אישית ופורסם ב-Azure Machine Learning.
1. Prompt flow המשולב עם מודל Phi-3 / Phi-3.5 המותאם אישית שלך ב-Azure AI Foundry.

> [!NOTE]
> תשתמש בקובץ *test_data.jsonl*, שנמצא בתיקיית הנתונים ממאגר **ULTRACHAT_200k** שהורד בפוסטים הקודמים, כמאגר הנתונים להערכת מודל Phi-3 / Phi-3.5 המותאם אישית.

#### שילוב מודל Phi-3 / Phi-3.5 מותאם אישית עם Prompt flow ב-Azure AI Foundry (גישה מבוססת קוד)
> [!NOTE]
> אם עקבת אחרי הגישה של low-code המתוארת ב"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", תוכל לדלג על התרגיל הזה ולהמשיך לתרגיל הבא.
> עם זאת, אם עקבת אחרי הגישה של code-first המתוארת ב"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" כדי לכוונן ולפרוס את הדגם Phi-3 / Phi-3.5 שלך, תהליך החיבור של הדגם שלך ל-Prompt flow שונה במקצת. תלמד את התהליך הזה בתרגיל הזה.
כדי להמשיך, עליך לשלב את מודל ה-Phi-3 / Phi-3.5 המותאם אישית שלך ב-Prompt flow ב-Azure AI Foundry.

#### יצירת Azure AI Foundry Hub

עליך ליצור Hub לפני יצירת הפרויקט. ה-Hub מתפקד כמו Resource Group, ומאפשר לך לארגן ולנהל מספר פרויקטים בתוך Azure AI Foundry.

1. היכנס ל-[Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. בחר **All hubs** מהטאב בצד שמאל.

1. בחר **+ New hub** מתפריט הניווט.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.he.png)

1. בצע את המשימות הבאות:

    - הזן **Hub name**. חייב להיות ערך ייחודי.
    - בחר את **Subscription** של Azure שלך.
    - בחר את **Resource group** לשימוש (צור חדש במידת הצורך).
    - בחר את **Location** שברצונך להשתמש בה.
    - בחר את **Connect Azure AI Services** לשימוש (צור חדש במידת הצורך).
    - בחר ב-**Connect Azure AI Search** את האפשרות **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.he.png)

1. בחר **Next**.

#### יצירת פרויקט ב-Azure AI Foundry

1. ב-Hub שיצרת, בחר **All projects** מהטאב בצד שמאל.

1. בחר **+ New project** מתפריט הניווט.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.he.png)

1. הזן **Project name**. חייב להיות ערך ייחודי.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.he.png)

1. בחר **Create a project**.

#### הוספת חיבור מותאם אישית למודל ה-Phi-3 / Phi-3.5 המותאם

כדי לשלב את מודל ה-Phi-3 / Phi-3.5 המותאם שלך ב-Prompt flow, עליך לשמור את נקודת הקצה (endpoint) והמפתח של המודל בחיבור מותאם אישית. הגדרה זו מבטיחה גישה למודל המותאם שלך ב-Prompt flow.

#### הגדרת api key ו-endpoint uri של מודל ה-Phi-3 / Phi-3.5 המותאם

1. בקר ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. נווט אל סביבת העבודה של Azure Machine learning שיצרת.

1. בחר **Endpoints** מהטאב בצד שמאל.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.he.png)

1. בחר את נקודת הקצה שיצרת.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.he.png)

1. בחר **Consume** מתפריט הניווט.

1. העתק את **REST endpoint** ואת **Primary key** שלך.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.he.png)

#### הוספת החיבור המותאם

1. בקר ב-[Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. נווט אל פרויקט Azure AI Foundry שיצרת.

1. בפרויקט שיצרת, בחר **Settings** מהטאב בצד שמאל.

1. בחר **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.he.png)

1. בחר **Custom keys** מתפריט הניווט.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.he.png)

1. בצע את המשימות הבאות:

    - בחר **+ Add key value pairs**.
    - עבור שם המפתח, הזן **endpoint** והדבק את נקודת הקצה שהעתקת מ-Azure ML Studio בשדה הערך.
    - בחר שוב **+ Add key value pairs**.
    - עבור שם המפתח, הזן **key** והדבק את המפתח שהעתקת מ-Azure ML Studio בשדה הערך.
    - לאחר הוספת המפתחות, סמן **is secret** כדי למנוע חשיפת המפתח.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.he.png)

1. בחר **Add connection**.

#### יצירת Prompt flow

הוספת חיבור מותאם אישית ב-Azure AI Foundry. כעת, ניצור Prompt flow באמצעות השלבים הבאים. לאחר מכן, תחבר את ה-Prompt flow לחיבור המותאם כדי להשתמש במודל המותאם בתוך ה-Prompt flow.

1. נווט אל פרויקט Azure AI Foundry שיצרת.

1. בחר **Prompt flow** מהטאב בצד שמאל.

1. בחר **+ Create** מתפריט הניווט.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.he.png)

1. בחר **Chat flow** מתפריט הניווט.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.he.png)

1. הזן **Folder name** לשימוש.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.he.png)

1. בחר **Create**.

#### הגדרת Prompt flow לשיחה עם מודל ה-Phi-3 / Phi-3.5 המותאם שלך

עליך לשלב את מודל ה-Phi-3 / Phi-3.5 המותאם ב-Prompt flow. עם זאת, ה-Prompt flow הקיים אינו מיועד למטרה זו. לכן, עליך לעצב מחדש את ה-Prompt flow כדי לאפשר את השילוב של המודל המותאם.

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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.he.png)

1. הוסף את הקוד הבא ל-*integrate_with_promptflow.py* כדי להשתמש במודל ה-Phi-3 / Phi-3.5 המותאם ב-Prompt flow.

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
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.he.png)

> [!NOTE]
> למידע מפורט יותר על שימוש ב-Prompt flow ב-Azure AI Foundry, ניתן לעיין ב-[Prompt flow ב-Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. בחר **Chat input**, **Chat output** כדי לאפשר שיחה עם המודל שלך.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.he.png)

1. כעת אתה מוכן לשוחח עם מודל ה-Phi-3 / Phi-3.5 המותאם שלך. בתרגיל הבא תלמד כיצד להפעיל את ה-Prompt flow ולהשתמש בו לשיחה עם המודל המותאם.

> [!NOTE]
>
> ה-flow המחודש אמור להיראות כמו בתמונה למטה:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.he.png)
>

#### הפעלת Prompt flow

1. בחר **Start compute sessions** כדי להפעיל את ה-Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.he.png)

1. בחר **Validate and parse input** כדי לעדכן את הפרמטרים.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.he.png)

1. בחר את **Value** של ה-**connection** לחיבור המותאם שיצרת. לדוגמה, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.he.png)

#### שיחה עם מודל ה-Phi-3 / Phi-3.5 המותאם שלך

1. בחר **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.he.png)

1. הנה דוגמה לתוצאות: כעת תוכל לשוחח עם מודל ה-Phi-3 / Phi-3.5 המותאם שלך. מומלץ לשאול שאלות המבוססות על הנתונים ששימשו לאימון המודל.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.he.png)

### פריסת Azure OpenAI להערכת מודל ה-Phi-3 / Phi-3.5

כדי להעריך את מודל ה-Phi-3 / Phi-3.5 ב-Azure AI Foundry, עליך לפרוס מודל Azure OpenAI. מודל זה ישמש להערכת ביצועי מודל ה-Phi-3 / Phi-3.5.

#### פריסת Azure OpenAI

1. היכנס ל-[Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. נווט אל פרויקט Azure AI Foundry שיצרת.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.he.png)

1. בפרויקט שיצרת, בחר **Deployments** מהטאב בצד שמאל.

1. בחר **+ Deploy model** מתפריט הניווט.

1. בחר **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.he.png)

1. בחר את מודל Azure OpenAI שברצונך להשתמש בו. לדוגמה, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.he.png)

1. בחר **Confirm**.

### הערכת מודל ה-Phi-3 / Phi-3.5 המותאם באמצעות הערכת Prompt flow של Azure AI Foundry

### התחלת הערכה חדשה

1. בקר ב-[Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. נווט אל פרויקט Azure AI Foundry שיצרת.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.he.png)

1. בפרויקט שיצרת, בחר **Evaluation** מהטאב בצד שמאל.

1. בחר **+ New evaluation** מתפריט הניווט.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.he.png)

1. בחר בהערכת **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.he.png)

1. בצע את המשימות הבאות:

    - הזן את שם ההערכה. חייב להיות ערך ייחודי.
    - בחר **Question and answer without context** כסוג המשימה. מכיוון שמאגר הנתונים **UlTRACHAT_200k** בו השתמשנו במדריך זה אינו מכיל הקשר.
    - בחר את ה-Prompt flow שברצונך להעריך.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.he.png)

1. בחר **Next**.

1. בצע את המשימות הבאות:

    - בחר **Add your dataset** להעלאת מאגר הנתונים. לדוגמה, תוכל להעלות את קובץ מאגר הנתונים למבחן, כמו *test_data.json1*, הכלול בהורדת מאגר הנתונים **ULTRACHAT_200k**.
    - בחר את **Dataset column** המתאים למאגר הנתונים שלך. לדוגמה, אם אתה משתמש במאגר הנתונים **ULTRACHAT_200k**, בחר **${data.prompt}** כעמודת הנתונים.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.he.png)

1. בחר **Next**.

1. בצע את המשימות הבאות להגדרת מדדי ביצועים ואיכות:

    - בחר את מדדי הביצועים והאיכות שברצונך להשתמש בהם.
    - בחר את מודל Azure OpenAI שיצרת להערכת המודל. לדוגמה, בחר **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.he.png)

1. בצע את המשימות הבאות להגדרת מדדי סיכון ובטיחות:

    - בחר את מדדי הסיכון והבטיחות שברצונך להשתמש בהם.
    - בחר את הסף לחישוב שיעור הפגמים שברצונך להשתמש בו. לדוגמה, בחר **Medium**.
    - עבור **question**, בחר **Data source** ל-**{$data.prompt}**.
    - עבור **answer**, בחר **Data source** ל-**{$run.outputs.answer}**.
    - עבור **ground_truth**, בחר **Data source** ל-**{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.he.png)

1. בחר **Next**.

1. בחר **Submit** כדי להתחיל את ההערכה.

1. ההערכה תיקח זמן להשלמה. תוכל לעקוב אחר ההתקדמות בטאב **Evaluation**.

### סקירת תוצאות ההערכה
> [!NOTE]
> התוצאות המוצגות למטה נועדו להמחיש את תהליך ההערכה. במדריך זה השתמשנו במודל שעבר כוונון עדין על סט נתונים קטן יחסית, מה שעלול להוביל לתוצאות שאינן מיטביות. התוצאות בפועל עשויות להשתנות משמעותית בהתאם לגודל, איכות ומגוון סט הנתונים שבו משתמשים, וכן בהתאם לקונפיגורציה הספציפית של המודל.
לאחר סיום ההערכה, תוכלו לעיין בתוצאות עבור מדדי הביצועים והבטיחות.

1. מדדי ביצועים ואיכות:

    - הערכת יעילות המודל ביצירת תגובות קוהרנטיות, שוטפות ורלוונטיות.

    ![תוצאת הערכה.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.he.png)

1. מדדי סיכון ובטיחות:

    - ודאו שהתוצרים של המודל בטוחים ותואמים לעקרונות Responsible AI, תוך הימנעות מתוכן מזיק או פוגעני.

    ![תוצאת הערכה.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.he.png)

1. ניתן לגלול למטה כדי לצפות ב**תוצאות מדדים מפורטים**.

    ![תוצאת הערכה.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.he.png)

1. על ידי הערכת מודל ה-Phi-3 / Phi-3.5 המותאם אישית שלך מול מדדי ביצועים ובטיחות, תוכל לוודא שהמודל לא רק יעיל, אלא גם עומד בעקרונות Responsible AI, מה שהופך אותו למוכן לפריסה בעולם האמיתי.

## מזל טוב!

### השלמת את המדריך הזה

הערכת בהצלחה את מודל ה-Phi-3 המותאם אישית המשולב עם Prompt flow ב-Azure AI Foundry. זהו שלב חשוב לוודא שמודלי ה-AI שלך לא רק מבצעים היטב, אלא גם עומדים בעקרונות Responsible AI של מיקרוסופט, כדי לעזור לך לבנות יישומי AI אמינים ואחראיים.

![ארכיטקטורה.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.he.png)

## ניקוי משאבי Azure

נקה את משאבי ה-Azure שלך כדי למנוע חיובים נוספים בחשבונך. עבור לפורטל Azure ומחק את המשאבים הבאים:

- משאב Azure Machine learning.
- נקודת הקצה של מודל Azure Machine learning.
- משאב פרויקט Azure AI Foundry.
- משאב Prompt flow של Azure AI Foundry.

### השלבים הבאים

#### תיעוד

- [הערכת מערכות AI באמצעות לוח הבקרה Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [מדדי הערכה ומעקב ל-AI גנרטיבי](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [תיעוד Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [תיעוד Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### חומרי הדרכה

- [מבוא לגישת Responsible AI של מיקרוסופט](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [מבוא ל-Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### הפניות

- [מהו Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [הכרזה על כלים חדשים ב-Azure AI שיעזרו לך לבנות יישומי AI גנרטיביים בטוחים ואמינים יותר](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [הערכת יישומי AI גנרטיביים](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.