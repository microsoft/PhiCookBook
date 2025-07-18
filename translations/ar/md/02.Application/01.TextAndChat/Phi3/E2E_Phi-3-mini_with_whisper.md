<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:13:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ar"
}
-->
# روبوت الدردشة التفاعلي Phi 3 Mini 4K Instruct مع Whisper

## نظرة عامة

روبوت الدردشة التفاعلي Phi 3 Mini 4K Instruct هو أداة تتيح للمستخدمين التفاعل مع عرض Microsoft Phi 3 Mini 4K instruct باستخدام إدخال نصي أو صوتي. يمكن استخدام روبوت الدردشة في مهام متنوعة مثل الترجمة، تحديثات الطقس، وجمع المعلومات العامة.

### البدء

لاستخدام هذا الروبوت، اتبع التعليمات التالية:

1. افتح ملف [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. في النافذة الرئيسية للدفتر، سترى واجهة صندوق دردشة مع مربع إدخال نص وزر "إرسال".
3. لاستخدام روبوت الدردشة النصي، ببساطة اكتب رسالتك في مربع الإدخال النصي واضغط على زر "إرسال". سيرد روبوت الدردشة بملف صوتي يمكن تشغيله مباشرة من داخل الدفتر.

**ملاحظة**: هذه الأداة تتطلب وجود GPU والوصول إلى نماذج Microsoft Phi-3 وOpenAI Whisper، والتي تُستخدم للتعرف على الكلام والترجمة.

### متطلبات GPU

لتشغيل هذا العرض التوضيحي تحتاج إلى 12 جيجابايت من ذاكرة GPU.

تعتمد متطلبات الذاكرة لتشغيل عرض **Microsoft-Phi-3-Mini-4K instruct** على GPU على عدة عوامل، مثل حجم البيانات المدخلة (صوت أو نص)، اللغة المستخدمة للترجمة، سرعة النموذج، والذاكرة المتاحة على GPU.

بشكل عام، تم تصميم نموذج Whisper ليعمل على وحدات معالجة الرسومات. الحد الأدنى الموصى به لذاكرة GPU لتشغيل نموذج Whisper هو 8 جيجابايت، لكنه يمكن التعامل مع كميات أكبر من الذاكرة إذا لزم الأمر.

من المهم ملاحظة أن تشغيل كمية كبيرة من البيانات أو حجم مرتفع من الطلبات على النموذج قد يتطلب ذاكرة GPU أكبر و/أو قد يسبب مشاكل في الأداء. يُنصح باختبار حالة الاستخدام الخاصة بك مع إعدادات مختلفة ومراقبة استخدام الذاكرة لتحديد الإعدادات المثلى لاحتياجاتك الخاصة.

## مثال E2E لروبوت الدردشة التفاعلي Phi 3 Mini 4K Instruct مع Whisper

يوضح دفتر Jupyter المعنون [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) كيفية استخدام عرض Microsoft Phi 3 Mini 4K instruct لتوليد نص من إدخال صوتي أو نصي. يعرف الدفتر عدة دوال:

1. `tts_file_name(text)`: هذه الدالة تولد اسم ملف بناءً على النص المدخل لحفظ ملف الصوت الناتج.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: تستخدم هذه الدالة واجهة برمجة تطبيقات Edge TTS لتوليد ملف صوتي من قائمة مقاطع نصية. المعطيات هي قائمة المقاطع، سرعة الكلام، اسم الصوت، ومسار الحفظ لملف الصوت الناتج.
1. `talk(input_text)`: تولد هذه الدالة ملف صوتي باستخدام واجهة Edge TTS وتحفظه باسم ملف عشوائي في مجلد /content/audio. المعطى هو النص المراد تحويله إلى كلام.
1. `run_text_prompt(message, chat_history)`: تستخدم هذه الدالة عرض Microsoft Phi 3 Mini 4K instruct لتوليد ملف صوتي من رسالة نصية وتضيفه إلى سجل الدردشة.
1. `run_audio_prompt(audio, chat_history)`: تحول هذه الدالة ملف صوتي إلى نص باستخدام نموذج Whisper API ثم تمرره إلى دالة `run_text_prompt()`.
1. يقوم الكود بتشغيل تطبيق Gradio يسمح للمستخدمين بالتفاعل مع عرض Phi 3 Mini 4K instruct إما بكتابة الرسائل أو رفع ملفات صوتية. يتم عرض الناتج كرسالة نصية داخل التطبيق.

## استكشاف الأخطاء وإصلاحها

تثبيت تعريفات Cuda GPU

1. تأكد من تحديث تطبيقات Linux الخاصة بك

    ```bash
    sudo apt update
    ```

1. تثبيت تعريفات Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. تسجيل موقع تعريف cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. التحقق من حجم ذاكرة Nvidia GPU (مطلوب 12 جيجابايت من ذاكرة GPU)

    ```bash
    nvidia-smi
    ```

1. تفريغ الذاكرة المؤقتة: إذا كنت تستخدم PyTorch، يمكنك استدعاء torch.cuda.empty_cache() لتحرير كل الذاكرة المؤقتة غير المستخدمة بحيث يمكن لتطبيقات GPU الأخرى استخدامها

    ```python
    torch.cuda.empty_cache() 
    ```

1. التحقق من Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. قم بالمهام التالية لإنشاء رمز Hugging Face.

    - انتقل إلى [صفحة إعدادات رموز Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - اختر **New token**.
    - أدخل اسم المشروع الذي تريد استخدامه.
    - اختر **Type** إلى **Write**.

> **ملاحظة**
>
> إذا واجهت الخطأ التالي:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> لحل هذه المشكلة، اكتب الأمر التالي داخل الطرفية الخاصة بك.
>
> ```bash
> sudo ldconfig
> ```

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.