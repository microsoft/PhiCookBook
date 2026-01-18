<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:34:07+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "ur"
}
-->
# **اپنا Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 فیملی کے ساتھ بنائیں**

کیا آپ نے GitHub Copilot Chat میں workspace agent استعمال کیا ہے؟ کیا آپ اپنی ٹیم کا اپنا کوڈ ایجنٹ بنانا چاہتے ہیں؟ یہ عملی لیب اوپن سورس ماڈل کو ملا کر ایک انٹرپرائز سطح کے کوڈ بزنس ایجنٹ بنانے کی کوشش کرتی ہے۔

## **بنیاد**

### **Microsoft Phi-3 کیوں منتخب کریں**

Phi-3 ایک فیملی سیریز ہے، جس میں phi-3-mini، phi-3-small، اور phi-3-medium شامل ہیں جو مختلف تربیتی پیرامیٹرز کی بنیاد پر متن کی تخلیق، مکالمے کی تکمیل، اور کوڈ جنریشن کے لیے ہیں۔ اس کے علاوہ phi-3-vision بھی ہے جو Vision پر مبنی ہے۔ یہ انٹرپرائزز یا مختلف ٹیموں کے لیے آف لائن جنریٹو AI حل بنانے کے لیے موزوں ہے۔

اس لنک کو پڑھنے کی سفارش کی جاتی ہے [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat ایکسٹینشن آپ کو ایک چیٹ انٹرفیس فراہم کرتا ہے جو آپ کو GitHub Copilot کے ساتھ بات چیت کرنے اور VS Code کے اندر ہی کوڈنگ سے متعلق سوالات کے جوابات حاصل کرنے کی سہولت دیتا ہے، بغیر دستاویزات میں جانے یا آن لائن فورمز تلاش کرنے کی ضرورت کے۔

Copilot Chat ممکنہ طور پر syntax highlighting، indentation، اور دیگر فارمیٹنگ خصوصیات استعمال کرتا ہے تاکہ پیدا کردہ جواب کو واضح بنایا جا سکے۔ صارف کے سوال کی نوعیت کے مطابق، نتیجہ میں ایسے لنکس شامل ہو سکتے ہیں جو Copilot نے جواب تیار کرنے کے لیے استعمال کیے، جیسے سورس کوڈ فائلز یا دستاویزات، یا VS Code کی فعالیت تک رسائی کے بٹن۔

- Copilot Chat آپ کے ڈیولپر فلو میں ضم ہو کر جہاں ضرورت ہو مدد فراہم کرتا ہے:

- ایڈیٹر یا ٹرمینل سے براہ راست inline چیٹ شروع کریں تاکہ کوڈنگ کے دوران مدد حاصل ہو

- Chat ویو استعمال کریں تاکہ آپ کے پاس کسی بھی وقت AI اسسٹنٹ موجود ہو

- Quick Chat لانچ کریں تاکہ فوری سوال پوچھ کر دوبارہ اپنے کام پر واپس جا سکیں

آپ GitHub Copilot Chat کو مختلف حالات میں استعمال کر سکتے ہیں، جیسے:

- مسئلہ حل کرنے کے بہترین طریقے پر کوڈنگ سوالات کے جوابات دینا

- کسی اور کے کوڈ کی وضاحت کرنا اور بہتری کی تجاویز دینا

- کوڈ کی اصلاحات تجویز کرنا

- یونٹ ٹیسٹ کیسز تیار کرنا

- کوڈ دستاویزات تیار کرنا

اس لنک کو پڑھنے کی سفارش کی جاتی ہے [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat میں **@workspace** کا حوالہ دے کر آپ اپنے پورے کوڈ بیس کے بارے میں سوالات پوچھ سکتے ہیں۔ سوال کی بنیاد پر، Copilot متعلقہ فائلز اور سمبلز کو ذہانت سے تلاش کرتا ہے، جنہیں وہ اپنے جواب میں لنکس اور کوڈ مثالوں کے طور پر شامل کرتا ہے۔

آپ کے سوال کا جواب دینے کے لیے، **@workspace** ان ہی ذرائع سے تلاش کرتا ہے جنہیں ایک ڈیولپر VS Code میں کوڈ بیس کو نیویگیٹ کرتے وقت استعمال کرتا ہے:

- ورک اسپیس کی تمام فائلیں، سوائے ان فائلوں کے جو .gitignore فائل کے ذریعے نظر انداز کی گئی ہوں

- ڈائریکٹری کا ڈھانچہ جس میں nested فولڈرز اور فائل کے نام شامل ہوں

- GitHub کا کوڈ سرچ انڈیکس، اگر ورک اسپیس GitHub ریپوزیٹری ہو اور کوڈ سرچ کے ذریعے انڈیکس کیا گیا ہو

- ورک اسپیس میں سمبلز اور تعریفیں

- فعال ایڈیٹر میں منتخب شدہ یا نظر آنے والا متن

نوٹ: اگر آپ نے کوئی فائل کھولی ہو یا نظر انداز شدہ فائل میں متن منتخب کیا ہو تو .gitignore کو نظر انداز کیا جاتا ہے۔

اس لنک کو پڑھنے کی سفارش کی جاتی ہے [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **اس لیب کے بارے میں مزید جانیں**

GitHub Copilot نے انٹرپرائزز کی پروگرامنگ کی کارکردگی کو بہت بہتر بنایا ہے، اور ہر انٹرپرائز GitHub Copilot کی متعلقہ خصوصیات کو اپنی مرضی کے مطابق بنانا چاہتا ہے۔ بہت سے انٹرپرائزز نے اپنے کاروباری منظرناموں اور اوپن سورس ماڈلز کی بنیاد پر GitHub Copilot جیسے کسٹم ایکسٹینشنز تیار کیے ہیں۔ انٹرپرائزز کے لیے کسٹم ایکسٹینشنز کو کنٹرول کرنا آسان ہوتا ہے، لیکن اس سے صارف کے تجربے پر بھی اثر پڑتا ہے۔ آخرکار، GitHub Copilot عام منظرناموں اور پیشہ ورانہ مہارت کے لیے زیادہ مضبوط خصوصیات رکھتا ہے۔ اگر تجربہ مستقل رکھا جا سکے تو اپنی مرضی کے مطابق انٹرپرائز کی اپنی ایکسٹینشن بہتر ہوگی۔ GitHub Copilot Chat انٹرپرائزز کو چیٹ کے تجربے میں توسیع کے لیے متعلقہ APIs فراہم کرتا ہے۔ مستقل تجربہ برقرار رکھنا اور کسٹم خصوصیات کا ہونا بہتر صارف تجربہ ہے۔

یہ لیب بنیادی طور پر Phi-3 ماڈل کو مقامی NPU اور Azure ہائبرڈ کے ساتھ ملا کر GitHub Copilot Chat میں ایک کسٹم ایجنٹ ***@PHI3*** بناتی ہے تاکہ انٹرپرائز ڈیولپرز کو کوڈ جنریشن مکمل کرنے میں مدد دے سکے ***(@PHI3 /gen)*** اور تصاویر کی بنیاد پر کوڈ تیار کرے ***(@PHI3 /img)***۔

![PHI3](../../../../../../../translated_images/ur/cover.1017ebc9a7c46d09.webp)

### ***نوٹ:*** 

یہ لیب فی الحال Intel CPU اور Apple Silicon کے AIPC پر نافذ کی گئی ہے۔ ہم Qualcomm ورژن کے NPU کو بھی اپ ڈیٹ کرتے رہیں گے۔

## **لیب**

| نام | تفصیل | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | متعلقہ ماحول اور انسٹالیشن ٹولز کی ترتیب اور تنصیب | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | AIPC / Apple Silicon کے ساتھ مل کر، مقامی NPU استعمال کرتے ہوئے Phi-3-mini کے ذریعے کوڈ جنریشن بنائیں | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Azure Machine Learning Service کے ماڈل کیٹلاگ - Phi-3-vision امیج کو تعینات کر کے کوڈ تیار کریں | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | GitHub Copilot Chat میں ایک کسٹم Phi-3 ایجنٹ بنائیں جو کوڈ جنریشن، گراف جنریشن کوڈ، RAG وغیرہ مکمل کرے | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | سیمپل کوڈ ڈاؤن لوڈ کریں | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **وسائل**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot کے بارے میں مزید جانیں [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat کے بارے میں مزید جانیں [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API کے بارے میں مزید جانیں [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Foundry کے بارے میں مزید جانیں [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI Foundry کے Model Catalog کے بارے میں مزید جانیں [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔