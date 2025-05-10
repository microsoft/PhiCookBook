<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:57:29+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "ms"
}
-->
### سيناريو المثال

تخيل أن لديك صورة (`demo.png`) وتريد إنشاء كود Python يقوم بمعالجة هذه الصورة وحفظ نسخة جديدة منها (`phi-3-vision.jpg`).

الكود أعلاه يقوم بأتمتة هذه العملية عن طريق:

1. إعداد البيئة والتكوينات اللازمة.
2. إنشاء نص توجيهي يطلب من النموذج توليد كود Python المطلوب.
3. إرسال النص التوجيهي إلى النموذج وجمع الكود المولد.
4. استخراج وتشغيل الكود المولد.
5. عرض الصور الأصلية والمعالجة.

هذا الأسلوب يستفيد من قوة الذكاء الاصطناعي لأتمتة مهام معالجة الصور، مما يجعل العملية أسهل وأسرع لتحقيق أهدافك.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

دعونا نفصل ما يقوم به الكود خطوة بخطوة:

1. **تثبيت الحزمة المطلوبة**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    هذا الأمر يثبت حزمة `langchain_nvidia_ai_endpoints` مع التأكد من أنها أحدث إصدار.

2. **استيراد الوحدات اللازمة**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    هذه الاستيرادات تجلب الوحدات الضرورية للتعامل مع نقاط نهاية NVIDIA AI، وتأمين كلمات المرور، والتفاعل مع نظام التشغيل، وترميز/فك ترميز البيانات بصيغة base64.

3. **إعداد مفتاح API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    هذا الكود يتحقق مما إذا كانت متغير البيئة `NVIDIA_API_KEY` محددًا. إذا لم يكن كذلك، يطلب من المستخدم إدخال مفتاح API بطريقة آمنة.

4. **تحديد النموذج ومسار الصورة**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    هنا يتم تعيين النموذج المستخدم، وإنشاء كائن من `ChatNVIDIA` مع النموذج المحدد، وتحديد مسار ملف الصورة.

5. **إنشاء النص التوجيهي**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    هذا يحدد نصًا توجيهيًا يطلب من النموذج توليد كود Python لمعالجة الصورة.

6. **ترميز الصورة بصيغة Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    هذا الكود يقرأ ملف الصورة، ويرمزها بصيغة base64، وينشئ وسم HTML للصورة مع البيانات المشفرة.

7. **دمج النص والصورة في التوجيه**:
    ```python
    prompt = f"{text} {image}"
    ```  
    هنا يتم دمج النص التوجيهي ووسم الصورة HTML في سلسلة واحدة.

8. **توليد الكود باستخدام ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    هذا الكود يرسل التوجيه إلى `ChatNVIDIA` ويجمع سلسلة الكود الناتج.

9. **استخراج كود Python من المحتوى المولد**:
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    هذا الجزء يستخرج كود Python الفعلي من المحتوى المولد عن طريق إزالة تنسيق الماركداون.

10. **تشغيل الكود المولد**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    هذا يشغل كود Python المستخرج كعملية فرعية ويجمع مخرجاته.

11. **عرض الصور**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    هذه الأسطر تعرض الصور باستخدام وحدة `IPython.display`.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau tafsiran yang timbul daripada penggunaan terjemahan ini.