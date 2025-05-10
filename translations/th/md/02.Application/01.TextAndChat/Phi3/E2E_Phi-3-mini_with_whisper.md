<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:31:24+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "th"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## ภาพรวม

Interactive Phi 3 Mini 4K Instruct Chatbot เป็นเครื่องมือที่ช่วยให้ผู้ใช้โต้ตอบกับ Microsoft Phi 3 Mini 4K instruct demo ผ่านการป้อนข้อความหรือเสียงได้ แชทบอทนี้สามารถใช้ทำงานหลากหลาย เช่น การแปลภาษา อัปเดตสภาพอากาศ และรวบรวมข้อมูลทั่วไป

### เริ่มต้นใช้งาน

ในการใช้แชทบอทนี้ ให้ทำตามขั้นตอนดังนี้:

1. เปิด [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. ในหน้าต่างหลักของโน้ตบุ๊ก คุณจะเห็นอินเทอร์เฟซกล่องแชทพร้อมช่องป้อนข้อความและปุ่ม "Send"
3. หากต้องการใช้แชทบอทแบบข้อความ ให้พิมพ์ข้อความลงในช่องป้อนข้อความแล้วกดปุ่ม "Send" แชทบอทจะตอบกลับด้วยไฟล์เสียงที่สามารถเล่นได้ภายในโน้ตบุ๊กเลย

**Note**: เครื่องมือนี้ต้องการ GPU และการเข้าถึงโมเดล Microsoft Phi-3 และ OpenAI Whisper ซึ่งใช้สำหรับการรู้จำเสียงและการแปลภาษา

### ความต้องการ GPU

ในการรันเดโมนี้ต้องการหน่วยความจำ GPU อย่างน้อย 12GB

ความต้องการหน่วยความจำสำหรับการรัน **Microsoft-Phi-3-Mini-4K instruct** บน GPU จะขึ้นอยู่กับหลายปัจจัย เช่น ขนาดข้อมูลป้อนเข้า (เสียงหรือข้อความ) ภาษาที่ใช้แปล ความเร็วของโมเดล และหน่วยความจำที่มีบน GPU

โดยทั่วไป โมเดล Whisper ถูกออกแบบให้ทำงานบน GPU ปริมาณหน่วยความจำ GPU ขั้นต่ำที่แนะนำสำหรับการรันโมเดล Whisper คือ 8GB แต่สามารถรองรับหน่วยความจำที่มากกว่านี้ได้หากจำเป็น

ควรทราบว่าการรันข้อมูลจำนวนมากหรือคำขอจำนวนมากบนโมเดล อาจต้องการหน่วยความจำ GPU มากขึ้นและ/หรืออาจส่งผลต่อประสิทธิภาพ ควรทดสอบกรณีการใช้งานของคุณกับการตั้งค่าต่างๆ และติดตามการใช้หน่วยความจำเพื่อหาการตั้งค่าที่เหมาะสมกับความต้องการเฉพาะของคุณ

## ตัวอย่าง E2E สำหรับ Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

โน้ตบุ๊กชื่อ [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) แสดงวิธีใช้ Microsoft Phi 3 Mini 4K instruct Demo เพื่อสร้างข้อความจากเสียงหรือข้อความที่ป้อนเข้า โน้ตบุ๊กนี้กำหนดฟังก์ชันหลายอย่าง:

1. `tts_file_name(text)`: ฟังก์ชันนี้สร้างชื่อไฟล์ตามข้อความที่ป้อนเข้าเพื่อบันทึกไฟล์เสียงที่สร้างขึ้น
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: ฟังก์ชันนี้ใช้ Edge TTS API เพื่อสร้างไฟล์เสียงจากรายการของชิ้นข้อความที่ป้อนเข้า พารามิเตอร์ป้อนเข้าคือรายการชิ้นข้อความ อัตราความเร็วเสียง ชื่อเสียง และเส้นทางบันทึกไฟล์เสียงที่สร้างขึ้น
1. `talk(input_text)`: ฟังก์ชันนี้สร้างไฟล์เสียงโดยใช้ Edge TTS API และบันทึกไฟล์เสียงเป็นชื่อไฟล์สุ่มในไดเรกทอรี /content/audio พารามิเตอร์ป้อนเข้าคือข้อความที่ต้องการแปลงเป็นเสียง
1. `run_text_prompt(message, chat_history)`: ฟังก์ชันนี้ใช้ Microsoft Phi 3 Mini 4K instruct demo เพื่อสร้างไฟล์เสียงจากข้อความที่ป้อนเข้าและเพิ่มลงในประวัติแชท
1. `run_audio_prompt(audio, chat_history)`: ฟังก์ชันนี้แปลงไฟล์เสียงเป็นข้อความโดยใช้ Whisper model API และส่งต่อไปยังฟังก์ชัน `run_text_prompt()`
1. โค้ดเปิดใช้งานแอป Gradio ที่ช่วยให้ผู้ใช้โต้ตอบกับ Phi 3 Mini 4K instruct demo โดยการพิมพ์ข้อความหรืออัปโหลดไฟล์เสียง ผลลัพธ์จะแสดงเป็นข้อความภายในแอป

## การแก้ไขปัญหา

ติดตั้งไดรเวอร์ Cuda GPU

1. ตรวจสอบให้แน่ใจว่าแอปพลิเคชัน Linux ของคุณเป็นเวอร์ชันล่าสุด

    ```bash
    sudo apt update
    ```

1. ติดตั้งไดรเวอร์ Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. ลงทะเบียนตำแหน่งไดรเวอร์ cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. ตรวจสอบขนาดหน่วยความจำ Nvidia GPU (ต้องการ 12GB ของหน่วยความจำ GPU)

    ```bash
    nvidia-smi
    ```

1. ล้างแคช: หากคุณใช้ PyTorch สามารถเรียกใช้ torch.cuda.empty_cache() เพื่อปล่อยหน่วยความจำแคชที่ไม่ได้ใช้งานทั้งหมดให้กับแอปพลิเคชัน GPU อื่น ๆ

    ```python
    torch.cuda.empty_cache() 
    ```

1. ตรวจสอบ Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. ทำตามขั้นตอนต่อไปนี้เพื่อสร้าง Hugging Face token

    - ไปที่ [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)
    - เลือก **New token**
    - กรอกชื่อโปรเจกต์ที่ต้องการใช้ในช่อง **Name**
    - เลือก **Type** เป็น **Write**

> **Note**
>
> หากพบข้อผิดพลาดดังต่อไปนี้:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> เพื่อแก้ไข ให้พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลของคุณ
>
> ```bash
> sudo ldconfig
> ```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใดๆ ที่เกิดจากการใช้การแปลนี้