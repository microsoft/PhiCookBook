<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-05-09T21:54:54+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "br"
}
-->
## Szenarios de Fine Tuning

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.25759a0154a97ad90e43a6cace37d6bea87f0ac0236ada3ad5d4a1fbacc3bdf7.br.png)

**Plataforma** Isso inclui várias tecnologias como Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito e ONNX Runtime.

**Infraestrutura** Isso inclui CPU e FPGA, que são essenciais para o processo de fine-tuning. Vou mostrar os ícones de cada uma dessas tecnologias.

**Ferramentas & Framework** Isso inclui ONNX Runtime e ONNX Runtime. Vou mostrar os ícones de cada uma dessas tecnologias.  
[Insert icons for ONNX Runtime and ONNX Runtime]

O processo de fine-tuning com tecnologias Microsoft envolve vários componentes e ferramentas. Ao entender e utilizar essas tecnologias, podemos ajustar nossos aplicativos de forma eficaz e criar soluções melhores.

## Model as Service

Ajuste fino do modelo usando fine-tuning hospedado, sem a necessidade de criar e gerenciar computação.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.6184d80a336ea9d7bb67a581e9e5d0b021cafdffff7ba257c2012e2123e0d77e.br.png)

O fine-tuning serverless está disponível para os modelos Phi-3-mini e Phi-3-medium, permitindo que desenvolvedores personalizem rapidamente os modelos para cenários de nuvem e edge sem precisar se preocupar com a computação. Também anunciamos que o Phi-3-small agora está disponível através da oferta Models-as-a-Service, para que os desenvolvedores possam começar rapidamente com o desenvolvimento de IA sem precisar gerenciar a infraestrutura subjacente.

## Model as a Platform

Os usuários gerenciam sua própria computação para fazer o fine-tuning de seus modelos.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.cf8b08ef05bf57f362da90834be87562502f4370de4a7325a9fb03b8c008e5e7.br.png)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Fine Tuning Scenarios

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Adaptar LLMs pré-treinados para tarefas ou domínios específicos|Yes|Yes|Yes|Yes|Yes|Yes|
|Fine-tuning para tarefas de NLP como classificação de texto, reconhecimento de entidades nomeadas e tradução automática|Yes|Yes|Yes|Yes|Yes|Yes|
|Fine-tuning para tarefas de QA|Yes|Yes|Yes|Yes|Yes|Yes|
|Fine-tuning para gerar respostas humanizadas em chatbots|Yes|Yes|Yes|Yes|Yes|Yes|
|Fine-tuning para gerar música, arte ou outras formas de criatividade|Yes|Yes|Yes|Yes|Yes|Yes|
|Redução de custos computacionais e financeiros|Yes|Yes|No|Yes|Yes|No|
|Redução do uso de memória|No|Yes|No|Yes|Yes|Yes|
|Uso de menos parâmetros para fine-tuning eficiente|No|Yes|Yes|No|No|Yes|
|Forma eficiente em memória de paralelismo de dados que dá acesso à memória agregada de todas as GPUs disponíveis|No|No|No|Yes|Yes|Yes|

## Exemplos de Performance de Fine Tuning

![Finetuning Performance](../../../../translated_images/Finetuningexamples.9dbf84557eef43e011eb7cadf51f51686f9245f7953e2712a27095ab7d18a6d1.br.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.