<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:36:39+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "th"
}
-->
# ยินดีต้อนรับสู่ VS Code Extension ของคุณ

## มีอะไรอยู่ในโฟลเดอร์นี้

* โฟลเดอร์นี้ประกอบด้วยไฟล์ทั้งหมดที่จำเป็นสำหรับส่วนขยายของคุณ
* `package.json` - นี่คือไฟล์ manifest ที่คุณประกาศส่วนขยายและคำสั่งของคุณ
  * ปลั๊กอินตัวอย่างจะลงทะเบียนคำสั่งและกำหนดชื่อเรื่องกับชื่อคำสั่ง ด้วยข้อมูลนี้ VS Code จะสามารถแสดงคำสั่งใน command palette ได้ โดยยังไม่ต้องโหลดปลั๊กอิน
* `src/extension.ts` - นี่คือไฟล์หลักที่คุณจะเขียนการทำงานของคำสั่งของคุณ
  * ไฟล์นี้จะส่งออกฟังก์ชันหนึ่งชื่อ `activate` ซึ่งจะถูกเรียกครั้งแรกเมื่อส่วนขยายของคุณถูกเปิดใช้งาน (ในกรณีนี้โดยการเรียกใช้คำสั่ง) ภายในฟังก์ชัน `activate` เราจะเรียก `registerCommand`
  * เราส่งฟังก์ชันที่มีการทำงานของคำสั่งเป็นพารามิเตอร์ที่สองให้กับ `registerCommand`

## การตั้งค่า

* ติดตั้งส่วนขยายที่แนะนำ (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner และ dbaeumer.vscode-eslint)

## เริ่มใช้งานได้ทันที

* กด `F5` เพื่อเปิดหน้าต่างใหม่ที่โหลดส่วนขยายของคุณ
* รันคำสั่งของคุณจาก command palette โดยกด (`Ctrl+Shift+P` หรือ `Cmd+Shift+P` บน Mac) แล้วพิมพ์ `Hello World`
* ตั้ง breakpoints ในโค้ดของคุณภายใน `src/extension.ts` เพื่อดีบักส่วนขยาย
* ดูผลลัพธ์จากส่วนขยายของคุณใน debug console

## ทำการเปลี่ยนแปลง

* คุณสามารถเริ่มส่วนขยายใหม่จากแถบเครื่องมือดีบักหลังจากเปลี่ยนโค้ดใน `src/extension.ts`
* คุณยังสามารถรีโหลด (`Ctrl+R` หรือ `Cmd+R` บน Mac) หน้าต่าง VS Code ที่มีส่วนขยายของคุณเพื่อโหลดการเปลี่ยนแปลง

## สำรวจ API

* คุณสามารถเปิดชุด API ทั้งหมดของเราได้เมื่อเปิดไฟล์ `node_modules/@types/vscode/index.d.ts`

## รันเทสต์

* ติดตั้ง [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* รันงาน "watch" ผ่านคำสั่ง **Tasks: Run Task** ให้แน่ใจว่างานนี้กำลังทำงานอยู่ มิฉะนั้นเทสต์อาจไม่ถูกค้นพบ
* เปิด Testing view จาก activity bar แล้วคลิกปุ่ม Run Test หรือใช้คีย์ลัด `Ctrl/Cmd + ; A`
* ดูผลลัพธ์ของการทดสอบใน Test Results view
* แก้ไข `src/test/extension.test.ts` หรือสร้างไฟล์ทดสอบใหม่ภายในโฟลเดอร์ `test`
  * ตัวรันเทสต์ที่ให้มาจะพิจารณาเฉพาะไฟล์ที่ตรงกับรูปแบบชื่อ `**.test.ts` เท่านั้น
  * คุณสามารถสร้างโฟลเดอร์ภายใน `test` เพื่อจัดระเบียบเทสต์ของคุณตามต้องการ

## ก้าวไปไกลขึ้น

* ลดขนาดส่วนขยายและปรับปรุงเวลาการเริ่มต้นโดยการ [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)
* [Publish your extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) บนตลาดส่วนขยายของ VS Code
* ทำให้งาน build อัตโนมัติด้วยการตั้งค่า [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ควรใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้