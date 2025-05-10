<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-09T21:13:08+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "th"
}
-->
## วิธีใช้ chat-completion components จาก Azure ML system registry เพื่อปรับแต่งโมเดล

ในตัวอย่างนี้เราจะทำการปรับแต่งโมเดล Phi-3-mini-4k-instruct เพื่อให้โมเดลสามารถตอบสนทนาระหว่างคนสองคนโดยใช้ชุดข้อมูล ultrachat_200k

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.th.png)

ตัวอย่างนี้จะแสดงวิธีการปรับแต่งโมเดลโดยใช้ Azure ML SDK และ Python จากนั้นนำโมเดลที่ปรับแต่งแล้วไปใช้งานบน endpoint ออนไลน์เพื่อทำการทำนายแบบเรียลไทม์

### ข้อมูลสำหรับการฝึก

เราจะใช้ชุดข้อมูล ultrachat_200k ซึ่งเป็นเวอร์ชันที่ถูกกรองอย่างเข้มข้นของชุดข้อมูล UltraChat และถูกใช้ในการฝึก Zephyr-7B-β ซึ่งเป็นโมเดลแชท 7b ที่ทันสมัยที่สุด

### โมเดล

เราจะใช้โมเดล Phi-3-mini-4k-instruct เพื่อแสดงวิธีที่ผู้ใช้สามารถปรับแต่งโมเดลสำหรับงาน chat-completion หากคุณเปิดโน้ตบุ๊กนี้มาจากการ์ดโมเดลเฉพาะ โปรดจำไว้ว่าให้เปลี่ยนชื่อโมเดลให้ตรงกับโมเดลที่คุณใช้

### งานที่ต้องทำ

- เลือกโมเดลที่จะปรับแต่ง
- เลือกและสำรวจข้อมูลสำหรับการฝึก
- กำหนดค่าการทำงานของงานปรับแต่ง
- รันงานปรับแต่ง
- ตรวจสอบเมตริกการฝึกและประเมินผล
- ลงทะเบียนโมเดลที่ปรับแต่งแล้ว
- นำโมเดลที่ปรับแต่งไปใช้งานแบบเรียลไทม์
- ทำความสะอาดทรัพยากร

## 1. ตั้งค่าความพร้อมเบื้องต้น

- ติดตั้ง dependencies
- เชื่อมต่อกับ AzureML Workspace ดูรายละเอียดเพิ่มเติมได้ที่ set up SDK authentication โดยเปลี่ยน <WORKSPACE_NAME>, <RESOURCE_GROUP> และ <SUBSCRIPTION_ID> ตามที่เหมาะสม
- เชื่อมต่อกับ azureml system registry
- กำหนดชื่องานทดลอง (experiment) ที่ต้องการ (ถ้ามี)
- ตรวจสอบหรือสร้าง compute

> [!NOTE]
> ความต้องการคือโหนด GPU เดียวสามารถมีการ์ด GPU หลายใบได้ เช่น ในโหนด Standard_NC24rs_v3 มี NVIDIA V100 GPUs 4 ใบ ขณะที่ Standard_NC12s_v3 มี 2 ใบ ดูเอกสารสำหรับข้อมูลนี้ จำนวนการ์ด GPU ต่อโหนดถูกตั้งไว้ในพารามิเตอร์ gpus_per_node ด้านล่าง การตั้งค่านี้ให้ถูกต้องจะช่วยให้ใช้ GPU ทุกใบในโหนดได้อย่างเต็มที่ SKU ของ GPU compute ที่แนะนำสามารถดูได้ที่นี่และที่นี่

### ไลบรารี Python

ติดตั้ง dependencies โดยรันเซลล์ด้านล่าง ขั้นตอนนี้ไม่ใช่ตัวเลือกถ้ารันในสภาพแวดล้อมใหม่

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### การโต้ตอบกับ Azure ML

1. สคริปต์ Python นี้ใช้สำหรับโต้ตอบกับบริการ Azure Machine Learning (Azure ML) โดยมีรายละเอียดดังนี้:

    - นำเข้าโมดูลที่จำเป็นจาก azure.ai.ml, azure.identity และ azure.ai.ml.entities รวมถึงโมดูล time

    - พยายามทำการยืนยันตัวตนโดยใช้ DefaultAzureCredential() ซึ่งช่วยให้การยืนยันตัวตนง่ายขึ้นสำหรับการพัฒนาแอปพลิเคชันบนคลาวด์ Azure หากล้มเหลวจะใช้ InteractiveBrowserCredential() ซึ่งจะเปิดหน้าต่างล็อกอินแบบโต้ตอบ

    - จากนั้นพยายามสร้างอินสแตนซ์ MLClient โดยใช้เมธอด from_config ซึ่งอ่านค่าคอนฟิกจากไฟล์ config.json หากล้มเหลวจะสร้าง MLClient โดยระบุ subscription_id, resource_group_name และ workspace_name ด้วยตนเอง

    - สร้างอินสแตนซ์ MLClient อีกตัวหนึ่งสำหรับ Azure ML registry ชื่อ "azureml" ซึ่งเป็นที่เก็บโมเดล, pipeline สำหรับการปรับแต่ง และสภาพแวดล้อม

    - กำหนดชื่อ experiment_name เป็น "chat_completion_Phi-3-mini-4k-instruct"

    - สร้าง timestamp ที่ไม่ซ้ำกันโดยแปลงเวลาปัจจุบัน (วินาทีตั้งแต่ epoch) เป็นจำนวนเต็มและแปลงเป็นสตริง เพื่อใช้สร้างชื่อหรือเวอร์ชันที่ไม่ซ้ำกัน

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. เลือก foundation model สำหรับการปรับแต่ง

1. Phi-3-mini-4k-instruct เป็นโมเดลขนาด 3.8 พันล้านพารามิเตอร์ น้ำหนักเบา และเป็น state-of-the-art ที่สร้างขึ้นบนชุดข้อมูลของ Phi-2 โมเดลนี้อยู่ในตระกูล Phi-3 และเวอร์ชัน Mini มีสองแบบคือ 4K และ 128K ซึ่งหมายถึงความยาวของ context (หน่วยเป็น tokens) ที่รองรับ เราต้องปรับแต่งโมเดลให้เหมาะกับการใช้งานเฉพาะ คุณสามารถเรียกดูโมเดลเหล่านี้ใน Model Catalog ของ AzureML Studio โดยกรองตามงาน chat-completion ในตัวอย่างนี้เราใช้ Phi-3-mini-4k-instruct หากคุณเปิดโน้ตบุ๊กนี้สำหรับโมเดลอื่น โปรดเปลี่ยนชื่อและเวอร์ชันของโมเดลให้เหมาะสม

    > [!NOTE]
    > model id ของโมเดลนี้จะถูกส่งเป็น input ให้กับงานปรับแต่ง นอกจากนี้ยังสามารถดูได้ในช่อง Asset ID บนหน้ารายละเอียดโมเดลใน Model Catalog ของ AzureML Studio

2. สคริปต์ Python นี้โต้ตอบกับบริการ Azure Machine Learning (Azure ML) โดยมีรายละเอียดดังนี้:

    - กำหนด model_name เป็น "Phi-3-mini-4k-instruct"

    - ใช้เมธอด get ของ models ใน registry_ml_client เพื่อดึงเวอร์ชันล่าสุดของโมเดลที่มีชื่อนี้จาก Azure ML registry โดยส่งชื่อโมเดลและ label เพื่อดึงเวอร์ชันล่าสุด

    - พิมพ์ข้อความแจ้งชื่อ โมเดล เวอร์ชัน และ id ของโมเดลที่จะใช้ในการปรับแต่ง โดยใช้เมธอด format เพื่อแทรกข้อมูลเหล่านี้ในข้อความ ชื่อ เวอร์ชัน และ id ของโมเดลถูกเข้าถึงผ่าน property ของ foundation_model

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. สร้าง compute สำหรับใช้งานกับงาน

งาน finetune ใช้งานได้เฉพาะกับ GPU compute เท่านั้น ขนาดของ compute ขึ้นอยู่กับขนาดของโมเดล และในหลายกรณีอาจยากที่จะเลือก compute ที่เหมาะสม สำหรับเซลล์นี้เราจะช่วยแนะนำให้ผู้ใช้เลือก compute ที่เหมาะสม

> [!NOTE]
> Compute ที่ระบุด้านล่างทำงานด้วยการตั้งค่าที่เหมาะสมที่สุด หากเปลี่ยนแปลงการตั้งค่าอาจทำให้เกิดข้อผิดพลาด Cuda Out Of Memory ได้ ในกรณีนี้ให้ลองอัปเกรด compute เป็นขนาดที่ใหญ่ขึ้น

> [!NOTE]
> ขณะเลือก compute_cluster_size ด้านล่าง ให้ตรวจสอบว่า compute นั้นมีอยู่ใน resource group ของคุณ หาก compute ใดไม่พร้อมใช้งาน คุณสามารถร้องขอเพื่อเข้าถึงทรัพยากร compute นั้นได้

### ตรวจสอบว่าโมเดลรองรับการปรับแต่งหรือไม่

1. สคริปต์ Python นี้โต้ตอบกับโมเดลใน Azure Machine Learning (Azure ML) โดยมีรายละเอียดดังนี้:

    - นำเข้าโมดูล ast ซึ่งมีฟังก์ชันสำหรับประมวลผลโครงสร้างไวยากรณ์ของ Python

    - ตรวจสอบว่า foundation_model มีแท็กชื่อ finetune_compute_allow_list หรือไม่ แท็กใน Azure ML คือคู่ key-value ที่ใช้สร้างและกรองโมเดล

    - หากมีแท็ก finetune_compute_allow_list จะใช้ฟังก์ชัน ast.literal_eval เพื่อแปลงค่าของแท็ก (ซึ่งเป็นสตริง) ให้เป็นลิสต์ของ Python จากนั้นกำหนดให้ตัวแปร computes_allow_list และพิมพ์ข้อความแจ้งว่าควรสร้าง compute จากลิสต์นี้

    - หากไม่มีแท็กนี้ จะกำหนด computes_allow_list เป็น None และพิมพ์ข้อความแจ้งว่าแท็กนี้ไม่มีในแท็กของโมเดล

    - สรุปคือสคริปต์นี้ตรวจสอบแท็กเฉพาะใน metadata ของโมเดล แปลงค่าของแท็กเป็นลิสต์หากมี และแจ้งผลให้ผู้ใช้ทราบ

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### ตรวจสอบ Compute Instance

1. สคริปต์ Python นี้โต้ตอบกับ Azure Machine Learning (Azure ML) และตรวจสอบ compute instance หลายอย่าง รายละเอียดดังนี้:

    - พยายามดึง compute instance ที่มีชื่อเก็บในตัวแปร compute_cluster จาก Azure ML workspace หากสถานะ provisioning ของ compute instance คือ "failed" จะโยนข้อผิดพลาด ValueError

    - ตรวจสอบว่าตัวแปร computes_allow_list ไม่ใช่ None หากไม่ใช่ จะเปลี่ยนชื่อขนาด compute ในลิสต์เป็นตัวพิมพ์เล็กทั้งหมด แล้วตรวจสอบว่าขนาดของ compute instance ปัจจุบันอยู่ในลิสต์นี้หรือไม่ หากไม่อยู่ จะโยนข้อผิดพลาด ValueError

    - หาก computes_allow_list เป็น None จะตรวจสอบว่าขนาด compute instance อยู่ในลิสต์ขนาด GPU VM ที่ไม่รองรับหรือไม่ หากใช่ จะโยนข้อผิดพลาด ValueError

    - ดึงลิสต์ขนาด compute ทั้งหมดที่มีใน workspace แล้ววนลูปตรวจสอบแต่ละขนาด ถ้าชื่อขนาดตรงกับ compute instance ปัจจุบัน จะดึงจำนวน GPU ของ compute นั้นและตั้งค่า gpu_count_found เป็น True

    - ถ้า gpu_count_found เป็น True จะพิมพ์จำนวน GPU ของ compute instance ถ้าไม่ใช่ จะโยนข้อผิดพลาด ValueError

    - สรุปคือสคริปต์นี้ตรวจสอบสถานะ provisioning, ขนาด compute ว่าอยู่ในลิสต์อนุญาตหรือปฏิเสธ และจำนวน GPU ของ compute instance ใน Azure ML workspace

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. เลือกชุดข้อมูลสำหรับการปรับแต่งโมเดล

1. เราใช้ชุดข้อมูล ultrachat_200k ชุดข้อมูลนี้แบ่งเป็นสี่ส่วน เหมาะสำหรับการปรับแต่งแบบ Supervised fine-tuning (sft) และ Generation ranking (gen) จำนวนตัวอย่างในแต่ละส่วนแสดงดังนี้:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. เซลล์ถัดไปแสดงการเตรียมข้อมูลพื้นฐานสำหรับการปรับแต่ง:

### แสดงข้อมูลบางแถว

เราต้องการให้ตัวอย่างนี้รันได้เร็ว จึงบันทึกไฟล์ train_sft และ test_sft ที่มีข้อมูล 5% ของแถวที่ถูกตัดมาแล้ว ซึ่งหมายความว่าโมเดลที่ปรับแต่งจะมีความแม่นยำน้อยลง ดังนั้นไม่ควรนำไปใช้ในงานจริง
ไฟล์ download-dataset.py ใช้สำหรับดาวน์โหลดชุดข้อมูล ultrachat_200k และแปลงชุดข้อมูลให้อยู่ในรูปแบบที่ pipeline การปรับแต่งใช้งานได้ เนื่องจากชุดข้อมูลมีขนาดใหญ่ เราจึงใช้เพียงส่วนหนึ่งของชุดข้อมูลเท่านั้น

1. การรันสคริปต์ด้านล่างจะดาวน์โหลดข้อมูลเพียง 5% เท่านั้น สามารถเพิ่มได้โดยเปลี่ยนพารามิเตอร์ dataset_split_pc เป็นเปอร์เซ็นต์ที่ต้องการ

    > [!NOTE]
    > โมเดลภาษาบางตัวมีรหัสภาษาที่ต่างกัน ดังนั้นชื่อคอลัมน์ในชุดข้อมูลควรสอดคล้องกับรหัสภาษาเหล่านั้น

1. ตัวอย่างรูปแบบข้อมูลที่ควรเป็น
ชุดข้อมูล chat-completion เก็บในรูปแบบ parquet โดยแต่ละรายการใช้สคีมาแบบนี้:

    - นี่คือเอกสาร JSON (JavaScript Object Notation) ซึ่งเป็นรูปแบบแลกเปลี่ยนข้อมูลยอดนิยม ไม่ใช่โค้ดที่รันได้ แต่เป็นวิธีเก็บและส่งข้อมูล โครงสร้างมีดังนี้:

    - "prompt": คีย์นี้เก็บข้อความที่เป็นงานหรือคำถามที่ส่งให้ AI assistant

    - "messages": คีย์นี้เก็บอาเรย์ของอ็อบเจ็กต์ แต่ละอ็อบเจ็กต์แทนข้อความในการสนทนาระหว่างผู้ใช้และ AI assistant โดยแต่ละข้อความมีคีย์สองตัวคือ:

    - "content": ข้อความของข้อความนั้น
    - "role": บทบาทของผู้ส่งข้อความ อาจเป็น "user" หรือ "assistant"
    - "prompt_id": ตัวระบุเฉพาะของ prompt นี้

1. ในเอกสาร JSON นี้ แสดงการสนทนาที่ผู้ใช้ขอให้ AI assistant สร้างตัวเอกสำหรับเรื่องราว dystopian ผู้ช่วยตอบกลับ และผู้ใช้ขอรายละเอียดเพิ่มเติม ผู้ช่วยยินดีให้ข้อมูลเพิ่มเติม การสนทนาทั้งหมดนี้เชื่อมโยงกับ prompt id เฉพาะ

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

1. สคริปต์ Python นี้ใช้ดาวน์โหลดชุดข้อมูลโดยใช้สคริปต์ช่วยชื่อ download-dataset.py รายละเอียดดังนี้:

    - นำเข้าโมดูล os ซึ่งช่วยให้ใช้งานฟังก์ชันที่ขึ้นกับระบบปฏิบัติการได้

    - ใช้ os.system เพื่อรันสคริปต์ download-dataset.py ในเชลล์ พร้อมอาร์กิวเมนต์ระบุชุดข้อมูลที่จะดาวน์โหลด (HuggingFaceH4/ultrachat_200k), โฟลเดอร์ที่จะดาวน์โหลด (ultrachat_200k_dataset), และเปอร์เซ็นต์ของชุดข้อมูลที่จะใช้แบ่ง (5) ค่าที่คืนจาก os.system เก็บในตัวแปร exit_status

    - ตรวจสอบว่า exit_status ไม่เท่ากับ 0 หรือไม่ โดย 0 หมายถึงคำสั่งรันสำเร็จ หากไม่ใช่จะโยน Exception พร้อมข้อความว่าเกิดข้อผิดพลาดในการดาวน์โหลดชุดข้อมูล

    - สรุปคือสคริปต์นี้รันคำสั่งดาวน์โหลดชุดข้อมูลโดยใช้สคริปต์ช่วย และแจ้งข้อผิดพลาดถ้าคำสั่งล้มเหลว

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### โหลดข้อมูลเข้า DataFrame

1. สคริปต์ Python นี้โหลดไฟล์ JSON Lines เข้า pandas DataFrame และแสดง 5 แถวแรก รายละเอียดดังนี้:

    - นำเข้าไลบรารี pandas ซึ่งเป็นไลบรารีสำหรับจัดการและวิเคราะห์ข้อมูล

    - กำหนดค่าตัวเลือก pandas ให้แสดงความกว้างของคอลัมน์แบบเต็มโดยไม่ตัดข้อความ

    - ใช้ pd.read_json โหลดไฟล์ train_sft.jsonl จากโฟลเดอร์ ultrachat_200k_dataset โดยกำหนด lines=True เพราะไฟล์เป็น JSON Lines ซึ่งแต่ละบรรทัดเป็นอ็อบเจ็กต์ JSON แยกกัน

    - ใช้เมธอด head เพื่อแสดง 5 แถวแรก หาก DataFrame มีน้อยกว่า 5 แถวจะแสดงทั้งหมด

    - สรุปคือสคริปต์นี้โหลดไฟล์ JSON Lines เข้า DataFrame และแสดง 5 แถวแรกพร้อมแสดงข้อความเต็มในแต่ละคอลัมน์

    ```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. ส่งงาน fine tuning โดยใช้โมเดลและข้อมูลเป็น input

สร้างงานที่ใช้ chat-completion pipeline component ดูรายละเอียดพารามิเตอร์ทั้งหมดที่รองรับการปรับแต่งได้เพิ่มเติม

### กำหนดพารามิเตอร์สำหรับการปรับแต่ง

1. พารามิเตอร์การปรับแต่งแบ่งออกเป็น 2 กลุ่ม คือ พารามิเตอร์การฝึก และพารามิเตอร์การปรับแต่งประสิทธิภาพ

1. พารามิเตอร์การฝึกกำหนดลักษณะการฝึก เช่น

    - ตัว optimizer และ scheduler ที่ใช้
    - เมตริกที่ใช้วัดผลการปรับแต่ง
    - จำนวนขั้นตอนการฝึก ขนาด batch และอื่นๆ
    - พารามิเตอร์การปรับแต่งประสิทธิภาพช่วยเพิ่มประสิทธิภาพการใช้หน่วยความจำ GPU และใช้ทรัพยากรคอมพิวต์ได้อย่างมีประสิทธิภาพ

1. ด้านล่างนี้เป็นพารามิเตอร์บางส่วนในกลุ่มนี้ ซึ่งแตกต่างกันไปตามแต่ละโมเดลและถูกแพ็กเกจมาพร้อมกับโมเดลเพื่อจัดการความแตกต่างเหล่านี้

    - เปิดใช้งาน deepspeed และ LoRA
    - เปิดใช้งาน mixed precision training
    - เปิดใช้งาน multi-node training

> [!NOTE]
> การปรับแต่งแบบ supervised อาจทำให้โมเดลสูญเสีย alignment หรือเกิด forgetting อย่างรุนแรง แนะนำให้ตรวจสอบปัญหานี้และรันขั้นตอน alignment หลังจากปรับแต่งเสร็จ

### พารามิเตอร์ Fine Tuning

1. สคริปต์ Python นี้ตั้งค่าพารามิเตอร์สำหรับการปรับแต่งโมเดล machine learning รายละเอียดดังนี้:

    - ตั้งค่าพารามิเตอร์การฝึกเริ่มต้น เช่น จำนวน epoch, batch size สำหรับฝึกและประเมินผล, อัตราการเรียนรู้, และชนิดของ learning rate scheduler

    - ตั้งค่าพารามิเตอร์การปรับแต่งเริ่มต้น เช่น เปิดใช้งาน Layer-wise Relevance Propagation (LoRa) และ DeepSpeed หรือไม่ และกำหนด stage ของ DeepSpeed

    - รวมพารามิเตอร์การฝึกและการปรับแต่งไว้ในดิกชันนารีเดียวชื่อ finetune_parameters

    - ตรวจสอบว่า foundation_model มีพารามิเตอร์เริ่มต้นเฉพาะโมเดลหรือไม่ หากมีจะแสดงข้อความเตือนและอัปเดต finetune_parameters ด้วยพารามิเตอร์เฉพาะโมเดล โดยใช้ ast.literal_eval เพื่อแปลงค่าจากสตริงเป็นดิกชันนารี Python

    - พิมพ์พารามิเตอร์การปรับแต่งที่ใช้ในรันนี้


training pipeline ที่อิงจากพารามิเตอร์ต่างๆ แล้วแสดงชื่อที่ใช้แสดงผลนี้ ```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
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
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### การกำหนดค่า Pipeline

สคริปต์ Python นี้กำลังนิยามและกำหนดค่า machine learning pipeline โดยใช้ Azure Machine Learning SDK รายละเอียดของสิ่งที่ทำมีดังนี้:
1. นำเข้ามอดูลที่จำเป็นจาก Azure AI ML SDK
1. ดึง pipeline component ที่ชื่อว่า "chat_completion_pipeline" จาก registry
1. กำหนด pipeline job โดยใช้ `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False` หมายความว่า pipeline จะหยุดทำงานถ้ามีขั้นตอนใดล้มเหลว
1. สรุปคือ สคริปต์นี้กำหนดและตั้งค่า machine learning pipeline สำหรับงาน chat completion โดยใช้ Azure Machine Learning SDK

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### การส่งงาน (Submit the Job)

1. สคริปต์ Python นี้กำลังส่งงาน machine learning pipeline job ไปยัง Azure Machine Learning workspace และรอจนกว่างานจะเสร็จสิ้น รายละเอียดของสิ่งที่ทำมีดังนี้:
- เรียกใช้เมธอด create_or_update ของ jobs ใน workspace_ml_client เพื่อส่ง pipeline job โดย pipeline ที่จะรันถูกระบุโดย pipeline_object และ experiment ที่จะรันงานถูกระบุโดย experiment_name
- จากนั้นเรียกใช้เมธอด stream ของ jobs ใน workspace_ml_client เพื่อรอให้ pipeline job เสร็จสิ้น งานที่รอถูกระบุโดย name attribute ของ pipeline_job object
- สรุปคือ สคริปต์นี้ส่งงาน machine learning pipeline job ไปยัง Azure Machine Learning workspace และรอจนกว่างานจะเสร็จ

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. ลงทะเบียนโมเดลที่ผ่านการ fine tune กับ workspace

เราจะลงทะเบียนโมเดลจากผลลัพธ์ของงาน fine tuning ซึ่งจะติดตาม lineage ระหว่างโมเดลที่ผ่านการ fine tune กับงาน fine tuning นั้นๆ งาน fine tuning ยังติดตาม lineage ไปยัง foundation model, ข้อมูล และโค้ดการฝึกอบรม

### การลงทะเบียน ML Model

1. สคริปต์ Python นี้กำลังลงทะเบียนโมเดล machine learning ที่ผ่านการฝึกใน Azure Machine Learning pipeline รายละเอียดของสิ่งที่ทำมีดังนี้:
- นำเข้ามอดูลที่จำเป็นจาก Azure AI ML SDK
- ตรวจสอบว่า trained_model output มีอยู่ใน pipeline job หรือไม่ โดยเรียกใช้เมธอด get ของ jobs ใน workspace_ml_client และเข้าถึง outputs attribute
- สร้าง path ไปยังโมเดลที่ฝึกโดยการจัดรูปแบบสตริงโดยใช้ชื่อ pipeline job และชื่อ output ("trained_model")
- กำหนดชื่อสำหรับโมเดลที่ผ่านการ fine tune โดยเพิ่ม "-ultrachat-200k" ต่อท้ายชื่อโมเดลเดิมและแทนที่ slash ด้วย hyphen
- เตรียมการลงทะเบียนโมเดลโดยสร้าง Model object พร้อมพารามิเตอร์ต่างๆ รวมถึง path ของโมเดล, ประเภทของโมเดล (MLflow model), ชื่อและเวอร์ชันของโมเดล และคำอธิบายของโมเดล
- ลงทะเบียนโมเดลโดยเรียกใช้เมธอด create_or_update ของ models ใน workspace_ml_client พร้อมส่ง Model object เป็นอาร์กิวเมนต์
- แสดงโมเดลที่ลงทะเบียนแล้ว

1. สรุปคือ สคริปต์นี้กำลังลงทะเบียนโมเดล machine learning ที่ผ่านการฝึกใน Azure Machine Learning pipeline

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. นำโมเดลที่ผ่านการ fine tune ไป deploy ที่ online endpoint

Online endpoints ให้ REST API ที่ทนทานและสามารถใช้เชื่อมต่อกับแอปพลิเคชันที่ต้องการใช้โมเดลนี้

### การจัดการ Endpoint

1. สคริปต์ Python นี้กำลังสร้าง managed online endpoint ใน Azure Machine Learning สำหรับโมเดลที่ลงทะเบียนแล้ว รายละเอียดของสิ่งที่ทำมีดังนี้:
- นำเข้ามอดูลที่จำเป็นจาก Azure AI ML SDK
- กำหนดชื่อเฉพาะสำหรับ online endpoint โดยเพิ่ม timestamp ต่อท้ายสตริง "ultrachat-completion-"
- เตรียมสร้าง online endpoint โดยสร้าง ManagedOnlineEndpoint object พร้อมพารามิเตอร์ต่างๆ เช่น ชื่อ endpoint, คำอธิบาย endpoint และโหมดการยืนยันตัวตน ("key")
- สร้าง online endpoint โดยเรียกใช้เมธอด begin_create_or_update ของ workspace_ml_client พร้อมส่ง ManagedOnlineEndpoint object เป็นอาร์กิวเมนต์ แล้วรอจนกระทั่งการสร้างเสร็จสิ้นโดยเรียก wait

1. สรุปคือ สคริปต์นี้กำลังสร้าง managed online endpoint ใน Azure Machine Learning สำหรับโมเดลที่ลงทะเบียนแล้ว

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> คุณสามารถดูรายชื่อ SKU ที่รองรับสำหรับการ deploy ได้ที่นี่ - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### การ deploy ML Model

1. สคริปต์ Python นี้กำลัง deploy โมเดล machine learning ที่ลงทะเบียนแล้วไปยัง managed online endpoint ใน Azure Machine Learning รายละเอียดของสิ่งที่ทำมีดังนี้:

    - นำเข้าโมดูล ast ซึ่งให้ฟังก์ชันสำหรับจัดการโครงสร้างไวยากรณ์ Python แบบต้นไม้

    - กำหนด instance type สำหรับการ deploy เป็น "Standard_NC6s_v3"

    - ตรวจสอบว่ามีแท็ก inference_compute_allow_list อยู่ใน foundation model หรือไม่ ถ้ามีจะเปลี่ยนค่าจากสตริงเป็นลิสต์ Python และเก็บไว้ใน inference_computes_allow_list ถ้าไม่มีจะตั้งค่า inference_computes_allow_list เป็น None

    - ตรวจสอบว่า instance type ที่ระบุอยู่ใน allow list หรือไม่ ถ้าไม่อยู่จะแสดงข้อความแจ้งให้ผู้ใช้เลือก instance type จาก allow list

    - เตรียมสร้าง deployment โดยสร้าง ManagedOnlineDeployment object พร้อมพารามิเตอร์ต่างๆ เช่น ชื่อ deployment, ชื่อ endpoint, ID ของโมเดล, instance type และจำนวน instance, การตั้งค่า liveness probe และการตั้งค่า request

    - สร้าง deployment โดยเรียกใช้เมธอด begin_create_or_update ของ workspace_ml_client พร้อมส่ง ManagedOnlineDeployment object เป็นอาร์กิวเมนต์ แล้วรอจนกระทั่งการสร้างเสร็จสิ้นโดยเรียก wait

    - ตั้งค่า traffic ของ endpoint ให้ส่ง 100% ของ traffic ไปยัง deployment ชื่อ "demo"

    - อัปเดต endpoint โดยเรียกใช้เมธอด begin_create_or_update ของ workspace_ml_client พร้อมส่ง endpoint object เป็นอาร์กิวเมนต์ แล้วรอจนกระทั่งการอัปเดตเสร็จสิ้นโดยเรียก result

1. สรุปคือ สคริปต์นี้กำลัง deploy โมเดล machine learning ที่ลงทะเบียนแล้วไปยัง managed online endpoint ใน Azure Machine Learning

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. ทดสอบ endpoint ด้วยข้อมูลตัวอย่าง

เราจะดึงข้อมูลตัวอย่างจากชุดข้อมูลทดสอบและส่งไปยัง online endpoint เพื่อทำการ inference จากนั้นจะแสดงผลป้ายคะแนนควบคู่กับป้ายคำตอบจริง

### การอ่านผลลัพธ์

1. สคริปต์ Python นี้กำลังอ่านไฟล์ JSON Lines เข้าเป็น pandas DataFrame, เลือกตัวอย่างแบบสุ่ม, และรีเซ็ตดัชนี รายละเอียดของสิ่งที่ทำมีดังนี้:

    - อ่านไฟล์ ./ultrachat_200k_dataset/test_gen.jsonl เข้าเป็น pandas DataFrame โดยใช้ฟังก์ชัน read_json พร้อมอาร์กิวเมนต์ lines=True เพราะไฟล์นี้เป็น JSON Lines ที่แต่ละบรรทัดเป็น JSON object แยกกัน

    - เลือกตัวอย่างแบบสุ่ม 1 แถวจาก DataFrame โดยใช้ฟังก์ชัน sample พร้อมอาร์กิวเมนต์ n=1 เพื่อระบุจำนวนแถวที่สุ่มเลือก

    - รีเซ็ตดัชนีของ DataFrame โดยใช้ฟังก์ชัน reset_index พร้อมอาร์กิวเมนต์ drop=True เพื่อลบดัชนีเดิมและแทนที่ด้วยดัชนีใหม่ที่เป็นค่าเต็มจำนวนเริ่มต้น

    - แสดง 2 แถวแรกของ DataFrame โดยใช้ฟังก์ชัน head กับอาร์กิวเมนต์ 2 อย่างไรก็ตามเนื่องจาก DataFrame มีเพียง 1 แถวหลังจากการสุ่ม จึงจะแสดงเพียงแถวนั้นแถวเดียว

1. สรุปคือ สคริปต์นี้กำลังอ่านไฟล์ JSON Lines เข้าเป็น pandas DataFrame, เลือกตัวอย่างแบบสุ่ม 1 แถว, รีเซ็ตดัชนี และแสดงแถวแรก

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### การสร้าง JSON Object

1. สคริปต์ Python นี้กำลังสร้าง JSON object ด้วยพารามิเตอร์เฉพาะและบันทึกลงไฟล์ รายละเอียดของสิ่งที่ทำมีดังนี้:

    - นำเข้าโมดูล json ซึ่งให้ฟังก์ชันสำหรับจัดการข้อมูล JSON

    - สร้างพจนานุกรม parameters ที่มีคีย์และค่าซึ่งแทนพารามิเตอร์สำหรับโมเดล machine learning โดยคีย์ได้แก่ "temperature", "top_p", "do_sample", และ "max_new_tokens" ซึ่งมีค่าตามลำดับคือ 0.6, 0.9, True และ 200

    - สร้างพจนานุกรม test_json อีกชุดหนึ่งที่มีสองคีย์คือ "input_data" และ "params" โดยค่าของ "input_data" เป็นพจนานุกรมอีกชุดหนึ่งที่มีคีย์ "input_string" และ "parameters" โดยค่าของ "input_string" เป็นลิสต์ที่เก็บข้อความแรกจาก test_df DataFrame ส่วนค่าของ "parameters" คือพจนานุกรม parameters ที่สร้างไว้ก่อนหน้า ค่าของ "params" เป็นพจนานุกรมว่าง

    - เปิดไฟล์ชื่อ sample_score.json

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### การเรียกใช้ Endpoint

1. สคริปต์ Python นี้กำลังเรียกใช้ online endpoint ใน Azure Machine Learning เพื่อทำการสกอร์ไฟล์ JSON รายละเอียดของสิ่งที่ทำมีดังนี้:

    - เรียกใช้เมธอด invoke ของ online_endpoints ใน workspace_ml_client ซึ่งใช้ส่งคำขอไปยัง online endpoint และรับคำตอบกลับ

    - ระบุชื่อ endpoint และ deployment ผ่านอาร์กิวเมนต์ endpoint_name และ deployment_name ในกรณีนี้ ชื่อ endpoint เก็บในตัวแปร online_endpoint_name และชื่อ deployment คือ "demo"

    - ระบุเส้นทางไฟล์ JSON ที่จะทำการสกอร์ผ่านอาร์กิวเมนต์ request_file ในกรณีนี้ไฟล์คือ ./ultrachat_200k_dataset/sample_score.json

    - เก็บผลลัพธ์ที่ได้จาก endpoint ในตัวแปร response

    - แสดงผลลัพธ์ดิบ (raw response)

1. สรุปคือ สคริปต์นี้กำลังเรียกใช้ online endpoint ใน Azure Machine Learning เพื่อสกอร์ไฟล์ JSON และแสดงผลลัพธ์

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. ลบ online endpoint

1. อย่าลืมลบ online endpoint มิฉะนั้นจะทำให้ระบบคิดค่าบริการสำหรับการใช้ compute ที่ endpoint ใช้อยู่ สายโค้ด Python นี้กำลังลบ online endpoint ใน Azure Machine Learning รายละเอียดของสิ่งที่ทำมีดังนี้:

    - เรียกใช้เมธอด begin_delete ของ online_endpoints ใน workspace_ml_client เพื่อเริ่มการลบ online endpoint

    - ระบุชื่อ endpoint ที่จะลบผ่านอาร์กิวเมนต์ name ในกรณีนี้ชื่อ endpoint เก็บในตัวแปร online_endpoint_name

    - เรียกใช้เมธอด wait เพื่อรอให้การลบเสร็จสมบูรณ์ นี่เป็นการทำงานแบบบล็อก ซึ่งจะหยุดสคริปต์ไม่ให้ทำงานต่อจนกว่าการลบจะเสร็จ

    - สรุปคือ สายโค้ดนี้เริ่มการลบ online endpoint ใน Azure Machine Learning และรอจนกว่าการลบจะเสร็จสมบูรณ์

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ควรใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้