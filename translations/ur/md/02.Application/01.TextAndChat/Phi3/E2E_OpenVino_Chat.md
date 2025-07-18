<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:01:46+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "ur"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

یہ کوڈ ایک ماڈل کو OpenVINO فارمیٹ میں ایکسپورٹ کرتا ہے، اسے لوڈ کرتا ہے، اور دیے گئے پرامپٹ کے جواب میں استعمال کرتا ہے۔

1. **ماڈل کو ایکسپورٹ کرنا**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - یہ کمانڈ `optimum-cli` ٹول کا استعمال کرتے ہوئے ماڈل کو OpenVINO فارمیٹ میں ایکسپورٹ کرتی ہے، جو مؤثر انفرنس کے لیے بہتر بنایا گیا ہے۔
   - ایکسپورٹ کیا جانے والا ماڈل `"microsoft/Phi-3-mini-4k-instruct"` ہے، جو ماضی کے سیاق و سباق کی بنیاد پر متن تیار کرنے کے کام کے لیے ترتیب دیا گیا ہے۔
   - ماڈل کے وزن 4-بٹ انٹیجرز (`int4`) میں کوانٹائز کیے گئے ہیں، جو ماڈل کے سائز کو کم کرنے اور پراسیسنگ کو تیز کرنے میں مدد دیتے ہیں۔
   - دیگر پیرامیٹرز جیسے `group-size`، `ratio`، اور `sym` کوانٹائزیشن کے عمل کو بہتر بنانے کے لیے استعمال ہوتے ہیں۔
   - ایکسپورٹ کیا گیا ماڈل `./model/phi3-instruct/int4` ڈائریکٹری میں محفوظ کیا جاتا ہے۔

2. **ضروری لائبریریاں امپورٹ کرنا**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - یہ لائنز `transformers` لائبریری اور `optimum.intel.openvino` ماڈیول سے کلاسز امپورٹ کرتی ہیں، جو ماڈل کو لوڈ اور استعمال کرنے کے لیے ضروری ہیں۔

3. **ماڈل ڈائریکٹری اور کنفیگریشن سیٹ کرنا**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` اس جگہ کی نشاندہی کرتا ہے جہاں ماڈل فائلز محفوظ ہیں۔
   - `ov_config` ایک ڈکشنری ہے جو OpenVINO ماڈل کو کم تاخیر کو ترجیح دینے، ایک انفرنس اسٹریم استعمال کرنے، اور کیش ڈائریکٹری استعمال نہ کرنے کے لیے ترتیب دیتی ہے۔

4. **ماڈل لوڈ کرنا**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - یہ لائن مخصوص ڈائریکٹری سے ماڈل کو لوڈ کرتی ہے، جو پہلے سے طے شدہ کنفیگریشن سیٹنگز استعمال کرتی ہے۔ اگر ضرورت ہو تو ریموٹ کوڈ ایکزیکیوشن کی اجازت بھی دیتی ہے۔

5. **ٹوکینائزر لوڈ کرنا**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - یہ لائن ٹوکینائزر کو لوڈ کرتی ہے، جو متن کو ایسے ٹوکنز میں تبدیل کرنے کا ذمہ دار ہے جنہیں ماڈل سمجھ سکتا ہے۔

6. **ٹوکینائزر کے دلائل سیٹ کرنا**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - یہ ڈکشنری بتاتی ہے کہ خاص ٹوکنز کو ٹوکینائزڈ آؤٹ پٹ میں شامل نہ کیا جائے۔

7. **پرامپٹ کی تعریف کرنا**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - یہ سٹرنگ ایک گفتگو کا پرامپٹ سیٹ کرتی ہے جہاں صارف AI اسسٹنٹ سے اپنا تعارف کرانے کو کہتا ہے۔

8. **پرامپٹ کو ٹوکینائز کرنا**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - یہ لائن پرامپٹ کو ایسے ٹوکنز میں تبدیل کرتی ہے جنہیں ماڈل پراسیس کر سکتا ہے، اور نتیجہ PyTorch ٹینسرز کی صورت میں واپس کرتی ہے۔

9. **جواب تیار کرنا**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - یہ لائن ماڈل کا استعمال کرتے ہوئے ان پٹ ٹوکنز کی بنیاد پر جواب تیار کرتی ہے، جس میں زیادہ سے زیادہ 1024 نئے ٹوکنز شامل کیے جاتے ہیں۔

10. **جواب کو ڈی کوڈ کرنا**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - یہ لائن تیار کردہ ٹوکنز کو دوبارہ انسان کے پڑھنے کے قابل سٹرنگ میں تبدیل کرتی ہے، خاص ٹوکنز کو چھوڑ کر، اور پہلا نتیجہ حاصل کرتی ہے۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔