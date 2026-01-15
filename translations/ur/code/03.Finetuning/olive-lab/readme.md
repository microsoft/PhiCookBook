<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-16T15:47:15+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "ur"
}
-->
# لیب۔ آن ڈیوائس انفرنس کے لیے AI ماڈلز کو بہتر بنائیں

## تعارف

> [!IMPORTANT]  
> اس لیب کے لیے **Nvidia A10 یا A100 GPU** درکار ہے جس کے ساتھ متعلقہ ڈرائیورز اور CUDA ٹول کٹ (ورژن 12+) انسٹال ہوں۔

> [!NOTE]  
> یہ ایک **35 منٹ** کی لیب ہے جو آپ کو OLIVE کے ذریعے آن ڈیوائس انفرنس کے لیے ماڈلز کو بہتر بنانے کے بنیادی تصورات کا عملی تعارف فراہم کرے گی۔

## سیکھنے کے مقاصد

اس لیب کے اختتام پر، آپ OLIVE استعمال کر کے درج ذیل کام کر سکیں گے:

- AWQ کوانٹائزیشن طریقہ کار استعمال کرتے ہوئے AI ماڈل کو کوانٹائز کرنا۔  
- کسی مخصوص کام کے لیے AI ماڈل کو فائن ٹیون کرنا۔  
- ONNX Runtime پر مؤثر آن ڈیوائس انفرنس کے لیے LoRA ایڈاپٹرز (فائن ٹیون شدہ ماڈل) تیار کرنا۔

### Olive کیا ہے

Olive (*O*NNX *live*) ایک ماڈل آپٹیمائزیشن ٹول کٹ ہے جس کے ساتھ CLI بھی آتا ہے جو آپ کو ONNX runtime +++https://onnxruntime.ai+++ کے لیے معیاری اور کارکردگی والے ماڈلز فراہم کرنے کی سہولت دیتا ہے۔

![Olive Flow](../../../../../translated_images/ur/olive-flow.a47985655a756dcb.png)

Olive کا ان پٹ عام طور پر PyTorch یا Hugging Face ماڈل ہوتا ہے اور آؤٹ پٹ ایک بہتر بنایا گیا ONNX ماڈل ہوتا ہے جو ONNX runtime چلانے والے ڈیوائس (تعیناتی ہدف) پر چلتا ہے۔ Olive ماڈل کو تعیناتی ہدف کے AI ایکسیلیریٹر (NPU, GPU, CPU) کے لیے بہتر بناتا ہے جو Qualcomm، AMD، Nvidia یا Intel جیسے ہارڈویئر فراہم کنندہ کی طرف سے فراہم کیا جاتا ہے۔

Olive ایک *workflow* چلاتا ہے، جو ماڈل آپٹیمائزیشن کے انفرادی کاموں کی ترتیب وار سیریز ہوتی ہے جنہیں *passes* کہا جاتا ہے - مثال کے طور پر: ماڈل کمپریشن، گراف کیپچر، کوانٹائزیشن، گراف آپٹیمائزیشن۔ ہر پاس کے پیرامیٹرز ہوتے ہیں جنہیں بہترین میٹرکس جیسے درستگی اور تاخیر حاصل کرنے کے لیے ایڈجسٹ کیا جا سکتا ہے، جو متعلقہ ایویلیوایٹر کے ذریعے جانچے جاتے ہیں۔ Olive ایک سرچ اسٹریٹجی استعمال کرتا ہے جو ہر پاس کو ایک ایک کر کے یا پاسز کے سیٹ کو ایک ساتھ خودکار طریقے سے ٹیون کرتا ہے۔

#### Olive کے فوائد

- گراف آپٹیمائزیشن، کمپریشن اور کوانٹائزیشن کی مختلف تکنیکوں کے ساتھ تجربات کے دوران ہونے والی الجھن اور وقت کو کم کریں۔ اپنی کوالٹی اور کارکردگی کی حدود مقرر کریں اور Olive خود بخود آپ کے لیے بہترین ماڈل تلاش کرے گا۔  
- **40+ بلٹ ان ماڈل آپٹیمائزیشن کمپونینٹس** جو کوانٹائزیشن، کمپریشن، گراف آپٹیمائزیشن اور فائن ٹیوننگ کی جدید تکنیکوں کا احاطہ کرتے ہیں۔  
- عام ماڈل آپٹیمائزیشن کاموں کے لیے آسان CLI، مثلاً olive quantize، olive auto-opt، olive finetune۔  
- ماڈل پیکجنگ اور تعیناتی بلٹ ان۔  
- **Multi LoRA serving** کے لیے ماڈلز تیار کرنے کی حمایت۔  
- YAML/JSON استعمال کر کے ورک فلو بنانے کی سہولت تاکہ ماڈل آپٹیمائزیشن اور تعیناتی کے کاموں کو منظم کیا جا سکے۔  
- **Hugging Face** اور **Azure AI** انٹیگریشن۔  
- بلٹ ان **کیشنگ** میکانزم جو **لاگت بچاتا ہے**۔

## لیب کی ہدایات

> [!NOTE]  
> براہ کرم یقینی بنائیں کہ آپ نے اپنا Azure AI Hub اور پروجیکٹ تیار کر لیا ہے اور Lab 1 کے مطابق اپنا A100 کمپیوٹ سیٹ اپ کر لیا ہے۔

### مرحلہ 0: اپنے Azure AI کمپیوٹ سے کنیکٹ ہوں

آپ **VS Code** میں ریموٹ فیچر استعمال کرتے ہوئے Azure AI کمپیوٹ سے کنیکٹ ہوں گے۔

1. اپنا **VS Code** ڈیسک ٹاپ ایپلیکیشن کھولیں:  
1. **Shift+Ctrl+P** دباکر **کمانڈ پیلیٹ** کھولیں۔  
1. کمانڈ پیلیٹ میں تلاش کریں **AzureML - remote: Connect to compute instance in New Window**۔  
1. کمپیوٹ سے کنیکٹ ہونے کے لیے آن اسکرین ہدایات پر عمل کریں۔ اس میں آپ کی Azure سبسکرپشن، ریسورس گروپ، پروجیکٹ اور کمپیوٹ کا نام منتخب کرنا شامل ہوگا جو آپ نے Lab 1 میں سیٹ کیا تھا۔  
1. جب آپ Azure ML کمپیوٹ نوڈ سے کنیکٹ ہو جائیں گے تو یہ **Visual Code کے نیچے بائیں جانب** دکھائی دے گا `><Azure ML: Compute Name`

### مرحلہ 1: اس ریپو کو کلون کریں

VS Code میں، آپ **Ctrl+J** دباکر نیا ٹرمینل کھول سکتے ہیں اور اس ریپو کو کلون کریں:

ٹرمینل میں آپ کو پرامپٹ نظر آئے گا

```
azureuser@computername:~/cloudfiles/code$ 
```  
حل کو کلون کریں

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### مرحلہ 2: VS Code میں فولڈر کھولیں

متعلقہ فولڈر میں VS Code کھولنے کے لیے ٹرمینل میں درج ذیل کمانڈ چلائیں، جو ایک نئی ونڈو کھولے گی:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

متبادل طور پر، آپ **File** > **Open Folder** منتخب کر کے بھی فولڈر کھول سکتے ہیں۔

### مرحلہ 3: Dependencies

VS Code میں اپنے Azure AI کمپیوٹ انسٹینس میں ٹرمینل کھولیں (اشارہ: **Ctrl+J**) اور درج ذیل کمانڈز چلائیں تاکہ dependencies انسٹال ہو سکیں:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> تمام dependencies انسٹال ہونے میں تقریباً 5 منٹ لگیں گے۔

اس لیب میں آپ ماڈلز Azure AI ماڈل کیٹلاگ میں ڈاؤن لوڈ اور اپلوڈ کریں گے۔ ماڈل کیٹلاگ تک رسائی کے لیے آپ کو Azure میں لاگ ان کرنا ہوگا:

```bash
az login
```

> [!NOTE]  
> لاگ ان کے وقت آپ سے سبسکرپشن منتخب کرنے کو کہا جائے گا۔ یقینی بنائیں کہ آپ وہی سبسکرپشن منتخب کریں جو اس لیب کے لیے فراہم کی گئی ہے۔

### مرحلہ 4: Olive کمانڈز چلائیں

VS Code میں اپنے Azure AI کمپیوٹ انسٹینس میں ٹرمینل کھولیں (اشارہ: **Ctrl+J**) اور یقینی بنائیں کہ `olive-ai` کونڈا ماحول فعال ہے:

```bash
conda activate olive-ai
```

اب درج ذیل Olive کمانڈز کمانڈ لائن میں چلائیں۔

1. **ڈیٹا کا معائنہ کریں:** اس مثال میں، آپ Phi-3.5-Mini ماڈل کو فائن ٹیون کرنے جا رہے ہیں تاکہ یہ سفر سے متعلق سوالات کے جواب دینے میں مہارت حاصل کر لے۔ نیچے دیا گیا کوڈ JSON لائنز فارمیٹ میں ڈیٹا سیٹ کے چند ریکارڈز دکھاتا ہے:

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **ماڈل کو کوانٹائز کریں:** ماڈل کی تربیت سے پہلے، آپ اسے Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ تکنیک استعمال کرتے ہوئے کوانٹائز کریں گے۔ AWQ ماڈل کے وزن کو اس وقت پیدا ہونے والی ایکٹیویشنز کو مدنظر رکھتے ہوئے کوانٹائز کرتا ہے۔ اس کا مطلب ہے کہ کوانٹائزیشن کا عمل ایکٹیویشنز میں اصل ڈیٹا کی تقسیم کو شامل کرتا ہے، جس سے روایتی وزن کوانٹائزیشن کے مقابلے میں ماڈل کی درستگی بہتر طور پر محفوظ رہتی ہے۔

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ کوانٹائزیشن مکمل ہونے میں **تقریباً 8 منٹ** لگتے ہیں، جو ماڈل کے سائز کو تقریباً **7.5GB سے 2.5GB تک کم کر دیتا ہے**۔

    اس لیب میں ہم آپ کو دکھا رہے ہیں کہ Hugging Face سے ماڈلز کیسے ان پٹ کریں (مثال کے طور پر: `microsoft/Phi-3.5-mini-instruct`)۔ تاہم، Olive آپ کو Azure AI کیٹلاگ سے ماڈلز ان پٹ کرنے کی بھی اجازت دیتا ہے، بس `model_name_or_path` دلیل کو Azure AI اثاثہ ID میں اپ ڈیٹ کریں (مثال کے طور پر: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`)۔

1. **ماڈل کی تربیت کریں:** اس کے بعد، `olive finetune` کمانڈ کوانٹائزڈ ماڈل کو فائن ٹیون کرتی ہے۔ ماڈل کو فائن ٹیون کرنے سے پہلے کوانٹائز کرنا بہتر درستگی دیتا ہے کیونکہ فائن ٹیوننگ عمل کوانٹائزیشن کی وجہ سے ہونے والے کچھ نقصان کو بحال کر دیتا ہے۔

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

    فائن ٹیوننگ مکمل ہونے میں **تقریباً 6 منٹ** لگتے ہیں (100 سٹیپس کے ساتھ)۔

1. **آپٹیمائز کریں:** ماڈل کی تربیت کے بعد، آپ Olive کی `auto-opt` کمانڈ استعمال کرتے ہوئے ماڈل کو بہتر بنائیں گے، جو ONNX گراف کو کیپچر کرے گی اور خودکار طور پر کئی آپٹیمائزیشنز کرے گی تاکہ CPU کے لیے ماڈل کی کارکردگی بہتر ہو، ماڈل کو کمپریس اور فیوز کرے گی۔ یہ بات قابل ذکر ہے کہ آپ دوسرے ڈیوائسز جیسے NPU یا GPU کے لیے بھی آپٹیمائز کر سکتے ہیں بس `--device` اور `--provider` دلائل کو اپ ڈیٹ کر کے - لیکن اس لیب کے لیے ہم CPU استعمال کریں گے۔

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

    آپٹیمائزیشن مکمل ہونے میں **تقریباً 5 منٹ** لگتے ہیں۔

### مرحلہ 5: ماڈل انفرنس کا فوری ٹیسٹ

ماڈل کی انفرنس ٹیسٹ کرنے کے لیے، اپنے فولڈر میں **app.py** نامی پائتھن فائل بنائیں اور درج ذیل کوڈ کاپی پیسٹ کریں:

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

کوڈ چلائیں:

```bash
python app.py
```

### مرحلہ 6: ماڈل کو Azure AI پر اپلوڈ کریں

ماڈل کو Azure AI ماڈل ریپوزیٹری میں اپلوڈ کرنے سے ماڈل آپ کی ڈیولپمنٹ ٹیم کے دیگر ارکان کے ساتھ شیئر کیا جا سکتا ہے اور ماڈل کے ورژن کنٹرول کا انتظام بھی ہوتا ہے۔ ماڈل اپلوڈ کرنے کے لیے درج ذیل کمانڈ چلائیں:

> [!NOTE]  
> `{}` پلیس ہولڈرز کو اپنے ریسورس گروپ اور Azure AI پروجیکٹ کے نام سے اپ ڈیٹ کریں۔

اپنا ریسورس گروپ `"resourceGroup"` اور Azure AI پروجیکٹ کا نام معلوم کرنے کے لیے درج ذیل کمانڈ چلائیں:

```
az ml workspace show
```

یا +++ai.azure.com+++ پر جا کر **management center** > **project** > **overview** منتخب کریں۔

`{}` پلیس ہولڈرز کو اپنے ریسورس گروپ اور Azure AI پروجیکٹ کے نام سے اپ ڈیٹ کریں۔

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

آپ پھر اپنے اپلوڈ کیے گئے ماڈل کو دیکھ سکتے ہیں اور https://ml.azure.com/model/list پر ماڈل کو تعینات کر سکتے ہیں۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔