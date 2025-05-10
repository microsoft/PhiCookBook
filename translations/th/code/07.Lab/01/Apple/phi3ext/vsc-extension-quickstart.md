<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:08:02+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "th"
}
-->
# ยินดีต้อนรับสู่ส่วนขยาย VS Code ของคุณ

## มีอะไรในโฟลเดอร์นี้

* โฟลเดอร์นี้ประกอบด้วยไฟล์ทั้งหมดที่จำเป็นสำหรับส่วนขยายของคุณ
* `package.json` - นี่คือไฟล์ manifest ที่คุณประกาศส่วนขยายและคำสั่งของคุณ
  * ปลั๊กอินตัวอย่างจะลงทะเบียนคำสั่งและกำหนดชื่อเรื่องกับชื่อคำสั่ง ข้อมูลนี้ช่วยให้ VS Code แสดงคำสั่งใน command palette โดยยังไม่ต้องโหลดปลั๊กอิน
* `src/extension.ts` - นี่คือไฟล์หลักที่คุณจะเขียนการทำงานของคำสั่งของคุณ
  * ไฟล์นี้ส่งออกฟังก์ชันเดียว `activate` ซึ่งจะถูกเรียกครั้งแรกเมื่อส่วนขยายของคุณถูกเปิดใช้งาน (ในกรณีนี้โดยการรันคำสั่ง) ภายในฟังก์ชัน `activate` เราจะเรียก `registerCommand`
  * เราส่งฟังก์ชันที่มีการทำงานของคำสั่งเป็นพารามิเตอร์ตัวที่สองให้กับ `registerCommand`

## การตั้งค่า

* ติดตั้งส่วนขยายที่แนะนำ (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner และ dbaeumer.vscode-eslint)


## เริ่มต้นใช้งานได้ทันที

* กด `F5` เพื่อเปิดหน้าต่างใหม่ที่โหลดส่วนขยายของคุณแล้ว
* รันคำสั่งของคุณจาก command palette โดยกด (`Ctrl+Shift+P` หรือ `Cmd+Shift+P` บน Mac) แล้วพิมพ์ `Hello World`
* ตั้งจุดหยุด (breakpoints) ในโค้ดของคุณใน `src/extension.ts` เพื่อดีบักส่วนขยาย
* ดูผลลัพธ์จากส่วนขยายของคุณได้ที่ debug console

## การแก้ไข

* คุณสามารถเปิดใช้งานส่วนขยายอีกครั้งจากแถบเครื่องมือดีบักหลังจากแก้ไขโค้ดใน `src/extension.ts`
* คุณยังสามารถโหลดใหม่ (`Ctrl+R` หรือ `Cmd+R` บน Mac) หน้าต่าง VS Code ที่มีส่วนขยายของคุณเพื่อโหลดการเปลี่ยนแปลง

## สำรวจ API

* คุณสามารถเปิดชุด API ทั้งหมดของเราได้เมื่อเปิดไฟล์ `node_modules/@types/vscode/index.d.ts`

## การรันทดสอบ

* ติดตั้ง [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* รันงาน "watch" ผ่านคำสั่ง **Tasks: Run Task** ให้แน่ใจว่างานนี้กำลังทำงานอยู่ มิฉะนั้นอาจไม่พบการทดสอบ
* เปิดมุมมอง Testing จาก activity bar แล้วคลิกปุ่ม "Run Test" หรือใช้คีย์ลัด `Ctrl/Cmd + ; A`
* ดูผลลัพธ์ของการทดสอบในมุมมอง Test Results
* แก้ไข `src/test/extension.test.ts` หรือสร้างไฟล์ทดสอบใหม่ในโฟลเดอร์ `test`
  * ตัวทดสอบที่ให้มาจะพิจารณาเฉพาะไฟล์ที่ตรงกับรูปแบบชื่อ `**.test.ts` เท่านั้น
  * คุณสามารถสร้างโฟลเดอร์ภายใน `test` เพื่อจัดโครงสร้างการทดสอบตามที่ต้องการ

## ก้าวไปไกลกว่าเดิม

* ลดขนาดส่วนขยายและปรับปรุงเวลาเริ่มต้นด้วยการ [รวมส่วนขยายของคุณ](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)
* [เผยแพร่ส่วนขยายของคุณ](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) บนตลาดส่วนขยาย VS Code
* อัตโนมัติการสร้างโดยตั้งค่า [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้