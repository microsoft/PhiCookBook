<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-07T10:15:02+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ar"
}
-->
# مرحبًا بك في امتداد VS Code الخاص بك

## ما يحتويه المجلد

* يحتوي هذا المجلد على جميع الملفات اللازمة لامتدادك.
* `package.json` - هذا هو ملف التعريف الذي تعلن فيه عن امتدادك والأمر الخاص به.
  * يقوم المكون الإضافي النموذجي بتسجيل أمر ويحدد عنوانه واسم الأمر. باستخدام هذه المعلومات، يمكن لـ VS Code عرض الأمر في لوحة الأوامر. لا يحتاج بعد إلى تحميل المكون الإضافي.
* `src/extension.ts` - هذا هو الملف الرئيسي حيث ستوفر تنفيذ الأمر الخاص بك.
  * يصدر الملف دالة واحدة، `activate`، والتي يتم استدعاؤها في أول مرة يتم فيها تفعيل امتدادك (في هذه الحالة عن طريق تنفيذ الأمر). داخل دالة `activate` نستدعي `registerCommand`.
  * نمرر الدالة التي تحتوي على تنفيذ الأمر كوسيط ثاني إلى `registerCommand`.

## الإعداد

* قم بتثبيت الامتدادات الموصى بها (amodio.tsl-problem-matcher، ms-vscode.extension-test-runner، و dbaeumer.vscode-eslint)


## ابدأ العمل فورًا

* اضغط `F5` لفتح نافذة جديدة مع تحميل امتدادك.
* نفذ الأمر الخاص بك من لوحة الأوامر بالضغط على (`Ctrl+Shift+P` أو `Cmd+Shift+P` على نظام ماك) وكتابة `Hello World`.
* ضع نقاط توقف في الكود داخل `src/extension.ts` لتصحيح امتدادك.
* اعثر على المخرجات من امتدادك في وحدة تحكم التصحيح.

## إجراء التغييرات

* يمكنك إعادة تشغيل الامتداد من شريط أدوات التصحيح بعد تعديل الكود في `src/extension.ts`.
* يمكنك أيضًا إعادة تحميل (`Ctrl+R` أو `Cmd+R` على نظام ماك) نافذة VS Code مع امتدادك لتحميل التغييرات.


## استكشاف واجهة برمجة التطبيقات (API)

* يمكنك فتح مجموعة كاملة من واجهة برمجة التطبيقات الخاصة بنا عند فتح الملف `node_modules/@types/vscode/index.d.ts`.

## تشغيل الاختبارات

* قم بتثبيت [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* شغّل مهمة "المراقبة" عبر أمر **Tasks: Run Task**. تأكد من أن المهمة تعمل، وإلا قد لا يتم اكتشاف الاختبارات.
* افتح عرض الاختبار من شريط النشاط واضغط زر "تشغيل الاختبار"، أو استخدم مفتاح الاختصار `Ctrl/Cmd + ; A`
* شاهد مخرجات نتائج الاختبار في عرض نتائج الاختبار.
* قم بإجراء تغييرات على `src/test/extension.test.ts` أو أنشئ ملفات اختبار جديدة داخل مجلد `test`.
  * سيأخذ مشغل الاختبارات المزود بعين الاعتبار فقط الملفات التي تطابق نمط الاسم `**.test.ts`.
  * يمكنك إنشاء مجلدات داخل مجلد `test` لتنظيم اختباراتك بالطريقة التي تريدها.

## التقدم أكثر

* قلل حجم الامتداد وحسن وقت بدء التشغيل من خلال [تجميع امتدادك](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [انشر امتدادك](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) على سوق امتدادات VS Code.
* أتمتة عمليات البناء عن طريق إعداد [التكامل المستمر](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.