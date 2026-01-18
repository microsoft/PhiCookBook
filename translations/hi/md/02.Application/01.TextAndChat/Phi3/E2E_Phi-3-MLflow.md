<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:28:26+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "hi"
}
-->
# MLflow

[MLflow](https://mlflow.org/) एक ओपन-सोर्स प्लेटफ़ॉर्म है जो मशीन लर्निंग के पूरे जीवनचक्र को प्रबंधित करने के लिए बनाया गया है।

![MLFlow](../../../../../../translated_images/hi/MlFlowmlops.ed16f47809d74d9a.webp)

MLFlow का उपयोग ML जीवनचक्र को प्रबंधित करने के लिए किया जाता है, जिसमें प्रयोग, पुनरुत्पादकता, तैनाती और एक केंद्रीय मॉडल रजिस्ट्री शामिल है। MLflow वर्तमान में चार घटक प्रदान करता है।

- **MLflow Tracking:** प्रयोगों, कोड, डेटा कॉन्फ़िगरेशन और परिणामों को रिकॉर्ड और क्वेरी करें।
- **MLflow Projects:** डेटा साइंस कोड को इस तरह पैकेज करें कि उसे किसी भी प्लेटफ़ॉर्म पर पुनरुत्पादित किया जा सके।
- **Mlflow Models:** मशीन लर्निंग मॉडल को विभिन्न सर्विंग वातावरणों में तैनात करें।
- **Model Registry:** मॉडल को एक केंद्रीय रिपॉजिटरी में संग्रहित, एनोटेट और प्रबंधित करें।

इसमें प्रयोगों को ट्रैक करने, कोड को पुनरुत्पादक रन में पैकेज करने, और मॉडल साझा करने व तैनात करने की क्षमताएं शामिल हैं। MLFlow को Databricks में एकीकृत किया गया है और यह विभिन्न ML लाइब्रेरीज़ का समर्थन करता है, जिससे यह लाइब्रेरी-एग्नोस्टिक बन जाता है। इसे किसी भी मशीन लर्निंग लाइब्रेरी और किसी भी प्रोग्रामिंग भाषा के साथ इस्तेमाल किया जा सकता है, क्योंकि यह सुविधा के लिए REST API और CLI प्रदान करता है।

![MLFlow](../../../../../../translated_images/hi/MLflow2.5a22eb718f6311d1.webp)

MLFlow की मुख्य विशेषताएं हैं:

- **Experiment Tracking:** पैरामीटर और परिणामों को रिकॉर्ड और तुलना करें।
- **Model Management:** मॉडल को विभिन्न सर्विंग और इन्फरेंस प्लेटफ़ॉर्म पर तैनात करें।
- **Model Registry:** MLflow मॉडल के जीवनचक्र को सहयोगात्मक रूप से प्रबंधित करें, जिसमें संस्करण नियंत्रण और एनोटेशन शामिल हैं।
- **Projects:** ML कोड को साझा करने या प्रोडक्शन उपयोग के लिए पैकेज करें।

MLFlow MLOps लूप का भी समर्थन करता है, जिसमें डेटा तैयार करना, मॉडल पंजीकृत और प्रबंधित करना, मॉडल को निष्पादन के लिए पैकेज करना, सेवाओं को तैनात करना और मॉनिटरिंग शामिल है। इसका उद्देश्य प्रोटोटाइप से प्रोडक्शन वर्कफ़्लो तक के प्रोसेस को सरल बनाना है, खासकर क्लाउड और एज वातावरणों में।

## E2E परिदृश्य - एक रैपर बनाना और Phi-3 को MLFlow मॉडल के रूप में उपयोग करना

इस E2E उदाहरण में हम Phi-3 छोटे भाषा मॉडल (SLM) के चारों ओर रैपर बनाने के दो अलग-अलग तरीके दिखाएंगे और फिर इसे MLFlow मॉडल के रूप में स्थानीय या क्लाउड में, जैसे Azure Machine Learning वर्कस्पेस में चलाएंगे।

![MLFlow](../../../../../../translated_images/hi/MlFlow1.fd745e47dbd3fecf.webp)

| प्रोजेक्ट | विवरण | स्थान |
| ------------ | ----------- | -------- |
| Transformer Pipeline | यदि आप MLFlow के प्रयोगात्मक ट्रांसफॉर्मर्स फ्लेवर के साथ HuggingFace मॉडल का उपयोग करना चाहते हैं, तो Transformer Pipeline रैपर बनाने का सबसे आसान विकल्प है। | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | लेखन के समय, ट्रांसफॉर्मर पाइपलाइन ने ONNX फॉर्मेट में HuggingFace मॉडलों के लिए MLFlow रैपर जनरेशन का समर्थन नहीं किया, भले ही प्रयोगात्मक optimum Python पैकेज हो। ऐसे मामलों में, आप MLFlow मोड के लिए अपना कस्टम Python रैपर बना सकते हैं। | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## प्रोजेक्ट: Transformer Pipeline

1. आपको MLFlow और HuggingFace के संबंधित Python पैकेज की आवश्यकता होगी:

    ``` Python
    import mlflow
    import transformers
    ```

2. इसके बाद, आपको HuggingFace रजिस्ट्री में लक्षित Phi-3 मॉडल का संदर्भ देकर एक ट्रांसफॉर्मर पाइपलाइन शुरू करनी चाहिए। जैसा कि _Phi-3-mini-4k-instruct_ के मॉडल कार्ड से देखा जा सकता है, इसका कार्य "Text Generation" प्रकार का है:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. अब आप अपने Phi-3 मॉडल की ट्रांसफॉर्मर पाइपलाइन को MLFlow फॉर्मेट में सहेज सकते हैं और अतिरिक्त विवरण जैसे लक्षित आर्टिफैक्ट पथ, विशिष्ट मॉडल कॉन्फ़िगरेशन सेटिंग्स और इन्फरेंस API प्रकार प्रदान कर सकते हैं:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## प्रोजेक्ट: Custom Python Wrapper

1. हम यहाँ Microsoft के [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) का उपयोग कर सकते हैं ONNX मॉडल के इन्फरेंस और टोकन एन्कोडिंग/डिकोडिंग के लिए। आपको अपने लक्षित कंप्यूट के लिए _onnxruntime_genai_ पैकेज चुनना होगा, नीचे दिए गए उदाहरण में CPU लक्षित है:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. हमारी कस्टम क्लास दो मेथड्स लागू करती है: _load_context()_ जो Phi-3 Mini 4K Instruct के **ONNX मॉडल**, **जनरेटर पैरामीटर** और **टोकनाइज़र** को इनिशियलाइज़ करता है; और _predict()_ जो दिए गए प्रॉम्प्ट के लिए आउटपुट टोकन जनरेट करता है:

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

1. अब आप _mlflow.pyfunc.log_model()_ फ़ंक्शन का उपयोग करके Phi-3 मॉडल के लिए एक कस्टम Python रैपर (पिकल फॉर्मेट में) जनरेट कर सकते हैं, साथ ही मूल ONNX मॉडल और आवश्यक डिपेंडेंसीज़ के साथ:

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

## जनरेट किए गए MLFlow मॉडलों के सिग्नेचर

1. ऊपर Transformer Pipeline प्रोजेक्ट के चरण 3 में, हमने MLFlow मॉडल के कार्य को "_llm/v1/chat_" सेट किया। ऐसी निर्देशिका एक मॉडल का API रैपर बनाती है, जो OpenAI के Chat API के अनुकूल होता है, जैसा कि नीचे दिखाया गया है:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. परिणामस्वरूप, आप अपने प्रॉम्प्ट को निम्नलिखित प्रारूप में सबमिट कर सकते हैं:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. फिर, OpenAI API-अनुकूल पोस्ट-प्रोसेसिंग का उपयोग करें, जैसे _response[0][‘choices’][0][‘message’][‘content’]_, ताकि आउटपुट को इस तरह सुंदर बनाया जा सके:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. ऊपर Custom Python Wrapper प्रोजेक्ट के चरण 3 में, हमने MLFlow पैकेज को दिए गए इनपुट उदाहरण से मॉडल का सिग्नेचर जनरेट करने की अनुमति दी। हमारे MLFlow रैपर का सिग्नेचर इस प्रकार होगा:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. इसलिए, हमारे प्रॉम्प्ट में "prompt" डिक्शनरी की आवश्यकता होगी, कुछ इस तरह:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. मॉडल का आउटपुट तब स्ट्रिंग फॉर्मेट में प्रदान किया जाएगा:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।