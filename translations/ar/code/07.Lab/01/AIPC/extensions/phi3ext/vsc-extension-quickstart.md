<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-07-16T16:40:01+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ar"
}
-->
# مرحبًا بك في إضافة VS Code الخاصة بك

## ما الموجود في المجلد

* يحتوي هذا المجلد على جميع الملفات اللازمة لإضافتك.
* `package.json` - هذا هو ملف التعريف الذي تعلن فيه عن الإضافة والأمر الخاص بك.
  * يقوم الملحق النموذجي بتسجيل أمر ويحدد عنوانه واسم الأمر. باستخدام هذه المعلومات يمكن لـ VS Code عرض الأمر في لوحة الأوامر. لا يحتاج بعد إلى تحميل الملحق.
* `src/extension.ts` - هذا هو الملف الرئيسي حيث ستوفر تنفيذ الأمر الخاص بك.
  * يصدر الملف دالة واحدة، `activate`، التي تُستدعى في المرة الأولى التي يتم فيها تفعيل الإضافة (في هذه الحالة عن طريق تنفيذ الأمر). داخل دالة `activate` نستدعي `registerCommand`.
  * نمرر الدالة التي تحتوي على تنفيذ الأمر كمعامل ثاني إلى `registerCommand`.

## الإعداد

* قم بتثبيت الإضافات الموصى بها (amodio.tsl-problem-matcher، ms-vscode.extension-test-runner، و dbaeumer.vscode-eslint)

## ابدأ العمل فورًا

* اضغط على `F5` لفتح نافذة جديدة مع تحميل الإضافة الخاصة بك.
* نفذ الأمر الخاص بك من لوحة الأوامر بالضغط على (`Ctrl+Shift+P` أو `Cmd+Shift+P` على ماك) وكتابة `Hello World`.
* ضع نقاط توقف في الكود داخل `src/extension.ts` لتصحيح الإضافة.
* اعثر على مخرجات الإضافة في وحدة تحكم التصحيح.

## إجراء التعديلات

* يمكنك إعادة تشغيل الإضافة من شريط أدوات التصحيح بعد تعديل الكود في `src/extension.ts`.
* يمكنك أيضًا إعادة تحميل نافذة VS Code مع الإضافة الخاصة بك بالضغط على (`Ctrl+R` أو `Cmd+R` على ماك) لتحميل التغييرات.

## استكشاف API

* يمكنك فتح مجموعة API الكاملة عند فتح الملف `node_modules/@types/vscode/index.d.ts`.

## تشغيل الاختبارات

* قم بتثبيت [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* شغّل مهمة "watch" عبر أمر **Tasks: Run Task**. تأكد من تشغيلها، وإلا قد لا يتم اكتشاف الاختبارات.
* افتح عرض الاختبارات من شريط النشاط واضغط على زر "Run Test"، أو استخدم الاختصار `Ctrl/Cmd + ; A`
* شاهد نتائج الاختبارات في عرض نتائج الاختبار.
* قم بإجراء تغييرات على `src/test/extension.test.ts` أو أنشئ ملفات اختبار جديدة داخل مجلد `test`.
  * سيأخذ مشغل الاختبارات المقدم بعين الاعتبار فقط الملفات التي تطابق نمط الاسم `**.test.ts`.
  * يمكنك إنشاء مجلدات داخل مجلد `test` لتنظيم اختباراتك كما تريد.

## التقدم أكثر

* قلل حجم الإضافة وحسّن وقت بدء التشغيل عن طريق [تجميع الإضافة](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [انشر الإضافة الخاصة بك](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) في سوق إضافات VS Code.
* أتمتة عمليات البناء عن طريق إعداد [التكامل المستمر](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.