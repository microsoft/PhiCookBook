<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-03-27T09:22:29+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_OpenVino_Chat.md",
  "language_code": "fa"
}
-->
[نمونه چت OpenVino](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

این کد یک مدل را به فرمت OpenVINO صادر می‌کند، آن را بارگذاری می‌کند و از آن برای تولید پاسخ به یک ورودی مشخص استفاده می‌کند.

1. **صادر کردن مدل**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - این دستور از `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` استفاده می‌کند.

2. **وارد کردن کتابخانه‌های مورد نیاز**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - این خطوط کلاس‌هایی را از ماژول `transformers` library and the `optimum.intel.openvino` وارد می‌کنند که برای بارگذاری و استفاده از مدل ضروری هستند.

3. **تنظیم دایرکتوری مدل و پیکربندی**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` یک دیکشنری است که مدل OpenVINO را برای اولویت دادن به تأخیر کم، استفاده از یک جریان استنتاج و عدم استفاده از دایرکتوری کش تنظیم می‌کند.

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
   - این خط مدل را از دایرکتوری مشخص شده بارگذاری می‌کند، با استفاده از تنظیمات پیکربندی که قبلاً تعریف شده‌اند. همچنین اجازه اجرای کد از راه دور را در صورت نیاز فراهم می‌کند.

5. **بارگذاری توکنایزر**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - این خط توکنایزر را بارگذاری می‌کند که مسئول تبدیل متن به توکن‌هایی است که مدل می‌تواند آن‌ها را درک کند.

6. **تنظیم آرگومان‌های توکنایزر**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - این دیکشنری مشخص می‌کند که توکن‌های ویژه نباید به خروجی توکنایزر اضافه شوند.

7. **تعریف ورودی**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - این رشته یک ورودی مکالمه را تنظیم می‌کند که در آن کاربر از دستیار هوش مصنوعی می‌خواهد خودش را معرفی کند.

8. **توکنایز کردن ورودی**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - این خط ورودی را به توکن‌هایی تبدیل می‌کند که مدل می‌تواند پردازش کند و نتیجه را به صورت تنسورهای PyTorch باز می‌گرداند.

9. **تولید پاسخ**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - این خط از مدل برای تولید پاسخ بر اساس توکن‌های ورودی استفاده می‌کند، با حداکثر 1024 توکن جدید.

10. **رمزگشایی پاسخ**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - این خط توکن‌های تولید شده را به یک رشته خوانا برای انسان تبدیل می‌کند، هرگونه توکن ویژه را نادیده می‌گیرد و اولین نتیجه را دریافت می‌کند.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را رعایت کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل اشتباهات یا نادرستی‌هایی باشد. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.