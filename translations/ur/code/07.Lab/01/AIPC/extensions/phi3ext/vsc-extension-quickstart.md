<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-07-16T16:40:21+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ur"
}
-->
# آپ کے VS Code ایکسٹینشن میں خوش آمدید

## فولڈر میں کیا ہے

* اس فولڈر میں آپ کے ایکسٹینشن کے لیے تمام ضروری فائلیں موجود ہیں۔
* `package.json` - یہ مینفیسٹ فائل ہے جس میں آپ اپنا ایکسٹینشن اور کمانڈ ظاہر کرتے ہیں۔
  * سیمپل پلگ ان ایک کمانڈ رجسٹر کرتا ہے اور اس کا عنوان اور کمانڈ نام متعین کرتا ہے۔ اس معلومات کی مدد سے VS Code کمانڈ پیلیٹ میں کمانڈ دکھا سکتا ہے۔ ابھی اسے پلگ ان لوڈ کرنے کی ضرورت نہیں ہے۔
* `src/extension.ts` - یہ مرکزی فائل ہے جہاں آپ اپنے کمانڈ کا نفاذ فراہم کریں گے۔
  * یہ فائل ایک فنکشن `activate` ایکسپورٹ کرتی ہے، جو آپ کے ایکسٹینشن کے پہلی بار فعال ہونے پر کال کی جاتی ہے (اس صورت میں کمانڈ چلانے سے)۔ `activate` فنکشن کے اندر ہم `registerCommand` کال کرتے ہیں۔
  * ہم کمانڈ کے نفاذ والا فنکشن `registerCommand` کو دوسرا پیرامیٹر کے طور پر دیتے ہیں۔

## سیٹ اپ

* تجویز کردہ ایکسٹینشنز انسٹال کریں (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, اور dbaeumer.vscode-eslint)

## فوراً شروع کریں

* `F5` دبائیں تاکہ ایک نئی ونڈو کھلے جس میں آپ کا ایکسٹینشن لوڈ ہو۔
* کمانڈ پیلیٹ سے (`Ctrl+Shift+P` یا Mac پر `Cmd+Shift+P`) اپنا کمانڈ چلائیں اور `Hello World` ٹائپ کریں۔
* اپنے کوڈ میں `src/extension.ts` کے اندر بریک پوائنٹس سیٹ کریں تاکہ ایکسٹینشن کو ڈیبگ کر سکیں۔
* ڈیبگ کنسول میں اپنے ایکسٹینشن کا آؤٹ پٹ دیکھیں۔

## تبدیلیاں کریں

* `src/extension.ts` میں کوڈ تبدیل کرنے کے بعد ڈیبگ ٹول بار سے ایکسٹینشن کو دوبارہ شروع کر سکتے ہیں۔
* آپ VS Code ونڈو کو بھی ری لوڈ کر سکتے ہیں (`Ctrl+R` یا Mac پر `Cmd+R`) تاکہ آپ کی تبدیلیاں لوڈ ہو جائیں۔

## API کو دریافت کریں

* جب آپ فائل `node_modules/@types/vscode/index.d.ts` کھولیں گے تو آپ ہماری API کا مکمل سیٹ دیکھ سکتے ہیں۔

## ٹیسٹ چلائیں

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) انسٹال کریں
* **Tasks: Run Task** کمانڈ کے ذریعے "watch" ٹاسک چلائیں۔ اس بات کو یقینی بنائیں کہ یہ چل رہا ہو ورنہ ٹیسٹ دریافت نہیں ہوں گے۔
* ایکٹیویٹی بار سے Testing ویو کھولیں اور "Run Test" بٹن پر کلک کریں، یا ہاٹکی `Ctrl/Cmd + ; A` استعمال کریں۔
* Test Results ویو میں ٹیسٹ کے نتائج دیکھیں۔
* `src/test/extension.test.ts` میں تبدیلی کریں یا `test` فولڈر کے اندر نئے ٹیسٹ فائلز بنائیں۔
  * فراہم کردہ ٹیسٹ رنر صرف ان فائلوں کو دیکھے گا جن کے نام کا پیٹرن `**.test.ts` ہو۔
  * آپ `test` فولڈر کے اندر فولڈرز بنا کر اپنے ٹیسٹ کسی بھی ترتیب میں رکھ سکتے ہیں۔

## مزید آگے بڑھیں

* [اپنے ایکسٹینشن کو بنڈل کر کے](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo) اس کا سائز کم کریں اور اسٹارٹ اپ وقت بہتر بنائیں۔
* VS Code ایکسٹینشن مارکیٹ پلیس پر [اپنا ایکسٹینشن شائع کریں](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)۔
* [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) سیٹ اپ کر کے بلڈز کو خودکار بنائیں۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔