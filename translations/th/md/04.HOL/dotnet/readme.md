<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:43:58+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "th"
}
-->
﻿## ยินดีต้อนรับสู่ Phi labs ที่ใช้ C#

มีตัวอย่าง labs หลายแบบที่แสดงให้เห็นวิธีการผสานรวม Phi models เวอร์ชันต่าง ๆ ที่ทรงพลังในสภาพแวดล้อม .NET

## สิ่งที่ต้องมี

ก่อนรันตัวอย่าง ให้แน่ใจว่าคุณได้ติดตั้งสิ่งเหล่านี้แล้ว:

**.NET 9:** ตรวจสอบว่าคุณมี [เวอร์ชันล่าสุดของ .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ติดตั้งอยู่ในเครื่องของคุณ

**(ไม่บังคับ) Visual Studio หรือ Visual Studio Code:** คุณจะต้องมี IDE หรือโปรแกรมแก้ไขโค้ดที่รองรับการรันโปรเจกต์ .NET [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) หรือ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) เป็นตัวเลือกที่แนะนำ

**ใช้ git** ทำการโคลนเวอร์ชัน Phi-3, Phi3.5 หรือ Phi-4 ที่มีให้จาก [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) ลงในเครื่องของคุณ

**ดาวน์โหลดโมเดล Phi-4 ONNX** ลงในเครื่องของคุณ:

### ไปยังโฟลเดอร์ที่จะเก็บโมเดล

```bash
cd c:\phi\models
```

### เพิ่มการรองรับ lfs

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

**สำคัญ:** ตัวอย่างเดโมปัจจุบันถูกออกแบบมาให้ใช้เวอร์ชัน ONNX ของโมเดล ขั้นตอนก่อนหน้าจะโคลนโมเดลดังต่อไปนี้

## เกี่ยวกับ Labs

โซลูชันหลักมีตัวอย่าง Labs หลายตัวที่แสดงความสามารถของ Phi models โดยใช้ C#

| โปรเจกต์ | โมเดล | คำอธิบาย |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 หรือ Phi-3.5 | ตัวอย่างคอนโซลแชทที่ให้ผู้ใช้ถามคำถามได้ โปรเจกต์จะโหลดโมเดล ONNX Phi-3 ในเครื่องโดยใช้ `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that allows the user to ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. รันโปรเจกต์ด้วยคำสั่ง

    ```bash
    dotnet run
    ```

1. โปรเจกต์ตัวอย่างจะขอรับข้อมูลจากผู้ใช้และตอบกลับโดยใช้โมเดลในเครื่อง

   ตัวอย่างเดโมที่รันจะคล้ายกับนี้:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญแนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้