<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:56:54+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "br"
}
-->
# **Inferência Phi-3 em Servidor Local**

Podemos implantar o Phi-3 em um servidor local. Os usuários podem escolher as soluções [Ollama](https://ollama.com) ou [LM Studio](https://llamaedge.com), ou podem escrever seu próprio código. Você pode conectar os serviços locais do Phi-3 através do [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) ou do [Langchain](https://www.langchain.com/) para criar aplicações Copilot.

## **Use o Semantic Kernel para acessar o Phi-3-mini**

Na aplicação Copilot, criamos aplicações por meio do Semantic Kernel / LangChain. Esse tipo de framework de aplicação é geralmente compatível com o Azure OpenAI Service / modelos OpenAI, e também pode suportar modelos open source no Hugging Face e modelos locais. O que devemos fazer se quisermos usar o Semantic Kernel para acessar o Phi-3-mini? Usando .NET como exemplo, podemos combiná-lo com o Hugging Face Connector no Semantic Kernel. Por padrão, ele pode corresponder ao id do modelo no Hugging Face (na primeira vez que você usar, o modelo será baixado do Hugging Face, o que pode levar bastante tempo). Você também pode se conectar ao serviço local construído. Comparando os dois, recomendamos usar o último, pois oferece um grau maior de autonomia, especialmente em aplicações empresariais.

![sk](../../../../../translated_images/sk.d03785c25edc6d445a2e9ae037979e544e0b0c482f43c7617b0324e717b9af62.br.png)

Pela figura, acessar serviços locais através do Semantic Kernel pode facilmente conectar ao servidor do modelo Phi-3-mini auto-hospedado. Aqui está o resultado da execução:

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca2020eefcaeaaee184d29bb0cf1c37b00fd9c79acc23a6dc8d2.br.png)

***Código de Exemplo*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.