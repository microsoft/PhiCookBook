<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:05:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "he"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

קוד זה מייצא מודל לפורמט OpenVINO, טוען אותו ומשתמש בו כדי ליצור תגובה להנחיה נתונה.

1. **ייצוא המודל**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - הפקודה הזו משתמשת בכלי `optimum-cli` כדי לייצא מודל לפורמט OpenVINO, שמותאם לביצוע יעיל של אינפרנס.  
   - המודל שמיוצא הוא `"microsoft/Phi-3-mini-4k-instruct"`, והוא מוגדר למשימת יצירת טקסט בהתבסס על הקשר קודם.  
   - המשקלים של המודל מקודדים ל־4 ביטים שלמים (`int4`), מה שעוזר להקטין את גודל המודל ולהאיץ את העיבוד.  
   - פרמטרים נוספים כמו `group-size`, `ratio` ו־`sym` משמשים לכוונון מדויק של תהליך הקוונטיזציה.  
   - המודל המיוצא נשמר בתיקייה `./model/phi3-instruct/int4`.

2. **ייבוא ספריות נחוצות**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - שורות אלו מייבאות מחלקות מספריית `transformers` וממודול `optimum.intel.openvino`, הנחוצות לטעינה ושימוש במודל.

3. **הגדרת תיקיית המודל והקונפיגורציה**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` מציין היכן מאוחסנים קבצי המודל.  
   - `ov_config` הוא מילון שמגדיר את מודל OpenVINO כך שייתן עדיפות לזמני השהייה נמוכים, ישתמש בזרם אינפרנס אחד ולא ישתמש בתיקיית מטמון.

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
   - שורה זו טוענת את המודל מהתיקייה שצוינה, תוך שימוש בהגדרות הקונפיגורציה שהוגדרו קודם. היא גם מאפשרת הרצת קוד מרוחק במידת הצורך.

5. **טעינת הטוקנייזר**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - שורה זו טוענת את הטוקנייזר, שאחראי על המרת טקסט לטוקנים שהמודל יכול להבין.

6. **הגדרת פרמטרים לטוקנייזר**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - מילון זה מגדיר שלא יתווספו טוקנים מיוחדים לפלט הטוקניזציה.

7. **הגדרת ההנחיה**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - מחרוזת זו מגדירה הנחיית שיחה שבה המשתמש מבקש מהעוזר האינטליגנטי להציג את עצמו.

8. **טוקניזציה של ההנחיה**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - שורה זו ממירה את ההנחיה לטוקנים שהמודל יכול לעבד, ומחזירה את התוצאה כמטריצות PyTorch.

9. **יצירת תגובה**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - שורה זו משתמשת במודל כדי ליצור תגובה בהתבסס על הטוקנים שהוזנו, עם מקסימום של 1024 טוקנים חדשים.

10. **פענוח התגובה**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - שורה זו ממירה את הטוקנים שנוצרו חזרה למחרוזת קריאה לבני אדם, מדלגת על טוקנים מיוחדים ומחזירה את התוצאה הראשונה.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.