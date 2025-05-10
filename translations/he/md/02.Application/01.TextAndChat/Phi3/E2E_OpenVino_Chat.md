<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:57:20+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "he"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

הקוד הזה מייצא מודל לפורמט OpenVINO, טוען אותו ומשתמש בו כדי ליצור תגובה להנחיה נתונה.

1. **ייצוא המודל**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - הפקודה הזו משתמשת ב-`optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **ייבוא הספריות הדרושות**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - השורות האלו מייבאות מחלקות מ-`transformers` library and the `optimum.intel.openvino`, שנדרשות לטעינה ושימוש במודל.

3. **הגדרת תיקיית המודל והקונפיגורציה**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` הוא מילון שמגדיר את מודל ה-OpenVINO כך שייתן עדיפות לזמן תגובה נמוך, ישתמש בזרם אינפרנס אחד, ולא ישתמש בתיקיית מטמון.

4. **טעינת המודל**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - השורה הזו טוענת את המודל מהתיקייה שצוינה, תוך שימוש בהגדרות הקונפיגורציה שהוגדרו קודם. היא גם מאפשרת הרצת קוד מרוחק במידת הצורך.

5. **טעינת ה-tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - השורה הזו טוענת את ה-tokenizer, שאחראי על המרת הטקסט לטוקנים שהמודל יכול להבין.

6. **הגדרת פרמטרים ל-tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - המילון הזה מגדיר שלא יתווספו טוקנים מיוחדים לפלט הטוקניזציה.

7. **הגדרת ההנחיה**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - המחרוזת הזו מגדירה שיחה שבה המשתמש מבקש מהעוזר החכם להציג את עצמו.

8. **טוקניזציה של ההנחיה**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - השורה הזו ממירה את ההנחיה לטוקנים שהמודל יכול לעבד, ומחזירה את התוצאה כמטריצות PyTorch.

9. **יצירת תגובה**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - השורה הזו משתמשת במודל כדי ליצור תגובה על בסיס הטוקנים שהוזנו, עם מקסימום של 1024 טוקנים חדשים.

10. **פענוח התגובה**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - השורה הזו ממירה את הטוקנים שנוצרו חזרה למחרוזת קריאה לבן אדם, מדלגת על טוקנים מיוחדים, ומחזירה את התוצאה הראשונה.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפת המקור כמקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו אחראים לכל אי הבנה או פרשנות שגויה הנובעים מהשימוש בתרגום זה.