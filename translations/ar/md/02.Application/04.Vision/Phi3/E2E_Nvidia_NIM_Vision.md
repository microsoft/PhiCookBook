### سيناريو المثال

تخيل أن لديك صورة (`demo.png`) وترغب في إنشاء كود بايثون يعالج هذه الصورة ويحفظ نسخة جديدة منها (`phi-3-vision.jpg`).

الكود أعلاه يقوم بأتمتة هذه العملية من خلال:

1. إعداد البيئة والتكوينات اللازمة.
2. إنشاء موجه يوجه النموذج لتوليد كود بايثون المطلوب.
3. إرسال الموجه إلى النموذج وجمع الكود الناتج.
4. استخراج وتشغيل الكود الناتج.
5. عرض الصور الأصلية والمعالجة.

يعتمد هذا الأسلوب على قوة الذكاء الاصطناعي لأتمتة مهام معالجة الصور، مما يجعل تحقيق أهدافك أسهل وأسرع.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

دعونا نوضح ما يفعله الكود خطوة بخطوة:

1. **تثبيت الحزمة المطلوبة**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    هذا الأمر يثبت حزمة `langchain_nvidia_ai_endpoints`، مع التأكد من أنها أحدث نسخة.

2. **استيراد الوحدات الضرورية**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    هذه الاستيرادات تجلب الوحدات اللازمة للتفاعل مع نقاط نهاية NVIDIA AI، وإدارة كلمات المرور بأمان، والتعامل مع نظام التشغيل، وترميز/فك ترميز البيانات بصيغة base64.

3. **إعداد مفتاح API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    هذا الكود يتحقق مما إذا كان متغير البيئة `NVIDIA_API_KEY` مضبوطًا. إذا لم يكن كذلك، يطلب من المستخدم إدخال مفتاح API بأمان.

4. **تحديد النموذج ومسار الصورة**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    هذا يحدد النموذج المستخدم، وينشئ نسخة من `ChatNVIDIA` مع النموذج المحدد، ويحدد مسار ملف الصورة.

5. **إنشاء موجه نصي**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    هذا يحدد موجهًا نصيًا يوجه النموذج لتوليد كود بايثون لمعالجة صورة.

6. **ترميز الصورة بصيغة Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    هذا الكود يقرأ ملف الصورة، ويرمزها بصيغة base64، وينشئ وسم HTML للصورة مع البيانات المشفرة.

7. **دمج النص والصورة في الموجه**:
    ```python
    prompt = f"{text} {image}"
    ```  
    هذا يجمع الموجه النصي ووسم الصورة HTML في سلسلة واحدة.

8. **توليد الكود باستخدام ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    هذا الكود يرسل الموجه إلى نموذج `ChatNVIDIA` ويجمع الكود الناتج على شكل أجزاء، ويطبع ويضيف كل جزء إلى سلسلة `code`.

9. **استخراج كود بايثون من المحتوى الناتج**:
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    هذا يستخرج كود بايثون الفعلي من المحتوى الناتج عن طريق إزالة تنسيق الماركداون.

10. **تشغيل الكود الناتج**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    هذا يشغل كود بايثون المستخرج كعملية فرعية ويجمع مخرجاته.

11. **عرض الصور**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    هذه الأسطر تعرض الصور باستخدام وحدة `IPython.display`.

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.