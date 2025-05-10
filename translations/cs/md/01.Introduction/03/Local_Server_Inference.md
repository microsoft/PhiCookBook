<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-05-09T12:08:28+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "cs"
}
-->
# **Inference Phi-3 in Local Server**

We can deploy Phi-3 on a local server. Users can choose [Ollama](https://ollama.com) or [LM Studio](https://llamaedge.com) solutions, or they can write their own code. You can connect Phi-3's local services through [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) or [Langchain](https://www.langchain.com/) to build Copilot applications


## **Use Semantic Kernel to access Phi-3-mini**

In the Copilot application, we create applications through Semantic Kernel / LangChain. This type of application framework is generally compatible with Azure OpenAI Service / OpenAI models, and can also support open source models on Hugging Face and local models. What should we do if we want to use Semantic Kernel to access Phi-3-mini? Using .NET as an example, we can combine it with the Hugging Face Connector in  Semantic Kernel. By default, it can correspond to the model id on Hugging Face (the first time you use it, the model will be downloaded from Hugging Face, which takes a long time). You can also connect to the built local service. Compared with the two, we recommend using the latter because it has a higher degree of autonomy, especially in enterprise applications.

![sk](../../../../../translated_images/sk.c244b32f4811c6f0938b9e95b0b2f4b28105bff6495bdc3b24cd42b3e3e89bb9.cs.png)


From the figure accessing local services through Semantic Kernel can easily connect to the self-built Phi-3-mini model server. Here is the running result


![skrun](../../../../../translated_images/skrun.fb7a635a22ae8b7919d6e15c0eb27262526ed69728c5a1d2773a97d4562657c7.cs.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.