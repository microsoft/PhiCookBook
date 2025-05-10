<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-05-09T18:39:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "ms"
}
-->
# MLflow

[MLflow](https://mlflow.org/) היא פלטפורמה קוד פתוח שנועדה לנהל את מחזור החיים המלא של למידת מכונה.

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.ms.png)

MLFlow משמשת לניהול מחזור החיים של למידת מכונה, כולל ניסויים, שחזור, פריסה ורישום מרכזי של מודלים. כיום MLflow מציעה ארבעה רכיבים.

- **MLflow Tracking:** תיעוד וחיפוש ניסויים, קוד, תצורת נתונים ותוצאות.
- **MLflow Projects:** אריזת קוד מדעי נתונים בפורמט שמאפשר לשחזר הרצות על כל פלטפורמה.
- **Mlflow Models:** פריסת מודלים של למידת מכונה בסביבות שונות.
- **Model Registry:** אחסון, תיוג וניהול מודלים במאגר מרכזי.

הפלטפורמה כוללת יכולות למעקב אחרי ניסויים, אריזת קוד להרצות שניתן לשחזר, ושיתוף ופריסת מודלים. MLFlow משולבת ב-Databricks ותומכת במגוון ספריות למידת מכונה, מה שהופך אותה לנייטרלית לספריות. ניתן להשתמש בה עם כל ספריית למידת מכונה ובכל שפת תכנות, שכן היא מספקת REST API ו-CLI לנוחות.

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.ms.png)

תכונות מרכזיות של MLFlow כוללות:

- **מעקב ניסויים:** תיעוד והשוואת פרמטרים ותוצאות.
- **ניהול מודלים:** פריסת מודלים לפלטפורמות שירות והסקה שונות.
- **Model Registry:** ניהול שיתופי של מחזור החיים של מודלים ב-MLflow, כולל ניהול גרסאות ותיוגים.
- **Projects:** אריזת קוד ML לשיתוף או שימוש בפרודקשן.

MLFlow תומכת גם בלולאת MLOps, שכוללת הכנת נתונים, רישום וניהול מודלים, אריזת מודלים להרצה, פריסת שירותים ומעקב אחר המודלים. המטרה היא לפשט את המעבר מפרוטוטייפ לזרימת עבודה בפרודקשן, במיוחד בסביבות ענן וקצה.

## תרחיש E2E - בניית עטיפה ושימוש ב-Phi-3 כמודל MLFlow

בדוגמה זו נציג שתי גישות שונות לבניית עטיפה סביב מודל השפה הקטן Phi-3 (SLM), ולאחר מכן להריץ אותו כמודל MLFlow, בין אם מקומית ובין אם בענן, למשל ב-Azure Machine Learning workspace.

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.ms.png)

| פרויקט | תיאור | מיקום |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline היא האפשרות הפשוטה ביותר לבניית עטיפה אם רוצים להשתמש במודל HuggingFace עם הטעם הניסיוני של MLFlow לטרנספורמרים. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | נכון למועד כתיבת שורות אלה, ה-Transformer Pipeline לא תמכה ביצירת עטיפת MLFlow למודלים של HuggingFace בפורמט ONNX, אפילו עם חבילת ה-optimum הניסיונית של Python. במקרים כאלה ניתן לבנות עטיפת Python מותאמת אישית עבור מצב MLFlow. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## פרויקט: Transformer Pipeline

1. תזדקקו לחבילות Python הרלוונטיות מ-MLFlow ו-HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. לאחר מכן, יש לאתחל את ה-transformer pipeline על ידי התייחסות למודל Phi-3 הרצוי במאגר HuggingFace. כפי שניתן לראות מכרטיס המודל של _Phi-3-mini-4k-instruct_, המשימה שלו היא מסוג "Text Generation":

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. כעת ניתן לשמור את ה-transformer pipeline של מודל Phi-3 בפורמט MLFlow ולספק פרטים נוספים כמו נתיב היעד לארטיפקטים, הגדרות קונפיגורציה ספציפיות למודל וסוג API לאינפרנס:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## פרויקט: Custom Python Wrapper

1. כאן נשתמש ב-API generate() של [ONNX Runtime](https://github.com/microsoft/onnxruntime-genai) מבית Microsoft עבור אינפרנס של מודל ONNX וקידוד/פענוח טוקנים. יש לבחור את חבילת _onnxruntime_genai_ המתאימה לסביבת החישוב שלכם, בדוגמה הבאה נבחר CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. המחלקה המותאמת שלנו מממשת שתי שיטות: _load_context()_ לאתחול **מודל ONNX** של Phi-3 Mini 4K Instruct, **פרמטרים של הגנרטור** ו**טוקנייזר**; ו-_predict()_ ליצירת טוקנים פלט עבור הפקודה שניתנה:

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # Retrieving model from the artifacts
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # Defining the model
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # Defining the tokenizer
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # Retrieving prompt from the input
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # Generating the model's response
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

1. כעת ניתן להשתמש בפונקציה _mlflow.pyfunc.log_model()_ כדי ליצור עטיפת Python מותאמת אישית (בפורמט pickle) עבור מודל Phi-3, יחד עם מודל ה-ONNX המקורי ותלויות נדרשות:

    ``` Python
    model_info = mlflow.pyfunc.log_model(
        artifact_path = artifact_path,
        python_model = Phi3Model(),
        artifacts = {
            "phi3-mini-onnx": "cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4",
        },
        input_example = input_example,
        signature = infer_signature(input_example, ["Run"]),
        extra_pip_requirements = ["torch", "onnxruntime_genai", "numpy"],
    )
    ```

## חתימות של מודלי MLFlow שנוצרו

1. בשלב 3 של פרויקט Transformer Pipeline לעיל, הגדרנו את משימת מודל ה-MLFlow ל-“_llm/v1/chat_”. הוראה זו יוצרת עטיפת API למודל, שתואמת ל-OpenAI Chat API כפי שמוצג להלן:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. כתוצאה מכך, ניתן לשלוח את הפקודה שלכם בפורמט הבא:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. לאחר מכן, השתמשו בעיבוד פוסט תואם ל-OpenAI API, למשל _response[0][‘choices’][0][‘message’][‘content’]_, כדי לעצב את הפלט למשהו כזה:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. בשלב 3 של פרויקט Custom Python Wrapper לעיל, אפשרנו לחבילת MLFlow ליצור את חתימת המודל מתוך דוגמת קלט נתונה. החתימה של עטיפת ה-MLFlow שלנו תיראה כך:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. לכן, הפקודה שלנו תצטרך לכלול את מפתח המילון "prompt", בדומה לכך:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. הפלט של המודל יינתן אז בפורמט מחרוזת:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.