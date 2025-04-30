<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "99474e9687279d0657412c806856b559",
  "translation_date": "2025-04-03T07:53:05+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_Nvidia_NIM_Vision.md",
  "language_code": "ur"
}
-->
### مثال منظر

فرض کریں کہ آپ کے پاس ایک تصویر (`demo.png`) ہے اور آپ چاہتے ہیں کہ Python کوڈ تیار کریں جو اس تصویر کو پروسیس کرے اور اس کا ایک نیا ورژن محفوظ کرے (`phi-3-vision.jpg`)۔

اوپر دیا گیا کوڈ اس عمل کو خودکار کرتا ہے:

1. ماحول اور ضروری کنفیگریشنز سیٹ کرنا۔
2. ایک پرامپٹ بنانا جو ماڈل کو مطلوبہ Python کوڈ تیار کرنے کی ہدایت دے۔
3. پرامپٹ کو ماڈل کو بھیجنا اور تیار شدہ کوڈ جمع کرنا۔
4. تیار شدہ کوڈ کو نکالنا اور چلانا۔
5. اصل اور پروسیس شدہ تصاویر دکھانا۔

یہ طریقہ AI کی طاقت کو استعمال کرتا ہے تاکہ تصویر پروسیسنگ کے کاموں کو خودکار بنایا جا سکے، جس سے آپ کے اہداف کو حاصل کرنا آسان اور تیز ہو جاتا ہے۔

[نمونہ کوڈ حل](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

آئیے کوڈ کے پورے عمل کو مرحلہ وار سمجھتے ہیں:

1. **ضروری پیکیج انسٹال کریں**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    یہ کمانڈ `langchain_nvidia_ai_endpoints` پیکیج انسٹال کرتی ہے، اور یہ یقینی بناتی ہے کہ یہ تازہ ترین ورژن ہو۔

2. **ضروری ماڈیولز امپورٹ کریں**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    یہ امپورٹس NVIDIA AI اینڈپوائنٹس کے ساتھ تعامل، پاس ورڈز کو محفوظ طریقے سے ہینڈل کرنا، آپریٹنگ سسٹم کے ساتھ تعامل، اور base64 فارمیٹ میں ڈیٹا کو انکوڈ/ڈیکوڈ کرنے کے لیے ضروری ماڈیولز لاتے ہیں۔

3. **API کی کلید سیٹ کریں**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    یہ کوڈ چیک کرتا ہے کہ آیا `NVIDIA_API_KEY` انوائرنمنٹ ویریبل سیٹ ہے۔ اگر نہیں، تو یہ صارف کو محفوظ طریقے سے اپنی API کلید درج کرنے کا اشارہ دیتا ہے۔

4. **ماڈل اور تصویر کے راستے کی وضاحت کریں**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    یہ استعمال کیے جانے والے ماڈل کو سیٹ کرتا ہے، `ChatNVIDIA` کا ایک انسٹینس مخصوص ماڈل کے ساتھ بناتا ہے، اور تصویر فائل کے راستے کی وضاحت کرتا ہے۔

5. **ٹیکسٹ پرامپٹ بنائیں**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    یہ ایک ٹیکسٹ پرامپٹ کو ڈیفائن کرتا ہے جو ماڈل کو تصویر پروسیس کرنے کے لیے Python کوڈ تیار کرنے کی ہدایت دیتا ہے۔

6. **تصویر کو Base64 میں انکوڈ کریں**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    یہ کوڈ تصویر فائل کو پڑھتا ہے، اسے base64 میں انکوڈ کرتا ہے، اور انکوڈ شدہ ڈیٹا کے ساتھ ایک HTML تصویر ٹیگ بناتا ہے۔

7. **ٹیکسٹ اور تصویر کو پرامپٹ میں یکجا کریں**:
    ```python
    prompt = f"{text} {image}"
    ```
    یہ ٹیکسٹ پرامپٹ اور HTML تصویر ٹیگ کو ایک ہی اسٹرنگ میں یکجا کرتا ہے۔

8. **ChatNVIDIA کا استعمال کرتے ہوئے کوڈ تیار کریں**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    یہ کوڈ پرامپٹ کو `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` اسٹرنگ میں بھیجتا ہے۔

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
    یہ نکالا گیا Python کوڈ بطور سب پروسیس چلاتا ہے اور اس کا آؤٹ پٹ حاصل کرتا ہے۔

11. **تصاویر دکھائیں**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    یہ لائنیں `IPython.display` ماڈیول کا استعمال کرتے ہوئے تصاویر دکھاتی ہیں۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔