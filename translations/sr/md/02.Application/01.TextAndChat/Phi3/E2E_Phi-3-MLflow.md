<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:36:28+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "sr"
}
-->
# MLflow

[MLflow](https://mlflow.org/) је платформа отвореног кода дизајнирана за управљање целокупним животним циклусом машинског учења.

![MLFlow](../../../../../../translated_images/sr/MlFlowmlops.ed16f47809d74d9a.png)

MLFlow се користи за управљање ML животним циклусом, укључујући експериментисање, репродуктивност, имплементацију и централни регистар модела. Тренутно MLflow нуди четири компоненте.

- **MLflow Tracking:** Бележење и претраживање експеримената, кода, конфигурације података и резултата.
- **MLflow Projects:** Паковање кода из области науке о подацима у формату који омогућава репродукцију покретања на било којој платформи.
- **Mlflow Models:** Имплементација модела машинског учења у различитим окружењима за сервисирање.
- **Model Registry:** Чување, означавање и управљање моделима у централном репозиторијуму.

Обухвата могућности за праћење експеримената, паковање кода у репродуктивне покрете и дељење и имплементацију модела. MLFlow је интегрисан у Databricks и подржава разне ML библиотеке, што га чини независним од библиотеке. Може се користити са било којом библиотеком машинског учења и у било ком програмском језику, јер пружа REST API и CLI ради лакшег коришћења.

![MLFlow](../../../../../../translated_images/sr/MLflow2.5a22eb718f6311d1.png)

Кључне карактеристике MLFlow укључују:

- **Праћење експеримената:** Бележење и поређење параметара и резултата.
- **Управљање моделима:** Имплементација модела на различите платформе за сервисирање и инференцу.
- **Model Registry:** Заједничко управљање животним циклусом MLflow модела, укључујући верзионисање и означавање.
- **Пројекти:** Паковање ML кода за дељење или производну употребу.

MLFlow такође подржава MLOps циклус, који укључује припрему података, регистрацију и управљање моделима, паковање модела за извршавање, имплементацију сервиса и праћење модела. Циљ је поједноставити процес преласка са прототипа на производни ток рада, посебно у облачним и edge окружењима.

## E2E сценарио - Израда wrapper-а и коришћење Phi-3 као MLFlow модела

У овом E2E примеру показаћемо два различита приступа изради wrapper-а око малог језичког модела Phi-3 (SLM) и затим његово покретање као MLFlow модела било локално или у облаку, нпр. у Azure Machine Learning радном простору.

![MLFlow](../../../../../../translated_images/sr/MlFlow1.fd745e47dbd3fecf.png)

| Пројекат | Опис | Локација |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline је најједноставнија опција за израду wrapper-а ако желите да користите HuggingFace модел са MLFlow експерименталним transformers приступом. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | У тренутку писања, transformer pipeline није подржавао генерисање MLFlow wrapper-а за HuggingFace моделе у ONNX формату, чак ни уз експериментални optimum Python пакет. За овакве случајеве можете направити свој прилагођени Python wrapper за MLFlow модел. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Пројекат: Transformer Pipeline

1. Биће вам потребни релевантни Python пакети из MLFlow и HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Затим треба да иницијализујете transformer pipeline позивајући циљни Phi-3 модел из HuggingFace регистра. Као што се види из модела _Phi-3-mini-4k-instruct_, његов задатак је типа „Text Generation“:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Сада можете сачувати transformer pipeline вашег Phi-3 модела у MLFlow формату и дати додатне детаље као што су циљна путања артефаката, специфична подешавања модела и тип inference API-ја:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Пројекат: Custom Python Wrapper

1. Овде можемо користити Microsoft-ов [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) за inference ONNX модела и кодирање/декодирање токена. Морате изабрати _onnxruntime_genai_ пакет за ваш циљни рачунар, у примеру испод је то CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Наша прилагођена класа имплементира две методе: _load_context()_ за иницијализацију **ONNX модела** Phi-3 Mini 4K Instruct, **параметара генератора** и **tokenizer-а**; и _predict()_ за генерисање излазних токена за дати prompt:

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

1. Сада можете користити функцију _mlflow.pyfunc.log_model()_ за генерисање прилагођеног Python wrapper-а (у pickle формату) за Phi-3 модел, заједно са оригиналним ONNX моделом и потребним зависностима:

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

## Потписи генерисаних MLFlow модела

1. У кораку 3 пројекта Transformer Pipeline горе, задали смо MLFlow моделу задатак „_llm/v1/chat_“. Та инструкција генерише API wrapper модела, компатибилан са OpenAI Chat API-јем као што је приказано испод:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Као резултат, можете послати ваш prompt у следећем формату:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Затим, користите OpenAI API-компатибилну постобраду, нпр. _response[0][‘choices’][0][‘message’][‘content’]_, да уљепшате излаз у нешто овако:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. У кораку 3 пројекта Custom Python Wrapper горе, омогућавамо MLFlow пакету да генерише потпис модела на основу датог примера улаза. Потпис нашег MLFlow wrapper-а ће изгледати овако:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Дакле, наш prompt би требао да садржи кључ речника "prompt", слично овоме:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Излаз модела ће бити дат у облику стринга:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.