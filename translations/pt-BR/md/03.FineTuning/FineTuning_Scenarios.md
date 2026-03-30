## Cenários de Fine Tuning

![FineTuning with MS Services](../../../../translated_images/pt-BR/FinetuningwithMS.3d0cec8ae693e094.webp)

Esta seção fornece uma visão geral dos cenários de fine-tuning em ambientes Microsoft Foundry e Azure, incluindo modelos de implantação, camadas de infraestrutura e técnicas de otimização comumente usadas.

**Plataforma**  
Isso inclui serviços gerenciados como Microsoft Foundry (antigo Microsoft Foundry) e Azure Machine Learning, que fornecem gerenciamento de modelos, orquestração, rastreamento de experimentos e fluxos de trabalho de implantação.

**Infraestrutura**  
O fine-tuning requer recursos computacionais escaláveis. Em ambientes Azure, isso normalmente inclui máquinas virtuais baseadas em GPU e recursos de CPU para cargas de trabalho leves, junto com armazenamento escalável para conjuntos de dados e checkpoints.

**Ferramentas e Framework**  
Os fluxos de trabalho de fine-tuning comumente dependem de frameworks e bibliotecas de otimização como Hugging Face Transformers, DeepSpeed e PEFT (Parameter-Efficient Fine-Tuning).

O processo de fine-tuning com tecnologias Microsoft abrange serviços de plataforma, infraestrutura computacional e frameworks de treinamento. Ao entender como esses componentes funcionam juntos, os desenvolvedores podem adaptar de forma eficiente modelos base para tarefas específicas e cenários de produção.

## Modelo como Serviço

Realize o fine-tuning do modelo usando fine-tuning hospedado, sem a necessidade de criar e gerenciar computação.

![MaaS Fine Tuning](../../../../translated_images/pt-BR/MaaSfinetune.3eee4630607aff0d.webp)

O fine-tuning serverless está agora disponível para as famílias de modelos Phi-3, Phi-3.5 e Phi-4, permitindo que os desenvolvedores personalizem os modelos rápida e facilmente para cenários na nuvem e na borda sem precisar providenciar computação.

## Modelo como Plataforma

Os usuários gerenciam sua própria computação para realizar o fine-tuning de seus modelos.

![Maap Fine Tuning](../../../../translated_images/pt-BR/MaaPFinetune.fd3829c1122f5d1c.webp)

[Exemplo de Fine Tuning](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Comparação de Técnicas de Fine-Tuning

|Cenário|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Adaptar LLMs pré-treinados para tarefas ou domínios específicos|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para tarefas de PLN como classificação de texto, reconhecimento de entidades nomeadas e tradução automática|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para tarefas de QA|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para geração de respostas semelhantes a humanas em chatbots|Sim|Sim|Sim|Sim|Sim|Sim|
|Fine-tuning para geração de música, arte ou outras formas de criatividade|Sim|Sim|Sim|Sim|Sim|Sim|
|Redução dos custos computacionais e financeiros|Sim|Sim|Sim|Sim|Sim|Sim|
|Redução do uso de memória|Sim|Sim|Sim|Sim|Sim|Sim|
|Uso de menos parâmetros para fine-tuning eficiente|Sim|Sim|Sim|Não|Não|Sim|
|Forma eficiente em memória de paralelismo de dados que dá acesso à memória agregada da GPU de todos os dispositivos GPU disponíveis|Não|Não|Não|Sim|Sim|Não|

> [!NOTE]
> LoRA, QLoRA, PEFT e DoRA são métodos de fine-tuning eficientes em parâmetros, enquanto DeepSpeed e ZeRO focam em treinamento distribuído e otimização de memória.

## Exemplos de Performance no Fine Tuning

![Finetuning Performance](../../../../translated_images/pt-BR/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->