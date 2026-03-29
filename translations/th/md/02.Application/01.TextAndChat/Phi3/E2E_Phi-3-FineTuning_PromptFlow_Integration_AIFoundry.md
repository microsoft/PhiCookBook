# ปรับแต่งและผสานรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt flow ใน Microsoft Foundry

ตัวอย่างแบบครบวงจรนี้อิงจากคำแนะนำ "ปรับแต่งและผสานรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt Flow ใน Microsoft Foundry" จาก Microsoft Tech Community ซึ่งแนะนำกระบวนการปรับแต่ง ติดตั้งใช้งาน และผสานรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt flow ใน Microsoft Foundry
ต่างจากตัวอย่างแบบครบวงจร "[ปรับแต่งและผสานรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" ที่เกี่ยวข้องกับการรันโค้ดในเครื่อง ตัวอย่างนี้มุ่งเน้นที่การปรับแต่งและผสานรวมโมเดลของคุณภายใน Azure AI / ML Studio ทั้งหมด

## ภาพรวม

ในตัวอย่างนี้ คุณจะได้เรียนรู้วิธีปรับแต่งโมเดล Phi-3 และผสานรวมกับ Prompt flow ใน Microsoft Foundry โดยใช้ Azure AI / ML Studio คุณจะสร้างเวิร์กโฟลว์สำหรับการติดตั้งใช้งานและนำโมเดล AI ที่กำหนดเองใช้ ตัวอย่างนี้แบ่งออกเป็นสามสถานการณ์:

**สถานการณ์ที่ 1: ตั้งค่าทรัพยากร Azure และเตรียมพร้อมสำหรับการปรับแต่ง**

**สถานการณ์ที่ 2: ปรับแต่งโมเดล Phi-3 และติดตั้งใช้งานใน Azure Machine Learning Studio**

**สถานการณ์ที่ 3: ผสานรวมกับ Prompt flow และสนทนากับโมเดลที่กำหนดเองใน Microsoft Foundry**

นี่คือภาพรวมของตัวอย่างนี้

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/th/00-01-architecture.198ba0f1ae6d841a.webp)

### สารบัญ

1. **[สถานการณ์ที่ 1: ตั้งค่าทรัพยากร Azure และเตรียมพร้อมสำหรับการปรับแต่ง](#สถานการณ์ที่-1-ตั้งค่าทรัพยากร-azure-และเตรียมพร้อมสำหรับการปรับแต่ง)**
    - [สร้าง Azure Machine Learning Workspace](#สร้าง-azure-machine-learning-workspace)
    - [ขอข้อจำกัดการใช้งาน GPU ใน Azure Subscription](#ขอข้อจำกัดการใช้งาน-gpu-ใน-azure-subscription)
    - [เพิ่มการมอบหมายบทบาท](#เพิ่มการมอบหมายบทบาท)
    - [ตั้งค่าโปรเจกต์](#ตั้งค่าโปรเจกต์)
    - [เตรียมชุดข้อมูลสำหรับการปรับแต่ง](#เตรียมชุดข้อมูลสำหรับการปรับแต่ง)

1. **[สถานการณ์ที่ 2: ปรับแต่งโมเดล Phi-3 และติดตั้งใช้งานใน Azure Machine Learning Studio](#กรณีที่-2-ปรับแต่งโมเดล-phi-3-และติดตั้งใช้งานใน-azure-machine-learning-studio)**
    - [ปรับแต่งโมเดล Phi-3](#ปรับแต่งโมเดล-phi-3)
    - [ติดตั้งโมเดล Phi-3 ที่ปรับแต่งแล้ว](#ติดตั้งโมเดล-phi-3-ที่ปรับแต่งแล้ว)

1. **[สถานการณ์ที่ 3: ผสานรวมกับ Prompt flow และสนทนากับโมเดลที่กำหนดเองใน Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [ผสานรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt flow](#เชื่อมต่อโมเดล-phi-3-ที่ปรับแต่งกับ-prompt-flow)
    - [สนทนากับโมเดล Phi-3 ที่กำหนดเองของคุณ](#แชทกับโมเดล-phi-3-แบบกำหนดเองของคุณ)

## สถานการณ์ที่ 1: ตั้งค่าทรัพยากร Azure และเตรียมพร้อมสำหรับการปรับแต่ง

### สร้าง Azure Machine Learning Workspace

1. พิมพ์ *azure machine learning* ใน **แถบค้นหา** ที่ด้านบนของหน้าเว็บพอร์ทัล แล้วเลือก **Azure Machine Learning** จากตัวเลือกที่แสดงขึ้นมา

    ![Type azure machine learning.](../../../../../../translated_images/th/01-01-type-azml.acae6c5455e67b4b.webp)

2. เลือก **+ Create** จากเมนูนำทาง

3. เลือก **New workspace** จากเมนูนำทาง

    ![Select new workspace.](../../../../../../translated_images/th/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. ดำเนินการดังนี้:

    - เลือก **Subscription** ของ Azure ของคุณ
    - เลือก **Resource group** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - ป้อน **Workspace Name** ซึ่งต้องเป็นค่าที่ไม่ซ้ำกัน
    - เลือก **Region** ที่คุณต้องการใช้
    - เลือก **Storage account** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Key vault** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Application insights** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Container registry** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)

    ![Fill azure machine learning.](../../../../../../translated_images/th/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. เลือก **Review + Create**

6. เลือก **Create**

### ขอข้อจำกัดการใช้งาน GPU ใน Azure Subscription

ในการเรียนรู้นี้ คุณจะได้เรียนรู้วิธีปรับแต่งและติดตั้งโมเดล Phi-3 โดยใช้ GPU สำหรับการปรับแต่ง คุณจะใช้ GPU *Standard_NC24ads_A100_v4* ซึ่งต้องมีการขอข้อจำกัดการใช้งาน สำหรับการติดตั้งใช้งาน คุณจะใช้ GPU *Standard_NC6s_v3* ซึ่งก็ต้องมีการขอข้อจำกัดการใช้งานเช่นกัน

> [!NOTE]
>
> เฉพาะ Subscription แบบ Pay-As-You-Go (ประเภท Subscription มาตรฐาน) เท่านั้นที่มีสิทธิ์ได้รับการจัดสรร GPU; Subscription พิเศษตอนนี้ยังไม่รองรับ
>

1. ไปที่ [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. ดำเนินการดังนี้เพื่อขอขอบเขตการใช้ *Standard NCADSA100v4 Family*:

    - เลือก **Quota** จากแท็บด้านซ้าย
    - เลือก **Virtual machine family** ที่จะใช้ เช่น เลือก **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** ซึ่งรวมถึง GPU *Standard_NC24ads_A100_v4*
    - เลือก **Request quota** จากเมนูนำทาง

        ![Request quota.](../../../../../../translated_images/th/02-02-request-quota.c0428239a63ffdd5.webp)

    - ในหน้า Request quota ป้อน **New cores limit** ที่คุณต้องการใช้ เช่น 24
    - ในหน้า Request quota เลือก **Submit** เพื่อขอขอบเขตการใช้งาน GPU

1. ดำเนินการดังนี้เพื่อขอขอบเขตการใช้ *Standard NCSv3 Family*:

    - เลือก **Quota** จากแท็บด้านซ้าย
    - เลือก **Virtual machine family** ที่จะใช้ เช่น เลือก **Standard NCSv3 Family Cluster Dedicated vCPUs** ซึ่งรวมถึง GPU *Standard_NC6s_v3*
    - เลือก **Request quota** จากเมนูนำทาง
    - ในหน้า Request quota ป้อน **New cores limit** ที่คุณต้องการใช้ เช่น 24
    - ในหน้า Request quota เลือก **Submit** เพื่อขอขอบเขตการใช้งาน GPU

### เพิ่มการมอบหมายบทบาท

ในการปรับแต่งและติดตั้งโมเดลของคุณ คุณต้องสร้าง User Assigned Managed Identity (UAI) ก่อน และมอบสิทธิ์ที่เหมาะสมให้กับมัน UAI นี้จะใช้สำหรับการตรวจสอบสิทธิ์ระหว่างการติดตั้งใช้งาน

#### สร้าง User Assigned Managed Identity (UAI)

1. พิมพ์ *managed identities* ใน **แถบค้นหา** ที่ด้านบนของหน้าเว็บพอร์ทัล แล้วเลือก **Managed Identities** จากตัวเลือกที่แสดงขึ้นมา

    ![Type managed identities.](../../../../../../translated_images/th/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. เลือก **+ Create**

    ![Select create.](../../../../../../translated_images/th/03-02-select-create.92bf8989a5cd98f2.webp)

1. ดำเนินการดังนี้:

    - เลือก **Subscription** ของ Azure ของคุณ
    - เลือก **Resource group** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Region** ที่ต้องการใช้
    - ป้อน **Name** ซึ่งต้องเป็นค่าที่ไม่ซ้ำกัน

    ![Select create.](../../../../../../translated_images/th/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. เลือก **Review + create**

1. เลือก **+ Create**

#### มอบหมายบทบาท Contributor กับ Managed Identity

1. ไปที่ Managed Identity ที่คุณสร้างขึ้น

1. เลือก **Azure role assignments** จากแท็บด้านซ้าย

1. เลือก **+Add role assignment** จากเมนูนำทาง

1. ในหน้า Add role assignment ดำเนินการดังนี้:
    - เลือก **Scope** เป็น **Resource group**
    - เลือก **Subscription** ของ Azure ของคุณ
    - เลือก **Resource group** ที่ต้องการใช้
    - เลือก **Role** เป็น **Contributor**

    ![Fill contributor role.](../../../../../../translated_images/th/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. เลือก **Save**

#### มอบหมายบทบาท Storage Blob Data Reader ให้ Managed Identity

1. พิมพ์ *storage accounts* ใน **แถบค้นหา** ที่ด้านบนของหน้าเว็บพอร์ทัล แล้วเลือก **Storage accounts** จากตัวเลือกที่แสดงขึ้นมา

    ![Type storage accounts.](../../../../../../translated_images/th/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. เลือกบัญชีจัดเก็บข้อมูลที่เชื่อมโยงกับ Azure Machine Learning workspace ที่คุณสร้าง เช่น *finetunephistorage*

1. ดำเนินการดังนี้เพื่อไปยังหน้า Add role assignment:

    - ไปที่บัญชี Azure Storage ที่คุณสร้าง
    - เลือก **Access Control (IAM)** จากแท็บด้านซ้าย
    - เลือก **+ Add** จากเมนูนำทาง
    - เลือก **Add role assignment** จากเมนูนำทาง

    ![Add role.](../../../../../../translated_images/th/03-06-add-role.353ccbfdcf0789c2.webp)

1. ในหน้า Add role assignment ดำเนินการดังนี้:

    - ในหน้าบทบาท พิมพ์ *Storage Blob Data Reader* ใน **แถบค้นหา** แล้วเลือก **Storage Blob Data Reader** จากตัวเลือกที่แสดงขึ้นมา
    - ในหน้าบทบาท เลือก **Next**
    - ในหน้าสมาชิก เลือก **Assign access to** เป็น **Managed identity**
    - ในหน้าสมาชิก เลือก **+ Select members**
    - ในหน้าการเลือก managed identities เลือก **Subscription** ของ Azure ของคุณ
    - ในหน้าการเลือก managed identities เลือก **Managed identity** เป็น **Manage Identity**
    - ในหน้าการเลือก managed identities เลือก Managed Identity ที่คุณสร้าง เช่น *finetunephi-managedidentity*
    - เลือก **Select**

    ![Select managed identity.](../../../../../../translated_images/th/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. เลือก **Review + assign**

#### มอบหมายบทบาท AcrPull ให้ Managed Identity

1. พิมพ์ *container registries* ใน **แถบค้นหา** ที่ด้านบนของหน้าเว็บพอร์ทัล แล้วเลือก **Container registries** จากตัวเลือกที่แสดงขึ้นมา

    ![Type container registries.](../../../../../../translated_images/th/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. เลือก container registry ที่เชื่อมโยงกับ Azure Machine Learning workspace เช่น *finetunephicontainerregistry*

1. ดำเนินการดังนี้เพื่อไปยังหน้า Add role assignment:

    - เลือก **Access Control (IAM)** จากแท็บด้านซ้าย
    - เลือก **+ Add** จากเมนูนำทาง
    - เลือก **Add role assignment** จากเมนูนำทาง

1. ในหน้า Add role assignment ดำเนินการดังนี้:

    - ในหน้าบทบาท พิมพ์ *AcrPull* ใน **แถบค้นหา** แล้วเลือก **AcrPull** จากตัวเลือกที่แสดงขึ้นมา
    - เลือก **Next**
    - ในหน้าสมาชิก เลือก **Assign access to** เป็น **Managed identity**
    - เลือก **+ Select members**
    - เลือก **Subscription** ของ Azure ของคุณ
    - เลือก **Managed identity** เป็น **Manage Identity**
    - เลือก Managed Identity ที่คุณสร้าง เช่น *finetunephi-managedidentity*
    - เลือก **Select**
    - เลือก **Review + assign**

### ตั้งค่าโปรเจกต์

เพื่อดาวน์โหลดชุดข้อมูลที่จำเป็นสำหรับการปรับแต่ง คุณจะตั้งค่าสภาพแวดล้อมในเครื่อง

ในการฝึกหัดนี้ คุณจะ

- สร้างโฟลเดอร์สำหรับทำงานภายในนั้น
- สร้างสภาพแวดล้อมเสมือน
- ติดตั้งแพ็กเกจที่จำเป็น
- สร้างไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูล

#### สร้างโฟลเดอร์สำหรับทำงานภายในนั้น

1. เปิดหน้าต่างเทอร์มินัลและพิมพ์คำสั่งต่อไปนี้เพื่อสร้างโฟลเดอร์ชื่อ *finetune-phi* ในเส้นทางเริ่มต้น

    ```console
    mkdir finetune-phi
    ```

2. พิมพ์คำสั่งนี้ในเทอร์มินัลเพื่อเข้าสู่โฟลเดอร์ *finetune-phi* ที่คุณสร้างไว้

    ```console
    cd finetune-phi
    ```

#### สร้างสภาพแวดล้อมเสมือน

1. พิมพ์คำสั่งนี้ในเทอร์มินัลเพื่อสร้างสภาพแวดล้อมเสมือนชื่อ *.venv*
    ```console
    python -m venv .venv
    ```

2. พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลของคุณเพื่อเปิดใช้งานสภาพแวดล้อมเสมือน

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> หากสำเร็จ คุณจะเห็น *(.venv)* ปรากฏอยู่หน้าตัวบรรทัดคำสั่ง

#### ติดตั้งแพ็กเกจที่จำเป็น

1. พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลของคุณเพื่อติดตั้งแพ็กเกจที่จำเป็น

    ```console
    pip install datasets==2.19.1
    ```

#### สร้าง `donload_dataset.py`

> [!NOTE]
> โครงสร้างโฟลเดอร์สมบูรณ์:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. เปิด **Visual Studio Code**

1. เลือก **File** จากแถบเมนู

1. เลือก **Open Folder**

1. เลือกโฟลเดอร์ *finetune-phi* ที่คุณสร้างไว้ ซึ่งตั้งอยู่ที่ *C:\Users\yourUserName\finetune-phi*

    ![เลือกโฟลเดอร์ที่คุณสร้างไว้](../../../../../../translated_images/th/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. ในแถบด้านซ้ายของ Visual Studio Code คลิกขวาและเลือก **New File** เพื่อสร้างไฟล์ชื่อ *download_dataset.py*

    ![สร้างไฟล์ใหม่](../../../../../../translated_images/th/04-02-create-new-file.cf9a330a3a9cff92.webp)

### เตรียมชุดข้อมูลสำหรับการปรับแต่ง

ในการฝึกนี้ คุณจะรันไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูล *ultrachat_200k* ลงในสภาพแวดล้อมภายในเครื่องของคุณ จากนั้นคุณจะใช้ชุดข้อมูลนี้เพื่อปรับแต่งโมเดล Phi-3 ใน Azure Machine Learning

ในการฝึกนี้ คุณจะ:

- เพิ่มโค้ดลงในไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูล
- รันไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูลลงในสภาพแวดล้อมภายในเครื่อง

#### ดาวน์โหลดชุดข้อมูลโดยใช้ *download_dataset.py*

1. เปิดไฟล์ *download_dataset.py* ใน Visual Studio Code

1. เพิ่มโค้ดต่อไปนี้ลงในไฟล์ *download_dataset.py*

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # โหลดชุดข้อมูลด้วยชื่อ การกำหนดค่า และอัตราส่วนการแบ่งที่ระบุ
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # แบ่งชุดข้อมูลเป็นชุดฝึกและชุดทดสอบ (80% ฝึก, 20% ทดสอบ)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # สร้างไดเรกทอรีหากยังไม่มี
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # เปิดไฟล์ในโหมดเขียน
        with open(filepath, 'w', encoding='utf-8') as f:
            # ทำซ้ำสำหรับแต่ละระเบียนในชุดข้อมูล
            for record in dataset:
                # ส่งออกระเบียนเป็นวัตถุ JSON และเขียนลงในไฟล์
                json.dump(record, f)
                # เขียนตัวอักษรขึ้นบรรทัดใหม่เพื่อแยกระเบียน
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # โหลดและแบ่งชุดข้อมูล ULTRACHAT_200k ด้วยการกำหนดค่าและอัตราส่วนการแบ่งเฉพาะ
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # ดึงชุดข้อมูลฝึกและทดสอบจากการแบ่ง
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # บันทึกชุดข้อมูลฝึกลงในไฟล์ JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # บันทึกชุดข้อมูลทดสอบลงในไฟล์ JSONL แยกต่างหาก
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลของคุณเพื่อรันสคริปต์และดาวน์โหลดชุดข้อมูลลงในสภาพแวดล้อมภายในเครื่อง

    ```console
    python download_dataset.py
    ```

1. ตรวจสอบให้แน่ใจว่าชุดข้อมูลได้ถูกบันทึกอย่างสำเร็จในไดเรกทอรี *finetune-phi/data* ในเครื่องของคุณ

> [!NOTE]
>
> #### หมายเหตุเกี่ยวกับขนาดชุดข้อมูลและเวลาการปรับแต่ง
>
> ในบทแนะนำนี้ คุณใช้เพียง 1% ของชุดข้อมูล (`split='train[:1%]'`) ซึ่งช่วยลดปริมาณข้อมูลอย่างมากและทำให้การอัปโหลดและการปรับแต่งรวดเร็วขึ้น คุณสามารถปรับเปอร์เซ็นต์เพื่อหาจุดสมดุลระหว่างเวลาการฝึกและประสิทธิภาพของโมเดล การใช้ชุดข้อมูลย่อยขนาดเล็กช่วยลดเวลาที่ใช้ในการปรับแต่ง ทำให้การฝึกง่ายขึ้นสำหรับบทแนะนำนี้

## กรณีที่ 2: ปรับแต่งโมเดล Phi-3 และติดตั้งใช้งานใน Azure Machine Learning Studio

### ปรับแต่งโมเดล Phi-3

ในการฝึกนี้ คุณจะปรับแต่งโมเดล Phi-3 ใน Azure Machine Learning Studio

ในการฝึกนี้ คุณจะ:

- สร้างคลัสเตอร์คอมพิวเตอร์สำหรับการปรับแต่ง
- ปรับแต่งโมเดล Phi-3 ใน Azure Machine Learning Studio

#### สร้างคลัสเตอร์คอมพิวเตอร์สำหรับการปรับแต่ง

1. เยี่ยมชม [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. เลือก **Compute** จากแท็บด้านซ้าย

1. เลือก **Compute clusters** จากเมนูการนำทาง

1. เลือก **+ New**

    ![เลือก compute](../../../../../../translated_images/th/06-01-select-compute.a29cff290b480252.webp)

1. ทำตามขั้นตอนดังนี้:

    - เลือก **Region** ที่คุณต้องการใช้
    - เลือก **Virtual machine tier** เป็น **Dedicated**
    - เลือก **Virtual machine type** เป็น **GPU**
    - เลือกตัวกรอง **Virtual machine size** เป็น **Select from all options**
    - เลือก **Virtual machine size** เป็น **Standard_NC24ads_A100_v4**

    ![สร้างคลัสเตอร์](../../../../../../translated_images/th/06-02-create-cluster.f221b65ae1221d4e.webp)

1. เลือก **Next**

1. ทำตามขั้นตอนดังนี้:

    - กรอกชื่อ **Compute name** ซึ่งต้องไม่ซ้ำกับชื่ออื่น
    - เลือกจำนวนโหนดขั้นต่ำเป็น **0**
    - เลือกจำนวนโหนดสูงสุดเป็น **1**
    - เลือกเวลาหยุดงานก่อนปรับลดจำนวนโหนดเป็น **120** วินาที

    ![สร้างคลัสเตอร์](../../../../../../translated_images/th/06-03-create-cluster.4a54ba20914f3662.webp)

1. เลือก **Create**

#### ปรับแต่งโมเดล Phi-3

1. เยี่ยมชม [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. เลือกพื้นที่ทำงาน Azure Machine Learning ที่คุณสร้างไว้

    ![เลือกพื้นที่ทำงานที่คุณสร้างไว้](../../../../../../translated_images/th/06-04-select-workspace.a92934ac04f4f181.webp)

1. ทำตามขั้นตอนดังนี้:

    - เลือก **Model catalog** จากแท็บด้านซ้าย
    - พิมพ์ *phi-3-mini-4k* ในแถบค้นหา และเลือก **Phi-3-mini-4k-instruct** จากตัวเลือกที่แสดง

    ![พิมพ์ phi-3-mini-4k](../../../../../../translated_images/th/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. เลือก **Fine-tune** จากเมนูนำทาง

    ![เลือก fine tune](../../../../../../translated_images/th/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. ทำตามขั้นตอนดังนี้:

    - เลือก **Select task type** เป็น **Chat completion**
    - เลือก **+ Select data** เพื่ออัปโหลด **Training data**
    - เลือกประเภทการอัปโหลด Validation data เป็น **Provide different validation data**
    - เลือก **+ Select data** เพื่ออัปโหลด **Validation data**

    ![กรอกข้อมูลการปรับแต่ง](../../../../../../translated_images/th/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> คุณสามารถเลือก **Advanced settings** เพื่อปรับแต่งค่าคอนฟิก เช่น **learning_rate** และ **lr_scheduler_type** เพื่อเพิ่มประสิทธิภาพการปรับแต่งให้ตรงกับความต้องการของคุณ

1. เลือก **Finish**

1. ในการฝึกนี้ คุณได้ทำการปรับแต่งโมเดล Phi-3 สำเร็จใน Azure Machine Learning โปรดทราบว่ากระบวนการปรับแต่งอาจใช้เวลานาน หลังจากรันงานปรับแต่งแล้ว คุณต้องรอจนกว่าจะเสร็จสิ้น คุณสามารถตรวจสอบสถานะงานปรับแต่งได้โดยไปที่แท็บ Jobs ในพื้นที่ทำงาน Azure Machine Learning ของคุณ ในชุดถัดไป คุณจะได้ติดตั้งโมเดลที่ปรับแต่งแล้วและเชื่อมต่อกับ Prompt flow

    ![ดูงานปรับแต่ง](../../../../../../translated_images/th/06-08-output.2bd32e59930672b1.webp)

### ติดตั้งโมเดล Phi-3 ที่ปรับแต่งแล้ว

เพื่อเชื่อมต่อโมเดล Phi-3 ที่ปรับแต่งแล้วกับ Prompt flow คุณต้องติดตั้งโมเดลเพื่อให้เข้าถึงได้แบบเรียลไทม์ กระบวนการนี้รวมถึงการลงทะเบียนโมเดล สร้าง endpoint ออนไลน์ และติดตั้งโมเดล

ในการฝึกนี้ คุณจะ:

- ลงทะเบียนโมเดลที่ปรับแต่งแล้วในพื้นที่ทำงาน Azure Machine Learning
- สร้าง endpoint ออนไลน์
- ติดตั้งโมเดล Phi-3 ที่ลงทะเบียนแล้ว

#### ลงทะเบียนโมเดลที่ปรับแต่งแล้ว

1. เยี่ยมชม [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. เลือกพื้นที่ทำงาน Azure Machine Learning ที่คุณสร้างไว้

    ![เลือกพื้นที่ทำงานที่คุณสร้างไว้](../../../../../../translated_images/th/06-04-select-workspace.a92934ac04f4f181.webp)

1. เลือก **Models** จากแท็บด้านซ้าย

1. เลือก **+ Register**

1. เลือก **From a job output**

    ![ลงทะเบียนโมเดล](../../../../../../translated_images/th/07-01-register-model.ad1e7cc05e4b2777.webp)

1. เลือกงานที่คุณสร้างไว้

    ![เลือกงาน](../../../../../../translated_images/th/07-02-select-job.3e2e1144cd6cd093.webp)

1. เลือก **Next**

1. เลือก **Model type** เป็น **MLflow**

1. ตรวจสอบว่าตัวเลือก **Job output** ได้ถูกเลือกไว้แล้ว ซึ่งจะถูกเลือกโดยอัตโนมัติ

    ![เลือกค่า output](../../../../../../translated_images/th/07-03-select-output.4cf1a0e645baea1f.webp)

2. เลือก **Next**

3. เลือก **Register**

    ![เลือกลงทะเบียน](../../../../../../translated_images/th/07-04-register.fd82a3b293060bc7.webp)

4. คุณสามารถดูโมเดลที่คุณลงทะเบียนไว้ได้โดยไปที่เมนู **Models** จากแท็บด้านซ้าย

    ![โมเดลที่ลงทะเบียนแล้ว](../../../../../../translated_images/th/07-05-registered-model.7db9775f58dfd591.webp)

#### ติดตั้งโมเดลที่ปรับแต่งแล้ว

1. ไปยังพื้นที่ทำงาน Azure Machine Learning ที่คุณสร้างไว้

1. เลือก **Endpoints** จากแท็บด้านซ้าย

1. เลือก **Real-time endpoints** จากเมนูนำทาง

    ![สร้าง endpoint](../../../../../../translated_images/th/07-06-create-endpoint.1ba865c606551f09.webp)

1. เลือก **Create**

1. เลือกโมเดลที่ลงทะเบียนไว้ที่คุณสร้างไว้

    ![เลือกโมเดลที่ลงทะเบียน](../../../../../../translated_images/th/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. เลือก **Select**

1. ทำตามขั้นตอนดังนี้:

    - เลือก **Virtual machine** เป็น *Standard_NC6s_v3*
    - เลือกจำนวนอินสแตนซ์ที่คุณต้องการ เช่น *1*
    - เลือก **Endpoint** เป็น **New** เพื่อสร้าง endpoint ใหม่
    - กรอกชื่อ **Endpoint name** ซึ่งต้องไม่ซ้ำกับชื่ออื่น
    - กรอกชื่อ **Deployment name** ซึ่งต้องไม่ซ้ำกับชื่ออื่น

    ![กรอกการตั้งค่าการติดตั้ง](../../../../../../translated_images/th/07-08-deployment-setting.43ddc4209e673784.webp)

1. เลือก **Deploy**

> [!WARNING]
> เพื่อป้องกันค่าใช้จ่ายเพิ่มเติมในบัญชีของคุณ โปรดลบ endpoint ที่สร้างไว้ในพื้นที่ทำงาน Azure Machine Learning
>

#### ตรวจสอบสถานะการติดตั้งใน Azure Machine Learning Workspace

1. ไปยังพื้นที่ทำงาน Azure Machine Learning ที่คุณสร้างไว้

1. เลือก **Endpoints** จากแท็บด้านซ้าย

1. เลือก endpoint ที่คุณสร้างไว้

    ![เลือก endpoints](../../../../../../translated_images/th/07-09-check-deployment.325d18cae8475ef4.webp)

1. บนหน้านี้ คุณสามารถจัดการ endpoint ระหว่างกระบวนการติดตั้งได้

> [!NOTE]
> เมื่อการติดตั้งเสร็จสมบูรณ์ ตรวจสอบให้แน่ใจว่า **Live traffic** ถูกตั้งค่าเป็น **100%** หากยังไม่ถูกตั้งค่า ให้เลือก **Update traffic** เพื่อปรับแต่งการตั้งค่านี้ โปรดทราบว่าคุณไม่สามารถทดสอบโมเดลได้หากการจราจรถูกตั้งค่าเป็น 0%
>
> ![ตั้งค่า traffic](../../../../../../translated_images/th/07-10-set-traffic.085b847e5751ff3d.webp)
>

## กรณีที่ 3: เชื่อมต่อกับ Prompt flow และสนทนากับโมเดลที่ปรับแต่งใน Microsoft Foundry

### เชื่อมต่อโมเดล Phi-3 ที่ปรับแต่งกับ Prompt flow

หลังจากประสบความสำเร็จในการติดตั้งโมเดลที่ปรับแต่งแล้ว คุณสามารถเชื่อมโมเดลนี้กับ Prompt Flow เพื่อใช้งานโมเดลของคุณในแอปพลิเคชันเรียลไทม์ ช่วยให้คุณสามารถทำงานเชิงโต้ตอบต่างๆ กับโมเดล Phi-3 ที่กำหนดเองได้

ในการฝึกนี้ คุณจะ:

- สร้าง Microsoft Foundry Hub
- สร้างโปรเจกต์ Microsoft Foundry
- สร้าง Prompt flow
- เพิ่มการเชื่อมต่อแบบกำหนดเองสำหรับโมเดล Phi-3 ที่ปรับแต่งแล้ว
- ตั้งค่า Prompt flow เพื่อสนทนากับโมเดล Phi-3 ของคุณ

> [!NOTE]
> คุณยังสามารถเชื่อมต่อกับ Promptflow ผ่าน Azure ML Studio ได้ กระบวนการเชื่อมต่อนี้ใช้ได้เหมือนกันใน Azure ML Studio

#### สร้าง Microsoft Foundry Hub

คุณต้องสร้าง Hub ก่อนที่จะสร้างโปรเจกต์ Hub ทำหน้าที่เหมือน Resource Group ช่วยให้คุณจัดระเบียบและจัดการโปรเจกต์หลายรายการภายใน Microsoft Foundry ได้ง่ายขึ้น
1. ไปที่ [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)

1. เลือก **All hubs** จากแท็บด้านซ้าย

1. เลือก **+ New hub** จากเมนูนำทาง

    ![Create hub.](../../../../../../translated_images/th/08-01-create-hub.8f7dd615bb8d9834.webp)

1. ดำเนินการดังต่อไปนี้:

    - ป้อน **Hub name** ซึ่งจะต้องเป็นค่าที่ไม่ซ้ำกัน
    - เลือก **Subscription** ของ Azure ของคุณ
    - เลือก **Resource group** ที่จะใช้ (สร้างใหม่หากจำเป็น)
    - เลือก **Location** ที่คุณต้องการใช้
    - เลือก **Connect Azure AI Services** ที่จะใช้ (สร้างใหม่หากจำเป็น)
    - เลือก **Connect Azure AI Search** เป็น **Skip connecting**

    ![Fill hub.](../../../../../../translated_images/th/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. เลือก **Next**

#### สร้างโครงการ Microsoft Foundry

1. ใน Hub ที่คุณสร้างขึ้น เลือก **All projects** จากแท็บด้านซ้าย

1. เลือก **+ New project** จากเมนูนำทาง

    ![Select new project.](../../../../../../translated_images/th/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. ป้อน **Project name** ซึ่งต้องเป็นค่าที่ไม่ซ้ำกัน

    ![Create project.](../../../../../../translated_images/th/08-05-create-project.4d97f0372f03375a.webp)

1. เลือก **Create a project**

#### เพิ่มการเชื่อมต่อแบบกำหนดเองสำหรับโมเดล Phi-3 ที่ผ่านการปรับแต่ง

เพื่อรวมโมเดล Phi-3 แบบกำหนดเองของคุณกับ Prompt flow คุณต้องบันทึก endpoint และคีย์ของโมเดลในการเชื่อมต่อแบบกำหนดเอง การตั้งค่านี้ช่วยให้คุณเข้าถึงโมเดล Phi-3 แบบกำหนดเองผ่าน Prompt flow

#### ตั้งค่า api key และ endpoint uri ของโมเดล Phi-3 ที่ผ่านการปรับแต่ง

1. ไปที่ [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)

1. ไปยัง workspace ของ Azure Machine learning ที่คุณสร้างขึ้น

1. เลือก **Endpoints** จากแท็บด้านซ้าย

    ![Select endpoints.](../../../../../../translated_images/th/08-06-select-endpoints.aff38d453bcf9605.webp)

1. เลือก endpoint ที่คุณสร้างขึ้น

    ![Select endpoints.](../../../../../../translated_images/th/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. เลือก **Consume** จากเมนูนำทาง

1. คัดลอก **REST endpoint** และ **Primary key** ของคุณ

    ![Copy api key and endpoint uri.](../../../../../../translated_images/th/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### เพิ่มการเชื่อมต่อแบบกำหนดเอง

1. ไปที่ [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)

1. ไปยังโครงการ Microsoft Foundry ที่คุณสร้างขึ้น

1. ในโครงการที่คุณสร้าง เลือก **Settings** จากแท็บด้านซ้าย

1. เลือก **+ New connection**

    ![Select new connection.](../../../../../../translated_images/th/08-09-select-new-connection.02eb45deadc401fc.webp)

1. เลือก **Custom keys** จากเมนูนำทาง

    ![Select custom keys.](../../../../../../translated_images/th/08-10-select-custom-keys.856f6b2966460551.webp)

1. ดำเนินการดังนี้:

    - เลือก **+ Add key value pairs**
    - สำหรับชื่อคีย์ ให้ป้อน **endpoint** และวาง endpoint ที่คัดลอกมาจาก Azure ML Studio ในช่องค่า
    - เลือก **+ Add key value pairs** อีกครั้ง
    - สำหรับชื่อคีย์ ให้ป้อน **key** และวางคีย์ที่คัดลอกมาจาก Azure ML Studio ในช่องค่า
    - หลังจากเพิ่มคีย์แล้ว ให้เลือก **is secret** เพื่อป้องกันไม่ให้คีย์ถูกเปิดเผย

    ![Add connection.](../../../../../../translated_images/th/08-11-add-connection.785486badb4d2d26.webp)

1. เลือก **Add connection**

#### สร้าง Prompt flow

คุณได้เพิ่มการเชื่อมต่อแบบกำหนดเองใน Microsoft Foundry แล้ว ตอนนี้มาสร้าง Prompt flow ตามขั้นตอนต่อไปนี้ จากนั้นคุณจะเชื่อมต่อ Prompt flow นี้กับการเชื่อมต่อแบบกำหนดเอง เพื่อให้คุณสามารถใช้โมเดลที่ปรับแต่งแล้วภายใน Prompt flow

1. ไปยังโครงการ Microsoft Foundry ที่คุณสร้างขึ้น

1. เลือก **Prompt flow** จากแท็บด้านซ้าย

1. เลือก **+ Create** จากเมนูนำทาง

    ![Select Promptflow.](../../../../../../translated_images/th/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. เลือก **Chat flow** จากเมนูนำทาง

    ![Select chat flow.](../../../../../../translated_images/th/08-13-select-flow-type.2ec689b22da32591.webp)

1. ป้อน **Folder name** ที่จะใช้

    ![Enter name.](../../../../../../translated_images/th/08-14-enter-name.ff9520fefd89f40d.webp)

2. เลือก **Create**

#### ตั้งค่า Prompt flow เพื่อแชทกับโมเดล Phi-3 แบบกำหนดเองของคุณ

คุณต้องรวมโมเดล Phi-3 ที่ผ่านการปรับแต่งกับ Prompt flow อย่างไรก็ตาม Prompt flow ที่มีอยู่ไม่ได้ออกแบบมาเพื่อวัตถุประสงค์นี้ ดังนั้นคุณต้องออกแบบ Prompt flow ใหม่เพื่อให้สามารถรวมโมเดลกำหนดเองนี้ได้

1. ใน Prompt flow ให้ดำเนินการดังต่อไปนี้เพื่อติดตั้งโฟลว์ใหม่:

    - เลือก **Raw file mode**
    - ลบโค้ดทั้งหมดที่มีอยู่ในไฟล์ *flow.dag.yml*
    - เพิ่มโค้ดต่อไปนี้ในไฟล์ *flow.dag.yml*

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

    - เลือก **Save**

    ![Select raw file mode.](../../../../../../translated_images/th/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. เพิ่มโค้ดต่อไปนี้ในไฟล์ *integrate_with_promptflow.py* เพื่อใช้โมเดล Phi-3 แบบกำหนดเองใน Prompt flow

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # การตั้งค่าการบันทึก
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

        # "connection" คือชื่อของการเชื่อมต่อแบบกำหนดเอง, "endpoint", "key" คือคีย์ในการเชื่อมต่อแบบกำหนดเอง
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
            
            # บันทึกการตอบกลับ JSON ทั้งหมด
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

    ![Paste prompt flow code.](../../../../../../translated_images/th/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> สำหรับข้อมูลรายละเอียดเพิ่มเติมเกี่ยวกับการใช้ Prompt flow ใน Microsoft Foundry คุณสามารถดูได้ที่ [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)

1. เลือก **Chat input**, **Chat output** เพื่อเปิดใช้งานการแชทกับโมเดลของคุณ

    ![Input Output.](../../../../../../translated_images/th/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. ตอนนี้คุณพร้อมที่จะเริ่มแชทกับโมเดล Phi-3 แบบกำหนดเองของคุณแล้ว ในแบบฝึกหัดถัดไป คุณจะได้เรียนรู้วิธีเริ่มต้น Prompt flow และใช้แชทกับโมเดล Phi-3 ที่ปรับแต่งแล้วของคุณ

> [!NOTE]
>
> โฟลว์ที่สร้างใหม่ควรมีลักษณะตามภาพด้านล่าง:
>
> ![Flow example.](../../../../../../translated_images/th/08-18-graph-example.d6457533952e690c.webp)
>

### แชทกับโมเดล Phi-3 แบบกำหนดเองของคุณ

ตอนนี้คุณได้ปรับแต่งและรวมโมเดล Phi-3 แบบกำหนดเองของคุณกับ Prompt flow แล้ว คุณพร้อมที่จะเริ่มโต้ตอบกับโมเดลนี้ แบบฝึกหัดนี้จะแนะนำคุณผ่านขั้นตอนการตั้งค่าและเริ่มการแชทกับโมเดลของคุณโดยใช้ Prompt flow โดยการทำตามขั้นตอนเหล่านี้ คุณจะสามารถใช้ความสามารถของโมเดล Phi-3 ที่ปรับแต่งให้เหมาะสมกับงานและการสนทนาต่างๆ ได้อย่างเต็มที่

- แชทกับโมเดล Phi-3 แบบกำหนดเองของคุณโดยใช้ Prompt flow

#### เริ่ม Prompt flow

1. เลือก **Start compute sessions** เพื่อเริ่ม Prompt flow

    ![Start compute session.](../../../../../../translated_images/th/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. เลือก **Validate and parse input** เพื่อปรับปรุงพารามิเตอร์

    ![Validate input.](../../../../../../translated_images/th/09-02-validate-input.317c76ef766361e9.webp)

1. เลือก **Value** ของ **connection** เป็นการเชื่อมต่อแบบกำหนดเองที่คุณสร้าง เช่น *connection*

    ![Connection.](../../../../../../translated_images/th/09-03-select-connection.99bdddb4b1844023.webp)

#### แชทกับโมเดลกำหนดเองของคุณ

1. เลือก **Chat**

    ![Select chat.](../../../../../../translated_images/th/09-04-select-chat.61936dce6612a1e6.webp)

1. ตัวอย่างผลลัพธ์: ตอนนี้คุณสามารถแชทกับโมเดล Phi-3 แบบกำหนดเองของคุณได้ ขอแนะนำให้ถามคำถามที่เกี่ยวกับข้อมูลที่ใช้สำหรับการปรับแต่งโมเดล

    ![Chat with prompt flow.](../../../../../../translated_images/th/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด กรุณาทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นฉบับควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เรายังไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->