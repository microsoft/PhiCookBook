<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5621d23b682762686e0eccc7ce8bd9ec",
  "translation_date": "2025-04-03T07:10:41+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_OpenVino_Chat.md",
  "language_code": "ur"
}
-->
[OpenVino چیٹ سیمپل](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

یہ کوڈ ایک ماڈل کو OpenVINO فارمیٹ میں ایکسپورٹ کرتا ہے، اسے لوڈ کرتا ہے، اور دیے گئے پرومپٹ کے جواب میں ایک ریسپانس تیار کرتا ہے۔

1. **ماڈل کو ایکسپورٹ کرنا**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - یہ کمانڈ `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` استعمال کرتی ہے۔

2. **ضروری لائبریریاں درآمد کرنا**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - یہ لائنیں `transformers` library and the `optimum.intel.openvino` ماڈیول سے کلاسز کو درآمد کرتی ہیں، جو ماڈل کو لوڈ کرنے اور استعمال کرنے کے لیے ضروری ہیں۔

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
   - `ov_config` ایک ڈکشنری ہے جو OpenVINO ماڈل کو کم لیٹنسی کو ترجیح دینے، ایک انفیرینس اسٹریم استعمال کرنے، اور کیش ڈائریکٹری استعمال نہ کرنے کے لیے کنفیگر کرتی ہے۔

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
   - یہ لائن ماڈل کو مخصوص ڈائریکٹری سے لوڈ کرتی ہے، جو پہلے سے دی گئی کنفیگریشن سیٹنگز استعمال کرتی ہے۔ یہ ضرورت پڑنے پر ریموٹ کوڈ ایکزیکیوشن کی بھی اجازت دیتی ہے۔

5. **ٹوکینائزر لوڈ کرنا**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - یہ لائن ٹوکینائزر کو لوڈ کرتی ہے، جو ٹیکسٹ کو ان ٹوکنز میں تبدیل کرنے کے لیے ذمہ دار ہے جنہیں ماڈل سمجھ سکتا ہے۔

6. **ٹوکینائزر آرگومنٹس سیٹ کرنا**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - یہ ڈکشنری مخصوص کرتی ہے کہ اسپیشل ٹوکنز کو ٹوکینائزڈ آؤٹ پٹ میں شامل نہ کیا جائے۔

7. **پرومپٹ کو ڈیفائن کرنا**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - یہ اسٹرنگ ایک گفتگو کا پرومپٹ سیٹ کرتی ہے جہاں صارف AI اسسٹنٹ سے اپنا تعارف کرانے کے لیے کہتا ہے۔

8. **پرومپٹ کو ٹوکینائز کرنا**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - یہ لائن پرومپٹ کو ان ٹوکنز میں تبدیل کرتی ہے جنہیں ماڈل پراسیس کر سکتا ہے، اور نتیجہ کو PyTorch ٹینسرز کی شکل میں واپس کرتی ہے۔

9. **ریسپانس تیار کرنا**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - یہ لائن ماڈل کو استعمال کرتی ہے تاکہ ان پٹ ٹوکنز کی بنیاد پر ایک ریسپانس تیار کیا جا سکے، جس میں زیادہ سے زیادہ 1024 نئے ٹوکنز شامل ہوں۔

10. **ریسپانس کو ڈی کوڈ کرنا**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - یہ لائن تیار کردہ ٹوکنز کو دوبارہ انسان کے لیے قابلِ پڑھائی اسٹرنگ میں تبدیل کرتی ہے، اسپیشل ٹوکنز کو چھوڑ کر، اور پہلا نتیجہ حاصل کرتی ہے۔

**اعلانِ لاتعلقی**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کو یقینی بنانے کی کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔