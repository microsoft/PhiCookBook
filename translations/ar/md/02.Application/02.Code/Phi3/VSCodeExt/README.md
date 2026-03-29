# **قم ببناء وكيل GitHub Copilot Chat الخاص بـ Visual Studio Code باستخدام عائلة Microsoft Phi-3**

هل استخدمت وكيل مساحة العمل في GitHub Copilot Chat؟ هل ترغب في بناء وكيل الكود الخاص بفريقك؟ يأمل هذا المختبر العملي في دمج نموذج مفتوح المصدر لبناء وكيل أعمال كود على مستوى المؤسسات.

## **الأساس**

### **لماذا تختار Microsoft Phi-3**

Phi-3 هي سلسلة عائلية، تشمل phi-3-mini، phi-3-small، و phi-3-medium اعتمادًا على معلمات تدريب مختلفة لتوليد النصوص، إكمال الحوار، وتوليد الكود. يوجد أيضًا phi-3-vision المبني على الرؤية. وهو مناسب للمؤسسات أو الفرق المختلفة لإنشاء حلول AI توليدية تعمل دون اتصال.

يوصى بقراءة هذا الرابط [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

تمكنك إضافة GitHub Copilot Chat من الحصول على واجهة محادثة تسمح لك بالتفاعل مع GitHub Copilot والحصول على إجابات لأسئلة متعلقة بالبرمجة مباشرة داخل VS Code، دون الحاجة إلى تصفح الوثائق أو البحث في المنتديات على الإنترنت.

قد يستخدم Copilot Chat تمييز الصياغة، والتراجع، وميزات تنسيق أخرى لإضافة وضوح إلى الاستجابة المولدة. اعتمادًا على نوع السؤال من المستخدم، قد يتضمن الناتج روابط للسياق الذي استخدمه Copilot لتوليد الاستجابة، مثل ملفات شفرة المصدر أو الوثائق، أو أزرارًا للوصول إلى وظائف VS Code.

- يتكامل Copilot Chat في تدفق عمل المطور ويمنحك المساعدة حيث تحتاج إليها:

- ابدأ محادثة دردشة مضمنة مباشرة من المحرر أو الطرفية للحصول على مساعدة أثناء الترميز

- استخدم عرض الدردشة للحصول على مساعد AI بجانبك لمساعدتك في أي وقت

- أطلق الدردشة السريعة لطرح سؤال سريع والعودة إلى ما تفعله

يمكنك استخدام GitHub Copilot Chat في سيناريوهات مختلفة، مثل:

- الإجابة على أسئلة البرمجة حول أفضل طريقة لحل مشكلة

- شرح كود لشخص آخر واقتراح تحسينات

- اقتراح إصلاحات للكود

- توليد حالات اختبار وحدة

- توليد توثيق الكود

يوصى بقراءة هذا الرابط [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

الرجوع إلى **@workspace** في Copilot Chat يتيح لك طرح أسئلة حول كامل قاعدة الكود الخاصة بك. استنادًا إلى السؤال، يقوم Copilot بجلب الملفات والرموز ذات الصلة بذكاء، والتي يقوم بعد ذلك بالإشارة إليها في إجابته كرابط وأمثلة كود.

للإجابة على سؤالك، يبحث **@workspace** من خلال نفس المصادر التي يستخدمها المطور عند التنقل في قاعدة الكود في VS Code:

- جميع الملفات في مساحة العمل، باستثناء الملفات التي تم تجاهلها بواسطة ملف .gitignore

- هيكل الدليل مع المجلدات والملفات المتداخلة

- فهرس بحث الكود في GitHub، إذا كانت مساحة العمل مستودعًا في GitHub ومفهرسة بواسطة بحث الكود

- الرموز والتعريفات في مساحة العمل

- النص المحدد حاليًا أو النص الظاهر في المحرر النشط

ملاحظة: يتم تجاوز .gitignore إذا كان لديك ملف مفتوح أو لديك نص محدد ضمن ملف تم تجاهله.

يوصى بقراءة هذا الرابط [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **تعرف أكثر على هذا المختبر**

حسن GitHub Copilot بشكل كبير من كفاءة البرمجة في المؤسسات، وكل مؤسسة تأمل في تخصيص الوظائف ذات الصلة بـ GitHub Copilot. قامت العديد من المؤسسات بتخصيص إضافات مشابهة لـ GitHub Copilot بناءً على سيناريوهات أعمالها ونماذج مفتوحة المصدر. بالنسبة للمؤسسات، فإن الإضافات المخصصة أسهل في التحكم، لكن هذا يؤثر أيضًا على تجربة المستخدم. فـ GitHub Copilot يمتلك وظائف أقوى في التعامل مع السيناريوهات العامة والاحترافية. إذا أمكن الحفاظ على تجربة متسقة، فسيكون من الأفضل تخصيص إضافة خاصة بالمؤسسة. يوفر GitHub Copilot Chat واجهات برمجية ذات صلة للمؤسسات لتوسيع تجربة الدردشة. الحفاظ على تجربة متسقة وامتلاك وظائف مخصصة هو تجربة مستخدم أفضل.

يعتمد هذا المختبر أساسًا على نموذج Phi-3 المدمج مع NPU المحلي وهجين Azure لبناء وكيل مخصص في GitHub Copilot Chat ***@PHI3*** لمساعدة مطوري المؤسسات في إكمال توليد الكود***(@PHI3 /gen)*** وتوليد الكود بناءً على الصور ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/ar/cover.1017ebc9a7c46d09.webp)

### ***ملاحظة:*** 

يتم تنفيذ هذا المختبر حاليًا على AIPC بمعالجات Intel وApple Silicon. سنستمر في تحديث نسخة Qualcomm من NPU.


## **المختبر**


| الاسم | الوصف | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - التثبيتات(✅) | تكوين وتثبيت البيئات والأدوات ذات الصلة | [اذهب](./HOL/AIPC/01.Installations.md) |[اذهب](./HOL/Apple/01.Installations.md) |
| Lab1 - تشغيل تدفق الطلب مع Phi-3-mini (✅) | بالتعاون مع AIPC / Apple Silicon، استخدام NPU المحلي لإنشاء توليد كود عبر Phi-3-mini | [اذهب](./HOL/AIPC/02.PromptflowWithNPU.md) |  [اذهب](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - نشر Phi-3-vision على خدمة Azure Machine Learning(✅) | توليد الكود عبر نشر كتالوج النماذج الخاص بخدمة Azure Machine Learning - صورة Phi-3-vision | [اذهب](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[اذهب](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - إنشاء وكيل @phi-3 في GitHub Copilot Chat(✅)  | إنشاء وكيل Phi-3 مخصص في GitHub Copilot Chat لإكمال توليد الكود، إنشاء كود الرسم البياني، RAG، إلخ. | [اذهب](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [اذهب](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| كود مثال (✅)  | تنزيل كود مثال | [اذهب](../../../../../../../code/07.Lab/01/AIPC) | [اذهب](../../../../../../../code/07.Lab/01/Apple) |


## **الموارد**

1. كتاب طهي Phi-3 [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. تعرف أكثر على GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. تعرف أكثر على GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. تعرف أكثر على واجهة برمجة تطبيقات GitHub Copilot Chat [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. تعرف أكثر على Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. تعرف أكثر على كتالوج النماذج الخاص بـ Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. ينبغي اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والموثوق. للمعلومات الدقيقة والهامة، يُنصح باستخدام ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء تفاهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->