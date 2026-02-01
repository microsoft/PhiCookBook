[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

این کد یک مدل را به فرمت OpenVINO صادر می‌کند، آن را بارگذاری می‌کند و از آن برای تولید پاسخ به یک پرسش داده شده استفاده می‌کند.

1. **صادر کردن مدل**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - این دستور از ابزار `optimum-cli` برای صادر کردن مدل به فرمت OpenVINO استفاده می‌کند که برای استنتاج بهینه شده است.  
   - مدلی که صادر می‌شود `"microsoft/Phi-3-mini-4k-instruct"` است و برای تولید متن بر اساس زمینه قبلی تنظیم شده است.  
   - وزن‌های مدل به اعداد صحیح ۴ بیتی (`int4`) کوانتیزه شده‌اند که به کاهش حجم مدل و افزایش سرعت پردازش کمک می‌کند.  
   - پارامترهای دیگری مانند `group-size`، `ratio` و `sym` برای تنظیم دقیق‌تر فرآیند کوانتیزه کردن به کار می‌روند.  
   - مدل صادر شده در مسیر `./model/phi3-instruct/int4` ذخیره می‌شود.

2. **وارد کردن کتابخانه‌های لازم**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - این خطوط کلاس‌هایی از کتابخانه `transformers` و ماژول `optimum.intel.openvino` را وارد می‌کنند که برای بارگذاری و استفاده از مدل لازم هستند.

3. **تنظیم مسیر مدل و پیکربندی**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` مشخص می‌کند که فایل‌های مدل در کجا ذخیره شده‌اند.  
   - `ov_config` یک دیکشنری است که مدل OpenVINO را برای اولویت دادن به تأخیر کم، استفاده از یک جریان استنتاج و عدم استفاده از دایرکتوری کش پیکربندی می‌کند.

4. **بارگذاری مدل**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - این خط مدل را از مسیر مشخص شده با استفاده از تنظیمات پیکربندی بارگذاری می‌کند. همچنین در صورت نیاز اجازه اجرای کد از راه دور را می‌دهد.

5. **بارگذاری توکنایزر**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - این خط توکنایزر را بارگذاری می‌کند که مسئول تبدیل متن به توکن‌هایی است که مدل می‌تواند آن‌ها را پردازش کند.

6. **تنظیم آرگومان‌های توکنایزر**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - این دیکشنری مشخص می‌کند که توکن‌های ویژه نباید به خروجی توکنیزه شده اضافه شوند.

7. **تعریف پرسش (Prompt)**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - این رشته یک پرسش مکالمه‌ای را تنظیم می‌کند که در آن کاربر از دستیار هوش مصنوعی می‌خواهد خود را معرفی کند.

8. **توکنیزه کردن پرسش**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - این خط پرسش را به توکن‌هایی تبدیل می‌کند که مدل می‌تواند آن‌ها را پردازش کند و نتیجه را به صورت تنسورهای PyTorch بازمی‌گرداند.

9. **تولید پاسخ**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - این خط از مدل برای تولید پاسخ بر اساس توکن‌های ورودی استفاده می‌کند، با حداکثر ۱۰۲۴ توکن جدید.

10. **رمزگشایی پاسخ**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - این خط توکن‌های تولید شده را به رشته‌ای قابل خواندن برای انسان تبدیل می‌کند، توکن‌های ویژه را نادیده می‌گیرد و اولین نتیجه را برمی‌گرداند.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.