# المختبر. تحسين نماذج الذكاء الاصطناعي للاستدلال على الجهاز

## المقدمة

> [!IMPORTANT]
> يتطلب هذا المختبر وجود **بطاقة رسومات Nvidia A10 أو A100** مع التعريفات المرتبطة وأدوات CUDA (الإصدار 12 أو أحدث) مثبتة.

> [!NOTE]
> هذا مختبر مدته **35 دقيقة** يمنحك مقدمة عملية لمفاهيم تحسين النماذج للاستدلال على الجهاز باستخدام OLIVE.

## أهداف التعلم

بنهاية هذا المختبر، ستكون قادرًا على استخدام OLIVE لـ:

- تقليل دقة نموذج الذكاء الاصطناعي باستخدام طريقة التقليل AWQ.
- ضبط نموذج الذكاء الاصطناعي لمهمة محددة.
- توليد محولات LoRA (النموذج المضبوط) لاستدلال فعال على الجهاز باستخدام ONNX Runtime.

### ما هو Olive

Olive (*O*NNX *live*) هو مجموعة أدوات لتحسين النماذج مع واجهة سطر أوامر مرافقة تتيح لك نشر النماذج على ONNX runtime +++https://onnxruntime.ai+++ مع جودة وأداء عاليين.

![Olive Flow](../../../../../translated_images/ar/olive-flow.c4f76d9142c579b2.webp)

عادةً ما يكون الإدخال إلى Olive نموذج PyTorch أو Hugging Face، والإخراج هو نموذج ONNX محسن يتم تنفيذه على جهاز (هدف النشر) يعمل بنظام ONNX runtime. يقوم Olive بتحسين النموذج لمسرع الذكاء الاصطناعي الخاص بجهاز النشر (NPU، GPU، CPU) المقدم من بائع الأجهزة مثل Qualcomm أو AMD أو Nvidia أو Intel.

يقوم Olive بتنفيذ *سير عمل*، وهو تسلسل مرتب من مهام تحسين النموذج الفردية المسماة *التمريرات* - من أمثلة التمريرات: ضغط النموذج، التقاط الرسم البياني، التقليل، تحسين الرسم البياني. لكل تمريرة مجموعة من المعلمات التي يمكن ضبطها لتحقيق أفضل المقاييس، مثل الدقة والكمون، التي يتم تقييمها بواسطة المقيم المختص. يستخدم Olive استراتيجية بحث تعتمد على خوارزمية بحث لضبط كل تمريرة تلقائيًا واحدة تلو الأخرى أو مجموعة تمريرات معًا.

#### فوائد Olive

- **تقليل الإحباط والوقت** الناتج عن التجارب اليدوية المتكررة مع تقنيات تحسين الرسم البياني، الضغط، والتقليل. حدد قيود الجودة والأداء ودع Olive يجد أفضل نموذج لك تلقائيًا.
- **أكثر من 40 مكونًا مدمجًا لتحسين النماذج** تغطي أحدث التقنيات في التقليل، الضغط، تحسين الرسم البياني، وضبط النماذج.
- **واجهة سطر أوامر سهلة الاستخدام** للمهام الشائعة في تحسين النماذج. على سبيل المثال، olive quantize، olive auto-opt، olive finetune.
- تغليف النماذج والنشر مدمج.
- يدعم توليد نماذج لـ **خدمة Multi LoRA**.
- بناء سير عمل باستخدام YAML/JSON لتنظيم مهام تحسين النماذج والنشر.
- تكامل مع **Hugging Face** و **Azure AI**.
- آلية **تخزين مؤقت** مدمجة لتقليل **التكاليف**.

## تعليمات المختبر

> [!NOTE]
> يرجى التأكد من إعداد Azure AI Hub والمشروع الخاص بك وضبط حوسبة A100 كما في المختبر 1.

### الخطوة 0: الاتصال بحوسبة Azure AI الخاصة بك

سوف تتصل بحوسبة Azure AI باستخدام ميزة الاتصال عن بُعد في **VS Code**.

1. افتح تطبيق **VS Code** على سطح المكتب:
2. افتح **لوحة الأوامر** باستخدام **Shift+Ctrl+P**
3. في لوحة الأوامر، ابحث عن **AzureML - remote: Connect to compute instance in New Window**.
4. اتبع التعليمات الظاهرة على الشاشة للاتصال بالحوسبة. سيتطلب ذلك اختيار اشتراك Azure، مجموعة الموارد، المشروع واسم الحوسبة التي قمت بإعدادها في المختبر 1.
5. بمجرد الاتصال بعقدة Azure ML Compute، سيظهر ذلك في **أسفل يسار Visual Code** `><Azure ML: Compute Name`

### الخطوة 1: استنساخ هذا المستودع

في VS Code، يمكنك فتح نافذة طرفية جديدة باستخدام **Ctrl+J** واستنساخ هذا المستودع:

في الطرفية سترى الموجه

```
azureuser@computername:~/cloudfiles/code$ 
```
استنساخ الحل

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### الخطوة 2: فتح المجلد في VS Code

لفتح VS Code في المجلد المناسب، نفذ الأمر التالي في الطرفية، والذي سيفتح نافذة جديدة:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

بدلاً من ذلك، يمكنك فتح المجلد عن طريق اختيار **ملف** > **فتح مجلد**.

### الخطوة 3: تثبيت التبعيات

افتح نافذة طرفية في VS Code على جهاز Azure AI Compute الخاص بك (نصيحة: **Ctrl+J**) ونفذ الأوامر التالية لتثبيت التبعيات:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> سيستغرق تثبيت جميع التبعيات حوالي 5 دقائق.

في هذا المختبر، ستقوم بتنزيل وتحميل النماذج إلى كتالوج نماذج Azure AI. للوصول إلى كتالوج النماذج، ستحتاج إلى تسجيل الدخول إلى Azure باستخدام:

```bash
az login
```

> [!NOTE]
> عند تسجيل الدخول، سيُطلب منك اختيار الاشتراك. تأكد من تعيين الاشتراك إلى الاشتراك المخصص لهذا المختبر.

### الخطوة 4: تنفيذ أوامر Olive

افتح نافذة طرفية في VS Code على جهاز Azure AI Compute الخاص بك (نصيحة: **Ctrl+J**) وتأكد من تفعيل بيئة `olive-ai` conda:

```bash
conda activate olive-ai
```

بعد ذلك، نفذ أوامر Olive التالية في سطر الأوامر.

1. **فحص البيانات:** في هذا المثال، ستقوم بضبط نموذج Phi-3.5-Mini ليكون متخصصًا في الإجابة على أسئلة متعلقة بالسفر. يعرض الكود أدناه السجلات الأولى من مجموعة البيانات، والتي تكون بصيغة JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```
2. **تقليل دقة النموذج:** قبل تدريب النموذج، تقوم أولاً بتقليله باستخدام الأمر التالي الذي يستخدم تقنية تسمى Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. تقوم AWQ بتقليل أوزان النموذج مع مراعاة التنشيطات التي يتم إنتاجها أثناء الاستدلال. هذا يعني أن عملية التقليل تأخذ في الاعتبار توزيع البيانات الفعلي في التنشيطات، مما يؤدي إلى الحفاظ بشكل أفضل على دقة النموذج مقارنة بطرق تقليل الأوزان التقليدية.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    تستغرق عملية تقليل AWQ حوالي **8 دقائق**، والتي ستؤدي إلى **تقليل حجم النموذج من ~7.5 جيجابايت إلى ~2.5 جيجابايت**.

    في هذا المختبر، نوضح لك كيفية إدخال النماذج من Hugging Face (على سبيل المثال: `microsoft/Phi-3.5-mini-instruct`). ومع ذلك، يسمح لك Olive أيضًا بإدخال النماذج من كتالوج Azure AI عن طريق تحديث الوسيط `model_name_or_path` إلى معرف أصل Azure AI (على سبيل المثال: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

3. **تدريب النموذج:** بعد ذلك، يقوم أمر `olive finetune` بضبط النموذج الذي تم تقليله. تقليل النموذج *قبل* الضبط يعطي دقة أفضل لأن عملية الضبط تعوض بعض الخسارة الناتجة عن التقليل.

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

    يستغرق الضبط حوالي **6 دقائق** (مع 100 خطوة).

4. **التحسين:** بعد تدريب النموذج، تقوم الآن بتحسين النموذج باستخدام أمر `auto-opt` من Olive، والذي سيقوم بالتقاط رسم ONNX البياني وتنفيذ عدد من التحسينات تلقائيًا لتحسين أداء النموذج على وحدة المعالجة المركزية عن طريق ضغط النموذج ودمج العمليات. من الجدير بالذكر أنه يمكنك أيضًا تحسين النموذج لأجهزة أخرى مثل NPU أو GPU فقط عن طريق تحديث الوسيطات `--device` و `--provider` - لكن لأغراض هذا المختبر سنستخدم CPU.

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

    تستغرق عملية التحسين حوالي **5 دقائق**.

### الخطوة 5: اختبار سريع للاستدلال على النموذج

لاختبار استدلال النموذج، أنشئ ملف Python في مجلدك باسم **app.py** ونسخ والصق الكود التالي:

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

نفذ الكود باستخدام:

```bash
python app.py
```

### الخطوة 6: رفع النموذج إلى Azure AI

رفع النموذج إلى مستودع نماذج Azure AI يجعل النموذج قابلًا للمشاركة مع أعضاء فريق التطوير الآخرين ويتولى أيضًا التحكم في إصدارات النموذج. لرفع النموذج، نفذ الأمر التالي:

> [!NOTE]
> حدّث أماكن الحجز `{}` باسم مجموعة الموارد واسم مشروع Azure AI الخاص بك.

للعثور على مجموعة الموارد `"resourceGroup"` واسم مشروع Azure AI، نفذ الأمر التالي:

```
az ml workspace show
```

أو من خلال الذهاب إلى +++ai.azure.com+++ واختيار **مركز الإدارة** > **المشروع** > **نظرة عامة**

حدّث أماكن الحجز `{}` باسم مجموعة الموارد واسم مشروع Azure AI الخاص بك.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

يمكنك بعد ذلك رؤية النموذج الذي رفعته ونشره على https://ml.azure.com/model/list

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.