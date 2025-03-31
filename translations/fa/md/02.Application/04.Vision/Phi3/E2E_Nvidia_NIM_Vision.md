<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-03-27T12:52:39+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_Nvidia_NIM_Vision.md",
  "language_code": "fa"
}
-->
### سناریوی نمونه

فرض کنید یک تصویر (`demo.png`) دارید و می‌خواهید کدی به زبان پایتون تولید کنید که این تصویر را پردازش کرده و نسخه جدیدی از آن را ذخیره کند (`phi-3-vision.jpg`).

کد بالا این فرآیند را به صورت زیر خودکار می‌کند:

1. تنظیم محیط و پیکربندی‌های لازم.
2. ایجاد یک پیام (prompt) که به مدل دستور می‌دهد کد پایتون مورد نیاز را تولید کند.
3. ارسال پیام به مدل و جمع‌آوری کد تولیدشده.
4. استخراج و اجرای کد تولیدشده.
5. نمایش تصاویر اصلی و پردازش‌شده.

این روش از قدرت هوش مصنوعی برای خودکارسازی وظایف پردازش تصویر استفاده می‌کند و دستیابی به اهداف شما را ساده‌تر و سریع‌تر می‌سازد.

[نمونه کد راه‌حل](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

بیایید مرحله به مرحله بررسی کنیم که کل کد چه کاری انجام می‌دهد:

1. **نصب بسته موردنیاز**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    این دستور بسته `langchain_nvidia_ai_endpoints` را نصب می‌کند و اطمینان حاصل می‌کند که آخرین نسخه آن نصب شده است.

2. **وارد کردن ماژول‌های لازم**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    این واردات، ماژول‌های لازم برای تعامل با نقاط پایانی هوش مصنوعی NVIDIA، مدیریت ایمن رمزها، تعامل با سیستم‌عامل و کدگذاری/رمزگشایی داده‌ها به فرمت base64 را در اختیار می‌گذارد.

3. **تنظیم کلید API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    این کد بررسی می‌کند که آیا متغیر محیطی `NVIDIA_API_KEY` تنظیم شده است یا نه. اگر تنظیم نشده باشد، از کاربر می‌خواهد کلید API خود را به صورت ایمن وارد کند.

4. **تعریف مدل و مسیر تصویر**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    این کد مدل مورد استفاده را تنظیم می‌کند، یک نمونه از `ChatNVIDIA` با مدل مشخص ایجاد می‌کند و مسیر فایل تصویر را تعریف می‌کند.

5. **ایجاد پیام متنی**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    این بخش یک پیام متنی تعریف می‌کند که به مدل دستور می‌دهد کد پایتون برای پردازش تصویر تولید کند.

6. **کدگذاری تصویر به فرمت Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    این کد فایل تصویر را می‌خواند، آن را به فرمت base64 کدگذاری می‌کند و یک تگ HTML تصویر با داده‌های کدگذاری‌شده ایجاد می‌کند.

7. **ترکیب متن و تصویر در پیام**:
    ```python
    prompt = f"{text} {image}"
    ```
    این بخش پیام متنی و تگ HTML تصویر را در یک رشته واحد ترکیب می‌کند.

8. **تولید کد با استفاده از ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    این کد پیام را به `ChatNVIDIA` ارسال می‌کند و کد تولیدشده را در رشته `code` ذخیره می‌کند.

9. **استخراج کد پایتون از محتوای تولیدشده**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    این بخش کد پایتون واقعی را از محتوای تولیدشده استخراج می‌کند و قالب‌بندی markdown را حذف می‌کند.

10. **اجرای کد تولیدشده**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    این کد استخراج‌شده را به عنوان یک فرآیند جانبی اجرا کرده و خروجی آن را ضبط می‌کند.

11. **نمایش تصاویر**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    این خطوط تصاویر را با استفاده از ماژول `IPython.display` نمایش می‌دهند.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.