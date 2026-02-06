## วิธีใช้ส่วนประกอบ chat-completion จาก Azure ML system registry เพื่อปรับแต่งโมเดล

ในตัวอย่างนี้เราจะทำการปรับแต่งโมเดล Phi-3-mini-4k-instruct เพื่อทำการสนทนาระหว่างคน 2 คนโดยใช้ชุดข้อมูล ultrachat_200k

![MLFineTune](../../../../translated_images/th/MLFineTune.928d4c6b3767dd35.webp)

ตัวอย่างจะแสดงวิธีการปรับแต่งโดยใช้ Azure ML SDK และ Python จากนั้นทำการ deploy โมเดลที่ปรับแต่งแล้วไปยัง online endpoint เพื่อการทำนายแบบเรียลไทม์

### ข้อมูลการฝึกอบรม

เราจะใช้ชุดข้อมูล ultrachat_200k ซึ่งเป็นเวอร์ชันที่ผ่านการกรองอย่างเข้มงวดของชุดข้อมูล UltraChat และถูกใช้ในการฝึก Zephyr-7B-β ซึ่งเป็นโมเดลแชท 7b ที่ทันสมัยที่สุด

### โมเดล

เราจะใช้โมเดล Phi-3-mini-4k-instruct เพื่อแสดงวิธีที่ผู้ใช้งานสามารถปรับแต่งโมเดลสำหรับงานแชทแบบสมบูรณ์ ถ้าคุณเปิดโน้ตบุ๊กนี้จาก model card เฉพาะ อย่าลืมแทนที่ชื่อโมเดลเฉพาะนั้น

### งานที่ต้องทำ

- เลือกโมเดลเพื่อปรับแต่ง
- เลือกและสำรวจชุดข้อมูลฝึกอบรม
- กำหนดค่าการปรับแต่งงาน
- รันงานปรับแต่ง
- ตรวจสอบตัวชี้วัดการฝึกอบรมและประเมินผล
- ลงทะเบียนโมเดลที่ปรับแต่งแล้ว
- นำโมเดลที่ปรับแต่งแล้วออกใช้งานเพื่อการทำนายแบบเรียลไทม์
- ทำความสะอาดทรัพยากร

## 1. ตั้งค่าความต้องการเบื้องต้น

- ติดตั้ง dependencies
- เชื่อมต่อกับ AzureML Workspace เรียนรู้เพิ่มเติมที่ตั้งค่า SDK authentication แทนที่ <WORKSPACE_NAME>, <RESOURCE_GROUP> และ <SUBSCRIPTION_ID> ด้านล่าง
- เชื่อมต่อไปยัง azureml system registry
- ตั้งชื่อ experiment แบบไม่บังคับ
- ตรวจสอบหรือสร้าง compute

> [!NOTE]
> ความต้องการคือโหนด GPU เดียวสามารถมีหลายการ์ด GPU ตัวอย่างเช่น ในโหนด Standard_NC24rs_v3 มี NVIDIA V100 GPUs 4 ตัว ในขณะที่ Standard_NC12s_v3 มี NVIDIA V100 GPUs 2 ตัว ดูเอกสารเพื่อข้อมูลนี้ จำนวนการ์ด GPU ต่อโหนดตั้งในพารามิเตอร์ gpus_per_node ด้านล่าง การตั้งค่านี้ถูกต้องจะช่วยให้ใช้งาน GPU ทุกตัวในโหนดได้ SKU ของ GPU compute ที่แนะนำสามารถดูได้ที่นี่และที่นี่

### ไลบรารี Python

ติดตั้ง dependencies โดยรัน cell ด้านล่าง นี่ไม่ใช่ขั้นตอนเลือกได้หากรันในสภาพแวดล้อมใหม่

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### การโต้ตอบกับ Azure ML

1. สคริปต์ Python นี้ใช้เพื่อโต้ตอบกับบริการ Azure Machine Learning (Azure ML) นี่คือสรุปสิ่งที่ทำ:

    - นำเข้าโมดูลที่จำเป็นจาก azure.ai.ml, azure.identity, และ azure.ai.ml.entities รวมถึงโมดูล time

    - พยายามยืนยันตัวตนด้วย DefaultAzureCredential() ซึ่งให้ประสบการณ์การยืนยันตัวที่ง่ายเพื่อเริ่มพัฒนาแอปฯ ใน Azure cloud หากล้มเหลวจะเปลี่ยนไปใช้ InteractiveBrowserCredential() ซึ่งมีหน้าต่างล็อกอินแบบโต้ตอบ

    - จากนั้นพยายามสร้างอินสแตนซ์ MLClient โดยใช้วิธี from_config ซึ่งอ่านการตั้งค่าจากไฟล์ config เริ่มต้น (config.json) หากล้มเหลวจะสร้าง MLClient โดยระบุ subscription_id, resource_group_name และ workspace_name ด้วยตนเอง

    - สร้าง MLClient อีกอันหนึ่งโดยระบุ registry "azureml" ซึ่งเป็นที่เก็บโมเดล, pipeline การปรับแต่ง และสภาพแวดล้อม

    - กำหนดชื่อ experiment เป็น "chat_completion_Phi-3-mini-4k-instruct"

    - สร้าง timestamp ที่ไม่ซ้ำกันโดยแปลงเวลาปัจจุบัน (วินาทีตั้งแต่ epoch) เป็นจำนวนเต็มแล้วแปลงเป็นสตริง timestamp นี้ใช้สำหรับสร้างชื่อและเวอร์ชันที่ไม่ซ้ำ

    ```python
    # นำเข้ามอดูลที่จำเป็นจาก Azure ML และ Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # นำเข้ามอดูล time
    
    # พยายามยืนยันตัวตนโดยใช้ DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # หาก DefaultAzureCredential ล้มเหลว ให้ใช้ InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # พยายามสร้างอินสแตนซ์ MLClient โดยใช้ไฟล์คอนฟิกเริ่มต้น
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # หากไม่สำเร็จ ให้สร้างอินสแตนซ์ MLClient โดยระบุรายละเอียดด้วยตนเอง
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # สร้างอินสแตนซ์ MLClient อีกตัวสำหรับ Azure ML registry ชื่อ "azureml"
    # รีจิสทรีนี้เป็นที่เก็บโมเดล, pipeline ปรับแต่ง และ environment
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # ตั้งชื่อการทดลอง
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # สร้าง timestamp ที่ไม่ซ้ำกันซึ่งใช้สำหรับชื่อและเวอร์ชันที่ต้องไม่ซ้ำกัน
    timestamp = str(int(time.time()))
    ```

## 2. เลือกโมเดลฐานเพื่อปรับแต่ง

1. Phi-3-mini-4k-instruct เป็นโมเดลขนาด 3.8 พันล้านพารามิเตอร์ น้ำหนักเบา และทันสมัย สร้างขึ้นบนชุดข้อมูลที่ใช้สำหรับ Phi-2 โมเดลนี้เป็นส่วนหนึ่งของตระกูล Phi-3 และเวอร์ชัน Mini มี 2 แบบคือ 4K และ 128K ซึ่งหมายถึงความยาวบริบท (จำนวนโทเค็น) ที่รองรับได้ เราต้องปรับแต่งโมเดลเพื่อวัตถุประสงค์เฉพาะ เราสามารถเรียกดูโมเดลเหล่านี้ได้ใน Model Catalog ใน AzureML Studio โดยกรองด้วยงาน chat-completion ในตัวอย่างนี้เราใช้โมเดล Phi-3-mini-4k-instruct หากเปิดโน้ตบุ๊กนี้เพื่อโมเดลอื่น กรุณาแทนที่ชื่อและเวอร์ชันโมเดลตามนั้น

> [!NOTE]
> รหัสไอดีของโมเดล นี้จะถูกส่งเป็นอินพุตให้กับงานปรับแต่ง นอกจากนี้ยังปรากฏในช่อง Asset ID ของหน้ารายละเอียดโมเดลใน Model Catalog ของ AzureML Studio

2. สคริปต์ Python นี้โต้ตอบกับบริการ Azure Machine Learning (Azure ML) นี่คือสรุปสิ่งที่ทำ:

    - กำหนด model_name เป็น "Phi-3-mini-4k-instruct"

    - ใช้วิธี get ของ properties models ของ registry_ml_client เพื่อดึงเวอร์ชันล่าสุดของโมเดลที่มีชื่อนี้จาก Azure ML registry get เรียกพร้อมกับอาร์กิวเมนต์สองตัวคือชื่อโมเดลและ label ที่บอกให้ดึงเวอร์ชันล่าสุด

    - แสดงข้อความในคอนโซลแจ้งชื่อ รุ่น และไอดีของโมเดลที่จะใช้ในการปรับแต่ง โดยใช้ format แทรกชื่อ รุ่น และไอดีจาก properties ของ foundation_model

    ```python
    # ตั้งชื่อโมเดล
    model_name = "Phi-3-mini-4k-instruct"
    
    # ดึงเวอร์ชันล่าสุดของโมเดลจาก Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # แสดงชื่อโมเดล, เวอร์ชัน และรหัส
    # ข้อมูลนี้มีประโยชน์สำหรับการติดตามและแก้ไขข้อผิดพลาด
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. สร้าง compute เพื่อใช้กับงาน

งาน finetune ทำงานได้เฉพาะกับ GPU compute ขนาดของ compute ขึ้นกับขนาดโมเดลและส่วนใหญ่จะยากที่จะกำหนดให้ถูกต้อง ส่วนนี่จะแนะนำผู้ใช้เลือก compute ที่เหมาะสมสำหรับงาน

> [!NOTE]
> compute ด้านล่างถูกตั้งค่าที่เหมาะสมที่สุด หากเปลี่ยนแปลงการตั้งค่า อาจทำให้เกิดข้อผิดพลาด Cuda Out Of Memory ในกรณีนี้ควรปรับขนาด compute เป็นขนาดใหญ่ขึ้น

> [!NOTE]
> เมื่อเลือก compute_cluster_size ด้านล่าง ให้แน่ใจว่า compute นั้นมีอยู่ใน resource group ของคุณ หากไม่มีสามารถร้องขอเข้าถึงทรัพยากร compute ได้

### ตรวจสอบโมเดลว่ารองรับ Fine Tuning หรือไม่

1. สคริปต์ Python นี้โต้ตอบกับโมเดล Azure Machine Learning (Azure ML) นี่คือสรุปสิ่งที่ทำ:

    - นำเข้าโมดูล ast ซึ่งใช้สำหรับประมวลผลต้นไม้โครงสร้างซินแทกซ์ Python

    - ตรวจสอบว่า foundation_model มีแท็กชื่อ finetune_compute_allow_list หรือไม่ แท็กใน Azure ML เป็นคู่คีย์-ค่า ที่ใช้กรองและจัดเรียงโมเดล

    - ถ้าแท็ก finetune_compute_allow_list มีอยู่ ใช้ฟังก์ชัน ast.literal_eval เพื่อแปลงค่าแท็ก (ซึ่งเป็นสตริง) เป็นลิสต์ Python จากนั้นเก็บในตัวแปร computes_allow_list และแสดงข้อความแนะนำให้สร้าง compute จากลิสต์นั้น

    - ถ้าแท็ก finetune_compute_allow_list ไม่มีอยู่ จะกำหนด computes_allow_list เป็น None และแสดงข้อความแจ้งว่าแท็กนี้ไม่มีในแท็กของโมเดล

    - สรุป สคริปต์นี้ตรวจสอบแท็กเฉพาะในเมตาดาต้าของโมเดล แปลงค่าของแท็กเป็นลิสต์หากมี และแจ้งผลให้ผู้ใช้ทราบ

    ```python
    # นำเข้าโมดูล ast ซึ่งให้ฟังก์ชันสำหรับประมวลผลโครงสร้างต้นไม้ของไวยากรณ์นามธรรมของ Python
    import ast
    
    # ตรวจสอบว่ามีแท็ก 'finetune_compute_allow_list' อยู่ในแท็กของโมเดลหรือไม่
    if "finetune_compute_allow_list" in foundation_model.tags:
        # หากพบแท็ก ให้ใช้ ast.literal_eval เพื่อแปลงค่าของแท็ก (ซึ่งเป็นสตริง) ให้เป็นรายการของ Python อย่างปลอดภัย
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # แปลงสตริงเป็นรายการของ Python
        # แสดงข้อความแจ้งว่าควรสร้าง compute จากรายการนี้
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # หากไม่พบแท็ก ให้ตั้งค่า computes_allow_list เป็น None
        computes_allow_list = None
        # แสดงข้อความแจ้งว่าแท็ก 'finetune_compute_allow_list' ไม่ใช่ส่วนหนึ่งของแท็กในโมเดล
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### ตรวจสอบ Compute Instance

1. สคริปต์ Python นี้โต้ตอบกับ Azure Machine Learning (Azure ML) และตรวจสอบ compute instance หลายด้าน นี่คือสรุปสิ่งที่ทำ:

    - พยายามดึง compute instance ชื่อ compute_cluster จาก workspace ของ Azure ML ถ้าสถานะ provisioning เป็น "failed" จะโยนข้อผิดพลาด ValueError

    - ตรวจสอบว่า computes_allow_list ไม่ใช่ None ถ้าไม่ใช่ จะเปลี่ยนชื่อขนาด compute ทั้งหมดในลิสต์เป็นตัวพิมพ์เล็ก และตรวจสอบว่าขนาด compute ปัจจุบันอยู่ในลิสต์นั้นหรือไม่ ถ้าไม่ใช่ จะโยน ValueError

    - ถ้า computes_allow_list เป็น None จะตรวจสอบว่าขนาด compute ปัจจุบันอยู่ในลิสต์ของขนาด VM GPU ที่ไม่รองรับหรือไม่ ถ้าใช่ จะโยน ValueError

    - ดึงรายการขนาด compute ทั้งหมดใน workspace จากนั้นวนไล่ตรวจสอบแต่ละขนาด ถ้าชื่อขนาดตรงกับขนาด compute ปัจจุบัน จะดึงจำนวน GPU ของขนาด compute นั้นและตั้งตัวแปร gpu_count_found เป็น True

    - ถ้า gpu_count_found เป็น True แสดงจำนวน GPU ใน compute instance ถ้าไม่ใช่ โยน ValueError

    - สรุป สคริปต์นี้ตรวจสอบสถานะ provisioning ของ compute instance ขนาดเทียบกับ allow list หรือ deny list และจำนวน GPU ที่มีอยู่

    ```python
    # พิมพ์ข้อความข้อผิดพลาด
    print(e)
    # ยกข้อผิดพลาด ValueError หากขนาดการประมวลผลไม่พร้อมใช้งานในพื้นที่ทำงาน
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # ดึงอินสแตนซ์การประมวลผลจากพื้นที่ทำงาน Azure ML
    compute = workspace_ml_client.compute.get(compute_cluster)
    # ตรวจสอบว่ารัฐการจัดเตรียมของอินสแตนซ์การประมวลผลเป็น "ล้มเหลว" หรือไม่
    if compute.provisioning_state.lower() == "failed":
        # ยกข้อผิดพลาด ValueError หากรัฐการจัดเตรียมเป็น "ล้มเหลว"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # ตรวจสอบว่า computes_allow_list ไม่ใช่ None
    if computes_allow_list is not None:
        # แปลงขนาดการประมวลผลทั้งหมดใน computes_allow_list เป็นตัวพิมพ์เล็ก
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # ตรวจสอบว่าขนาดของอินสแตนซ์การประมวลผลอยู่ใน computes_allow_list_lower_case หรือไม่
        if compute.size.lower() not in computes_allow_list_lower_case:
            # ยกข้อผิดพลาด ValueError หากขนาดของอินสแตนซ์การประมวลผลไม่อยู่ใน computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # กำหนดรายการขนาด VM GPU ที่ไม่รองรับ
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # ตรวจสอบว่าขนาดของอินสแตนซ์การประมวลผลอยู่ใน unsupported_gpu_vm_list หรือไม่
        if compute.size.lower() in unsupported_gpu_vm_list:
            # ยกข้อผิดพลาด ValueError หากขนาดของอินสแตนซ์การประมวลผลอยู่ใน unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # กำหนดตัวแปรแฟลกเพื่อตรวจสอบว่าจำนวน GPU ในอินสแตนซ์การประมวลผลถูกพบหรือไม่
    gpu_count_found = False
    # ดึงรายการขนาดการประมวลผลทั้งหมดที่มีในพื้นที่ทำงาน
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # วนลูปผ่านรายการขนาดการประมวลผลที่มีอยู่
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # ตรวจสอบว่าชื่อของขนาดการประมวลผลตรงกับขนาดของอินสแตนซ์การประมวลผลหรือไม่
        if compute_sku.name.lower() == compute.size.lower():
            # หากตรงกัน ดึงจำนวน GPU สำหรับขนาดการประมวลผลนั้นและตั้งค่า gpu_count_found เป็น True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # หาก gpu_count_found เป็น True ให้พิมพ์จำนวน GPU ในอินสแตนซ์การประมวลผล
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # หาก gpu_count_found เป็น False ให้ยกข้อผิดพลาด ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. เลือกชุดข้อมูลสำหรับปรับแต่งโมเดล

1. เราใช้ชุดข้อมูล ultrachat_200k ชุดข้อมูลนี้แบ่งเป็น 4 ส่วน เหมาะสำหรับ Supervised fine-tuning (sft) Generation ranking (gen) จำนวนตัวอย่างในแต่ละส่วนแสดงดังนี้:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. เซลล์ถัดไปจะแสดงการเตรียมข้อมูลพื้นฐานเพื่อปรับแต่ง:

### แสดงตัวอย่างข้อมูลบางแถว

เราต้องการให้ตัวอย่างนี้รันได้เร็ว จึงบันทึกไฟล์ train_sft และ test_sft ที่มีแถวที่ถูกจัดแต่งรูปแบบแล้วเพียง 5% หมายความว่าโมเดลที่ปรับแต่งจะมีความแม่นยำน้อยลง ดังนั้นไม่ควรนำไปใช้จริง
ใช้สคริปต์ download-dataset.py เพื่อดาวน์โหลดชุดข้อมูล ultrachat_200k และแปลงข้อมูลให้อยู่ในรูปแบบที่ pipeline ปรับแต่งใช้ได้ และเพราะชุดข้อมูลใหญ่ เราจึงมีเพียงบางส่วนของชุดข้อมูลนี้เท่านั้น

1. รันสคริปต์ด้านล่างเพียงดาวน์โหลดข้อมูล 5% เท่านั้น สามารถเพิ่มเปอร์เซ็นต์ได้โดยเปลี่ยนค่า dataset_split_pc เป็นเปอร์เซ็นต์ที่ต้องการ

> [!NOTE]
> โมเดลภาษาบางตัวมีรหัสภาษาต่างกัน ดังนั้นชื่อคอลัมน์ในชุดข้อมูลควรสะท้อนสิ่งนี้ด้วย

1. ตัวอย่างของข้อมูลที่ควรเป็น
ชุดข้อมูลแชทแบบสมบูรณ์จัดเก็บในรูปแบบ parquet โดยแต่ละรายการใช้โครงสร้างดังนี้:

    - นี่คือเอกสาร JSON (JavaScript Object Notation) ซึ่งเป็นรูปแบบแลกเปลี่ยนข้อมูลที่นิยม ไม่ใช่โค้ดที่รันได้ แต่เป็นวิธีเก็บและถ่ายโอนข้อมูล นี่คือสรุปโครงสร้าง:

    - "prompt": คีย์นี้เก็บข้อความสายงานหรือคำถามที่ถามให้ AI ช่วย

    - "messages": คีย์นี้เก็บอาร์เรย์ของอ็อบเจ็กต์ แต่ละอ็อบเจ็กต์แทนข้อความในบทสนทนาระหว่างผู้ใช้และผู้ช่วย AI แต่ละข้อความมีคีย์สองอัน:

    - "content": ข้อความเนื้อหาของข้อความนั้น
    - "role": บทบาทของผู้ส่งข้อความ อาจเป็น "user" หรือ "assistant"
    - "prompt_id": รหัสเฉพาะของ prompt นั้น

1. ในเอกสาร JSON นี้ บทสนทนาคือผู้ใช้ถามผู้ช่วย AI ให้สร้างตัวเอกของเรื่องราวสังคมดิสโทเปีย ผู้ช่วยตอบกลับ จากนั้นผู้ใช้ขอรายละเอียดเพิ่มเติม ผู้ช่วยตกลงให้รายละเอียดเพิ่มเติม บทสนทนาทั้งหมดเชื่อมโยงกับ prompt_id เฉพาะตัว

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### ดาวน์โหลดข้อมูล

1. สคริปต์ Python นี้ใช้ดาวน์โหลดชุดข้อมูลโดยใช้สคริปต์ช่วยชื่อ download-dataset.py นี่คือสรุปสิ่งที่ทำ:

    - นำเข้าโมดูล os ซึ่งช่วยให้อยู่ในสภาพแวดล้อมการทำงานระบบปฏิบัติการต่างๆ

    - ใช้ os.system เพื่อรันสคริปต์ download-dataset.py ในเชลล์พร้อมอาร์กิวเมนต์บรรทัดคำสั่งที่ระบุชุดข้อมูล (HuggingFaceH4/ultrachat_200k) โฟลเดอร์สำหรับดาวน์โหลด (ultrachat_200k_dataset) และเปอร์เซ็นต์การแยกชุดข้อมูล (5) ค่า exit_status เก็บสถานะการออกคำสั่ง

    - ตรวจสอบว่า exit_status ไม่ใช่ 0 ซึ่งหมายถึงคำสั่งล้มเหลว ถ้าใช่ จะขว้าง Exception พร้อมข้อความบอกว่ามีข้อผิดพลาดในการดาวน์โหลดชุดข้อมูล

    - สรุป สคริปต์นี้รันคำสั่งดาวน์โหลดชุดข้อมูลผ่านสคริปต์ช่วย และขว้างข้อผิดพลาดหากคำสั่งล้มเหลว

    ```python
    # นำเข้าโมดูล os ซึ่งให้วิธีการใช้ฟังก์ชันที่ขึ้นอยู่กับระบบปฏิบัติการ
    import os
    
    # ใช้ฟังก์ชัน os.system เพื่อรันสคริปต์ download-dataset.py ใน shell พร้อมด้วยอาร์กิวเมนต์บรรทัดคำสั่งที่ระบุ
    # อาร์กิวเมนต์ระบุชุดข้อมูลที่จะดาวน์โหลด (HuggingFaceH4/ultrachat_200k), โฟลเดอร์ที่จะดาวน์โหลดไปเก็บ (ultrachat_200k_dataset) และเปอร์เซ็นต์ของชุดข้อมูลที่จะแบ่ง (5)
    # ฟังก์ชัน os.system คืนค่ารหัสสถานะออกจากคำสั่งที่รัน; รหัสสถานะนี้ถูกเก็บไว้ในตัวแปร exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # ตรวจสอบว่า exit_status ไม่ใช่ 0
    # ในระบบปฏิบัติการที่คล้าย Unix, รหัสสถานะออก 0 มักหมายความว่าคำสั่งสำเร็จ ในขณะที่เลขอื่นใดหมายถึงข้อผิดพลาด
    # หาก exit_status ไม่ใช่ 0, ให้โยน Exception พร้อมข้อความที่ระบุว่ามีข้อผิดพลาดในการดาวน์โหลดชุดข้อมูล
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### โหลดข้อมูลลง DataFrame

1. สคริปต์ Python นี้โหลดไฟล์ JSON Lines ลงใน DataFrame ของ pandas และแสดง 5 แถวแรก นี่คือสรุปสิ่งที่ทำ:

    - นำเข้าห้องสมุด pandas ซึ่งเป็นไลบรารีสำหรับจัดการและวิเคราะห์ข้อมูลที่ทรงพลัง

    - กำหนดความกว้างคอลัมน์สูงสุดของ pandas ให้เป็น 0 หมายความว่าแสดงข้อความเต็มในแต่ละคอลัมน์เมื่อพิมพ์ DataFrame
- ใช้ฟังก์ชัน pd.read_json เพื่อโหลดไฟล์ train_sft.jsonl จากไดเรกทอรี ultrachat_200k_dataset เข้าไปใน DataFrame อาร์กิวเมนต์ lines=True ระบุว่าไฟล์เป็นรูปแบบ JSON Lines ซึ่งแต่ละบรรทัดเป็นอ็อบเจ็กต์ JSON แยกกัน

- ใช้วิธี head เพื่อแสดง 5 แถวแรกของ DataFrame หาก DataFrame มีแถวน้อยกว่า 5 แถว จะทำการแสดงทั้งหมด

- สรุปคือสคริปต์นี้กำลังโหลดไฟล์ JSON Lines เข้า DataFrame และแสดง 5 แถวแรกพร้อมแสดงข้อความคอลัมน์เต็ม

    ```python
    # นำเข้าห้องสมุด pandas ซึ่งเป็นห้องสมุดที่ทรงพลังสำหรับการจัดการและวิเคราะห์ข้อมูล
    import pandas as pd
    
    # ตั้งค่าความกว้างสูงสุดของคอลัมน์สำหรับตัวเลือกการแสดงผลของ pandas เป็น 0
    # หมายความว่าข้อความเต็มของแต่ละคอลัมน์จะแสดงโดยไม่ถูกตัดเมื่อพิมพ์ DataFrame
    pd.set_option("display.max_colwidth", 0)
    
    # ใช้ฟังก์ชัน pd.read_json เพื่อโหลดไฟล์ train_sft.jsonl จากไดเรกทอรี ultrachat_200k_dataset ลงใน DataFrame
    # อาร์กิวเมนต์ lines=True บ่งชี้ว่าไฟล์อยู่ในรูปแบบ JSON Lines ซึ่งแต่ละบรรทัดเป็นอ็อบเจ็กต์ JSON แยกต่างหาก
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # ใช้วิธี head เพื่อแสดง 5 แถวแรกของ DataFrame
    # หาก DataFrame มีแถวน้อยกว่า 5 แถว จะทำการแสดงทั้งหมด
    df.head()
    ```

## 5. ส่งงาน fine tuning โดยใช้โมเดลและข้อมูลเป็นอินพุต

สร้างงานที่ใช้คอมโพเนนต์ pipeline chat-completion เรียนรู้เพิ่มเติมเกี่ยวกับพารามิเตอร์ทั้งหมดที่รองรับสำหรับการปรับแต่งแบบละเอียด

### กำหนดพารามิเตอร์ finetune

1. พารามิเตอร์ finetune สามารถจัดกลุ่มได้เป็น 2 ประเภท - พารามิเตอร์การฝึกอบรม, พารามิเตอร์การเพิ่มประสิทธิภาพ

1. พารามิเตอร์การฝึกอบรมกำหนดลักษณะการฝึกอบรม เช่น -

    - ตัว optimizer, scheduler ที่จะใช้
    - เมตริกที่ใช้ในการเพิ่มประสิทธิภาพ finetune
    - จำนวนขั้นตอนการฝึกอบรมและขนาดแบตช์ ฯลฯ
    - พารามิเตอร์การเพิ่มประสิทธิภาพช่วยในการจัดการหน่วยความจำ GPU และใช้ทรัพยากรคอมพิวต์ได้อย่างมีประสิทธิภาพ

1. ด้านล่างเป็นพารามิเตอร์บางส่วนที่จัดอยู่ในกลุ่มนี้ พารามิเตอร์การเพิ่มประสิทธิภาพแตกต่างกันตามแต่ละโมเดลและถูกจัดแพ็กเกจมาพร้อมกับโมเดลเพื่อจัดการความแตกต่างเหล่านี้

    - เปิดใช้งาน deepspeed และ LoRA
    - เปิดใช้งานการฝึกอบรมแบบผสมความแม่นยำ (mixed precision training)
    - เปิดใช้งานการฝึกอบรมหลายโหนด (multi-node training)

> [!NOTE]
> การปรับแต่งแบบมีผู้ดูแลอาจทำให้เกิดการสูญเสียความสอดคล้องหรือการลืมข้อมูลอย่างรุนแรง แนะนำให้ตรวจสอบปัญหานี้และทำการปรับความสอดคล้องขั้นตอนหลังจากที่คุณทำ finetune เสร็จ

### พารามิเตอร์การปรับแต่งแบบละเอียด

1. สคริปต์ Python นี้กำลังตั้งค่าพารามิเตอร์สำหรับการปรับแต่งแบบละเอียดของโมเดลแมชชีนเลิร์นนิง รายละเอียดดังนี้:

    - ตั้งค่าพารามิเตอร์การฝึกอบรมเริ่มต้น เช่น จำนวน epochs ในการฝึก ขนาดแบตช์สำหรับการฝึกและประเมินผล อัตราการเรียนรู้ และประเภทของ learning rate scheduler

    - ตั้งค่าพารามิเตอร์การเพิ่มประสิทธิภาพเริ่มต้น เช่น การใช้ Layer-wise Relevance Propagation (LoRa) และ DeepSpeed และระดับของ DeepSpeed

    - รวมพารามิเตอร์การฝึกอบรมและการเพิ่มประสิทธิภาพเข้าด้วยกันเป็นพจนานุกรมชื่อ finetune_parameters

    - ตรวจสอบว่า foundation_model มีพารามิเตอร์เริ่มต้นเฉพาะโมเดลหรือไม่ หากมี จะพิมพ์ข้อความเตือนและอัปเดตพจนานุกรม finetune_parameters ด้วยพารามิเตอร์เริ่มต้นเฉพาะโมเดลนั้น ฟังก์ชัน ast.literal_eval ใช้เพื่อแปลงพารามิเตอร์เริ่มต้นเฉพาะโมเดลจากสตริงเป็นพจนานุกรม Python

    - แสดงชุดพารามิเตอร์ปรับแต่งแบบละเอียดที่ใช้กับรันนี้

    - สรุปคือสคริปต์นี้ตั้งค่าและแสดงพารามิเตอร์สำหรับการปรับแต่งแบบละเอียดของโมเดลแมชชีนเลิร์นนิง พร้อมความสามารถในการแทนที่พารามิเตอร์เริ่มต้นด้วยพารามิเตอร์เฉพาะโมเดล

    ```python
    # ตั้งค่าพารามิเตอร์การฝึกอบรมเริ่มต้น เช่น จำนวน epochs สำหรับการฝึก ขนาดชุดข้อมูลสำหรับการฝึกและการประเมิน อัตราการเรียนรู้ และประเภทตัวปรับแต่งอัตราการเรียนรู้
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # ตั้งค่าพารามิเตอร์การปรับแต่งเริ่มต้น เช่น การใช้ Layer-wise Relevance Propagation (LoRa) และ DeepSpeed และระดับของ DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # รวมพารามิเตอร์การฝึกอบรมและการปรับแต่งเข้าเป็นพจนานุกรมเดียวชื่อ finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # ตรวจสอบว่า foundation_model มีพารามิเตอร์เริ่มต้นเฉพาะโมเดลหรือไม่
    # หากมี ให้แสดงข้อความเตือนและอัปเดตพจนานุกรม finetune_parameters ด้วยค่าพารามิเตอร์เริ่มต้นเฉพาะโมเดลเหล่านี้
    # ฟังก์ชัน ast.literal_eval ถูกใช้เพื่อแปลงค่าพารามิเตอร์เริ่มต้นเฉพาะโมเดลจากสตริงเป็นพจนานุกรมของ Python
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # แปลงสตริงเป็นพจนานุกรมของ Python
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # แสดงชุดพารามิเตอร์การปรับแต่งขั้นสุดท้ายที่จะใช้สำหรับการรันนั้น
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Training Pipeline

1. สคริปต์ Python นี้กำหนดฟังก์ชันเพื่อสร้างชื่อที่จะแสดงสำหรับ pipeline การฝึกอบรมแมชชีนเลิร์นนิง จากนั้นเรียกใช้ฟังก์ชันนี้เพื่อสร้างและพิมพ์ชื่อที่จะแสดง รายละเอียดดังนี้:

1. ฟังก์ชัน get_pipeline_display_name ถูกกำหนด ฟังก์ชันนี้สร้างชื่อที่จะแสดงโดยอิงตามพารามิเตอร์ต่างๆ ที่เกี่ยวข้องกับ pipeline การฝึกอบรม

1. ภายในฟังก์ชัน คำนวณขนาดแบตช์รวมโดยการคูณขนาดแบตช์ต่ออุปกรณ์ จำนวนขั้นตอนการสะสม gradient จำนวน GPUs ต่อโหนด และจำนวนโหนดที่ใช้สำหรับ fine-tuning

1. ดึงพารามิเตอร์อื่นๆ เช่น ประเภทของ learning rate scheduler, การใช้ DeepSpeed หรือไม่ ระดับ DeepSpeed, การใช้ Layer-wise Relevance Propagation (LoRa) หรือไม่, จำนวน checkpoint โมเดลที่เก็บได้สูงสุด, และความยาวลำดับสูงสุด

1. สร้างสตริงที่รวมพารามิเตอร์ทั้งหมดโดยแยกด้วยขีดกลาง หากใช้ DeepSpeed หรือ LoRa สตริงจะรวมคำว่า "ds" ตามด้วยระดับ DeepSpeed หรือ "lora" ตามลำดับ หากไม่ใช้ จะรวมคำว่า "nods" หรือ "nolora" ตามลำดับ

1. ฟังก์ชันจะคืนค่าสตริงนี้ ซึ่งใช้เป็นชื่อแสดงสำหรับ pipeline การฝึกอบรม

1. หลังจากกำหนดฟังก์ชันแล้ว จะเรียกใช้ฟังก์ชันเพื่อสร้างชื่อแสดง จากนั้นพิมพ์ชื่อที่แสดงนี้

1. สรุปคือสคริปต์นี้สร้างชื่อแสดงสำหรับ pipeline การฝึกอบรมแมชชีนเลิร์นนิงโดยอิงตามพารามิเตอร์หลายอย่าง จากนั้นพิมพ์ชื่อแสดงนี้

    ```python
    # กำหนดฟังก์ชันเพื่อสร้างชื่อแสดงสำหรับกระบวนการฝึกอบรม
    def get_pipeline_display_name():
        # คำนวณขนาดแบตช์ทั้งหมดโดยคูณขนาดแบตช์ต่ออุปกรณ์ จำนวนขั้นตอนสะสม gradient จำนวน GPU ต่อโหนด และจำนวนโหนดที่ใช้สำหรับการปรับแต่ง
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # ดึงประเภทตัวจัดการอัตราการเรียนรู้
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # ดึงข้อมูลว่ามีการใช้ DeepSpeed หรือไม่
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # ดึงระยะของ DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # หากใช้ DeepSpeed ให้รวม "ds" ตามด้วยระยะของ DeepSpeed ในชื่อแสดง หากไม่ใช้ ให้รวม "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # ดึงข้อมูลว่ามีการใช้ Layer-wise Relevance Propagation (LoRa) หรือไม่
        lora = finetune_parameters.get("apply_lora", "false")
        # หากใช้ LoRa ให้รวม "lora" ในชื่อแสดง หากไม่ใช้ ให้รวม "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # ดึงขีดจำกัดจำนวนจุดตรวจสอบโมเดลที่เก็บไว้
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # ดึงความยาวลำดับสูงสุด
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # สร้างชื่อแสดงโดยการเชื่อมพารามิเตอร์ทั้งหมดเข้าด้วยกัน โดยคั่นด้วยขีดกลาง
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # เรียกฟังก์ชันเพื่อสร้างชื่อแสดง
    pipeline_display_name = get_pipeline_display_name()
    # พิมพ์ชื่อแสดง
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### กำหนดค่า Pipeline

สคริปต์ Python นี้กำหนดและกำหนดค่า pipeline การเรียนรู้ของเครื่องโดยใช้ Azure Machine Learning SDK รายละเอียดดังนี้:

1. นำเข้ามอดูลที่จำเป็นจาก Azure AI ML SDK

1. ดึงคอมโพเนนต์ pipeline ชื่อ "chat_completion_pipeline" จากรีจิสทรี

1. กำหนดงาน pipeline โดยใช้ตัวตกแต่ง `@pipeline` และฟังก์ชัน `create_pipeline` โดยตั้งชื่อ pipeline เป็น `pipeline_display_name`

1. ภายในฟังก์ชัน `create_pipeline` สร้างอินสแตนซ์ของคอมโพเนนต์ pipeline ที่ดึงมาโดยให้พารามิเตอร์ต่างๆ เช่น เส้นทางโมเดล คลัสเตอร์คอมพิวต์สำหรับขั้นตอนต่างๆ การแยกชุดข้อมูลสำหรับการฝึกและทดสอบ จำนวน GPU ที่ใช้ในการปรับแต่งละเอียด และพารามิเตอร์ fine-tuning อื่นๆ

1. ทำการแมปเอาต์พุตของงาน fine-tuning ให้เป็นเอาต์พุตของงาน pipeline เพื่อให้โมเดลที่ปรับแต่งแล้วสามารถลงทะเบียนได้อย่างง่ายดาย ซึ่งจำเป็นสำหรับการปรับใช้โมเดลบน endpoint ออนไลน์หรือแบบ batch

1. สร้างอินสแตนซ์ pipeline โดยเรียกใช้ฟังก์ชัน `create_pipeline`

1. ตั้งค่าการตั้งค่า `force_rerun` ของ pipeline เป็น `True` หมายความว่าจะไม่ใช้ผลลัพธ์ที่แคชจากงานก่อนหน้านี้

1. ตั้งค่าการตั้งค่า `continue_on_step_failure` ของ pipeline เป็น `False` หมายความว่า pipeline จะหยุดหากขั้นตอนใดล้มเหลว

1. สรุปคือสคริปต์นี้กำหนดและกำหนดค่า pipeline การเรียนรู้ของเครื่องสำหรับงาน chat completion โดยใช้ Azure Machine Learning SDK

    ```python
    # นำเข้าชุดโมดูลที่จำเป็นจาก Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # ดึงคอมโพเนนต์ของ pipeline ที่ชื่อ "chat_completion_pipeline" จาก registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # กำหนด pipeline job โดยใช้ตัวตกแต่ง @pipeline และฟังก์ชัน create_pipeline
    # ตั้งชื่อ pipeline เป็น pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # เริ่มต้นคอมโพเนนต์ pipeline ที่ดึงมาโดยใช้พารามิเตอร์ต่าง ๆ
        # ซึ่งรวมถึงเส้นทางของโมเดล, กลุ่มคอมพิวต์สำหรับขั้นตอนต่าง ๆ, แบ่งชุดข้อมูลสำหรับเทรนและทดสอบ, จำนวน GPU ที่ใช้ในการปรับแต่ง และพารามิเตอร์การปรับแต่งอื่น ๆ
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # แมปการแบ่งชุดข้อมูลกับพารามิเตอร์
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # การตั้งค่าการฝึกอบรม
            number_of_gpu_to_use_finetuning=gpus_per_node,  # ตั้งค่าเป็นจำนวน GPU ที่มีอยู่ในคอมพิวต์
            **finetune_parameters
        )
        return {
            # แมปผลลัพธ์ของงานการปรับแต่งไปยังผลลัพธ์ของ pipeline job
            # ทำเช่นนี้เพื่อให้เราสามารถลงทะเบียนโมเดลที่ปรับแต่งได้อย่างง่ายดาย
            # การลงทะเบียนโมเดลเป็นสิ่งจำเป็นเพื่อปรับใช้โมเดลไปยัง endpoint ออนไลน์หรือ batch
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # สร้างอินสแตนซ์ของ pipeline โดยเรียกใช้ฟังก์ชัน create_pipeline
    pipeline_object = create_pipeline()
    
    # ไม่ใช้ผลลัพธ์เก่าจากงานก่อนหน้า
    pipeline_object.settings.force_rerun = True
    
    # ตั้งค่า continue on step failure เป็น False
    # หมายความว่า pipeline จะหยุดทำงานหากขั้นตอนใดล้มเหลว
    pipeline_object.settings.continue_on_step_failure = False
    ```

### ส่งงาน

1. สคริปต์ Python นี้ส่งงาน pipeline การเรียนรู้ของเครื่องไปยัง Azure Machine Learning workspace แล้วรอจนกว่างานจะเสร็จสิ้น รายละเอียดดังนี้:

    - เรียกใช้เมทอด create_or_update ของออบเจ็กต์ jobs ใน workspace_ml_client เพื่อส่งงาน pipeline ที่ระบุโดย pipeline_object และทดลองภายใต้ experiment_name

    - จากนั้นเรียกใช้เมทอด stream ของออบเจ็กต์ jobs ใน workspace_ml_client เพื่อรอให้ pipeline job เสร็จสิ้น ใช้งานที่รอโดยระบุชื่อในแอตทริบิวต์ name ของออบเจ็กต์ pipeline_job

    - สรุปคือสคริปต์นี้ส่งงาน pipeline การเรียนรู้ของเครื่องไปยัง Azure Machine Learning workspace แล้วรอจนงานเสร็จ

    ```python
    # ส่งงาน pipeline ไปยัง Azure Machine Learning workspace
    # pipeline ที่จะรันถูกระบุโดย pipeline_object
    # การทดลองที่งานถูกรันอยู่ภายใต้ ถูกระบุโดย experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # รอให้งาน pipeline เสร็จสมบูรณ์
    # งานที่จะรอถูกระบุโดย attribute ชื่อของ pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. ลงทะเบียนโมเดลที่ผ่านการปรับแต่งละเอียดกับ workspace

เราจะลงทะเบียนโมเดลจากผลลัพธ์ของงาน fine tuning ซึ่งจะติดตามความสัมพันธ์ระหว่างโมเดลที่ปรับแต่งละเอียดกับงาน fine tuning งาน fine tuning ยังติดตามความสัมพันธ์กับ foundation model, ข้อมูล และโค้ดการฝึกอบรม

### ลงทะเบียนโมเดล ML

1. สคริปต์ Python นี้ลงทะเบียนโมเดลแมชชีนเลิร์นนิงที่ฝึกใน Azure Machine Learning pipeline รายละเอียดดังนี้:

    - นำเข้ามอดูลที่จำเป็นจาก Azure AI ML SDK

    - ตรวจสอบว่าเอาต์พุต trained_model มีอยู่ในงาน pipeline หรือไม่ โดยเรียกใช้เมทอด get ของออบเจ็กต์ jobs ใน workspace_ml_client และเข้าถึงแอตทริบิวต์ outputs

    - สร้างเส้นทางไปยังโมเดลที่ฝึกโดยจัดรูปแบบสตริงด้วยชื่อของ pipeline job และชื่อของเอาต์พุต ("trained_model")

    - กำหนดชื่อสำหรับโมเดลที่ปรับแต่งละเอียดโดยต่อท้าย "-ultrachat-200k" กับชื่อโมเดลเดิม และแทนที่เครื่องหมายทับด้วยขีดกลาง

    - เตรียมลงทะเบียนโมเดลโดยสร้างออบเจ็กต์ Model ด้วยพารามิเตอร์ต่างๆ เช่น เส้นทางไปยังโมเดล ประเภทโมเดล (MLflow model) ชื่อและเวอร์ชันของโมเดล และคำอธิบายของโมเดล

    - ลงทะเบียนโมเดลโดยเรียกใช้เมทอด create_or_update ของออบเจ็กต์ models ใน workspace_ml_client พร้อมออบเจ็กต์ Model เป็นอาร์กิวเมนต์

    - พิมพ์โมเดลที่ลงทะเบียน

1. สรุปคือสคริปต์นี้กำลังลงทะเบียนโมเดลแมชชีนเลิร์นนิงที่ฝึกใน Azure Machine Learning pipeline
    
    ```python
    # นำเข้ามอดูลที่จำเป็นจาก Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # ตรวจสอบว่าเอาต์พุต `trained_model` มีอยู่จากงาน pipeline หรือไม่
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # สร้างเส้นทางไปยังโมเดลที่ผ่านการฝึกโดยจัดรูปแบบสตริงด้วยชื่อของงาน pipeline และชื่อของเอาต์พุต ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # กำหนดชื่อสำหรับโมเดลที่ปรับแต่งโดยเพิ่ม "-ultrachat-200k" ต่อท้ายชื่อโมเดลเดิมและแทนที่เครื่องหมายทับด้วยขีดกลาง
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # เตรียมลงทะเบียนโมเดลโดยการสร้างอ็อบเจ็กต์ Model พร้อมพารามิเตอร์ต่างๆ
    # ซึ่งรวมถึงเส้นทางไปยังโมเดล ประเภทของโมเดล (โมเดล MLflow) ชื่อและเวอร์ชันของโมเดล และคำอธิบายของโมเดล
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # ใช้เวลาปัจจุบันเป็นเวอร์ชันเพื่อหลีกเลี่ยงความขัดแย้งของเวอร์ชัน
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # ลงทะเบียนโมเดลโดยเรียกใช้เมธอด create_or_update ของอ็อบเจ็กต์ models ใน workspace_ml_client โดยมีอ็อบเจ็กต์ Model เป็นอาร์กิวเมนต์
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # แสดงผลโมเดลที่ลงทะเบียนแล้ว
    print("registered model: \n", registered_model)
    ```

## 7. ปรับใช้โมเดลที่ผ่านการปรับแต่งละเอียดไปยัง endpoint ออนไลน์

endpoint ออนไลน์ให้ REST API ที่ทนทานซึ่งสามารถใช้เชื่อมต่อกับแอปพลิเคชันที่ต้องการใช้โมเดลได้

### จัดการ Endpoint

1. สคริปต์ Python นี้สร้าง managed online endpoint ใน Azure Machine Learning สำหรับโมเดลที่ลงทะเบียน รายละเอียดดังนี้:

    - นำเข้ามอดูลที่จำเป็นจาก Azure AI ML SDK

    - กำหนดชื่อเฉพาะสำหรับ online endpoint โดยต่อท้าย timestamp กับสตริง "ultrachat-completion-"

    - เตรียมการสร้าง endpoint ออนไลน์โดยสร้างออบเจ็กต์ ManagedOnlineEndpoint ด้วยพารามิเตอร์ต่างๆ เช่น ชื่อ endpoint คำอธิบาย endpoint และโหมดการตรวจสอบสิทธิ์ ("key")

    - สร้าง online endpoint โดยเรียกใช้เมทอด begin_create_or_update ของ workspace_ml_client กับออบเจ็กต์ ManagedOnlineEndpoint จากนั้นรอการดำเนินการเสร็จสิ้นโดยเรียกใช้เมทอด wait

1. สรุปคือสคริปต์นี้สร้าง managed online endpoint ใน Azure Machine Learning สำหรับโมเดลที่ลงทะเบียน

    ```python
    # นำเข้ามอดูลที่จำเป็นจาก Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # กำหนดชื่อที่ไม่ซ้ำกันสำหรับ online endpoint โดยการเพิ่ม timestamp ต่อท้ายข้อความ "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # เตรียมสร้าง online endpoint โดยการสร้างวัตถุ ManagedOnlineEndpoint พร้อมพารามิเตอร์ต่างๆ
    # ซึ่งรวมถึงชื่อของ endpoint, คำอธิบายของ endpoint, และโหมดการตรวจสอบสิทธิ์ ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # สร้าง online endpoint โดยเรียกใช้เมธอด begin_create_or_update ของ workspace_ml_client พร้อมวัตถุ ManagedOnlineEndpoint เป็นอาร์กิวเมนต์
    # จากนั้นรอให้การทำงานสร้างเสร็จสมบูรณ์โดยการเรียกเมธอด wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> คุณสามารถพบรายการ SKU ที่สนับสนุนสำหรับการปรับใช้ที่นี่ — [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ปรับใช้โมเดล ML

1. สคริปต์ Python นี้ปรับใช้โมเดลแมชชีนเลิร์นนิงที่ลงทะเบียนไปยัง managed online endpoint ใน Azure Machine Learning รายละเอียดดังนี้:

    - นำเข้าโมดูล ast ซึ่งให้ฟังก์ชันสำหรับประมวลผลต้นไม้ไวยากรณ์เชิงนามธรรมของ Python

    - ตั้งชนิดอินสแตนซ์สำหรับการปรับใช้เป็น "Standard_NC6s_v3"

    - ตรวจสอบว่ามีแท็ก inference_compute_allow_list ใน foundation model หรือไม่ หากมี จะใช้ ast.literal_eval แปลงค่านี้จากสตริงเป็นลิสต์ Python และเก็บในตัวแปร inference_computes_allow_list หากไม่มี จะตั้งค่าเป็น None

    - ตรวจสอบว่าชนิดอินสแตนซ์ที่ระบุอยู่ในรายการอนุญาตหรือไม่ หากไม่ใช่ จะพิมพ์ข้อความแจ้งให้ผู้ใช้เลือกชนิดอินสแตนซ์จากรายการอนุญาต

    - เตรียมสร้าง deployment โดยสร้างออบเจ็กต์ ManagedOnlineDeployment พร้อมพารามิเตอร์ต่างๆ เช่น ชื่อ deployment, ชื่อ endpoint, ID โมเดล, ชนิดและจำนวนอินสแตนซ์, การตั้งค่า liveness probe และการตั้งค่าคำขอ

    - สร้าง deployment โดยเรียกใช้เมทอด begin_create_or_update ของ workspace_ml_client พร้อม ManagedOnlineDeployment จากนั้นรอการดำเนินการเสร็จสิ้นโดยเรียกใช้เมทอด wait

    - ตั้งค่าการจราจรของ endpoint ให้ส่ง 100% ไปยัง deployment ชื่อ "demo"

    - อัปเดต endpoint โดยเรียกใช้เมทอด begin_create_or_update ของ workspace_ml_client พร้อมออบเจ็กต์ endpoint จากนั้นรอการดำเนินการเสร็จสิ้นโดยเรียกใช้เมทอด result

1. สรุปคือสคริปต์นี้กำลังปรับใช้โมเดลแมชชีนเลิร์นนิงที่ลงทะเบียนไปยัง managed online endpoint ใน Azure Machine Learning

    ```python
    # นำเข้าโมดูล ast ซึ่งให้ฟังก์ชันสำหรับประมวลผลโครงสร้างต้นไม้ของไวยากรณ์นามธรรมของ Python
    import ast
    
    # ตั้งค่าประเภทอินสแตนซ์สำหรับการปรับใช้
    instance_type = "Standard_NC6s_v3"
    
    # ตรวจสอบว่ามีแท็ก `inference_compute_allow_list` อยู่ในโมเดลพื้นฐานหรือไม่
    if "inference_compute_allow_list" in foundation_model.tags:
        # หากมี ให้แปลงค่าของแท็กจากสตริงเป็นรายการของ Python และกำหนดค่าให้กับ `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # หากไม่มี ให้ตั้งค่า `inference_computes_allow_list` เป็น `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # ตรวจสอบว่าประเภทอินสแตนซ์ที่ระบุอยู่ในรายการอนุญาตหรือไม่
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # เตรียมสร้างการปรับใช้โดยการสร้างวัตถุ `ManagedOnlineDeployment` ด้วยพารามิเตอร์ต่างๆ
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # สร้างการปรับใช้โดยเรียกใช้เมธอด `begin_create_or_update` ของ `workspace_ml_client` โดยใช้วัตถุ `ManagedOnlineDeployment` เป็นอาร์กิวเมนต์
    # จากนั้นรอให้กระบวนการสร้างเสร็จสิ้นโดยเรียกใช้เมธอด `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # ตั้งค่าการจราจรของจุดสิ้นสุดเพื่อส่งการจราจร 100% ไปยังการปรับใช้ "demo"
    endpoint.traffic = {"demo": 100}
    
    # อัปเดตจุดสิ้นสุดโดยเรียกใช้เมธอด `begin_create_or_update` ของ `workspace_ml_client` โดยใช้วัตถุ `endpoint` เป็นอาร์กิวเมนต์
    # จากนั้นรอให้กระบวนการอัปเดตเสร็จสิ้นโดยเรียกใช้เมธอด `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. ทดสอบ endpoint ด้วยข้อมูลตัวอย่าง

เราจะดึงข้อมูลตัวอย่างจากชุดข้อมูลทดสอบและส่งไปยัง online endpoint เพื่อทำการอนุมาน จากนั้นจะแสดงผลป้ายคะแนนพร้อมกับป้ายชี้แจงที่แท้จริง

### อ่านผลลัพธ์

1. สคริปต์ Python นี้กำลังอ่านไฟล์ JSON Lines เข้าไปใน pandas DataFrame เลือกตัวอย่างแบบสุ่ม แล้วรีเซ็ตดัชนี รายละเอียดดังนี้:

    - อ่านไฟล์ ./ultrachat_200k_dataset/test_gen.jsonl เข้า pandas DataFrame ใช้ฟังก์ชัน read_json กับอาร์กิวเมนต์ lines=True เพราะไฟล์เป็นรูปแบบ JSON Lines ซึ่งแต่ละบรรทัดเป็นอ็อบเจ็กต์ JSON แยกกัน

    - เลือกตัวอย่างแบบสุ่มจำนวน 1 แถวจาก DataFrame โดยใช้ฟังก์ชัน sample กับอาร์กิวเมนต์ n=1 เพื่อระบุจำนวนแถวสุ่มที่เลือก

    - รีเซ็ตดัชนีของ DataFrame โดยใช้ฟังก์ชัน reset_index กับอาร์กิวเมนต์ drop=True เพื่อลบดัชนีเดิมและแทนที่ด้วยดัชนีใหม่เป็นเลขจำนวนเต็มเริ่มต้น

    - แสดง 2 แถวแรกของ DataFrame โดยใช้ฟังก์ชัน head กับอาร์กิวเมนต์ 2 อย่างไรก็ตามเนื่องจาก DataFrame มีเพียง 1 แถวหลังการสุ่ม จึงจะแสดงเพียงแถวนั้นแถวเดียว

1. สรุปคือสคริปต์นี้อ่านไฟล์ JSON Lines เข้า pandas DataFrame เลือกตัวอย่างแบบสุ่ม 1 แถว รีเซ็ตดัชนี และแสดงแถวแรก

    ```python
    # นำเข้าไลบรารี pandas
    import pandas as pd
    
    # อ่านไฟล์ JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' ลงใน pandas DataFrame
    # อาร์กิวเมนต์ 'lines=True' ระบุว่าไฟล์อยู่ในรูปแบบ JSON Lines ซึ่งแต่ละบรรทัดเป็นอ็อบเจ็กต์ JSON แยกกัน
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # เลือกตัวอย่างสุ่ม 1 แถวจาก DataFrame
    # อาร์กิวเมนต์ 'n=1' กำหนดจำนวนแถวสุ่มที่เลือก
    test_df = test_df.sample(n=1)
    
    # รีเซ็ตดัชนีของ DataFrame
    # อาร์กิวเมนต์ 'drop=True' ระบุให้ลบดัชนีเดิมและแทนที่ด้วยดัชนีใหม่ที่เป็นค่าจำนวนเต็มค่าเริ่มต้น
    # อาร์กิวเมนต์ 'inplace=True' ระบุให้แก้ไข DataFrame ในที่เดียวกัน (โดยไม่สร้างอ็อบเจ็กต์ใหม่)
    test_df.reset_index(drop=True, inplace=True)
    
    # แสดง 2 แถวแรกของ DataFrame
    # อย่างไรก็ตาม เนื่องจาก DataFrame มีแค่แถวเดียวหลังการสุ่ม จึงจะแสดงเพียงแถวนั้นเท่านั้น
    test_df.head(2)
    ```

### สร้างอ็อบเจ็กต์ JSON

1. สคริปต์ Python นี้กำลังสร้างอ็อบเจ็กต์ JSON ด้วยพารามิเตอร์เฉพาะและบันทึกลงไฟล์ รายละเอียดดังนี้:

    - นำเข้าโมดูล json ซึ่งให้ฟังก์ชันสำหรับทำงานกับข้อมูล JSON
    - มันสร้างพจนานุกรม parameters ที่มีคีย์และค่าซึ่งแทนพารามิเตอร์สำหรับโมเดลแมชชีนเลิร์นนิง คีย์คือ "temperature", "top_p", "do_sample", และ "max_new_tokens" และค่าที่สอดคล้องกันคือ 0.6, 0.9, True, และ 200 ตามลำดับ

    - มันสร้างพจนานุกรมอีกตัวชื่อ test_json โดยมีสองคีย์คือ "input_data" และ "params" ค่าใน "input_data" เป็นพจนานุกรมอีกตัวที่มีคีย์ "input_string" และ "parameters" ค่าใน "input_string" เป็นรายการที่มีข้อความแรกจาก DataFrame ชื่อ test_df ค่าใน "parameters" คือพจนานุกรม parameters ที่สร้างขึ้นก่อนหน้านี้ ค่าใน "params" เป็นพจนานุกรมว่าง

    - มันเปิดไฟล์ชื่อ sample_score.json
    
    ```python
    # นำเข้าโมดูล json ซึ่งให้ฟังก์ชันสำหรับทำงานกับข้อมูล JSON
    import json
    
    # สร้างพจนานุกรม `parameters` ที่มีคีย์และค่าซึ่งแทนพารามิเตอร์สำหรับโมเดลเรียนรู้ด้วยเครื่อง
    # คีย์คือ "temperature", "top_p", "do_sample" และ "max_new_tokens" โดยมีค่าตามลำดับคือ 0.6, 0.9, True และ 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # สร้างพจนานุกรมอีกตัว `test_json` ที่มีสองคีย์คือ "input_data" และ "params"
    # ค่าของ "input_data" เป็นพจนานุกรมอีกตัวที่มีคีย์ "input_string" และ "parameters"
    # ค่าของ "input_string" เป็นรายชื่อที่ประกอบด้วยข้อความแรกจาก DataFrame `test_df`
    # ค่าของ "parameters" คือพจนานุกรม `parameters` ที่สร้างไว้ก่อนหน้านี้
    # ค่าของ "params" คือพจนานุกรมว่าง
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # เปิดไฟล์ชื่อ `sample_score.json` ในไดเรกทอรี `./ultrachat_200k_dataset` ในโหมดเขียน
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # เขียนพจนานุกรม `test_json` ลงในไฟล์ในรูปแบบ JSON โดยใช้ฟังก์ชัน `json.dump`
        json.dump(test_json, f)
    ```

### การเรียกใช้ Endpoint

1. สคริปต์ Python นี้กำลังเรียกใช้ endpoint ออนไลน์ใน Azure Machine Learning เพื่อทำการให้คะแนนไฟล์ JSON นี่คือการอธิบายสิ่งที่ทำ:

    - มันเรียกใช้เมธอด invoke ของคุณสมบัติ online_endpoints ของอ็อบเจ็กต์ workspace_ml_client เมธอดนี้ใช้ส่งคำขอไปยัง endpoint ออนไลน์และรับการตอบกลับ

    - มันระบุชื่อ endpoint และการเปิดใช้ด้วยอาร์กิวเมนต์ endpoint_name และ deployment_name ในกรณีนี้ ชื่อ endpoint ถูกเก็บไว้ในตัวแปร online_endpoint_name และชื่อ deployment คือ "demo"

    - มันระบุเส้นทางไปยังไฟล์ JSON ที่จะให้คะแนนด้วยอาร์กิวเมนต์ request_file ในกรณีนี้ ไฟล์คือ ./ultrachat_200k_dataset/sample_score.json

    - มันเก็บการตอบกลับจาก endpoint ในตัวแปร response

    - มันพิมพ์การตอบกลับดิบ

1. สรุปคือ สคริปต์นี้กำลังเรียกใช้ endpoint ออนไลน์ใน Azure Machine Learning เพื่อให้คะแนนไฟล์ JSON และพิมพ์การตอบกลับ

    ```python
    # เรียกใช้ endpoint ออนไลน์ใน Azure Machine Learning เพื่อทำการสกอร์ไฟล์ `sample_score.json`
    # เมธอด `invoke` ของพร็อพเพอร์ตี้ `online_endpoints` ของอ็อบเจ็กต์ `workspace_ml_client` ใช้ส่งคำขอไปยัง endpoint ออนไลน์และรับการตอบกลับ
    # อาร์กิวเมนต์ `endpoint_name` ระบุชื่อของ endpoint ซึ่งเก็บอยู่ในตัวแปร `online_endpoint_name`
    # อาร์กิวเมนต์ `deployment_name` ระบุชื่อของการปรับใช้ซึ่งคือ "demo"
    # อาร์กิวเมนต์ `request_file` ระบุเส้นทางไปยังไฟล์ JSON ที่จะทำการสกอร์ คือ `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # พิมพ์การตอบกลับดิบจาก endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. ลบ online endpoint

1. อย่าลืมลบ online endpoint มิฉะนั้นคุณจะปล่อยให้มีการคิดค่าบริการตามการใช้งานคอมพิวต์ของ endpoint โค้ด Python บรรทัดนี้ลบ online endpoint ใน Azure Machine Learning นี่คือการอธิบายสิ่งที่ทำ:

    - มันเรียกใช้เมธอด begin_delete ของคุณสมบัติ online_endpoints ของอ็อบเจ็กต์ workspace_ml_client เมธอดนี้ใช้เริ่มต้นการลบ online endpoint

    - มันระบุชื่อของ endpoint ที่จะลบด้วยอาร์กิวเมนต์ name ในกรณีนี้ ชื่อ endpoint ถูกเก็บไว้ในตัวแปร online_endpoint_name

    - มันเรียกใช้เมธอด wait เพื่อรอให้การลบเสร็จสิ้น นี่คือการดำเนินการแบบบล็อก ซึ่งหมายความว่าจะป้องกันไม่ให้สคริปต์ดำเนินต่อจนกว่าการลบจะเสร็จสมบูรณ์

    - สรุปคือ บรรทัดนี้เริ่มต้นการลบ online endpoint ใน Azure Machine Learning และรอให้การดำเนินการเสร็จสิ้น

    ```python
    # ลบจุดสิ้นสุดออนไลน์ใน Azure Machine Learning
    # เมธอด `begin_delete` ของพร็อพเพอร์ตี้ `online_endpoints` ของออบเจ็กต์ `workspace_ml_client` ถูกใช้เพื่อเริ่มการลบจุดสิ้นสุดออนไลน์
    # อาร์กิวเมนต์ `name` ระบุชื่อของจุดสิ้นสุดที่จะถูกลบ ซึ่งถูกเก็บอยู่ในตัวแปร `online_endpoint_name`
    # เมธอด `wait` ถูกเรียกใช้เพื่อรอให้การดำเนินการลบเสร็จสมบูรณ์ นี่คือการดำเนินการแบบบล็อก ซึ่งหมายความว่าจะป้องกันสคริปต์ไม่ให้ดำเนินต่อจนกว่าการลบจะเสร็จสิ้น
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) ถึงแม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลด้วยระบบอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->