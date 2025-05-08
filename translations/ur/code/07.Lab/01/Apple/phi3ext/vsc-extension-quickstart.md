<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-07T15:23:18+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ur"
}
-->
# آپ کے VS Code ایکسٹینشن میں خوش آمدید

## فولڈر میں کیا ہے

* یہ فولڈر آپ کے ایکسٹینشن کے لیے تمام ضروری فائلز پر مشتمل ہے۔
* `package.json` - یہ manifest فائل ہے جس میں آپ اپنے ایکسٹینشن اور کمانڈ کا اعلان کرتے ہیں۔
  * sample plugin ایک کمانڈ رجسٹر کرتا ہے اور اس کا عنوان اور کمانڈ نام متعین کرتا ہے۔ اس معلومات کی مدد سے VS Code کمانڈ کو command palette میں دکھا سکتا ہے۔ ابھی اسے plugin لوڈ کرنے کی ضرورت نہیں ہے۔
* `src/extension.ts` - یہ مین فائل ہے جہاں آپ اپنے کمانڈ کا implementation فراہم کریں گے۔
  * یہ فائل ایک فنکشن `activate` export کرتی ہے، جو پہلی بار آپ کے ایکسٹینشن کے فعال ہونے پر کال ہوتی ہے (اس کیس میں کمانڈ چلانے سے)۔ `activate` فنکشن کے اندر ہم `registerCommand` کو کال کرتے ہیں۔
  * ہم کمانڈ کے implementation والی فنکشن کو `registerCommand` کو دوسرا parameter کے طور پر پاس کرتے ہیں۔

## سیٹ اپ

* سفارش کردہ ایکسٹینشنز انسٹال کریں (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, اور dbaeumer.vscode-eslint)

## فوراً شروع کریں

* `F5` دبائیں تاکہ آپ کا ایکسٹینشن لوڈ شدہ ایک نئی ونڈو کھلے۔
* کمانڈ پیلیٹ سے اپنا کمانڈ چلائیں (Mac پر `Ctrl+Shift+P` یا `Cmd+Shift+P` دبائیں) اور `Hello World` ٹائپ کریں۔
* `src/extension.ts` میں اپنے کوڈ میں breakpoints سیٹ کریں تاکہ ایکسٹینشن کی ڈیبگنگ کی جا سکے۔
* ڈیبگ کنسول میں اپنے ایکسٹینشن کا آؤٹ پٹ دیکھیں۔

## تبدیلیاں کریں

* `src/extension.ts` میں کوڈ تبدیل کرنے کے بعد debug toolbar سے ایکسٹینشن کو دوبارہ لانچ کر سکتے ہیں۔
* آپ VS Code کی ونڈو کو دوبارہ لوڈ بھی کر سکتے ہیں (`Ctrl+R` یا Mac پر `Cmd+R`) تاکہ اپنی تبدیلیاں لوڈ ہوں۔

## API کو دریافت کریں

* جب آپ `node_modules/@types/vscode/index.d.ts` فائل کھولیں گے تو ہمارا مکمل API سیٹ آپ کے لیے کھل جائے گا۔

## ٹیسٹ چلائیں

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) انسٹال کریں
* **Tasks: Run Task** کمانڈ کے ذریعے "watch" ٹاسک چلائیں۔ یہ یقینی بنائیں کہ یہ چل رہا ہو ورنہ ٹیسٹ دریافت نہیں ہوں گے۔
* activity bar سے Testing ویو کھولیں اور "Run Test" بٹن پر کلک کریں، یا ہاٹکی `Ctrl/Cmd + ; A` استعمال کریں۔
* Test Results ویو میں ٹیسٹ کے نتائج دیکھیں۔
* `src/test/extension.test.ts` میں تبدیلی کریں یا `test` فولڈر کے اندر نئے ٹیسٹ فائلز بنائیں۔
  * فراہم کردہ test runner صرف وہ فائلز دیکھے گا جو `**.test.ts` نام کے پیٹرن سے میل کھاتی ہوں۔
  * آپ `test` فولڈر کے اندر اپنی مرضی کے مطابق فولڈرز بنا کر ٹیسٹس کو منظم کر سکتے ہیں۔

## آگے بڑھیں

* [اپنے ایکسٹینشن کو باندھ کر](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) اس کا سائز کم کریں اور startup وقت بہتر بنائیں۔
* VS Code ایکسٹینشن مارکیٹ پلیس پر [اپنا ایکسٹینشن شائع کریں](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)۔
* [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) سیٹ اپ کر کے بلڈز کو خودکار بنائیں۔

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر نہیں ہوگی۔