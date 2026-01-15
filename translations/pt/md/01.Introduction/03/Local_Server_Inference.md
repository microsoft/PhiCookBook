<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:56:48+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "pt"
}
-->
# **Inferência Phi-3 em Servidor Local**

Podemos implementar o Phi-3 num servidor local. Os utilizadores podem escolher as soluções [Ollama](https://ollama.com) ou [LM Studio](https://llamaedge.com), ou podem escrever o seu próprio código. É possível ligar os serviços locais do Phi-3 através do [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) ou do [Langchain](https://www.langchain.com/) para criar aplicações Copilot.

## **Usar Semantic Kernel para aceder ao Phi-3-mini**

Na aplicação Copilot, criamos aplicações através do Semantic Kernel / LangChain. Este tipo de framework de aplicação é geralmente compatível com o Azure OpenAI Service / modelos OpenAI, e também pode suportar modelos open source no Hugging Face e modelos locais. O que devemos fazer se quisermos usar o Semantic Kernel para aceder ao Phi-3-mini? Usando .NET como exemplo, podemos combiná-lo com o Hugging Face Connector no Semantic Kernel. Por defeito, ele corresponde ao id do modelo no Hugging Face (na primeira vez que o usar, o modelo será descarregado do Hugging Face, o que demora algum tempo). Também pode ligar-se ao serviço local construído. Comparando os dois, recomendamos usar o último porque oferece um maior grau de autonomia, especialmente em aplicações empresariais.

![sk](../../../../../translated_images/pt/sk.d03785c25edc6d44.webp)

A partir da figura, aceder a serviços locais através do Semantic Kernel permite ligar facilmente ao servidor do modelo Phi-3-mini construído por si. Aqui está o resultado da execução:

![skrun](../../../../../translated_images/pt/skrun.5aafc1e7197dca20.webp)

***Código de Exemplo*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.