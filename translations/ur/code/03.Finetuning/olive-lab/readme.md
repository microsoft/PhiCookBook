<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76956c0c22e5686908a6d85ec72126af",
  "translation_date": "2025-04-03T06:14:20+00:00",
  "source_file": "code\\03.Finetuning\\olive-lab\\readme.md",
  "language_code": "ur"
}
-->
# لیب: AI ماڈلز کو ڈیوائس پر انفیرینس کے لیے بہتر بنائیں

## تعارف

> [!IMPORTANT]
> اس لیب کے لیے **Nvidia A10 یا A100 GPU** اور اس کے متعلقہ ڈرائیورز اور CUDA ٹول کٹ (ورژن 12+) کی انسٹالیشن ضروری ہے۔

> [!NOTE]
> یہ ایک **35 منٹ** کا لیب ہے جو آپ کو OLIVE کے ذریعے ماڈلز کو ڈیوائس پر انفیرینس کے لیے بہتر بنانے کے بنیادی تصورات کا عملی تعارف فراہم کرے گا۔

## سیکھنے کے مقاصد

اس لیب کے اختتام تک، آپ OLIVE کا استعمال کرتے ہوئے یہ کر سکیں گے:

- AWQ کوانٹائزیشن طریقے کا استعمال کرتے ہوئے AI ماڈل کو کوانٹائز کرنا۔
- کسی خاص کام کے لیے AI ماڈل کو فائن ٹیون کرنا۔
- LoRA ایڈاپٹرز (فائن ٹیونڈ ماڈل) تیار کرنا تاکہ ONNX Runtime پر ڈیوائس انفیرینس مؤثر طریقے سے ہو سکے۔

### اولیو کیا ہے؟

اولیو (*O*NNX *live*) ایک ماڈل آپٹمائزیشن ٹول کٹ ہے جس کے ساتھ CLI آتا ہے، جو آپ کو ONNX runtime +++https://onnxruntime.ai+++ کے لیے ماڈلز کو معیار اور کارکردگی کے ساتھ بھیجنے کی سہولت فراہم کرتا ہے۔

![Olive Flow](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.ur.png)

اولیو میں عام طور پر ایک PyTorch یا Hugging Face ماڈل ان پٹ ہوتا ہے، اور آؤٹ پٹ ایک بہتر بنایا گیا ONNX ماڈل ہوتا ہے جو اس ڈیوائس (تعیناتی ہدف) پر چلایا جاتا ہے جو ONNX runtime چلاتا ہے۔ اولیو ماڈل کو تعیناتی ہدف کے AI ایکسیلیریٹر (NPU، GPU، CPU) کے لیے بہتر بناتا ہے، جو Qualcomm، AMD، Nvidia یا Intel جیسے ہارڈویئر فراہم کنندہ سے ہوتا ہے۔

اولیو ایک *ورک فلو* انجام دیتا ہے، جو ماڈل آپٹمائزیشن کے انفرادی ٹاسکس کی ترتیب وار سلسلہ *پاسز* کہلاتا ہے - مثال کے طور پر پاسز: ماڈل کمپریشن، گراف کیپچر، کوانٹائزیشن، گراف آپٹمائزیشن۔ ہر پاس میں ایک سیٹ پیرامیٹرز ہوتے ہیں جنہیں بہترین میٹرکس حاصل کرنے کے لیے ٹیون کیا جا سکتا ہے، جیسے کہ ایکوریسی اور لیٹنسی، جن کا جائزہ متعلقہ ایویلیوایٹر لیتا ہے۔ اولیو ایک سرچ اسٹریٹجی استعمال کرتا ہے جو ہر پاس یا پاسز کے سیٹ کو ایک ایک کر کے یا ایک ساتھ خودکار طریقے سے ٹیون کرنے کے لیے سرچ الگورتھم کا استعمال کرتا ہے۔

#### اولیو کے فوائد

- گراف آپٹمائزیشن، کمپریشن اور کوانٹائزیشن کے مختلف تکنیکوں کے ساتھ ٹرائل اینڈ ایرر دستی تجربات کی **مایوسی اور وقت کو کم کریں**۔ اپنی معیار اور کارکردگی کی پابندیاں متعین کریں اور اولیو کو خود بخود آپ کے لیے بہترین ماڈل تلاش کرنے دیں۔
- **40+ بلٹ ان ماڈل آپٹمائزیشن اجزاء**، جو کوانٹائزیشن، کمپریشن، گراف آپٹمائزیشن اور فائن ٹیوننگ میں جدید تکنیکوں کا احاطہ کرتے ہیں۔
- عام ماڈل آپٹمائزیشن ٹاسکس کے لیے **آسان CLI**۔ مثال کے طور پر، olive quantize، olive auto-opt، olive finetune۔
- ماڈل پیکجنگ اور تعیناتی بلٹ ان۔
- **ملٹی LoRA سرونگ** کے لیے ماڈلز تیار کرنے کی سپورٹ۔
- ماڈل آپٹمائزیشن اور تعیناتی ٹاسکس کو آرکیسٹریٹ کرنے کے لیے YAML/JSON کا استعمال کرتے ہوئے ورک فلو بنائیں۔
- **Hugging Face** اور **Azure AI** انٹیگریشن۔
- **کیشنگ** میکانزم بلٹ ان، **لاگت بچانے** کے لیے۔

## لیب ہدایات
> [!NOTE]
> براہ کرم یقینی بنائیں کہ آپ نے اپنی Azure AI ہب اور پروجیکٹ کو پروویژن کیا ہے اور اپنی A100 کمپیوٹ کو لیب 1 کے مطابق سیٹ اپ کیا ہے۔

### مرحلہ 0: اپنے Azure AI کمپیوٹ سے کنیکٹ کریں

آپ **VS Code** میں ریموٹ فیچر کا استعمال کرتے ہوئے Azure AI کمپیوٹ سے کنیکٹ کریں گے۔

1. اپنی **VS Code** ڈیسک ٹاپ ایپلیکیشن کھولیں:
1. **کمانڈ پلیٹ** کھولنے کے لیے **Shift+Ctrl+P** دبائیں۔
1. کمانڈ پلیٹ میں **AzureML - remote: Connect to compute instance in New Window** تلاش کریں۔
1. کمپیوٹ سے کنیکٹ کرنے کے لیے اسکرین پر دی گئی ہدایات پر عمل کریں۔ اس میں آپ کے Azure سبسکرپشن، ریسورس گروپ، پروجیکٹ اور کمپیوٹ کا نام منتخب کرنا شامل ہوگا جو آپ نے لیب 1 میں سیٹ اپ کیا تھا۔
1. ایک بار جب آپ اپنے Azure ML کمپیوٹ نوڈ سے کنیکٹ ہو جائیں، تو یہ **VS Code کے نیچے بائیں جانب** ظاہر ہوگا `><Azure ML: Compute Name`۔

### مرحلہ 1: اس ریپو کو کلون کریں

VS Code میں، آپ **Ctrl+J** دباکر ایک نیا ٹرمینل کھول سکتے ہیں اور اس ریپو کو کلون کر سکتے ہیں:

ٹرمینل میں آپ کو یہ پرامپٹ نظر آئے گا:

```
azureuser@computername:~/cloudfiles/code$ 
```
حل کو کلون کریں:

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### مرحلہ 2: فولڈر کو VS Code میں کھولیں

متعلقہ فولڈر میں VS Code کھولنے کے لیے، ٹرمینل میں درج ذیل کمانڈ کو چلائیں، جو ایک نئی ونڈو کھولے گی:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

متبادل کے طور پر، آپ فولڈر کو **File** > **Open Folder** منتخب کرکے کھول سکتے ہیں۔

### مرحلہ 3: ڈیپینڈنسیز

Azure AI کمپیوٹ انسٹینس میں VS Code میں ایک ٹرمینل ونڈو کھولیں (ٹپ: **Ctrl+J**) اور درج ذیل کمانڈز کو چلائیں تاکہ ڈیپینڈنسیز انسٹال ہو سکیں:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> تمام ڈیپینڈنسیز کو انسٹال کرنے میں تقریباً **5 منٹ** لگیں گے۔

اس لیب میں آپ ماڈلز کو Azure AI ماڈل کیٹلاگ میں ڈاؤن لوڈ اور اپ لوڈ کریں گے۔ ماڈل کیٹلاگ تک رسائی کے لیے، آپ کو Azure میں لاگ ان کرنا ہوگا:

```bash
az login
```

> [!NOTE]
> لاگ ان کے وقت آپ سے اپنی سبسکرپشن منتخب کرنے کو کہا جائے گا۔ یقینی بنائیں کہ آپ اس لیب کے لیے فراہم کردہ سبسکرپشن کو سیٹ کریں۔

### مرحلہ 4: اولیو کمانڈز کو چلائیں

Azure AI کمپیوٹ انسٹینس میں VS Code میں ایک ٹرمینل ونڈو کھولیں (ٹپ: **Ctrl+J**) اور یقینی بنائیں کہ `olive-ai` کونڈا ماحول ایکٹیویٹڈ ہے:

```bash
conda activate olive-ai
```

اب، درج ذیل اولیو کمانڈز کمانڈ لائن میں چلائیں۔

1. **ڈیٹا کا معائنہ کریں:** اس مثال میں، آپ Phi-3.5-Mini ماڈل کو فائن ٹیون کریں گے تاکہ یہ ٹریول سے متعلق سوالات کا جواب دینے میں ماہر ہو۔ درج ذیل کوڈ ڈیٹا سیٹ کے ابتدائی چند ریکارڈز کو ظاہر کرتا ہے، جو JSON لائنز فارمیٹ میں ہیں:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **ماڈل کو کوانٹائز کریں:** ماڈل کو ٹرین کرنے سے پہلے، آپ درج ذیل کمانڈ کا استعمال کرتے ہوئے اسے کوانٹائز کریں گے، جو ایک تکنیک Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ استعمال کرتا ہے۔ AWQ ماڈل کے ویٹس کو ان ایکٹیویشنز کو مدنظر رکھتے ہوئے کوانٹائز کرتا ہے جو انفیرینس کے دوران پیدا ہوتے ہیں۔ اس کا مطلب ہے کہ کوانٹائزیشن کا عمل ایکٹیویشنز میں موجود ڈیٹا ڈسٹریبیوشن کو مدنظر رکھتا ہے، جس سے ماڈل کی ایکوریسی کو روایتی ویٹ کوانٹائزیشن کے مقابلے میں بہتر طور پر محفوظ کیا جاتا ہے۔

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ کوانٹائزیشن مکمل ہونے میں **تقریباً 8 منٹ** لگتے ہیں، جو ماڈل کا سائز **~7.5GB سے ~2.5GB** تک کم کر دیتا ہے۔

    اس لیب میں، ہم آپ کو دکھا رہے ہیں کہ Hugging Face سے ماڈلز کو ان پٹ کیسے دیا جاتا ہے (مثال کے طور پر: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` کمانڈ کوانٹائزڈ ماڈل کو فائن ٹیون کرتا ہے۔ ماڈل کو فائن ٹیون کرنے سے پہلے کوانٹائز کرنا، بجائے بعد میں، بہتر ایکوریسی دیتا ہے کیونکہ فائن ٹیوننگ کا عمل کوانٹائزیشن کے نقصانات میں سے کچھ کو بحال کرتا ہے۔

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

    فائن ٹیوننگ (100 اسٹیپس کے ساتھ) مکمل ہونے میں **تقریباً 6 منٹ** لگتے ہیں۔

1. **آپٹمائز کریں:** ماڈل کو ٹرین کرنے کے بعد، اب آپ اولیو کے `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` آرگیومنٹس کا استعمال کرتے ہوئے ماڈل کو آپٹمائز کریں گے - لیکن اس لیب کے مقاصد کے لیے ہم CPU استعمال کریں گے۔

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

    آپٹمائزیشن مکمل ہونے میں **تقریباً 5 منٹ** لگتے ہیں۔

### مرحلہ 5: ماڈل انفیرینس کا فوری ٹیسٹ

ماڈل کے انفیرینس کو ٹیسٹ کرنے کے لیے، اپنے فولڈر میں ایک Python فائل بنائیں جس کا نام **app.py** ہو اور درج ذیل کوڈ کو کاپی اور پیسٹ کریں:

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

کوڈ کو چلانے کے لیے درج ذیل کمانڈ کا استعمال کریں:

```bash
python app.py
```

### مرحلہ 6: ماڈل کو Azure AI پر اپ لوڈ کریں

ماڈل کو Azure AI ماڈل ریپوزٹری میں اپ لوڈ کرنے سے ماڈل آپ کی ڈویلپمنٹ ٹیم کے دوسرے ممبرز کے ساتھ شیئر ہو سکتا ہے اور ماڈل کا ورژن کنٹرول بھی ہینڈل ہو جاتا ہے۔ ماڈل اپ لوڈ کرنے کے لیے درج ذیل کمانڈ چلائیں:

> [!NOTE]
> `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` اور Azure AI پروجیکٹ کے نام کو اپ ڈیٹ کریں، اور درج ذیل کمانڈ چلائیں:

```
az ml workspace show
```

یا پھر +++ai.azure.com+++ پر جا کر **management center** **project** **overview** منتخب کریں۔

`{}` پلیس ہولڈرز کو اپنے ریسورس گروپ اور Azure AI پروجیکٹ کے نام سے اپ ڈیٹ کریں۔

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

آپ اپنے اپ لوڈ کردہ ماڈل کو دیکھ سکتے ہیں اور اسے https://ml.azure.com/model/list پر ڈپلائے کر سکتے ہیں۔

**ڈسکلوزر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔