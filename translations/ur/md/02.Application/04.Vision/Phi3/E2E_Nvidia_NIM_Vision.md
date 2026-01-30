### مثال کا منظرنامہ

تصور کریں کہ آپ کے پاس ایک تصویر ہے (`demo.png`) اور آپ Python کوڈ بنانا چاہتے ہیں جو اس تصویر کو پروسیس کرے اور اس کی ایک نئی ورژن محفوظ کرے (`phi-3-vision.jpg`)۔

اوپر دیا گیا کوڈ اس عمل کو خودکار بناتا ہے:

1. ماحول اور ضروری ترتیبات کو سیٹ کرنا۔
2. ایک پرامپٹ بنانا جو ماڈل کو مطلوبہ Python کوڈ بنانے کی ہدایت دیتا ہے۔
3. پرامپٹ کو ماڈل کو بھیجنا اور تیار شدہ کوڈ جمع کرنا۔
4. تیار شدہ کوڈ نکالنا اور چلانا۔
5. اصل اور پروسیس کی گئی تصاویر دکھانا۔

یہ طریقہ کار AI کی طاقت کا فائدہ اٹھاتے ہوئے تصویر پروسیسنگ کے کاموں کو خودکار بناتا ہے، جس سے آپ کے مقاصد حاصل کرنا آسان اور تیز ہو جاتا ہے۔

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

آئیے پورے کوڈ کو مرحلہ وار سمجھتے ہیں:

1. **ضروری پیکیج انسٹال کریں**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    یہ کمانڈ `langchain_nvidia_ai_endpoints` پیکیج انسٹال کرتی ہے، اور یقینی بناتی ہے کہ یہ تازہ ترین ورژن ہو۔

2. **ضروری ماڈیولز درآمد کریں**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    یہ درآمدات NVIDIA AI endpoints کے ساتھ تعامل، پاس ورڈز کو محفوظ طریقے سے ہینڈل کرنے، آپریٹنگ سسٹم کے ساتھ کام کرنے، اور base64 فارمیٹ میں ڈیٹا انکوڈ/ڈیکوڈ کرنے کے لیے ضروری ماڈیولز لاتی ہیں۔

3. **API کلید سیٹ کریں**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    یہ کوڈ چیک کرتا ہے کہ آیا `NVIDIA_API_KEY` ماحول کی متغیر سیٹ ہے یا نہیں۔ اگر نہیں، تو یہ صارف سے محفوظ طریقے سے API کلید داخل کرنے کو کہتا ہے۔

4. **ماڈل اور تصویر کا راستہ متعین کریں**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    یہ ماڈل کو سیٹ کرتا ہے، `ChatNVIDIA` کی ایک مثال بناتا ہے جس میں مخصوص ماڈل استعمال ہوتا ہے، اور تصویر کی فائل کا راستہ متعین کرتا ہے۔

5. **متنی پرامپٹ بنائیں**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    یہ ایک متنی پرامپٹ متعین کرتا ہے جو ماڈل کو تصویر پروسیسنگ کے لیے Python کوڈ بنانے کی ہدایت دیتا ہے۔

6. **تصویر کو base64 میں انکوڈ کریں**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    یہ کوڈ تصویر کی فائل پڑھتا ہے، اسے base64 میں انکوڈ کرتا ہے، اور انکوڈ شدہ ڈیٹا کے ساتھ ایک HTML امیج ٹیگ بناتا ہے۔

7. **متن اور تصویر کو پرامپٹ میں یکجا کریں**:
    ```python
    prompt = f"{text} {image}"
    ```
    یہ متنی پرامپٹ اور HTML امیج ٹیگ کو ایک سٹرنگ میں جوڑتا ہے۔

8. **ChatNVIDIA کے ذریعے کوڈ تیار کریں**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    یہ کوڈ پرامپٹ کو `ChatNVIDIA` ماڈل کو بھیجتا ہے اور تیار شدہ کوڈ کو ٹکڑوں میں جمع کرتا ہے، ہر ٹکڑا پرنٹ اور `code` سٹرنگ میں شامل کرتا ہے۔

9. **تیار شدہ مواد سے Python کوڈ نکالیں**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    یہ مارک ڈاؤن فارمیٹنگ ہٹاکر اصل Python کوڈ نکالتا ہے۔

10. **تیار شدہ کوڈ چلائیں**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    یہ نکالا گیا Python کوڈ ایک subprocess کے طور پر چلاتا ہے اور اس کا آؤٹ پٹ حاصل کرتا ہے۔

11. **تصاویر دکھائیں**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    یہ لائنز `IPython.display` ماڈیول کا استعمال کرتے ہوئے تصاویر دکھاتی ہیں۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔