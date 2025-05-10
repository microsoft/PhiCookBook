<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T04:26:44+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "he"
}
-->
# מעבדה. אופטימיזציה של מודלים מבוססי AI להרצה במכשיר

## הקדמה

> [!IMPORTANT]  
> מעבדה זו דורשת **כרטיס מסך Nvidia A10 או A100** עם דרייברים מותקנים וכלי CUDA (גרסה 12 ומעלה).

> [!NOTE]  
> זוהי מעבדה של **35 דקות** שתעניק לכם היכרות מעשית עם מושגי הליבה באופטימיזציה של מודלים להרצה במכשיר באמצעות OLIVE.

## מטרות הלמידה

בסיום המעבדה תוכלו להשתמש ב-OLIVE כדי:

- לבצע כימות (Quantize) למודל AI באמצעות שיטת הכימות AWQ.  
- לכוונן דק (Fine-tune) מודל AI למשימה ספציפית.  
- ליצור מתאמי LoRA (מודל מכוונן) להרצה יעילה במכשיר באמצעות ONNX Runtime.

### מהו Olive

Olive (*O*NNX *live*) הוא ערכת כלים לאופטימיזציה של מודלים עם CLI נלווה, שמאפשרת לשלוח מודלים להרצה ב-ONNX runtime +++https://onnxruntime.ai+++ באיכות ובביצועים גבוהים.

![Olive Flow](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.he.png)

הקלט ל-Olive הוא בדרך כלל מודל PyTorch או Hugging Face, והפלט הוא מודל ONNX מותאם שמורץ על מכשיר (יעד פריסה) שמריץ את ONNX runtime. Olive מבצע אופטימיזציה של המודל בהתאם למאיץ AI של יעד הפריסה (NPU, GPU, CPU) שמסופק על ידי ספק חומרה כמו Qualcomm, AMD, Nvidia או Intel.

Olive מפעיל *workflow*, רצף מסודר של משימות אופטימיזציה למודל הנקראות *passes* – למשל דחיסה, לכידת גרף, כימות, אופטימיזציית גרף. לכל pass יש פרמטרים שניתן לכוונן כדי להגיע למטריקות הטובות ביותר, כמו דיוק וזמן תגובה, שמוערכות על ידי מעריך מתאים. Olive משתמש באסטרטגיית חיפוש עם אלגוריתם שמכוונן כל pass בנפרד או קבוצות של passes יחד.

#### יתרונות Olive

- **מקטין תסכול וזמן** של ניסוי וטעייה ידניים עם טכניקות שונות לאופטימיזציית גרף, דחיסה וכימות. הגדירו את דרישות האיכות והביצועים ותנו ל-Olive למצוא את המודל הטוב ביותר עבורכם.  
- **מעל 40 רכיבי אופטימיזציה מובנים** הכוללים טכניקות מתקדמות בכימות, דחיסה, אופטימיזציית גרף וכיוונון עדין.  
- **CLI פשוט לשימוש** למשימות אופטימיזציה נפוצות. למשל: olive quantize, olive auto-opt, olive finetune.  
- אריזת מודלים ופריסה מובנים.  
- תומך ביצירת מודלים עבור **Multi LoRA serving**.  
- בניית workflow באמצעות YAML/JSON לניהול משימות אופטימיזציה ופריסה.  
- אינטגרציה עם **Hugging Face** ו-**Azure AI**.  
- מנגנון **מטמון** מובנה ל**חיסכון בעלויות**.

## הוראות למעבדה

> [!NOTE]  
> ודאו שהקמתם את Azure AI Hub והפרויקט שלכם והגדרתם את חישוב ה-A100 בהתאם למעבדה 1.

### שלב 0: התחברו ל-Azure AI Compute שלכם

התחברו ל-Azure AI compute באמצעות תכונת ה-remote ב-**VS Code**.

1. פתחו את אפליקציית **VS Code** במחשב.  
1. פתחו את **command palette** עם **Shift+Ctrl+P**.  
1. חפשו ב-command palette את **AzureML - remote: Connect to compute instance in New Window**.  
1. עקבו אחרי ההוראות על המסך כדי להתחבר ל-Compute. תידרשו לבחור במנוי Azure, קבוצת משאבים, פרויקט ושם המחשב שהגדרתם במעבדה 1.  
1. לאחר ההתחברות, השם של Azure ML Compute יוצג בפינה השמאלית התחתונה של Visual Code `><Azure ML: Compute Name`

### שלב 1: שכפלו את המאגר

ב-VS Code, פתחו טרמינל חדש עם **Ctrl+J** ושכפלו את המאגר:

בטרמינל יופיע השורת פקודה

```
azureuser@computername:~/cloudfiles/code$ 
```  
שכפול הפתרון

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### שלב 2: פתחו תיקיה ב-VS Code

כדי לפתוח את VS Code בתיקיה המתאימה, הריצו את הפקודה הבאה בטרמינל, שתפתח חלון חדש:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

או לחלופין, פתחו את התיקיה באמצעות **File** > **Open Folder**.

### שלב 3: תלותיות

פתחו טרמינל ב-VS Code ב-Azure AI Compute Instance שלכם (קיצור: **Ctrl+J**) והריצו את הפקודות הבאות להתקנת התלויות:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> ההתקנה תיקח כ-5 דקות.

במעבדה זו תורידו ותעלו מודלים לקטלוג המודלים של Azure AI. כדי לגשת לקטלוג, התחברו ל-Azure באמצעות:

```bash
az login
```

> [!NOTE]  
> בזמן ההתחברות תתבקשו לבחור את המנוי שלכם. ודאו שבחרתם את המנוי שהוקצה למעבדה זו.

### שלב 4: הריצו פקודות Olive

פתחו טרמינל ב-VS Code ב-Azure AI Compute Instance (קיצור: **Ctrl+J**) ודאו שסביבת conda בשם `olive-ai` מופעלת:

```bash
conda activate olive-ai
```

לאחר מכן, הריצו את פקודות Olive הבאות בשורת הפקודה.

1. **בדקו את הנתונים:** בדוגמה זו, תכווננו את מודל Phi-3.5-Mini כך שיתמחה במענה לשאלות הקשורות לטיולים. הקוד מטה מציג את הרשומות הראשונות של מערך הנתונים, שנמצא בפורמט JSON lines:  
   
    ```bash
    head data/data_sample_travel.jsonl
    ```  
1. **כימות המודל:** לפני האימון, תחילה מבצעים כימות עם הפקודה הבאה, שמשתמשת בטכניקה שנקראת Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ מכמת את המשקלים של המודל תוך התחשבות באקטיבציות המופקות בזמן ההסקה. משמעות הדבר היא שתהליך הכימות מתחשב בהתפלגות הנתונים בפועל באקטיבציות, מה שמוביל לשימור טוב יותר של הדיוק לעומת שיטות כימות משקולות מסורתיות.  
   
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```  
   
    תהליך הכימות עם AWQ לוקח **כ-8 דקות** ויקטין את גודל המודל מ~7.5GB ל~2.5GB.  
   
   במעבדה זו אנו מדגימים כיצד להכניס מודלים מ-Hugging Face (לדוגמה: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` פקודת finetune מכווננת את המודל המקוים. כימות המודל *לפני* כיוונון עדין במקום אחרי מביא לדיוק טוב יותר כי תהליך הכיוונון מחזיר חלק מהאובדן שנגרם בכימות.  
   
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```  
   
    כיוונון עדין (עם 100 צעדים) לוקח **כ-6 דקות**.

1. **אופטימיזציה:** לאחר שהמודל אומן, עכשיו מבצעים אופטימיזציה באמצעות `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` של Olive – אך למטרות המעבדה נשתמש ב-CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```  
   
    האופטימיזציה תיקח **כ-5 דקות**.

### שלב 5: בדיקת הסקה מהירה של המודל

כדי לבדוק הסקה מהמודל, צרו קובץ Python בתיקיה בשם **app.py** והדביקו את הקוד הבא:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

הריצו את הקוד באמצעות:

```bash
python app.py
```

### שלב 6: העלאת מודל ל-Azure AI

העלאת המודל למאגר מודלים של Azure AI מאפשרת לשתף את המודל עם חברי צוות פיתוח נוספים ומטפלת גם בניהול גרסאות. כדי להעלות את המודל, הריצו את הפקודה הבאה:

> [!NOTE]  
> עדכנו את `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` ואת שם פרויקט Azure AI, והריצו את הפקודה:

```
az ml workspace show
```

או דרך +++ai.azure.com+++ ובחירת **management center** > **project** > **overview**

עדכנו את `{}` עם שם קבוצת המשאבים ושם פרויקט Azure AI שלכם.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
לאחר מכן תוכלו לראות את המודל שהעליתם ולפרוס אותו בכתובת https://ml.azure.com/model/list

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא אחראים לכל אי הבנה או פרשנות שגויה הנובעת מהשימוש בתרגום זה.