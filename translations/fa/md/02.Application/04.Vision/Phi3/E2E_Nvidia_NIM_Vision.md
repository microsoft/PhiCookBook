<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-07T13:43:03+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "fa"
}
-->
### سناریوی نمونه

تصور کنید یک تصویر (`demo.png`) دارید و می‌خواهید کدی به زبان Python تولید کنید که این تصویر را پردازش کرده و نسخه جدیدی از آن را ذخیره کند (`phi-3-vision.jpg`).

کد بالا این فرآیند را به‌صورت خودکار انجام می‌دهد با:

1. راه‌اندازی محیط و تنظیمات لازم.
2. ایجاد یک پرسش متنی که مدل را برای تولید کد Python مورد نیاز راهنمایی می‌کند.
3. ارسال پرسش به مدل و دریافت کد تولید شده.
4. استخراج و اجرای کد تولید شده.
5. نمایش تصاویر اصلی و پردازش شده.

این روش از قدرت هوش مصنوعی برای خودکارسازی وظایف پردازش تصویر استفاده می‌کند و رسیدن به اهداف شما را آسان‌تر و سریع‌تر می‌کند.

[نمونه کد حل مسئله](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

بیایید قدم به قدم ببینیم کل کد چه کاری انجام می‌دهد:

1. **نصب بسته مورد نیاز**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    این دستور بسته `langchain_nvidia_ai_endpoints` را نصب می‌کند و اطمینان می‌دهد که آخرین نسخه آن نصب شده است.

2. **وارد کردن ماژول‌های لازم**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    این واردسازی‌ها ماژول‌های لازم برای تعامل با NVIDIA AI endpoints، مدیریت امن رمزعبور، تعامل با سیستم عامل و کدگذاری/کدگشایی داده‌ها به فرمت base64 را فراهم می‌کنند.

3. **تنظیم کلید API**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    این کد بررسی می‌کند که آیا متغیر محیطی `NVIDIA_API_KEY` تنظیم شده است یا خیر. در صورت عدم وجود، از کاربر درخواست می‌کند کلید API خود را به‌صورت امن وارد کند.

4. **تعریف مدل و مسیر تصویر**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    این قسمت مدل مورد استفاده را تعیین می‌کند، یک نمونه از `ChatNVIDIA` با مدل مشخص شده می‌سازد و مسیر فایل تصویر را تعریف می‌کند.

5. **ایجاد پرسش متنی**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    این بخش یک پرسش متنی تعریف می‌کند که مدل را برای تولید کد Python جهت پردازش تصویر راهنمایی می‌کند.

6. **کدگذاری تصویر به base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    این کد فایل تصویر را می‌خواند، آن را به base64 تبدیل می‌کند و یک تگ HTML تصویر با داده‌های کدگذاری شده ایجاد می‌کند.

7. **ترکیب متن و تصویر در پرسش**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    این بخش متن پرسش و تگ تصویر HTML را در یک رشته واحد ترکیب می‌کند.

8. **تولید کد با استفاده از ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    این کد پرسش را به `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` ارسال می‌کند.

9. **استخراج کد Python از محتوای تولید شده**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    این قسمت کد Python واقعی را از محتوای تولید شده با حذف قالب‌بندی markdown استخراج می‌کند.

10. **اجرای کد تولید شده**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    این کد کد استخراج شده Python را به‌صورت یک زیر فرایند اجرا کرده و خروجی آن را ضبط می‌کند.

11. **نمایش تصاویر**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    این خطوط تصاویر را با استفاده از ماژول `IPython.display` نمایش می‌دهند.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.