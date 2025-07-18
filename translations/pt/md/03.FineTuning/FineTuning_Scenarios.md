<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-07-17T08:25:55+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "pt"
}
-->
## Cenários de Fine Tuning

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.3d0cec8ae693e094c38c72575e63f2c9bf1cf980ab90f1388e102709f9c979e5.pt.png)

**Plataforma** Inclui várias tecnologias como Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito e ONNX Runtime.

**Infraestrutura** Inclui a CPU e FPGA, que são essenciais para o processo de fine-tuning. Deixe-me mostrar-lhe os ícones de cada uma destas tecnologias.

**Ferramentas & Framework** Inclui ONNX Runtime e ONNX Runtime. Deixe-me mostrar-lhe os ícones de cada uma destas tecnologias.  
[Inserir ícones para ONNX Runtime e ONNX Runtime]

O processo de fine-tuning com tecnologias Microsoft envolve vários componentes e ferramentas. Ao compreender e utilizar estas tecnologias, podemos ajustar eficazmente as nossas aplicações e criar soluções melhores.

## Modelo como Serviço

Faça fine-tuning do modelo usando fine-tuning hospedado, sem necessidade de criar e gerir computação.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.3eee4630607aff0d0a137b16ab79ec5977ece923cd1fdd89557a2655c632669d.pt.png)

O fine-tuning serverless está disponível para os modelos Phi-3-mini e Phi-3-medium, permitindo aos desenvolvedores personalizar rapidamente e facilmente os modelos para cenários na cloud e na edge, sem terem de providenciar computação. Também anunciámos que o Phi-3-small está agora disponível através da nossa oferta Models-as-a-Service, para que os desenvolvedores possam começar rapidamente e facilmente o desenvolvimento de IA sem terem de gerir a infraestrutura subjacente.

## Modelo como Plataforma

Os utilizadores gerem a sua própria computação para fazer fine-tuning dos seus modelos.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.fd3829c1122f5d1c4a6a91593ebc348548410e162acda34f18034384e3b3816a.pt.png)

[Exemplo de Fine Tuning](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Cenários de Fine Tuning

| | | | | | | |
|-|-|-|-|-|-|-|
|Cenário|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Adaptar LLMs pré-treinados a tarefas ou domínios específicos|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para tarefas de NLP como classificação de texto, reconhecimento de entidades nomeadas e tradução automática|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para tarefas de QA|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para gerar respostas semelhantes às humanas em chatbots|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para gerar música, arte ou outras formas de criatividade|Sim|Sim|Sim|Sim|Sim|Sim|
|Redução de custos computacionais e financeiros|Sim|Sim|Não|Sim|Sim|Não|
|Redução do uso de memória|Não|Sim|Não|Sim|Sim|Sim|
|Uso de menos parâmetros para fine-tuning eficiente|Não|Sim|Sim|Não|Não|Sim|
|Forma eficiente em memória de paralelismo de dados que dá acesso à memória agregada das GPUs disponíveis|Não|Não|Não|Sim|Sim|Sim|

## Exemplos de Performance de Fine Tuning

![Finetuning Performance](../../../../translated_images/Finetuningexamples.a9a41214f8f5afc186adb16a413b1c17e2f43a89933ba95feb5aee84b0b24add.pt.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.