<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:56:20+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "th"
}
-->
# ยินดีต้อนรับสู่ส่วนขยาย VS Code ของคุณ

## มีอะไรในโฟลเดอร์นี้

* โฟลเดอร์นี้ประกอบด้วยไฟล์ทั้งหมดที่จำเป็นสำหรับส่วนขยายของคุณ
* `package.json` - นี่คือไฟล์ manifest ที่คุณประกาศส่วนขยายและคำสั่งของคุณ
  * ปลั๊กอินตัวอย่างจะลงทะเบียนคำสั่งและกำหนดชื่อเรื่องกับชื่อคำสั่ง ด้วยข้อมูลนี้ VS Code สามารถแสดงคำสั่งใน command palette ได้ โดยยังไม่จำเป็นต้องโหลดปลั๊กอิน
* `src/extension.ts` - นี่คือไฟล์หลักที่คุณจะเขียนการทำงานของคำสั่งของคุณ
  * ไฟล์นี้ส่งออกฟังก์ชันหนึ่งชื่อ `activate` ซึ่งจะถูกเรียกครั้งแรกเมื่อส่วนขยายของคุณถูกเปิดใช้งาน (ในกรณีนี้โดยการรันคำสั่ง) ภายในฟังก์ชัน `activate` เราจะเรียก `registerCommand`
  * เราส่งผ่านฟังก์ชันที่มีการทำงานของคำสั่งเป็นพารามิเตอร์ตัวที่สองให้กับ `registerCommand`

## การตั้งค่า

* ติดตั้งส่วนขยายที่แนะนำ (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, และ dbaeumer.vscode-eslint)


## เริ่มใช้งานได้ทันที

* กด `F5` เพื่อเปิดหน้าต่างใหม่ที่โหลดส่วนขยายของคุณแล้ว
* รันคำสั่งของคุณจาก command palette โดยกด (`Ctrl+Shift+P` หรือ `Cmd+Shift+P` บน Mac) แล้วพิมพ์ `Hello World`
* ตั้ง breakpoints ในโค้ดของคุณภายใน `src/extension.ts` เพื่อดีบักส่วนขยาย
* ดูผลลัพธ์จากส่วนขยายของคุณใน debug console

## แก้ไขเปลี่ยนแปลง

* คุณสามารถเปิดใช้งานส่วนขยายใหม่จากแถบเครื่องมือดีบักหลังจากแก้ไขโค้ดใน `src/extension.ts`
* คุณยังสามารถรีโหลด (`Ctrl+R` หรือ `Cmd+R` บน Mac) หน้าต่าง VS Code ที่มีส่วนขยายของคุณเพื่อโหลดการเปลี่ยนแปลงได้

## สำรวจ API

* คุณสามารถเปิดชุด API ทั้งหมดได้เมื่อเปิดไฟล์ `node_modules/@types/vscode/index.d.ts`

## รันการทดสอบ

* ติดตั้ง [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* รันงาน "watch" ผ่านคำสั่ง **Tasks: Run Task** ให้แน่ใจว่างานนี้กำลังทำงานอยู่ มิฉะนั้นการทดสอบอาจไม่ถูกค้นพบ
* เปิดมุมมอง Testing จากแถบกิจกรรมและคลิกปุ่ม Run Test หรือใช้ปุ่มลัด `Ctrl/Cmd + ; A`
* ดูผลลัพธ์ของการทดสอบในมุมมอง Test Results
* แก้ไข `src/test/extension.test.ts` หรือสร้างไฟล์ทดสอบใหม่ภายในโฟลเดอร์ `test`
  * ตัวรันการทดสอบที่ให้มาจะพิจารณาเฉพาะไฟล์ที่ตรงกับรูปแบบชื่อ `**.test.ts` เท่านั้น
  * คุณสามารถสร้างโฟลเดอร์ภายใน `test` เพื่อจัดโครงสร้างการทดสอบตามต้องการ

## ก้าวไปอีกขั้น

* ลดขนาดส่วนขยายและปรับปรุงเวลาเริ่มต้นด้วยการ [รวมส่วนขยายของคุณ](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)
* [เผยแพร่ส่วนขยายของคุณ](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) บนตลาดส่วนขยาย VS Code
* ทำให้งานสร้างอัตโนมัติโดยตั้งค่า [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใดๆ ที่เกิดจากการใช้การแปลนี้