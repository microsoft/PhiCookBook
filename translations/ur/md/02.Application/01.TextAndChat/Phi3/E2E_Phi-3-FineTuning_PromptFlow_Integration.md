<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-07-17T00:09:16+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "ur"
}
-->
# Fine-tune اور Prompt flow کے ساتھ custom Phi-3 ماڈلز کو انٹیگریٹ کریں

یہ end-to-end (E2E) نمونہ Microsoft Tech Community کی گائیڈ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" پر مبنی ہے۔ یہ custom Phi-3 ماڈلز کو fine-tune کرنے، deploy کرنے، اور Prompt flow کے ساتھ انٹیگریٹ کرنے کے عمل کا تعارف کراتا ہے۔

## جائزہ

اس E2E نمونے میں، آپ سیکھیں گے کہ Phi-3 ماڈل کو کیسے fine-tune کیا جائے اور اسے Prompt flow کے ساتھ کیسے انٹیگریٹ کیا جائے۔ Azure Machine Learning اور Prompt flow کا استعمال کرتے ہوئے، آپ custom AI ماڈلز کو deploy اور استعمال کرنے کے لیے ایک ورک فلو قائم کریں گے۔ یہ E2E نمونہ تین منظرناموں میں تقسیم ہے:

**منظرنامہ 1: Azure وسائل سیٹ اپ کریں اور fine-tuning کی تیاری کریں**

**منظرنامہ 2: Phi-3 ماڈل کو fine-tune کریں اور Azure Machine Learning Studio میں deploy کریں**

**منظرنامہ 3: Prompt flow کے ساتھ انٹیگریٹ کریں اور اپنے custom ماڈل کے ساتھ چیٹ کریں**

یہاں اس E2E نمونے کا ایک جائزہ دیا گیا ہے۔

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468cf3bbb3158cf273380cbdf7fcec042c7328e1559c6b2e2632.ur.png)

### فہرست مضامین

1. **[منظرنامہ 1: Azure وسائل سیٹ اپ کریں اور fine-tuning کی تیاری کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace بنائیں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription میں GPU کوٹہ کی درخواست کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [رول اسائنمنٹ شامل کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [پروجیکٹ سیٹ اپ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [fine-tuning کے لیے ڈیٹا سیٹ تیار کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[منظرنامہ 2: Phi-3 ماڈل کو fine-tune کریں اور Azure Machine Learning Studio میں deploy کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI سیٹ اپ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 ماڈل کو fine-tune کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [fine-tuned ماڈل کو deploy کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[منظرنامہ 3: Prompt flow کے ساتھ انٹیگریٹ کریں اور اپنے custom ماڈل کے ساتھ چیٹ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [custom Phi-3 ماڈل کو Prompt flow کے ساتھ انٹیگریٹ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [اپنے custom ماڈل کے ساتھ چیٹ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## منظرنامہ 1: Azure وسائل سیٹ اپ کریں اور fine-tuning کی تیاری کریں

### Azure Machine Learning Workspace بنائیں

1. پورٹل صفحے کے اوپر **search bar** میں *azure machine learning* ٹائپ کریں اور ظاہر ہونے والے اختیارات میں سے **Azure Machine Learning** منتخب کریں۔

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c600d87008fb78206d2cf90c0b920c231618a8ec8baaa6f46c3.ur.png)

1. نیویگیشن مینو سے **+ Create** منتخب کریں۔

1. نیویگیشن مینو سے **New workspace** منتخب کریں۔

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4fbb808d1bbcd92962692b1fa687f4c5d3952f453177825bc.ur.png)

1. درج ذیل کام انجام دیں:

    - اپنی Azure **Subscription** منتخب کریں۔
    - استعمال کے لیے **Resource group** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - **Workspace Name** درج کریں۔ یہ منفرد ہونا چاہیے۔
    - وہ **Region** منتخب کریں جہاں آپ کام کرنا چاہتے ہیں۔
    - استعمال کے لیے **Storage account** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - استعمال کے لیے **Key vault** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - استعمال کے لیے **Application insights** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - استعمال کے لیے **Container registry** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb141b9e8c16f31834e82e831275bd9faad0b70343f46255de.ur.png)

1. **Review + Create** منتخب کریں۔

1. **Create** منتخب کریں۔

### Azure Subscription میں GPU کوٹہ کی درخواست کریں

اس E2E نمونے میں، آپ fine-tuning کے لیے *Standard_NC24ads_A100_v4 GPU* استعمال کریں گے، جس کے لیے کوٹہ کی درخواست ضروری ہے، اور deployment کے لیے *Standard_E4s_v3* CPU استعمال کریں گے، جس کے لیے کوٹہ کی درخواست ضروری نہیں ہے۔

> [!NOTE]
>
> صرف Pay-As-You-Go سبسکرپشنز (معیاری سبسکرپشن کی قسم) GPU الاٹمنٹ کے اہل ہیں؛ benefit سبسکرپشنز فی الحال سپورٹ نہیں کی جاتیں۔
>
> جو لوگ benefit سبسکرپشنز (جیسے Visual Studio Enterprise Subscription) استعمال کر رہے ہیں یا جو fine-tuning اور deployment کے عمل کو جلدی آزمانا چاہتے ہیں، اس ٹیوٹوریل میں CPU کے ساتھ کم سے کم ڈیٹا سیٹ کے ذریعے fine-tuning کے لیے بھی رہنمائی فراہم کی گئی ہے۔ تاہم، یہ بات اہم ہے کہ GPU کے ساتھ بڑے ڈیٹا سیٹس استعمال کرنے پر fine-tuning کے نتائج نمایاں طور پر بہتر ہوتے ہیں۔

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. *Standard NCADSA100v4 Family* کوٹہ کی درخواست کے لیے درج ذیل کام کریں:

    - بائیں طرف کے ٹیب سے **Quota** منتخب کریں۔
    - استعمال کے لیے **Virtual machine family** منتخب کریں۔ مثال کے طور پر، **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** منتخب کریں، جس میں *Standard_NC24ads_A100_v4* GPU شامل ہے۔
    - نیویگیشن مینو سے **Request quota** منتخب کریں۔

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab8348515fcfba9d0279114f04065df8bd6fb78e3d3704e627545.ur.png)

    - Request quota صفحے میں، وہ **New cores limit** درج کریں جو آپ استعمال کرنا چاہتے ہیں۔ مثال کے طور پر، 24۔
    - Request quota صفحے میں، GPU کوٹہ کی درخواست کے لیے **Submit** منتخب کریں۔

> [!NOTE]
> آپ اپنی ضروریات کے مطابق GPU یا CPU منتخب کرنے کے لیے [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) دستاویز کا حوالہ دے سکتے ہیں۔

### رول اسائنمنٹ شامل کریں

اپنے ماڈلز کو fine-tune اور deploy کرنے کے لیے، آپ کو پہلے ایک User Assigned Managed Identity (UAI) بنانی ہوگی اور اسے مناسب اجازتیں دینی ہوں گی۔ یہ UAI deployment کے دوران authentication کے لیے استعمال ہوگی۔

#### User Assigned Managed Identity (UAI) بنائیں

1. پورٹل صفحے کے اوپر **search bar** میں *managed identities* ٹائپ کریں اور ظاہر ہونے والے اختیارات میں سے **Managed Identities** منتخب کریں۔

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8a95d6e7762f1b087275a9634677f0a4e355717550ace3c02.ur.png)

1. **+ Create** منتخب کریں۔

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a8c70af922bf28a573c0744fb642f8228d62214b010a070d9.ur.png)

1. درج ذیل کام انجام دیں:

    - اپنی Azure **Subscription** منتخب کریں۔
    - استعمال کے لیے **Resource group** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - وہ **Region** منتخب کریں جہاں آپ کام کرنا چاہتے ہیں۔
    - **Name** درج کریں۔ یہ منفرد ہونا چاہیے۔

1. **Review + create** منتخب کریں۔

1. **+ Create** منتخب کریں۔

#### Managed Identity کو Contributor رول اسائنمنٹ دیں

1. اس Managed Identity resource پر جائیں جو آپ نے بنائی ہے۔

1. بائیں طرف کے ٹیب سے **Azure role assignments** منتخب کریں۔

1. نیویگیشن مینو سے **+Add role assignment** منتخب کریں۔

1. Add role assignment صفحے میں، درج ذیل کام کریں:
    - **Scope** کو **Resource group** پر سیٹ کریں۔
    - اپنی Azure **Subscription** منتخب کریں۔
    - استعمال کے لیے **Resource group** منتخب کریں۔
    - **Role** کو **Contributor** منتخب کریں۔

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e008e224cf336687c04c9fe24740e47e34ce041b50b47e0ed1.ur.png)

1. **Save** منتخب کریں۔

#### Managed Identity کو Storage Blob Data Reader رول اسائنمنٹ دیں

1. پورٹل صفحے کے اوپر **search bar** میں *storage accounts* ٹائپ کریں اور ظاہر ہونے والے اختیارات میں سے **Storage accounts** منتخب کریں۔

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49bcd9cce3ffd1b6218afb6e5c3700b628da7b7c294be71b911.ur.png)

1. اس storage account کو منتخب کریں جو آپ کے Azure Machine Learning workspace سے منسلک ہے۔ مثال کے طور پر، *finetunephistorage*۔

1. Add role assignment صفحے پر جانے کے لیے درج ذیل کام کریں:

    - اس Azure Storage account پر جائیں جو آپ نے بنایا ہے۔
    - بائیں طرف کے ٹیب سے **Access Control (IAM)** منتخب کریں۔
    - نیویگیشن مینو سے **+ Add** منتخب کریں۔
    - نیویگیشن مینو سے **Add role assignment** منتخب کریں۔

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0ae84790d65dc5726a9b57c496d916b8700d41e0b3b468451.ur.png)

1. Add role assignment صفحے میں، درج ذیل کام کریں:

    - Role صفحے میں، **search bar** میں *Storage Blob Data Reader* ٹائپ کریں اور ظاہر ہونے والے اختیارات میں سے **Storage Blob Data Reader** منتخب کریں۔
    - Role صفحے میں، **Next** منتخب کریں۔
    - Members صفحے میں، **Assign access to** کے تحت **Managed identity** منتخب کریں۔
    - Members صفحے میں، **+ Select members** منتخب کریں۔
    - Select managed identities صفحے میں، اپنی Azure **Subscription** منتخب کریں۔
    - Select managed identities صفحے میں، **Managed identity** کو **Manage Identity** منتخب کریں۔
    - Select managed identities صفحے میں، وہ Manage Identity منتخب کریں جو آپ نے بنائی ہے۔ مثال کے طور پر، *finetunephi-managedidentity*۔
    - Select managed identities صفحے میں، **Select** منتخب کریں۔

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df788963e1dc0a68c39ee297363aabe979b487c60b3037662f.ur.png)

1. **Review + assign** منتخب کریں۔

#### Managed Identity کو AcrPull رول اسائنمنٹ دیں

1. پورٹل صفحے کے اوپر **search bar** میں *container registries* ٹائپ کریں اور ظاہر ہونے والے اختیارات میں سے **Container registries** منتخب کریں۔

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c64c0f778633c652ce08e4ac28f142a17afc10de81bb8c336.ur.png)

1. اس container registry کو منتخب کریں جو Azure Machine Learning workspace سے منسلک ہے۔ مثال کے طور پر، *finetunephicontainerregistries*

1. Add role assignment صفحے پر جانے کے لیے درج ذیل کام کریں:

    - بائیں طرف کے ٹیب سے **Access Control (IAM)** منتخب کریں۔
    - نیویگیشن مینو سے **+ Add** منتخب کریں۔
    - نیویگیشن مینو سے **Add role assignment** منتخب کریں۔

1. Add role assignment صفحے میں، درج ذیل کام کریں:

    - Role صفحے میں، **search bar** میں *AcrPull* ٹائپ کریں اور ظاہر ہونے والے اختیارات میں سے **AcrPull** منتخب کریں۔
    - Role صفحے میں، **Next** منتخب کریں۔
    - Members صفحے میں، **Assign access to** کے تحت **Managed identity** منتخب کریں۔
    - Members صفحے میں، **+ Select members** منتخب کریں۔
    - Select managed identities صفحے میں، اپنی Azure **Subscription** منتخب کریں۔
    - Select managed identities صفحے میں، **Managed identity** کو **Manage Identity** منتخب کریں۔
    - Select managed identities صفحے میں، وہ Manage Identity منتخب کریں جو آپ نے بنائی ہے۔ مثال کے طور پر، *finetunephi-managedidentity*۔
    - Select managed identities صفحے میں، **Select** منتخب کریں۔
    - **Review + assign** منتخب کریں۔

### پروجیکٹ سیٹ اپ کریں

اب، آپ ایک فولڈر بنائیں گے جہاں کام کریں گے اور ایک virtual environment سیٹ اپ کریں گے تاکہ ایک ایسا پروگرام تیار کیا جا سکے جو صارفین کے ساتھ تعامل کرے اور Azure Cosmos DB میں محفوظ چیٹ ہسٹری کو استعمال کرتے ہوئے جوابات فراہم کرے۔

#### کام کرنے کے لیے فولڈر بنائیں

1. ایک ٹرمینل ونڈو کھولیں اور درج ذیل کمانڈ ٹائپ کریں تاکہ ڈیفالٹ راستے میں *finetune-phi* نامی فولڈر بنایا جا سکے۔

    ```console
    mkdir finetune-phi
    ```

1. اپنے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ آپ اس *finetune-phi* فولڈر میں جا سکیں جو آپ نے بنایا ہے۔

    ```console
    cd finetune-phi
    ```

#### virtual environment بنائیں

1. اپنے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ *.venv* نامی virtual environment بنایا جا سکے۔

    ```console
    python -m venv .venv
    ```

1. اپنے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ virtual environment کو فعال کیا جا سکے۔

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> اگر یہ کامیاب ہو گیا ہے، تو آپ کو کمانڈ پرامپٹ سے پہلے *(.venv)* نظر آنا چاہیے۔
#### مطلوبہ پیکجز انسٹال کریں

1. مطلوبہ پیکجز انسٹال کرنے کے لیے اپنے ٹرمینل میں درج ذیل کمانڈز ٹائپ کریں۔

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### پروجیکٹ فائلز بنائیں

اس مشق میں، آپ ہمارے پروجیکٹ کے لیے ضروری فائلز بنائیں گے۔ ان فائلز میں ڈیٹا سیٹ ڈاؤن لوڈ کرنے، Azure Machine Learning ماحول سیٹ اپ کرنے، Phi-3 ماڈل کو فائن ٹیون کرنے، اور فائن ٹیون کیے گئے ماڈل کو ڈیپلائے کرنے کے اسکرپٹس شامل ہیں۔ آپ ایک *conda.yml* فائل بھی بنائیں گے تاکہ فائن ٹیوننگ کا ماحول ترتیب دیا جا سکے۔

اس مشق میں آپ:

- *download_dataset.py* فائل بنائیں گے تاکہ ڈیٹا سیٹ ڈاؤن لوڈ کیا جا سکے۔
- *setup_ml.py* فائل بنائیں گے تاکہ Azure Machine Learning ماحول سیٹ اپ کیا جا سکے۔
- *finetuning_dir* فولڈر میں *fine_tune.py* فائل بنائیں گے تاکہ ڈیٹا سیٹ استعمال کرتے ہوئے Phi-3 ماڈل کو فائن ٹیون کیا جا سکے۔
- فائن ٹیوننگ ماحول ترتیب دینے کے لیے *conda.yml* فائل بنائیں گے۔
- فائن ٹیون کیے گئے ماڈل کو ڈیپلائے کرنے کے لیے *deploy_model.py* فائل بنائیں گے۔
- فائن ٹیون کیے گئے ماڈل کو Prompt flow کے ذریعے انٹیگریٹ اور چلانے کے لیے *integrate_with_promptflow.py* فائل بنائیں گے۔
- Prompt flow کے ورک فلو ڈھانچے کے لیے flow.dag.yml فائل بنائیں گے۔
- Azure کی معلومات درج کرنے کے لیے *config.py* فائل بنائیں گے۔

> [!NOTE]
>
> مکمل فولڈر اسٹرکچر:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. **Visual Studio Code** کھولیں۔

1. مینو بار سے **File** منتخب کریں۔

1. **Open Folder** منتخب کریں۔

1. *finetune-phi* فولڈر منتخب کریں جو آپ نے بنایا ہے، جو کہ *C:\Users\yourUserName\finetune-phi* پر واقع ہے۔

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639c12e7da258ac8b3deca260786edb07598e206725cd1593ce.ur.png)

1. Visual Studio Code کے بائیں پین میں، رائٹ کلک کریں اور **New File** منتخب کریں، پھر *download_dataset.py* نامی نئی فائل بنائیں۔

1. Visual Studio Code کے بائیں پین میں، رائٹ کلک کریں اور **New File** منتخب کریں، پھر *setup_ml.py* نامی نئی فائل بنائیں۔

1. Visual Studio Code کے بائیں پین میں، رائٹ کلک کریں اور **New File** منتخب کریں، پھر *deploy_model.py* نامی نئی فائل بنائیں۔

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a398766a39eac9f15240a9a4da566bd8dca86f471e78eadc69e.ur.png)

1. Visual Studio Code کے بائیں پین میں، رائٹ کلک کریں اور **New Folder** منتخب کریں، پھر *finetuning_dir* نامی نیا فولڈر بنائیں۔

1. *finetuning_dir* فولڈر میں، *fine_tune.py* نامی نئی فائل بنائیں۔

#### *conda.yml* فائل بنائیں اور ترتیب دیں

1. Visual Studio Code کے بائیں پین میں، رائٹ کلک کریں اور **New File** منتخب کریں، پھر *conda.yml* نامی نئی فائل بنائیں۔

1. *conda.yml* فائل میں درج ذیل کوڈ شامل کریں تاکہ Phi-3 ماڈل کے لیے فائن ٹیوننگ ماحول ترتیب دیا جا سکے۔

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### *config.py* فائل بنائیں اور ترتیب دیں

1. Visual Studio Code کے بائیں پین میں، رائٹ کلک کریں اور **New File** منتخب کریں، پھر *config.py* نامی نئی فائل بنائیں۔

1. *config.py* فائل میں اپنی Azure کی معلومات شامل کرنے کے لیے درج ذیل کوڈ شامل کریں۔

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Azure کے ماحول کے متغیرات شامل کریں

1. Azure Subscription ID شامل کرنے کے لیے درج ذیل کام کریں:

    - پورٹل پیج کے اوپر **search bar** میں *subscriptions* ٹائپ کریں اور ظاہر ہونے والے آپشنز میں سے **Subscriptions** منتخب کریں۔
    - وہ Azure Subscription منتخب کریں جو آپ استعمال کر رہے ہیں۔
    - اپنی Subscription ID کو کاپی کریں اور *config.py* فائل میں پیسٹ کریں۔

    ![Find subscription id.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637e01163bfdd2a606e7d06f05455ab56e05cb5107e938e7a90.ur.png)

1. Azure Workspace Name شامل کرنے کے لیے درج ذیل کام کریں:

    - Azure Machine Learning resource پر جائیں جو آپ نے بنایا ہے۔
    - اپنا اکاؤنٹ نام کاپی کریں اور *config.py* فائل میں پیسٹ کریں۔

    ![Find Azure Machine Learning name.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a702b1bb5e9d8e9f5e5424abe066a0ff310da980582e65721f.ur.png)

1. Azure Resource Group Name شامل کرنے کے لیے درج ذیل کام کریں:

    - Azure Machine Learning resource پر جائیں جو آپ نے بنایا ہے۔
    - اپنا Azure Resource Group Name کاپی کریں اور *config.py* فائل میں پیسٹ کریں۔

    ![Find resource group name.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a399243d7c94d5aabd86070ab6535d3cf2ec38c78538626666.ur.png)

2. Azure Managed Identity name شامل کرنے کے لیے درج ذیل کام کریں:

    - Managed Identities resource پر جائیں جو آپ نے بنایا ہے۔
    - اپنا Azure Managed Identity name کاپی کریں اور *config.py* فائل میں پیسٹ کریں۔

    ![Find UAI.](../../../../../../translated_images/01-17-find-uai.3529464f534998271ea7c5aebafa887051567417f3b4244ff58fdd443192b6d7.ur.png)

### فائن ٹیوننگ کے لیے ڈیٹا سیٹ تیار کریں

اس مشق میں، آپ *download_dataset.py* فائل چلائیں گے تاکہ *ULTRACHAT_200k* ڈیٹا سیٹس اپنے لوکل ماحول میں ڈاؤن لوڈ کر سکیں۔ پھر آپ اس ڈیٹا سیٹ کو Azure Machine Learning میں Phi-3 ماڈل کو فائن ٹیون کرنے کے لیے استعمال کریں گے۔

#### *download_dataset.py* کے ذریعے اپنا ڈیٹا سیٹ ڈاؤن لوڈ کریں

1. Visual Studio Code میں *download_dataset.py* فائل کھولیں۔

1. *download_dataset.py* میں درج ذیل کوڈ شامل کریں۔

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **کم سے کم ڈیٹا سیٹ کے ساتھ CPU پر فائن ٹیوننگ کے لیے رہنمائی**
>
> اگر آپ CPU استعمال کر کے فائن ٹیون کرنا چاہتے ہیں، تو یہ طریقہ ان لوگوں کے لیے بہترین ہے جن کے پاس فائدہ مند سبسکرپشنز ہیں (جیسے Visual Studio Enterprise Subscription) یا جو فائن ٹیوننگ اور ڈیپلائمنٹ کے عمل کو جلدی ٹیسٹ کرنا چاہتے ہیں۔
>
> `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` کو `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')` سے بدل دیں۔
>

1. اپنے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ اسکرپٹ چلائیں اور ڈیٹا سیٹ اپنے لوکل ماحول میں ڈاؤن لوڈ کریں۔

    ```console
    python download_data.py
    ```

1. تصدیق کریں کہ ڈیٹا سیٹس کامیابی سے آپ کے لوکل *finetune-phi/data* ڈائریکٹری میں محفوظ ہو گئے ہیں۔

> [!NOTE]
>
> **ڈیٹا سیٹ کا سائز اور فائن ٹیوننگ کا وقت**
>
> اس E2E نمونے میں، آپ صرف ڈیٹا سیٹ کا 1% (`train_sft[:1%]`) استعمال کر رہے ہیں۔ اس سے ڈیٹا کی مقدار بہت کم ہو جاتی ہے، جس سے اپلوڈ اور فائن ٹیوننگ دونوں کے عمل تیز ہو جاتے ہیں۔ آپ تربیتی وقت اور ماڈل کی کارکردگی کے درمیان مناسب توازن تلاش کرنے کے لیے فیصد کو ایڈجسٹ کر سکتے ہیں۔ ڈیٹا سیٹ کے چھوٹے حصے کا استعمال فائن ٹیوننگ کے لیے درکار وقت کو کم کرتا ہے، جس سے یہ عمل E2E نمونے کے لیے زیادہ قابلِ انتظام ہو جاتا ہے۔

## منظر نامہ 2: Phi-3 ماڈل کو فائن ٹیون کریں اور Azure Machine Learning Studio میں ڈیپلائے کریں

### Azure CLI سیٹ اپ کریں

آپ کو اپنے ماحول کی تصدیق کے لیے Azure CLI سیٹ اپ کرنا ہوگا۔ Azure CLI آپ کو کمانڈ لائن سے براہ راست Azure وسائل کا انتظام کرنے کی اجازت دیتا ہے اور Azure Machine Learning کو ان وسائل تک رسائی کے لیے ضروری اسناد فراہم کرتا ہے۔ شروع کرنے کے لیے [Azure CLI انسٹال کریں](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. ٹرمینل ونڈو کھولیں اور اپنے Azure اکاؤنٹ میں لاگ ان کرنے کے لیے درج ذیل کمانڈ ٹائپ کریں۔

    ```console
    az login
    ```

1. اپنے Azure اکاؤنٹ کو منتخب کریں۔

1. اپنی Azure سبسکرپشن منتخب کریں۔

    ![Find resource group name.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a8792c687d36e4fc4f4ee37fd76640e6e4e5aed3329513f2328.ur.png)

> [!TIP]
>
> اگر آپ کو Azure میں سائن ان کرنے میں دشواری ہو رہی ہے، تو ڈیوائس کوڈ استعمال کرنے کی کوشش کریں۔ ٹرمینل ونڈو کھولیں اور اپنے Azure اکاؤنٹ میں سائن ان کرنے کے لیے درج ذیل کمانڈ ٹائپ کریں:
>
> ```console
> az login --use-device-code
> ```
>

### Phi-3 ماڈل کو فائن ٹیون کریں

اس مشق میں، آپ فراہم کردہ ڈیٹا سیٹ کا استعمال کرتے ہوئے Phi-3 ماڈل کو فائن ٹیون کریں گے۔ سب سے پہلے، آپ *fine_tune.py* فائل میں فائن ٹیوننگ کا عمل متعین کریں گے۔ پھر، آپ Azure Machine Learning ماحول کو ترتیب دیں گے اور *setup_ml.py* فائل چلا کر فائن ٹیوننگ کا عمل شروع کریں گے۔ یہ اسکرپٹ یقینی بناتا ہے کہ فائن ٹیوننگ Azure Machine Learning ماحول میں ہو۔

*setup_ml.py* چلانے سے، آپ Azure Machine Learning ماحول میں فائن ٹیوننگ کا عمل شروع کریں گے۔

#### *fine_tune.py* فائل میں کوڈ شامل کریں

1. *finetuning_dir* فولڈر میں جائیں اور Visual Studio Code میں *fine_tune.py* فائل کھولیں۔

1. *fine_tune.py* میں درج ذیل کوڈ شامل کریں۔

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. *fine_tune.py* فائل کو محفوظ کریں اور بند کریں۔

> [!TIP]
> **آپ Phi-3.5 ماڈل کو بھی فائن ٹیون کر سکتے ہیں**
>
> *fine_tune.py* فائل میں، آپ `pretrained_model_name` کو `"microsoft/Phi-3-mini-4k-instruct"` سے کسی بھی ماڈل کے نام میں تبدیل کر سکتے ہیں جسے آپ فائن ٹیون کرنا چاہتے ہیں۔ مثال کے طور پر، اگر آپ اسے `"microsoft/Phi-3.5-mini-instruct"` میں بدلتے ہیں، تو آپ Phi-3.5-mini-instruct ماڈل کو فائن ٹیون کرنے کے لیے استعمال کریں گے۔ اپنی پسند کا ماڈل نام تلاش کرنے اور استعمال کرنے کے لیے [Hugging Face](https://huggingface.co/) پر جائیں، ماڈل تلاش کریں، اور اس کا نام اپنی اسکرپٹ میں `pretrained_model_name` فیلڈ میں کاپی پیسٹ کریں۔
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tune Phi-3.5.":::
>

#### *setup_ml.py* فائل میں کوڈ شامل کریں

1. Visual Studio Code میں *setup_ml.py* فائل کھولیں۔

1. *setup_ml.py* میں درج ذیل کوڈ شامل کریں۔

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, اور `LOCATION` کو اپنی مخصوص تفصیلات سے بدلیں۔

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **کم سے کم ڈیٹا سیٹ کے ساتھ CPU پر فائن ٹیوننگ کے لیے رہنمائی**
>
> اگر آپ CPU استعمال کر کے فائن ٹیون کرنا چاہتے ہیں، تو یہ طریقہ ان لوگوں کے لیے بہترین ہے جن کے پاس فائدہ مند سبسکرپشنز ہیں (جیسے Visual Studio Enterprise Subscription) یا جو فائن ٹیوننگ اور ڈیپلائمنٹ کے عمل کو جلدی ٹیسٹ کرنا چاہتے ہیں۔
>
> 1. *setup_ml* فائل کھولیں۔
> 1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, اور `DOCKER_IMAGE_NAME` کو درج ذیل سے بدلیں۔ اگر آپ کے پاس *Standard_E16s_v3* تک رسائی نہیں ہے، تو آپ CPU انسٹنس کے مساوی استعمال کر سکتے ہیں یا نیا کوٹہ درخواست کر سکتے ہیں۔
> 1. `LOCATION` کو اپنی مخصوص تفصیلات سے بدلیں۔
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. *setup_ml.py* اسکرپٹ چلانے کے لیے درج ذیل کمانڈ ٹائپ کریں تاکہ Azure Machine Learning میں فائن ٹیوننگ کا عمل شروع ہو۔

    ```python
    python setup_ml.py
    ```

1. اس مشق میں، آپ نے کامیابی سے Azure Machine Learning کا استعمال کرتے ہوئے Phi-3 ماڈل کو فائن ٹیون کیا۔ *setup_ml.py* اسکرپٹ چلانے سے، آپ نے Azure Machine Learning ماحول سیٹ اپ کیا اور *fine_tune.py* فائل میں متعین فائن ٹیوننگ کا عمل شروع کیا۔ براہ کرم نوٹ کریں کہ فائن ٹیوننگ کا عمل کافی وقت لے سکتا ہے۔ `python setup_ml.py` کمانڈ چلانے کے بعد، آپ کو عمل مکمل ہونے تک انتظار کرنا ہوگا۔ آپ ٹرمینل میں دیے گئے لنک کے ذریعے Azure Machine Learning پورٹل میں فائن ٹیوننگ جاب کی حالت مانیٹر کر سکتے ہیں۔

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871ee8ba32fa508cc4018c0f04e51ad14b95c421ad77151f768f.ur.png)

### فائن ٹیون کیے گئے ماڈل کو ڈیپلائے کریں

فائن ٹیون کیے گئے Phi-3 ماڈل کو Prompt Flow کے ساتھ انٹیگریٹ کرنے کے لیے، آپ کو ماڈل کو ڈیپلائے کرنا ہوگا تاکہ یہ ریئل ٹائم انفرنس کے لیے دستیاب ہو۔ اس عمل میں ماڈل کی رجسٹریشن، آن لائن اینڈ پوائنٹ بنانا، اور ماڈل کی تعیناتی شامل ہے۔

#### ڈیپلائے کرنے کے لیے ماڈل کا نام، اینڈ پوائنٹ کا نام، اور ڈیپلائمنٹ کا نام سیٹ کریں

1. *config.py* فائل کھولیں۔

1. `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` کو اپنی پسند کے ماڈل کے نام سے بدلیں۔

1. `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` کو اپنی پسند کے اینڈ پوائنٹ کے نام سے بدلیں۔

1. `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` کو اپنی پسند کے ڈیپلائمنٹ کے نام سے بدلیں۔

#### *deploy_model.py* فائل میں کوڈ شامل کریں

*deploy_model.py* فائل چلانے سے پورا ڈیپلائمنٹ عمل خودکار ہو جاتا ہے۔ یہ ماڈل کو رجسٹر کرتا ہے، اینڈ پوائنٹ بناتا ہے، اور config.py فائل میں دی گئی ترتیبات کے مطابق ڈیپلائمنٹ کرتا ہے، جن میں ماڈل کا نام، اینڈ پوائنٹ کا نام، اور ڈیپلائمنٹ کا نام شامل ہیں۔

1. Visual Studio Code میں *deploy_model.py* فائل کھولیں۔

1. *deploy_model.py* میں درج ذیل کوڈ شامل کریں۔

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. `JOB_NAME` حاصل کرنے کے لیے درج ذیل کام کریں:

    - Azure Machine Learning resource پر جائیں جو آپ نے بنایا ہے۔
    - **Studio web URL** منتخب کریں تاکہ Azure Machine Learning ورک اسپیس کھلے۔
    - بائیں طرف کے ٹیب سے **Jobs** منتخب کریں۔
    - فائن ٹیوننگ کے لیے تجربہ منتخب کریں، مثلاً *finetunephi*۔
    - وہ جاب منتخب کریں جو آپ نے بنائی ہے۔
- اپنے کام کا نام *deploy_model.py* فائل میں `JOB_NAME = "your-job-name"` کے اندر کاپی اور پیسٹ کریں۔

1. `COMPUTE_INSTANCE_TYPE` کو اپنی مخصوص تفصیلات سے تبدیل کریں۔

1. Azure Machine Learning میں تعیناتی کے عمل کو شروع کرنے کے لیے *deploy_model.py* اسکرپٹ چلانے کے لیے درج ذیل کمانڈ ٹائپ کریں۔

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> اپنے اکاؤنٹ پر اضافی چارجز سے بچنے کے لیے، Azure Machine Learning ورک اسپیس میں بنائے گئے endpoint کو حذف کرنا یقینی بنائیں۔
>

#### Azure Machine Learning ورک اسپیس میں تعیناتی کی صورتحال چیک کریں

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. اس Azure Machine Learning ورک اسپیس پر جائیں جو آپ نے بنایا ہے۔

1. Azure Machine Learning ورک اسپیس کھولنے کے لیے **Studio web URL** منتخب کریں۔

1. بائیں طرف کے ٹیب سے **Endpoints** منتخب کریں۔

    ![Select endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff109f3b7a6b6e4e9689f99b2d7bf021b057f6c0ecbd1ba90c0.ur.png)

2. وہ endpoint منتخب کریں جو آپ نے بنایا ہے۔

    ![Select endpoints that you created.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4b726505fcfb7d262b0510de029dcbaf36422bb75b77f25dd.ur.png)

3. اس صفحے پر، آپ تعیناتی کے عمل کے دوران بنائے گئے endpoints کا انتظام کر سکتے ہیں۔

## منظر نامہ 3: Prompt flow کے ساتھ انٹیگریٹ کریں اور اپنے کسٹم ماڈل سے بات کریں

### کسٹم Phi-3 ماڈل کو Prompt flow کے ساتھ انٹیگریٹ کریں

اپنے fine-tuned ماڈل کی کامیاب تعیناتی کے بعد، اب آپ اسے Prompt flow کے ساتھ انٹیگریٹ کر سکتے ہیں تاکہ اپنے ماڈل کو حقیقی وقت کی ایپلیکیشنز میں استعمال کریں، جو آپ کے کسٹم Phi-3 ماڈل کے ساتھ مختلف انٹرایکٹو کاموں کو ممکن بناتا ہے۔

#### fine-tuned Phi-3 ماڈل کی api key اور endpoint uri سیٹ کریں

1. اس Azure Machine Learning ورک اسپیس پر جائیں جو آپ نے بنایا ہے۔
1. بائیں طرف کے ٹیب سے **Endpoints** منتخب کریں۔
1. وہ endpoint منتخب کریں جو آپ نے بنایا ہے۔
1. نیویگیشن مینو سے **Consume** منتخب کریں۔
1. اپنی **REST endpoint** کو کاپی کریں اور *config.py* فائل میں `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` کی جگہ پیسٹ کریں۔
1. اپنی **Primary key** کو کاپی کریں اور *config.py* فائل میں `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` کی جگہ پیسٹ کریں۔

    ![Copy api key and endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53bf44401e184f65a0a088daa76a65f5df5eb4489ae40b890f6.ur.png)

#### *flow.dag.yml* فائل میں کوڈ شامل کریں

1. Visual Studio Code میں *flow.dag.yml* فائل کھولیں۔

1. *flow.dag.yml* میں درج ذیل کوڈ شامل کریں۔

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

#### *integrate_with_promptflow.py* فائل میں کوڈ شامل کریں

1. Visual Studio Code میں *integrate_with_promptflow.py* فائل کھولیں۔

1. *integrate_with_promptflow.py* میں درج ذیل کوڈ شامل کریں۔

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
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
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### اپنے کسٹم ماڈل سے بات کریں

1. Azure Machine Learning میں تعیناتی کے عمل کو شروع کرنے کے لیے *deploy_model.py* اسکرپٹ چلانے کے لیے درج ذیل کمانڈ ٹائپ کریں۔

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. نتائج کی ایک مثال یہ ہے: اب آپ اپنے کسٹم Phi-3 ماڈل سے بات کر سکتے ہیں۔ مشورہ دیا جاتا ہے کہ fine-tuning کے لیے استعمال ہونے والے ڈیٹا کی بنیاد پر سوالات پوچھیں۔

    ![Prompt flow example.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6412447c9786c562be969a8c3b19791eadffce725fa84f014.ur.png)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔