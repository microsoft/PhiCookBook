<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-07T13:43:33+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "ur"
}
-->
### منظر نامہ کی مثال

تصور کریں کہ آپ کے پاس ایک تصویر (`demo.png`) ہے اور آپ ایسا Python کوڈ بنانا چاہتے ہیں جو اس تصویر کو پروسیس کرے اور اس کی ایک نئی ورژن محفوظ کرے (`phi-3-vision.jpg`)۔

اوپر دیا گیا کوڈ یہ عمل خودکار بناتا ہے:

1. ماحول اور ضروری ترتیبات کا قیام۔
2. ایک پرامپٹ بنانا جو ماڈل کو مطلوبہ Python کوڈ بنانے کی ہدایت دیتا ہے۔
3. پرامپٹ کو ماڈل کو بھیجنا اور تیار شدہ کوڈ حاصل کرنا۔
4. تیار شدہ کوڈ نکالنا اور چلانا۔
5. اصل اور پروسیس کی گئی تصاویر دکھانا۔

یہ طریقہ کار AI کی طاقت کا استعمال کرتے ہوئے تصویر کی پروسیسنگ کے کاموں کو خودکار بناتا ہے، جس سے آپ کے مقاصد حاصل کرنا آسان اور تیز ہو جاتا ہے۔

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

آئیے پورے کوڈ کو قدم بہ قدم سمجھتے ہیں:

1. **ضروری پیکیج انسٹال کریں**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    یہ کمانڈ `langchain_nvidia_ai_endpoints` پیکیج انسٹال کرتی ہے، اس بات کو یقینی بناتے ہوئے کہ یہ تازہ ترین ورژن ہو۔

2. **ضروری ماڈیولز درآمد کریں**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    یہ درآمدات NVIDIA AI endpoints کے ساتھ تعامل کے لیے، پاس ورڈز کو محفوظ طریقے سے سنبھالنے، آپریٹنگ سسٹم کے ساتھ تعامل، اور base64 فارمیٹ میں ڈیٹا کو انکوڈ/ڈیکوڈ کرنے کے لیے ضروری ماڈیولز لاتی ہیں۔

3. **API کلید سیٹ کریں**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    یہ کوڈ چیک کرتا ہے کہ آیا `NVIDIA_API_KEY` ماحول متغیر سیٹ ہے یا نہیں۔ اگر نہیں، تو یہ صارف کو محفوظ طریقے سے اپنی API کلید داخل کرنے کا کہتا ہے۔

4. **ماڈل اور تصویر کا راستہ متعین کریں**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    یہ ماڈل کو سیٹ کرتا ہے، مخصوص ماڈل کے ساتھ `ChatNVIDIA` کا ایک انسٹانس بناتا ہے، اور تصویر کی فائل کا راستہ متعین کرتا ہے۔

5. **متنی پرامپٹ بنائیں**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    یہ ایک متنی پرامپٹ کی تعریف کرتا ہے جو ماڈل کو تصویر پروسیسنگ کے لیے Python کوڈ بنانے کی ہدایت دیتا ہے۔

6. **تصویر کو base64 میں انکوڈ کریں**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    یہ کوڈ تصویر کی فائل پڑھتا ہے، اسے base64 میں انکوڈ کرتا ہے، اور انکوڈڈ ڈیٹا کے ساتھ HTML تصویر ٹیگ بناتا ہے۔

7. **متن اور تصویر کو پرامپٹ میں یکجا کریں**:
    ```python
    prompt = f"{text} {image}"
    ```
    یہ متنی پرامپٹ اور HTML تصویر ٹیگ کو ایک واحد سٹرنگ میں جوڑتا ہے۔

8. **ChatNVIDIA کا استعمال کرتے ہوئے کوڈ بنائیں**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    یہ کوڈ پرامپٹ کو `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` سٹرنگ کو بھیجتا ہے۔

9. **تیار شدہ مواد سے Python کوڈ نکالیں**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    یہ تیار شدہ مواد سے اصل Python کوڈ نکالتا ہے اور مارک ڈاؤن فارمیٹنگ کو ہٹا دیتا ہے۔

10. **تیار شدہ کوڈ چلائیں**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    یہ نکالا گیا Python کوڈ subprocess کے طور پر چلاتا ہے اور اس کی آؤٹ پٹ حاصل کرتا ہے۔

11. **تصاویر دکھائیں**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    یہ لائنز `IPython.display` ماڈیول کا استعمال کرتے ہوئے تصاویر دکھاتی ہیں۔

**دستخطی دستبرد**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم یاد رکھیں کہ خودکار تراجم میں غلطیاں یا نقائص ہو سکتے ہیں۔ اصل دستاویز اپنی مادری زبان میں مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔