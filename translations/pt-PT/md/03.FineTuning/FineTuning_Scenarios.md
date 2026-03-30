## Cenários de Ajuste Fino

![FineTuning with MS Services](../../../../translated_images/pt-PT/FinetuningwithMS.3d0cec8ae693e094.webp)

Esta secção fornece uma visão geral dos cenários de ajuste fino nos ambientes Microsoft Foundry e Azure, incluindo modelos de implementação, camadas de infraestrutura e técnicas de otimização comumente usadas.

**Plataforma**  
Isto inclui serviços geridos como Microsoft Foundry (anteriormente Microsoft Foundry) e Azure Machine Learning, que fornecem gestão de modelos, orquestração, acompanhamento de experimentos e fluxos de trabalho de implementação.

**Infraestrutura**  
O ajuste fino requer recursos computacionais escaláveis. Em ambientes Azure, isso tipicamente inclui máquinas virtuais baseadas em GPU e recursos de CPU para cargas de trabalho leves, juntamente com armazenamento escalável para conjuntos de dados e pontos de verificação.

**Ferramentas e Framework**  
Os fluxos de trabalho de ajuste fino normalmente dependem de frameworks e bibliotecas de otimização como Hugging Face Transformers, DeepSpeed, e PEFT (Ajuste Fino Eficiente em Parâmetros).

O processo de ajuste fino com tecnologias Microsoft abrange serviços de plataforma, infraestrutura computacional e frameworks de treino. Compreendendo como estes componentes funcionam em conjunto, os desenvolvedores podem adaptar eficientemente modelos base a tarefas específicas e cenários de produção.

## Modelo como Serviço

Ajuste fino do modelo usando ajuste fino hospedado, sem a necessidade de criar e gerir computação.

![MaaS Fine Tuning](../../../../translated_images/pt-PT/MaaSfinetune.3eee4630607aff0d.webp)

O ajuste fino serverless está agora disponível para as famílias de modelos Phi-3, Phi-3.5 e Phi-4, permitindo aos desenvolvedores personalizar os modelos para cenários na cloud e na edge de forma rápida e fácil, sem necessidade de arranjar recursos computacionais.

## Modelo como Plataforma 

Os utilizadores gerem a sua própria computação para realizar o ajuste fino dos seus modelos.

![Maap Fine Tuning](../../../../translated_images/pt-PT/MaaPFinetune.fd3829c1122f5d1c.webp)

[Exemplo de Ajuste Fino](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Comparação de Técnicas de Ajuste Fino

|Cenário|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Adaptação de LLMs pré-treinados a tarefas ou domínios específicos|Sim|Sim|Sim|Sim|Sim|Sim|
|Ajuste fino para tarefas de PLN como classificação de texto, reconhecimento de entidades nomeadas e tradução automática|Sim|Sim|Sim|Sim|Sim|Sim|
|Ajuste fino para tarefas de Perguntas e Respostas (QA)|Sim|Sim|Sim|Sim|Sim|Sim|
|Ajuste fino para gerar respostas humanas em chatbots|Sim|Sim|Sim|Sim|Sim|Sim|
|Ajuste fino para gerar música, arte ou outras formas de criatividade|Sim|Sim|Sim|Sim|Sim|Sim|
|Redução dos custos computacionais e financeiros|Sim|Sim|Sim|Sim|Sim|Sim|
|Redução do uso de memória|Sim|Sim|Sim|Sim|Sim|Sim|
|Uso de menos parâmetros para ajuste fino eficiente|Sim|Sim|Sim|Não|Não|Sim|
|Forma eficiente de paralelismo de dados em memória que dá acesso à memória agregada de GPU de todos os dispositivos GPU disponíveis|Não|Não|Não|Sim|Sim|Não|

> [!NOTE]
> LoRA, QLoRA, PEFT e DoRA são métodos de ajuste fino eficientes em parâmetros, enquanto DeepSpeed e ZeRO focam-se em treino distribuído e otimização de memória.

## Exemplos de Desempenho de Ajuste Fino

![Finetuning Performance](../../../../translated_images/pt-PT/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->