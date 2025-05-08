<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-07T14:08:28+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "ur"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

یہ کوڈ ایک ماڈل کو OpenVINO فارمیٹ میں ایکسپورٹ کرتا ہے، اسے لوڈ کرتا ہے، اور دیے گئے پرامپٹ کے جواب میں ردعمل پیدا کرنے کے لیے استعمال کرتا ہے۔

1. **ماڈل ایکسپورٹ کرنا**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - یہ کمانڈ `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` استعمال کرتی ہے۔

2. **ضروری لائبریریز امپورٹ کرنا**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - یہ لائنز `transformers` library and the `optimum.intel.openvino` ماڈیول سے کلاسز امپورٹ کرتی ہیں، جو ماڈل کو لوڈ اور استعمال کرنے کے لیے ضروری ہیں۔

3. **ماڈل ڈائریکٹری اور کنفیگریشن سیٹ کرنا**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` ایک ڈکشنری ہے جو OpenVINO ماڈل کو کم تاخیر کو ترجیح دینے، ایک انفیرینس اسٹریم استعمال کرنے، اور کیش ڈائریکٹری استعمال نہ کرنے کے لیے کنفیگر کرتی ہے۔

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
   - یہ لائن مخصوص ڈائریکٹری سے ماڈل لوڈ کرتی ہے، جو پہلے سے متعین کنفیگریشن سیٹنگز استعمال کرتی ہے۔ اگر ضرورت ہو تو ریموٹ کوڈ ایکزیکیوشن کی اجازت بھی دیتی ہے۔

5. **ٹوکنازر لوڈ کرنا**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - یہ لائن ٹوکنازر لوڈ کرتی ہے، جو متن کو ایسے ٹوکنز میں تبدیل کرنے کا ذمہ دار ہے جنہیں ماڈل سمجھ سکے۔

6. **ٹوکنازر آرگیومنٹس سیٹ کرنا**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - یہ ڈکشنری مخصوص کرتی ہے کہ خاص ٹوکنز ٹوکنائزڈ آؤٹ پٹ میں شامل نہ کیے جائیں۔

7. **پرامپٹ کی تعریف کرنا**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - یہ سٹرنگ ایک بات چیت کا پرامپٹ سیٹ کرتی ہے جہاں یوزر AI اسسٹنٹ سے خود کا تعارف کروانے کو کہتا ہے۔

8. **پرامپٹ کو ٹوکنائز کرنا**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - یہ لائن پرامپٹ کو ایسے ٹوکنز میں تبدیل کرتی ہے جنہیں ماڈل پروسیس کر سکتا ہے، اور نتیجہ PyTorch ٹینسرز کی صورت میں واپس دیتی ہے۔

9. **ردعمل جنریٹ کرنا**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - یہ لائن ان پٹ ٹوکنز کی بنیاد پر ماڈل کا استعمال کرتے ہوئے ردعمل پیدا کرتی ہے، جس میں زیادہ سے زیادہ 1024 نئے ٹوکنز شامل ہو سکتے ہیں۔

10. **ردعمل کو ڈی کوڈ کرنا**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - یہ لائن جنریٹ کیے گئے ٹوکنز کو دوبارہ انسان پڑھنے کے قابل سٹرنگ میں تبدیل کرتی ہے، خاص ٹوکنز کو چھوڑ کر، اور پہلا نتیجہ حاصل کرتی ہے۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا بے قاعدگیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔