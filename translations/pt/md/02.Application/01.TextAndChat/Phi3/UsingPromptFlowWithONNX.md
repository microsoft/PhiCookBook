<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T02:59:38+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "pt"
}
-->
# Utilizar GPU Windows para criar solução Prompt flow com Phi-3.5-Instruct ONNX

O documento seguinte é um exemplo de como usar o PromptFlow com ONNX (Open Neural Network Exchange) para desenvolver aplicações de IA baseadas em modelos Phi-3.

PromptFlow é um conjunto de ferramentas de desenvolvimento concebido para simplificar o ciclo completo de desenvolvimento de aplicações de IA baseadas em LLM (Large Language Model), desde a ideação e prototipagem até aos testes e avaliação.

Ao integrar o PromptFlow com ONNX, os programadores podem:

- Otimizar o desempenho do modelo: tirar partido do ONNX para uma inferência e implementação eficiente do modelo.
- Simplificar o desenvolvimento: usar o PromptFlow para gerir o fluxo de trabalho e automatizar tarefas repetitivas.
- Melhorar a colaboração: facilitar uma melhor colaboração entre os membros da equipa, fornecendo um ambiente de desenvolvimento unificado.

**Prompt flow** é um conjunto de ferramentas de desenvolvimento concebido para simplificar o ciclo completo de desenvolvimento de aplicações de IA baseadas em LLM, desde a ideação, prototipagem, testes, avaliação até à implementação em produção e monitorização. Facilita muito a engenharia de prompts e permite construir aplicações LLM com qualidade de produção.

O Prompt flow pode ligar-se ao OpenAI, Azure OpenAI Service e modelos personalizáveis (Huggingface, LLM/SLM local). Pretendemos implementar o modelo ONNX quantizado do Phi-3.5 em aplicações locais. O Prompt flow pode ajudar-nos a planear melhor o nosso negócio e a completar soluções locais baseadas no Phi-3.5. Neste exemplo, vamos combinar a ONNX Runtime GenAI Library para completar a solução Prompt flow baseada em GPU Windows.

## **Instalação**

### **ONNX Runtime GenAI para GPU Windows**

Leia esta orientação para configurar o ONNX Runtime GenAI para GPU Windows [clicar aqui](./ORTWindowGPUGuideline.md)

### **Configurar Prompt flow no VSCode**

1. Instale a extensão Prompt flow para VS Code

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.pt.png)

2. Após instalar a extensão Prompt flow para VS Code, clique na extensão e escolha **Installation dependencies** seguindo esta orientação para instalar o SDK do Prompt flow no seu ambiente

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.pt.png)

3. Descarregue o [Código de Exemplo](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) e abra este exemplo no VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.pt.png)

4. Abra o ficheiro **flow.dag.yaml** para escolher o seu ambiente Python

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.pt.png)

   Abra o ficheiro **chat_phi3_ort.py** para alterar a localização do seu modelo Phi-3.5-instruct ONNX

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.pt.png)

5. Execute o seu prompt flow para testar

Abra o ficheiro **flow.dag.yaml** e clique no editor visual

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.pt.png)

Depois de clicar, execute para testar

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.pt.png)

1. Pode executar em batch no terminal para verificar mais resultados


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Pode consultar os resultados no seu browser predefinido


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.pt.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.