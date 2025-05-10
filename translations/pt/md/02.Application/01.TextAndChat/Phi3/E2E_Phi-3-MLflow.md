<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-05-09T18:36:15+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "pt"
}
-->
# MLflow

[MLflow](https://mlflow.org/) é uma plataforma open-source projetada para gerenciar o ciclo de vida completo de machine learning.

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.pt.png)

MLFlow é usado para gerenciar o ciclo de vida de ML, incluindo experimentação, reprodutibilidade, deployment e um registro central de modelos. Atualmente, MLflow oferece quatro componentes.

- **MLflow Tracking:** Registrar e consultar experimentos, código, configuração de dados e resultados.
- **MLflow Projects:** Empacotar código de ciência de dados em um formato que permite reproduzir execuções em qualquer plataforma.
- **Mlflow Models:** Fazer deploy de modelos de machine learning em diversos ambientes de serving.
- **Model Registry:** Armazenar, anotar e gerenciar modelos em um repositório central.

Ele inclui funcionalidades para rastrear experimentos, empacotar código em execuções reprodutíveis, além de compartilhar e implantar modelos. MLFlow está integrado ao Databricks e suporta várias bibliotecas de ML, sendo agnóstico quanto à biblioteca. Pode ser usado com qualquer biblioteca de machine learning e em qualquer linguagem de programação, pois oferece uma API REST e CLI para facilitar o uso.

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.pt.png)

Principais recursos do MLFlow incluem:

- **Experiment Tracking:** Registrar e comparar parâmetros e resultados.
- **Model Management:** Implantar modelos em várias plataformas de serving e inferência.
- **Model Registry:** Gerenciar colaborativamente o ciclo de vida dos modelos MLflow, incluindo versionamento e anotações.
- **Projects:** Empacotar código de ML para compartilhamento ou uso em produção.

MLFlow também suporta o ciclo MLOps, que inclui preparar dados, registrar e gerenciar modelos, empacotar modelos para execução, implantar serviços e monitorar modelos. Seu objetivo é simplificar o processo de transição de um protótipo para um fluxo de trabalho em produção, especialmente em ambientes de nuvem e edge.

## Cenário E2E - Construindo um wrapper e usando Phi-3 como um modelo MLFlow

Neste exemplo E2E, vamos demonstrar duas abordagens diferentes para construir um wrapper em torno do modelo de linguagem pequeno Phi-3 (SLM) e executá-lo como um modelo MLFlow, seja localmente ou na nuvem, por exemplo, no workspace do Azure Machine Learning.

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.pt.png)

| Projeto | Descrição | Localização |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline é a opção mais simples para construir um wrapper se você quiser usar um modelo HuggingFace com o sabor experimental transformers do MLFlow. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | No momento da escrita, o transformer pipeline não suportava a geração de wrapper MLFlow para modelos HuggingFace em formato ONNX, mesmo com o pacote experimental optimum Python. Para casos assim, você pode construir seu próprio wrapper Python personalizado para modo MLFlow. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Projeto: Transformer Pipeline

1. Você vai precisar dos pacotes Python relevantes do MLFlow e HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Em seguida, deve iniciar um transformer pipeline referenciando o modelo Phi-3 desejado no registro HuggingFace. Como pode ser visto no card do modelo _Phi-3-mini-4k-instruct_, sua tarefa é do tipo “Text Generation”:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Agora, você pode salvar o pipeline transformer do seu modelo Phi-3 no formato MLFlow e fornecer detalhes adicionais como o caminho dos artefatos, configurações específicas do modelo e tipo de API de inferência:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Projeto: Custom Python Wrapper

1. Podemos usar aqui a [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) da Microsoft para a inferência do modelo ONNX e codificação/decodificação de tokens. Você deve escolher o pacote _onnxruntime_genai_ para seu ambiente de execução, no exemplo abaixo voltado para CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Nossa classe customizada implementa dois métodos: _load_context()_ para inicializar o **modelo ONNX** do Phi-3 Mini 4K Instruct, os **parâmetros do gerador** e o **tokenizer**; e _predict()_ para gerar tokens de saída para o prompt fornecido:

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

1. Agora você pode usar a função _mlflow.pyfunc.log_model()_ para gerar um wrapper Python personalizado (em formato pickle) para o modelo Phi-3, junto com o modelo ONNX original e as dependências necessárias:

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

## Assinaturas dos modelos MLFlow gerados

1. No passo 3 do projeto Transformer Pipeline acima, definimos a tarefa do modelo MLFlow como “_llm/v1/chat_”. Essa instrução gera um wrapper de API do modelo, compatível com a API de chat da OpenAI, conforme mostrado abaixo:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Como resultado, você pode enviar seu prompt no seguinte formato:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Depois, use o pós-processamento compatível com a API OpenAI, por exemplo, _response[0][‘choices’][0][‘message’][‘content’]_, para deixar sua saída mais legível, algo assim:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. No passo 3 do projeto Custom Python Wrapper acima, permitimos que o pacote MLFlow gere a assinatura do modelo a partir de um exemplo de entrada fornecido. A assinatura do nosso wrapper MLFlow ficará assim:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Portanto, nosso prompt precisará conter a chave do dicionário "prompt", parecido com isto:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. A saída do modelo será então fornecida em formato string:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.