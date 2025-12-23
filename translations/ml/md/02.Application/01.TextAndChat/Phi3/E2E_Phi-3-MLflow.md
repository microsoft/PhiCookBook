<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-12-21T20:57:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "ml"
}
-->
# MLflow

[MLflow](https://mlflow.org/) ഒരു ഒപ്പൺ-സോഴ്‌സ് പ്ലാറ്റ്ഫോമാണ്, ആൻഡ്-ടു-ആൻഡ് മെഷീൻ ലേണിങ് ലൈഫ്‌സൈക്കിള്‍ നിയന്ത്രിക്കാൻ രൂപകൽപ്പന ചെയ്തത്.

![MLFlow](../../../../../../translated_images/MlFlowmlops.ed16f47809d74d9ac0407bf43985ec022ad01f3d970083e465326951e43b2e01.ml.png)

MLFlow പരീക്ഷണങ്ങൾ, പുനരുത്പാദ്യത, വിന്യസനം എന്നിവ ഉൾപ്പെടെയുള്ള ML ലൈഫ്‌സൈക്ലിനെ നിയന്ത്രിക്കാൻ ഉപയോഗിക്കുന്നു, കൂടാതെ ഒരു കേന്ദ്ര മോഡൽ റെജിസ്ട്രിയാണ്. MLFlow ഇപ്പോൾ നാല് ഘടകങ്ങൾ പണിയിതു.

- **MLflow Tracking:** പരീക്ഷണങ്ങൾ, കോഡ്, ഡാറ്റ കോൺഫിഗ് എന്നിവ രേഖപ്പെടുത്തുകയും ക്വറി ചെയ്യുകയും ചെയ്യുക.
- **MLflow Projects:** റണ്‍ റീപ്രോഡ്യൂസ്ബിൾ ആക്കാൻ ഡാറ്റാ സയൻസ് കോഡ് ഫോർമാറ്റിൽ പാക്കേജ് ചെയ്യുക.
- **Mlflow Models:** വൈവിധ്യമായ സർവിംഗ് പരിസ്ഥിതികളിൽ മെഷീൻ ലേണിങ് മോഡലുകൾ വിന്യസിക്കുക.
- **Model Registry:** മോഡലുകൾ ഒരു കേന്ദ്ര സംഭരണത്തിൽ സ്റ്റോർ ചെയ്യുക, അനോട്ടേറ്റ് ചെയ്യുക, മാനേജ് ചെയ്യുക.

ഇത് പരീക്ഷണങ്ങൾ ട്രാക്കിംഗ് ചെയ്യാനുള്ള, കോഡ് റീപ്രൊഡ്യൂസ്ബിൾ റണുകൾ ആയി പാക്കേജ് ചെയ്യാനുള്ള, മോഡലുകൾ പങ്കുവെക്കാനും വിന്യസിക്കാനും ഉള്ള ശേഷികൾ ഉൾക്കൊള്ളുന്നു. MLFlow Databricks-ൽ ഇന്റეგ്രേറ്റ് ചെയ്തിട്ടുണ്ട് һәм വിവിധ ML ലൈബ്രറികളുമായി അനുയോജ്യമാണ്, അതിനാൽ ലൈബ്രറി-അഗ്നോസ്റ്റിക് ആണ്. ഇത് REST APIയും CLIയുമൊടു любക്കത്തിൽ ഉപയോഗിക്കാവുന്നതാണ്, അതിനാൽ ഏതെങ്കിലും മെഷീൻ ലേണിങ് ലൈബ്രറിയോടും ഏതൊരു പ്രോഗ്രാമിംഗ് ഭാഷയിലും ഉപയോഗിക്കാവുന്നതാണ്.

![MLFlow](../../../../../../translated_images/MLflow2.5a22eb718f6311d16f1a1952a047dc6b9e392649f1e0fc7bc3c3dcd65e3af07c.ml.png)

MLFlow-യുടെ പ്രധാന ഫീച്ചറുകൾ:

- **Experiment Tracking:** പാരാമീറ്ററുകളും ഫലങ്ങളും രേഖപ്പെടുത്തുകയും താരതമ്യം ചെയ്യുകയും ചെയ്യുക.
- **Model Management:** വിവിധ സർവിംഗ് और ഇൻഫറൻസ് പ്ലാറ്റ്ഫോമുകളിൽ മോഡലുകൾ വിന്യസിക്കുക.
- **Model Registry:** വേർഷനിംഗ്, അനോട്ടേഷനുകൾ എന്നിവ ഉൾപ്പെടെയുള്ള MLflow മോഡലുകളുടെ ലൈഫ്‌സൈക്കിൾ സഹകരിച്ച് മാനേജ് ചെയ്യുക.
- **Projects:** ഷെയറിംഗ് അല്ലെങ്കിൽ പ്രൊഡക്ഷൻ ഉപയോഗത്തിന് ML കോഡ് പാക്കേജ് ചെയ്യുക.
MLFlow MLOps ലൂപും പിന്തുണയ്ക്കുന്നു, അത് ഡാറ്റ ഒരുക്കൽ, മോഡലുകൾ രജിസ്റ്റർ ചെയ്ത് മാനേജ് ചെയ്യൽ, എക്സിക്യൂഷനിലേക്ക് മോഡലുകൾ പാക്കേജ് ചെയ്യൽ, സർവീസുകൾ വിന്യസിക്കൽ, മോഡലുകൾ നിരീക്ഷിക്കൽ എന്നിവ ഉൾക്കൊള്ളുന്നു. ഇത് പ്രോട്ടോട്ടൈപ്പിൽ നിന്നുള്ള ഒരു പ്രൊഡക്ഷൻ വർക്‌ഫ്ലോയിലേക്കുള്ള മാറ്റം ലളിതമാക്കാൻ ലക്ഷ്യമിടുന്നു, പ്രത്യേകിച്ച് ക്ലൗഡിലും എഡ്ജ് പരിസ്ഥിതികളിലും.

## E2E Scenario - Building a wrapper and using Phi-3 as an MLFlow model

ഈ E2E സാമ്പിളിൽ നാം Phi-3 സ്മോൾ ലാംഗ്വജ് മോഡലിന്റെ (SLM) ചുറ്റുമുള്ള ഒരുWrapper രണ്ട് വ്യത്യസ്ത സമീപനങ്ങളിലും നിർമ്മിച്ച് അത് MLFlow മോഡലായി ലോക്കലായി അല്ലെങ്കിൽ ക്ലൗഡിൽ (ഉദാഹരണത്തിന് Azure Machine Learning workspace) പ്രവർത്തിപ്പിക്കുന്നത് കാണിക്കും.

![MLFlow](../../../../../../translated_images/MlFlow1.fd745e47dbd3fecfee254096d496cdf1cb3e1789184f9efcead9c2a96e5a979b.ml.png)

| Project | Description | Location |
| ------------ | ----------- | -------- |
| Transformer Pipeline | HuggingFace മോഡൽ MLFlow-ലൂ കാസ്തവമായി experimental transformers ഫ്ലേവറുമായി ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്നെങ്കിൽ wrapper നിർമ്മിക്കാൻ ഏറ്റവും ലളിതമായ ഓപ്‌ഷനാണ് Transformer PIpeline. | [**TransformerPipeline.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | എഴുതപ്പെട്ട സമയത്ത്, ട്രാൻസ്ഫോർമർ പൈപ്പ്ലൈൻ ONNX ഫോർമാറ്റിലുള്ള HuggingFace മോഡലുകൾക്കായി MLFlow wrapper ജനറേഷൻ പിന്തുണച്ചിരുന്നില്ല, ഒപ്റ്റിമം experimental Python പാക്കേജും ഉപയോഗിച്ചിരുന്നാലും. ഇത്തരം കേസുകൾക്കായി, നിങ്ങൾക്ക് MLFlow മോഡലിനായി നിങ്ങളുടെ കസ്റ്റം Python wrapper നിർമ്മിക്കാൻ കഴിയും | [**CustomPythonWrapper.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Project: Transformer Pipeline

1. MLFlow, HuggingFace എന്നിവയിൽ നിന്നുള്ള അനുയോജ്യ Python പാക്കേജുകൾ നിങ്ങൾക്ക് ആവശ്യമാണ്:

    ``` Python
    import mlflow
    import transformers
    ```

2. അടുത്തതായി, HuggingFace രജിസ്ട്രിയിൽ ലക്ഷ്യ Phi-3 മോഡൽ പരാമർശിച്ച് ഒരു ട്രാൻസ്ഫോർമർ പൈപ്പ്ലൈൻ ആരംഭിക്കേണ്ടതാണ്. _Phi-3-mini-4k-instruct_ മോഡൽ കാർഡിൽ കാണുന്നതുപോലെ, ഇതിന്റെ ടാസ്‌ക് “Text Generation” തരം ആണ്:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Phi-3 മോഡലിന്റെ ട്രാൻസ്ഫോർമർ പൈപ്പ്ലൈനെ MLFlow ഫോർമാറ്റിൽ സേവ് ചെയ്യുകയും ലക്ഷ്യ ആർട്ടിഫാക്റ്റ്സ് പാത്ത്, പ്രത്യേക മോഡൽ കോൺഫിഗറേഷൻ സെറ്റിങ്ങുകൾ, ഇൻഫറൻസ് API തരം തുടങ്ങി അധിക വിശദാംശങ്ങൾ നൽകുകയും ചെയ്യാം:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Project: Custom Python Wrapper

1. ONNX മോഡലിന്റെ ഇൻഫറൻസ്, ടോക്കൺ എൻകോഡിംഗ്/ഡികോഡിംഗ് എന്നിവയ്ക്കായി ഞങ്ങൾ ഇവിടെ Microsoft's [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) ഉപയോഗിക്കാം. നിങ്ങളുടെ ലക്ഷ്യ കംപ്യൂട്ടിന് അനുയോജ്യമായ _onnxruntime_genai_ പാക്കേജിനെ തിരഞ്ഞെടുക്കണം; താഴെയുള്ള ഉദാഹരണം CPU-നെ ലക്ഷ്യമ بنایا ഉണ്ട്:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. ഞങ്ങളുടെ കസ്റ്റം ക്ലാസ് രണ്ട് മെത്തഡുകൾ നടപ്പാക്കുന്നു: _load_context()_ Phi-3 Mini 4K Instruct-ന്റെ **ONNX model**, **generator parameters** და **tokenizer** ആരംഭിക്കാൻ; ಮತ್ತು _predict()_ നൽകിയ പ്രോംപ്റ്റ് için ഔട്ട്പുട്ട് ടോക്കൺസ് ജനറേറ്റ് ചെയ്യാൻ:

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # ആർട്ടിഫാക്ടുകളിലെ നിന്ന് മോഡൽ വീണ്ടെടുക്കുന്നു
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # മോഡൽ നിർവചിക്കുന്നു
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # ടോക്കണൈസർ നിർവചിക്കുന്നു
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # ഇൻപുട്ടിൽ നിന്ന് പ്രോംപ്റ്റ് വീണ്ടെടുക്കുന്നു
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # മോഡലിന്റെ മറുപടി സൃഷ്ടിക്കുന്നു
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

1. Phi-3 മോഡലിനായി ഓറിജിനൽ ONNX മോഡലും ആവശ്യമായ ഡിപെൻഡൻസികളും കൂടെ ഉൾകൊള്ളുന്ന കസ്റ്റം Python wrapper (pickle ഫോർമാറ്റിൽ) ജനറേറ്റ് ചെയ്യാൻ നിങ്ങൾക്ക് _mlflow.pyfunc.log_model()_ ഫങ്ഷൻ ഉപയോഗിക്കാം:

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

1. മുകളിലുള്ള Transformer Pipeline പ്രോജക്റ്റിലെ ഘട്ടം 3-ൽ, ഞങ്ങൾ MLFlow മോഡലിന്റെ ടാസ്‌ക് “_llm/v1/chat_” ആയി സജ്ജമാക്കിയിരുന്നു. ഇത്തരം നിർദേശനം OpenAI-യുടെ Chat API-നോടുTAൺസമ്പന്നമായ മോഡൽ API wrapper ജനറേറ്റ് ചെയ്യുന്നു, താഴെ കാണിച്ചതുപോലെ:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. അതിന് परिणामമായി, നിങ്ങൾ ചുവടെയുള്ള ഫോർമാറ്റിൽ നിങ്ങളുടെ പ്രോംപ്റ്റ് സമർപ്പിക്കാൻ കഴിയും:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. പിന്നെ OpenAI API-സുസ്ഥിതീകരിച്ച പോസ്റ്റ്-പ്രോസസ്സിംഗ് ഉപയോഗിക്കുക, ഉദാഹരണത്തിന് _response[0][‘choices’][0][‘message’][‘content’]_ എന്നിവ, ഔട്ട്പുട്ട് ഇങ്ങനെ സുന്ദരമാക്കാൻ:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. മുകളിൽ Custom Python Wrapper പ്രോജക്റ്റിലെ ഘട്ടം 3-ൽ, കൊടുത്ത ഇൻപുട്ട് ഉദാഹരണത്തിൽ നിന്നാണ് MLFlow പാക്കേജ് മോഡലിന്റെ സിഗ്നേച്ചർ ജനറേറ്റ് ചെയ്യാനനുമതിയുള്ളത്. നമ്മുടെ MLFlow wrapper-ന്റെ സിഗ്നേച്ചർ ഇങ്ങനെ കാണപ്പെടും:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. അതുകൊണ്ട്, നമ്മുടെ പ്രോംപ്റ്റിൽ "prompt" എന്ന ഡിക്ഷനറി കീ ഉണ്ടായിരിക്കണം, ഇതുപോലെ:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. മോഡലിന്റെ ഔട്ട്പുട്ട് പിന്നീട് string ഫോർമാറ്റിൽ നൽകിയേക്കും:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്ക്ലെയിമർ:
ഈ രേഖ AI വിവർത്തനസേവനം Co‑op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ചാണ് വിവർത്തനം ചെയ്യപ്പെട്ടത്. ഞങ്ങൾ ശരിയായി വിവർത്തനം ചെയ്യാൻ努ർവികസിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയംകർമ്മിത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാമെന്നു ശ്രദ്ധിക്കുക. പ്രധാനമായ വിവരങ്ങൾക്കായി മൂല പ്രമാണം അതിൻറെ യഥാഭാഷയിലാണ് ഔദ്യോഗിക ഉറവിടം എന്ന് കരുതേണ്ടതാണ്. നിർണായകമായ കാര്യങ്ങൾക്കായി പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതൊരു തെറ്റിദ്ധാരണയ്ക്കോ തെറ്റായ വ്യാഖ്യാനത്തിനോ നമ്മൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->