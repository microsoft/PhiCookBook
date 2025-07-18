<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:37:17+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "th"
}
-->
## ยินดีต้อนรับสู่ Phi labs ที่ใช้ C#

มีชุดแลปที่แสดงวิธีการผสานรวม Phi models เวอร์ชันต่างๆ ที่ทรงพลังในสภาพแวดล้อม .NET

## ข้อกำหนดเบื้องต้น

ก่อนรันตัวอย่าง ให้แน่ใจว่าคุณได้ติดตั้งสิ่งต่อไปนี้แล้ว:

**.NET 9:** ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง [เวอร์ชันล่าสุดของ .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) บนเครื่องของคุณ

**(ไม่บังคับ) Visual Studio หรือ Visual Studio Code:** คุณจะต้องมี IDE หรือโปรแกรมแก้ไขโค้ดที่สามารถรันโปรเจกต์ .NET ได้ แนะนำให้ใช้ [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) หรือ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)

**ใช้ git** เพื่อโคลน Phi-3, Phi3.5 หรือ Phi-4 เวอร์ชันที่มีอยู่จาก [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) มายังเครื่องของคุณ

**ดาวน์โหลดโมเดล Phi-4 ONNX** ลงในเครื่องของคุณ:

### ไปยังโฟลเดอร์สำหรับเก็บโมเดล

```bash
cd c:\phi\models
```

### เพิ่มการสนับสนุนสำหรับ lfs

```bash
git lfs install 
```

### โคลนและดาวน์โหลดโมเดล Phi-4 mini instruct และโมเดล Phi-4 multi modal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**ดาวน์โหลดโมเดล Phi-3 ONNX** ลงในเครื่องของคุณ:

### โคลนและดาวน์โหลดโมเดล Phi-3 mini 4K instruct และโมเดล Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**สำคัญ:** ตัวอย่างในปัจจุบันออกแบบมาให้ใช้เวอร์ชัน ONNX ของโมเดล ขั้นตอนก่อนหน้านี้จะโคลนโมเดลดังกล่าว

## เกี่ยวกับแลป

โซลูชันหลักมีตัวอย่างแลปหลายตัวที่แสดงความสามารถของ Phi models โดยใช้ C#

| โปรเจกต์ | โมเดล | คำอธิบาย |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 หรือ Phi-3.5 | ตัวอย่างแชทคอนโซลที่ให้ผู้ใช้ถามคำถาม โปรเจกต์โหลดโมเดล ONNX Phi-3 ในเครื่องโดยใช้ไลบรารี `Microsoft.ML.OnnxRuntime` |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 หรือ Phi-3.5 | ตัวอย่างแชทคอนโซลที่ให้ผู้ใช้ถามคำถาม โปรเจกต์โหลดโมเดล ONNX Phi-3 ในเครื่องโดยใช้ไลบรารี `Microsoft.Semantic.Kernel` |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 หรือ Phi-3.5 | ตัวอย่างโปรเจกต์ที่ใช้โมเดล phi3 vision ในเครื่องเพื่อวิเคราะห์ภาพ โปรเจกต์โหลดโมเดล ONNX Phi-3 Vision ในเครื่องโดยใช้ไลบรารี `Microsoft.ML.OnnxRuntime` |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 หรือ Phi-3.5 | ตัวอย่างโปรเจกต์ที่ใช้โมเดล phi3 vision ในเครื่องเพื่อวิเคราะห์ภาพ โปรเจกต์โหลดโมเดล ONNX Phi-3 Vision ในเครื่องโดยใช้ไลบรารี `Microsoft.ML.OnnxRuntime` พร้อมเมนูตัวเลือกต่างๆ เพื่อโต้ตอบกับผู้ใช้ |
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | ตัวอย่างแชทคอนโซลที่ให้ผู้ใช้ถามคำถาม โปรเจกต์โหลดโมเดล ONNX Phi-4 ในเครื่องโดยใช้ไลบรารี `Microsoft.ML.OnnxRuntime` |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | ตัวอย่างแชทคอนโซลที่ให้ผู้ใช้ถามคำถาม โปรเจกต์โหลดโมเดล ONNX Phi-4 ในเครื่องโดยใช้ไลบรารี `Semantic Kernel` |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | ตัวอย่างแชทคอนโซลที่ให้ผู้ใช้ถามคำถาม โปรเจกต์โหลดโมเดล ONNX Phi-4 ในเครื่องโดยใช้ไลบรารี `Microsoft.ML.OnnxRuntimeGenAI` และใช้งาน `IChatClient` จาก `Microsoft.Extensions.AI` |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | ตัวอย่างแชทคอนโซลที่ให้ผู้ใช้ถามคำถาม โดยแชทนี้มีระบบหน่วยความจำ |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | ตัวอย่างโปรเจกต์ที่ใช้โมเดล Phi-4 ในเครื่องเพื่อวิเคราะห์ภาพและแสดงผลลัพธ์ในคอนโซล โปรเจกต์โหลดโมเดล Phi-4-`multimodal-instruct-onnx` ในเครื่องโดยใช้ไลบรารี `Microsoft.ML.OnnxRuntime` |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | ตัวอย่างโปรเจกต์ที่ใช้โมเดล Phi-4 ในเครื่องเพื่อวิเคราะห์ไฟล์เสียง สร้างข้อความถอดเสียง และแสดงผลลัพธ์ในคอนโซล โปรเจกต์โหลดโมเดล Phi-4-`multimodal-instruct-onnx` ในเครื่องโดยใช้ไลบรารี `Microsoft.ML.OnnxRuntime` |

## วิธีรันโปรเจกต์

เพื่อรันโปรเจกต์ ให้ทำตามขั้นตอนดังนี้:

1. โคลนรีโพซิทอรีมายังเครื่องของคุณ

1. เปิดเทอร์มินัลและไปยังโปรเจกต์ที่ต้องการ เช่น รัน `LabsPhi4-Chat-01OnnxRuntime`

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. รันโปรเจกต์ด้วยคำสั่ง

    ```bash
    dotnet run
    ```

1. ตัวอย่างโปรเจกต์จะขอรับข้อมูลจากผู้ใช้และตอบกลับโดยใช้โมเดลในเครื่อง

   ตัวอย่างการรันจะคล้ายกับนี้:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้