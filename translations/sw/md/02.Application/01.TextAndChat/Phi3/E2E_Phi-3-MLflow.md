<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-05-09T18:39:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "sw"
}
-->
# MLflow

[MLflow](https://mlflow.org/) ni jukwaa la chanzo huria lililoundwa kusimamia mzunguko mzima wa maisha ya ujifunzaji wa mashine.

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.sw.png)

MLFlow hutumika kusimamia mzunguko wa maisha wa ML, ikiwa ni pamoja na majaribio, kurudisha matokeo, uanzishaji na rejista kuu ya modeli. MLFlow kwa sasa hutoa vipengele vinne.

- **MLflow Tracking:** Rekodi na uliza majaribio, msimbo, usanidi wa data na matokeo.
- **MLflow Projects:** Pakia msimbo wa sayansi ya data kwa muundo unaoruhusu kuendesha tena kwenye jukwaa lolote.
- **Mlflow Models:** Weka modeli za ujifunzaji wa mashine kwenye mazingira tofauti ya huduma.
- **Model Registry:** Hifadhi, fafanua na simamia modeli katika hifadhi kuu.

Inajumuisha uwezo wa kufuatilia majaribio, kufunga msimbo katika kuendesha tena, na kushiriki na kupeleka modeli. MLFlow imeunganishwa na Databricks na inaunga mkono maktaba mbalimbali za ML, hivyo haihitaji maktaba maalum. Inaweza kutumika na maktaba yoyote ya ujifunzaji wa mashine na lugha yoyote ya programu, kwani hutoa REST API na CLI kwa urahisi.

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.sw.png)

Vipengele muhimu vya MLFlow ni pamoja na:

- **Ufuatiliaji wa Majaribio:** Rekodi na linganisha vigezo na matokeo.
- **Usimamizi wa Modeli:** Weka modeli kwenye jukwaa mbalimbali za huduma na utabiri.
- **Model Registry:** Simamia kwa ushirikiano mzunguko wa maisha wa MLflow Models, ikiwa ni pamoja na toleo na maelezo.
- **Projects:** Pakia msimbo wa ML kwa ajili ya kushiriki au matumizi ya uzalishaji.
MLFlow pia inaunga mkono mzunguko wa MLOps, unaojumuisha kuandaa data, kusajili na kusimamia modeli, kufunga modeli kwa ajili ya utekelezaji, kupeleka huduma, na kufuatilia modeli. Lengo lake ni kurahisisha mchakato wa kutoka mfano hadi mtiririko wa uzalishaji, hasa katika mazingira ya wingu na edge.

## E2E Scenario - Kujenga wrapper na kutumia Phi-3 kama modeli ya MLFlow

Katika mfano huu wa E2E tutaonyesha njia mbili tofauti za kujenga wrapper kuzunguka Phi-3 mfano mdogo wa lugha (SLM) kisha kuutumia kama modeli ya MLFlow ama kwa ndani au wingu, mfano katika Azure Machine Learning workspace.

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.sw.png)

| Mradi | Maelezo | Mahali |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline ni njia rahisi zaidi ya kujenga wrapper ikiwa unataka kutumia mfano wa HuggingFace na ladha ya majaribio ya transformers ya MLFlow. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | Wakati wa kuandika, transformer pipeline haikuunga mkono uundaji wa wrapper ya MLFlow kwa mfano wa HuggingFace katika muundo wa ONNX, hata ukiwa na kifurushi cha majaribio cha optimum Python. Kwa kesi kama hizi, unaweza kujenga wrapper yako maalum ya Python kwa mode ya MLFlow | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Mradi: Transformer Pipeline

1. Utahitaji vifurushi vya Python vinavyohitajika kutoka MLFlow na HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Kisha, unapaswa kuanzisha transformer pipeline kwa kurejelea mfano wa Phi-3 unaolengwa katika rejista ya HuggingFace. Kama inavyoonekana kwenye kadi ya mfano ya _Phi-3-mini-4k-instruct_, kazi yake ni ya aina ya “Text Generation”:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Sasa unaweza kuhifadhi transformer pipeline ya mfano wako wa Phi-3 katika muundo wa MLFlow na kutoa maelezo ya ziada kama njia ya kuhifadhi artifacts, usanidi maalum wa modeli na aina ya API ya utabiri:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Mradi: Custom Python Wrapper

1. Tunaweza kutumia hapa API ya [ONNX Runtime generate()](https://github.com/microsoft/onnxruntime-genai) ya Microsoft kwa ajili ya utabiri wa mfano wa ONNX na usimbaji/ufumbuzi wa tokeni. Unapaswa kuchagua kifurushi _onnxruntime_genai_ kwa kompyuta unayotaka, mfano huu unalenga CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Darasa letu maalum lina utekelezaji wa njia mbili: _load_context()_ kuanzisha **mfano wa ONNX** wa Phi-3 Mini 4K Instruct, **vigezo vya kizalishaji** na **tokenizer**; na _predict()_ kuzalisha tokeni za matokeo kwa ombi lililotolewa:

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

1. Sasa unaweza kutumia _mlflow.pyfunc.log_model()_ kuunda wrapper maalum ya Python (katika muundo wa pickle) kwa mfano wa Phi-3, pamoja na mfano halisi wa ONNX na utegemezi unaohitajika:

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

## Sahihi za modeli zilizotengenezwa za MLFlow

1. Katika hatua ya 3 ya mradi wa Transformer Pipeline hapo juu, tuliweka kazi ya modeli ya MLFlow kuwa “_llm/v1/chat_”. Maelekezo haya hutengeneza wrapper ya API ya modeli, inayolingana na OpenAI Chat API kama ilivyoonyeshwa hapa chini:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Matokeo yake, unaweza kuwasilisha ombi lako kwa muundo ufuatao:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Kisha, tumia urekebishaji unaolingana na OpenAI API, mfano _response[0][‘choices’][0][‘message’][‘content’]_, kuboresha matokeo yako hadi kitu kama hiki:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. Katika hatua ya 3 ya mradi wa Custom Python Wrapper hapo juu, tunaruhusu kifurushi cha MLFlow kuunda sahihi ya modeli kutoka kwa mfano wa ingizo uliopewa. Sahihi ya wrapper yetu ya MLFlow itaonekana kama hii:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Hivyo, ombi letu litahitaji kuwa na ufunguo wa kamusi "prompt", kama ifuatavyo:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Matokeo ya modeli yatatolewa kisha kwa muundo wa mfuatano wa herufi:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Kanganyo**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upotovu wa maana. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebwi dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.