<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-07-17T08:26:08+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "br"
}
-->
## Cenários de Fine Tuning

![FineTuning com Serviços MS](../../../../translated_images/FinetuningwithMS.3d0cec8ae693e094.br.png)

**Plataforma** Isso inclui várias tecnologias como Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito e ONNX Runtime.

**Infraestrutura** Isso inclui CPU e FPGA, que são essenciais para o processo de fine-tuning. Deixe-me mostrar os ícones de cada uma dessas tecnologias.

**Ferramentas & Framework** Isso inclui ONNX Runtime e ONNX Runtime. Deixe-me mostrar os ícones de cada uma dessas tecnologias.  
[Inserir ícones para ONNX Runtime e ONNX Runtime]

O processo de fine-tuning com tecnologias Microsoft envolve vários componentes e ferramentas. Ao entender e utilizar essas tecnologias, podemos ajustar nossos aplicativos de forma eficaz e criar soluções melhores.

## Modelo como Serviço

Faça fine-tuning do modelo usando fine-tuning hospedado, sem a necessidade de criar e gerenciar computação.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.3eee4630607aff0d.br.png)

O fine-tuning serverless está disponível para os modelos Phi-3-mini e Phi-3-medium, permitindo que desenvolvedores personalizem rapidamente os modelos para cenários em nuvem e edge sem precisar se preocupar com a computação. Também anunciamos que o Phi-3-small está agora disponível através da nossa oferta Models-as-a-Service, para que os desenvolvedores possam começar rapidamente o desenvolvimento em IA sem precisar gerenciar a infraestrutura subjacente.

## Modelo como Plataforma

Os usuários gerenciam sua própria computação para fazer fine-tuning dos seus modelos.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.fd3829c1122f5d1c.br.png)

[Exemplo de Fine Tuning](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Cenários de Fine Tuning

| | | | | | | |
|-|-|-|-|-|-|-|
|Cenário|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Adaptar LLMs pré-treinados para tarefas ou domínios específicos|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para tarefas de NLP como classificação de texto, reconhecimento de entidades nomeadas e tradução automática|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para tarefas de QA|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para gerar respostas humanizadas em chatbots|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para gerar música, arte ou outras formas de criatividade|Sim|Sim|Sim|Sim|Sim|Sim|
|Redução de custos computacionais e financeiros|Sim|Sim|Não|Sim|Sim|Não|
|Redução do uso de memória|Não|Sim|Não|Sim|Sim|Sim|
|Uso de menos parâmetros para fine-tuning eficiente|Não|Sim|Sim|Não|Não|Sim|
|Forma eficiente de paralelismo de dados que permite acesso à memória agregada de todas as GPUs disponíveis|Não|Não|Não|Sim|Sim|Sim|

## Exemplos de Performance em Fine Tuning

![Performance de Fine Tuning](../../../../translated_images/Finetuningexamples.a9a41214f8f5afc1.br.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.