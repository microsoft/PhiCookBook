<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:18:59+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "th"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## ภาพรวม

Interactive Phi 3 Mini 4K Instruct Chatbot เป็นเครื่องมือที่ช่วยให้ผู้ใช้สามารถโต้ตอบกับ Microsoft Phi 3 Mini 4K instruct demo ผ่านการป้อนข้อมูลด้วยข้อความหรือเสียง แชทบอทนี้สามารถใช้ทำงานหลากหลาย เช่น การแปลภาษา อัปเดตสภาพอากาศ และการรวบรวมข้อมูลทั่วไป

### เริ่มต้นใช้งาน

เพื่อใช้แชทบอทนี้ ให้ทำตามขั้นตอนดังนี้:

1. เปิด [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. ในหน้าต่างหลักของโน้ตบุ๊ก คุณจะเห็นอินเทอร์เฟซกล่องแชทที่มีช่องป้อนข้อความและปุ่ม "Send"
3. หากต้องการใช้แชทบอทแบบข้อความ ให้พิมพ์ข้อความของคุณลงในช่องป้อนข้อความแล้วคลิกปุ่ม "Send" แชทบอทจะตอบกลับด้วยไฟล์เสียงที่สามารถเล่นได้โดยตรงภายในโน้ตบุ๊ก

**Note**: เครื่องมือนี้ต้องการ GPU และการเข้าถึงโมเดล Microsoft Phi-3 และ OpenAI Whisper ซึ่งใช้สำหรับการรู้จำเสียงและการแปลภาษา

### ความต้องการ GPU

ในการรันเดโมนี้ คุณต้องมีหน่วยความจำ GPU อย่างน้อย 12GB

ความต้องการหน่วยความจำสำหรับการรัน **Microsoft-Phi-3-Mini-4K instruct** บน GPU จะขึ้นอยู่กับหลายปัจจัย เช่น ขนาดของข้อมูลนำเข้า (เสียงหรือข้อความ) ภาษาในการแปล ความเร็วของโมเดล และหน่วยความจำที่มีอยู่บน GPU

โดยทั่วไป โมเดล Whisper ถูกออกแบบมาให้รันบน GPU โดยแนะนำให้มีหน่วยความจำ GPU อย่างน้อย 8GB แต่สามารถรองรับหน่วยความจำที่มากกว่านี้ได้หากจำเป็น

ควรทราบว่าการรันข้อมูลจำนวนมากหรือคำขอจำนวนมากบนโมเดล อาจต้องการหน่วยความจำ GPU มากขึ้นและ/หรืออาจทำให้ประสิทธิภาพลดลง แนะนำให้ทดสอบกรณีการใช้งานของคุณด้วยการตั้งค่าต่าง ๆ และตรวจสอบการใช้หน่วยความจำเพื่อหาการตั้งค่าที่เหมาะสมกับความต้องการเฉพาะของคุณ

## ตัวอย่าง E2E สำหรับ Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

โน้ตบุ๊กชื่อ [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) แสดงวิธีการใช้ Microsoft Phi 3 Mini 4K instruct Demo เพื่อสร้างข้อความจากเสียงหรือข้อความที่ป้อนเข้า โน้ตบุ๊กนี้กำหนดฟังก์ชันหลายตัวดังนี้:

1. `tts_file_name(text)`: ฟังก์ชันนี้สร้างชื่อไฟล์จากข้อความนำเข้าเพื่อใช้บันทึกไฟล์เสียงที่สร้างขึ้น
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: ฟังก์ชันนี้ใช้ Edge TTS API เพื่อสร้างไฟล์เสียงจากรายการข้อความย่อยที่ป้อนเข้า โดยรับพารามิเตอร์เป็นรายการข้อความย่อย อัตราความเร็วเสียง ชื่อเสียง และเส้นทางสำหรับบันทึกไฟล์เสียงที่สร้างขึ้น
1. `talk(input_text)`: ฟังก์ชันนี้สร้างไฟล์เสียงโดยใช้ Edge TTS API และบันทึกไฟล์ด้วยชื่อไฟล์สุ่มในไดเรกทอรี /content/audio โดยรับพารามิเตอร์เป็นข้อความนำเข้าที่จะแปลงเป็นเสียง
1. `run_text_prompt(message, chat_history)`: ฟังก์ชันนี้ใช้ Microsoft Phi 3 Mini 4K instruct demo เพื่อสร้างไฟล์เสียงจากข้อความที่ป้อนเข้าและเพิ่มลงในประวัติการแชท
1. `run_audio_prompt(audio, chat_history)`: ฟังก์ชันนี้แปลงไฟล์เสียงเป็นข้อความโดยใช้ Whisper model API และส่งต่อไปยังฟังก์ชัน `run_text_prompt()`
1. โค้ดจะเปิดแอป Gradio ที่ช่วยให้ผู้ใช้โต้ตอบกับ Phi 3 Mini 4K instruct demo ได้โดยการพิมพ์ข้อความหรืออัปโหลดไฟล์เสียง ผลลัพธ์จะแสดงเป็นข้อความภายในแอป

## การแก้ไขปัญหา

การติดตั้งไดรเวอร์ Cuda GPU

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

1. ตรวจสอบขนาดหน่วยความจำ Nvidia GPU (ต้องการหน่วยความจำ GPU 12GB)

    ```bash
    nvidia-smi
    ```

1. ล้างแคช: หากคุณใช้ PyTorch คุณสามารถเรียกใช้ torch.cuda.empty_cache() เพื่อปล่อยหน่วยความจำแคชที่ไม่ได้ใช้งานทั้งหมด เพื่อให้แอปพลิเคชัน GPU อื่น ๆ สามารถใช้งานได้

    ```python
    torch.cuda.empty_cache() 
    ```

1. ตรวจสอบ Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. ดำเนินการตามขั้นตอนต่อไปนี้เพื่อสร้าง Hugging Face token

    - ไปที่ [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)
    - เลือก **New token**
    - กรอกชื่อโปรเจกต์ที่ต้องการใช้
    - เลือก **Type** เป็น **Write**

> **Note**
>
> หากคุณพบข้อผิดพลาดดังต่อไปนี้:
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
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้