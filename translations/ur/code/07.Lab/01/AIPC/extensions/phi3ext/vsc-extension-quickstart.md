<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-07T15:21:08+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ur"
}
-->
# آپ کے VS Code ایکسٹینشن میں خوش آمدید

## فولڈر میں کیا ہے

* یہ فولڈر آپ کے ایکسٹینشن کے لیے تمام ضروری فائلیں رکھتا ہے۔
* `package.json` - یہ مینفسٹ فائل ہے جس میں آپ اپنے ایکسٹینشن اور کمانڈ کا اعلان کرتے ہیں۔
  * سیمپل پلگ ان ایک کمانڈ رجسٹر کرتا ہے اور اس کا عنوان اور کمانڈ نام متعین کرتا ہے۔ اس معلومات کے ساتھ VS Code کمانڈ پیلیٹ میں کمانڈ دکھا سکتا ہے۔ ابھی اسے پلگ ان لوڈ کرنے کی ضرورت نہیں ہے۔
* `src/extension.ts` - یہ مین فائل ہے جہاں آپ اپنے کمانڈ کا نفاذ فراہم کریں گے۔
  * یہ فائل ایک فنکشن `activate` ایکسپورٹ کرتی ہے، جو پہلی بار آپ کے ایکسٹینشن کے فعال ہونے پر (اس صورت میں کمانڈ چلانے پر) کال ہوتی ہے۔ `activate` فنکشن کے اندر ہم `registerCommand` کو کال کرتے ہیں۔
  * ہم کمانڈ کے نفاذ والا فنکشن دوسرا پیرامیٹر کے طور پر `registerCommand` کو دیتے ہیں۔

## سیٹ اپ

* تجویز کردہ ایکسٹینشنز انسٹال کریں (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, اور dbaeumer.vscode-eslint)

## فوراً شروع کریں

* `F5` دبائیں تاکہ آپ کے ایکسٹینشن کے ساتھ ایک نئی ونڈو کھلے۔
* کمانڈ پیلیٹ سے اپنے کمانڈ کو چلائیں، `Ctrl+Shift+P` یا میک پر `Cmd+Shift+P` دبائیں اور `Hello World` ٹائپ کریں۔
* اپنے کوڈ میں `src/extension.ts` کے اندر بریک پوائنٹس سیٹ کریں تاکہ ایکسٹینشن کی ڈیبگنگ ہو سکے۔
* ڈیبگ کنسول میں اپنے ایکسٹینشن کا آؤٹ پٹ دیکھیں۔

## تبدیلیاں کریں

* کوڈ میں تبدیلی کے بعد آپ ڈیبگ ٹول بار سے ایکسٹینشن کو دوبارہ شروع کر سکتے ہیں `src/extension.ts` میں۔
* آپ VS Code ونڈو کو بھی ری لوڈ کر سکتے ہیں (`Ctrl+R` یا میک پر `Cmd+R`) تاکہ آپ کی تبدیلیاں لوڈ ہوں۔

## API دریافت کریں

* جب آپ `node_modules/@types/vscode/index.d.ts` فائل کھولیں گے تو ہمارا مکمل API سیٹ کھل جائے گا۔

## ٹیسٹ چلائیں

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) انسٹال کریں
* **Tasks: Run Task** کمانڈ کے ذریعے "watch" ٹاسک چلائیں۔ اس بات کو یقینی بنائیں کہ یہ چل رہا ہو ورنہ ٹیسٹ دریافت نہیں ہوں گے۔
* ایکٹیویٹی بار سے Testing ویو کھولیں اور "Run Test" بٹن پر کلک کریں، یا ہاٹکی `Ctrl/Cmd + ; A` استعمال کریں۔
* Test Results ویو میں ٹیسٹ کے نتائج دیکھیں۔
* `src/test/extension.test.ts` میں تبدیلی کریں یا `test` فولڈر کے اندر نئے ٹیسٹ فائلز بنائیں۔
  * فراہم کردہ ٹیسٹ رنر صرف `**.test.ts` نام کے پیٹرن سے میل کھانے والی فائلز کو مدنظر رکھے گا۔
  * آپ `test` فولڈر کے اندر اپنے ٹیسٹ کی ساخت بنانے کے لیے مزید فولڈرز بھی بنا سکتے ہیں۔

## مزید آگے بڑھیں

* [اپنے ایکسٹینشن کو بنڈل کر کے](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo) اس کا سائز کم کریں اور اسٹارٹ اپ وقت بہتر بنائیں۔
* VS Code ایکسٹینشن مارکیٹ پلیس پر [اپنا ایکسٹینشن شائع کریں](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)۔
* [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) سیٹ اپ کر کے بلڈز کو خودکار بنائیں۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم نوٹ کریں کہ خودکار ترجمے میں غلطیاں یا عدم صحت ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں معتبر ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر نہیں ہوگی۔