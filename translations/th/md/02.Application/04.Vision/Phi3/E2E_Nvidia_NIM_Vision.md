<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-17T04:56:11+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "th"
}
-->
### ตัวอย่างสถานการณ์

ลองนึกภาพว่าคุณมีภาพ (`demo.png`) และต้องการสร้างโค้ด Python ที่ประมวลผลภาพนี้และบันทึกเป็นเวอร์ชันใหม่ (`phi-3-vision.jpg`)

โค้ดข้างต้นจะช่วยทำงานนี้โดยอัตโนมัติด้วยการ:

1. ตั้งค่าสภาพแวดล้อมและการกำหนดค่าที่จำเป็น
2. สร้าง prompt ที่สั่งให้โมเดลสร้างโค้ด Python ที่ต้องการ
3. ส่ง prompt ไปยังโมเดลและเก็บโค้ดที่ได้มา
4. ดึงโค้ดที่สร้างขึ้นมาและรันโค้ดนั้น
5. แสดงภาพต้นฉบับและภาพที่ผ่านการประมวลผลแล้ว

วิธีนี้ใช้ประโยชน์จากพลังของ AI ในการทำงานประมวลผลภาพให้อัตโนมัติ ทำให้การทำงานง่ายและรวดเร็วขึ้น

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

มาดูทีละขั้นตอนว่าโค้ดทั้งหมดทำอะไรบ้าง:

1. **ติดตั้งแพ็กเกจที่จำเป็น**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    คำสั่งนี้ติดตั้งแพ็กเกจ `langchain_nvidia_ai_endpoints` ให้เป็นเวอร์ชันล่าสุด

2. **นำเข้าโมดูลที่จำเป็น**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    การนำเข้าเหล่านี้จะเรียกใช้โมดูลที่จำเป็นสำหรับการติดต่อกับ NVIDIA AI endpoints, การจัดการรหัสผ่านอย่างปลอดภัย, การทำงานกับระบบปฏิบัติการ และการเข้ารหัส/ถอดรหัสข้อมูลในรูปแบบ base64

3. **ตั้งค่า API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    โค้ดนี้จะตรวจสอบว่า environment variable `NVIDIA_API_KEY` ถูกตั้งค่าหรือไม่ หากไม่ ระบบจะขอให้ผู้ใช้กรอก API key อย่างปลอดภัย

4. **กำหนดโมเดลและเส้นทางภาพ**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    กำหนดโมเดลที่จะใช้ สร้างอินสแตนซ์ของ `ChatNVIDIA` ด้วยโมเดลที่ระบุ และกำหนดเส้นทางไปยังไฟล์ภาพ

5. **สร้างข้อความ prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    กำหนดข้อความ prompt ที่สั่งให้โมเดลสร้างโค้ด Python สำหรับประมวลผลภาพ

6. **เข้ารหัสภาพเป็น Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    โค้ดนี้อ่านไฟล์ภาพ เข้ารหัสเป็น base64 และสร้างแท็กภาพ HTML ที่ฝังข้อมูลภาพไว้

7. **รวมข้อความและภาพเป็น prompt เดียวกัน**:
    ```python
    prompt = f"{text} {image}"
    ```
    รวมข้อความ prompt และแท็กภาพ HTML เข้าด้วยกันเป็นสตริงเดียว

8. **สร้างโค้ดโดยใช้ ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    ส่ง prompt ไปยังโมเดล `ChatNVIDIA` และเก็บโค้ดที่ได้มาเป็นชิ้น ๆ พร้อมพิมพ์และต่อข้อความแต่ละชิ้นเข้ากับตัวแปร `code`

9. **ดึงโค้ด Python จากเนื้อหาที่สร้างขึ้น**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    ดึงโค้ด Python ที่แท้จริงออกมาจากเนื้อหาที่สร้างขึ้นโดยตัดส่วน markdown ออก

10. **รันโค้ดที่สร้างขึ้น**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    รันโค้ด Python ที่ดึงออกมาเป็น subprocess และเก็บผลลัพธ์

11. **แสดงภาพ**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    โค้ดเหล่านี้ใช้โมดูล `IPython.display` ในการแสดงภาพต่าง ๆ

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้