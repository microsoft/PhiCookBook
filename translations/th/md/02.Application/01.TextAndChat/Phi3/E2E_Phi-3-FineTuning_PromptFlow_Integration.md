<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-05-09T17:33:28+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "th"
}
-->
# ปรับแต่งและผสานรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt flow

ตัวอย่างแบบครบวงจร (E2E) นี้อ้างอิงจากคู่มือ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" จาก Microsoft Tech Community ซึ่งแนะนำขั้นตอนการปรับแต่ง การนำไปใช้ และการผสานรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt flow

## ภาพรวม

ในตัวอย่าง E2E นี้ คุณจะได้เรียนรู้วิธีปรับแต่งโมเดล Phi-3 และผสานรวมกับ Prompt flow โดยใช้ Azure Machine Learning และ Prompt flow เพื่อสร้างเวิร์กโฟลว์สำหรับการนำโมเดล AI ที่กำหนดเองไปใช้และใช้งาน ตัวอย่างนี้แบ่งออกเป็นสามสถานการณ์:

**สถานการณ์ที่ 1: ตั้งค่า Azure resources และเตรียมความพร้อมสำหรับการปรับแต่ง**

**สถานการณ์ที่ 2: ปรับแต่งโมเดล Phi-3 และนำไปใช้ใน Azure Machine Learning Studio**

**สถานการณ์ที่ 3: ผสานรวมกับ Prompt flow และสนทนากับโมเดลที่กำหนดเองของคุณ**

นี่คือภาพรวมของตัวอย่าง E2E นี้

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.th.png)

### สารบัญ

1. **[สถานการณ์ที่ 1: ตั้งค่า Azure resources และเตรียมความพร้อมสำหรับการปรับแต่ง](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [สร้าง Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ขอเพิ่มโควต้า GPU ใน Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [เพิ่มการมอบหมายบทบาท](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ตั้งค่าโปรเจกต์](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [เตรียมชุดข้อมูลสำหรับการปรับแต่ง](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[สถานการณ์ที่ 2: ปรับแต่งโมเดล Phi-3 และนำไปใช้ใน Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [ตั้งค่า Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ปรับแต่งโมเดล Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [นำโมเดลที่ปรับแต่งแล้วไปใช้](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[สถานการณ์ที่ 3: ผสานรวมกับ Prompt flow และสนทนากับโมเดลที่กำหนดเองของคุณ](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [ผสานรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [สนทนากับโมเดลที่กำหนดเองของคุณ](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## สถานการณ์ที่ 1: ตั้งค่า Azure resources และเตรียมความพร้อมสำหรับการปรับแต่ง

### สร้าง Azure Machine Learning Workspace

1. พิมพ์ *azure machine learning* ใน **แถบค้นหา** ที่ด้านบนของหน้า portal แล้วเลือก **Azure Machine Learning** จากตัวเลือกที่ปรากฏ

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.th.png)

1. เลือก **+ Create** จากเมนูนำทาง

1. เลือก **New workspace** จากเมนูนำทาง

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.th.png)

1. ดำเนินการดังนี้:

    - เลือก Azure **Subscription** ของคุณ
    - เลือก **Resource group** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - กรอก **Workspace Name** ซึ่งต้องไม่ซ้ำกับชื่ออื่น
    - เลือก **Region** ที่ต้องการใช้
    - เลือก **Storage account** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Key vault** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Application insights** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Container registry** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.th.png)

1. เลือก **Review + Create**

1. เลือก **Create**

### ขอเพิ่มโควต้า GPU ใน Azure Subscription

ในตัวอย่าง E2E นี้ คุณจะใช้ *Standard_NC24ads_A100_v4 GPU* สำหรับการปรับแต่ง ซึ่งต้องมีการขอโควต้า และใช้ *Standard_E4s_v3* CPU สำหรับการนำไปใช้ ซึ่งไม่ต้องขอโควต้า

> [!NOTE]
>
> เฉพาะ Subscription แบบ Pay-As-You-Go (ประเภท Subscription มาตรฐาน) เท่านั้นที่มีสิทธิ์ขอจัดสรร GPU; Subscription ประเภท benefit ยังไม่รองรับในขณะนี้
>
> สำหรับผู้ที่ใช้ Subscription ประเภท benefit (เช่น Visual Studio Enterprise Subscription) หรือผู้ที่ต้องการทดสอบกระบวนการปรับแต่งและนำไปใช้แบบรวดเร็ว บทแนะนำนี้ยังแนะนำวิธีปรับแต่งด้วยชุดข้อมูลขนาดเล็กโดยใช้ CPU แต่ควรทราบว่าผลลัพธ์จากการปรับแต่งจะดีขึ้นมากเมื่อใช้ GPU กับชุดข้อมูลขนาดใหญ่

1. เข้าไปที่ [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. ดำเนินการดังนี้เพื่อขอ *Standard NCADSA100v4 Family* โควต้า:

    - เลือก **Quota** จากแท็บด้านซ้าย
    - เลือก **Virtual machine family** ที่ต้องการใช้ เช่น เลือก **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** ซึ่งรวมถึง *Standard_NC24ads_A100_v4* GPU
    - เลือก **Request quota** จากเมนูนำทาง

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.th.png)

    - ในหน้าขอเพิ่มโควต้า กรอก **New cores limit** ที่ต้องการ เช่น 24
    - เลือก **Submit** เพื่อส่งคำขอโควต้า GPU

> [!NOTE]
> คุณสามารถเลือก GPU หรือ CPU ที่เหมาะสมกับความต้องการโดยดูได้จากเอกสาร [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist)

### เพิ่มการมอบหมายบทบาท

เพื่อปรับแต่งและนำโมเดลของคุณไปใช้ คุณต้องสร้าง User Assigned Managed Identity (UAI) และมอบสิทธิ์ที่เหมาะสมให้กับ UAI ตัวนี้ซึ่งจะใช้สำหรับการยืนยันตัวตนในระหว่างการนำไปใช้

#### สร้าง User Assigned Managed Identity(UAI)

1. พิมพ์ *managed identities* ใน **แถบค้นหา** ที่ด้านบนของหน้า portal แล้วเลือก **Managed Identities** จากตัวเลือกที่ปรากฏ

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.th.png)

1. เลือก **+ Create**

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.th.png)

1. ดำเนินการดังนี้:

    - เลือก Azure **Subscription** ของคุณ
    - เลือก **Resource group** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Region** ที่ต้องการใช้
    - กรอก **Name** ซึ่งต้องไม่ซ้ำกับชื่ออื่น

1. เลือก **Review + create**

1. เลือก **+ Create**

#### เพิ่มการมอบหมายบทบาท Contributor ให้กับ Managed Identity

1. ไปยัง Managed Identity ที่คุณสร้างขึ้น

1. เลือก **Azure role assignments** จากแท็บด้านซ้าย

1. เลือก **+Add role assignment** จากเมนูนำทาง

1. ในหน้าการเพิ่มมอบหมายบทบาท ดำเนินการดังนี้:
    - เลือก **Scope** เป็น **Resource group**
    - เลือก Azure **Subscription** ของคุณ
    - เลือก **Resource group** ที่จะใช้
    - เลือก **Role** เป็น **Contributor**

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.th.png)

1. เลือก **Save**

#### เพิ่มการมอบหมายบทบาท Storage Blob Data Reader ให้กับ Managed Identity

1. พิมพ์ *storage accounts* ใน **แถบค้นหา** ที่ด้านบนของหน้า portal แล้วเลือก **Storage accounts** จากตัวเลือกที่ปรากฏ

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.th.png)

1. เลือก storage account ที่เชื่อมโยงกับ Azure Machine Learning workspace ที่คุณสร้าง เช่น *finetunephistorage*

1. ดำเนินการดังนี้เพื่อไปยังหน้าการเพิ่มมอบหมายบทบาท:

    - ไปยัง Azure Storage account ที่คุณสร้าง
    - เลือก **Access Control (IAM)** จากแท็บด้านซ้าย
    - เลือก **+ Add** จากเมนูนำทาง
    - เลือก **Add role assignment** จากเมนูนำทาง

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.th.png)

1. ในหน้าการเพิ่มมอบหมายบทบาท ดำเนินการดังนี้:

    - ในหน้าบทบาท พิมพ์ *Storage Blob Data Reader* ใน **แถบค้นหา** แล้วเลือก **Storage Blob Data Reader** จากตัวเลือกที่ปรากฏ
    - เลือก **Next**
    - ในหน้าสมาชิก เลือก **Assign access to** เป็น **Managed identity**
    - เลือก **+ Select members**
    - ในหน้าการเลือก managed identities เลือก Azure **Subscription** ของคุณ
    - เลือก **Managed identity** เป็น **Manage Identity**
    - เลือก Manage Identity ที่คุณสร้าง เช่น *finetunephi-managedidentity*
    - เลือก **Select**

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.th.png)

1. เลือก **Review + assign**

#### เพิ่มการมอบหมายบทบาท AcrPull ให้กับ Managed Identity

1. พิมพ์ *container registries* ใน **แถบค้นหา** ที่ด้านบนของหน้า portal แล้วเลือก **Container registries** จากตัวเลือกที่ปรากฏ

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.th.png)

1. เลือก container registry ที่เชื่อมโยงกับ Azure Machine Learning workspace เช่น *finetunephicontainerregistries*

1. ดำเนินการดังนี้เพื่อไปยังหน้าการเพิ่มมอบหมายบทบาท:

    - เลือก **Access Control (IAM)** จากแท็บด้านซ้าย
    - เลือก **+ Add** จากเมนูนำทาง
    - เลือก **Add role assignment** จากเมนูนำทาง

1. ในหน้าการเพิ่มมอบหมายบทบาท ดำเนินการดังนี้:

    - ในหน้าบทบาท พิมพ์ *AcrPull* ใน **แถบค้นหา** แล้วเลือก **AcrPull** จากตัวเลือกที่ปรากฏ
    - เลือก **Next**
    - ในหน้าสมาชิก เลือก **Assign access to** เป็น **Managed identity**
    - เลือก **+ Select members**
    - ในหน้าการเลือก managed identities เลือก Azure **Subscription** ของคุณ
    - เลือก **Managed identity** เป็น **Manage Identity**
    - เลือก Manage Identity ที่คุณสร้าง เช่น *finetunephi-managedidentity*
    - เลือก **Select**
    - เลือก **Review + assign**

### ตั้งค่าโปรเจกต์

ตอนนี้ คุณจะสร้างโฟลเดอร์สำหรับทำงาน และตั้งค่าสภาพแวดล้อมเสมือน (virtual environment) เพื่อพัฒนาโปรแกรมที่โต้ตอบกับผู้ใช้ และใช้ประวัติการสนทนาที่เก็บไว้ใน Azure Cosmos DB เพื่อช่วยให้การตอบสนองมีความเหมาะสม

#### สร้างโฟลเดอร์สำหรับทำงาน

1. เปิดหน้าต่าง terminal แล้วพิมพ์คำสั่งต่อไปนี้เพื่อสร้างโฟลเดอร์ชื่อ *finetune-phi* ในเส้นทางเริ่มต้น

    ```console
    mkdir finetune-phi
    ```

1. พิมพ์คำสั่งต่อไปนี้ใน terminal เพื่อเข้าไปยังโฟลเดอร์ *finetune-phi* ที่คุณสร้าง

    ```console
    cd finetune-phi
    ```

#### สร้างสภาพแวดล้อมเสมือน

1. พิมพ์คำสั่งต่อไปนี้ใน terminal เพื่อสร้างสภาพแวดล้อมเสมือนชื่อ *.venv*

    ```console
    python -m venv .venv
    ```

1. พิมพ์คำสั่งต่อไปนี้ใน terminal เพื่อเปิดใช้งานสภาพแวดล้อมเสมือน

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> ถ้าทำงานได้ถูกต้อง คุณจะเห็น *(.venv)* ปรากฏก่อนพรอมต์คำสั่ง

#### ติดตั้งแพ็กเกจที่จำเป็น

1. พิมพ์คำสั่งต่อไปนี้ใน terminal เพื่อติดตั้งแพ็กเกจที่จำเป็น

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### สร้างไฟล์โปรเจกต์

ในแบบฝึกหัดนี้ คุณจะสร้างไฟล์ที่จำเป็นสำหรับโปรเจกต์ของเรา ซึ่งรวมถึงสคริปต์สำหรับดาวน์โหลดชุดข้อมูล ตั้งค่าสภาพแวดล้อม Azure Machine Learning ปรับแต่งโมเดล Phi-3 และนำโมเดลที่ปรับแต่งแล้วไปใช้ นอกจากนี้ยังสร้างไฟล์ *conda.yml* เพื่อเตรียมสภาพแวดล้อมสำหรับการปรับแต่ง

ในแบบฝึกหัดนี้ คุณจะ:

- สร้างไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูล
- สร้างไฟล์ *setup_ml.py* เพื่อเตรียมสภาพแวดล้อม Azure Machine Learning
- สร้างไฟล์ *fine_tune.py* ในโฟลเดอร์ *finetuning_dir* เพื่อปรับแต่งโมเดล Phi-3 ด้วยชุดข้อมูล
- สร้างไฟล์ *conda.yml* เพื่อเตรียมสภาพแวดล้อมสำหรับการปรับแต่ง
- สร้างไฟล์ *deploy_model.py* เพื่อนำโมเดลที่ปรับแต่งแล้วไปใช้
- สร้างไฟล์ *integrate_with_promptflow.py* เพื่อผสานรวมโมเดลที่ปรับแต่งแล้วและเรียกใช้โมเดลผ่าน Prompt flow
- สร้างไฟล์ flow.dag.yml เพื่อกำหนดโครงสร้างเวิร์กโฟลว์สำหรับ Prompt flow
- สร้างไฟล์ *config.py* เพื่อกรอกข้อมูล Azure

> [!NOTE]
>
> โครงสร้างโฟลเดอร์ทั้งหมด:
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

1. เปิด **Visual Studio Code**

1. เลือก **File** จากแถบเมนู

1. เลือก **Open Folder**

1. เลือกโฟลเดอร์ *finetune-phi* ที่คุณสร้างไว้ ซึ่งอยู่ที่ *C:\Users\yourUserName\finetune-phi*

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.th.png)

1. ในแถบด้านซ้ายของ Visual Studio Code คลิกขวาและเลือก **New File** เพื่อสร้างไฟล์ใหม่ชื่อ *download_dataset.py*

1. ในแถบด้านซ้ายของ Visual Studio Code คลิกขวาและเลือก **New File** เพื่อสร้างไฟล์ใหม่ชื่อ *setup_ml.py*

1. ในแถบด้านซ้ายของ Visual Studio Code คลิกขวาและเลือก **New File** เพื่อสร้างไฟล์ใหม่ชื่อ *deploy_model.py*

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.th.png)

1. ในแถบด้านซ้ายของ Visual Studio Code คลิกขวาและเลือก **New Folder** เพื่อสร้างโฟลเดอร์ใหม่ชื่อ *finetuning_dir*

1. ในโฟลเดอร์ *finetuning_dir* สร้างไฟล์ใหม่ชื่อ *fine_tune.py*

#### สร้างและตั้งค่าไฟล์ *conda.yml*

1. ในแถบด้านซ้ายของ Visual Studio Code คลิกขวาและเลือก **New File** เพื่อสร้างไฟล์ใหม่ชื่อ *conda.yml*

1. เพิ่มโค้ดต่อไปนี้ในไฟล์ *conda.yml* เพื่อเตรียมสภาพแวดล้อมสำหรับการปรับแต่งโมเดล Phi-3

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

#### สร้างและตั้งค่าไฟล์ *config.py*

1. ในแถบด้านซ้ายของ Visual Studio Code คลิกขวาและเลือก **New File** เพื่อสร้างไฟล์ใหม่ชื่อ *config.py*

1. เพิ่มโค้ดต่อไปนี้ในไฟล์ *config.py* เพื่อกรอกข้อมูล Azure ของคุณ

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

#### เพิ่มตัวแปรสภาพแวดล้อม Azure

1. ดำ
![ค้นหา subscription id.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.th.png)

1. ทำตามขั้นตอนต่อไปนี้เพื่อเพิ่มชื่อ Azure Workspace:

    - ไปที่ Azure Machine Learning resource ที่คุณสร้างไว้
    - คัดลอกและวางชื่อบัญชีของคุณลงในไฟล์ *config.py*

    ![ค้นหาชื่อ Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.th.png)

1. ทำตามขั้นตอนต่อไปนี้เพื่อเพิ่มชื่อ Azure Resource Group:

    - ไปที่ Azure Machine Learning resource ที่คุณสร้างไว้
    - คัดลอกและวางชื่อ Azure Resource Group ของคุณลงในไฟล์ *config.py*

    ![ค้นหาชื่อ resource group.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.th.png)

2. ทำตามขั้นตอนต่อไปนี้เพื่อเพิ่มชื่อ Azure Managed Identity

    - ไปที่ Managed Identities resource ที่คุณสร้างไว้
    - คัดลอกและวางชื่อ Azure Managed Identity ของคุณลงในไฟล์ *config.py*

    ![ค้นหา UAI.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.th.png)

### เตรียมชุดข้อมูลสำหรับการ fine-tuning

ในแบบฝึกหัดนี้ คุณจะรันไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูล *ULTRACHAT_200k* ลงในสภาพแวดล้อมของคุณ จากนั้นจะใช้ชุดข้อมูลนี้ในการ fine-tune โมเดล Phi-3 ใน Azure Machine Learning

#### ดาวน์โหลดชุดข้อมูลของคุณโดยใช้ *download_dataset.py*

1. เปิดไฟล์ *download_dataset.py* ใน Visual Studio Code

1. เพิ่มโค้ดต่อไปนี้ลงใน *download_dataset.py*

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
> **คำแนะนำสำหรับการ fine-tune ด้วยชุดข้อมูลขนาดเล็กโดยใช้ CPU**
>
> หากคุณต้องการใช้ CPU ในการ fine-tune วิธีนี้เหมาะสำหรับผู้ที่มี subscription ประเภท benefit (เช่น Visual Studio Enterprise Subscription) หรือสำหรับทดสอบกระบวนการ fine-tune และ deployment อย่างรวดเร็ว
>
> แทนที่ `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลเพื่อรันสคริปต์และดาวน์โหลดชุดข้อมูลลงในสภาพแวดล้อมของคุณ

    ```console
    python download_data.py
    ```

1. ตรวจสอบให้แน่ใจว่าชุดข้อมูลถูกบันทึกลงในไดเรกทอรี *finetune-phi/data* บนเครื่องของคุณเรียบร้อยแล้ว

> [!NOTE]
>
> **ขนาดชุดข้อมูลและเวลาที่ใช้ในการ fine-tune**
>
> ในตัวอย่าง E2E นี้ คุณใช้เพียง 1% ของชุดข้อมูล (`train_sft[:1%]`) ซึ่งช่วยลดปริมาณข้อมูลอย่างมาก ทำให้การอัปโหลดและการ fine-tune เร็วขึ้น คุณสามารถปรับเปอร์เซ็นต์เพื่อหาจุดสมดุลระหว่างเวลาการฝึกและประสิทธิภาพของโมเดล การใช้ชุดข้อมูลย่อยที่เล็กลงจะช่วยลดเวลาที่ต้องใช้ในการ fine-tune ทำให้กระบวนการเหมาะสมกับตัวอย่าง E2E มากขึ้น

## สถานการณ์ที่ 2: Fine-tune โมเดล Phi-3 และ Deploy ใน Azure Machine Learning Studio

### ตั้งค่า Azure CLI

คุณต้องตั้งค่า Azure CLI เพื่อยืนยันตัวตนในสภาพแวดล้อมของคุณ Azure CLI ช่วยให้คุณจัดการทรัพยากร Azure โดยตรงจากบรรทัดคำสั่งและให้ข้อมูลรับรองที่จำเป็นสำหรับ Azure Machine Learning ในการเข้าถึงทรัพยากรเหล่านี้ เริ่มต้นได้โดยติดตั้ง [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. เปิดหน้าต่างเทอร์มินัลและพิมพ์คำสั่งต่อไปนี้เพื่อล็อกอินเข้าสู่บัญชี Azure ของคุณ

    ```console
    az login
    ```

1. เลือกบัญชี Azure ที่จะใช้งาน

1. เลือก subscription ของ Azure ที่จะใช้งาน

    ![ค้นหาชื่อ resource group.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.th.png)

> [!TIP]
>
> หากคุณประสบปัญหาในการเข้าสู่ระบบ Azure ให้ลองใช้ device code เปิดหน้าต่างเทอร์มินัลแล้วพิมพ์คำสั่งต่อไปนี้เพื่อล็อกอินเข้าสู่บัญชี Azure ของคุณ:
>
> ```console
> az login --use-device-code
> ```
>

### Fine-tune โมเดล Phi-3

ในแบบฝึกหัดนี้ คุณจะทำการ fine-tune โมเดล Phi-3 โดยใช้ชุดข้อมูลที่เตรียมไว้ก่อนหน้านี้ ขั้นแรก คุณจะกำหนดกระบวนการ fine-tune ในไฟล์ *fine_tune.py* จากนั้นจะตั้งค่าสภาพแวดล้อม Azure Machine Learning และเริ่มกระบวนการ fine-tune โดยรันไฟล์ *setup_ml.py* สคริปต์นี้จะช่วยให้การ fine-tune เกิดขึ้นภายในสภาพแวดล้อม Azure Machine Learning

โดยการรัน *setup_ml.py* คุณจะเริ่มกระบวนการ fine-tune ในสภาพแวดล้อม Azure Machine Learning

#### เพิ่มโค้ดในไฟล์ *fine_tune.py*

1. ไปที่โฟลเดอร์ *finetuning_dir* และเปิดไฟล์ *fine_tune.py* ใน Visual Studio Code

1. เพิ่มโค้ดต่อไปนี้ลงใน *fine_tune.py*

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

1. บันทึกและปิดไฟล์ *fine_tune.py*

> [!TIP]
> **คุณสามารถ fine-tune โมเดล Phi-3.5 ได้**
>
> ในไฟล์ *fine_tune.py* คุณสามารถเปลี่ยนค่าฟิลด์ `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` ในสคริปต์ของคุณได้
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tune Phi-3.5.":::
>

#### เพิ่มโค้ดในไฟล์ *setup_ml.py*

1. เปิดไฟล์ *setup_ml.py* ใน Visual Studio Code

1. เพิ่มโค้ดต่อไปนี้ลงใน *setup_ml.py*

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

1. แทนที่ `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` ด้วยรายละเอียดเฉพาะของคุณ

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **คำแนะนำสำหรับการ fine-tune ด้วยชุดข้อมูลขนาดเล็กโดยใช้ CPU**
>
> หากคุณต้องการใช้ CPU ในการ fine-tune วิธีนี้เหมาะสำหรับผู้ที่มี subscription ประเภท benefit (เช่น Visual Studio Enterprise Subscription) หรือสำหรับทดสอบกระบวนการ fine-tune และ deployment อย่างรวดเร็ว
>
> 1. เปิดไฟล์ *setup_ml*
> 1. แทนที่ `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` ด้วยรายละเอียดเฉพาะของคุณ
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. พิมพ์คำสั่งต่อไปนี้เพื่อรันสคริปต์ *setup_ml.py* และเริ่มกระบวนการ fine-tune ใน Azure Machine Learning

    ```python
    python setup_ml.py
    ```

1. ในแบบฝึกหัดนี้ คุณได้ทำการ fine-tune โมเดล Phi-3 สำเร็จแล้วโดยใช้ Azure Machine Learning โดยการรันสคริปต์ *setup_ml.py* คุณได้ตั้งค่าสภาพแวดล้อม Azure Machine Learning และเริ่มกระบวนการ fine-tune ที่กำหนดไว้ในไฟล์ *fine_tune.py* โปรดทราบว่ากระบวนการ fine-tune อาจใช้เวลานาน หลังจากรัน `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.th.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` โดยใช้ชื่อที่ต้องการสำหรับ deployment ของคุณ

#### เพิ่มโค้ดในไฟล์ *deploy_model.py*

การรันไฟล์ *deploy_model.py* จะทำให้กระบวนการ deployment ทั้งหมดเป็นไปโดยอัตโนมัติ โดยจะลงทะเบียนโมเดล สร้าง endpoint และดำเนินการ deployment ตามการตั้งค่าในไฟล์ config.py ซึ่งรวมถึงชื่อโมเดล ชื่อ endpoint และชื่อ deployment

1. เปิดไฟล์ *deploy_model.py* ใน Visual Studio Code

1. เพิ่มโค้ดต่อไปนี้ลงใน *deploy_model.py*

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

1. ทำตามขั้นตอนต่อไปนี้เพื่อรับค่า `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` โดยใช้รายละเอียดเฉพาะของคุณ

1. พิมพ์คำสั่งต่อไปนี้เพื่อรันสคริปต์ *deploy_model.py* และเริ่มกระบวนการ deployment ใน Azure Machine Learning

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> เพื่อหลีกเลี่ยงค่าใช้จ่ายเพิ่มเติมในบัญชีของคุณ โปรดลบ endpoint ที่สร้างขึ้นใน Azure Machine Learning workspace เมื่อไม่ใช้งานแล้ว
>

#### ตรวจสอบสถานะ deployment ใน Azure Machine Learning Workspace

1. ไปที่ [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. ไปที่ Azure Machine Learning workspace ที่คุณสร้างไว้

1. เลือก **Studio web URL** เพื่อเปิด Azure Machine Learning workspace

1. เลือก **Endpoints** จากแท็บด้านซ้าย

    ![เลือก endpoints.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.th.png)

2. เลือก endpoint ที่คุณสร้างขึ้น

    ![เลือก endpoints ที่คุณสร้างขึ้น.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.th.png)

3. ในหน้านี้ คุณสามารถจัดการ endpoints ที่สร้างขึ้นในกระบวนการ deployment ได้

## สถานการณ์ที่ 3: รวมเข้ากับ Prompt flow และสนทนากับโมเดลที่ปรับแต่งเอง

### รวมโมเดล Phi-3 ที่ปรับแต่งเองเข้ากับ Prompt flow

หลังจากที่คุณ deploy โมเดลที่ fine-tune เรียบร้อยแล้ว คุณสามารถรวมโมเดลนี้เข้ากับ Prompt flow เพื่อใช้งานโมเดลของคุณในแอปพลิเคชันแบบเรียลไทม์ ช่วยให้ทำงานโต้ตอบต่าง ๆ กับโมเดล Phi-3 ที่ปรับแต่งเองได้หลากหลาย

#### ตั้งค่า api key และ endpoint uri ของโมเดล Phi-3 ที่ fine-tune แล้ว

1. ไปที่ Azure Machine Learning workspace ที่คุณสร้างไว้
1. เลือก **Endpoints** จากแท็บด้านซ้าย
1. เลือก endpoint ที่คุณสร้างขึ้น
1. เลือก **Consume** จากเมนูนำทาง
1. คัดลอกและวาง **REST endpoint** ของคุณลงในไฟล์ *config.py* โดยแทนที่ `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` ด้วย **Primary key** ของคุณ

    ![คัดลอก api key และ endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.th.png)

#### เพิ่มโค้ดในไฟล์ *flow.dag.yml*

1. เปิดไฟล์ *flow.dag.yml* ใน Visual Studio Code

1. เพิ่มโค้ดต่อไปนี้ลงใน *flow.dag.yml*

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

#### เพิ่มโค้ดในไฟล์ *integrate_with_promptflow.py*

1. เปิดไฟล์ *integrate_with_promptflow.py* ใน Visual Studio Code

1. เพิ่มโค้ดต่อไปนี้ลงใน *integrate_with_promptflow.py*

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

### สนทนากับโมเดลที่ปรับแต่งเองของคุณ

1. พิมพ์คำสั่งต่อไปนี้เพื่อรันสคริปต์ *deploy_model.py* และเริ่มกระบวนการ deployment ใน Azure Machine Learning

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. นี่คือตัวอย่างผลลัพธ์: ตอนนี้คุณสามารถสนทนากับโมเดล Phi-3 ที่ปรับแต่งเองได้ แนะนำให้ถามคำถามที่เกี่ยวข้องกับข้อมูลที่ใช้ในการ fine-tune

    ![ตัวอย่าง Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.th.png)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญด้านภาษามนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้