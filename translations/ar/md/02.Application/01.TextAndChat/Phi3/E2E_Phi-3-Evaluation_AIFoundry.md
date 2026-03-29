# تقييم نموذج Phi-3 / Phi-3.5 المحسن في Microsoft Foundry مع التركيز على مبادئ الذكاء الاصطناعي المسؤول من Microsoft

يعتمد هذا المثال الشامل (E2E) على الدليل "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" من مجتمع Microsoft Tech.

## نظرة عامة

### كيف يمكنك تقييم سلامة وأداء نموذج Phi-3 / Phi-3.5 المحسن في Microsoft Foundry؟

قد يؤدي تحسين النموذج أحيانًا إلى استجابات غير مقصودة أو غير مرغوب فيها. لضمان بقاء النموذج آمنًا وفعالًا، من المهم تقييم احتمالية توليد المحتوى الضار وقدرته على إنتاج استجابات دقيقة وذات صلة ومتسقة. في هذا البرنامج التعليمي، ستتعلم كيفية تقييم سلامة وأداء نموذج Phi-3 / Phi-3.5 المحسن المدمج مع Prompt flow في Microsoft Foundry.

فيما يلي عملية التقييم في Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/ar/architecture.10bec55250f5d6a4.webp)

*مصدر الصورة: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> لمزيد من المعلومات التفصيلية واستكشاف موارد إضافية حول Phi-3 / Phi-3.5، يرجى زيارة [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### المتطلبات الأساسية

- [Python](https://www.python.org/downloads)
- [اشتراك Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- نموذج Phi-3 / Phi-3.5 المحسن

### جدول المحتويات

1. [**السيناريو 1: مقدمة لتقييم Prompt flow في Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [مقدمة لتقييم السلامة](#مقدمة-لتقييم-السلامة)
    - [مقدمة لتقييم الأداء](#مقدمة-لتقييم-الأداء)

1. [**السيناريو 2: تقييم نموذج Phi-3 / Phi-3.5 في Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [قبل أن تبدأ](#قبل-أن-تبدأ)
    - [نشر Azure OpenAI لتقييم نموذج Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [تقييم نموذج Phi-3 / Phi-3.5 المحسن باستخدام تقييم Prompt flow في Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [تهانينا!](#تهانينا)

## **السيناريو 1: مقدمة لتقييم Prompt flow في Microsoft Foundry**

### مقدمة لتقييم السلامة

لضمان أن نموذج الذكاء الاصطناعي الخاص بك أخلاقي وآمن، من الضروري تقييمه بناءً على مبادئ الذكاء الاصطناعي المسؤول من Microsoft. في Microsoft Foundry، تتيح لك تقييمات السلامة التحقق من مدى تعرض نموذجك لهجمات فك الحظر (jailbreak) وإمكانية توليده لمحتوى ضار، وهو ما يتماشى مباشرة مع هذه المبادئ.

![Safaty evaluation.](../../../../../../translated_images/ar/safety-evaluation.083586ec88dfa950.webp)

*مصدر الصورة: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### مبادئ الذكاء الاصطناعي المسؤول من Microsoft

قبل بدء الخطوات التقنية، من الضروري فهم مبادئ الذكاء الاصطناعي المسؤول من Microsoft، وهو إطار أخلاقي مصمم لتوجيه التطوير المسؤول، والنشر، وتشغيل أنظمة الذكاء الاصطناعي. توجه هذه المبادئ التصميم المسؤول والتطوير والنشر لأنظمة الذكاء الاصطناعي، لضمان بناء تقنيات الذكاء الاصطناعي بطريقة عادلة وشفافة وشاملة. تشكل هذه المبادئ الأساس لتقييم سلامة نماذج الذكاء الاصطناعي.

تشمل مبادئ الذكاء الاصطناعي المسؤول من Microsoft ما يلي:

- **العدالة والشمول**: يجب على أنظمة الذكاء الاصطناعي معاملة الجميع بعدل وتجنب التأثير على مجموعات مشابهة من الأشخاص بطرق مختلفة. على سبيل المثال، عندما تقدم أنظمة الذكاء الاصطناعي إرشادات حول العلاج الطبي أو طلبات القروض أو التوظيف، يجب أن تقدم نفس التوصيات للجميع الذين لديهم أعراض أو ظروف مالية أو مؤهلات مهنية مماثلة.

- **الموثوقية والسلامة**: لبناء الثقة، من الضروري أن تعمل أنظمة الذكاء الاصطناعي بشكل موثوق وآمن ومتسق. يجب أن تكون هذه الأنظمة قادرة على العمل كما صُممت في الأصل، والاستجابة بأمان للحالات غير المتوقعة، ومقاومة التلاعب الضار. تعكس كيفية تصرفها وتنوع الحالات التي يمكنها التعامل معها مدى المواقف والظروف التي توقعها المطورون أثناء التصميم والاختبار.

- **الشفافية**: عندما تساعد أنظمة الذكاء الاصطناعي في اتخاذ قرارات تؤثر تأثيرًا كبيرًا على حياة الأشخاص، من الضروري أن يفهم الناس كيف تم اتخاذ تلك القرارات. على سبيل المثال، قد يستخدم بنك نظام ذكاء اصطناعي لتحديد ما إذا كان الشخص جديرًا بالائتمان. قد تستخدم شركة نظام ذكاء اصطناعي لتحديد أكثر المرشحين مؤهلاً للتوظيف.

- **الخصوصية والأمن**: مع تزايد انتشار الذكاء الاصطناعي، يصبح حماية الخصوصية وتأمين المعلومات الشخصية والتجارية أكثر أهمية وتعقيدًا. تتطلب الخصوصية وأمن البيانات اهتمامًا وثيقًا مع الذكاء الاصطناعي لأن الوصول إلى البيانات ضروري لأنظمة الذكاء الاصطناعي لتقديم تنبؤات وقرارات دقيقة ومستنيرة حول الأشخاص.

- **المساءلة**: يجب أن يكون الأشخاص الذين يصممون وينشرون أنظمة الذكاء الاصطناعي مسؤولين عن كيفية عمل أنظمتهم. ينبغي على المؤسسات الاستعانة بالمعايير الصناعية لتطوير قواعد للمساءلة. يمكن لهذه القواعد ضمان ألا تكون أنظمة الذكاء الاصطناعي السلطة النهائية في أي قرار يؤثر على حياة الناس. كما يمكنها ضمان احتفاظ البشر بالسيطرة الفعالة على أنظمة الذكاء الاصطناعي التي تتمتع بدرجة عالية من الاستقلالية.

![Fill hub.](../../../../../../translated_images/ar/responsibleai2.c07ef430113fad8c.webp)

*مصدر الصورة: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> لتعلم المزيد عن مبادئ الذكاء الاصطناعي المسؤول من Microsoft، قم بزيارة [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### مؤشرات السلامة

في هذا البرنامج التعليمي، ستقوم بتقييم سلامة نموذج Phi-3 المحسن باستخدام مؤشرات السلامة في Microsoft Foundry. تساعدك هذه المؤشرات على تقييم قدرة النموذج على توليد محتوى ضار ومدى تعرضه لهجمات فك الحظر. تشمل مؤشرات السلامة ما يلي:

- **المحتوى المتعلق بإيذاء الذات**: يقيم ما إذا كان للنموذج ميل لإنتاج محتوى متعلق بإيذاء الذات.
- **المحتوى الكريه والغير عادل**: يقيم ما إذا كان للنموذج ميل لإنتاج محتوى كريه أو غير عادل.
- **المحتوى العنيف**: يقيم ما إذا كان للنموذج ميل لإنتاج محتوى عنيف.
- **المحتوى الجنسي**: يقيم ما إذا كان للنموذج ميل لإنتاج محتوى جنسي غير مناسب.

يضمن تقييم هذه الجوانب ألا ينتج نموذج الذكاء الاصطناعي محتوى ضارًا أو مسيئًا، متماشيًا مع قيم المجتمع والمعايير التنظيمية.

![Evaluate based on safety.](../../../../../../translated_images/ar/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### مقدمة لتقييم الأداء

لضمان أن نموذج الذكاء الاصطناعي الخاص بك يعمل كما هو متوقع، من المهم تقييم أدائه بناءً على مؤشرات الأداء. في Microsoft Foundry، تسمح تقييمات الأداء لك بتقييم فاعلية نموذجك في إنتاج استجابات دقيقة وذات صلة ومتسقة.

![Safaty evaluation.](../../../../../../translated_images/ar/performance-evaluation.48b3e7e01a098740.webp)

*مصدر الصورة: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### مؤشرات الأداء

في هذا البرنامج التعليمي، ستقوم بتقييم أداء نموذج Phi-3 / Phi-3.5 المحسن باستخدام مؤشرات الأداء في Microsoft Foundry. تساعدك هذه المؤشرات على تقييم فعالية النموذج في إنتاج استجابات دقيقة وذات صلة ومتسقة. تشمل مؤشرات الأداء ما يلي:

- **التوثيق**: تقييم مدى توافق الإجابات المولدة مع المعلومات من المصدر المدخل.
- **الملاءمة**: تقييم مدى صلة الاستجابات المُنتَجة بالأسئلة المطروحة.
- **الاتساق**: تقييم مدى سلاسة تدفق النص المولد، قراءته بشكل طبيعي، وتشابهها مع لغة شبيهة بالبشر.
- **الطلاقة**: تقييم مهارة اللغة في النص المنتج.
- **التشابه مع GPT**: مقارنة الاستجابة المولدة مع الحقيقة الأرضية للتشابه.
- **معدل F1**: حساب نسبة الكلمات المشتركة بين الاستجابة المولدة وبيانات المصدر.

تساعدك هذه المؤشرات على تقييم فاعلية النموذج في إنتاج استجابات دقيقة وذات صلة ومتسقة.

![Evaluate based on performance.](../../../../../../translated_images/ar/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **السيناريو 2: تقييم نموذج Phi-3 / Phi-3.5 في Microsoft Foundry**

### قبل أن تبدأ

هذا البرنامج التعليمي هو متابعة للتدوينات السابقة، "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" و "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." في هذه المشاركات، استعرضنا عملية تحسين نموذج Phi-3 / Phi-3.5 في Microsoft Foundry ودمجه مع Prompt flow.

في هذا البرنامج التعليمي، ستقوم بنشر نموذج Azure OpenAI كمقيم في Microsoft Foundry واستخدامه لتقييم نموذج Phi-3 / Phi-3.5 المحسن الخاص بك.

قبل بدء هذا البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية، كما وُصفت في البرامج التعليمية السابقة:

1. مجموعة بيانات مُعدة لتقييم نموذج Phi-3 / Phi-3.5 المحسن.
1. نموذج Phi-3 / Phi-3.5 تم تحسينه ونشره في Azure Machine Learning.
1. Prompt flow مدمج مع نموذج Phi-3 / Phi-3.5 المحسن الخاص بك في Microsoft Foundry.

> [!NOTE]
> ستستخدم ملف *test_data.jsonl* الموجود في مجلد البيانات من مجموعة البيانات **ULTRACHAT_200k** التي تم تنزيلها في التدوينات السابقة، كمجموعة بيانات لتقييم نموذج Phi-3 / Phi-3.5 المحسن.

#### دمج نموذج Phi-3 / Phi-3.5 المخصص مع Prompt flow في Microsoft Foundry (نهج الكود أولاً)

> [!NOTE]
> إذا اتبعت النهج منخفض الكود الموضح في "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)"، يمكنك تخطي هذا التمرين والمتابعة إلى التمرين التالي.
> ومع ذلك، إذا اتبعت نهج الكود أولاً الموضح في "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" لتحسين ونشر نموذج Phi-3 / Phi-3.5 الخاص بك، فإن عملية ربط نموذجك بـ Prompt flow تختلف قليلًا. ستتعلم هذه العملية في هذا التمرين.

للمتابعة، تحتاج إلى دمج نموذج Phi-3 / Phi-3.5 المحسن الخاص بك في Prompt flow في Microsoft Foundry.

#### إنشاء Microsoft Foundry Hub

يجب عليك إنشاء Hub قبل إنشاء المشروع. يعمل الـ Hub كمجموعة موارد، مما يسمح لك بتنظيم وإدارة مشاريع متعددة داخل Microsoft Foundry.
1. سجّل الدخول إلى [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. اختر **All hubs** من تبويب الجانب الأيسر.

1. اختر **+ New hub** من قائمة التنقل.

    ![Create hub.](../../../../../../translated_images/ar/create-hub.5be78fb1e21ffbf1.webp)

1. نفّذ المهام التالية:

    - أدخل **Hub name**. يجب أن تكون قيمة فريدة.
    - اختر **Subscription** الخاص بك في Azure.
    - اختر **Resource group** الذي تريد استخدامه (أنشئ مجموعة جديدة إذا لزم الأمر).
    - اختر **Location** التي ترغب في استخدامها.
    - اختر **Connect Azure AI Services** التي تريد استخدامها (أنشئ واحدة جديدة إذا لزم الأمر).
    - اختر **Connect Azure AI Search** لتحديد **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/ar/fill-hub.baaa108495c71e34.webp)

1. اختر **Next**.

#### إنشاء مشروع في Microsoft Foundry

1. في Hub الذي أنشأته، اختر **All projects** من تبويب الجانب الأيسر.

1. اختر **+ New project** من قائمة التنقل.

    ![Select new project.](../../../../../../translated_images/ar/select-new-project.cd31c0404088d7a3.webp)

1. أدخل **Project name**. يجب أن تكون قيمة فريدة.

    ![Create project.](../../../../../../translated_images/ar/create-project.ca3b71298b90e420.webp)

1. اختر **Create a project**.

#### إضافة اتصال مخصص لنموذج Phi-3 / Phi-3.5 المعدل

لدمج نموذج Phi-3 / Phi-3.5 المخصص مع Prompt flow، تحتاج إلى حفظ نقطة النهاية المفتاحية للنموذج في اتصال مخصص. يضمن هذا الإعداد الوصول إلى نموذج Phi-3 / Phi-3.5 المخصص الخاص بك في Prompt flow.

#### إعداد مفتاح API وعنوان URI لنموذج Phi-3 / Phi-3.5 المعدل

1. زر [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. انتقل إلى مساحة عمل Azure Machine Learning التي أنشأتها.

1. اختر **Endpoints** من تبويب الجانب الأيسر.

    ![Select endpoints.](../../../../../../translated_images/ar/select-endpoints.ee7387ecd68bd18d.webp)

1. اختر نقطة النهاية التي أنشأتها.

    ![Select endpoints.](../../../../../../translated_images/ar/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. اختر **Consume** من قائمة التنقل.

1. انسخ **REST endpoint** و **Primary key** الخاصة بك.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ar/copy-endpoint-key.0650c3786bd646ab.webp)

#### إضافة الاتصال المخصص

1. زر [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. انتقل إلى مشروع Microsoft Foundry الذي أنشأته.

1. في المشروع الذي أنشأته، اختر **Settings** من تبويب الجانب الأيسر.

1. اختر **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/ar/select-new-connection.fa0f35743758a74b.webp)

1. اختر **Custom keys** من قائمة التنقل.

    ![Select custom keys.](../../../../../../translated_images/ar/select-custom-keys.5a3c6b25580a9b67.webp)

1. نفّذ المهام التالية:

    - اختر **+ Add key value pairs**.
    - لأسم المفتاح، أدخل **endpoint** والصق نقطة النهاية التي نسختها من Azure ML Studio في حقل القيمة.
    - اختر **+ Add key value pairs** مرة أخرى.
    - لأسم المفتاح، أدخل **key** والصق المفتاح الذي نسخته من Azure ML Studio في حقل القيمة.
    - بعد إضافة المفاتيح، اختر **is secret** لمنع كشف المفتاح.

    ![Add connection.](../../../../../../translated_images/ar/add-connection.ac7f5faf8b10b0df.webp)

1. اختر **Add connection**.

#### إنشاء Prompt flow

لقد أضفت اتصالًا مخصصًا في Microsoft Foundry. الآن، دعنا ننشئ Prompt flow باستخدام الخطوات التالية. ثم، ستربط هذا الـ Prompt flow بالاتصال المخصص لاستخدام النموذج المعدل ضمن Prompt flow.

1. انتقل إلى مشروع Microsoft Foundry الذي أنشأته.

1. اختر **Prompt flow** من تبويب الجانب الأيسر.

1. اختر **+ Create** من قائمة التنقل.

    ![Select Promptflow.](../../../../../../translated_images/ar/select-promptflow.18ff2e61ab9173eb.webp)

1. اختر **Chat flow** من قائمة التنقل.

    ![Select chat flow.](../../../../../../translated_images/ar/select-flow-type.28375125ec9996d3.webp)

1. أدخل **Folder name** للاستخدام.

    ![Select chat flow.](../../../../../../translated_images/ar/enter-name.02ddf8fb840ad430.webp)

1. اختر **Create**.

#### إعداد Prompt flow للدردشة مع نموذج Phi-3 / Phi-3.5 المخصص

تحتاج إلى دمج نموذج Phi-3 / Phi-3.5 المعدل في Prompt flow. ومع ذلك، فإن Prompt flow الموجود غير مصمم لهذا الغرض. لذلك، يجب عليك إعادة تصميم Prompt flow لتمكين دمج النموذج المخصص.

1. في Prompt flow، قم بالمهام التالية لإعادة بناء التدفق الحالي:

    - اختر **Raw file mode**.
    - احذف كل الكود الموجود في ملف *flow.dag.yml*.
    - أضف الكود التالي إلى *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - اختر **Save**.

    ![Select raw file mode.](../../../../../../translated_images/ar/select-raw-file-mode.06c1eca581ce4f53.webp)

1. أضف الكود التالي إلى *integrate_with_promptflow.py* لاستخدام نموذج Phi-3 / Phi-3.5 المخصص في Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # إعداد تسجيل الدخول
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" هو اسم الاتصال المخصص، "endpoint"، "key" هي المفاتيح في الاتصال المخصص
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # تسجيل استجابة JSON الكاملة
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/ar/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> لمزيد من المعلومات التفصيلية حول استخدام Prompt flow في Microsoft Foundry، يمكنك الرجوع إلى [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. اختر **Chat input**، **Chat output** لتمكين الدردشة مع النموذج الخاص بك.

    ![Select Input Output.](../../../../../../translated_images/ar/select-input-output.c187fc58f25fbfc3.webp)

1. الآن أنت جاهز للدردشة مع نموذج Phi-3 / Phi-3.5 المخصص الخاص بك. في التمرين التالي، ستتعلم كيفية بدء Prompt flow واستخدامه للدردشة مع النموذج المعدل.

> [!NOTE]
>
> يجب أن يبدو التدفق المعاد بناؤه كالصورة أدناه:
>
> ![Flow example](../../../../../../translated_images/ar/graph-example.82fd1bcdd3fc545b.webp)
>

#### بدء Prompt flow

1. اختر **Start compute sessions** لبدء Prompt flow.

    ![Start compute session.](../../../../../../translated_images/ar/start-compute-session.9acd8cbbd2c43df1.webp)

1. اختر **Validate and parse input** لتحديث المعايير.

    ![Validate input.](../../../../../../translated_images/ar/validate-input.c1adb9543c6495be.webp)

1. اختر **Value** الخاصة بالاتصال إلى الاتصال المخصص الذي أنشأته. مثلاً، *connection*.

    ![Connection.](../../../../../../translated_images/ar/select-connection.1f2b59222bcaafef.webp)

#### الدردشة مع نموذج Phi-3 / Phi-3.5 المخصص الخاص بك

1. اختر **Chat**.

    ![Select chat.](../../../../../../translated_images/ar/select-chat.0406bd9687d0c49d.webp)

1. إليك مثال على النتائج: الآن يمكنك الدردشة مع نموذج Phi-3 / Phi-3.5 المخصص الخاص بك. يُنصح بطرح أسئلة بناءً على البيانات المستخدمة في التعديل الدقيق.

    ![Chat with prompt flow.](../../../../../../translated_images/ar/chat-with-promptflow.1cf8cea112359ada.webp)

### نشر Azure OpenAI لتقييم نموذج Phi-3 / Phi-3.5

لتقييم نموذج Phi-3 / Phi-3.5 في Microsoft Foundry، تحتاج إلى نشر نموذج Azure OpenAI. سيتم استخدام هذا النموذج لتقييم أداء نموذج Phi-3 / Phi-3.5.

#### نشر Azure OpenAI

1. سجّل الدخول إلى [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. انتقل إلى مشروع Microsoft Foundry الذي أنشأته.

    ![Select Project.](../../../../../../translated_images/ar/select-project-created.5221e0e403e2c9d6.webp)

1. في المشروع الذي أنشأته، اختر **Deployments** من تبويب الجانب الأيسر.

1. اختر **+ Deploy model** من قائمة التنقل.

1. اختر **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/ar/deploy-openai-model.95d812346b25834b.webp)

1. اختر نموذج Azure OpenAI الذي ترغب في استخدامه. مثلاً، **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/ar/select-openai-model.959496d7e311546d.webp)

1. اختر **Confirm**.

### تقييم نموذج Phi-3 / Phi-3.5 المعدل باستخدام تقييم Prompt flow في Microsoft Foundry

### بدء تقييم جديد

1. زر [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. انتقل إلى مشروع Microsoft Foundry الذي أنشأته.

    ![Select Project.](../../../../../../translated_images/ar/select-project-created.5221e0e403e2c9d6.webp)

1. في المشروع الذي أنشأته، اختر **Evaluation** من تبويب الجانب الأيسر.

1. اختر **+ New evaluation** من قائمة التنقل.

    ![Select evaluation.](../../../../../../translated_images/ar/select-evaluation.2846ad7aaaca7f4f.webp)

1. اختر تقييم **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/ar/promptflow-evaluation.cb9758cc19b4760f.webp)

1. نفّذ المهام التالية:

    - أدخل اسم التقييم. يجب أن يكون فريدًا.
    - اختر **Question and answer without context** كنوع المهمة. لأن مجموعة البيانات **UlTRACHAT_200k** المستخدمة في هذا الدليل لا تحتوي على سياق.
    - اختر الـ Prompt flow الذي تريد تقييمه.

    ![Prompt flow evaluation.](../../../../../../translated_images/ar/evaluation-setting1.4aa08259ff7a536e.webp)

1. اختر **Next**.

1. نفّذ المهام التالية:

    - اختر **Add your dataset** لتحميل مجموعة البيانات. على سبيل المثال، يمكنك تحميل ملف مجموعة البيانات الاختبارية، مثل *test_data.json1*، الذي يتضمن عند تحميل مجموعة بيانات **ULTRACHAT_200k**.
    - اختر العمود المناسب في مجموعة البيانات الذي يتطابق مع مجموعة البيانات لديك. مثلاً، إذا كنت تستخدم مجموعة بيانات **ULTRACHAT_200k**، اختر **${data.prompt}** كعمود مجموعة البيانات.

    ![Prompt flow evaluation.](../../../../../../translated_images/ar/evaluation-setting2.07036831ba58d64e.webp)

1. اختر **Next**.

1. نفّذ المهام التالية لتكوين مقاييس الأداء والجودة:

    - اختر مقاييس الأداء والجودة التي تريد استخدامها.
    - اختر نموذج Azure OpenAI الذي أنشأته للتقييم. مثلاً، اختر **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/ar/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. نفّذ المهام التالية لتكوين مقاييس المخاطر والسلامة:

    - اختر مقاييس المخاطر والسلامة التي تريد استخدامها.
    - اختر العتبة لحساب معدل العيوب الذي تريد استخدامه. مثلاً، اختر **Medium**.
    - بالنسبة لـ **question**، اختر **Data source** إلى **{$data.prompt}**.
    - بالنسبة لـ **answer**، اختر **Data source** إلى **{$run.outputs.answer}**.
    - بالنسبة لـ **ground_truth**، اختر **Data source** إلى **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/ar/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. اختر **Next**.

1. اختر **Submit** لبدء التقييم.

1. سيستغرق التقييم بعض الوقت لإكماله. يمكنك متابعة التقدم في تبويب **Evaluation**.

### مراجعة نتائج التقييم

> [!NOTE]
> النتائج المعروضة أدناه تهدف إلى توضيح عملية التقييم. في هذا الدليل، استخدمنا نموذجًا معدلًا على مجموعة بيانات صغيرة نسبيًا، مما قد يؤدي إلى نتائج أقل من المثلى. قد تختلف النتائج الفعلية بشكل كبير اعتمادًا على حجم وجودة وتنوع مجموعة البيانات المستخدمة، بالإضافة إلى التكوين المحدد للنموذج.

بمجرد الانتهاء من التقييم، يمكنك مراجعة النتائج لكل من مقاييس الأداء والسلامة.
1. مقاييس الأداء والجودة:

    - تقييم فعالية النموذج في توليد استجابات متماسكة وطليقة وذات صلة.

    ![نتيجة التقييم.](../../../../../../translated_images/ar/evaluation-result-gpu.85f48b42dfb74254.webp)

1. مقاييس المخاطر والسلامة:

    - ضمان أن مخرجات النموذج آمنة وتتوافق مع مبادئ الذكاء الاصطناعي المسؤول، مع تجنب أي محتوى ضار أو مسيء.

    ![نتيجة التقييم.](../../../../../../translated_images/ar/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. يمكنك التمرير لأسفل لعرض **نتيجة المقاييس التفصيلية**.

    ![نتيجة التقييم.](../../../../../../translated_images/ar/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. من خلال تقييم نموذج Phi-3 / Phi-3.5 المخصص مقابل كل من مقاييس الأداء والسلامة، يمكنك التأكد من أن النموذج ليس فقط فعّالاً، ولكن أيضاً يلتزم بممارسات الذكاء الاصطناعي المسؤول، مما يجعله جاهزًا للنشر في العالم الحقيقي.

## تهانينا!

### لقد أكملت هذا الدرس

لقد قمت بنجاح بتقييم نموذج Phi-3 المحسن والمتكامل مع Prompt flow في Microsoft Foundry. هذه خطوة مهمة لضمان أن نماذج الذكاء الاصطناعي الخاصة بك لا تؤدي بشكل جيد فقط، بل أيضاً تلتزم بمبادئ الذكاء الاصطناعي المسؤول من Microsoft لمساعدتك في بناء تطبيقات ذكاء اصطناعي موثوقة وجديرة بالثقة.

![الهندسة المعمارية.](../../../../../../translated_images/ar/architecture.10bec55250f5d6a4.webp)

## تنظيف موارد Azure

قم بتنظيف موارد Azure الخاصة بك لتجنب رسوم إضافية على حسابك. انتقل إلى بوابة Azure واحذف الموارد التالية:

- مورد Azure Machine learning.
- نقطة نهاية نموذج Azure Machine learning.
- مورد مشروع Microsoft Foundry.
- مورد Microsoft Foundry Prompt flow.

### الخطوات التالية

#### الوثائق

- [تقييم أنظمة الذكاء الاصطناعي باستخدام لوحة معلومات الذكاء الاصطناعي المسؤول](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [مقاييس التقييم والمراقبة للذكاء الاصطناعي التوليدي](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [توثيق Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [توثيق Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### محتوى التدريب

- [مقدمة إلى نهج الذكاء الاصطناعي المسؤول من Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [مقدمة إلى Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### المرجع

- [ما هو الذكاء الاصطناعي المسؤول؟](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [الإعلان عن أدوات جديدة في Azure AI لمساعدتك في بناء تطبيقات ذكاء اصطناعي توليدية أكثر أمانًا وجديرة بالثقة](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [تقييم تطبيقات الذكاء الاصطناعي التوليدية](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق به. للمعلومات الحرجة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->