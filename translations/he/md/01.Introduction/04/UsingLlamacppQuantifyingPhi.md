<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:13:57+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "he"
}
-->
# **כימות משפחת Phi באמצעות llama.cpp**

## **מה זה llama.cpp**

llama.cpp היא ספריית תוכנה בקוד פתוח שכתובה בעיקר ב-C++ ומבצעת אינפרנס על מודלים גדולים של שפה (LLMs), כגון Llama. המטרה הראשית שלה היא לספק ביצועים מתקדמים לאינפרנס של LLM במגוון רחב של חומרה עם התקנה מינימלית. בנוסף, קיימות חיבוריות בפייתון לספרייה זו, המציעות API ברמה גבוהה להשלמת טקסט ושרת אינטרנט תואם OpenAI.

המטרה העיקרית של llama.cpp היא לאפשר אינפרנס של LLM עם התקנה מינימלית וביצועים מתקדמים על מגוון חומרות - מקומית ובענן.

- מימוש פשוט ב-C/C++ ללא תלות חיצונית
- סיליקון של Apple נתמך באופן מלא - מותאם באמצעות ARM NEON, Accelerate ו-Metal frameworks
- תמיכה ב-AVX, AVX2 ו-AVX512 בארכיטקטורות x86
- כימות במספר ביטים 1.5, 2, 3, 4, 5, 6 ו-8 לאינפרנס מהיר יותר ושימוש זיכרון מופחת
- קרנלים מותאמים ל-CUDA להרצת LLM על GPUs של NVIDIA (תמיכה ב-GPUs של AMD דרך HIP)
- תמיכה ב-backend של Vulkan ו-SYCL
- אינפרנס היברידי CPU+GPU להאצת חלקית של מודלים גדולים יותר מנפח ה-VRAM הכולל

## **כימות Phi-3.5 באמצעות llama.cpp**

ניתן לכמת את מודל Phi-3.5-Instruct באמצעות llama.cpp, אך Phi-3.5-Vision ו-Phi-3.5-MoE עדיין לא נתמכים. הפורמט שהומר על ידי llama.cpp הוא gguf, שהוא גם הפורמט הנפוץ ביותר לכימות.

קיימים מודלים רבים בפורמט GGUF בכמות גדולה ב-Hugging Face. AI Foundry, Ollama ו-LlamaEdge מסתמכים על llama.cpp, ולכן מודלים בפורמט GGUF משמשים לעיתים קרובות.

### **מה זה GGUF**

GGUF הוא פורמט בינארי המותאם לטעינה ושמירה מהירה של מודלים, מה שהופך אותו ליעיל מאוד למטרות אינפרנס. GGUF מיועד לשימוש עם GGML ומנועים אחרים. GGUF פותח על ידי @ggerganov, שגם הוא המפתח של llama.cpp, מסגרת אינפרנס פופולרית ב-C/C++. מודלים שפותחו תחילה במסגרת כמו PyTorch יכולים להיות מומרות לפורמט GGUF לשימוש עם אותם מנועים.

### **ONNX לעומת GGUF**

ONNX הוא פורמט מסורתי ללמידת מכונה ולמידה עמוקה, הנתמך היטב במסגרת AI שונות ויש לו תרחישי שימוש טובים במכשירי קצה. לגבי GGUF, הוא מבוסס על llama.cpp וניתן לומר שהוא נוצר בעידן ה-GenAI. לשניהם שימושים דומים. אם אתם רוצים ביצועים טובים יותר בחומרה משובצת ושכבות אפליקציה, ONNX עשוי להיות הבחירה שלכם. אם אתם משתמשים במסגרת נגזרת וטכנולוגיה של llama.cpp, אז GGUF עשוי להיות מתאים יותר.

### **כימות Phi-3.5-Instruct באמצעות llama.cpp**

**1. קונפיגורציית סביבה**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. כימות**

המרת Phi-3.5-Instruct ל-FP16 GGUF באמצעות llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

כימות Phi-3.5 ל-INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. בדיקות**

התקנת llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***הערה*** 

אם אתם משתמשים ב-Apple Silicon, התקינו את llama-cpp-python כך


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

בדיקות 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **משאבים**

1. למידע נוסף על llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. למידע נוסף על onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. למידע נוסף על GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור הסמכות. עבור מידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.