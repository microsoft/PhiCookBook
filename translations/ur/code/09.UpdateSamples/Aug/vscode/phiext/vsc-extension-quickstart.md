<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-07T15:25:33+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "ur"
}
-->
# آپ کے VS Code ایکسٹینشن میں خوش آمدید

## فولڈر میں کیا ہے

* یہ فولڈر آپ کے ایکسٹینشن کے لیے تمام ضروری فائلز پر مشتمل ہے۔
* `package.json` - یہ مینفسٹ فائل ہے جس میں آپ اپنا ایکسٹینشن اور کمانڈ ظاہر کرتے ہیں۔
  * سیمپل پلگ ان ایک کمانڈ رجسٹر کرتا ہے اور اس کا عنوان اور کمانڈ نام متعین کرتا ہے۔ اس معلومات کے ذریعے VS Code کمانڈ پیلیٹ میں کمانڈ دکھا سکتا ہے۔ ابھی اسے پلگ ان لوڈ کرنے کی ضرورت نہیں ہے۔
* `src/extension.ts` - یہ مین فائل ہے جہاں آپ اپنے کمانڈ کا نفاذ فراہم کریں گے۔
  * فائل ایک فنکشن `activate` ایکسپورٹ کرتی ہے، جو آپ کے ایکسٹینشن کے پہلی بار ایکٹیویٹ ہونے پر (اس کیس میں کمانڈ چلانے پر) کال ہوتا ہے۔ `activate` فنکشن کے اندر ہم `registerCommand` کو کال کرتے ہیں۔
  * ہم کمانڈ کے نفاذ والا فنکشن `registerCommand` کو دوسرا پیرامیٹر کے طور پر دیتے ہیں۔

## سیٹ اپ

* تجویز کردہ ایکسٹینشنز انسٹال کریں (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, اور dbaeumer.vscode-eslint)

## فوراً شروع کریں

* ایک نیا ونڈو کھولنے کے لیے `F5` دبائیں جس میں آپ کا ایکسٹینشن لوڈ ہو۔
* کمانڈ پیلیٹ سے اپنا کمانڈ چلائیں (`Ctrl+Shift+P` یا میک پر `Cmd+Shift+P` دبائیں) اور `Hello World` ٹائپ کریں۔
* اپنے کوڈ میں `src/extension.ts` کے اندر بریک پوائنٹس سیٹ کریں تاکہ ایکسٹینشن کو ڈیبگ کر سکیں۔
* ڈیبگ کنسول میں اپنے ایکسٹینشن کا آؤٹ پٹ دیکھیں۔

## تبدیلیاں کریں

* `src/extension.ts` میں کوڈ تبدیل کرنے کے بعد ڈیبگ ٹول بار سے ایکسٹینشن کو دوبارہ لانچ کر سکتے ہیں۔
* آپ VS Code ونڈو کو اپنے ایکسٹینشن کے ساتھ دوبارہ لوڈ بھی کر سکتے ہیں (`Ctrl+R` یا میک پر `Cmd+R`) تاکہ تبدیلیاں لوڈ ہو جائیں۔

## API کو دریافت کریں

* جب آپ `node_modules/@types/vscode/index.d.ts` فائل کھولیں گے تو ہمارا پورا API سیٹ آپ کے لیے کھل جائے گا۔

## ٹیسٹ چلائیں

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) انسٹال کریں
* **Tasks: Run Task** کمانڈ کے ذریعے "watch" ٹاسک چلائیں۔ اس بات کو یقینی بنائیں کہ یہ چل رہا ہو ورنہ ٹیسٹ دریافت نہیں ہوں گے۔
* ایکٹیویٹی بار سے Testing ویو کھولیں اور "Run Test" بٹن پر کلک کریں، یا ہاٹ کی `Ctrl/Cmd + ; A` استعمال کریں۔
* ٹیسٹ کے نتائج کا آؤٹ پٹ Test Results ویو میں دیکھیں۔
* `src/test/extension.test.ts` میں تبدیلی کریں یا `test` فولڈر میں نئی ٹیسٹ فائلز بنائیں۔
  * فراہم کردہ ٹیسٹ رنر صرف وہی فائلز سمجھے گا جن کے نام کا پیٹرن `**.test.ts` سے میل کھاتا ہو۔
  * آپ اپنے ٹیسٹ کی ساخت کے لیے `test` فولڈر میں مزید فولڈرز بنا سکتے ہیں۔

## مزید آگے بڑھیں

* اپنے ایکسٹینشن کا سائز کم کریں اور اسٹارٹ اپ وقت بہتر بنائیں [اپنے ایکسٹینشن کو بنڈل کر کے](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)۔
* VS Code ایکسٹینشن مارکیٹ پلیس پر [اپنا ایکسٹینشن شائع کریں](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)۔
* [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) سیٹ اپ کر کے بلڈز کو خودکار بنائیں۔

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا بے ترتیبی ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر نہیں ہوگی۔