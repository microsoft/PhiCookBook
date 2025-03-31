<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-03-27T12:51:37+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_Nvidia_NIM_Vision.md",
  "language_code": "ar"
}
-->
### مثال سيناريو

تخيل أن لديك صورة (`demo.png`) وترغب في إنشاء كود Python يعالج هذه الصورة ويحفظ نسخة جديدة منها (`phi-3-vision.jpg`).

يقوم الكود أعلاه بأتمتة هذه العملية من خلال:

1. إعداد البيئة والتكوينات اللازمة.
2. إنشاء موجه يوجه النموذج لتوليد كود Python المطلوب.
3. إرسال الموجه للنموذج وجمع الكود المُولد.
4. استخراج وتشغيل الكود المُولد.
5. عرض الصور الأصلية والمُعالجة.

هذا النهج يستفيد من قوة الذكاء الاصطناعي لأتمتة مهام معالجة الصور، مما يجعل تحقيق أهدافك أسهل وأسرع.

[حل الكود النموذجي](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

دعونا نوضح ما يقوم به الكود بالكامل خطوة بخطوة:

1. **تثبيت الحزمة المطلوبة**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    هذا الأمر يثبت حزمة `langchain_nvidia_ai_endpoints`، ويضمن أنها أحدث إصدار.

2. **استيراد الوحدات اللازمة**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    هذه الاستيرادات تجلب الوحدات الضرورية للتفاعل مع نقاط النهاية للذكاء الاصطناعي من NVIDIA، تأمين كلمات المرور، التفاعل مع نظام التشغيل، وترميز/فك ترميز البيانات بتنسيق base64.

3. **إعداد مفتاح API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    يتحقق هذا الكود مما إذا كان متغير البيئة `NVIDIA_API_KEY` مضبوطًا. إذا لم يكن كذلك، فإنه يطلب من المستخدم إدخال مفتاح API بشكل آمن.

4. **تحديد النموذج ومسار الصورة**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    يتم تحديد النموذج المراد استخدامه، وإنشاء مثيل لـ `ChatNVIDIA` بالنموذج المحدد، وتحديد مسار ملف الصورة.

5. **إنشاء موجه نصي**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    يتم هنا تعريف موجه نصي يوجه النموذج لتوليد كود Python لمعالجة الصورة.

6. **ترميز الصورة بتنسيق Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    يقرأ هذا الكود ملف الصورة، يرمزه بتنسيق base64، وينشئ وسم HTML للصورة بالبيانات المُرمزة.

7. **دمج النص والصورة في الموجه**:
    ```python
    prompt = f"{text} {image}"
    ```
    يتم دمج الموجه النصي ووسم الصورة في سلسلة نصية واحدة.

8. **توليد الكود باستخدام ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    يرسل هذا الكود الموجه إلى `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` كسلسلة نصية.

9. **استخراج كود Python من المحتوى المُولد**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    يتم استخراج كود Python الفعلي من المحتوى المُولد عن طريق إزالة تنسيق Markdown.

10. **تشغيل الكود المُولد**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    يقوم هذا بتشغيل كود Python المُستخرج كعملية فرعية ويلتقط مخرجاته.

11. **عرض الصور**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    تعرض هذه الأسطر الصور باستخدام وحدة `IPython.display`.

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. بالنسبة للمعلومات الحساسة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.