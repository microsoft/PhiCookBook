<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:26:39+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "ur"
}
-->
# MLflow

[MLflow](https://mlflow.org/) ایک اوپن سورس پلیٹ فارم ہے جو مشین لرننگ کے پورے لائف سائیکل کو منظم کرنے کے لیے بنایا گیا ہے۔

![MLFlow](../../../../../../translated_images/ur/MlFlowmlops.ed16f47809d74d9a.png)

MLFlow مشین لرننگ کے لائف سائیکل کو منظم کرنے کے لیے استعمال ہوتا ہے، جس میں تجربات، دوبارہ قابلِ تکرار ہونا، تعیناتی اور ایک مرکزی ماڈل رجسٹری شامل ہے۔ MLflow اس وقت چار اجزاء پیش کرتا ہے۔

- **MLflow Tracking:** تجربات، کوڈ، ڈیٹا کنفیگریشن اور نتائج کو ریکارڈ اور تلاش کریں۔
- **MLflow Projects:** ڈیٹا سائنس کے کوڈ کو اس طرح پیکج کریں کہ اسے کسی بھی پلیٹ فارم پر دوبارہ چلایا جا سکے۔
- **Mlflow Models:** مشین لرننگ ماڈلز کو مختلف سروسنگ ماحول میں تعینات کریں۔
- **Model Registry:** ماڈلز کو ایک مرکزی ذخیرے میں محفوظ، تشریح اور منظم کریں۔

یہ تجربات کو ٹریک کرنے، کوڈ کو دوبارہ چلانے کے قابل پیکج کرنے، اور ماڈلز کو شیئر اور تعینات کرنے کی صلاحیتیں فراہم کرتا ہے۔ MLFlow کو Databricks میں شامل کیا گیا ہے اور یہ مختلف ML لائبریریز کی حمایت کرتا ہے، اس لیے یہ لائبریری سے آزاد ہے۔ اسے کسی بھی مشین لرننگ لائبریری اور کسی بھی پروگرامنگ زبان کے ساتھ استعمال کیا جا سکتا ہے کیونکہ یہ سہولت کے لیے REST API اور CLI فراہم کرتا ہے۔

![MLFlow](../../../../../../translated_images/ur/MLflow2.5a22eb718f6311d1.png)

MLFlow کی اہم خصوصیات میں شامل ہیں:

- **Experiment Tracking:** پیرامیٹرز اور نتائج کو ریکارڈ اور موازنہ کریں۔
- **Model Management:** ماڈلز کو مختلف سروسنگ اور انفرنس پلیٹ فارمز پر تعینات کریں۔
- **Model Registry:** MLflow ماڈلز کے لائف سائیکل کو مشترکہ طور پر منظم کریں، جس میں ورژننگ اور تشریحات شامل ہیں۔
- **Projects:** ML کوڈ کو شیئرنگ یا پروڈکشن کے استعمال کے لیے پیکج کریں۔

MLFlow MLOps لوپ کی بھی حمایت کرتا ہے، جس میں ڈیٹا کی تیاری، ماڈلز کی رجسٹریشن اور انتظام، ماڈلز کو چلانے کے لیے پیکجنگ، سروسز کی تعیناتی، اور ماڈلز کی نگرانی شامل ہے۔ اس کا مقصد پروٹوٹائپ سے پروڈکشن ورک فلو تک کے عمل کو آسان بنانا ہے، خاص طور پر کلاؤڈ اور ایج ماحول میں۔

## E2E منظر نامہ - ایک ریپر بنانا اور Phi-3 کو MLFlow ماڈل کے طور پر استعمال کرنا

اس E2E نمونے میں ہم دو مختلف طریقے دکھائیں گے جن سے Phi-3 چھوٹے زبان کے ماڈل (SLM) کے گرد ایک ریپر بنایا جا سکتا ہے اور پھر اسے MLFlow ماڈل کے طور پر مقامی یا کلاؤڈ میں، مثلاً Azure Machine Learning ورک اسپیس میں چلایا جا سکتا ہے۔

![MLFlow](../../../../../../translated_images/ur/MlFlow1.fd745e47dbd3fecf.png)

| پروجیکٹ | تفصیل | مقام |
| ------------ | ----------- | -------- |
| Transformer Pipeline | اگر آپ MLFlow کے تجرباتی transformers ورژن کے ساتھ HuggingFace ماڈل استعمال کرنا چاہتے ہیں تو Transformer Pipeline ریپر بنانے کا سب سے آسان طریقہ ہے۔ | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | تحریر کے وقت، transformer pipeline نے ONNX فارمیٹ میں HuggingFace ماڈلز کے لیے MLFlow ریپر جنریشن کی حمایت نہیں کی، چاہے تجرباتی optimum Python پیکج استعمال کیا جائے۔ ایسے معاملات کے لیے، آپ MLFlow ماڈل کے لیے اپنا کسٹم Python ریپر بنا سکتے ہیں۔ | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## پروجیکٹ: Transformer Pipeline

1. آپ کو MLFlow اور HuggingFace کے متعلقہ Python پیکجز کی ضرورت ہوگی:

    ``` Python
    import mlflow
    import transformers
    ```

2. اگلا قدم transformer pipeline شروع کرنا ہے، جس میں HuggingFace رجسٹری میں موجود ہدف Phi-3 ماڈل کی طرف اشارہ کیا جائے۔ جیسا کہ _Phi-3-mini-4k-instruct_ کے ماڈل کارڈ سے ظاہر ہے، اس کا کام "Text Generation" قسم کا ہے:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. اب آپ اپنے Phi-3 ماڈل کی transformer pipeline کو MLFlow فارمیٹ میں محفوظ کر سکتے ہیں اور اضافی تفصیلات فراہم کر سکتے ہیں جیسے ہدف آرٹیفیکٹس کا راستہ، مخصوص ماڈل کنفیگریشن سیٹنگز، اور انفرنس API کی قسم:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## پروجیکٹ: Custom Python Wrapper

1. یہاں ہم Microsoft کے [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) کو ONNX ماڈل کی انفرنس اور ٹوکنز کی انکوڈنگ/ڈیکوڈنگ کے لیے استعمال کر سکتے ہیں۔ آپ کو اپنے ہدف کمپیوٹ کے لیے _onnxruntime_genai_ پیکج منتخب کرنا ہوگا، نیچے دیے گئے مثال میں CPU کو ہدف بنایا گیا ہے:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. ہماری کسٹم کلاس دو طریقے نافذ کرتی ہے: _load_context()_ جو Phi-3 Mini 4K Instruct کے **ONNX ماڈل**، **جنریٹر پیرامیٹرز** اور **ٹوکنازر** کو شروع کرتا ہے؛ اور _predict()_ جو دیے گئے پرامپٹ کے لیے آؤٹ پٹ ٹوکنز تیار کرتا ہے:

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

1. اب آپ _mlflow.pyfunc.log_model()_ فنکشن استعمال کر کے Phi-3 ماڈل کے لیے ایک کسٹم Python ریپر (pickle فارمیٹ میں) بنا سکتے ہیں، جس کے ساتھ اصل ONNX ماڈل اور ضروری انحصار بھی شامل ہوں:

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

## جنریٹ کیے گئے MLFlow ماڈلز کے دستخط

1. اوپر Transformer Pipeline پروجیکٹ کے مرحلہ 3 میں، ہم نے MLFlow ماڈل کے کام کو "_llm/v1/chat_" مقرر کیا۔ ایسی ہدایت ایک ماڈل API ریپر بناتی ہے جو OpenAI کے Chat API کے ساتھ مطابقت رکھتا ہے، جیسا کہ نیچے دکھایا گیا ہے:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. نتیجتاً، آپ اپنا پرامپٹ درج ذیل فارمیٹ میں بھیج سکتے ہیں:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. پھر، OpenAI API کے مطابق پوسٹ پروسیسنگ استعمال کریں، مثلاً _response[0][‘choices’][0][‘message’][‘content’]_، تاکہ آپ کا آؤٹ پٹ کچھ اس طرح خوبصورت ہو جائے:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. اوپر Custom Python Wrapper پروجیکٹ کے مرحلہ 3 میں، ہم MLFlow پیکج کو ماڈل کے دستخط ایک دیے گئے ان پٹ مثال سے بنانے دیتے ہیں۔ ہمارے MLFlow ریپر کے دستخط کچھ اس طرح ہوں گے:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. لہٰذا، ہمارے پرامپٹ میں "prompt" ڈکشنری کی کلید شامل ہونی چاہیے، کچھ اس طرح:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. ماڈل کا آؤٹ پٹ پھر سٹرنگ فارمیٹ میں فراہم کیا جائے گا:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔