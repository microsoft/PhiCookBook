<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:29:06+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "mr"
}
-->
# MLflow

[MLflow](https://mlflow.org/) हा एक मुक्त स्रोत प्लॅटफॉर्म आहे जो मशीन लर्निंगच्या संपूर्ण जीवनचक्राचे व्यवस्थापन करण्यासाठी तयार केला गेला आहे.

![MLFlow](../../../../../../translated_images/MlFlowmlops.ed16f47809d74d9a.mr.png)

MLFlow मशीन लर्निंग जीवनचक्राचे व्यवस्थापन करण्यासाठी वापरला जातो, ज्यामध्ये प्रयोग, पुनरुत्पादकता, तैनाती आणि एक केंद्रीय मॉडेल रजिस्ट्रेशन यांचा समावेश आहे. सध्या MLflow चार घटक ऑफर करतो.

- **MLflow Tracking:** प्रयोग, कोड, डेटा कॉन्फिगरेशन आणि निकाल नोंदवणे आणि शोधणे.
- **MLflow Projects:** डेटा सायन्स कोड अशा स्वरूपात पॅकेज करणे जे कोणत्याही प्लॅटफॉर्मवर पुन्हा चालवता येईल.
- **Mlflow Models:** विविध सेवा वातावरणांमध्ये मशीन लर्निंग मॉडेल्स तैनात करणे.
- **Model Registry:** मॉडेल्स एका केंद्रीय संग्रहात साठवणे, टिप्पणी करणे आणि व्यवस्थापित करणे.

यामध्ये प्रयोग ट्रॅक करण्याची, कोड पुनरुत्पादक रनमध्ये पॅकेज करण्याची, तसेच मॉडेल्स शेअर आणि तैनात करण्याची क्षमता आहे. MLFlow Databricks मध्ये समाकलित आहे आणि विविध ML लायब्ररींना समर्थन देते, त्यामुळे ते लायब्ररी-स्वतंत्र आहे. हे कोणत्याही मशीन लर्निंग लायब्ररीसह आणि कोणत्याही प्रोग्रामिंग भाषेत वापरता येते, कारण ते REST API आणि CLI सुविधा प्रदान करते.

![MLFlow](../../../../../../translated_images/MLflow2.5a22eb718f6311d1.mr.png)

MLFlow चे मुख्य वैशिष्ट्ये:

- **Experiment Tracking:** पॅरामीटर्स आणि निकाल नोंदवणे आणि तुलना करणे.
- **Model Management:** विविध सेवा आणि इन्फरन्स प्लॅटफॉर्मवर मॉडेल्स तैनात करणे.
- **Model Registry:** MLflow मॉडेल्सच्या जीवनचक्राचे सहकार्याने व्यवस्थापन करणे, ज्यात आवृत्ती नियंत्रण आणि टिप्पण्या यांचा समावेश आहे.
- **Projects:** ML कोड शेअरिंग किंवा उत्पादनासाठी पॅकेज करणे.

MLFlow MLOps लूपला देखील समर्थन देते, ज्यामध्ये डेटा तयार करणे, मॉडेल नोंदणी आणि व्यवस्थापन, मॉडेल्सचे पॅकेजिंग, सेवा तैनात करणे आणि मॉडेल्सचे निरीक्षण करणे यांचा समावेश आहे. हे प्रोटोटाइपपासून उत्पादन कार्यप्रवाहाकडे जाण्याची प्रक्रिया सुलभ करण्याचा उद्देश ठेवते, विशेषतः क्लाउड आणि एज वातावरणात.

## E2E उदाहरण - Phi-3 साठी wrapper तयार करणे आणि MLFlow मॉडेल म्हणून वापरणे

या E2E उदाहरणात आपण Phi-3 लहान भाषा मॉडेल (SLM) च्या भोवती wrapper तयार करण्यासाठी दोन वेगवेगळ्या पद्धती दाखवू आणि नंतर ते MLFlow मॉडेल म्हणून स्थानिक किंवा क्लाउडमध्ये, उदा. Azure Machine Learning वर्कस्पेसमध्ये कसे चालवायचे ते पाहू.

![MLFlow](../../../../../../translated_images/MlFlow1.fd745e47dbd3fecf.mr.png)

| प्रोजेक्ट | वर्णन | स्थान |
| ------------ | ----------- | -------- |
| Transformer Pipeline | जर तुम्हाला MLFlow च्या प्रयोगात्मक transformers flavour सह HuggingFace मॉडेल वापरायचे असेल तर Transformer Pipeline wrapper तयार करण्याचा सर्वात सोपा पर्याय आहे. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | लेखनाच्या वेळी, transformer pipeline ने HuggingFace मॉडेल्ससाठी ONNX स्वरूपात MLFlow wrapper जनरेट करण्यास समर्थन दिले नव्हते, अगदी प्रयोगात्मक optimum Python पॅकेजसहही. अशा प्रकरणांसाठी, तुम्ही MLFlow मोडसाठी तुमचा स्वतःचा Python wrapper तयार करू शकता. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## प्रोजेक्ट: Transformer Pipeline

1. तुम्हाला MLFlow आणि HuggingFace कडून संबंधित Python पॅकेजेसची गरज भासेल:

    ``` Python
    import mlflow
    import transformers
    ```

2. नंतर, तुम्ही HuggingFace रजिस्ट्रीतून लक्ष्य Phi-3 मॉडेलचा संदर्भ देऊन transformer pipeline सुरू करायला हवे. _Phi-3-mini-4k-instruct_ च्या मॉडेल कार्डनुसार, त्याचे कार्य "Text Generation" प्रकाराचे आहे:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. आता तुम्ही तुमच्या Phi-3 मॉडेलचा transformer pipeline MLFlow स्वरूपात जतन करू शकता आणि अतिरिक्त तपशील जसे की लक्ष्य आर्टिफॅक्ट्सचा मार्ग, विशिष्ट मॉडेल कॉन्फिगरेशन सेटिंग्ज आणि इन्फरन्स API प्रकार प्रदान करू शकता:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## प्रोजेक्ट: Custom Python Wrapper

1. येथे आपण Microsoft चा [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) ONNX मॉडेलच्या इन्फरन्स आणि टोकन्स एन्कोडिंग/डिकोडिंगसाठी वापरू शकतो. तुमच्या लक्ष्य संगणनासाठी _onnxruntime_genai_ पॅकेज निवडावे लागेल, खालील उदाहरण CPU साठी आहे:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. आमच्या कस्टम क्लासमध्ये दोन पद्धती आहेत: _load_context()_ जी Phi-3 Mini 4K Instruct चा **ONNX मॉडेल**, **जनरेटर पॅरामीटर्स** आणि **tokenizer** प्रारंभ करते; आणि _predict()_ जी दिलेल्या प्रॉम्प्टसाठी आउटपुट टोकन्स तयार करते:

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

1. आता तुम्ही _mlflow.pyfunc.log_model()_ फंक्शन वापरून Phi-3 मॉडेलसाठी कस्टम Python wrapper (pickle स्वरूपात) तयार करू शकता, ज्यामध्ये मूळ ONNX मॉडेल आणि आवश्यक अवलंबित्वे असतील:

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

## तयार केलेल्या MLFlow मॉडेल्सच्या सिग्नेचर्स

1. वर Transformer Pipeline प्रोजेक्टच्या टप्पा 3 मध्ये, आपण MLFlow मॉडेलचे कार्य "_llm/v1/chat_" असे सेट केले. अशा सूचनेने OpenAI च्या Chat API शी सुसंगत मॉडेल API wrapper तयार होतो, खाली दाखवले आहे:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. परिणामी, तुम्ही तुमचा प्रॉम्प्ट खालील स्वरूपात सबमिट करू शकता:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. नंतर, OpenAI API-सुसंगत पोस्ट-प्रोसेसिंग वापरा, उदा. _response[0][‘choices’][0][‘message’][‘content’]_, ज्यामुळे तुमचा आउटपुट सुंदर दिसेल:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. वर Custom Python Wrapper प्रोजेक्टच्या टप्पा 3 मध्ये, आम्ही MLFlow पॅकेजला दिलेल्या इनपुट उदाहरणावरून मॉडेलची सिग्नेचर तयार करण्याची परवानगी दिली आहे. आमच्या MLFlow wrapper ची सिग्नेचर अशी दिसेल:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. त्यामुळे, आमच्या प्रॉम्प्टमध्ये "prompt" नावाचा dictionary की असणे आवश्यक आहे, खालीलप्रमाणे:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. मॉडेलचा आउटपुट नंतर स्ट्रिंग स्वरूपात दिला जाईल:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.