<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-05-07T11:04:32+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "ar"
}
-->
# MLflow

[MLflow](https://mlflow.org/) هي منصة مفتوحة المصدر مصممة لإدارة دورة حياة تعلم الآلة من البداية إلى النهاية.

![MLFlow](../../../../../../translated_images/MlFlowmlops.ed16f47809d74d9ac0407bf43985ec022ad01f3d970083e465326951e43b2e01.ar.png)

يُستخدم MLFlow لإدارة دورة حياة تعلم الآلة، بما في ذلك التجارب، إعادة الإنتاج، النشر وسجل النماذج المركزي. تقدم MLflow حاليًا أربعة مكونات.

- **MLflow Tracking:** تسجيل واستعلام التجارب، الكود، تكوين البيانات والنتائج.
- **MLflow Projects:** تغليف كود علوم البيانات بصيغة تسمح بإعادة تنفيذها على أي منصة.
- **Mlflow Models:** نشر نماذج تعلم الآلة في بيئات تقديم متنوعة.
- **Model Registry:** تخزين، توضيح وإدارة النماذج في مستودع مركزي.

تشمل قدراتها تتبع التجارب، تغليف الكود في عمليات قابلة لإعادة الإنتاج، ومشاركة ونشر النماذج. تم دمج MLFlow في Databricks ويدعم مجموعة متنوعة من مكتبات تعلم الآلة، مما يجعله غير مرتبط بمكتبة معينة. يمكن استخدامه مع أي مكتبة تعلم آلة وأي لغة برمجة، حيث يوفر واجهة REST API وCLI لسهولة الاستخدام.

![MLFlow](../../../../../../translated_images/MLflow2.5a22eb718f6311d16f1a1952a047dc6b9e392649f1e0fc7bc3c3dcd65e3af07c.ar.png)

الميزات الرئيسية لـ MLFlow تشمل:

- **تتبع التجارب:** تسجيل ومقارنة المعلمات والنتائج.
- **إدارة النماذج:** نشر النماذج على منصات تقديم واستدلال مختلفة.
- **سجل النماذج:** إدارة دورة حياة نماذج MLflow بشكل تعاوني، بما في ذلك النسخ والتعليقات التوضيحية.
- **المشاريع:** تغليف كود تعلم الآلة للمشاركة أو الاستخدام في الإنتاج.

يدعم MLFlow أيضًا دورة MLOps، التي تشمل تحضير البيانات، تسجيل وإدارة النماذج، تغليف النماذج للتنفيذ، نشر الخدمات، ومراقبة النماذج. يهدف إلى تبسيط عملية الانتقال من النموذج الأولي إلى سير عمل الإنتاج، خاصة في بيئات السحابة والحافة.

## السيناريو من البداية للنهاية - بناء غلاف واستخدام Phi-3 كنموذج MLFlow

في هذا المثال من البداية للنهاية سنوضح طريقتين مختلفتين لبناء غلاف حول نموذج اللغة الصغير Phi-3 (SLM) ثم تشغيله كنموذج MLFlow سواء محليًا أو في السحابة، مثل مساحة عمل Azure Machine Learning.

![MLFlow](../../../../../../translated_images/MlFlow1.fd745e47dbd3fecfee254096d496cdf1cb3e1789184f9efcead9c2a96e5a979b.ar.png)

| المشروع | الوصف | الموقع |
| ------------ | ----------- | -------- |
| Transformer Pipeline | يُعتبر Transformer Pipeline الخيار الأسهل لبناء غلاف إذا كنت تريد استخدام نموذج HuggingFace مع نكهة المحولات التجريبية في MLFlow. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | حتى وقت كتابة هذا، لم يدعم Transformer Pipeline توليد غلاف MLFlow لنماذج HuggingFace بصيغة ONNX، حتى مع حزمة optimum التجريبية لـ Python. في مثل هذه الحالات، يمكنك بناء غلاف Python مخصص لنموذج MLFlow. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## المشروع: Transformer Pipeline

1. ستحتاج إلى الحزم المناسبة من Python لـ MLFlow وHuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. بعد ذلك، يجب أن تبدأ Transformer Pipeline بالإشارة إلى نموذج Phi-3 المستهدف في سجل HuggingFace. كما يظهر في بطاقة نموذج _Phi-3-mini-4k-instruct_، مهمته هي من نوع "توليد النص":

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. يمكنك الآن حفظ Transformer Pipeline الخاص بنموذج Phi-3 بصيغة MLFlow وتقديم تفاصيل إضافية مثل مسار الأرتيفاكت المستهدف، إعدادات تكوين النموذج المحددة ونوع واجهة برمجة التطبيقات للاستدلال:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## المشروع: Custom Python Wrapper

1. يمكننا هنا استخدام [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) من Microsoft لاستدلال نموذج ONNX وترميز/فك ترميز الرموز. عليك اختيار حزمة _onnxruntime_genai_ للحوسبة المستهدفة، مع المثال أدناه الذي يستهدف CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. تنفذ فئتنا المخصصة طريقتين: _load_context()_ لتهيئة **نموذج ONNX** لـ Phi-3 Mini 4K Instruct، **معلمات المولد** و**المجزئ**؛ و _predict()_ لتوليد رموز الإخراج للموجه المقدم:

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # Retrieving model from the artifacts
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # Defining the model
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # Defining the tokenizer
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # Retrieving prompt from the input
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # Generating the model's response
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

1. يمكنك الآن استخدام دالة _mlflow.pyfunc.log_model()_ لتوليد غلاف Python مخصص (بصيغة pickle) لنموذج Phi-3، مع نموذج ONNX الأصلي والاعتمادات المطلوبة:

    ``` Python
    model_info = mlflow.pyfunc.log_model(
        artifact_path = artifact_path,
        python_model = Phi3Model(),
        artifacts = {
            "phi3-mini-onnx": "cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4",
        },
        input_example = input_example,
        signature = infer_signature(input_example, ["Run"]),
        extra_pip_requirements = ["torch", "onnxruntime_genai", "numpy"],
    )
    ```

## توقيعات نماذج MLFlow المولدة

1. في الخطوة 3 من مشروع Transformer Pipeline أعلاه، قمنا بتعيين مهمة نموذج MLFlow إلى "_llm/v1/chat_". هذا التوجيه يولد غلاف API للنموذج، متوافق مع Chat API الخاص بـ OpenAI كما هو موضح أدناه:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. كنتيجة لذلك، يمكنك تقديم موجهك بالتنسيق التالي:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. ثم، استخدم المعالجة اللاحقة المتوافقة مع OpenAI API، مثل _response[0][‘choices’][0][‘message’][‘content’]_، لتحسين مخرجاتك لتبدو كالتالي:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. في الخطوة 3 من مشروع Custom Python Wrapper أعلاه، نسمح لحزمة MLFlow بتوليد توقيع النموذج من مثال إدخال معين. توقيع غلاف MLFlow الخاص بنا سيبدو هكذا:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. لذا، يجب أن يحتوي موجهنا على مفتاح قاموس "prompt"، مشابه لهذا:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. سيتم تقديم مخرجات النموذج بعد ذلك بصيغة نصية:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.