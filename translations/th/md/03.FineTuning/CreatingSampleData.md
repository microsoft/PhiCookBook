<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:49:05+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "th"
}
-->
# สร้างชุดข้อมูลภาพโดยการดาวน์โหลด DataSet จาก Hugging Face และภาพที่เกี่ยวข้อง


### ภาพรวม

สคริปต์นี้เตรียมชุดข้อมูลสำหรับการเรียนรู้ของเครื่องโดยการดาวน์โหลดภาพที่จำเป็น กรองแถวที่ดาวน์โหลดภาพไม่สำเร็จ และบันทึกชุดข้อมูลเป็นไฟล์ CSV

### สิ่งที่ต้องเตรียม

ก่อนรันสคริปต์นี้ ให้แน่ใจว่าติดตั้งไลบรารีต่อไปนี้แล้ว: `Pandas`, `Datasets`, `requests`, `PIL` และ `io` นอกจากนี้คุณต้องแทนที่ `'Insert_Your_Dataset'` ในบรรทัดที่ 2 ด้วยชื่อชุดข้อมูลของคุณจาก Hugging Face

ไลบรารีที่จำเป็น:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### ฟังก์ชันการทำงาน

สคริปต์ทำงานตามขั้นตอนดังนี้:

1. ดาวน์โหลดชุดข้อมูลจาก Hugging Face โดยใช้ฟังก์ชัน `load_dataset()`
2. แปลงชุดข้อมูลจาก Hugging Face เป็น Pandas DataFrame เพื่อให้ง่ายต่อการจัดการโดยใช้เมธอด `to_pandas()`
3. สร้างโฟลเดอร์สำหรับบันทึกชุดข้อมูลและภาพ
4. กรองแถวที่ดาวน์โหลดภาพไม่สำเร็จโดยการวนลูปผ่านแต่ละแถวใน DataFrame ดาวน์โหลดภาพโดยใช้ฟังก์ชัน `download_image()` ที่กำหนดเอง และเพิ่มแถวที่ผ่านการกรองลงใน DataFrame ใหม่ชื่อ `filtered_rows`
5. สร้าง DataFrame ใหม่จากแถวที่ผ่านการกรองและบันทึกลงดิสก์เป็นไฟล์ CSV
6. แสดงข้อความแจ้งตำแหน่งที่บันทึกชุดข้อมูลและภาพ

### ฟังก์ชันที่กำหนดเอง

ฟังก์ชัน `download_image()` ดาวน์โหลดภาพจาก URL และบันทึกลงเครื่องโดยใช้ Pillow Image Library (PIL) และโมดูล `io` ฟังก์ชันจะคืนค่า True หากดาวน์โหลดภาพสำเร็จ และคืนค่า False หากไม่สำเร็จ ฟังก์ชันยังจะโยนข้อผิดพลาดพร้อมข้อความเมื่อการร้องขอล้มเหลว

### วิธีการทำงาน

ฟังก์ชัน download_image รับพารามิเตอร์สองตัวคือ image_url ซึ่งเป็น URL ของภาพที่ต้องการดาวน์โหลด และ save_path ซึ่งเป็นเส้นทางที่ใช้บันทึกภาพที่ดาวน์โหลด

วิธีการทำงานของฟังก์ชันมีดังนี้:

เริ่มต้นด้วยการส่งคำขอ GET ไปยัง image_url โดยใช้เมธอด requests.get เพื่อดึงข้อมูลภาพจาก URL

บรรทัด response.raise_for_status() ตรวจสอบว่าคำขอสำเร็จหรือไม่ หากสถานะของการตอบกลับแสดงข้อผิดพลาด (เช่น 404 - ไม่พบหน้า) จะโยนข้อผิดพลาดขึ้นมา เพื่อให้แน่ใจว่าเราจะดาวน์โหลดภาพต่อก็ต่อเมื่อคำขอสำเร็จเท่านั้น

ข้อมูลภาพจะถูกส่งต่อไปยังเมธอด Image.open จากโมดูล PIL (Python Imaging Library) เมธอดนี้จะสร้างอ็อบเจ็กต์ Image จากข้อมูลภาพ

บรรทัด image.save(save_path) จะบันทึกภาพไปยัง save_path ที่ระบุ ซึ่งควรรวมชื่อไฟล์และนามสกุลที่ต้องการด้วย

สุดท้าย ฟังก์ชันจะคืนค่า True เพื่อบอกว่าการดาวน์โหลดและบันทึกภาพสำเร็จ หากเกิดข้อผิดพลาดใด ๆ ในระหว่างกระบวนการ ฟังก์ชันจะจับข้อผิดพลาดนั้น แสดงข้อความแจ้งข้อผิดพลาด และคืนค่า False

ฟังก์ชันนี้มีประโยชน์สำหรับดาวน์โหลดภาพจาก URL และบันทึกลงเครื่อง โดยจัดการกับข้อผิดพลาดที่อาจเกิดขึ้นระหว่างการดาวน์โหลดและแจ้งผลลัพธ์ว่าประสบความสำเร็จหรือไม่

ควรทราบว่าไลบรารี requests ใช้สำหรับส่งคำขอ HTTP, ไลบรารี PIL ใช้สำหรับจัดการภาพ และคลาส BytesIO ใช้จัดการข้อมูลภาพในรูปแบบสตรีมของไบต์



### สรุป

สคริปต์นี้ช่วยให้การเตรียมชุดข้อมูลสำหรับการเรียนรู้ของเครื่องเป็นเรื่องง่ายขึ้นโดยการดาวน์โหลดภาพที่จำเป็น กรองแถวที่ดาวน์โหลดภาพไม่สำเร็จ และบันทึกชุดข้อมูลเป็นไฟล์ CSV

### ตัวอย่างสคริปต์

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download the dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert the Hugging Face dataset to a Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save the dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows where image download fails
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Create a new DataFrame with the filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save the updated dataset to disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### ตัวอย่างโค้ดดาวน์โหลด  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### ตัวอย่างชุดข้อมูล  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้