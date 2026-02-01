# Usando GPU Windows para criar solução Prompt flow com Phi-3.5-Instruct ONNX

O documento a seguir é um exemplo de como usar PromptFlow com ONNX (Open Neural Network Exchange) para desenvolver aplicações de IA baseadas nos modelos Phi-3.

PromptFlow é um conjunto de ferramentas de desenvolvimento projetado para simplificar o ciclo completo de desenvolvimento de aplicações de IA baseadas em LLM (Large Language Model), desde a ideação e prototipagem até os testes e avaliação.

Ao integrar PromptFlow com ONNX, os desenvolvedores podem:

- Otimizar o desempenho do modelo: aproveitar o ONNX para inferência e implantação eficiente do modelo.
- Simplificar o desenvolvimento: usar PromptFlow para gerenciar o fluxo de trabalho e automatizar tarefas repetitivas.
- Melhorar a colaboração: facilitar a colaboração entre membros da equipe ao fornecer um ambiente de desenvolvimento unificado.

**Prompt flow** é um conjunto de ferramentas de desenvolvimento projetado para simplificar o ciclo completo de desenvolvimento de aplicações de IA baseadas em LLM, desde ideação, prototipagem, testes, avaliação até implantação em produção e monitoramento. Ele torna a engenharia de prompts muito mais fácil e permite construir aplicações LLM com qualidade de produção.

Prompt flow pode se conectar ao OpenAI, Azure OpenAI Service e modelos personalizáveis (Huggingface, LLM/SLM local). Nosso objetivo é implantar o modelo ONNX quantizado do Phi-3.5 em aplicações locais. O Prompt flow pode nos ajudar a planejar melhor nossos negócios e completar soluções locais baseadas no Phi-3.5. Neste exemplo, combinaremos a Biblioteca ONNX Runtime GenAI para completar a solução Prompt flow baseada em GPU Windows.

## **Instalação**

### **ONNX Runtime GenAI para GPU Windows**

Leia este guia para configurar o ONNX Runtime GenAI para GPU Windows [clique aqui](./ORTWindowGPUGuideline.md)

### **Configurar Prompt flow no VSCode**

1. Instale a extensão Prompt flow para VS Code

![pfvscode](../../../../../../translated_images/pt-BR/pfvscode.eff93dfc66a42cbe.webp)

2. Após instalar a extensão Prompt flow para VS Code, clique na extensão e escolha **Installation dependencies** para seguir o guia e instalar o SDK do Prompt flow no seu ambiente

![pfsetup](../../../../../../translated_images/pt-BR/pfsetup.b46e93096f5a254f.webp)

3. Baixe o [Código de Exemplo](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) e abra este exemplo no VS Code

![pfsample](../../../../../../translated_images/pt-BR/pfsample.8d89e70584ffe7c4.webp)

4. Abra o arquivo **flow.dag.yaml** para escolher seu ambiente Python

![pfdag](../../../../../../translated_images/pt-BR/pfdag.264a77f7366458ff.webp)

   Abra o arquivo **chat_phi3_ort.py** para alterar o local do seu modelo Phi-3.5-instruct ONNX

![pfphi](../../../../../../translated_images/pt-BR/pfphi.72da81d74244b45f.webp)

5. Execute seu prompt flow para testar

Abra o **flow.dag.yaml** e clique no editor visual

![pfv](../../../../../../translated_images/pt-BR/pfv.ba8a81f34b20f603.webp)

Após clicar, execute para testar

![pfflow](../../../../../../translated_images/pt-BR/pfflow.4e1135a089b1ce1b.webp)

1. Você pode executar em lote no terminal para verificar mais resultados


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Você pode conferir os resultados no seu navegador padrão


![pfresult](../../../../../../translated_images/pt-BR/pfresult.c22c826f8062d7cb.webp)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.