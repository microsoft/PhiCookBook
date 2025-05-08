<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-07T13:39:03+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "fa"
}
-->
# آزمایشگاه بهینه‌سازی مدل‌های هوش مصنوعی برای استنتاج روی دستگاه

## مقدمه

> [!IMPORTANT]  
> این آزمایشگاه نیازمند **کارت گرافیک Nvidia A10 یا A100** به همراه درایورها و ابزارهای CUDA (نسخه 12 به بالا) نصب شده است.

> [!NOTE]  
> این یک آزمایشگاه **۳۵ دقیقه‌ای** است که به شما مقدمه‌ای عملی درباره مفاهیم اصلی بهینه‌سازی مدل‌ها برای استنتاج روی دستگاه با استفاده از OLIVE ارائه می‌دهد.

## اهداف یادگیری

در پایان این آزمایشگاه، شما قادر خواهید بود با استفاده از OLIVE:

- مدل هوش مصنوعی را با روش کوانتیزاسیون AWQ کمّی‌سازی کنید.  
- مدل هوش مصنوعی را برای یک وظیفه خاص فاین‌تیون کنید.  
- آداپتورهای LoRA (مدل فاین‌تیون شده) را برای استنتاج بهینه روی دستگاه با ONNX Runtime تولید کنید.

### Olive چیست

Olive (*O*NNX *live*) یک مجموعه ابزار بهینه‌سازی مدل است که همراه با CLI ارائه می‌شود و به شما امکان می‌دهد مدل‌ها را برای ONNX runtime +++https://onnxruntime.ai+++ با کیفیت و کارایی بالا آماده کنید.

![Olive Flow](../../../../../translated_images/olive-flow.5daf97340275f8b61397e91430ff02724a2547937b352e7fdfc2f669c56dcd35.fa.png)

ورودی Olive معمولاً یک مدل PyTorch یا Hugging Face است و خروجی آن یک مدل ONNX بهینه‌شده است که روی دستگاه (هدف استقرار) با ONNX runtime اجرا می‌شود. Olive مدل را برای شتاب‌دهنده هوش مصنوعی هدف استقرار (NPU، GPU، CPU) که توسط فروشنده سخت‌افزاری مانند Qualcomm، AMD، Nvidia یا Intel ارائه شده، بهینه می‌کند.

Olive یک *گردش کار* اجرا می‌کند که دنباله‌ای مرتب از وظایف بهینه‌سازی مدل است که *پَس* نامیده می‌شوند — نمونه‌ای از پَس‌ها شامل: فشرده‌سازی مدل، ضبط گراف، کوانتیزاسیون، بهینه‌سازی گراف است. هر پَس دارای مجموعه‌ای از پارامترها است که می‌توان آنها را برای رسیدن به بهترین معیارها مثل دقت و تأخیر تنظیم کرد که توسط ارزیاب مربوطه سنجیده می‌شوند. Olive از یک استراتژی جستجو استفاده می‌کند که الگوریتم جستجویی را به کار می‌گیرد تا هر پَس را یکی‌یکی یا به صورت گروهی به صورت خودکار تنظیم کند.

#### مزایای Olive

- **کاهش زمان و ناامیدی** ناشی از آزمایش‌های دستی و آزمون‌وخطا با تکنیک‌های مختلف بهینه‌سازی گراف، فشرده‌سازی و کوانتیزاسیون. معیارهای کیفیت و عملکرد خود را تعریف کنید و بگذارید Olive بهترین مدل را به صورت خودکار پیدا کند.  
- **بیش از ۴۰ مؤلفه بهینه‌سازی مدل** داخلی که تکنیک‌های پیشرفته در کوانتیزاسیون، فشرده‌سازی، بهینه‌سازی گراف و فاین‌تیون را پوشش می‌دهد.  
- **رابط خط فرمان آسان** برای وظایف معمول بهینه‌سازی مدل؛ مثلاً olive quantize، olive auto-opt، olive finetune.  
- بسته‌بندی و استقرار مدل به صورت داخلی.  
- پشتیبانی از تولید مدل‌ها برای **سرویس‌دهی Multi LoRA**.  
- ساخت گردش‌های کاری با استفاده از YAML/JSON برای هماهنگی وظایف بهینه‌سازی و استقرار مدل.  
- ادغام با **Hugging Face** و **Azure AI**.  
- مکانیزم **کشینگ** داخلی برای **کاهش هزینه‌ها**.

## دستورالعمل‌های آزمایشگاه

> [!NOTE]  
> لطفاً مطمئن شوید Azure AI Hub و پروژه خود را راه‌اندازی کرده و محاسبات A100 خود را مطابق آزمایشگاه ۱ تنظیم کرده‌اید.

### گام ۰: اتصال به محاسبات Azure AI

با استفاده از قابلیت remote در **VS Code** به محاسبات Azure AI متصل شوید.

1. برنامه دسکتاپ **VS Code** را باز کنید:  
2. با کلیدهای **Shift+Ctrl+P** پنل فرمان را باز کنید.  
3. در پنل فرمان عبارت **AzureML - remote: Connect to compute instance in New Window** را جستجو کنید.  
4. دستورالعمل‌های روی صفحه را دنبال کنید تا به محاسبات متصل شوید. این شامل انتخاب اشتراک Azure، گروه منابع، پروژه و نام محاسباتی است که در آزمایشگاه ۱ تنظیم کرده‌اید.  
5. پس از اتصال به نود محاسباتی Azure ML، این اتصال در **پایین سمت چپ Visual Studio Code** نمایش داده می‌شود `><Azure ML: Compute Name`

### گام ۱: کلون کردن مخزن

در VS Code، با **Ctrl+J** ترمینال جدید باز کنید و این مخزن را کلون کنید:

در ترمینال باید پرامپت زیر را ببینید

```
azureuser@computername:~/cloudfiles/code$ 
```  
کلون کردن راه‌حل

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### گام ۲: باز کردن پوشه در VS Code

برای باز کردن VS Code در پوشه مربوطه، دستور زیر را در ترمینال اجرا کنید که یک پنجره جدید باز می‌کند:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

همچنین می‌توانید با انتخاب **File** > **Open Folder** پوشه را باز کنید.

### گام ۳: نصب وابستگی‌ها

در VS Code و در نمونه محاسبات Azure AI خود، پنجره ترمینال باز کنید (کلید میانبر: **Ctrl+J**) و دستورات زیر را برای نصب وابستگی‌ها اجرا کنید:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> نصب همه وابستگی‌ها حدود ۵ دقیقه طول می‌کشد.

در این آزمایشگاه مدل‌ها را از کاتالوگ مدل Azure AI دانلود و آپلود خواهید کرد. برای دسترسی به کاتالوگ مدل، باید وارد Azure شوید با دستور زیر:

```bash
az login
```

> [!NOTE]  
> هنگام ورود، از شما خواسته می‌شود اشتراک خود را انتخاب کنید. مطمئن شوید اشتراک مربوط به این آزمایشگاه را انتخاب کرده‌اید.

### گام ۴: اجرای دستورات Olive

در VS Code و در نمونه محاسبات Azure AI خود، پنجره ترمینال باز کنید (کلید میانبر: **Ctrl+J**) و مطمئن شوید محیط `olive-ai` کاندا فعال است:

```bash
conda activate olive-ai
```

سپس دستورات زیر Olive را در خط فرمان اجرا کنید.

1. **بازبینی داده‌ها:** در این مثال، مدل Phi-3.5-Mini را فاین‌تیون می‌کنید تا در پاسخ به سوالات مرتبط با سفر تخصصی شود. کد زیر چند رکورد اول داده‌ها را که در فرمت JSON lines هستند نشان می‌دهد:

    ```bash
    head data/data_sample_travel.jsonl
    ```

2. **کوانتیزاسیون مدل:** قبل از آموزش مدل، ابتدا با دستور زیر کوانتیزاسیون انجام می‌دهید که از تکنیکی به نام Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ استفاده می‌کند. AWQ وزن‌های مدل را با در نظر گرفتن فعال‌سازی‌های تولید شده در هنگام استنتاج کمّی می‌کند. این یعنی فرآیند کوانتیزاسیون توزیع واقعی داده‌ها در فعال‌سازی‌ها را در نظر می‌گیرد که باعث حفظ بهتر دقت مدل نسبت به روش‌های سنتی کوانتیزاسیون وزن می‌شود.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    کوانتیزاسیون AWQ حدود **۸ دقیقه** طول می‌کشد و **اندازه مدل را از حدود ۷.۵ گیگابایت به حدود ۲.۵ گیگابایت کاهش می‌دهد**.

    در این آزمایشگاه، نشان می‌دهیم چگونه مدل‌ها را از Hugging Face وارد کنید (برای مثال: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` دستور مدل کوانتیزه شده را فاین‌تیون می‌کند. کوانتیزاسیون مدل *قبل* از فاین‌تیون بهتر است چون فرایند فاین‌تیون مقداری از افت دقت ناشی از کوانتیزاسیون را جبران می‌کند.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    فاین‌تیون با ۱۰۰ گام حدود **۶ دقیقه** طول می‌کشد.

3. **بهینه‌سازی:** پس از آموزش مدل، اکنون مدل را با آرگومان‌های `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` در Olive بهینه می‌کنید — اما برای اهداف این آزمایشگاه، از CPU استفاده می‌کنیم.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    بهینه‌سازی حدود **۵ دقیقه** طول می‌کشد.

### گام ۵: تست سریع استنتاج مدل

برای تست استنتاج مدل، یک فایل پایتون به نام **app.py** در پوشه خود ایجاد کنید و کد زیر را کپی و جای‌گذاری کنید:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

کد را با دستور زیر اجرا کنید:

```bash
python app.py
```

### گام ۶: آپلود مدل به Azure AI

آپلود مدل در مخزن مدل Azure AI باعث می‌شود مدل قابل اشتراک با اعضای تیم توسعه شما باشد و همچنین کنترل نسخه مدل را مدیریت می‌کند. برای آپلود مدل دستور زیر را اجرا کنید:

> [!NOTE]  
> مقادیر `{}` مربوط به `resourceGroup` و نام پروژه Azure AI را به‌روزرسانی کنید و دستور زیر را اجرا کنید:

```
az ml workspace show
```

یا از طریق +++ai.azure.com+++ و انتخاب **management center** > **project** > **overview**

مقادیر `{}` را با نام گروه منابع و نام پروژه Azure AI خود جایگزین کنید.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

سپس می‌توانید مدل آپلود شده خود را مشاهده و مدل خود را در https://ml.azure.com/model/list مستقر کنید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.