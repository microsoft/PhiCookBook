<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8d36fc444748a50558d017e8a0772437",
  "translation_date": "2025-04-04T11:31:35+00:00",
  "source_file": "code\\07.Lab\\01\\AIPC\\extensions\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "mo"
}
-->
# VS Code Extension-ээ тавтай морилно уу

## Энэ хавтас юу агуулж байна

* Энэ хавтас нь таны өргөтгөлд шаардлагатай бүх файлуудыг агуулна.
* `package.json` - Энэ бол таны өргөтгөл болон командыг зарлах манифест файл юм.
  * Жишээ залгаас нь нэг команд бүртгэж, түүний гарчиг болон командын нэрийг тодорхойлдог. Энэ мэдээллийн тусламжтайгаар VS Code командын палеттад командыг харуулж чадна. Гэхдээ залгаасыг ачаалахад хараахан шаардлагагүй.
* `src/extension.ts` - Энэ бол таны командын хэрэгжилтийг хангах үндсэн файл юм.
  * Файл нь нэг функц, `activate`-ийг экспортолдог бөгөөд энэ нь таны өргөтгөл анх идэвхжсэн үед (энэ тохиолдолд командыг гүйцэтгэснээр) дуудагддаг. `activate` функцийн дотор бид `registerCommand`-ийг дуудаж байна.
  * Командын хэрэгжилтийг агуулсан функцийг `registerCommand`-д хоёрдугаар параметр байдлаар дамжуулдаг.

## Тохиргоо

* Зөвлөмж болгож буй өргөтгөлүүдийг суулгаарай (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, болон dbaeumer.vscode-eslint)

## Шууд эхлүүлж ажиллуулаарай

* Таны өргөтгөлтэй шинэ цонхыг ачаалахын тулд `F5` товчийг дарна уу.
* Командаа командын палеттаас гүйцэтгэхийн тулд (`Ctrl+Shift+P` эсвэл Mac дээр `Cmd+Shift+P`) дарж, `Hello World` гэж бичнэ үү.
* Таны өргөтгөлийн код дотор `src/extension.ts`-д тасалбаруудыг (breakpoints) тавьж өргөтгөлөө дебаг хийнэ үү.
* Өргөтгөлийнхөө гаралтыг дебаг консолд олно уу.

## Өөрчлөлт хийх

* `src/extension.ts` дахь кодыг өөрчлөхийн дараа дебагийн баарнаас өргөтгөлөө дахин эхлүүлж болно.
* Мөн VS Code цонхыг (`Ctrl+R` эсвэл Mac дээр `Cmd+R`) дахин ачаалж, өөрчлөлтүүдээ ачаалж болно.

## API-г судлах

* `node_modules/@types/vscode/index.d.ts` файлыг нээж, API-ийн бүрэн багцтай танилцаарай.

## Туршилт хийх

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)-ийг суулгаарай.
* **Tasks: Run Task** командыг ашиглан "watch" үүргийг ажиллуул. Энэ ажиллаж байгаа эсэхийг шалгаарай, эс тэгвэл туршилтууд олдохгүй байж магадгүй.
* Үйл ажиллагааны мөрнөөс Туршилтын харах цонхыг нээж "Run Test" товчийг дарна уу, эсвэл `Ctrl/Cmd + ; A` товчлуурыг ашиглана уу.
* Туршилтын үр дүнг Test Results харах цонхонд үзнэ үү.
* `src/test/extension.test.ts` дээр өөрчлөлт хийн эсвэл `test` хавтас дотор шинэ туршилтын файлууд үүсгээрэй.
  * Өгөгдсөн туршилтын гүйцэтгэгч нь `**.test.ts` нэрийн хэв маягтай файлуудыг л авч үзнэ.
  * Туршилтуудаа ямар ч байдлаар зохион байгуулахын тулд `test` хавтас дотор хавтас үүсгэж болно.

## Цааш явах

* Өргөтгөлөө [багцлах](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo) замаар өргөтгөлийн хэмжээг багасгаж, эхлүүлэх хугацааг сайжруулаарай.
* Өргөтгөлөө VS Code өргөтгөлийн зах зээлд [нийтлээрэй](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Тасралтгүй интеграцчилал](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)-ыг тохируулж, барилгуудыг автоматжуулаарай.

It seems like you may be asking for a translation, but I'm not sure what "mo" refers to. Could you clarify the language or context you're referring to? For example, are you asking for a translation into Maori, Mongolian, or another language? Let me know so I can assist you accurately!