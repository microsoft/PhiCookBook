<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-03-27T10:53:46+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-MLflow.md",
  "language_code": "ru"
}
-->
# MLflow

[MLflow](https://mlflow.org/) — это платформа с открытым исходным кодом, предназначенная для управления полным жизненным циклом машинного обучения.

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.ru.png)

MLFlow используется для управления жизненным циклом ML, включая эксперименты, воспроизводимость, развертывание и центральный реестр моделей. В настоящее время MLFlow предлагает четыре компонента:

- **MLflow Tracking:** Запись и запрос экспериментов, кода, конфигурации данных и результатов.
- **MLflow Projects:** Упаковка кода для анализа данных в формате, который позволяет воспроизводить запуски на любой платформе.
- **MLflow Models:** Развертывание моделей машинного обучения в различных средах обслуживания.
- **Model Registry:** Хранение, аннотирование и управление моделями в центральном репозитории.

Платформа предоставляет возможности для отслеживания экспериментов, упаковки кода в воспроизводимые запуски, а также для совместного использования и развертывания моделей. MLFlow интегрирован в Databricks и поддерживает множество библиотек машинного обучения, что делает его независимым от конкретной библиотеки. Он может быть использован с любой библиотекой машинного обучения и на любом языке программирования, так как предоставляет REST API и CLI для удобства.

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.ru.png)

Основные функции MLFlow включают:

- **Отслеживание экспериментов:** Запись и сравнение параметров и результатов.
- **Управление моделями:** Развертывание моделей на различных платформах обслуживания и инференса.
- **Реестр моделей:** Совместное управление жизненным циклом моделей MLFlow, включая версионирование и аннотации.
- **Проекты:** Упаковка кода ML для совместного использования или производственного применения.

MLFlow также поддерживает цикл MLOps, который включает подготовку данных, регистрацию и управление моделями, упаковку моделей для выполнения, развертывание сервисов и мониторинг моделей. Его цель — упростить процесс перехода от прототипа к рабочему процессу в производственной среде, особенно в облачных и периферийных вычислениях.

## Сценарий E2E — создание оболочки и использование Phi-3 как модели MLFlow

В этом примере мы покажем два разных подхода к созданию оболочки вокруг небольшой языковой модели Phi-3 (SLM) и ее запуску как модели MLFlow либо локально, либо в облаке, например, в рабочей области Azure Machine Learning.

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.ru.png)

| Проект | Описание | Расположение |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline — это самый простой способ создать оболочку, если вы хотите использовать модель HuggingFace с экспериментальным фрейворком трансформеров MLFlow. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | На момент написания фреймворк трансформеров не поддерживал генерацию оболочки MLFlow для моделей HuggingFace в формате ONNX, даже с экспериментальным пакетом Python Optimum. В таких случаях можно создать собственную оболочку на Python для режима MLFlow. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Проект: Transformer Pipeline

1. Вам понадобятся соответствующие пакеты Python от MLFlow и HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Затем необходимо инициировать конвейер трансформеров, указав целевую модель Phi-3 в реестре HuggingFace. Как видно из карточки модели _Phi-3-mini-4k-instruct_, ее задача — «Генерация текста»:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Теперь вы можете сохранить конвейер трансформеров модели Phi-3 в формате MLFlow и указать дополнительные детали, такие как путь к целевым артефактам, настройки конфигурации модели и тип API для инференса:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Проект: Custom Python Wrapper

1. Здесь мы можем использовать [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) от Microsoft для инференса модели ONNX и кодирования/декодирования токенов. Вам нужно выбрать пакет _onnxruntime_genai_ для вашего целевого вычислительного ресурса, например, для CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

2. Наш пользовательский класс реализует два метода: _load_context()_ для инициализации **модели ONNX** Phi-3 Mini 4K Instruct, **параметров генератора** и **токенизатора**; и _predict()_ для генерации выходных токенов на основе предоставленного запроса:

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

3. Теперь вы можете использовать функцию _mlflow.pyfunc.log_model()_ для создания пользовательской оболочки на Python (в формате pickle) для модели Phi-3 вместе с оригинальной моделью ONNX и необходимыми зависимостями:

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

## Сигнатуры созданных моделей MLFlow

1. В шаге 3 проекта Transformer Pipeline выше мы установили задачу модели MLFlow как «_llm/v1/chat_». Такая инструкция создает API-оболочку модели, совместимую с Chat API от OpenAI, как показано ниже:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

2. В результате вы можете отправить свой запрос в следующем формате:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

3. Затем используйте совместимую с OpenAI API постобработку, например, _response[0][‘choices’][0][‘message’][‘content’]_, чтобы преобразовать ваш результат в следующий вид:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

4. В шаге 3 проекта Custom Python Wrapper выше мы позволяем пакету MLFlow сгенерировать сигнатуру модели на основе предоставленного примера ввода. Сигнатура оболочки MLFlow будет выглядеть следующим образом:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

5. Таким образом, наш запрос должен содержать ключ словаря "prompt", например:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

6. Выходные данные модели будут предоставлены в строковом формате:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке должен считаться авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.