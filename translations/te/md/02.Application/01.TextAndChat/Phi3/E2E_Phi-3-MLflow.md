<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-12-21T20:55:32+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "te"
}
-->
# MLflow

[MLflow](https://mlflow.org/) అనేది end-to-end మెషిన్ లెర్నింగ్ లైఫ్‌సైకిల్‌ను నిర్వహించడానికి రూపొందించిన ఓపెన్-సోర్స్ ప్లాట్‌ఫారం.

![MLFlow](../../../../../../translated_images/MlFlowmlops.ed16f47809d74d9ac0407bf43985ec022ad01f3d970083e465326951e43b2e01.te.png)

MLFlowను ప్రయోగాలు, పునరుత్పత్తి, డిప్లాయ్మెంట్ మరియు కేంద్ర మోడల్ రిజిస్ట్రీ సహా ML లైఫ్‌సైకిల్‌ను నిర్వహించడానికి ఉపయోగిస్తారు. MLFlow ప్రస్తుతం నాలుగు घटకాలను అందిస్తుంది.

- **MLflow Tracking:** ప్రయోగాలు, కోడ్, డేటా కాన్ఫిగ్ మరియు ఫలితాలను రికార్డ్ చేసి ప్రశ్నించండి.
- **MLflow Projects:** ఏ ప్లాట్‌ఫారమ్‌లోనైనా రన్లను పునరుత్పత్తి చేయడానికి డేటా సైన్స్ కో드를 ఒక ఫార్మాట్‌లో ప్యాకేజ్ చేయండి.
- **Mlflow Models:** వివిధ సర్వింగ్ మార్గాలలో మెషిన్ లెర్నింగ్ మోడల్స్‌ను డిప్లాయ్ చేయండి.
- **Model Registry:** మోడల్స్‌ను ఒక కేంద్ర నిల్వలో నిల్వ చేయండి, ట్యాగ్ చేయండి మరియు నిర్వహించండి.

ఇది ప్రయోగాలను ట్రాక్ చేయడం, కోడ్‌ను పునరుత్పత్తి చేయగల రన్లుగా ప్యాకేజ్ చేయడం, మరియు మోడల్స్‌ను పంచుకోవడం మరియు వినియోగానికి పంపడం వంటి సామర్థ్యాలను ఉంది. MLFlow Databricksలో ఏకీకృతమై ఉంది మరియు వివిధ ML లైబ్రరీలను మద్దతిస్తుంది, దీని వల్ల అది లైబ్రరీ-నిరపేక్షంగా ఉంటుంది. ఇది ఏ మెషిన్ లెర్నింగ్ లైబ్రరీతోనైనా మరియు ఏ программింగ్ భాషలోనైనా ఉపయోగించవచ్చు, ఎందుకంటే అదనంగా అనుకూలత కోసం REST API మరియు CLIని అందిస్తుంది.

![MLFlow](../../../../../../translated_images/MLflow2.5a22eb718f6311d16f1a1952a047dc6b9e392649f1e0fc7bc3c3dcd65e3af07c.te.png)

MLFlow యొక్క ముఖ్య లక్షణాలు:

- **Experiment Tracking:** పరామితులు మరియు ఫలితాలను రికార్డ్ చేసి మరియు సరఖ్ఖించండి.
- **Model Management:** వివిధ సర్వింగ్ మరియు ఇన్ఫరెన్స్ ప్లాట్‌ఫారమ్‌లకు మోడల్స్‌ను డిప్లాయ్ చేయండి.
- **Model Registry:** వెర్షనింగ్ మరియు అనోటేషన్లు సహా MLflow Models యొక్క లైఫ్‌సైకిల్‌ను సహకారంగా నిర్వహించండి.
- **Projects:** భాగస్వామ్యం లేదా ప్రొడక్షన్ ఉపయోగం కోసం ML కోడ్‌ను ప్యాకేజ్ చేయండి.

MLFlow MLOps లూప్‌ని కూడా మద్దతు చేస్తుంది, దీనిలో డేటాను సిద్ధం చేయడం, మోడల్స్‌ను రిజిస్టర్ చేయడం మరియు నిర్వహించడం, అమలుకు మోడల్స్‌ను ప్యాకేజ్ చేయడం, సేవలను డిప్లాయ్ చేయడం మరియు మోడల్స్‌ను మానిటర్ చేయడం ఉన్నాయి. ఇది ప్రోటోటైప్ నుండి ప్రొడక్షన్ వర్క్‌ఫ్లోకు మారడానికి ప్రక్రియను సరళతరం చేయడమే లక్ష్యంగా పెట్టుకొంది, ప్రత్యేకంగా క్లౌడ్ మరియు ఎడ్జ్ పర్యావరణాల్లో.

## E2E Scenario - Building a wrapper and using Phi-3 as an MLFlow model

ఈ E2E నమూనాలో, Phi-3 చిన్న భాషా మోడల్ (SLM) చుట్టూ ఒక రాపర్‌ను నిర్మించడానికి రెండు వివిధ దృక్పథాలను మరియు ఆపై దాన్ని స్థానికంగా లేదా క్లౌడ్‌లో, ఉదాహరణకి Azure Machine Learning వర్క్‌స్పేస్‌లో MLFlow మోడల్‌గా ఎలా నడపాలనేదాన్ని ప్రదర్శిస్తాము.

![MLFlow](../../../../../../translated_images/MlFlow1.fd745e47dbd3fecfee254096d496cdf1cb3e1789184f9efcead9c2a96e5a979b.te.png)

| Project | Description | Location |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer PIpeline ఒక HuggingFace మోడల్‌ను MLFlow యొక్క ప్రయోగాత్మక transformers ఫ్లేవర్‌తో ఉపయోగించాలనుకుంటే రాపర్‌ను నిర్మించడానికి సులభترین ఎంపిక. | [**TransformerPipeline.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | రాయുമ്പോల్ సమయంలో, transformer pipeline MLFlow రాపర్ జనరేషన్‌ను ONNX ఫార్మాట్‌లో ఉన్న HuggingFace మోడల్స్ కోసం మద్దతు చేయలేదు, చాలా సందర్భాల్లో కూడా ప్రయోగాత్మక optimum Python ప్యాకేజ్ ఉన్నా కాదు. ఇలాంటి సందర్భాల కోసం, మీరు MLFlow కోసం మీ స్వంత కస్టం Python రాపర్‌ను నిర్మించవచ్చు | [**CustomPythonWrapper.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Project: Transformer Pipeline

1. మీరు MLFlow మరియు HuggingFace నుండి సంబంధిత Python ప్యాకేజీలను అవసరం పడతాయి:

    ``` Python
    import mlflow
    import transformers
    ```

2. తరువాత, HuggingFace రిజిస్ట్రీలో టార్గెట్ Phi-3 మోడల్‌కు సూచిస్తూ transformer pipeline ను ప్రారంభించాలి. _Phi-3-mini-4k-instruct_ యొక్క మోడల్ కార్డ్ నుంచి చూస్తే, దీని టాస్క్ “Text Generation” తరహాకు చెందుతుంద‌ని కనిపిస్తుంది:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. మీరు ఇప్పుడు మీ Phi-3 మోడల్ యొక్క transformer pipeline ను MLFlow ఫార్మాట్‌లో సేవ్ చేసి లక్ష్య ఆర్టిఫాక్ట్స్ పాత్, నిర్దిష్ట మోడల్ కాన్ఫిగరేషన్ సెట్టింగ్స్ మరియు ఇన్ఫరెన్స్ API టైప్ వంటి అదనపు వివరాలు అందించవచ్చు:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Project: Custom Python Wrapper

1. ఇక్కడ మేము ONNX మోడల్ యొక్క ఇన్ఫరెన్స్ మరియు టోకెన్స్ ఎంకోడింగ్/డికొడింగ్ కోసం Microsoft's [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) ను ఉపయోగించవచ్చు. మీ లక్ష్య కంప్యూట్ కోసం మీరు _onnxruntime_genai_ ప్యాకేజ్‌ను ఎంపిక చేయాలి, క్రింది ఉదాహరణ CPU లక్ష్యంగా ఉంటుంది:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. మా కస్టమ్ క్లాస్ రెండు మెథడ్స్‌ను అమలు చేస్తుంది: ఇచ్చిన ప్రాంప్ట్‌కు అవుట్‌పుట్ టోకెన్స్ ఉత్పత్తి చేయడానికి _predict()_; మరియు **ONNX మోడల్**, **జనరేటర్ పరామితులు** మరియు **టోకనైజర్**ను ప్రారంభించడానికి _load_context()_:

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # ఆర్టిఫాక్టుల నుండి మోడల్‌ను పొందడం
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # మోడల్‌ను నిర్వచించడం
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # టోకనైజర్‌ను నిర్వచించడం
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # ఇన్‌పుట్ నుండి ప్రాంప్ట్‌ను పొందడం
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # మోడల్ యొక్క ప్రతిస్పందనను ఉత్పత్తి చేయడం
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

1. మీరు ఇప్పుడు _mlflow.pyfunc.log_model()_ ఫంక్షన్‌ను ఉపయోగించి Phi-3 మోడల్ కోసం ఒక కస్టమ్ Python రాపర్ (pickle ఫార్మాట్‌లో), అసలు ONNX మోడల్ మరియు అవసరమైన డిపెండెన్సులతో జెనరేట్ చేయవచ్చు:

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

## Signatures of generated MLFlow models

1. పైలో Transformer Pipeline ప్రాజెక్ట్‌లో స్టెప్ 3లో, మేము MLFlow మోడల్ యొక్క టాస్క్‌ను “_llm/v1/chat_” గా సెట్ చేసాము. ఇలాంటి సూచన ఒక మోడల్ యొక్క API రాపర్‌ను జనరేట్ చేస్తుంది, అది OpenAI యొక్క Chat APIకి అనుకూలంగా ఉంటుంది, దిగువ చూపినట్లుగా:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. ఫలితంగా, మీరు మీ ప్రాంప్ట్‌ను క్రింది ఫార్మాట్‌లో సమర్పించవచ్చు:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. ఆపై, OpenAI API అనుకూల పోస్ట్-ప్రాసెసింగ్ ఉపయోగించి, ఉదాహరణకి _response[0][‘choices’][0][‘message’][‘content’]_, మీ అవుట్‌పుట్‌ను ఈ విధంగా అందగించవచ్చు:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. పై Custom Python Wrapper ప్రాజెక్ట్‌లోని స్టెప్ 3లో, మేము ఇచ్చిన ఇన్పుట్ ఉదాహరణ నుండి మోడల్ యొక్క సిగ్నేచర్‌ను MLFlow ప్యాకేజ్ ద్వారా 생성 చేయనివ్వగలము. మా MLFlow రాపర్ యొక్క సిగ్నేచర్ ఈ విధంగా ఉంటుంది:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. కాబట్టి, మా ప్రాంప్ట్‌కు "prompt" అనే డిక్షనరీ కీ అవసరం ఉంటుంది, దీని ఉదాహరణ ఇలాంటిది:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. ఆ తరువాత, మోడల్ యొక్క అవుట్‌పుట్ స్ట్రింగ్ ఫార్మాట్‌లో అందించబడుతుంది:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
డిస్క్లెమర్:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించారు. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండే అవకాశం ఉండొచ్చు అని గమనించండి. స్థానిక భాషలో ఉండే అసలు పత్రాన్నే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరులైన మానవ అనువాదాన్ని సిఫార్సు చేయబడింది. ఈ అనువాదాన్ని ఉపయోగించడానికి కారణంగా కలిగే ఏవైనా అవగాహనా లోపాలు లేదా తప్పుతీరుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->