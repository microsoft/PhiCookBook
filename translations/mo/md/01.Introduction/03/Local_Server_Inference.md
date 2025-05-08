<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-05-07T14:30:56+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "mo"
}
-->
# **Inference Phi-3 in Local Server**

We can deploy Phi-3 on a local server. Users can choose [Ollama](https://ollama.com) or [LM Studio](https://llamaedge.com) solutions, or they can write their own code. You can connect Phi-3's local services through [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) or [Langchain](https://www.langchain.com/) to build Copilot applications


## **Use Semantic Kernel to access Phi-3-mini**

In the Copilot application, we create applications through Semantic Kernel / LangChain. This type of application framework is generally compatible with Azure OpenAI Service / OpenAI models, and can also support open source models on Hugging Face and local models. What should we do if we want to use Semantic Kernel to access Phi-3-mini? Using .NET as an example, we can combine it with the Hugging Face Connector in  Semantic Kernel. By default, it can correspond to the model id on Hugging Face (the first time you use it, the model will be downloaded from Hugging Face, which takes a long time). You can also connect to the built local service. Compared with the two, we recommend using the latter because it has a higher degree of autonomy, especially in enterprise applications.

![sk](../../../../../translated_images/sk.d03785c25edc6d445a2e9ae037979e544e0b0c482f43c7617b0324e717b9af62.mo.png)


From the figure accessing local services through Semantic Kernel can easily connect to the self-built Phi-3-mini model server. Here is the running result


![skrun](../../../../../translated_images/skrun.5aafc1e7197dca2020eefcaeaaee184d29bb0cf1c37b00fd9c79acc23a6dc8d2.mo.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Disclaimer**:  
Dis dokumento ha bin tradusí uzando AI traduk-serviso [Co-op Translator](https://github.com/Azure/co-op-translator). Dum nos strebas por precizo, bonvolu konscii ke aŭtomataj tradukoj povas enhavi erarojn aŭ malprecizojn. La originala dokumento en ĝia denaska lingvo devas esti konsiderata la aŭtoritata fonto. Por kritikaj informoj, estas rekomendate profesia homa traduko. Ni ne estas respondeca por ajnaj miskomprenoj aŭ miskomprenoj rezultantaj de la uzo de ĉi tiu traduko.