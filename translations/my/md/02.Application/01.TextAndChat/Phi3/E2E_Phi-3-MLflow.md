<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:37:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "my"
}
-->
# MLflow

[MLflow](https://mlflow.org/) သည် စက်မှုသင်ယူမှု လုပ်ငန်းစဉ်အပြီးအစီးကို စီမံခန့်ခွဲရန် ရည်ရွယ်ထားသော အဖွင့်အရင်းအမြစ် ပလက်ဖောင်းတစ်ခုဖြစ်သည်။

![MLFlow](../../../../../../translated_images/my/MlFlowmlops.ed16f47809d74d9a.png)

MLFlow ကို စက်မှုသင်ယူမှု လုပ်ငန်းစဉ်များကို စီမံခန့်ခွဲရန် အသုံးပြုသည်၊ ၎င်းတွင် စမ်းသပ်မှု၊ ထပ်မံထုတ်လုပ်နိုင်မှု၊ တပ်ဆင်ခြင်းနှင့် ဗဟိုမော်ဒယ်မှတ်တမ်းစာရင်း စသည့် အစိတ်အပိုင်းများ ပါဝင်သည်။ MLflow သည် လက်ရှိတွင် အစိတ်အပိုင်းလေးခု ပါဝင်သည်။

- **MLflow Tracking:** စမ်းသပ်မှုများ၊ ကုဒ်၊ ဒေတာ ဖွဲ့စည်းမှုနှင့် ရလဒ်များကို မှတ်တမ်းတင်ပြီး ရှာဖွေစစ်ဆေးနိုင်သည်။
- **MLflow Projects:** ဒေတာသိပ္ပံကုဒ်ကို မည်သည့်ပလက်ဖောင်းတွင်မဆို ထပ်မံပြန်လည်ပြုလုပ်နိုင်သော ပုံစံဖြင့် ထုပ်ပိုးသည်။
- **Mlflow Models:** စက်မှုသင်ယူမှု မော်ဒယ်များကို မတူညီသော ဝန်ဆောင်မှု ပတ်ဝန်းကျင်များတွင် တပ်ဆင်နိုင်သည်။
- **Model Registry:** မော်ဒယ်များကို ဗဟိုသိုလှောင်ရာတွင် သိမ်းဆည်း၊ မှတ်ချက်ပေးခြင်းနှင့် စီမံခန့်ခွဲခြင်း ပြုလုပ်သည်။

၎င်းတွင် စမ်းသပ်မှုများကို မှတ်တမ်းတင်ခြင်း၊ ကုဒ်များကို ထပ်မံထုတ်လုပ်နိုင်သော အခြေအနေသို့ ထုပ်ပိုးခြင်းနှင့် မော်ဒယ်များကို မျှဝေခြင်းနှင့် တပ်ဆင်ခြင်း စသည့် လုပ်ဆောင်ချက်များ ပါဝင်သည်။ MLFlow ကို Databricks နှင့် ပေါင်းစပ်အသုံးပြုနိုင်ပြီး စက်မှုသင်ယူမှု စာကြည့်တိုက်အမျိုးမျိုးကို ထောက်ပံ့ပေးသောကြောင့် စာကြည့်တိုက်မရွေး အသုံးပြုနိုင်သည်။ မည်သည့် စက်မှုသင်ယူမှု စာကြည့်တိုက်နှင့် မည်သည့် ပရိုဂရမ်မင်းဘာသာစကားဖြင့်မဆို အသုံးပြုနိုင်ပြီး အဆင်ပြေစေရန် REST API နှင့် CLI ကို ပံ့ပိုးပေးသည်။

![MLFlow](../../../../../../translated_images/my/MLflow2.5a22eb718f6311d1.png)

MLFlow ၏ အဓိက လက္ခဏာများမှာ -

- **စမ်းသပ်မှု မှတ်တမ်းတင်ခြင်း:** ပါရာမီတာများနှင့် ရလဒ်များကို မှတ်တမ်းတင်ပြီး နှိုင်းယှဉ်နိုင်သည်။
- **မော်ဒယ် စီမံခန့်ခွဲမှု:** မော်ဒယ်များကို မတူညီသော ဝန်ဆောင်မှုနှင့် ခန့်မှန်းခြေ ပလက်ဖောင်းများတွင် တပ်ဆင်နိုင်သည်။
- **မော်ဒယ် မှတ်တမ်းစာရင်း:** MLflow မော်ဒယ်များ၏ အသက်တာကာလကို ပူးပေါင်းစီမံခန့်ခွဲနိုင်ပြီး ဗားရှင်းနှင့် မှတ်ချက်များ ထည့်သွင်းနိုင်သည်။
- **Projects:** ML ကုဒ်များကို မျှဝေခြင်း သို့မဟုတ် ထုတ်လုပ်မှုအတွက် ထုပ်ပိုးသည်။

MLFlow သည် MLOps လုပ်ငန်းစဉ်ကိုလည်း ထောက်ပံ့ပေးပြီး ဒေတာပြင်ဆင်ခြင်း၊ မော်ဒယ်မှတ်ပုံတင်ခြင်းနှင့် စီမံခန့်ခွဲခြင်း၊ မော်ဒယ်များကို အကောင်အထည်ဖော်ရန် ထုပ်ပိုးခြင်း၊ ဝန်ဆောင်မှုတပ်ဆင်ခြင်းနှင့် မော်ဒယ်များကို စောင့်ကြည့်ခြင်းတို့ ပါဝင်သည်။ ၎င်းသည် prototype မှ ထုတ်လုပ်မှုလုပ်ငန်းစဉ်သို့ ရွေ့လျားရာတွင် အထူးသဖြင့် cloud နှင့် edge ပတ်ဝန်းကျင်များတွင် လုပ်ငန်းစဉ်ကို လွယ်ကူစေရန် ရည်ရွယ်သည်။

## E2E အခြေအနေ - Wrapper တစ်ခု တည်ဆောက်ခြင်းနှင့် Phi-3 ကို MLFlow မော်ဒယ်အဖြစ် အသုံးပြုခြင်း

ဤ E2E နမူနာတွင် Phi-3 သေးငယ်သော ဘာသာစကားမော်ဒယ် (SLM) အတွက် wrapper နှစ်မျိုးကို တည်ဆောက်ပြီး MLFlow မော်ဒယ်အဖြစ် ဒေသတွင်း သို့မဟုတ် cloud တွင် (ဥပမာ Azure Machine Learning workspace တွင်) ပြေးဆွဲခြင်းကို ပြသမည်ဖြစ်သည်။

![MLFlow](../../../../../../translated_images/my/MlFlow1.fd745e47dbd3fecf.png)

| Project | ဖော်ပြချက် | တည်နေရာ |
| ------------ | ----------- | -------- |
| Transformer Pipeline | HuggingFace မော်ဒယ်ကို MLFlow ၏ စမ်းသပ်မှု transformers flavour ဖြင့် အသုံးပြုလိုပါက wrapper တည်ဆောက်ရန် အလွယ်ဆုံး နည်းလမ်းဖြစ်သည်။ | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | ယခုအချိန်တွင် transformer pipeline သည် ONNX ပုံစံရှိ HuggingFace မော်ဒယ်များအတွက် MLFlow wrapper ဖန်တီးမှုကို experimental optimum Python package ဖြင့်ပါ မထောက်ပံ့သေးပါ။ ထိုကဲ့သို့သောအခြေအနေများအတွက် သင်၏ ကိုယ်ပိုင် Python wrapper ကို MLFlow မော်ဒယ်အတွက် တည်ဆောက်နိုင်သည်။ | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Project: Transformer Pipeline

1. MLFlow နှင့် HuggingFace မှ သက်ဆိုင်ရာ Python package များ လိုအပ်ပါမည်။

    ``` Python
    import mlflow
    import transformers
    ```

2. နောက်တစ်ဆင့်တွင် HuggingFace မှ Phi-3 မော်ဒယ်ကို ရည်ညွှန်း၍ transformer pipeline ကို စတင်ဖန်တီးရမည်။ _Phi-3-mini-4k-instruct_ ၏ မော်ဒယ်ကတ်မှ မြင်ရသလို ၎င်း၏ တာဝန်မှာ “စာသားဖန်တီးခြင်း” ဖြစ်သည်။

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. ယခု Phi-3 မော်ဒယ်၏ transformer pipeline ကို MLFlow ပုံစံဖြင့် သိမ်းဆည်းပြီး ရည်ညွှန်းထားသော artifacts လမ်းကြောင်း၊ မော်ဒယ် ဖွဲ့စည်းမှု အချက်အလက်များနှင့် inference API အမျိုးအစား စသည့် အသေးစိတ်များ ထည့်သွင်းနိုင်သည်။

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Project: Custom Python Wrapper

1. ONNX မော်ဒယ်၏ inference နှင့် token encoding/decoding အတွက် Microsoft ၏ [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) ကို အသုံးပြုနိုင်သည်။ သင်၏ ရည်ရွယ်ထားသော ကွန်ပျူတာအတွက် _onnxruntime_genai_ package ကို ရွေးချယ်ရမည်ဖြစ်ပြီး ဤနမူနာတွင် CPU ကို ရည်ညွှန်းထားသည်။

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. ကျွန်ုပ်တို့၏ ကိုယ်ပိုင် class သည် _load_context()_ နည်းလမ်းနှစ်ခုကို အကောင်အထည်ဖော်ထားပြီး၊ Phi-3 Mini 4K Instruct ၏ **ONNX မော်ဒယ်**, **generator parameters** နှင့် **tokenizer** ကို စတင်တင်သွင်းသည်။ _predict()_ သည် ပေးထားသော prompt အတွက် output token များ ဖန်တီးပေးသည်။

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

1. ယခု _mlflow.pyfunc.log_model()_ function ကို အသုံးပြု၍ Phi-3 မော်ဒယ်အတွက် ကိုယ်ပိုင် Python wrapper (pickle ပုံစံ) ကို မူရင်း ONNX မော်ဒယ်နှင့် လိုအပ်သော အားဖြည့်ပစ္စည်းများနှင့်အတူ ဖန်တီးနိုင်သည်။

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

## ဖန်တီးထားသော MLFlow မော်ဒယ်များ၏ Signature များ

1. အထက်ပါ Transformer Pipeline project ၏ အဆင့် ၃ တွင် MLFlow မော်ဒယ်၏ တာဝန်ကို “_llm/v1/chat_” ဟု သတ်မှတ်ထားသည်။ ဤညွှန်ကြားချက်သည် OpenAI ၏ Chat API နှင့် ကိုက်ညီသော မော်ဒယ် API wrapper ကို ဖန်တီးပေးသည်။

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. ထို့ကြောင့် သင်၏ prompt ကို အောက်ပါ ပုံစံဖြင့် တင်သွင်းနိုင်သည်။

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. ထို့နောက် OpenAI API ကိုက်ညီသော post-processing ကို အသုံးပြု၍ ဥပမာ _response[0][‘choices’][0][‘message’][‘content’]_ ကဲ့သို့ output ကို လှပစွာ ပြင်ဆင်နိုင်သည်။

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. အထက်ပါ Custom Python Wrapper project ၏ အဆင့် ၃ တွင် MLFlow package ကို အသုံးပြု၍ ပေးထားသော input နမူနာမှ မော်ဒယ်၏ signature ကို ဖန်တီးခွင့်ပြုထားသည်။ ကျွန်ုပ်တို့၏ MLFlow wrapper ၏ signature သည် အောက်ပါအတိုင်း ဖြစ်မည်။

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. ထို့ကြောင့် ကျွန်ုပ်တို့၏ prompt တွင် "prompt" ဆိုသော dictionary key ပါဝင်ရမည်၊ ဥပမာအတိုင်းဖြစ်သည်။

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. မော်ဒယ်၏ output ကို string ပုံစံဖြင့် ပြန်လည်ပေးအပ်မည်။

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မခံပါ။