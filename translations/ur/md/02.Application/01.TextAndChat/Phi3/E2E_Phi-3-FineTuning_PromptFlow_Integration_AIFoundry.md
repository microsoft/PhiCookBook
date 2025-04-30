<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ed86d361ac6d4cc8bfb47428e6a2a247",
  "translation_date": "2025-04-03T07:27:27+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ur"
}
-->
# اپنی مرضی کے Phi-3 ماڈلز کو Azure AI Foundry میں Prompt flow کے ساتھ بہتر بنائیں اور ضم کریں

یہ مکمل گائیڈ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" پر مبنی ہے جو Microsoft Tech Community سے لیا گیا ہے۔ یہ گائیڈ آپ کو Phi-3 ماڈلز کو بہتر بنانے، ڈیپلائے کرنے اور Azure AI Foundry میں Prompt flow کے ساتھ ضم کرنے کے مراحل سے آگاہ کرتا ہے۔  
اس گائیڈ کے برعکس، "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)"، جو لوکل کوڈ چلانے پر مرکوز تھا، یہ ٹیوٹوریل مکمل طور پر Azure AI / ML Studio میں آپ کے ماڈل کو بہتر بنانے اور ضم کرنے پر مرکوز ہے۔

## جائزہ

اس مکمل گائیڈ میں، آپ سیکھیں گے کہ کس طرح Phi-3 ماڈل کو بہتر بنائیں اور Azure AI Foundry میں Prompt flow کے ساتھ ضم کریں۔ Azure AI / ML Studio کو استعمال کرتے ہوئے، آپ کسٹم AI ماڈلز کو ڈیپلائے اور استعمال کرنے کے لیے ایک ورک فلو قائم کریں گے۔ یہ گائیڈ تین منظرناموں میں تقسیم کیا گیا ہے:

**منظرنامہ 1: Azure وسائل کی ترتیب اور بہتر بنانے کے لیے تیاری**

**منظرنامہ 2: Phi-3 ماڈل کو بہتر بنائیں اور Azure Machine Learning Studio میں ڈیپلائے کریں**

**منظرنامہ 3: Prompt flow کے ساتھ ضم کریں اور Azure AI Foundry میں اپنے کسٹم ماڈل کے ساتھ چیٹ کریں**

یہ مکمل گائیڈ کا خلاصہ ہے:

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.ur.png)

### فہرست

1. **[منظرنامہ 1: Azure وسائل کی ترتیب اور بہتر بنانے کے لیے تیاری](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace بنائیں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription میں GPU کوٹہ کی درخواست کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [رول اسائنمنٹ شامل کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [پروجیکٹ ترتیب دیں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [بہتر بنانے کے لیے ڈیٹا سیٹ تیار کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[منظرنامہ 2: Phi-3 ماڈل کو بہتر بنائیں اور Azure Machine Learning Studio میں ڈیپلائے کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 ماڈل کو بہتر بنائیں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [بہتر بنائے گئے Phi-3 ماڈل کو ڈیپلائے کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[منظرنامہ 3: Prompt flow کے ساتھ ضم کریں اور Azure AI Foundry میں اپنے کسٹم ماڈل کے ساتھ چیٹ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [کسٹم Phi-3 ماڈل کو Prompt flow کے ساتھ ضم کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [اپنے کسٹم Phi-3 ماڈل کے ساتھ چیٹ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## منظرنامہ 1: Azure وسائل کی ترتیب اور بہتر بنانے کے لیے تیاری

### Azure Machine Learning Workspace بنائیں

1. **پورٹل پیج** کے اوپر سرچ بار میں *azure machine learning* ٹائپ کریں اور نظر آنے والے آپشنز میں سے **Azure Machine Learning** منتخب کریں۔

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.ur.png)

2. نیویگیشن مینو سے **+ Create** منتخب کریں۔

3. نیویگیشن مینو سے **New workspace** منتخب کریں۔

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.ur.png)

4. درج ذیل کام کریں:

    - اپنا Azure **Subscription** منتخب کریں۔
    - استعمال کرنے کے لیے **Resource group** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - **Workspace Name** درج کریں۔ یہ ایک منفرد ویلیو ہونی چاہیے۔
    - وہ **Region** منتخب کریں جسے آپ استعمال کرنا چاہتے ہیں۔
    - استعمال کرنے کے لیے **Storage account** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - استعمال کرنے کے لیے **Key vault** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - استعمال کرنے کے لیے **Application insights** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - استعمال کرنے کے لیے **Container registry** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.ur.png)

5. **Review + Create** منتخب کریں۔

6. **Create** منتخب کریں۔

### Azure Subscription میں GPU کوٹہ کی درخواست کریں

اس ٹیوٹوریل میں، آپ GPU استعمال کرتے ہوئے Phi-3 ماڈل کو بہتر بنائیں اور ڈیپلائے کریں گے۔ بہتر بنانے کے لیے، آپ *Standard_NC24ads_A100_v4* GPU استعمال کریں گے، جس کے لیے کوٹہ درخواست ضروری ہے۔ ڈیپلائے کرنے کے لیے، آپ *Standard_NC6s_v3* GPU استعمال کریں گے، جس کے لیے بھی کوٹہ درخواست ضروری ہے۔

> [!NOTE]
>
> صرف Pay-As-You-Go سبسکرپشنز (معیاری سبسکرپشن قسم) GPU الاٹمنٹ کے لیے اہل ہیں؛ بینیفٹ سبسکرپشنز فی الحال سپورٹ نہیں کی جاتی ہیں۔

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. *Standard NCADSA100v4 Family* کوٹہ کی درخواست کرنے کے لیے درج ذیل کام کریں:

    - **Quota** کو بائیں جانب ٹیب سے منتخب کریں۔
    - استعمال کرنے کے لیے **Virtual machine family** منتخب کریں۔ مثال کے طور پر، **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** منتخب کریں، جس میں *Standard_NC24ads_A100_v4* GPU شامل ہے۔
    - نیویگیشن مینو سے **Request quota** منتخب کریں۔

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.ur.png)

    - **Request quota** پیج کے اندر، وہ **New cores limit** درج کریں جو آپ استعمال کرنا چاہتے ہیں۔ مثال کے طور پر، 24۔
    - **Request quota** پیج کے اندر، **Submit** منتخب کریں تاکہ GPU کوٹہ کی درخواست کی جا سکے۔

1. *Standard NCSv3 Family* کوٹہ کی درخواست کرنے کے لیے درج ذیل کام کریں:

    - **Quota** کو بائیں جانب ٹیب سے منتخب کریں۔
    - استعمال کرنے کے لیے **Virtual machine family** منتخب کریں۔ مثال کے طور پر، **Standard NCSv3 Family Cluster Dedicated vCPUs** منتخب کریں، جس میں *Standard_NC6s_v3* GPU شامل ہے۔
    - نیویگیشن مینو سے **Request quota** منتخب کریں۔
    - **Request quota** پیج کے اندر، وہ **New cores limit** درج کریں جو آپ استعمال کرنا چاہتے ہیں۔ مثال کے طور پر، 24۔
    - **Request quota** پیج کے اندر، **Submit** منتخب کریں تاکہ GPU کوٹہ کی درخواست کی جا سکے۔

### رول اسائنمنٹ شامل کریں

اپنے ماڈلز کو بہتر بنانے اور ڈیپلائے کرنے کے لیے، آپ کو پہلے ایک User Assigned Managed Identity (UAI) بنانا ہوگا اور اسے مناسب اجازتیں دینا ہوں گی۔ یہ UAI ڈیپلائے کے دوران تصدیق کے لیے استعمال ہوگا۔

#### User Assigned Managed Identity(UAI) بنائیں

1. **پورٹل پیج** کے اوپر سرچ بار میں *managed identities* ٹائپ کریں اور نظر آنے والے آپشنز میں سے **Managed Identities** منتخب کریں۔

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.ur.png)

1. **+ Create** منتخب کریں۔

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.ur.png)

1. درج ذیل کام کریں:

    - اپنا Azure **Subscription** منتخب کریں۔
    - استعمال کرنے کے لیے **Resource group** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - وہ **Region** منتخب کریں جسے آپ استعمال کرنا چاہتے ہیں۔
    - **Name** درج کریں۔ یہ ایک منفرد ویلیو ہونی چاہیے۔

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.ur.png)

1. **Review + create** منتخب کریں۔

1. **+ Create** منتخب کریں۔

#### Managed Identity کو Contributor رول اسائنمنٹ دیں

1. اس Managed Identity ریسورس پر جائیں جو آپ نے بنایا ہے۔

1. بائیں جانب ٹیب سے **Azure role assignments** منتخب کریں۔

1. نیویگیشن مینو سے **+Add role assignment** منتخب کریں۔

1. **Add role assignment** پیج کے اندر درج ذیل کام کریں:
    - **Scope** کو **Resource group** پر سیٹ کریں۔
    - اپنا Azure **Subscription** منتخب کریں۔
    - استعمال کرنے کے لیے **Resource group** منتخب کریں۔
    - **Role** کو **Contributor** پر سیٹ کریں۔

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.ur.png)

2. **Save** منتخب کریں۔

#### Managed Identity کو Storage Blob Data Reader رول اسائنمنٹ دیں

1. **پورٹل پیج** کے اوپر سرچ بار میں *storage accounts* ٹائپ کریں اور نظر آنے والے آپشنز میں سے **Storage accounts** منتخب کریں۔

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.ur.png)

1. وہ اسٹوریج اکاؤنٹ منتخب کریں جو Azure Machine Learning workspace سے منسلک ہے۔ مثال کے طور پر، *finetunephistorage*۔

1. **Add role assignment** پیج پر جانے کے لیے درج ذیل کام کریں:

    - اس Azure Storage اکاؤنٹ پر جائیں جو آپ نے بنایا ہے۔
    - بائیں جانب ٹیب سے **Access Control (IAM)** منتخب کریں۔
    - نیویگیشن مینو سے **+ Add** منتخب کریں۔
    - نیویگیشن مینو سے **Add role assignment** منتخب کریں۔

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.ur.png)

1. **Add role assignment** پیج کے اندر درج ذیل کام کریں:

    - **Role** پیج کے اندر، سرچ بار میں *Storage Blob Data Reader* ٹائپ کریں اور نظر آنے والے آپشنز میں سے **Storage Blob Data Reader** منتخب کریں۔
    - **Role** پیج کے اندر، **Next** منتخب کریں۔
    - **Members** پیج کے اندر، **Assign access to** کو **Managed identity** پر سیٹ کریں۔
    - **Members** پیج کے اندر، **+ Select members** منتخب کریں۔
    - **Select managed identities** پیج کے اندر، اپنا Azure **Subscription** منتخب کریں۔
    - **Select managed identities** پیج کے اندر، **Managed identity** کو **Manage Identity** پر سیٹ کریں۔
    - **Select managed identities** پیج کے اندر، وہ Managed Identity منتخب کریں جو آپ نے بنایا ہے۔ مثال کے طور پر، *finetunephi-managedidentity*۔
    - **Select managed identities** پیج کے اندر، **Select** منتخب کریں۔

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.ur.png)

1. **Review + assign** منتخب کریں۔

#### Managed Identity کو AcrPull رول اسائنمنٹ دیں

1. **پورٹل پیج** کے اوپر سرچ بار میں *container registries* ٹائپ کریں اور نظر آنے والے آپشنز میں سے **Container registries** منتخب کریں۔

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.ur.png)

1. وہ کنٹینر رجسٹری منتخب کریں جو Azure Machine Learning workspace سے منسلک ہے۔ مثال کے طور پر، *finetunephicontainerregistry*۔

1. **Add role assignment** پیج پر جانے کے لیے درج ذیل کام کریں:

    - بائیں جانب ٹیب سے **Access Control (IAM)** منتخب کریں۔
    - نیویگیشن مینو سے **+ Add** منتخب کریں۔
    - نیویگیشن مینو سے **Add role assignment** منتخب کریں۔

1. **Add role assignment** پیج کے اندر درج ذیل کام کریں:

    - **Role** پیج کے اندر، سرچ بار میں *AcrPull* ٹائپ کریں اور نظر آنے والے آپشنز میں سے **AcrPull** منتخب کریں۔
    - **Role** پیج کے اندر، **Next** منتخب کریں۔
    - **Members** پیج کے اندر، **Assign access to** کو **Managed identity** پر سیٹ کریں۔
    - **Members** پیج کے اندر، **+ Select members** منتخب کریں۔
    - **Select managed identities** پیج کے اندر، اپنا Azure **Subscription** منتخب کریں۔
    - **Select managed identities** پیج کے اندر، **Managed identity** کو **Manage Identity** پر سیٹ کریں۔
    - **Select managed identities** پیج کے اندر، وہ Managed Identity منتخب کریں جو آپ نے بنایا ہے۔ مثال کے طور پر، *finetunephi-managedidentity*۔
    - **Select managed identities** پیج کے اندر، **Select** منتخب کریں۔
    - **Review + assign** منتخب کریں۔

### پروجیکٹ ترتیب دیں

ڈیٹا سیٹس کو بہتر بنانے کے لیے ڈاؤنلوڈ کرنے کے لیے، آپ ایک لوکل ماحول ترتیب دیں گے۔

اس مشق میں، آپ:

- ایک فولڈر بنائیں گے جس کے اندر کام کریں۔
- ایک ورچوئل ماحول بنائیں گے۔
- مطلوبہ پیکجز انسٹال کریں گے۔
- ایک *download_dataset.py* فائل بنائیں گے تاکہ ڈیٹا سیٹ ڈاؤنلوڈ کیا جا سکے۔

#### ایک فولڈر بنائیں جس کے اندر کام کریں

1. ایک ٹرمینل ونڈو کھولیں اور درج ذیل کمانڈ ٹائپ کریں تاکہ *finetune-phi* نامی فولڈر ڈیفالٹ پاتھ میں بنایا جا سکے۔

    ```console
    mkdir finetune-phi
    ```

2. اپنے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ *finetune-phi* فولڈر پر جائیں جو آپ نے بنایا۔

    ```console
    cd finetune-phi
    ```

#### ایک ورچوئل ماحول بنائیں

1. اپنے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ *.venv* نامی ورچوئل ماحول بنایا جا سکے۔

    ```console
    python -m venv .venv
    ```

2. اپنے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ ورچوئل ماحول کو ایکٹیویٹ کیا جا سکے۔

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> اگر یہ کام کرے، تو آپ کو کمانڈ پرامپٹ سے پہلے *(.venv)* نظر آنا چاہیے۔

#### مطلوبہ پیکجز انسٹال کریں

1. اپنے ٹرمینل میں درج ذیل کمانڈز ٹائپ کریں تاکہ مطلوبہ پیکجز انسٹال کیے جا سکیں۔

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` بنائیں

> [!NOTE]
> مکمل فولڈر اسٹرکچر:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** کھولیں۔

1. مینو بار سے **File** منتخب کریں۔

1. **Open Folder** منتخب کریں۔

1. وہ *finetune-phi* فولڈر منتخب کریں جو آپ نے بنایا، جو *C:\Users\yourUserName\finetune-phi* پر واقع ہے۔

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.ur.png)

1. Visual Studio Code کے بائیں پین میں، رائٹ کلک کریں اور **New File** منتخب کریں تاکہ ایک نئی فائل *download_dataset.py* کے نام سے بنائی جا سکے۔

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.ur.png)

### بہتر بنانے کے لیے ڈیٹا سیٹ تیار کریں

اس مشق میں، آپ *download_dataset.py* فائل کو چلائیں گے تاکہ *ultrachat_200k* ڈیٹا سیٹس کو اپنے لوکل ماحول میں ڈاؤنلوڈ کیا جا سکے۔ آپ پھر ان ڈیٹا سیٹس کو Azure Machine Learning میں Phi-3 ماڈل کو بہتر بنانے کے لیے استعمال کریں گے۔

اس مشق میں، آپ:

- *download_dataset.py* فائل میں کوڈ شامل کریں تاکہ ڈیٹا سیٹس ڈاؤنلوڈ کیے جا سکیں۔
- *download_dataset.py* فائل کو چلائیں تاکہ ڈیٹا سیٹس کو اپنے لوکل ماحول میں ڈاؤنلوڈ کیا جا سکے۔

#### *download_dataset.py* استعمال کرتے ہوئے اپنا ڈیٹا سیٹ ڈاؤنلوڈ کریں

1. *download_dataset.py* فائل کو Visual Studio Code میں کھولیں۔

1. *download_dataset.py* فائل میں درج ذیل کوڈ شامل کریں۔

    ```python
    import json
    import os
    from datasets import load_dataset

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
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. اپنے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ اسکرپٹ چلایا جا سکے اور ڈیٹا سیٹ کو اپنے لو
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. بائیں طرف کے ٹیب سے **Compute** منتخب کریں۔

1. نیویگیشن مینو سے **Compute clusters** منتخب کریں۔

1. **+ New** پر کلک کریں۔

    ![Compute منتخب کریں۔](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.ur.png)

1. درج ذیل کام کریں:

    - وہ **Region** منتخب کریں جسے آپ استعمال کرنا چاہتے ہیں۔
    - **Virtual machine tier** کو **Dedicated** پر سیٹ کریں۔
    - **Virtual machine type** کو **GPU** پر سیٹ کریں۔
    - **Virtual machine size** فلٹر کو **Select from all options** پر سیٹ کریں۔
    - **Virtual machine size** کو **Standard_NC24ads_A100_v4** پر سیٹ کریں۔

    ![کلسٹر بنائیں۔](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.ur.png)

1. **Next** منتخب کریں۔

1. درج ذیل کام کریں:

    - **Compute name** درج کریں۔ یہ ایک منفرد ویلیو ہونا چاہیے۔
    - **Minimum number of nodes** کو **0** پر سیٹ کریں۔
    - **Maximum number of nodes** کو **1** پر سیٹ کریں۔
    - **Idle seconds before scale down** کو **120** پر سیٹ کریں۔

    ![کلسٹر بنائیں۔](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.ur.png)

1. **Create** منتخب کریں۔

#### Phi-3 ماڈل کو Fine-tune کریں

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. وہ Azure Machine Learning workspace منتخب کریں جو آپ نے بنائی تھی۔

    ![بنائی گئی workspace منتخب کریں۔](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ur.png)

1. درج ذیل کام کریں:

    - بائیں طرف کے ٹیب سے **Model catalog** منتخب کریں۔
    - **search bar** میں *phi-3-mini-4k* لکھیں اور ظاہر ہونے والے آپشنز میں سے **Phi-3-mini-4k-instruct** منتخب کریں۔

    ![phi-3-mini-4k لکھیں۔](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.ur.png)

1. نیویگیشن مینو سے **Fine-tune** منتخب کریں۔

    ![Fine tune منتخب کریں۔](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.ur.png)

1. درج ذیل کام کریں:

    - **Select task type** کو **Chat completion** پر سیٹ کریں۔
    - **+ Select data** منتخب کریں اور **Training data** اپلوڈ کریں۔
    - Validation data اپلوڈ کے طریقے کو **Provide different validation data** پر سیٹ کریں۔
    - **+ Select data** منتخب کریں اور **Validation data** اپلوڈ کریں۔

    ![Fine-tuning صفحہ بھریں۔](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.ur.png)

    > [!TIP]
    >
    > آپ **Advanced settings** منتخب کر سکتے ہیں تاکہ جیسے **learning_rate** اور **lr_scheduler_type** کی ترتیب کو اپنی ضروریات کے مطابق Fine-tuning کے عمل کو بہتر بنانے کے لیے اپنی مرضی کے مطابق بنایا جا سکے۔

1. **Finish** منتخب کریں۔

1. اس مشق میں، آپ نے کامیابی سے Phi-3 ماڈل کو Azure Machine Learning کے ذریعے Fine-tune کیا۔ براہ کرم نوٹ کریں کہ Fine-tuning کا عمل کافی وقت لے سکتا ہے۔ Fine-tuning جاب چلانے کے بعد، آپ کو اس کے مکمل ہونے کا انتظار کرنا ہوگا۔ آپ اپنی Azure Machine Learning Workspace کے بائیں طرف کے Jobs ٹیب پر جا کر Fine-tuning جاب کی حیثیت کی نگرانی کر سکتے ہیں۔ اگلی سیریز میں، آپ Fine-tuned ماڈل کو ڈپلائے کریں گے اور اسے Prompt flow کے ساتھ ضم کریں گے۔

    ![Fine-tuning جاب دیکھیں۔](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.ur.png)

### Fine-tuned Phi-3 ماڈل کو ڈپلائے کریں

Fine-tuned Phi-3 ماڈل کو Prompt flow کے ساتھ ضم کرنے کے لیے، آپ کو ماڈل کو حقیقی وقت میں انفرنس کے لیے قابل رسائی بنانے کے لیے ڈپلائے کرنا ہوگا۔ اس عمل میں ماڈل کو رجسٹر کرنا، ایک آن لائن اینڈپوائنٹ بنانا، اور ماڈل کو ڈپلائے کرنا شامل ہے۔

اس مشق میں، آپ کریں گے:

- Fine-tuned ماڈل کو Azure Machine Learning workspace میں رجسٹر کریں۔
- ایک آن لائن اینڈپوائنٹ بنائیں۔
- رجسٹر شدہ Fine-tuned Phi-3 ماڈل کو ڈپلائے کریں۔

#### Fine-tuned ماڈل کو رجسٹر کریں

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. وہ Azure Machine Learning workspace منتخب کریں جو آپ نے بنائی تھی۔

    ![بنائی گئی workspace منتخب کریں۔](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ur.png)

1. بائیں طرف کے ٹیب سے **Models** منتخب کریں۔
1. **+ Register** منتخب کریں۔
1. **From a job output** منتخب کریں۔

    ![ماڈل رجسٹر کریں۔](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.ur.png)

1. وہ جاب منتخب کریں جو آپ نے بنائی تھی۔

    ![جاب منتخب کریں۔](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.ur.png)

1. **Next** منتخب کریں۔

1. **Model type** کو **MLflow** پر سیٹ کریں۔

1. یقینی بنائیں کہ **Job output** منتخب ہے؛ یہ خود بخود منتخب ہونا چاہیے۔

    ![آؤٹ پٹ منتخب کریں۔](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.ur.png)

2. **Next** منتخب کریں۔

3. **Register** منتخب کریں۔

    ![رجسٹر منتخب کریں۔](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.ur.png)

4. آپ اپنے رجسٹر شدہ ماڈل کو بائیں طرف کے ٹیب سے **Models** مینو پر جا کر دیکھ سکتے ہیں۔

    ![رجسٹر شدہ ماڈل۔](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.ur.png)

#### Fine-tuned ماڈل کو ڈپلائے کریں

1. اس Azure Machine Learning workspace میں جائیں جو آپ نے بنائی تھی۔

1. بائیں طرف کے ٹیب سے **Endpoints** منتخب کریں۔

1. نیویگیشن مینو سے **Real-time endpoints** منتخب کریں۔

    ![اینڈپوائنٹ بنائیں۔](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.ur.png)

1. **Create** منتخب کریں۔

1. وہ رجسٹر شدہ ماڈل منتخب کریں جو آپ نے بنایا تھا۔

    ![رجسٹر شدہ ماڈل منتخب کریں۔](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.ur.png)

1. **Select** منتخب کریں۔

1. درج ذیل کام کریں:

    - **Virtual machine** کو *Standard_NC6s_v3* پر سیٹ کریں۔
    - وہ **Instance count** منتخب کریں جو آپ استعمال کرنا چاہتے ہیں۔ مثال کے طور پر، *1*۔
    - **Endpoint** کو **New** پر سیٹ کریں تاکہ ایک نیا اینڈپوائنٹ بنایا جا سکے۔
    - **Endpoint name** درج کریں۔ یہ ایک منفرد ویلیو ہونا چاہیے۔
    - **Deployment name** درج کریں۔ یہ ایک منفرد ویلیو ہونا چاہیے۔

    ![ڈپلائےمنٹ سیٹنگ بھریں۔](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.ur.png)

1. **Deploy** منتخب کریں۔

> [!WARNING]
> اضافی چارجز سے بچنے کے لیے، یقینی بنائیں کہ آپ Azure Machine Learning workspace میں بنائے گئے اینڈپوائنٹ کو حذف کر دیں۔
>

#### Azure Machine Learning Workspace میں ڈپلائےمنٹ کی حیثیت چیک کریں

1. اس Azure Machine Learning workspace میں جائیں جو آپ نے بنائی تھی۔

1. بائیں طرف کے ٹیب سے **Endpoints** منتخب کریں۔

1. وہ اینڈپوائنٹ منتخب کریں جو آپ نے بنایا تھا۔

    ![اینڈپوائنٹس منتخب کریں](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.ur.png)

1. اس صفحے پر، آپ ڈپلائےمنٹ کے عمل کے دوران اینڈپوائنٹس کو منظم کر سکتے ہیں۔

> [!NOTE]
> ایک بار ڈپلائےمنٹ مکمل ہونے کے بعد، یقینی بنائیں کہ **Live traffic** کو **100%** پر سیٹ کیا گیا ہے۔ اگر ایسا نہیں ہے، تو **Update traffic** منتخب کریں تاکہ ٹریفک کی ترتیبات کو ایڈجسٹ کیا جا سکے۔ نوٹ کریں کہ اگر ٹریفک 0% پر سیٹ ہے تو آپ ماڈل کو ٹیسٹ نہیں کر سکتے۔
>
> ![ٹریفک سیٹ کریں۔](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.ur.png)
>

## منظر نامہ 3: Prompt flow کے ساتھ ضم کریں اور Azure AI Foundry میں اپنے کسٹم ماڈل کے ساتھ چیٹ کریں

### کسٹم Phi-3 ماڈل کو Prompt flow کے ساتھ ضم کریں

اپنا Fine-tuned ماڈل کامیابی سے ڈپلائے کرنے کے بعد، آپ اسے Prompt flow کے ساتھ ضم کر سکتے ہیں تاکہ حقیقی وقت کی ایپلیکیشنز میں اپنے ماڈل کو استعمال کیا جا سکے، جس سے اپنے کسٹم Phi-3 ماڈل کے ساتھ مختلف انٹرایکٹو کام انجام دینا ممکن ہو سکے۔

اس مشق میں، آپ کریں گے:

- Azure AI Foundry Hub بنائیں۔
- Azure AI Foundry Project بنائیں۔
- Prompt flow بنائیں۔
- Fine-tuned Phi-3 ماڈل کے لیے کسٹم کنکشن شامل کریں۔
- Prompt flow کو سیٹ اپ کریں تاکہ اپنے کسٹم Phi-3 ماڈل کے ساتھ چیٹ کر سکیں۔

> [!NOTE]
> آپ Azure ML Studio کے ذریعے بھی Prompt flow کے ساتھ ضم کر سکتے ہیں۔ وہی انضمام کا عمل Azure ML Studio پر بھی لاگو کیا جا سکتا ہے۔

#### Azure AI Foundry Hub بنائیں

آپ کو Project بنانے سے پہلے Hub بنانا ہوگا۔ Hub ایک Resource Group کی طرح کام کرتا ہے، جو آپ کو Azure AI Foundry میں متعدد Projects کو منظم کرنے کی اجازت دیتا ہے۔

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) پر جائیں۔

1. بائیں طرف کے ٹیب سے **All hubs** منتخب کریں۔

1. نیویگیشن مینو سے **+ New hub** منتخب کریں۔

    ![Hub بنائیں۔](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.ur.png)

1. درج ذیل کام کریں:

    - **Hub name** درج کریں۔ یہ ایک منفرد ویلیو ہونا چاہیے۔
    - اپنا Azure **Subscription** منتخب کریں۔
    - استعمال کرنے کے لیے **Resource group** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - وہ **Location** منتخب کریں جو آپ استعمال کرنا چاہتے ہیں۔
    - **Connect Azure AI Services** منتخب کریں (اگر ضرورت ہو تو نیا بنائیں)۔
    - **Connect Azure AI Search** کو **Skip connecting** پر سیٹ کریں۔

    ![Hub بھریں۔](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.ur.png)

1. **Next** منتخب کریں۔

#### Azure AI Foundry Project بنائیں

1. اس Hub میں جو آپ نے بنایا تھا، بائیں طرف کے ٹیب سے **All projects** منتخب کریں۔

1. نیویگیشن مینو سے **+ New project** منتخب کریں۔

    ![نیا Project منتخب کریں۔](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.ur.png)

1. **Project name** درج کریں۔ یہ ایک منفرد ویلیو ہونا چاہیے۔

    ![Project بنائیں۔](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.ur.png)

1. **Create a project** منتخب کریں۔

#### Fine-tuned Phi-3 ماڈل کے لیے کسٹم کنکشن شامل کریں

اپنے کسٹم Phi-3 ماڈل کو Prompt flow کے ساتھ ضم کرنے کے لیے، آپ کو ماڈل کے اینڈپوائنٹ اور key کو کسٹم کنکشن میں محفوظ کرنا ہوگا۔ یہ سیٹ اپ Prompt flow میں آپ کے کسٹم Phi-3 ماڈل تک رسائی کو یقینی بناتا ہے۔

#### Fine-tuned Phi-3 ماڈل کا api key اور endpoint uri سیٹ کریں

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) پر جائیں۔

1. اس Azure Machine Learning workspace میں جائیں جو آپ نے بنائی تھی۔

1. بائیں طرف کے ٹیب سے **Endpoints** منتخب کریں۔

    ![اینڈپوائنٹس منتخب کریں۔](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.ur.png)

1. وہ اینڈپوائنٹ منتخب کریں جو آپ نے بنایا تھا۔

    ![بنایا گیا اینڈپوائنٹ منتخب کریں۔](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.ur.png)

1. نیویگیشن مینو سے **Consume** منتخب کریں۔

1. اپنا **REST endpoint** اور **Primary key** کاپی کریں۔
![ایپ آئی کی اور اینڈ پوائنٹ یو آر آئی کاپی کریں۔](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.ur.png)

#### کسٹم کنکشن شامل کریں

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) پر جائیں۔

1. اس Azure AI Foundry پروجیکٹ پر جائیں جو آپ نے بنایا ہے۔

1. اس پروجیکٹ میں جو آپ نے بنایا ہے، بائیں طرف کے ٹیب سے **Settings** منتخب کریں۔

1. **+ New connection** منتخب کریں۔

    ![نیا کنکشن منتخب کریں۔](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.ur.png)

1. نیویگیشن مینو سے **Custom keys** منتخب کریں۔

    ![کسٹم کیز منتخب کریں۔](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.ur.png)

1. درج ذیل کام کریں:

    - **+ Add key value pairs** منتخب کریں۔
    - کلید کے نام کے لیے، **endpoint** درج کریں اور وہ اینڈ پوائنٹ ویلیو فیلڈ میں پیسٹ کریں جو آپ نے Azure ML Studio سے کاپی کیا تھا۔
    - دوبارہ **+ Add key value pairs** منتخب کریں۔
    - کلید کے نام کے لیے، **key** درج کریں اور وہ کلید ویلیو فیلڈ میں پیسٹ کریں جو آپ نے Azure ML Studio سے کاپی کی تھی۔
    - کلیدیں شامل کرنے کے بعد، **is secret** منتخب کریں تاکہ کلید کو ظاہر ہونے سے روکا جا سکے۔

    ![کنکشن شامل کریں۔](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.ur.png)

1. **Add connection** منتخب کریں۔

#### پرامپٹ فلو بنائیں

آپ نے Azure AI Foundry میں ایک کسٹم کنکشن شامل کر دیا ہے۔ اب، درج ذیل مراحل کے ذریعے پرامپٹ فلو بنائیں۔ پھر، آپ اس پرامپٹ فلو کو کسٹم کنکشن سے جوڑیں گے تاکہ آپ پرامپٹ فلو کے اندر فائن ٹونڈ ماڈل استعمال کر سکیں۔

1. اس Azure AI Foundry پروجیکٹ پر جائیں جو آپ نے بنایا ہے۔

1. بائیں طرف کے ٹیب سے **Prompt flow** منتخب کریں۔

1. نیویگیشن مینو سے **+ Create** منتخب کریں۔

    ![پرامپٹ فلو منتخب کریں۔](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.ur.png)

1. نیویگیشن مینو سے **Chat flow** منتخب کریں۔

    ![چیٹ فلو منتخب کریں۔](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.ur.png)

1. **Folder name** درج کریں۔

    ![نام درج کریں۔](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.ur.png)

2. **Create** منتخب کریں۔

#### پرامپٹ فلو کو اپنی کسٹم Phi-3 ماڈل سے چیٹ کے لیے ترتیب دیں

آپ کو اپنی فائن ٹونڈ Phi-3 ماڈل کو پرامپٹ فلو میں شامل کرنا ہوگا۔ تاہم، دستیاب پرامپٹ فلو اس مقصد کے لیے ڈیزائن نہیں کیا گیا ہے۔ لہٰذا، آپ کو پرامپٹ فلو کو دوبارہ ڈیزائن کرنا ہوگا تاکہ کسٹم ماڈل کو شامل کیا جا سکے۔

1. پرامپٹ فلو میں، موجودہ فلو کو دوبارہ بنانے کے لیے درج ذیل کام کریں:

    - **Raw file mode** منتخب کریں۔
    - *flow.dag.yml* فائل میں موجود تمام کوڈ کو حذف کریں۔
    - درج ذیل کوڈ کو *flow.dag.yml* فائل میں شامل کریں۔

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

    ![را فائل موڈ منتخب کریں۔](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.ur.png)

1. کسٹم Phi-3 ماڈل کو پرامپٹ فلو میں استعمال کرنے کے لیے درج ذیل کوڈ کو *integrate_with_promptflow.py* فائل میں شامل کریں۔

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
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
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
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![پرامپٹ فلو کوڈ پیسٹ کریں۔](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.ur.png)

> [!NOTE]
> Azure AI Foundry میں پرامپٹ فلو استعمال کرنے کے بارے میں مزید تفصیلات کے لیے، آپ [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) کو دیکھ سکتے ہیں۔

1. **Chat input**, **Chat output** منتخب کریں تاکہ ماڈل کے ساتھ چیٹ کی جا سکے۔

    ![ان پٹ آؤٹ پٹ۔](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.ur.png)

1. اب آپ اپنی کسٹم Phi-3 ماڈل کے ساتھ چیٹ کے لیے تیار ہیں۔ اگلی مشق میں، آپ سیکھیں گے کہ پرامپٹ فلو کو کیسے شروع کریں اور اپنی فائن ٹونڈ Phi-3 ماڈل کے ساتھ چیٹ کے لیے اسے کیسے استعمال کریں۔

> [!NOTE]
>
> دوبارہ بنایا گیا فلو نیچے دی گئی تصویر کی طرح دکھنا چاہیے:
>
> ![فلو کی مثال۔](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.ur.png)
>

### اپنی کسٹم Phi-3 ماڈل کے ساتھ چیٹ کریں

اب جب کہ آپ نے اپنی کسٹم Phi-3 ماڈل کو فائن ٹون اور پرامپٹ فلو میں شامل کر دیا ہے، آپ اس کے ساتھ بات چیت شروع کرنے کے لیے تیار ہیں۔ یہ مشق آپ کو پرامپٹ فلو کے ذریعے اپنی ماڈل کے ساتھ چیٹ کرنے کا طریقہ ترتیب دینے اور شروع کرنے کے عمل سے آگاہ کرے گی۔ ان مراحل کو مکمل کرکے، آپ اپنی فائن ٹونڈ Phi-3 ماڈل کی صلاحیتوں کو مختلف کاموں اور بات چیت کے لیے مکمل طور پر استعمال کر سکیں گے۔

- پرامپٹ فلو استعمال کرتے ہوئے اپنی کسٹم Phi-3 ماڈل کے ساتھ چیٹ کریں۔

#### پرامپٹ فلو شروع کریں

1. پرامپٹ فلو شروع کرنے کے لیے **Start compute sessions** منتخب کریں۔

    ![کمپیوٹ سیشن شروع کریں۔](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.ur.png)

1. پیرامیٹرز کو ری نیو کرنے کے لیے **Validate and parse input** منتخب کریں۔

    ![ان پٹ کی تصدیق کریں۔](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.ur.png)

1. **connection** کے ویلیو کو اس کسٹم کنکشن کے لیے منتخب کریں جو آپ نے بنایا ہے۔ مثال کے طور پر، *connection*۔

    ![کنکشن۔](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.ur.png)

#### اپنی کسٹم ماڈل کے ساتھ چیٹ کریں

1. **Chat** منتخب کریں۔

    ![چیٹ منتخب کریں۔](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.ur.png)

1. نتائج کی ایک مثال: اب آپ اپنی کسٹم Phi-3 ماڈل کے ساتھ چیٹ کر سکتے ہیں۔ تجویز کی جاتی ہے کہ ان سوالات کو پوچھیں جو فائن ٹوننگ کے لیے استعمال کیے گئے ڈیٹا پر مبنی ہوں۔

    ![پرامپٹ فلو کے ساتھ چیٹ کریں۔](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.ur.png)

**ڈسکلوزر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم یہ بات ذہن میں رکھیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہے۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔