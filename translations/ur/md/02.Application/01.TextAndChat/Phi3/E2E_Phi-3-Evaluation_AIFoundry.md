<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7799f9e2960966adc296d24cdf0d6486",
  "translation_date": "2025-04-03T07:11:38+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "ur"
}
-->
# Azure AI Foundry میں Fine-tuned Phi-3 / Phi-3.5 ماڈل کا Microsoft's Responsible AI اصولوں پر مبنی جائزہ لینا

یہ مکمل نمونہ Microsoft Tech Community کی گائیڈ "[Azure AI Foundry میں Fine-tuned Phi-3 / 3.5 ماڈلز کا Microsoft's Responsible AI اصولوں پر مبنی جائزہ](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" پر مبنی ہے۔

## خلاصہ

### Azure AI Foundry میں Fine-tuned Phi-3 / Phi-3.5 ماڈل کی حفاظت اور کارکردگی کا جائزہ کیسے لیا جا سکتا ہے؟

ماڈل کو Fine-tune کرنے سے کبھی کبھار غیر ارادی یا غیر مطلوبہ جوابات پیدا ہو سکتے ہیں۔ یہ یقینی بنانے کے لیے کہ ماڈل محفوظ اور مؤثر رہے، یہ ضروری ہے کہ ماڈل کے نقصان دہ مواد پیدا کرنے کی صلاحیت اور درست، متعلقہ، اور مربوط جوابات پیدا کرنے کی صلاحیت کا جائزہ لیا جائے۔ اس سبق میں، آپ سیکھیں گے کہ Azure AI Foundry میں Prompt flow کے ساتھ مربوط Fine-tuned Phi-3 / Phi-3.5 ماڈل کی حفاظت اور کارکردگی کا جائزہ کیسے لیا جائے۔

یہ ہے Azure AI Foundry کا جائزہ لینے کا عمل۔

![سبق کی تعمیرات۔](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.ur.png)

*تصویری ماخذ: [تخلیقی AI ایپلیکیشنز کا جائزہ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> مزید تفصیلی معلومات اور Phi-3 / Phi-3.5 کے بارے میں اضافی وسائل کو دریافت کرنے کے لیے، براہ کرم [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) پر جائیں۔

### ضروریات

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 ماڈل

### مواد کی فہرست

1. [**منظرنامہ 1: Azure AI Foundry کے Prompt flow جائزے کا تعارف**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [حفاظت کے جائزے کا تعارف](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [کارکردگی کے جائزے کا تعارف](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**منظرنامہ 2: Azure AI Foundry میں Phi-3 / Phi-3.5 ماڈل کا جائزہ لینا**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [شروع کرنے سے پہلے](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 / Phi-3.5 ماڈل کا جائزہ لینے کے لیے Azure OpenAI تعینات کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure AI Foundry کے Prompt flow جائزے کا استعمال کرتے ہوئے Fine-tuned Phi-3 / Phi-3.5 ماڈل کا جائزہ لینا](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [مبارک ہو!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **منظرنامہ 1: Azure AI Foundry کے Prompt flow جائزے کا تعارف**

### حفاظت کے جائزے کا تعارف

یہ یقینی بنانے کے لیے کہ آپ کا AI ماڈل اخلاقی اور محفوظ ہے، اسے Microsoft's Responsible AI اصولوں کے خلاف جانچنا بہت ضروری ہے۔ Azure AI Foundry میں، حفاظت کے جائزے آپ کے ماڈل کی نقصان دہ مواد پیدا کرنے کی صلاحیت اور jailbreak حملوں کے لیے اس کی کمزوری کا جائزہ لینے کی اجازت دیتے ہیں، جو ان اصولوں کے ساتھ براہ راست منسلک ہیں۔

![حفاظت کا جائزہ۔](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.ur.png)

*تصویری ماخذ: [تخلیقی AI ایپلیکیشنز کا جائزہ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft کے Responsible AI اصول

تکنیکی مراحل شروع کرنے سے پہلے، Microsoft's Responsible AI اصولوں کو سمجھنا ضروری ہے، جو AI سسٹمز کی ذمہ دارانہ ترقی، تعیناتی، اور عمل کے لیے ایک اخلاقی فریم ورک ہیں۔ یہ اصول AI ٹیکنالوجیز کو منصفانہ، شفاف، اور جامع طریقے سے بنانے کی رہنمائی کرتے ہیں۔ یہ اصول AI ماڈلز کی حفاظت کے جائزے کی بنیاد ہیں۔

Microsoft کے Responsible AI اصول شامل ہیں:

- **منصفانہ اور جامع**: AI سسٹمز کو ہر ایک کے ساتھ منصفانہ سلوک کرنا چاہیے اور اسی طرح کے حالات میں مختلف گروپوں پر مختلف اثرات نہیں ڈالنے چاہئیں۔ مثال کے طور پر، جب AI سسٹمز طبی علاج، قرض کی درخواستوں، یا ملازمت کے بارے میں رہنمائی فراہم کرتے ہیں، تو انہیں اسی علامات، مالی حالات، یا پیشہ ورانہ قابلیت رکھنے والے ہر فرد کو ایک جیسی سفارشات دینی چاہیے۔

- **قابل اعتماد اور محفوظ**: اعتماد پیدا کرنے کے لیے، یہ ضروری ہے کہ AI سسٹمز قابل اعتماد، محفوظ، اور مستقل طور پر کام کریں۔ یہ سسٹمز ان حالات کے خلاف مزاحمت کرنے کے قابل ہونے چاہئیں جن کا ڈیزائن اور جانچ کے دوران پیش گوئی کی گئی تھی۔

- **شفافیت**: جب AI سسٹمز لوگوں کی زندگیوں پر اثر ڈالنے والے فیصلوں میں مدد فراہم کرتے ہیں، تو یہ ضروری ہے کہ لوگ یہ سمجھیں کہ وہ فیصلے کیسے کیے گئے۔

- **پرائیویسی اور سیکیورٹی**: AI کے بڑھتے ہوئے استعمال کے ساتھ، پرائیویسی اور ذاتی معلومات کی حفاظت زیادہ اہم اور پیچیدہ ہو رہی ہے۔

- **جوابدہی**: جو لوگ AI سسٹمز کو ڈیزائن اور تعینات کرتے ہیں، انہیں اس بات کے جوابدہ ہونا چاہیے کہ ان کے سسٹمز کیسے کام کرتے ہیں۔

![فل ہب۔](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.ur.png)

*تصویری ماخذ: [ذمہ دار AI کیا ہے؟](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft's Responsible AI اصولوں کے بارے میں مزید جاننے کے لیے، [ذمہ دار AI کیا ہے؟](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) پر جائیں۔

#### حفاظتی میٹرکس

اس سبق میں، آپ Azure AI Foundry کے حفاظتی میٹرکس کا استعمال کرتے ہوئے Fine-tuned Phi-3 ماڈل کی حفاظت کا جائزہ لیں گے۔ یہ میٹرکس ماڈل کے نقصان دہ مواد پیدا کرنے کی صلاحیت اور jailbreak حملوں کے لیے اس کی کمزوری کا جائزہ لینے میں مدد دیتے ہیں۔ حفاظتی میٹرکس میں شامل ہیں:

- **خود کو نقصان پہنچانے والے مواد سے متعلق**: ماڈل کے خود کو نقصان پہنچانے والے مواد پیدا کرنے کے رجحان کا جائزہ۔
- **نفرت انگیز اور غیر منصفانہ مواد**: ماڈل کے نفرت انگیز یا غیر منصفانہ مواد پیدا کرنے کے رجحان کا جائزہ۔
- **تشدد سے متعلق مواد**: ماڈل کے تشدد سے متعلق مواد پیدا کرنے کے رجحان کا جائزہ۔
- **جنسی مواد**: ماڈل کے غیر مناسب جنسی مواد پیدا کرنے کے رجحان کا جائزہ۔

ان پہلوؤں کا جائزہ لینے سے یہ یقینی بنایا جاتا ہے کہ AI ماڈل نقصان دہ یا توہین آمیز مواد پیدا نہ کرے، جو معاشرتی اقدار اور ضوابط کے معیار کے مطابق ہو۔

![حفاظت کی بنیاد پر جائزہ لیں۔](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.ur.png)

### کارکردگی کے جائزے کا تعارف

یہ یقینی بنانے کے لیے کہ آپ کا AI ماڈل توقع کے مطابق کام کر رہا ہے، اس کی کارکردگی کو کارکردگی کے میٹرکس کے خلاف جانچنا ضروری ہے۔ Azure AI Foundry میں، کارکردگی کے جائزے آپ کے ماڈل کی درست، متعلقہ، اور مربوط جوابات پیدا کرنے کی صلاحیت کا جائزہ لینے کی اجازت دیتے ہیں۔

![حفاظت کا جائزہ۔](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.ur.png)

*تصویری ماخذ: [تخلیقی AI ایپلیکیشنز کا جائزہ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### کارکردگی کے میٹرکس

اس سبق میں، آپ Azure AI Foundry کے کارکردگی کے میٹرکس کا استعمال کرتے ہوئے Fine-tuned Phi-3 / Phi-3.5 ماڈل کی کارکردگی کا جائزہ لیں گے۔ یہ میٹرکس ماڈل کی درست، متعلقہ، اور مربوط جوابات پیدا کرنے کی صلاحیت کا جائزہ لینے میں مدد دیتے ہیں۔ کارکردگی کے میٹرکس میں شامل ہیں:

- **گراؤنڈڈنس**: پیدا کیے گئے جوابات کی معلومات کے منبع کے ساتھ مطابقت کا جائزہ۔
- **متعلقہ**: دیے گئے سوالات کے ساتھ پیدا کیے گئے جوابات کی مطابقت کا جائزہ۔
- **ہم آہنگی**: پیدا کیے گئے متن کے روانی، قدرتی پڑھنے، اور انسانی جیسی زبان سے مشابہت کا جائزہ۔
- **روانی**: پیدا کیے گئے متن کی زبان کی مہارت کا جائزہ۔
- **GPT مماثلت**: پیدا کیے گئے جواب کو گراؤنڈ ٹروتھ کے ساتھ مماثلت کے لیے موازنہ۔
- **F1 اسکور**: پیدا کیے گئے جواب اور منبع ڈیٹا کے درمیان مشترکہ الفاظ کے تناسب کا حساب۔

یہ میٹرکس ماڈل کی درست، متعلقہ، اور مربوط جوابات پیدا کرنے کی صلاحیت کا جائزہ لینے میں مدد کرتے ہیں۔

![کارکردگی کی بنیاد پر جائزہ لیں۔](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.ur.png)

## **منظرنامہ 2: Azure AI Foundry میں Phi-3 / Phi-3.5 ماڈل کا جائزہ لینا**

### شروع کرنے سے پہلے

یہ سبق پچھلے بلاگ پوسٹس کا تسلسل ہے، "[Fine-Tune اور Custom Phi-3 ماڈلز کو Prompt Flow کے ساتھ مربوط کریں: مرحلہ وار گائیڈ](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" اور "[Fine-Tune اور Custom Phi-3 ماڈلز کو Azure AI Foundry میں Prompt Flow کے ساتھ مربوط کریں](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)۔" ان پوسٹس میں، ہم نے Azure AI Foundry میں Fine-tuned Phi-3 / Phi-3.5 ماڈل کو Fine-tune کرنے اور Prompt flow کے ساتھ مربوط کرنے کے عمل کا جائزہ لیا۔

اس سبق میں، آپ Azure AI Foundry میں ایک evaluator کے طور پر Azure OpenAI ماڈل تعینات کریں گے اور اس کا استعمال کرتے ہوئے اپنے Fine-tuned Phi-3 / Phi-3.5 ماڈل کا جائزہ لیں گے۔

اس سبق کو شروع کرنے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل ضروریات ہیں، جیسا کہ پچھلے سبق میں بیان کیا گیا ہے:

1. Fine-tuned Phi-3 / Phi-3.5 ماڈل کا جائزہ لینے کے لیے تیار کردہ ڈیٹا سیٹ۔
1. Azure Machine Learning میں تعینات Fine-tuned Phi-3 / Phi-3.5 ماڈل۔
1. Azure AI Foundry میں Prompt flow کے ساتھ مربوط Fine-tuned Phi-3 / Phi-3.5 ماڈل۔

> [!NOTE]
> آپ *test_data.jsonl* فائل، جو پچھلے بلاگ پوسٹس میں ڈاؤن لوڈ کیے گئے **ULTRACHAT_200k** ڈیٹا سیٹ کے ڈیٹا فولڈر میں موجود ہے، کو Fine-tuned Phi-3 / Phi-3.5 ماڈل کے جائزے کے لیے استعمال کریں گے۔

#### Azure AI Foundry میں کوڈ-فرسٹ طریقے سے Custom Phi-3 / Phi-3.5 ماڈل کو Prompt flow کے ساتھ مربوط کریں

> [!NOTE]
> اگر آپ نے "[Fine-Tune اور Custom Phi-3 ماڈلز کو Azure AI Foundry میں Prompt Flow کے ساتھ مربوط کریں](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" میں بیان کردہ لو کوڈ طریقے کی پیروی کی ہے، تو آپ اس مشق کو چھوڑ کر اگلی مشق پر جا سکتے ہیں۔
> تاہم، اگر آپ نے "[Fine-Tune اور Custom Phi-3 ماڈلز کو Prompt Flow کے ساتھ مربوط کریں: مرحلہ وار گائیڈ](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" میں بیان کردہ کوڈ-فرسٹ طریقے کی پیروی کی ہے، تو آپ کے ماڈل کو Prompt flow کے ساتھ مربوط کرنے کا عمل تھوڑا مختلف ہوگا۔ آپ اس مشق میں یہ عمل سیکھیں گے۔

آگے بڑھنے کے لیے، آپ کو Azure AI Foundry میں اپنے Fine-tuned Phi-3 / Phi-3.5 ماڈل کو Prompt flow میں مربوط کرنا ہوگا۔

#### Azure AI Foundry Hub بنائیں

آپ کو پروجیکٹ بنانے سے پہلے ایک Hub بنانا ہوگا۔ Hub ایک Resource Group کی طرح کام کرتا ہے، جو آپ کو Azure AI Foundry میں متعدد پروجیکٹس کو منظم اور سنبھالنے کی اجازت دیتا ہے۔

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) میں سائن ان کریں۔

1. بائیں طرف کے ٹیب سے **All hubs** منتخب کریں۔

1. نیویگیشن مینو سے **+ New hub** منتخب کریں۔

    ![ہب بنائیں۔](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.ur.png)

1. درج ذیل کام کریں:

    - **Hub name** درج کریں۔ یہ ایک منفرد قدر ہونا چاہیے۔
    - اپنا Azure **Subscription** منتخب کریں۔
    - **Resource group** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - وہ **Location** منتخب کریں جسے آپ استعمال کرنا چاہتے ہیں۔
    - **Connect Azure AI Services** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - **Connect Azure AI Search** منتخب کریں اور **Skip connecting** پر کلک کریں۔
![ہب بھریں۔](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.ur.png)

1. **Next** منتخب کریں۔

#### Azure AI Foundry پروجیکٹ بنائیں

1. اپنے بنائے گئے ہب میں، بائیں جانب ٹیب سے **All projects** منتخب کریں۔

1. نیویگیشن مینو سے **+ New project** منتخب کریں۔

    ![نیا پروجیکٹ منتخب کریں۔](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.ur.png)

1. **Project name** درج کریں۔ یہ منفرد ہونا چاہیے۔

    ![پروجیکٹ بنائیں۔](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.ur.png)

1. **Create a project** منتخب کریں۔

#### Phi-3 / Phi-3.5 ماڈل کے لیے کسٹم کنکشن شامل کریں

اپنے کسٹم Phi-3 / Phi-3.5 ماڈل کو Prompt flow کے ساتھ مربوط کرنے کے لیے، آپ کو ماڈل کے endpoint اور key کو کسٹم کنکشن میں محفوظ کرنا ہوگا۔ یہ سیٹ اپ Prompt flow میں آپ کے کسٹم Phi-3 / Phi-3.5 ماڈل تک رسائی کو یقینی بناتا ہے۔

#### Fine-tuned Phi-3 / Phi-3.5 ماڈل کے api key اور endpoint uri سیٹ کریں

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. Azure Machine Learning ورک اسپیس پر جائیں جو آپ نے بنایا ہے۔

1. بائیں جانب ٹیب سے **Endpoints** منتخب کریں۔

    ![Endpoints منتخب کریں۔](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.ur.png)

1. وہ endpoint منتخب کریں جو آپ نے بنایا ہے۔

    ![Endpoints منتخب کریں۔](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.ur.png)

1. نیویگیشن مینو سے **Consume** منتخب کریں۔

1. اپنا **REST endpoint** اور **Primary key** کاپی کریں۔

    ![api key اور endpoint uri کاپی کریں۔](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.ur.png)

#### کسٹم کنکشن شامل کریں

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) پر جائیں۔

1. Azure AI Foundry پروجیکٹ پر جائیں جو آپ نے بنایا ہے۔

1. پروجیکٹ میں جو آپ نے بنایا ہے، بائیں جانب ٹیب سے **Settings** منتخب کریں۔

1. **+ New connection** منتخب کریں۔

    ![نیا کنکشن منتخب کریں۔](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.ur.png)

1. نیویگیشن مینو سے **Custom keys** منتخب کریں۔

    ![کسٹم keys منتخب کریں۔](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.ur.png)

1. درج ذیل کام کریں:

    - **+ Add key value pairs** منتخب کریں۔
    - key name کے لیے **endpoint** درج کریں اور Azure ML Studio سے کاپی کیا گیا endpoint ویلیو فیلڈ میں چسپاں کریں۔
    - دوبارہ **+ Add key value pairs** منتخب کریں۔
    - key name کے لیے **key** درج کریں اور Azure ML Studio سے کاپی کیا گیا key ویلیو فیلڈ میں چسپاں کریں۔
    - keys شامل کرنے کے بعد، **is secret** منتخب کریں تاکہ key ظاہر نہ ہو۔

    ![کنکشن شامل کریں۔](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.ur.png)

1. **Add connection** منتخب کریں۔

#### Prompt flow بنائیں

آپ نے Azure AI Foundry میں کسٹم کنکشن شامل کر دیا ہے۔ اب، درج ذیل مراحل کا استعمال کرتے ہوئے ایک Prompt flow بنائیں۔ پھر، آپ اس Prompt flow کو کسٹم کنکشن کے ساتھ جوڑیں گے تاکہ Prompt flow میں Fine-tuned ماڈل کا استعمال کیا جا سکے۔

1. Azure AI Foundry پروجیکٹ پر جائیں جو آپ نے بنایا ہے۔

1. بائیں جانب ٹیب سے **Prompt flow** منتخب کریں۔

1. نیویگیشن مینو سے **+ Create** منتخب کریں۔

    ![Prompt flow منتخب کریں۔](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.ur.png)

1. نیویگیشن مینو سے **Chat flow** منتخب کریں۔

    ![Chat flow منتخب کریں۔](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.ur.png)

1. **Folder name** درج کریں۔

    ![Chat flow منتخب کریں۔](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.ur.png)

1. **Create** منتخب کریں۔

#### Prompt flow کو Fine-tuned Phi-3 / Phi-3.5 ماڈل کے ساتھ چیٹ کرنے کے لیے سیٹ کریں

آپ کو Fine-tuned Phi-3 / Phi-3.5 ماڈل کو Prompt flow میں مربوط کرنا ہوگا۔ تاہم، موجودہ Prompt flow اس مقصد کے لیے ڈیزائن نہیں کیا گیا ہے۔ لہٰذا، آپ کو موجودہ flow کو دوبارہ ڈیزائن کرنا ہوگا تاکہ کسٹم ماڈل کو مربوط کیا جا سکے۔

1. Prompt flow میں درج ذیل کام کریں تاکہ موجودہ flow کو دوبارہ تعمیر کریں:

    - **Raw file mode** منتخب کریں۔
    - *flow.dag.yml* فائل میں موجود تمام کوڈ حذف کریں۔
    - درج ذیل کوڈ *flow.dag.yml* میں شامل کریں۔

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **Save** منتخب کریں۔

    ![Raw file mode منتخب کریں۔](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.ur.png)

1. درج ذیل کوڈ *integrate_with_promptflow.py* میں شامل کریں تاکہ Prompt flow میں کسٹم Phi-3 / Phi-3.5 ماڈل کا استعمال کیا جا سکے۔

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Prompt flow کوڈ چسپاں کریں۔](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.ur.png)

> [!NOTE]
> Azure AI Foundry میں Prompt flow استعمال کرنے کے بارے میں مزید تفصیلی معلومات کے لیے، آپ [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) دیکھ سکتے ہیں۔

1. **Chat input**, **Chat output** منتخب کریں تاکہ اپنے ماڈل کے ساتھ چیٹ کو فعال کریں۔

    ![Input Output منتخب کریں۔](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.ur.png)

1. اب آپ اپنے کسٹم Phi-3 / Phi-3.5 ماڈل کے ساتھ چیٹ کرنے کے لیے تیار ہیں۔ اگلے مشق میں، آپ سیکھیں گے کہ Prompt flow کو کیسے شروع کریں اور اسے اپنے Fine-tuned Phi-3 / Phi-3.5 ماڈل کے ساتھ چیٹ کے لیے کیسے استعمال کریں۔

> [!NOTE]
>
> دوبارہ تعمیر شدہ flow نیچے دی گئی تصویر کی طرح ہونا چاہیے:
>
> ![Flow مثال](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.ur.png)
>

#### Prompt flow شروع کریں

1. Prompt flow شروع کرنے کے لیے **Start compute sessions** منتخب کریں۔

    ![Compute session شروع کریں۔](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.ur.png)

1. پیرامیٹرز کو تجدید کرنے کے لیے **Validate and parse input** منتخب کریں۔

    ![Input کی تصدیق کریں۔](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.ur.png)

1. کسٹم کنکشن کے **connection** کی **Value** منتخب کریں جو آپ نے بنایا ہے۔ مثال کے طور پر، *connection*۔

    ![کنکشن۔](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.ur.png)

#### اپنے کسٹم Phi-3 / Phi-3.5 ماڈل کے ساتھ چیٹ کریں

1. **Chat** منتخب کریں۔

    ![Chat منتخب کریں۔](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.ur.png)

1. یہاں نتائج کی ایک مثال ہے: اب آپ اپنے کسٹم Phi-3 / Phi-3.5 ماڈل کے ساتھ چیٹ کر سکتے ہیں۔ یہ تجویز کیا جاتا ہے کہ آپ Fine-tuning کے لیے استعمال کردہ ڈیٹا کی بنیاد پر سوالات پوچھیں۔

    ![Prompt flow کے ساتھ چیٹ کریں۔](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.ur.png)

### Phi-3 / Phi-3.5 ماڈل کا جائزہ لینے کے لیے Azure OpenAI کو تعینات کریں

Azure AI Foundry میں Phi-3 / Phi-3.5 ماڈل کا جائزہ لینے کے لیے، آپ کو ایک Azure OpenAI ماڈل تعینات کرنے کی ضرورت ہوگی۔ یہ ماڈل Phi-3 / Phi-3.5 ماڈل کی کارکردگی کا جائزہ لینے کے لیے استعمال کیا جائے گا۔

#### Azure OpenAI تعینات کریں

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) میں سائن ان کریں۔

1. Azure AI Foundry پروجیکٹ پر جائیں جو آپ نے بنایا ہے۔

    ![پروجیکٹ منتخب کریں۔](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.ur.png)

1. پروجیکٹ میں جو آپ نے بنایا ہے، بائیں جانب ٹیب سے **Deployments** منتخب کریں۔

1. نیویگیشن مینو سے **+ Deploy model** منتخب کریں۔

1. **Deploy base model** منتخب کریں۔

    ![Deployments منتخب کریں۔](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.ur.png)

1. Azure OpenAI ماڈل منتخب کریں جو آپ استعمال کرنا چاہتے ہیں۔ مثال کے طور پر، **gpt-4o**۔

    ![Azure OpenAI ماڈل منتخب کریں۔](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.ur.png)

1. **Confirm** منتخب کریں۔

### Azure AI Foundry کے Prompt flow evaluation کے ذریعے Fine-tuned Phi-3 / Phi-3.5 ماڈل کا جائزہ لیں

### نیا جائزہ شروع کریں

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) پر جائیں۔

1. Azure AI Foundry پروجیکٹ پر جائیں جو آپ نے بنایا ہے۔

    ![پروجیکٹ منتخب کریں۔](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.ur.png)

1. پروجیکٹ میں جو آپ نے بنایا ہے، بائیں جانب ٹیب سے **Evaluation** منتخب کریں۔

1. نیویگیشن مینو سے **+ New evaluation** منتخب کریں۔
![ایویلیوایشن منتخب کریں۔](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.ur.png)

1. **Prompt flow** ایویلیوایشن منتخب کریں۔

   ![Prompt flow ایویلیوایشن منتخب کریں۔](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.ur.png)

1. درج ذیل کام انجام دیں:

   - ایویلیوایشن کا نام درج کریں۔ یہ منفرد ہونا چاہیے۔
   - ٹاسک کی قسم کے طور پر **Question and answer without context** منتخب کریں۔ کیونکہ اس ٹیوٹوریل میں استعمال ہونے والا **UlTRACHAT_200k** ڈیٹاسیٹ کانٹیکسٹ پر مشتمل نہیں ہے۔
   - وہ **Prompt flow** منتخب کریں جسے آپ ایویلیوایٹ کرنا چاہتے ہیں۔

   ![Prompt flow ایویلیوایشن۔](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.ur.png)

1. **Next** منتخب کریں۔

1. درج ذیل کام انجام دیں:

   - **Add your dataset** منتخب کریں تاکہ ڈیٹاسیٹ اپلوڈ کریں۔ مثال کے طور پر، آپ ٹیسٹ ڈیٹاسیٹ فائل اپلوڈ کر سکتے ہیں، جیسے *test_data.json1*، جو **ULTRACHAT_200k** ڈیٹاسیٹ کے ساتھ شامل ہے۔
   - اپنے ڈیٹاسیٹ کے مطابق مناسب **Dataset column** منتخب کریں۔ مثال کے طور پر، اگر آپ **ULTRACHAT_200k** ڈیٹاسیٹ استعمال کر رہے ہیں، تو **${data.prompt}** کو ڈیٹاسیٹ کالم کے طور پر منتخب کریں۔

   ![Prompt flow ایویلیوایشن۔](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.ur.png)

1. **Next** منتخب کریں۔

1. کارکردگی اور معیار کے میٹرکس کو کنفیگر کرنے کے لیے درج ذیل کام کریں:

   - وہ کارکردگی اور معیار کے میٹرکس منتخب کریں جو آپ استعمال کرنا چاہتے ہیں۔
   - وہ Azure OpenAI ماڈل منتخب کریں جو آپ نے ایویلیوایشن کے لیے بنایا ہے۔ مثال کے طور پر، **gpt-4o** منتخب کریں۔

   ![Prompt flow ایویلیوایشن۔](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.ur.png)

1. خطرے اور حفاظت کے میٹرکس کو کنفیگر کرنے کے لیے درج ذیل کام کریں:

   - وہ خطرے اور حفاظت کے میٹرکس منتخب کریں جو آپ استعمال کرنا چاہتے ہیں۔
   - وہ تھریش ہولڈ منتخب کریں جو آپ ڈیفیکٹ ریٹ کیلکولیٹ کرنے کے لیے استعمال کرنا چاہتے ہیں۔ مثال کے طور پر، **Medium** منتخب کریں۔
   - **question** کے لیے، **Data source** کو **{$data.prompt}** پر سیٹ کریں۔
   - **answer** کے لیے، **Data source** کو **{$run.outputs.answer}** پر سیٹ کریں۔
   - **ground_truth** کے لیے، **Data source** کو **{$data.message}** پر سیٹ کریں۔

   ![Prompt flow ایویلیوایشن۔](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.ur.png)

1. **Next** منتخب کریں۔

1. ایویلیوایشن شروع کرنے کے لیے **Submit** منتخب کریں۔

1. ایویلیوایشن مکمل ہونے میں کچھ وقت لگے گا۔ آپ **Evaluation** ٹیب میں پیش رفت کو مانیٹر کر سکتے ہیں۔

### ایویلیوایشن کے نتائج کا جائزہ لیں

> [!NOTE]
> نیچے دیے گئے نتائج ایویلیوایشن کے عمل کو سمجھانے کے لیے پیش کیے گئے ہیں۔ اس ٹیوٹوریل میں، ایک چھوٹے ڈیٹاسیٹ پر ٹرین کیے گئے ماڈل کا استعمال کیا گیا ہے، جس کی وجہ سے نتائج مثالی نہیں ہو سکتے۔ اصل نتائج ڈیٹاسیٹ کے سائز، معیار، اور تنوع کے ساتھ ساتھ ماڈل کی مخصوص کنفیگریشن پر منحصر ہوتے ہیں۔

ایویلیوایشن مکمل ہونے کے بعد، آپ کارکردگی اور حفاظت کے میٹرکس کے نتائج کا جائزہ لے سکتے ہیں۔

1. کارکردگی اور معیار کے میٹرکس:

   - ماڈل کی قابلیت کا جائزہ لیں کہ وہ مربوط، روانی سے بھرپور، اور متعلقہ جوابات پیدا کر رہا ہے۔

   ![ایویلیوایشن نتیجہ۔](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.ur.png)

1. خطرے اور حفاظت کے میٹرکس:

   - اس بات کو یقینی بنائیں کہ ماڈل کے آؤٹ پٹس محفوظ ہیں اور Microsoft کے ذمہ دار AI اصولوں کے مطابق ہیں، اور کسی نقصان دہ یا توہین آمیز مواد سے پاک ہیں۔

   ![ایویلیوایشن نتیجہ۔](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.ur.png)

1. آپ **Detailed metrics result** دیکھنے کے لیے نیچے اسکرول کر سکتے ہیں۔

   ![ایویلیوایشن نتیجہ۔](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.ur.png)

1. اپنے کسٹم Phi-3 / Phi-3.5 ماڈل کو کارکردگی اور حفاظت کے میٹرکس کے خلاف ایویلیوایٹ کر کے، آپ اس بات کی تصدیق کر سکتے ہیں کہ ماڈل نہ صرف مؤثر ہے بلکہ ذمہ دار AI طریقوں کی پیروی بھی کرتا ہے، اور حقیقی دنیا میں استعمال کے لیے تیار ہے۔

## مبارک ہو!

### آپ نے یہ ٹیوٹوریل مکمل کر لیا ہے

آپ نے کامیابی کے ساتھ Azure AI Foundry میں Prompt flow کے ساتھ انٹیگریٹ کیے گئے ٹرین شدہ Phi-3 ماڈل کی ایویلیوایشن مکمل کر لی ہے۔ یہ ایک اہم قدم ہے تاکہ یہ یقینی بنایا جا سکے کہ آپ کے AI ماڈلز نہ صرف اچھی کارکردگی دکھائیں بلکہ Microsoft کے ذمہ دار AI اصولوں کے مطابق بھی ہوں، اور قابل اعتماد AI ایپلیکیشنز بنانے میں مدد کریں۔

![آرکیٹیکچر۔](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.ur.png)

## Azure وسائل کو صاف کریں

اپنے Azure وسائل کو صاف کریں تاکہ آپ کے اکاؤنٹ پر اضافی چارجز نہ آئیں۔ Azure پورٹل پر جائیں اور درج ذیل وسائل کو حذف کریں:

- Azure Machine learning ریسورس۔
- Azure Machine learning ماڈل اینڈپوائنٹ۔
- Azure AI Foundry پروجیکٹ ریسورس۔
- Azure AI Foundry Prompt flow ریسورس۔

### اگلے اقدامات

#### دستاویزات

- [ذمہ دار AI ڈیش بورڈ کا استعمال کرتے ہوئے AI سسٹمز کا جائزہ لیں](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)  
- [جنریٹو AI کے لیے ایویلیوایشن اور مانیٹرنگ میٹرکس](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)  
- [Azure AI Foundry دستاویزات](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)  
- [Prompt flow دستاویزات](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### تربیتی مواد

- [Microsoft کے ذمہ دار AI طریقے کا تعارف](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)  
- [Azure AI Foundry کا تعارف](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### حوالہ

- [ذمہ دار AI کیا ہے؟](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)  
- [Azure AI میں نئے ٹولز کا اعلان تاکہ زیادہ محفوظ اور قابل اعتماد جنریٹو AI ایپلیکیشنز بنائی جا سکیں](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)  
- [جنریٹو AI ایپلیکیشنز کی ایویلیوایشن](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)  

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی بھرپور کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔