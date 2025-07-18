<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T17:01:42+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "th"
}
-->
# ยินดีต้อนรับสู่ส่วนขยาย VS Code ของคุณ

## มีอะไรอยู่ในโฟลเดอร์นี้

* โฟลเดอร์นี้ประกอบด้วยไฟล์ทั้งหมดที่จำเป็นสำหรับส่วนขยายของคุณ
* `package.json` - ไฟล์ manifest ที่คุณประกาศส่วนขยายและคำสั่งของคุณ
  * ปลั๊กอินตัวอย่างจะลงทะเบียนคำสั่งและกำหนดชื่อเรื่องกับชื่อคำสั่ง ด้วยข้อมูลนี้ VS Code จะสามารถแสดงคำสั่งใน command palette ได้ โดยยังไม่ต้องโหลดปลั๊กอิน
* `src/extension.ts` - ไฟล์หลักที่คุณจะเขียนโค้ดสำหรับคำสั่งของคุณ
  * ไฟล์นี้จะส่งออกฟังก์ชันหนึ่งชื่อ `activate` ซึ่งจะถูกเรียกครั้งแรกเมื่อส่วนขยายของคุณถูกเปิดใช้งาน (ในกรณีนี้คือเมื่อรันคำสั่ง) ภายในฟังก์ชัน `activate` เราจะเรียก `registerCommand`
  * เราส่งฟังก์ชันที่มีโค้ดคำสั่งเป็นพารามิเตอร์ตัวที่สองให้กับ `registerCommand`

## การตั้งค่า

* ติดตั้งส่วนขยายที่แนะนำ (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, และ dbaeumer.vscode-eslint)

## เริ่มใช้งานได้ทันที

* กด `F5` เพื่อเปิดหน้าต่างใหม่ที่โหลดส่วนขยายของคุณ
* รันคำสั่งของคุณจาก command palette โดยกด (`Ctrl+Shift+P` หรือ `Cmd+Shift+P` บน Mac) แล้วพิมพ์ `Hello World`
* ตั้ง breakpoints ในโค้ดของคุณภายใน `src/extension.ts` เพื่อดีบักส่วนขยาย
* ดูผลลัพธ์จากส่วนขยายของคุณใน debug console

## การแก้ไข

* คุณสามารถเปิดส่วนขยายใหม่จากแถบเครื่องมือดีบักหลังจากแก้ไขโค้ดใน `src/extension.ts`
* คุณยังสามารถรีโหลดหน้าต่าง VS Code (`Ctrl+R` หรือ `Cmd+R` บน Mac) ที่มีส่วนขยายของคุณเพื่อโหลดการเปลี่ยนแปลง

## สำรวจ API

* คุณสามารถเปิดชุด API ทั้งหมดได้โดยเปิดไฟล์ `node_modules/@types/vscode/index.d.ts`

## การรันเทสต์

* ติดตั้ง [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* รันงาน "watch" ผ่านคำสั่ง **Tasks: Run Task** ให้แน่ใจว่างานนี้กำลังทำงานอยู่ มิฉะนั้นเทสต์อาจไม่ถูกค้นพบ
* เปิด Testing view จาก activity bar แล้วคลิกปุ่ม "Run Test" หรือใช้คีย์ลัด `Ctrl/Cmd + ; A`
* ดูผลลัพธ์ของเทสต์ใน Test Results view
* แก้ไขไฟล์ `src/test/extension.test.ts` หรือสร้างไฟล์เทสต์ใหม่ในโฟลเดอร์ `test`
  * ตัวรันเทสต์ที่ให้มาจะพิจารณาเฉพาะไฟล์ที่ตรงกับรูปแบบชื่อ `**.test.ts`
  * คุณสามารถสร้างโฟลเดอร์ย่อยในโฟลเดอร์ `test` เพื่อจัดระเบียบเทสต์ของคุณได้ตามต้องการ

## ก้าวไปไกลกว่าเดิม

* ลดขนาดส่วนขยายและปรับปรุงเวลาเริ่มต้นโดยการ [บันเดิลส่วนขยายของคุณ](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)
* [เผยแพร่ส่วนขยายของคุณ](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) บนตลาดส่วนขยาย VS Code
* อัตโนมัติการสร้างโดยตั้งค่า [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้